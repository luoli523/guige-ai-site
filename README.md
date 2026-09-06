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
- 结构：执行摘要 · 2–4 主线深度解析（FACT/官方自报/待核）· 次要动态 · 来源 · 行动建议
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

## 待办

- [ ] 「关于本站」页的信源清单与筛选标准换成实际内容
- [x] 接入 bot：按 [docs/BOT.md](docs/BOT.md) 深读契约；写权限与定时由 Grok Bot 早报 routine 执行
- [ ] 主站首页新增「每日 AI 要闻」板块，消费本站 `index.xml` 或产出的 JSON

## 相关项目

- [luoli523.github.io](https://github.com/luoli523/luoli523.github.io) — 主站（Hugo）
- [fin-report](https://github.com/luoli523/fin-report) — AI 产业链投资简报，同类每日自动流水线
- [guige-skills](https://github.com/luoli523/guige-skills) — Claude Code 自定义技能包
