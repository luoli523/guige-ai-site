# Bot 更新指南（深读报告 · 唯一标准）

这份文档是**给 bot / AI学习总管读的操作规范**，也可整段塞进 system prompt。  
**本仓库只保留这一套报告标准**：与每日深度 HTML/PDF 同源同密度；站点 Markdown 为规范正文，HTML/PDF 由同一正文导出（可选）。

人看的站点说明见 [README](../README.md)。

---

## 渲染契约（不可改动）

**这份文档的其余部分你可以自己迭代**——选题标准、报告结构、写作规范，觉得哪里不好就改。
**唯独下面四条不要动，也不要在正文里违反。** 它们不是编辑口味，是站点模板的硬约束，
改了会让页面渲染坏掉：

1. **正文从 `##` 开始，不写 `#` 一级标题。**
   页面标题由 front matter 的 `title` 渲染成唯一的 H1，正文再写一个会变成一页两个 H1。
   （模板有 render hook 会把正文 H1 强制降级为 H2 兜底，但别依赖它。）
2. **不要手写目录。** 站点对超过 800 字的文章自动生成带锚点的目录。
   手写的那份既点不动、又会和自动目录并排重复。
3. **时区一律写 `Asia/Singapore`。** 不写 `Asia/Shanghai` 或其他等价写法。
   `date` 字段只给 `YYYY-MM-DD`，`T08:00:00+08:00` 由脚本补。
4. **文件路径固定 `content/daily/YYYY-MM-DD.md`，一天一篇。**
   路径和命名规则改动会同时破坏 URL、归档分组和首页排序。

要改这四条，先改站点模板（`layouts/`、`assets/css/`）并本地 `hugo --minify` 验证通过，
两边一起改。只改这份文档不会让模板跟着变。

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




## 队友派单（系统级 · 强制）

AI学习总管协调本站日报时，下列专才**只能真派、不能扮演**：

| 角色 | 真实 id | 职责 |
|---|---|---|
| X小宝 | `a1f784b9-b21c-4016-ad27-b995d2c7f2fb` | X Following / 公开 AI 帖 |
| Github研究小宝 | `8665fd5d-55fa-469a-bd41-a67f6c325098` | GitHub Release / 热仓 / 关键 org |
| huggingface小宝 | `ad9e51e2-5f91-4ff0-ba70-347ebb01c69d` | HF Trending / org 模型卡 |
| 研小宝 | `44d7deda-5d7d-40ae-a3cc-093c72597897` | 官博 / arXiv |
| V小宝 | `e13739b1-0541-48e2-8928-21f3ea8fd275` | 本站每日 hero 配图 |

**违规形态（2026-09-07 已发生，禁止再现）：** 用 Task 开子代理写「You are Xxx-style / acting as V小宝」在同一次 routine 里顶替真队友；配图工具不可用时用 Pillow 假图交差。

**正确形态：** `SendToAgent` → 等 `[agent]` 回传 → 总管汇总 → 一次推送、一次通知用户。

## 每日配图（V小宝）

正文定稿后、**单次** `new_brief.py` 推送之前，由 **AI学习总管** 根据当天内容自行选择合适的 **guige-*** skill 与风格/布局，再派 **V小宝** 出图，并挂到当日页。

### 选型（仅限：总管为「本站每日深读 hero」派 V小宝时）
这条概率规则**只约束 AI学习总管派本站日报配图**，不是 V小宝接任何生图单的通用规则；其他用途的图由各自任务说明决定。
**约 50% 概率使用 `guige-infographic`**（layout/style 仍可自选，如 dense-modules、guige-journal 等）；其余约 50% 再按主线题材选其他技能，例如：
- 概念梳理、手绘知识卡 → `guige-hand-write-pic`
- 架构/流程/对照表 → `guige-svg`
- 产品/结构拆解 → `guige-disassembly-diagram`
- 需要多页讲解 → `guige-slides`（取关键一页作 hero，或另约定）
派给 V小宝时写清：**用哪个 skill、layout/style/aspect/lang、要强调的 3–7 个要点**。不要每天锁死同一种非 infographic 默认。

### 产出约定
- 文件落盘：**`assets/img/daily/YYYY-MM-DD-infographic.png`**（注意是 `assets/` 不是 `static/`）
  - 放在 `assets/` 下，Hugo 构建时会自动转 WebP（约为 PNG 的 12%：2.1MB → 0.26MB）并写入真实宽高，
    避免图片压垮页面、也避免加载时跳版。落在 `static/` 只会原样输出 PNG
  - 文件名沿用；内容可以是信息图/手绘/SVG 导出 PNG 等
- front matter（由 JSON 传入 `new_brief.py`）：
  - `hero: "img/daily/YYYY-MM-DD-infographic.png"`
  - `hero_alt: "……"`（简短中文说明）
- 模板在标题/摘要/标签下方自动渲染 hero（读者点击可看大图），**不要**在正文里再手写一遍同图，也**不要**手写目录

### 总管流程（与四路信源一样：齐了再发）
1. 四路信源齐 → 写深读 JSON（尚可不含 hero）
2. 总管选题型与风格 → **`SendToAgent` 真·V小宝**出图（禁止扮演）；**等图到位**；禁止 Pillow 假图
3. 把 png 拷进 `assets/img/daily/`，JSON 补上 `hero` / `hero_alt`
4. `git pull` → `new_brief.py --commit --push`（或 `--force`）**只推一次**
5. 对用户只通知 daily 链接一次

缺图时：可先不上 hero（字段省略），但默认目标是「每天有图」。勿边到边刷。


## 报告结构（强制）

先满足[渲染契约](#渲染契约不可改动)的四条，再按下面组织内容。

正文使用 Markdown。**按信源分板块组装**——把四宝材料写厚写全，不要再压成「2–4 条主线深挖」那种固定叙事。标题文字可微调，但**语义板块必须齐全**。

> **密度硬约束（2026-09-07 事故复盘）：** 四板块是**重分配**不是**压缩**。当日四宝原文应尽量进入对应板块（重点/次要都要有条目与链接）；禁止为了「版面干净」把 12k 级素材砍成 5k 短讯。深读正文去空白后宜与近期合格日（如 9/4、9/6 ≈1.1万+）同量级；脚本下限 2500 只是拒短讯底线，**不是目标长度**。


### 对外正文隐私（强制）

站点日报是公开页。正文、summary、hero_alt、标签里**禁止**出现：

1. 用户的 **X / 社交账号 handle**（含 `@…`、登录态说明）
2. 内部 **bot / 队友名称**（如各「小宝」）及派单痕迹

信源署名用公开渠道名（OpenAI News、GitHub Trending、Hugging Face、X Following 等），不要写「××小宝采集」。


### 1. 今日导读（文首，强制）

- 约 **100 字量级**（可略多，但不要长文）
- **按重点 list 呈现**（建议 3–7 条短 bullet），不要一整段难扫的长段落
- 每一点尽量**直达终点**：用读者最关心的词（发了什么 / 谁表态 / 数字或门槛是什么 / 对工程意味着什么）
- 可另起一行极短「为何今天值得看」——仍保持列表优先

建议标题：`## 今日导读`

### 2. 四大内容板块（强制 · 顺序固定）

每一大板块内部都拆成：

- **重点关注** — 当日最该展开的条目（可多条；有一手链接与 FACT/官方自报/待核）
- **次要动态** — 值得扫一眼但不展开成长文的条目；本窗无料可写「本窗无高信号」

| 顺序 | 板块标题（建议） | 主要材料来自 | 写什么 |
|---|---|---|---|
| 1 | `## 权威行业动态` | **研小宝** | AI 大厂官博/研究页、官方技术与安全更新、高信号预印本（宁缺毋滥） |
| 2 | `## 热门 AI 开源项目跟踪` | **Github研究小宝** | Release、热仓、关键 org 动态 |
| 3 | `## 业界模型相关动态` | **huggingface小宝** | Trending / 新模型卡 / 量化与数据集等；区分「窗口内更新」与「仅热度」 |
| 4 | `## AI 大V 观点与业界热门实践` | **X小宝** | Following + 公开高信号实践/观点；演示完整度标待核 |

板块内允许表格、时间线、对照表。中文为主；模型名/公司名/专有名词保留原文。

### 3. 学习与行动建议（文末，强制）

- 面向 **AI 研究学习** 与 **开发从业者**
- 3–10 条可执行下一步（读哪篇、试哪 API/仓、记哪条风险、怎么复现）
- 建议标题：`## 学习与行动建议`

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
- 四宝素材应**尽量保留信息密度**进入对应板块；总管做交叉核实与去重，而不是为了「好看」砍成三条主线。

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
  "body_markdown": "## 今日导读\\n\\n- ……\\n\\n## 权威行业动态\\n\\n### 重点关注\\n\\n……\\n\\n### 次要动态\\n\\n……\\n\\n## 热门 AI 开源项目跟踪\\n\\n……\\n\\n## 业界模型相关动态\\n\\n……\\n\\n## AI 大V 观点与业界热门实践\\n\\n……\\n\\n## 学习与行动建议\\n\\n……"
}
```

| 字段 | 必填 | 说明 |
|---|---|---|
| `date` | 否 | `YYYY-MM-DD`。省略则用 **Asia/Singapore** 今天。不可过远未来 |
| `title` | 否 | 默认 `YYYY-MM-DD AI 深读` |
| `summary` | **是** | 首页卡片用一句摘要；正文另有「今日导读」列表。|
| `tags` | 建议 | ≤8，去重；公司/主题 |
| `sources` | 建议 | 信源渠道短名 |
| `body_markdown` | **是** | 完整深读 Markdown（**不含** YAML front matter） |

### 深度校验（脚本强制）

- `summary` 非空  
- `body_markdown` 去掉空白后长度 ≥ **2500** 字符  
- 正文需能匹配到这些语义标题（子串即可）：`今日导读`（或 `导读`）、`权威行业动态`、`开源项目`（或 `GitHub`/`Github`）、`模型相关`（或 `Hugging Face`/`HuggingFace`/`业界模型`）、`大V`（或 `热门实践`/`X`）、`行动建议`（或 `学习与行动`）  
- 旧版短讯 schema（仅有 `sections[].items` 且无 `body_markdown`）→ **拒绝**，提示改用深读格式  

---

## 与 HTML / PDF

- **站点 Markdown = 规范正文（canonical）**  
- 给用户的 HTML/PDF 应从同一 `body_markdown`（或同一结构化草稿）导出，章节与证据标签保持一致  
- 禁止再维护「短站上简报 + 另一套深读 HTML」两套互相矛盾的叙事  

---

## 硬规则

1. **不发空报告。** 深读不够格（长度/结构不达标）当天不发。  
2. **时区 Asia/Singapore。** `date` 只给 `YYYY-MM-DD`，脚本补 `T08:00:00+08:00`。  
3. **幂等。** 当天文件已存在 → 退出码 2；覆盖需 `--force`。  
4. **push 前先 `git pull --ff-only origin main`。**  
5. **可以改模板与样式**（`layouts/`、`assets/css/`），但改完必须本地 `hugo --minify` 构建通过才提交；
   构建挂了就回滚，不要把坏掉的站推上线。`docs/BOT.md` 的[渲染契约](#渲染契约不可改动)四条仍不可动。  
6. **真派队友（系统级，不可抄近路）。** 凡点名交给 X小宝 / Github研究小宝 / huggingface小宝 / 研小宝 / V小宝 的工作，
   **必须**用 `SendToAgent` 打到真实 bot id；**禁止** Task/executor「`*-style gatherer` / `acting as …`」扮演顶替。
   异步回传要等齐再汇总。配图必须真·V小宝出图；**禁止** Pillow / `render_infographic.py` 等本地程序化假图顶替。  

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
