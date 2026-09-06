# Bot 更新指南（深读报告 · 唯一标准）

这份文档是**给 bot / AI学习总管读的操作规范**，也可整段塞进 system prompt。  
**本仓库只保留这一套报告标准**：与每日深度 HTML/PDF 同源同密度；站点 Markdown 为规范正文，HTML/PDF 由同一正文导出（可选）。

人看的站点说明见 [README](../README.md)。

---

## 任务

每天产出**一篇当日 AI 行业/技术深读报告**，提交到本仓库。push 到 `main` 后 GitHub Actions 自动构建部署，几分钟内出现在站点每日页。

**一天一篇，一篇一个文件**：`content/daily/YYYY-MM-DD.md`。

报告必须达到「深读」密度，而不是 5–12 条一句话新闻卡片。短讯式简报**不符合本契约**，脚本会拒绝。

---


## 信源（每日必采，交叉核实）

不要只依赖 X。每日候选至少覆盖：

1. **X.com** — Following + 公开 AI 技术/产品讨论  
2. **GitHub** — 重要 Release、热仓、关键 org 新仓/大更新  
3. **Hugging Face** — Trending 模型/数据集、官方 org 新模型卡  
4. **官方 Blog / 研究页** — OpenAI、Anthropic、Google DeepMind、Meta AI、Microsoft Research  
5. **arXiv** — cs.AI / cs.CL / cs.LG 高热或大厂挂名预印本（宁缺毋滥）

`sources` 字段如实列出当天实际用到的渠道短名（如 `github.com`、`huggingface.co`、`arxiv.org`）。同一事件多源合并；二手传闻标 **待核** 或丢弃。

## 报告结构（强制）

正文使用 Markdown，至少包含以下一级/二级结构（标题文字可微调，但语义必须齐全）：

1. **执行摘要** — 3–8 句：今日主线、为何重要、对工程/学习的即时含义  
2. **主线深度解析** — **2–4 条主线**；每条建议包含：  
   - 背景  
   - 机制 / 能力边界（能讲清就讲）  
   - 证据（链接 + 数字；标注 **FACT** / **官方自报** / **待核**）  
   - 工程或学习启示  
   - 开放问题（可选）  
3. **次要动态** — 值得扫一眼但不展开成长文的条目  
4. **来源与延伸阅读** — 官方页、论文、评测、可靠媒体；链接齐全  
5. **今日行动建议** — 3–7 条可执行下一步（读哪篇、试哪 API、记哪条风险）

允许使用表格、时间线列表、对照表。中文为主；模型名/公司名/专有名词保留原文。

### 证据标注（强制）

| 标签 | 含义 |
|---|---|
| **FACT** | 可用官方文档、可核验源或研究者一作交叉确认 |
| **官方自报** | 厂商评测/宣传数字，引用时必须标明 |
| **待核** | 二手、未独立核验、或厂商联名演示缺原始帖 | 

规则：

- **不确定的信息不要写成确定事实。** 宁可标 **待核** 或删掉。  
- 不要编造日期、金额、benchmark、用户量。  
- 「据传 / 某某表示」若无链接与可验证变化，默认不写。

---

## 每日流程

```
采集 → 筛选 → 深读撰写 → 组装 JSON → scripts/new_brief.py → 按退出码决定下一步
```

**不要手写 front matter。** 产出 JSON，交给脚本渲染与校验。

```bash
cd /path/to/guige-ai-site
git pull --ff-only origin main
echo "$BRIEF_JSON" | python3 scripts/new_brief.py --commit --push
```

调试：

```bash
echo "$BRIEF_JSON" | python3 scripts/new_brief.py --check
```

覆盖当天已存在文件时加 `--force`（正常幂等应跳过）。

---

## 输入格式（JSON）

```json
{
  "date": "2026-09-06",
  "title": "可选；默认「YYYY-MM-DD AI 深读」",
  "summary": "一句话首页卡片摘要（必填，建议 ≤80 字）",
  "tags": ["OpenAI", "安全对齐", "Astra", "MCP"],
  "sources": ["x.com", "openai.com", "collusion.wiki"],
  "body_markdown": "## 执行摘要\\n\\n……\\n\\n## 主线 1 ……\\n\\n## 次要动态\\n\\n## 来源与延伸阅读\\n\\n## 今日行动建议\\n\\n……"
}
```

| 字段 | 必填 | 说明 |
|---|---|---|
| `date` | 否 | `YYYY-MM-DD`。省略则用 **Asia/Shanghai** 今天。不可过远未来 |
| `title` | 否 | 默认 `YYYY-MM-DD AI 深读` |
| `summary` | **是** | 首页卡片摘要；不可空 |
| `tags` | 建议 | ≤8，去重；公司/主题 |
| `sources` | 建议 | 信源渠道短名 |
| `body_markdown` | **是** | 完整深读 Markdown（**不含** YAML front matter） |

### 深度校验（脚本强制）

- `summary` 非空  
- `body_markdown` 去掉空白后长度 ≥ **2500** 字符  
- 正文需能匹配到这些语义标题（子串即可）：`执行摘要`、`主线`（或 `深度解析`）、`来源`、`行动`  
- 旧版短讯 schema（仅有 `sections[].items` 且无 `body_markdown`）→ **拒绝**，提示改用深读格式  

---

## 与 HTML / PDF

- **站点 Markdown = 规范正文（canonical）**  
- 给用户的 HTML/PDF 应从同一 `body_markdown`（或同一结构化草稿）导出，章节与证据标签保持一致  
- 禁止再维护「短站上简报 + 另一套深读 HTML」两套互相矛盾的叙事  

---

## 硬规则

1. **不发空报告。** 深读不够格（长度/结构不达标）当天不发。  
2. **时区 Asia/Shanghai。** `date` 只给 `YYYY-MM-DD`，脚本补 `T08:00:00+08:00`。  
3. **幂等。** 当天文件已存在 → 退出码 2；覆盖需 `--force`。  
4. **push 前先 `git pull --ff-only origin main`。**  
5. **不要碰 `content/daily/` 以外的文件**（改主题/布局另开 PR）。  

---

## 退出码

| 码 | 含义 | 该怎么办 |
|---|---|---|
| 0 | 成功 | 结束；把站点 URL 回传用户 |
| 1 | 输入或校验失败 | 读 stderr，修正 JSON，最多重试 2 次 |
| 2 | 当天报告已存在 | 正常结束；确需覆盖加 `--force` |
| 3 | Hugo 构建失败 | 已回滚；告警 |
| 4 | git 失败 | 内容可能已落盘；立即告警 |

---

## 环境准备

```bash
git clone https://github.com/luoli523/guige-ai-site.git
cd guige-ai-site
git config user.name  "guige-bot"
git config user.email "bot@users.noreply.github.com"
```

写权限：Deploy key（Allow write）或 Contents R/W PAT。  
强烈建议安装 **Hugo extended 0.159.1**，提交前构建校验。

---

## 告警

- 退出码 3 或 4  
- 退出码 1 连续重试 2 次仍失败  
- 连续 2 天没有成功产出  

---

## 最小示例（结构示意；真实发布应更长）

见仓库 `docs/examples/deep-brief.example.json`。真实 `body_markdown` 必须满足深度下限。
