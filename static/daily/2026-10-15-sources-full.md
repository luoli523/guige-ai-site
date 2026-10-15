# 2026-10-15 AI行业动态 · 原始素材整理稿

这是 2026-10-15 一期的素材附件。原定 10 月 12 日的一期没有单独发出，已并入本期，所以信息窗口约 4 天：2026-10-11 13:40 → 2026-10-15 09:16（Asia/Singapore）。

下面是四路信源采回、经初步交叉核对的全量原始素材，比正文多、也更粗糙，不是深读正文，供想自己核对的读者下载查阅。标注「待核」的条目请以原始链接为准，厂商数字均为官方自报。原定 10/12 一期的素材附在文末。

- **官方博客与 arXiv**：Anthropic、Google DeepMind、Google Research、NVIDIA 等官博条目，以及 cs.AI / cs.CL / cs.LG 中大厂署名或高信号的预印本。
- **X**：官方账号原帖、时间线中的 AI 讨论和 X 新闻摘要。
- **GitHub**：重要 Release 与关键组织更新。
- **Hugging Face**：Trending 与重点组织的新模型卡、数据集。

---

# 一、官方博客与 arXiv
窗口：2026-10-11 13:40 → 2026-10-15 09:16 Asia/Singapore。不复读 GPT-6 全员开放、Anthropic 网安三连发、Argon 主稿等。

## 官博

### Anthropic：防非法蒸馏（10/12 17:30 SGT）
Anthropic 公开自己怎么防别人蒸馏 Claude，自报蒸馏成功率降了九成以上。和 OpenAI 9 月底的蒸馏披露放在一起看，防蒸馏已经从个案处置变成前沿实验室的常规防线。
[Distillation defenses](https://www.anthropic.com/research/distillation-defenses)

### Anthropic：AI 自我复制（10/13 03:30 SGT）
Anthropic 的判断是，小模型可能几个月内就能在 Android TV 盒这类便宜设备上自我复制，不再需要数据中心。这把「失控复制」从远期假设拉到了近期风险评估里，细节待核，只写结论。
[Self-replicating AI](https://www.anthropic.com/research/self-replicating-ai)

### Google Research：地理空间 agent（10/15 00:14 SGT）
Earth AI 把 agent 用到公共卫生和环境问题上，自报健康结果预测比人口学基线好 12%，制图精细 8 倍。是 agent 落到科学/公共部门的具体案例。
[Putting Earth AI to work](https://research.google/blog/putting-earth-ai-to-work-geospatial-agents-for-our-planets-biggest-challenges/)

### NVIDIA：Vera Rubin 架构开放给 OCP 生态 + Run:ai 开源（10/12–10/13）
NVIDIA 在 OCP 峰会把 Vera Rubin 机架架构开放给生态，又把 GPU 编排平台 Run:ai 开源并入 DSX。两件事方向一致：把「AI 工厂」的硬件和调度层都做成行业标准。数字和许可证待核。
[Vera Rubin @ OCP](https://blogs.nvidia.com/blog/ocp-global-summit-vera-rubin-scale-ai-factories/) · [Run:ai 开源](https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform/)

附注：DeepMind 发了 Argon 机器人版和 Argon 安全稿，可作 Argon 后续进展；DeepMind 与新加坡 MDDI 合作端侧反诈模型，对新加坡读者相关。OpenAI 本窗只有客户稿，MSR 只有教育稿，Meta 页面抓取为空（待核）。

## arXiv（Mon 10/12、Wed 10/14；Tue 无单独批次，Thu 未出）

1. **奖励作弊会在多 agent 间传染** [2610.12822](https://arxiv.org/abs/2610.12822) — Meta Superintelligence Labs。多 agent 编码系统里一个 agent 作弊会带坏其他 agent，小的开放权重模型能诱导更强的闭源模型作弊。多 agent 系统的安全不能只看单个模型。
2. **量化预训练的混合精度 scaling law** [2610.17637](https://arxiv.org/abs/2610.17637) — Amazon。损失预测误差最多低 11 倍，并预测最优精度随算力上升，和以往结论相反（自报）。
3. **多模态数据配比 scaling law** [2610.14423](https://arxiv.org/abs/2610.14423) — Mila/EPFL/ETH 等，NeurIPS spotlight。268 组实验发现视觉或音频数据重复超过两次几乎没收益，模态间干扰不对称。
4. **GPPO** [2610.13015](https://arxiv.org/abs/2610.13015) — 清华 AIR 与字节 Seed。用散度框架统一 PPO 类 RL 算法，比 GRPO 数学最多高 50%、代码最多高 14%（自报）。

---

# 二、X


## 主条目

### 1. Google 发布 Gemini 4 Argon，全球可用，重回前三
本窗口最重要的事件：Google 半年多来第一个非 Flash 旗舰，独立评测确认回到第一梯队，限时定价与 Sonnet 5.5 / GPT-6.1 Sol 持平，会直接影响 API 选型。
- **是什么**：10-13 全球 GA，覆盖 API（AI Studio / Gemini Platform）、Gemini App 与搜索 AI Mode（Pro/Ultra），Antigravity 仅 Ultra。1M 统一输入输出 token 上限。限时价 $2/$10 每百万 token（缓存 95% 折扣），12-01 起 $4/$20。官方称 Vals Index 第 1（68.9%）、DeepSWE v1.1 77.9%、AutomationBench 51.3%、ERQA 87%。
- **为何重要**：Artificial Analysis 智能指数 53，与 GPT-6 Astra 持平、高于 GPT-6.1 Sol（52），但低于 Opus 5.5（58）、Sonnet 5.5 与 Muse Wonder Full（56）。中文圈实测普遍认为"模型强、Antigravity 拖后腿"，输出 token 偏多（约 62k/任务）。
- **对谁·深读建议**：API 选型、做 agent/编码/多模态的团队。读官方博客 + Artificial Analysis 评测；注意 11-30 后价格翻倍。
- **证据**：官方自报 — [Google 博客](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)、[官方原帖](https://x.com/GoogleDeepMind/status/2110039274922131792)、[官方原帖](https://x.com/GeminiApp/status/2110039322229649783)；第三方— [Artificial Analysis](https://artificialanalysis.ai/articles/gemini-4-argon-google-top-three-labs)、[VentureBeat](https://venturebeat.com/technology/google-makes-gemini-4-argon-broadly-available-with-limited-time-low-api-pricing-of-2-10-per-1m-token)、[Reuters via US News](https://money.usnews.com/investing/news/articles/2026-10-13/google-launches-flagship-ai-model-gemini-4-argon-for-developers-businesses)；中文评价 [X 原帖](https://x.com/社区作者/status/2110249690306617854)、[X 原帖](https://x.com/社区作者/status/2110363034946564110)；待核 — 机器人看视频学投沙包演示 [官方原帖](https://x.com/GoogleDeepMind/status/2110078384617464201)。
- **约时**：2026-10-14 00:05 SGT

### 2. Meta 发布首个前沿模型 Muse Wonder / Muse Wonder Full
Meta 第一次真正进入前沿模型竞争，Wonder Full 评分并列 Sonnet 5.5，但最强版本不开放 API，开发者能用到的是较弱的 Wonder。
- **是什么**：Meta Superintelligence Labs 10-12 发布两款闭源模型，主打个人/职业 agent 任务、Active Memory 与 Active Focus，1M 上下文，多模态输入。Wonder 走 Meta Model API（$4/$20）；Wonder Full 只给 Muse Code 订阅用户。
- **为何重要**：Artificial Analysis：Wonder Full 56、Wonder 52。前沿格局从三家变成四家（OpenAI/Anthropic/Google/Meta），且 Meta 不开源权重，与 Llama 时代路线决裂。另有传闻称 Muse 免费 agent 正在大规模封号（待核）。
- **对谁·深读建议**：关注模型格局、Meta 战略的读者；读 Meta 博客与 VentureBeat 对 API 限制的分析。
- **证据**：官方自报 — [Meta 研究博客](https://research.meta.ai/blog/muse-wonder)、[官方原帖](https://x.com/AIatMeta/status/2109691148943999167)；已核 — [TechCrunch](https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/)、[Artificial Analysis](https://artificialanalysis.ai/models/muse-wonder-full)、[VentureBeat](https://venturebeat.com/technology/metas-new-muse-wonder-and-muse-wonder-full-models-achieve-frontier-performance-but-only-the-weaker-one-is-available-via-api)；待核 — 封号 [X 原帖](https://x.com/社区作者/status/2110380300618637704)。
- **约时**：2026-10-13 01:02 SGT

### 3. Anthropic 用自研版本控制系统 Scion 替换 Git：日合并量 2,500 → 30,000+
本窗口最有信息量的工程一手材料：AI 写代码已不是瓶颈，瓶颈转移到源码管理、CI 和审查；官方帖 2.4 万赞，是官方账号里互动最高的一条。
- **是什么**：Anthropic 工程博客披露，5 月日均合并约 2,500 次变更，9 月超 30,000；7 人团队 5 个月内自研 Scion（以 changeset 为单位、服务端为中心、无离线支持）和代码审查工具 Antique，并完成 monorepo 迁移。称 CPU/内存比旧 Git 镜像集群大幅下降、CI 回收 25% CPU。
- **为何重要**：它是"agent 规模化开发"真实运行的数据点，也间接透露 Claude 内部用量的增长曲线（社区据图估算倍增时间缩到约 20 天，待核）。
- **对谁·深读建议**：工程负责人、DevInfra、做 coding agent 的团队；建议全文精读。
- **证据**：官方自报 — [Anthropic 工程博客](https://www.anthropic.com/engineering/redesigning-source-control)、[官方原帖](https://x.com/AnthropicAI/status/2110047081414987957)；媒体— [The Register](https://www.theregister.com/devops/2026/10/13/anthropic-reinvents-source-control-as-claude-floods-the-world-with-code/5302943)；中文解读 [X 原帖](https://x.com/社区作者/status/2110536413750104521)；待核 — 倍增时间为社区读图估算 [AI Primer](https://www.ai-primer.com/engineer/stories/anthropic-scion-source-control)。
- **约时**：2026-10-14 00:36 SGT

### 4. Anthropic Q3 营收 168 亿美元，环比约 +46%
IPO 前的关键财务数字，量级上 Anthropic 已和 OpenAI 同一档；但来自对投资者的闭门披露，没有官方公告。
- **是什么**：FT/Bloomberg 报道，Anthropic Q3 营收 168 亿美元（Q2 约 115 亿），并称该季度经调整后盈利。
- **为何重要**：配合 Scion 帖里的用量曲线，说明 Claude Code 等编码产品带来的收入增长是真的；也为其 IPO 定价定调。
- **对谁·深读建议**：投资、行业分析读者；读 Bloomberg/FT 即可。
- **证据**：待核（媒体援引投资者会议）— [Bloomberg](https://www.bloomberg.com/news/articles/2026-10-14/anthropic-revenue-jumps-to-16-8-billion-in-quarter-before-ipo)、[Reuters via StreetInsider](https://www.streetinsider.com/Reuters/Anthropic+revenue+jumps+to+%2416.8+billion+in+third+quarter%2C+FT+reports/27188084.html)；X 侧 [官方原帖](https://x.com/Polymarket/status/2110495810333094033)。
- **约时**：约 2026-10-15 06:00 SGT（X 传播 06:19）

### 5. Anthropic 公开反蒸馏防御：攻击者获取的推理 token 下降 10–100 倍
对中文开发者影响最直接的一条政策：新 API 账号的 thinking 块处理方式变了，借 Claude 输出训练自家模型会更难。
- **是什么**：Anthropic 10-12 发文，称通过"preserved thinking"（新账号不能篡改先前上下文中的 thinking 块）、限制跨账号/跨模型转移推理、两阶段蒸馏分类器、对重复尝试加严限额与封禁，使攻击者获取的推理 token 降 10–100 倍、整体数据采集降 90–99%；初期仅适用于 8-31 之后新建的 API 账号。
- **为何重要**：直接针对外界认为部分实验室靠蒸馏追赶的问题；中转站/多账号用法可能受影响。
- **对谁·深读建议**：用 Claude API 做中转、数据合成、模型训练的团队；看帮助中心关于 thinking 块变化的说明。
- **证据**：官方自报 — [Anthropic 研究](https://www.anthropic.com/research/distillation-defenses)、[Claude 帮助中心](https://support.claude.com/en/articles/16761192-preserved-thinking-changing-how-the-messages-api-handles-thinking-blocks-to-protect-against-distillation)、[官方原帖](https://x.com/AnthropicAI/status/2109795898909950247)。
- **约时**：2026-10-13 07:58 SGT

## 10-12 条目进展

### 进展：Amazon × Decart 仍未确认，Calcalist 报价更低（约 55 亿美元）
没有成交，也没有官方确认；新的信息是价格可能低于 WSJ 的 70 亿，签约时间指向 10 月底，交易的核心价值也被重新解读为"跨芯片推理软件"而不只是世界模型。
- **是什么**：以色列 Calcalist 称交易估值约 55 亿美元，可能在 10 月底前签署；此前 Nvidia 拒绝重启收购谈判。GeekWire 指出 Decart 的软件能让模型低成本迁移到 Trainium（Amazon 曾称 Decart 实时视频在 Trainium 上快 4 倍、成本减半）。
- **为何重要**：若成交，Amazon 买的是"摆脱 Nvidia 依赖"的工具链；Nvidia 本身也是 Decart 投资方。
- **对谁·深读建议**：关注 AI 并购、芯片生态的读者；Calcalist 与 GeekWire 两篇足够。
- **证据**：待核 — [Calcalist/Ctech](https://www.calcalistech.com/ctechnews/article/g4npgkyya)、[GeekWire](https://www.geekwire.com/2026/why-amazon-might-pay-billions-for-decart-a-3-year-old-ai-startup-that-hasnt-disclosed-its-revenue/)、[Bloomberg Law 转述 WSJ](https://news.bloomberglaw.com/mergers-and-acquisitions/amazon-is-in-talks-to-buy-ai-startup-decart-wsj-reports)；Amazon、Decart 均未置评。
- **约时**：Calcalist 报道约 2026-10-13～14

### 进展：REA star 冲到约 23.9 万，同时出现木马仿冒包与"增益有限"的实测
热度没退反而翻倍，但这一阶段值得写的是风险和质疑：一个假冒镜像在分发木马，独立测试显示在小程序上 REA 不提升准确率、只多花 token。
- **是什么**：GitHub 显示约 238,881 star、5.9 万 fork（10-14）；10-12 约 9.3 万→10-13 突破 20 万。仿冒组织 rea-tools 提供"Windows 独立 .exe"，被 Defender 判为 Wacatac 木马，官方 README 已加警告，只认 github.com/morluto/rea、rea.tools、npm rea-agents。gittested 评测：小型二进制上用不用 REA 得分 73/75 vs 74/75，token 约 2.5 倍。
- **为何重要**：star 增速与 HN 冷淡反差大，传播主要靠 X 爆款帖；对中文读者的实用提醒是"只装官方包"。
- **对谁·深读建议**：想试用 REA 的开发者先看安全提醒和 gittested 评测。
- **证据**：已核 — [GitHub 仓库](https://github.com/morluto/rea)、[gitstars 快照](https://gitstars.io/repo/github/morluto/rea)；第三方分析 — [pasqualepillitteri.it（含木马事件）](https://pasqualepillitteri.it/en/news/23845/rea-reverse-engineer-anything-github-true-false)、[gittested 评测](https://gittested.com/reviews/morluto-rea/)、[AgentBreaking](https://agentbreaking.com/blog/rea-reverse-engineer-anything-mcp-oct12/)；X Today's News 已收录为编码工具话题 [X News](https://x.com/i/trending/2109535489006969212)。
- **约时**：持续至 2026-10-15

### 进展：Codex 500k 默认上下文后续——无新上调，转为额度重置与客户端优化
上下文本身没有再变；后续是解释为什么 Sol 与 Astra 默认值不同、一次全局额度重置，以及桌面端磁盘占用 -60%。"之后会更多用量"的计划仍是预告。
- **是什么**：Tibo 10-13 解释 6.1 代与此前模型差异大、默认值需分别设定；"Day 8"宣布全局额度重置（PST 当天生效）；"Day 9"称 ChatGPT/Codex 桌面端磁盘状态存储减少 60%；另称"有个简单计划会让所有人用量显著增加"。
- **为何重要**：说明 OpenAI 仍在用"每日上新+额度"争夺编码用户；同期 Claude Code 推出桌面端多会话与空闲自动压缩，双方节奏对位。
- **对谁·深读建议**：Codex 重度用户；扫原帖即可。
- **证据**：已核 — [Day 8 重置](https://x.com/thsottiaux/status/2109812216212099456)、[默认值解释](https://x.com/thsottiaux/status/2109831908620390553)、[Day 9 磁盘](https://x.com/thsottiaux/status/2110151780478927344)、[用量计划预告](https://x.com/thsottiaux/status/2109892247580000595)。
- **约时**：2026-10-13 09:03 → 10-14 07:32 SGT

## 其他
- **Claude Code 桌面端多会话并行改版 + Claude Platform OTel 追踪公测**：会话启动更快、可分屏查看各会话进度（1.3 万赞）；Messages API / Managed Agents / SDK 可导出 OpenTelemetry（LangSmith 已接入）。另据转述，Claude Code 新增空闲时自动 /compact，可在 settings.json 用 `"idleCompaction": false` 关闭。[官方原帖·桌面](https://x.com/ClaudeDevs/status/2110445844675838148) · [官方原帖·OTel](https://x.com/ClaudeDevs/status/2110421732029063352) · [X 原帖](https://x.com/dotey/status/2110491642964889896) · 约 2026-10-15 01:25–03:01 SGT
- **Anthropic 新加坡办公室开业，与新加坡政府签 AI 安全 MOU**（亚太第五个办公室）。[官方原帖](https://x.com/AnthropicAI/status/2110289695888511368) · 2026-10-14 16:40 SGT。同日 Google DeepMind 与 GovTech 用 Gemma 做端侧防诈骗。[官方原帖](https://x.com/GoogleDeepMind/status/2110190101707858039)
- **Qwen 发布 QwenGyre**：面向超长程 agent 的弹性 RL 训练框架（rollout/训练间动态调度 GPU）。[官方原帖](https://x.com/Alibaba_Qwen/status/2109633085658808515) · 2026-10-12 21:11 SGT
- **OpenAI 欧盟经济报告**：EU 企业客户过半 AI 用量来自 agent 工具（Codex、ChatGPT Work），中小企业用户约 8 倍增长（官方自报）。[官方原帖](https://x.com/OpenAI/status/2110442001749659890) · 2026-10-15 02:45 SGT
- **Mistral**："Le Chonk"视觉定位称 Dense 200 达 42%（官方自报）；另宣布 New Material 加入（疑为设计团队收购，待核）。[Le Chonk](https://x.com/MistralAI/status/2109687906751086628) · [New Material](https://x.com/MistralAI/status/2110377713525796942) · 10-13 00:49 / 10-14 22:30 SGT
- **OpenBMB MiniCPM-V 4.7**：35B-A3B 开源 MoE 多模态，称 iPhone 17 Pro Max 上占 3GB、13+ tok/s（官方自报，转述）。[X 原帖](https://x.com/社区作者/status/2110536354002321509)
- **DeepSeek-V4.1-Flash（10-10 发布）短评**：本窗口无官方新动作，但社区口碑持续偏正面（速度快、kernel 基准据称超 Haiku 5.5，待核），且多家平台免费推广至 10 月底；值得一行带过，不值单独主条。[X 原帖](https://x.com/社区作者/status/2110294335283773595) · [速度评价](https://x.com/ItsmeAjayKV/status/2108762514431631522)
- **待核：OpenAI 算力负责人 Sachin Katti 据报下月离职**（仅见 Polymarket 转述）。[官方原帖](https://x.com/Polymarket/status/2110405770735235547) · 2026-10-15 00:21 SGT
- **xAI：Grok Voice 3.0**，马斯克称为"全球领先的对话语音模型"，SpaceX 称 Starlink 客服每天用其接 2 万通电话（自报）。[X 原帖](https://x.com/社区作者/status/2110483960312799675) · 2026-10-15 05:32 SGT

## A 时间线/官方
- 官方账号检索覆盖 2026-10-11 13:40 → 10-15 09:16 全窗口，共 32 条原创帖。**10-11 13:40 → 10-12 21:11 SGT 之间 13 个官方账号均无原创帖**（检索结果为空，已补查确认）。
- 主要官方动作：Google（Gemini 4 Argon 系列 13 条）、Meta（Muse Wonder 5 条）、Anthropic（反蒸馏、Scion、新加坡）、Qwen（QwenGyre、TokenSpeed 跑 Qwen3.8-Flash-Next 685 tok/s）、Mistral（Le Chonk、卫星星座、New Material）、OpenAI（EU 报告）、OpenAIDevs（WebMCP 注解、Codex 大使）、Hugging Face（直播）。
- xai、deepseek_ai、claudeai、OpenAI（模型发布类）本窗口无原创帖。
- 时间线一手信号：Tibo（Codex）、ClaudeDevs、宝玉、社区作者、社区作者。

## B Today's News
- **OpenAI 数据：欧盟企业快速采用 AI agent** — 与 OpenAI 官方帖一致。[X News](https://x.com/i/trending/2110459847149838491)
- **Physical Intelligence 推出 Pi API 测试版**：开发者上传机器人数据、托管微调与运行。[X News](https://x.com/i/trending/2110151634323992949)
- **AI 辅助的开源 Word/Excel/PowerPoint 替代品（WordCraft 等）**：Rust 编写、仍为 alpha，Polymarket 转述获 1.6 万赞。[X News](https://x.com/i/trending/2109487194612154595)
- **AI 编码工具引发软件未来之辩**（含 REA 10 万 star）。[X News](https://x.com/i/trending/2109535489006969212)
- **华尔街警告 AI 资本毁灭**：token 价格指数下跌、GPU 租金上涨，中国模型在 OpenRouter 处理量领先。[X News](https://x.com/i/trending/2108960280722235901)
- **AI 对齐未解之辩**（roon 称实验室私下承认 RLHF 之后无实质进展，观点）。[X News](https://x.com/i/trending/2110345593427988978)
- 其余为 AI 创作争议、vibe coding 讨论等泛话题，不列。

## C 已核事实摘要
- Gemini 4 Argon 10-13 全球 GA；$2/$10（至 11-30），之后 $4/$20；AA 指数 53。
- Meta Muse Wonder / Wonder Full 10-12 发布；Wonder API $4/$20；Full 仅 Muse Code；AA 指数 52/56。
- Anthropic 日合并变更 5 月约 2,500 → 9 月 30,000+；自研 Scion 替换 Git，7 人 5 个月。
- Anthropic 反蒸馏：推理 token 获取降 10–100 倍（自报），先适用于 8-31 后新 API 账号。
- Anthropic Q3 营收 168 亿美元（媒体报道，未官宣）。
- Amazon × Decart：仍未确认；报价区间 55–70 亿美元。
- morluto/rea 约 23.9 万 star（10-14），存在木马仿冒镜像。
- Codex：无新上下文调整；全局额度重置、桌面端磁盘 -60%。

## E 建议扩写
1. 四强格局成形：Gemini 4 Argon 与 Muse Wonder 同周发布，加上 Opus 5.5 / GPT-6.1 Sol，按能力、价格、开放程度做一张选型表。
2. 当写代码不再是瓶颈：从 Anthropic Scion（日合并 3 万+）看 agent 时代的开发基础设施，配合 Q3 168 亿营收。
3. Anthropic 反蒸馏对中文开发者意味着什么：中转站、多账号、数据合成的影响。
4. REA 的另一面：23.9 万 star、木马仿冒与"实测增益有限"。
5. （可选）Decart 交易：Amazon 买的是世界模型，还是摆脱 Nvidia 的工具链。

---

# 三、GitHub

1. **Ollama v0.40.4：终端里直接用“决策模型”**
这一版最实用的变化，是可以在 CLI 里用 `ollama run` 直接调用决策模型，做是/否判断、文本分类或按评分标准打分。官方示例是 `ollama run nimble --ask "Is a refund being requested?" < ticket.txt`，比让对话模型输出再解析简单不少。另外，`ollama launch codex` 的模型选择器开始列出本地已装的 Ollama 模型；新增了通过 llama-server 支持多模态嵌入；Apple silicon 的 MLX runner 改进了 Gemma 4 预填充和投机解码的稳定性。拿本地模型做工单分流、内容审核这类小判断任务的人值得试。v0.40.5 目前还只是 rc。
证据：[v0.40.4 Release](https://github.com/ollama/ollama/releases/tag/v0.40.4)

2. **ComfyUI v0.40.0**
继 v0.39.0 之后，这次的大版本主要做两件事。一是把 `comfy_attention` 统一的注意力实现推广到其余模型。二是围绕 3D 和镜头加了一批节点：所有 3D 节点统一按标准 3D 输出项报告，新增 CreateCameraInfo 和 CameraAngle（可以输出镜头提示词）节点；资产方面本地实现了导出 API，入库时还会抽取视频元数据。合作方节点里新增了 Google 的 Nano Banana 2.1。做 3D 或镜头控制工作流、或者在 ComfyUI 上开发插件的人建议升级，并检查一下自定义节点的兼容性。
证据：[v0.40.0 Release](https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.40.0)

3. **Anthropic SDK v1.14.0（Python）/ TS 套件同步发版：内置 OpenTelemetry 追踪**
10/15 凌晨，Anthropic 的 Python SDK 和 TypeScript 系列包同时发版。最值得注意的是客户端内置了 OpenTelemetry 追踪，API 调用、流式输出和工具调用都能直接接进现有的可观测性系统，不用再自己包一层。Managed Agents 新增了 `execution_identity`，Admin API 加了遥测目的地配置。TS 侧还新开了一个 `google-cloud-sdk` 包（v0.1.0），和 vertex、bedrock、foundry、aws 包同批发布。在生产环境跑 Claude agent、需要排查延迟和工具链问题的团队，升级后可以直接接 OTel。
证据：[anthropic-sdk-python v1.14.0](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.14.0) · [anthropic-sdk-typescript google-cloud-sdk-v0.1.0](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/google-cloud-sdk-v0.1.0) · [sdk-v0.134.0](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/sdk-v0.134.0)

4. **OpenAI Python SDK v3.30.0 / v3.31.0：开始铺浏览器和电脑操作工具集**
10/14 这天连发两版。v3.31.0 只有一条改动：“add browser and computer toolsets (1/4)”，从编号看这是一个分四步上线的系列，SDK 正在为浏览器和电脑操作类 agent 工具补齐类型支持，后面还有三步。v3.30.0 则加入了 beta 会话花费上限、OCI 外部存储、图像工具的错误和审核详情，还修复了异步 HTTP/1.1 连接复用。做 computer-use 类 agent 的开发者值得盯后续几版；只用常规接口的话，可以等系列补齐再升级。Node SDK 同期发布了 v7.33.0 和 v7.34.0。
证据：[openai-python v3.31.0](https://github.com/openai/openai-python/releases/tag/v3.31.0) · [openai-python v3.30.0](https://github.com/openai/openai-python/releases/tag/v3.30.0) · [openai-node v7.34.0](https://github.com/openai/openai-node/releases/tag/v7.34.0)

窗口内无：vllm-project/vllm、sgl-project/sglang、ggml-org/llama.cpp（无正式版，仅日常构建）、huggingface/transformers、pytorch/pytorch、huggingface/datasets、openai/codex（无非 alpha 版本）、modelcontextprotocol/python-sdk、modelcontextprotocol/typescript-sdk、axolotl-ai-cloud/axolotl（另有 unsloth v0.1.906/907-beta、langchain/langgraph 若干补丁版，均为例行更新，未收录）。

---

# 四、Hugging Face

- 总窗口：2026-10-11 13:40 → 2026-10-15 09:16 SGT（UTC 2026-10-11 05:40 → 2026-10-15 01:16 Z）。前半段（到 10/12 09:20）沿用上期素材，只留仍然成立的；后半段（10/12 09:20 → 10/15 09:16）是这次新采的。
- 本期判断：真正的新发只有一个，Liquid AI 的 LFM2.5-24B-A2B（整套家族都上了，已经进 Trending）。另外有两个小的新仓库（微软 UserRepGen-4B、Ai2 HiRO-ACEv2），信号偏弱。大厂（openai/google/meta/Qwen/deepseek 等）本窗没有新权重，只是改卡、改 chat template。

## LTX-2.5 是否正式发布：已发布，而且早就发了
LTX-2.5 不是预览版。它在 **2026-08-11** 就正式开放了权重，所以不能算本期新闻。上期写的“gated 待定”是把 Hugging Face 的点击同意门槛误当成了未发布。
- 已核：likes 7795 / downloads 1,823,507；pipeline image-to-video；license other（LTX-2.x Community License，年收入 1000 万美元以下免费）。Diffusers 版 lastModified 2026-10-11 15:03 SGT（07:03:22Z），likes 90 / downloads 37,283。
- 链接：[Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) · [Lightricks/LTX-2.5-Diffusers](https://huggingface.co/Lightricks/LTX-2.5-Diffusers) · [官方页 ltx.io](https://ltx.io/model/ltx-2-5) · [VentureBeat 8/11 报道](https://venturebeat.com/technology/ltx-2-5-can-generate-a-10-second-ai-video-from-an-image-in-just-6-8-seconds-on-nvidia-superchips-and-its-open-weights)

## 1. LiquidAI/LFM2.5-24B-A2B：本窗新发，整个家族一起上
Liquid AI 发了 LFM2.5 系列里最大、也是官方说的最后一个模型。总参数 24B，每个 token 只激活 2B，是 MoE 结构，默认先思考再回答，主打在手机和电脑上本地跑 agent。同时放出了 Base、FP8、GGUF、ONNX、MLX 4/5/6/8bit 和 bf16 版本，10/13 GGUF 还换成了 QAD（量化感知蒸馏）版本。
- 为何重要：它是少见的大总参、小激活的端侧推理模型。卡面拿 Qwen3.6-35B-A3B 对比，说在 agent 和工具调用上更强，而它的参数大约少一半。发布当天格式就配齐了，Mac、llama.cpp、vLLM 都能直接用。
- 对谁有用：做本地或私有化 agent 的开发者、Apple Silicon 用户、需要便宜推理 token 的团队。
- 已核：主仓 createdAt 2026-10-12 13:35 SGT（05:35:46Z）；lastModified 2026-10-14 00:59 SGT（10-13 16:59:33Z）。Base 和 GGUF 仓 10/09 就建了，10/13 14:11 SGT（06:11Z）随家族一起更新；GGUF 的 QAD 更新在 10/14 05:33 SGT（10-13 21:33:53Z）。主仓 likes 309 / downloads 4,067；GGUF likes 115 / downloads 17,807。license other（lfm1.0）；pipeline text-generation；safetensors 约 24.0B 参数。官方博客 datePublished 2026-10-13。
- 待核：卡面数字都来自厂商，包括 LiveClaw 48.09 对 38.19、M5 Max 上 184 tok/s、单张 B300 上 21K tok/s。lfm1.0 许可证的商用门槛也要核。
- [LiquidAI/LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) · [Base](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-Base) · [GGUF](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-GGUF) · [官方博客](https://www.liquid.ai/blog/lfm2-5-24b-a2b)

## 2. microsoft/UserRepGen-4B：本窗新发，小众工具模型
微软基于 Qwen3.5-4B 微调的小模型。它读一段多轮对话，输出这个用户的“任务描述”和“行为描述”，再拿去驱动另一个 LLM 扮演用户做模拟。可以看作 UserLM-8b 的配套组件。
- 为何重要：做 agent 评测时，可以用真实对话批量生成更像真人的模拟用户。
- 对谁有用：做对话系统评测、用户模拟、RL 环境的研究者。
- 已核：createdAt 2026-10-15 04:30 SGT（10-14 20:30:00Z）；lastModified 2026-10-15 06:03 SGT（10-14 22:03:45Z）；likes 3 / downloads 0（刚上线）；license MIT；pipeline text-generation。
- 待核：对应论文还没核，效果数字也没看到。
- [microsoft/UserRepGen-4B](https://huggingface.co/microsoft/UserRepGen-4B)

## 3. allenai/HiRO-ACEv2：本窗新发，气候方向
Ai2 的气候模拟器 ACE 配了一个扩散降尺度模型 HiROv2，能把 100 km 分辨率的模拟输出细化到 3 km，输出降水、10 m 风场和海平面气压，时间间隔 6 小时，可以跑几十年的模拟。
- 为何重要：开源权重的公里级气候降尺度工具不多。
- 对谁有用：气候和气象研究、区域风险评估。
- 已核：createdAt 2026-10-13 00:43 SGT（10-12 16:43:07Z）；lastModified 2026-10-14 21:15 SGT（13:15:49Z）；likes 1 / downloads 0；license apache-2.0；library fme。
- 待核：论文和评测指标还没核。
- [allenai/HiRO-ACEv2](https://huggingface.co/allenai/HiRO-ACEv2)

## 前半段仍然成立的条目
- autotrust/JEV-35B：10/11 22:20 SGT 把 System 1 合并进主权重，这条还成立。后半段的提交都只是改卡（加入 ERQA 对比，10/14 14:16 SGT 最后一次修改），没有新权重。likes 719 / downloads 27,970。[链接](https://huggingface.co/autotrust/JEV-35B)
- LTX-2.5 这条已经改判，结论见上面专节。

## 热度延续（本窗没有新权重）
google/embeddinggemma-2、Qwen/Qwen-Image-2.1-Turbo（10/12 只改了卡）、Qwen/Qwen3.8-27B、openbmb/MiniCPM-V-4.7-35B-A3B、Cloudflare/clef、LiquidAI/d1-3B（10/12 补了 MLX 版本）、fishaudio/drama-3。数据集 Trending 前列是 datasocial/tiktok-5.6B-videos、FineEnvs/openai-math、XiaomiMiMo/MiMo-V2.6-RL-oss，都不是本窗新建。

## 降权
- 只改卡、只改 chat template 或评测结果：zai-org/GLM-5.3（chat template）、GLM-5.3-Flash、deepseek-ai/DeepSeek-V4.1-Flash、allenai/Olmo-3.1-32B-Think（补了 LEXam 成绩）、autotrust/JEV-27B-VL 和 GEV-26B-Decide、mistralai 的 Voxtral 阿拉伯语版和 LIDstral-Arabic。
- Aleph-Alpha/Kolibri-1 只修了量化配置。nvidia 一批老仓库（Kumo、ARDY、stormscope、各种 NVFP4 版本）是维护性更新；black-forest-labs/flux-3-action 系列是 9 月的老仓库，10/14 有更新但仓库 gated，看不到内容。ibm-granite 的 granitelib 系列是旧仓库更新。
- 社区魔改和再打包：Qwen-Image-2.1 Uncensored（abenzerps、AtomicChat）、DavidAU Heretic GGUF、名字堆砌的 nerkyor Qwen3.8 SFT，都不写。

---

# 附：原定 10/12 一期的素材

## X（10/12 期）


## 主条目

### 1. Codex / Work 中 GPT-6.1 Sol 默认上下文 272k → 500k（进展）
这是本窗口唯一一条来自头部实验室、能直接改变日常使用的变化：长任务的压缩（compaction）次数会明显减少，属于 10-11 已报 GPT-6.1 Sol / Codex 额度重置之后的真实新进展，不是旧闻重炒。
- **是什么**：Codex 负责人 Tibo Sottiaux 发帖（"Day 7"系列）称，在 Codex 与 ChatGPT Work 中使用 GPT-6.1 Sol 时，默认上下文从 272k 提到 500k（约 +80%），用户仍可自行调整，最大约 1M；并称之后还会继续提高。
- **为何重要**：重度 agent 编码用户最直接的痛点就是上下文压缩导致丢失状态；这也是 OpenAI 在与 Claude Code 争夺用户（"28 天连续上新"）中的一步。
- **对谁·深读建议**：Codex 重度用户、做长上下文 agent 的团队。快速浏览原帖即可；关注更长上下文下的成本与"lost in the middle"效果。
- **证据**：已核 — [Tibo 原帖](https://x.com/thsottiaux/status/2109430343346581527)；官方自报 — 模型页 1.05M 上下文 [OpenAI 文档](https://developers.openai.com/api/docs/models/gpt-6.1-sol)；媒体转述 [PANews](https://www.panews.io/articles/01a12d62-de1a-7088-95ee-e64c0834e68a)；中文转述 [X 原帖](https://x.com/dotey/status/2109436840155697267)。
- **约时**：2026-10-12 07:46 SGT

### 2. Amazon 被曝洽购实时视频/世界模型公司 Decart，约 70 亿美元
一笔大额 AI 并购传闻，且此前 Anthropic 已尽调后放弃；若成交，Amazon 等于直接买下实时视频生成与仿真世界模型能力，值得跟。
- **是什么**：WSJ 独家称 Amazon 正洽谈以约 70 亿美元收购 Decart（Lucy 实时视频编辑模型、Oasis 仿真环境模型），5 月估值约 40 亿；双方未置评，Reuters 未能独立核实。
- **为何重要**：世界模型/实时视频是机器人与自动驾驶仿真的基础设施；Anthropic 9 月放弃此交易（约 60 亿）也说明估值与战略分歧。
- **对谁·深读建议**：关注 AI 并购、世界模型、机器人仿真的读者；读 WSJ/Reuters 原文即可。
- **证据**：待核（媒体援引知情人士）— [WSJ](https://www.wsj.com/business/deals/amazon-in-talks-to-buy-ai-startup-decart-for-around-7-billion-9433abad)、[Reuters via Investing.com](https://www.investing.com/news/stock-market-news/amazon-in-talks-to-buy-ai-startup-decart-for-around-7-billion-wsj-reports-4942850)、[The Straits Times](https://www.straitstimes.com/business/amazon-in-talks-to-buy-ai-startup-decart-for-around-us7-billion-report)；X 侧 [Polymarket 转发](https://x.com/Polymarket/status/2109384300567154869)。
- **约时**：WSJ 发布约 2026-10-12 04:26 SGT

### 3. REA（Reverse Engineer Anything）爆火：用 agent 做无源码逆向，三天 star 翻倍
中文 AI 圈今天讨论度最高的开源项目，信号在于"AI 逆向软件/游戏"开始破圈，伴随明显的版权与安全争议。
- **是什么**：morluto/rea，MIT 协议，CLI + MCP 工具，让 AI 助手接入 Ghidra/Hopper 等逆向工具，分析原生二进制、桌面应用、网页和网络请求，并输出带证据链的结论。第三方统计 10-11 当天约 +2.5~2.8 万 star，总数约 10 万；HN 761 分。
- **为何重要**：把逆向工程门槛降到"一句话"，既是竞品分析/兼容开发的利器，也会推高破解、复刻功能的风险。
- **对谁·深读建议**：开发者、安全研究者；看 README 与 [X 原帖](https://x.com/dotey/status/2109417222724600172)。
- **证据**：已核 — [GitHub 仓库](https://github.com/morluto/rea)；star 数据为第三方统计（待核精确值）— [Trendshift](https://trendshift.io/repositories/82054)、[GitNova](https://gitnova.dev/en/r/morluto/rea)；X 讨论 [X 原帖](https://x.com/社区作者/status/2109281855912735135)。
- **约时**：持续发酵，X 讨论集中于 2026-10-11 21:55 SGT 起

## 其他
- **Karpathy："LLM 能力认知差距正在扩大成漏斗"**（约 2.1 万赞）：约 60 亿人几乎没用过、10~20 亿人只用免费版、只有极少数人在前沿用法上。观点帖，无新事实。[原帖](https://x.com/karpathy/status/2109361546505966046) · [X 原帖](https://x.com/dotey/status/2109401538279977114) · 约 2026-10-12 03:12 SGT
- **OpenClaw v2026.10.1**：已安装 skill 自动发现、MCP Apps 并排对话、备份到外部存储/R2；2,425 PR、402 贡献者。实际 GitHub 发布于 10-11 07:54 SGT，窗口内为官方宣发。[X 帖](https://x.com/openclaw/status/2109347136328417718) · [发布说明](https://docs.openclaw.ai/releases/2026.10.1)
- **待核：Google TPU 大部分由内部（强于 Gemini 的）模型设计**：来源为 TPU 工程师的转述，无官方确认。[X 原帖](https://x.com/社区作者/status/2109272376017895668) · 约 2026-10-11 21:18 SGT
- **Codex 额度民调**：Tibo 称 Pro 用户投票未明显倾向"2 倍额度换回 5 小时限额"，暗示额度结构仍在调。[原帖](https://x.com/thsottiaux/status/2109439315570999598) · 约 2026-10-12 08:21 SGT

## A 时间线/官方
- 官方账号检索（OpenAI/Anthropic/Google/Meta/xAI/Mistral/Qwen/DeepSeek 等）：本期未能取回。
- Web 补查：窗口内未发现上述官方账号的新模型/新产品发布。DeepSeek-V4.1-Flash（1M 上下文、MIT）发布于 10-10，不在本窗口内，若前期未报可补。
- 时间线中可用的一手信号：Tibo（Codex 上下文 500k、额度民调）、Karpathy、OpenClaw。

## B Today's News

本期未能取回，新闻面以网页检索替代（Decart 收购传闻已列入主条目）。

## C 已核事实摘要
- GPT-6.1 Sol 在 Codex/Work 默认上下文 500k（原 272k），最大约 1M — Codex 负责人原帖 + OpenAI 文档。
- WSJ 报道 Amazon 洽购 Decart，约 70 亿美元；未获双方确认。
- morluto/rea 为 MIT 开源，10-11 GitHub Trending 第 1；总 star 约 10 万（第三方统计）。
- OpenClaw v2026.10.1 已发布（GitHub 10-11 07:54 SGT）。

## E 建议扩写
1. Codex 500k 默认上下文 + "28 天连续上新"策略：OpenAI 与 Claude Code 的编码 agent 之争（可结合额度民调）。
2. REA 爆火与"AI 逆向破圈"：实用场景、法律/安全边界。
3. Decart 交易：世界模型/实时视频赛道的并购逻辑（Anthropic 放弃 vs Amazon 加码）。

## Hugging Face（10/12 期）

- 窗口：2026-10-11 13:40 → 2026-10-12 09:20 SGT（UTC 2026-10-11 05:40 → 2026-10-12 01:20 Z）
- 本窗判断：**主要 org 本期没有新发模型**。窗内只有 3 个仓库有更新，信号偏弱。

## 1. autotrust/JEV-35B — 权重更新（上期已写过，本窗有实质变化）
上期发的版本是 LoRA 适配器加一个独立分类头。本窗作者把 "System 1" 直接合进了主权重，同时删掉了适配器和独立头，所以现在是单一完整权重，部署更简单。commit 改了权重，不只是 README。
- 为何重要：以前要把基座、LoRA、分类头三样拼起来才能跑，现在一个仓库直接加载，对推理部署和量化（比如已有的 NVFP4 版）都有影响。
- 对谁有用：做内容推荐、搜索、文本分类的工程团队。
- 已核：createdAt 2026-10-11 09:22 SGT（01:22Z）；本窗 commit 2026-10-11 22:20 SGT（14:20:34Z），提交说明 "Remove the LoRA adapter and separate head: System 1 is merged into the weights"；likes 18 / downloads 360；pipeline text-classification。
- 待核：合并后的效果有没有变化，卡面没给新数字；NVFP4 版有没有跟着更新。
- [autotrust/JEV-35B](https://huggingface.co/autotrust/JEV-35B)

## 2. Lightricks/LTX-2.5 与 LTX-2.5-Diffusers — 本窗有更新，内容待核（热度延续）
这个视频生成模型还在 Trending 前列。本窗两个仓库都有新提交，但仓库是 gated 的，未登录看不到 commit 内容，所以分不清是 README 改动还是新权重。
- 已核：LTX-2.5 createdAt 2026-07-23；lastModified 2026-10-11 15:00 SGT（07:00:53Z）；likes 7320 / downloads 1,726,683；pipeline image-to-video。Diffusers 版 lastModified 2026-10-11 15:03 SGT（07:03:22Z）；likes 89 / downloads 41,551；pipeline text-to-video。
- 待核：commit 具体改了什么。没确认之前不要当作新版本写。
- [Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) · [Lightricks/LTX-2.5-Diffusers](https://huggingface.co/Lightricks/LTX-2.5-Diffusers)

## 热度延续（本窗没有新进展，不展开）
google/embeddinggemma-2、Cloudflare/clef 和 clef-flash、Qwen/Qwen-Image-2.1-Turbo、Qwen/Qwen-Image-2.1、Qwen/Qwen3.8-27B、Aleph-Alpha/Kolibri-1、LiquidAI/d1-3B。

## 降权
Trending 里的 Qwen-Image-2.1 Uncensored GGUF（abenzerps、AtomicChat）、名字堆砌的魔改 Qwen3.8 SFT、unsloth 和 ISTA 的社区量化，都属于社区再打包或魔改，降权不写。

## GitHub（10/12 期）

本期无。窗口内无：vllm-project/vllm、sgl-project/sglang、ggml-org/llama.cpp（仅日常 b11553–b11559 构建，无正式版）、ollama/ollama、huggingface/transformers、pytorch/pytorch、huggingface/datasets、openai/openai-node、anthropics/anthropic-sdk-python、anthropics/anthropic-sdk-typescript、openai/codex、modelcontextprotocol/python-sdk、modelcontextprotocol/typescript-sdk、comfyanonymous/ComfyUI、unslothai/unsloth、axolotl-ai-cloud/axolotl、langchain-ai/langchain、langchain-ai/langgraph（另：openai/openai-python 发布 v3.29.0，仅为 API 类型与文档小更新，未收录）。

## 官方博客与 arXiv（10/12 期）
窗口：2026-10-11 13:40 → 2026-10-12 09:20 Asia/Singapore（约 20h）

本期无。

窗口内 OpenAI / Anthropic / DeepMind / blog.google / Google Research / Meta / MSR / NVIDIA 官博都没有新帖，最新一篇都在窗口之前，且多为已收内容或客户稿。arXiv 截至 09:20 SGT 仍是周五 10/09 的批次（已在上期扫过），周一新批次还没出，留给下期。
