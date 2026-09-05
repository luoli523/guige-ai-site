# Bot 更新指南

这份文档是**给 bot 读的操作规范**，也可以整段塞进 bot 的 system prompt。
人看的格式说明在 [README](../README.md#内容契约bot-的输出规范)。

---

## 任务

每天产出一篇当日 AI 行业要闻汇总，提交到本仓库。push 到 `main` 后 GitHub Actions 自动构建部署，
几分钟内出现在 <https://luoli523.github.io/guige-ai-site/>。

**一天一篇，一篇一个文件**：`content/daily/YYYY-MM-DD.md`。

---

## 每日流程

```
采集 → 筛选 → 组装 JSON → 调 scripts/new_brief.py → 按退出码决定下一步
```

**不要自己拼 Markdown 或 YAML front matter。** 产出 JSON，交给脚本渲染——
它会校验字段、转义引号、算好时区、跑一次 Hugo 构建确认不会把站点弄挂，再提交。

```bash
cd /path/to/guige-ai-site
git pull --ff-only origin main          # 先同步，避免 push 被拒
echo "$BRIEF_JSON" | python3 scripts/new_brief.py --commit --push
```

调试时先用 `--check`，只校验并打印渲染结果，不写文件、不提交：

```bash
echo "$BRIEF_JSON" | python3 scripts/new_brief.py --check
```

---

## 输入格式

```json
{
  "date": "2026-09-06",
  "summary": "一句话概括今天最重要的事，会显示在首页卡片上",
  "tags": ["Anthropic", "开源模型", "融资"],
  "sources": ["x.com", "techcrunch"],
  "intro": "可选。放在正文最前面的一段话，通常不用。",
  "sections": [
    {
      "heading": "模型与产品",
      "items": [
        {
          "title": "条目标题",
          "body": "一到两句说清发生了什么、为什么值得注意。",
          "url": "https://example.com/原文链接"
        }
      ]
    },
    { "heading": "公司与资本", "items": [] },
    { "heading": "技术与论文", "items": [] },
    { "heading": "政策与生态", "items": [] }
  ]
}
```

| 字段 | 必填 | 说明 |
|---|---|---|
| `date` | 否 | `YYYY-MM-DD`。省略则用**北京时间**今天。不能是未来日期 |
| `title` | 否 | 省略则自动生成 `YYYY-MM-DD AI 要闻`，建议省略 |
| `summary` | 建议 | 首页卡片摘要。省略则模板自动截取正文前 120 字，效果差很多 |
| `tags` | 建议 | 涉及的公司/主题，最多 8 个，自动去重。用于将来检索 |
| `sources` | 否 | 今天信息来自哪些渠道，显示在文章头部 |
| `sections[].heading` | 是 | 分类小标题。空 `items` 的小节会被自动丢弃，不必删 |
| `items[].title` | 是 | 条目标题，会加粗 |
| `items[].body` | 是 | 正文，一到两句 |
| `items[].url` | 建议 | 原文链接，必须 `http://` 或 `https://` 开头 |

---

## 筛选标准

一天只留真正有信息量的几条。判断依据：

- **有实质变化** —— 发布了、开放了、涨价了、停服了；而不是"某某表示""据传"
- **可验证** —— 有官方公告、有论文、有代码；而不是二手转述
- **对做事的人有用** —— 影响到实际的技术选型、成本或可用性
- **不重复** —— 同一件事只记一次；后续进展合并进原条目的描述，不新开一条

宁缺毋滥。**5 到 12 条是健康区间**，超过 15 条通常意味着筛得不够狠。

---

## 写作规范

- `body` 一到两句话，说清「发生了什么 + 为什么值得注意」，不要复述标题
- 用具体数字：参数量、上下文长度、价格、轮次金额、benchmark 分数
- 中文为主；模型名、公司名、专有名词保留原文（`Claude Opus 4.5` 不要写成「克劳德」）
- 中英文之间留空格
- **不确定的信息不要写。** 宁可少一条，也不要编造日期、金额或未经证实的传闻

---

## 硬规则

1. **不发空简报。** 采集不到东西就今天不发。脚本在总条数少于 2 时会直接拒绝（退出码 1），这是保护而不是障碍
2. **时区是 Asia/Shanghai。** 别自己算 UTC 偏移，`date` 只给 `YYYY-MM-DD`，脚本会补 `T08:00:00+08:00`
3. **幂等。** 当天文件已存在时脚本拒绝写入（退出码 2）。确实要重发才加 `--force`，正常重跑应当直接跳过
4. **push 前先 `git pull --ff-only origin main`**，否则会被远端拒绝
5. **不要碰 `content/daily/` 以外的任何文件**

---

## 退出码

| 码 | 含义 | 该怎么办 |
|---|---|---|
| 0 | 成功 | 结束 |
| 1 | 输入或校验失败 | 读 stderr 的具体报错，修正 JSON 后重试。**最多重试 2 次**，仍失败则告警 |
| 2 | 当天简报已存在 | 正常情况直接结束（说明今天已经跑过）。确实要覆盖才加 `--force` |
| 3 | Hugo 构建失败 | 内容已自动回滚。说明产出有问题（多半是 Markdown 里有异常字符），告警 |
| 4 | git 操作失败 | **内容已落盘但没提交**，需要人工介入。立即告警 |

---

## 环境准备

```bash
git clone https://github.com/luoli523/guige-ai-site.git
cd guige-ai-site
git config user.name  "guige-bot"
git config user.email "bot@users.noreply.github.com"
```

推送需要写权限，二选一：

- **Deploy key**（推荐）：仓库 Settings → Deploy keys，勾 *Allow write access*，用 SSH remote
- **PAT**：细粒度 token 只授权本仓库的 Contents: Read and write，remote 用
  `https://<TOKEN>@github.com/luoli523/guige-ai-site.git`

Hugo 不是必需的——没装就跳过构建校验，但**强烈建议装上**，它能在提交前拦住会让站点构建失败的内容。

---

## 告警

以下情况需要通知到人：

- 退出码 3 或 4
- 退出码 1 连续重试 2 次仍失败
- 连续 2 天没有成功产出

---

## 完整示例

```bash
cat <<'JSON' | python3 scripts/new_brief.py --commit --push
{
  "summary": "某厂商开源了新一代基座模型，权重与训练细节一并公开。",
  "tags": ["开源模型", "基座模型"],
  "sources": ["x.com", "arxiv"],
  "sections": [
    {
      "heading": "模型与产品",
      "items": [
        {
          "title": "XX 开源 70B 基座模型",
          "body": "Apache 2.0 许可，公开了完整训练配方与数据配比，MMLU 82.3，可商用。",
          "url": "https://example.com/announcement"
        },
        {
          "title": "YY 推理 API 降价 40%",
          "body": "输入 $0.5/M tokens，输出 $1.5/M，即日生效，长上下文档位同步下调。",
          "url": "https://example.com/pricing"
        }
      ]
    }
  ]
}
JSON
```
