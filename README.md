# 鬼哥的 AI 行业动态

> 每日 AI 行业与技术动态，自动采集、自动梳理、每日更新。

站点：<https://luoli523.github.io/guige-ai-site/>

一天一篇汇总简报。内容由后台 bot 抓取 X.com 与科技媒体、经 LLM 梳理后产出 Markdown，提交到本仓库即自动构建发布。页面明示 AI 自动生成，信源与筛选标准公开在「关于本站」页。

## 技术栈

| 项 | 选择 |
|---|---|
| 静态站生成 | Hugo **0.159.1 extended**（无第三方主题，layouts 手写） |
| 设计系统 | 复用主站 [luoli523.github.io](https://github.com/luoli523/luoli523.github.io) 的 Ghost Protocol 配色与字体 |
| 部署 | GitHub Actions → GitHub Pages，push 到 `main` 即发布 |
| 主题切换 | `localStorage.gg-theme`，与主站同域共享，切换状态跨站保持 |

## 目录结构

```
hugo.toml                     站点配置（baseURL 子路径、permalinks、taxonomy）
archetypes/daily.md           每日简报的 front matter 模板
assets/css/main.css           设计系统（token + 组件）
assets/css/syntax.css         代码高亮（hugo gen chromastyles 生成）
docs/BOT.md                   bot 更新指南（操作规范 + JSON schema + 退出码）
scripts/new_brief.py          JSON → 简报：校验、渲染、构建、提交
layouts/
  baseof.html                 页面外壳：head / orb / nav / footer / JS
  home.html                   首页：头条 + 往期列表
  list.html                   通用列表（tags 等）
  single.html                 通用单页（关于）
  404.html
  daily/list.html             归档页（按月分组）
  daily/single.html           单日简报页
  _partials/                  nav / footer / brief-card
content/
  daily/YYYY-MM-DD.md         每日简报 ← bot 产出落在这里
  daily/_index.md             归档页元信息
  about.md                    关于本站（信源与筛选标准）
```

## 内容契约（bot 的输出规范）

**唯一标准：深读报告。** 详见 **[docs/BOT.md](docs/BOT.md)**（可直接当 bot system prompt）。

- 文件：`content/daily/YYYY-MM-DD.md` → URL `/daily/YYYY-MM-DD/`
- 输入：JSON，必填 `summary` + `body_markdown`（完整深读 Markdown）
- 结构：一分钟速览 · 执行摘要 · 四类别主线（大厂与学术界 / X / 热门开源项目 / 模型相关，每类 1–3 条，通俗讲解 + 深入学习建议）· 次要动态 · 来源 · 行动建议
- 深度下限：正文去空白 ≥ 2500 字；旧版短讯 `sections/items` schema 已废弃

```bash
echo "$BRIEF_JSON" | python3 scripts/new_brief.py --check
echo "$BRIEF_JSON" | python3 scripts/new_brief.py --commit --push
```

首页卡片仍用 `summary`；正文为长文深读，不再是一句话新闻列表。


## 本地开发

```bash
hugo server            # http://localhost:1313/guige-ai-site/
hugo --minify          # 生产构建到 public/
```

代码高亮样式如需换主题：`hugo gen chromastyles --style=<name> > assets/css/syntax.css`

## 已完成

- [x] 站点骨架：Hugo 手写 layouts，复用主站 Ghost Protocol 设计系统
- [x] 接入 bot：按 [docs/BOT.md](docs/BOT.md) 深读契约；写权限与定时由 Grok Bot 早报 routine 执行
- [x] 主站首页「每日 AI 要闻」板块，浏览器端消费本站 `daily/index.json`
- [x] 每日配图：Hugo Pipes 转 WebP，首页/板块缩略图，点击放大
- [x] 长文右上角浮窗目录，跟随阅读高亮
- [x] 证据标注徽章（FACT / 官方自报 / 待核 计数）—— 2026-09-12 起新文不再打标签，徽章仅在存量文章上显示
- [x] 一分钟速览卡片 + 脚本层强制校验
- [x] 站内搜索（Pagefind）
- [x] 鬼哥对话气泡、音乐播放器、形象元素、favicon

## 待决策

需要拍板才能往下走的，按影响面排序。

- [ ] **内容模型：一天一篇汇总 → 一事一篇解读？**
      这是最大的一件。分类体系、搜索的价值、标签、相关推荐、内容资产的累积、
      将来能不能做付费，全部取决于它。参照 best.xiaohu.ai：297 篇存量、每天 4–10 篇、
      一事一篇；本站目前一天一篇汇总，归档只能按月排日期，长不出上面那些东西。
- [ ] **广度：要不要加「今日雷达」一节**
      四路信源采回的量远大于最终写进正文的量，瓶颈在 `BOT.md`「2–4 条主线」这个漏斗口。
      方案：保留主线深挖不动，另加一节按信源分组把剩余发现全量列出（一行一条带链接），
      深度与广度各占一栏。注意写成「可选但推荐、不替代主线」，否则容易被整节删掉。
- [ ] **`about` 页要不要进搜索索引**
      现在只索引 `content/daily/`（正文加了 `data-pagefind-body`）。加一行属性即可。

## 路线图

对标 [best.xiaohu.ai](https://best.xiaohu.ai/) 后梳理的，按性价比排序。

**近期**

- [ ] **播客版（TTS）** — 用 `guige-digital-human` 的 MiniMax 声音克隆做成鬼哥自己的声音。
      小互每篇都有播客但是合成音；用真人克隆音是本站独有优势，读者感知强，且不依赖任何决策
- [ ] **复制 Markdown / 下载 .md** — 原始 md 本来就在仓库里，直接暴露即可
- [ ] **相关内容推荐** — Hugo 内置 related content，靠 tags 算相似度
- [ ] 长文目录深度降到只显示 `##` — 现在「重点关注 / 次要动态」会重复四次，扫起来糊

**依赖内容模型决策**

- [ ] 分类体系与筛选器 — 一天一篇的话分类没有意义，必须先定内容模型

**远期**

- [ ] 会员付费 — 静态站做不了，需要外部服务（鉴权 + 支付）
- [ ] 多语言（中 / EN / 日）
- [ ] 每篇独立配色与字体
- [ ] 交互式组件（可切换状态的图解，而非静态配图）

## 相关项目

- [luoli523.github.io](https://github.com/luoli523/luoli523.github.io) — 主站（Hugo）
- [fin-report](https://github.com/luoli523/fin-report) — AI 产业链投资简报，同类每日自动流水线
- [guige-skills](https://github.com/luoli523/guige-skills) — Claude Code 自定义技能包
