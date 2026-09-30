# 2026-09-30 AI行业动态 · 全量原始素材归档

> 时间窗口：约 **2026-09-27 09:00 → 2026-09-30 09:11**（Asia/Singapore）。 
> 本文是四路信源采回后的**全量原始归档**，供核对与延伸阅读；**不是**站点深读正文。深读见当日简报页。

本归档按四个固定渠道组织，并附学术/实验室原始摘录：

- **官方博客与学术**：OpenAI / Anthropic / NVIDIA / Google Research、arXiv 精选等
- **X 公开讨论**：官方账号、Today's News 与可核验网页补强
- **GitHub**：重要 Release、热仓、关键 org 新仓
- **Hugging Face / 模型**：Trending 与本窗更新模型卡、数据集旁线

以下正文已做对外隐私 scrub：去掉内部采集角色名、协作痕迹、可信度角标堆砌，以及社交账号 handle；裸 URL 尽量改为短标签链接。

---

## 一、官方博客与学术素材

# 采集素材 · 2026-09-30 三日刊
窗口：2026-09-27 09:00 → 2026-09-30 09:11 Asia/Singapore 
火日：`2026-09-30 AI行业动态` 
规则：宁缺毋滥；人话 + 链接；不成稿。

## 结论
本窗**极满**：OpenAI **DevDay 2026**（GPT-6.1 Sol / dots / Ultrafast 等 20+）+ Anthropic **Claude Sonnet 5.5** 同周对打中端价位；NVIDIA 开源 **Open Agent Safety / OpenShell**；Google Research **Diffusion Controller**。DeepMind / Meta 官博 / MSR 博客窗内高信号 **ZERO**（上期 Live Avatar / 长视频 / Suncatcher 不重复）。 
arXiv：Sun 空；Mon28+Tue29；`/new` 仍停 Tue29（Wed30 未出）。抽 5：DeepMind 意识评估框架、MSR ROFT、Microsoft Night Science、Meta RSI 自蒸馏、Amazon TCSAlgBench。

---

## OpenAI（DevDay 2026 · Sep 29）

### Introducing GPT-6.1 Sol（+ DevDay Recap）
**人话一句** GPT-6.1 Sol：agentic coding / computer use / 专业工作上接近 Astra，标准 I/O 价约 Astra 的 1/5；DevDay 一口气 20+ 项发布。 
**为何重要** 本窗最大产品洪峰；与 Sonnet 5.5 同周抢「高性价比主力」。 
**要点（官方自报）** API `$2/$10` per 1M，缓存输入 `$0.10`（相对标准输入约 −95%）；DeepSWE 匹配 Astra、成本约 1/5；AutomationBench 相对 Opus 5.5 **+2.2 pp**（约 1/3 成本）；OSWorld 2.0 相对 GPT-6 Sol **+7 pp**、距 Astra **−2.1 pp**；Terminal-Bench Science 均本 `$5.47`/task vs Opus/Astra ~`$23`；事实错误回答约 **11.4%→7.7%**。API id `gpt-6.1-sol`；**尚未进 Chat**。安全附录：网络安全 **Critical**、生化学 **High**，与 Astra 同 safeguards 栈 → [deploymentsafety.openai.com/gpt-6-1-sol](https://deploymentsafety.openai.com/gpt-6-1-sol) 
**对谁有用 / 深读** 全员 → **必读抬主线**。 
**证据** [openai.com/index/introducing-gpt-6-1-sol](https://openai.com/index/introducing-gpt-6-1-sol) 
Recap [openai.com/index/devday-2026-recap](https://openai.com/index/devday-2026-recap) 
（Recap 另报 Ultrafast：Codex 上最高约 **8×**/300 tok/s，API 约 **6×** — 官方自报）

### Introducing dots
**人话一句** Dots：GPT-6 Astra 驱动的 always-on 智能体，自带云电脑，可连 4000+ 应用；先向 Pro / Business Premium / Enterprise 滚动开放。 
**为何重要** 消费/企业侧「常驻 agent」主赌注。 
**深读** 产品/agent → **抬主线**。 
**证据** [openai.com/index/introducing-dots](https://openai.com/index/introducing-dots)

### Towards safety cases for frontier AI training（Sep 28–29）
**人话一句** 主张继续做前沿 RL 前应具备结构化安全文档，并向 safety case 标准演进（alignment / containment / monitoring）。 
**要点** 强调勿让自动 grader 看见 CoT（防监控规避）— 官方自报。 
**深读** 安全/治理 → **选读**。 
**证据** [openai.com/index/towards-safety-cases-for-fro…](https://openai.com/index/towards-safety-cases-for-frontier-ai-training)

（窗内客户故事 / 地区政策 / 公益资助等跳过。）

## Anthropic

### Claude Sonnet 5.5（Sep 28）
**人话一句** Claude 5.5 家族第二款：相对 Sonnet 5 输出更快约 30%+、多数工作最高可省约 30% 成本；价位仍 `$2/$10`；首个带 cyber safeguards 的 Sonnet。 
**为何重要** 中端主力大跃升；与 GPT-6.1 Sol 同价位军备赛。 
**要点（官方自报）** Terminal-Bench 4.0 **70.6%** vs Sonnet 5 **10.3%**（Opus 5.5 Xhigh **66.4%**）；FrontierCode Max **46.2%** / Xhigh **52.1%**；CursorBench **55.5%**；GDPval-AA ≈ Opus 5.5（1844 vs 1846）；OSWorld 2.1 partial **80.1%**。API `claude-sonnet-5-5`；Haiku 5.5「coming weeks」。 
**对谁有用 / 深读** 全员 → **必读抬主线**。 
**证据** [www.anthropic.com/claude-sonnet-5-5](https://www.anthropic.com/claude-sonnet-5-5)

## NVIDIA

### Open Agent Safety Platform / OpenShell 0.1.0（Sep 28）
**人话一句** 开源 OpenShell（Vera CPU 沙箱）+ BlueField-4 上 Sentry 的分层 agent 安全参考架构：沙箱、策略证明、线速旁路监控。 
**为何重要** 硬件/运行时层面对 agent 逃逸与漂移的产业级回应；与同周 OAI safety cases / DevDay 共振。 
**要点（官方自报）** OpenShell **Apache 2.0**；0.1.0 无需改写 agent 即可强制沙箱/凭证隔离；兼容 Codex / Claude Code 等。 
**深读** 企业 agent 安全 / infra → **抬选读**。 
**证据** [developer.nvidia.com/blog/nvidia-open-agent-s…](https://developer.nvidia.com/blog/nvidia-open-agent-safety-platform-a-reference-for-continuous-in-silicon-agent-monitoring/) 
OpenShell [developer.nvidia.com/blog/add-runtime-control…](https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/) 
PR [investor.nvidia.com/news/press-release-detail…](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Launches-Open-Agent-Safety-Platform-to-Secure-Agents-From-Testing-to-Deployment/default.aspx)

### DSX MaxLPS（Sep 28）
**人话一句** 策略化功率共享：同一批准功耗预算下最多可多部署约 **40%** GPU；Nscale 实测归一化总吞吐 **+49.2%**。 
**深读** 算力厂基建 → **选读**。 
**证据** [developer.nvidia.com/blog/how-nvidia-dsx-maxl…](https://developer.nvidia.com/blog/how-nvidia-dsx-maxlps-maximizes-ai-factory-throughput-and-efficiency/)

## Google Research

### Diffusion Controller（页 Sep 29 / RSS ~Sep 30 02:38 SGT）
**人话一句** 「转向阻尼」侧网络：冻结主干即可增强文生图 prompt 对齐；white-box 联合版对基线 HPS-v2 约 **90%** win rate。 
**深读** 生成控制 / 灰盒适配 → **选读**。 
**证据** [research.google/blog/how-diffusion-controller…](https://research.google/blog/how-diffusion-controller-unifies-and-simplifies-ai-image-generation/)

## DeepMind / Meta / MSR（官博）
- **DeepMind 官博**：窗内 **ZERO**（最近 Live Avatar 已在上期）。 
- **Meta AI 官博**：仍停约 2026-07 → **ZERO**。 
- **MSR 博客**：403 / 窗内仅周年综述类 → **ZERO** 高信号。 
- **blog.google 营销稿**：跳过。

---

## arXiv（Mon28–Tue29 · 宁缺抽 5 · 已核挂名）
Sun 空；Wed30 未出。原料：`arxiv-raw.md`。数字均为**论文自报**，细表 待核。

### 1. AI consciousness assessment framework — [arxiv.org/abs/2609.35618（Tue](https://arxiv.org/abs/2609.35618（Tue) 29）
**人话一句** DeepMind 一票意识/哲学+AI 作者把「AI 有没有意识」收成可操作的五层功能描述层级。 
**挂名** Google DeepMind 等（Shane Legg、Murray Shanahan、Marcus Hutter、Thore Graepel 等）。 
**要点** 概念框架，无标准 bench 分（）；先谈 mapping 再谈 hard problem（官方自报）。 
**深读** 安全/治理/意识政策 → **选读**。

### 2. ROFT — [arxiv.org/abs/2609.35741（Tue](https://arxiv.org/abs/2609.35741（Tue) 29）
**人话一句** MSR：不要 RL——agent 事后只写回顾说明，用回顾文本做 next-token 微调，编码 agent 也能涨点还更省训。 
**挂名** Microsoft Research 等。 
**要点** SWE-bench Verified **49.2%**（20 updates）vs GRPO **48.0%**（40）；Pro **29.0%** vs **25.3%**；自称约 **−63%** 训练时间（官方自报）。 
**深读** 编码代理后训练 → **抬选读**。

### 3. Night Science ideation agent — [arxiv.org/abs/2609.35706（Tue](https://arxiv.org/abs/2609.35706（Tue) 29）
**人话一句** 微软把「夜科学」做成 RL 教出的 ideation agent，故意离开低熵套路。 
**挂名** Microsoft / Microsoft Research；UIUC。 
**要点** 多样性方向约 **+27.8%**；预测引用影响最高约 **+32 pp**、originality 最高约 **+66**（官方自报；代理指标待核）。 
**深读** 科研 agent / AI-for-science → **选读**。

### 4. RSI via On-Policy Distillation — [arxiv.org/abs/2609.30652（Mon](https://arxiv.org/abs/2609.30652（Mon) 28）
**人话一句** Meta：用「自己当特权老师」的 on-policy 自蒸馏（DCE+SRCL）做推理侧 RSI。 
**挂名** Meta AI；UCR。 
**要点** Qwen3-8B Avg12：DCE+SRCL **65.97%** vs OPSD **30.35%** vs GRPO **20.28%**（官方自报；泛化待核）。 
**深读** RSI / 推理后训练 → **抬选读**。

### 5. TCSAlgBench — [arxiv.org/abs/2609.35606（Tue](https://arxiv.org/abs/2609.35606（Tue) 29）
**人话一句** Amazon 用 STOC/COLT 2026 真论文定理做研究级自动证明评测，前沿模型五跑覆盖仍只有两成多。 
**挂名** Amazon。 
**要点** **398** 题 / **138** 篇（）；GPT-5.6 Sol max 五跑 verifier-accepted **23.6%**（官方自报）。 
**深读** 前沿评测 / 自动形式化 → **选读**。

### 近失
- RSI-Master `2609.35561`（SJTU/CMU 等）；VVR `2609.35641`；Workday agent skills `2609.35692`

---

## 组装提示（给总管）
1. **主线候选**：GPT-6.1 Sol + DevDay｜Sonnet 5.5｜dots｜NVIDIA OASP/OpenShell 
2. **次要**：safety cases｜Diffusion Controller｜DSX MaxLPS｜ROFT / Meta RSI / TCSAlgBench / Night Science / 意识框架 
3. 勿重复上期：Live Avatar、长视频 Co-Director、Suncatcher、Opus 5.5、GPT-6 Sol/Luna 
4. 公开页勿写内部 bot 名


---

## 二、X 公开讨论素材

# X/AI 三日刊源包 · 2026-09-30

- **窗口（Asia/Singapore）：** 2026-09-27 09:00 → 2026-09-30 ~09:12（约 72h；UTC 起点 2026-09-27T01:00:00Z）
- **火线标题上下文：** 2026-09-30 AI 行业三日动态（**OpenAI DevDay 落地** + Claude Sonnet 5.5 + 开源模型网络能力扩散）
- **采集：** Following 时间线+ Today's News / `search_news` + 官方账号 `search_posts_all`（omit end_time）+ 网页 （官方博客 / 文档 / TechCrunch 等）

- **稀疏？** **否** — 本窗以 **OpenAI DevDay（09-29）** 为中心，叠加 Anthropic Sonnet 5.5 与 GLM-5.3 网络能力报告；刻意不复读 09-27 包主题（agent 第三方数据披露、Claude Nine Loops、Gemini Live Avatar GA、SmolDataEnvs、Epoch 成本曲线），除非窗内有实质新事实（本窗无）。

---

## A. X 时间线 / 官方自报

### 1. OpenAI · dots（常驻云端 agent）— DevDay 主产品
- **是什么：** OpenAI 发布 **dots**：由 **GPT-6 Astra** 驱动的 always-on agent，自带云端电脑，可连接 **4000+** 应用/插件，在用户离线时继续推进项目；可在 ChatGPT / Slack / Teams 交互；用户可设自主边界与禁区。先对 **Pro / Business Premium / Enterprise**（合格市场）开放，官方称「无额外费用」档位内滚动上线。
- **为何重要：** 把「对话式助手」正式产品化成 **可委托的持续工作代理**；与 Meta Muse 等个人 agent 同赛道，但绑定 ChatGPT 分发与 Astra 旗舰能力。
- **对谁 / 深读：** 产品/企业 agent/平台 — **值得深读** 官方介绍与权限/安全段落；推文作入口即可。
- **证据：** + 官方自报 · [官网 Introducing dots](https://openai.com/index/introducing-dots) · [DevDay Recap](https://openai.com/index/devday-2026-recap) · [OpenAI 推文](https://x.com/OpenAI/status/2104984504133918973) · [sama](https://x.com/sama/status/2104995014208258235)
- **约时：** 2026-09-30 01:19–02:01 SGT（X）；活动日 09-29 PT

### 2. OpenAI · GPT-6.1 Sol（近 Astra、约 1/5 价）
- **是什么：** 发布 **GPT-6.1 Sol**：面向 agentic coding、computer use、专业工作负载的中端升级；官方称多项基准接近 **GPT-6 Astra**，标准 API 输入/输出价约 **Astra 的 1/5**（API 常见报价 **$2 / $10** per MTok；缓存输入约 **$0.10/MTok**，相对标准输入约 **95%** 折扣）。已在 **ChatGPT Work / Codex / API** 对 Plus+ 开放；**尚未**进入普通 Chat。对照：媒体称原定 **GPT-6.1 Astra** 因安全评估未发。
- **为何重要：** 一周内对 Sol 线大修，把「日常重负载」性价比锚到近旗舰；直接回应订阅/额度体感竞争。
- **对谁 / 深读：** 工程/采购/评测 — **值得深读** 官方页与 system card；媒体「Astra 取消」作背景 **待核/报道**。
- **证据：** · [Introducing GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol) · [System Card PDF](https://cdn.openai.com/pdf/38e3efcf-545e-44cd-99ec-2b7eb395f4cc/oai_GPT_6_1_Sol.pdf) · [OpenAI 推文](https://x.com/OpenAI/status/2104986129686741046) · [OpenAIDevs 线程](https://x.com/OpenAIDevs/status/2104993035507712318) · [TechCrunch](https://techcrunch.com/2026/09/29/openai-launches-gpt-6-1-sol-says-it-nearly-matches-gpt-6-astra-and-costs-less/)
- **约时：** 2026-09-30 01:26–02:00 SGT（X）

### 3. OpenAI · Ultrafast + Pro 500
- **是什么：** 推出付费速度档 **Ultrafast**：Codex 上最高约 **8×** token 生成（宣传约 **300 tok/s**），API 约 **6×**；**GPT-6 Astra Ultrafast** 已在 API / ChatGPT Work / Codex 可用（Work/Codex 侧绑定 **Pro 500** 与 Enterprise）；**Sol Ultrafast** 即将跟进。新订阅 **Pro 500**（约 **$500/月**）含 Ultrafast 与约 **25× Plus** 用量；同时重开 **Pro 200**（额度结构与旧客 grandfather 不同，细节以官网为准）。
- **为何重要：** 把「延迟/吞吐」拆成独立 SKU，改变重编码用户的计费与产品分层。
- **对谁 / 深读：** 平台工程/增长 — **值得扫** [Ultrafast 文档](https://developers.openai.com/api/docs/guides/ultrafast-mode) 与定价表；非重度 Codex 用户可略。
- **证据：** + 官方自报 · [DevDay Recap](https://openai.com/index/devday-2026-recap) · [Ultrafast 指南](https://developers.openai.com/api/docs/guides/ultrafast-mode) · [OpenAI 推文](https://x.com/OpenAI/status/2104993966043320759) · [sama](https://x.com/sama/status/2104994601140711896)
- **约时：** 2026-09-30 01:57–02:00 SGT

### 4. OpenAI · Decisions API（Luna 约束选择）
- **是什么：** **Decisions API**（有限预览）：用 **GPT-6 Luna** 在开发者给定的封闭选项集上做实时决策（分类、路由、agent 下一步），输入可为文本/图像，输出为可选答案而非长生成；官方称未来数日扩大开放。
- **为何重要：** 把「高吞吐结构化决策」从通用 chat 拆成专用低成本原语，与 Liquid 等 decision-model 叙事对照。
- **对谁 / 深读：** API/agent 编排 — **值得扫** Recap + Dev 社区汇总；等完整 docs 再落地。
- **证据：** · [DevDay Recap](https://openai.com/index/devday-2026-recap) · [OpenAIDevs](https://x.com/OpenAIDevs/status/2105003318917697873) · [社区汇总](https://community.openai.com/t/devday-2026-announcements-and-developer-resources/1402006)
- **约时：** 约 2026-09-30 02:34 SGT（X）

### 5. OpenAI · Codex / 安全云与生态（DevDay 工程向）
- **是什么：** DevDay 同步强化 **Codex**（云端持续跑、CLI 刷新、PR/diff 审查、语音跟踪 agent 等）与 **Codex Security Cloud**（默认接入 cyber-capable 模型扫描 GitHub 仓、持续审 commit、去重并准备修复）；另有 **OpenAI Marketplace**（企业承诺额度可花到批准合作伙伴软件，首批约 32 家含 Figma 等）及 Today's News 所称 **Codex 原生支持开源模型**（如 GLM-5.3 Flash / Kimi K3）等——后者以官方/合作方帖为准再核。
- **为何重要：** 编码 agent 从「本机会话」扩到 **云持续执行 + 安全扫描 + 多模型/marketplace**。
- **对谁 / 深读：** 工程安全/企业采购 — **扫** Security Cloud 帖与 Recap；开源模型接入细节 待核 到官方 docs。
- **证据：** 官方自报 + 部分待核 · [OpenAI Security Cloud 帖](https://x.com/OpenAI/status/2104987422308335828) · [OpenAIDevs 开发者汇总线](https://x.com/OpenAIDevs/status/2105073596611830252) · [DevDay Recap](https://openai.com/index/devday-2026-recap) · Today's News：[开源模型+ModRetro](https://x.com/i/trending/2105014688845312370)
- **约时：** 2026-09-30 01:31–07:13 SGT

### 6. Anthropic · Claude Sonnet 5.5
- **是什么：** 发布 **Claude Sonnet 5.5**（Claude 5.5 家族第二款）：相对 Sonnet 5 官方称 **快 30%+**、多数任务 **成本可低至约 30%**（同价 **$2/$10** MTok，因更省 token）；Terminal-Bench 4.0 约 **70.6%**（Sonnet 5 约 10.3%）；1M 上下文；现已上 Claude API / Bedrock / GCP / Azure。Haiku 5.5 预告数周内。
- **为何重要：** 在 Opus 5.5 之后迅速补齐「日常工程/文档」中端；与 OpenAI Sol 6.1 同周对位。
- **对谁 / 深读：** 工程/产品 — **值得深读** 官方页与 system card；推文可略。
- **证据：** · [Anthropic 介绍页](https://www.anthropic.com/claude-sonnet-5-5) · [官方推文](https://x.com/AnthropicAI/status/2104633259925630995) · [平台文档](https://platform.claude.com/docs/en/models/sonnet-5-5/overview)
- **约时：** 文 2026-09-28；推文约 2026-09-29 02:04 SGT

### 7. Anthropic · GLM-5.3 先进网络能力扩散报告
- **是什么：** 研究文（**2026-09-29**）：评估智谱 **Z.ai / GLM-5.3** 开源权重模型可自主完成端到端 exploit 构建；相对 Claude Mythos Preview（限量 Glasswing）能力跃迁类似；关键是 **防护弱**——模拟中简单手段绕过率约 **64%–100%**，同测对受保护 Claude 未成功。NIST CAISI（09-17）已称其为迄今最强开源网络能力模型，约落后美前沿聚合指标 **4 个月**。
- **为何重要：** 把「网络能力前沿」从闭源限量计划拉到 **人人可下的权重**；影响红队、开源治理与防御方工具选择。
- **对谁 / 深读：** 安全/政策/对齐 — **值得深读** Anthropic 文 + CAISI；勿把评测数字当攻击教程。
- **证据：** · [Anthropic 研究文](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities) · [CAISI/NIST](https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities)
- **约时：** 文 2026-09-29；时间线中文摘要约 09-30 07:14 SGT

### 8. xAI / Elon · Grok 4.7 称 AA cyber index 第一
- **是什么：** Elon 发帖宣称 **Grok 4.7** 在 **AA cyber index** 排名第一（附榜图引用）；属官方账号自报与第三方榜，非本窗新模型发版。
- **为何重要：** 与 Anthropic「开源/闭源网络能力」叙事同周对照；需核榜单方法与是否含 safeguard-off 设定。
- **对谁 / 深读：** 安全评测 — **略读**；等独立复现再深。
- **证据：** 官方自报 · [Elon 帖](https://x.com/elonmusk/status/2105088792139014331)
- **约时：** 约 2026-09-30 08:14 SGT

---

## B. Today's News（X News 摘要 · 已标）

### 9. OpenAI DevDay：dots + GPT-6.1 Sol 等 — Today's News
- **是什么：** 多条 X News 汇总 DevDay：dots 常驻 agent、GPT-6.1 Sol、Ultrafast、Decisions API、Pro 500 等；与官方 Recap 一致的主干已核。
- **为何重要：** 社交层传播入口；细节以官网为准。
- **对谁 / 深读：** 可用作选题入口 — **略读 News，深读官网**。
- **证据：** Today's News · [Dots/Sol 故事](https://x.com/i/trending/2105042846617337932) · [另一则](https://x.com/i/trending/2104715411208237242) 见 A.1–A.4
- **约时：** News 更新至约 2026-09-30 00:18–00:36 UTC（≈08:18–08:36 SGT）

### 10. 泄露榜 · Gemini 4 Pro 基准 — Today's News（待核）
- **是什么：** 流传表格称 **Gemini 4 Pro** 在 DeepSWE / Terminal-Bench / OSWorld 等领先 Opus 5.5 与 GPT-6 Astra，并报 2M 上下文与较低价；**无 Google 官方确认**；Elon 曾社区注「Accurate (for now)」属二手语气。
- **为何重要：** 若真则改写定价/能力预期；当前仍是泄露叙事。
- **对谁 / 深读：** 战略/评测 — **可忽略或存档待核**；勿当 。
- **证据：** 待核 · Today's News：[故事 1](https://x.com/i/trending/2103861639732969673) · [故事 2](https://x.com/i/trending/2104571318385717755)
- **约时：** News 约 09-28

### 11. Liquid AI · d1 decision model — Today's News
- **是什么：** Liquid 宣称首个 **decision model d1**，称在 Hugging Face **Decision Index** 上首次超过 Jev；面向封闭选项/路由/分类的一次前向决策，非长文本生成。与 OpenAI Decisions API 同周出现，但产品形态不同。
- **为何重要：** 「决策专用模型」品类升温；数字以公司自报+News 为主。
- **对谁 / 深读：** 推理/路由栈 — **略读**；等官方博客/可复现榜再深。
- **证据：** 待核偏多（Today's News + 生态转发）· [News](https://x.com/i/trending/2105087279467532724) · HF 侧有 [huggingface 转推 liquidai](https://x.com/huggingface/status/2105036570717831396)
- **约时：** 约 2026-09-30 00:18 UTC News；HF 转推约 09-30 04:46 SGT

### 12. 其他 Today's News（略 / 可忽略）
- Claude 在 DevDay 当日短暂宕机（约 14:00–14:36 UTC）— 运维噪声。 
- Claude「attribution laundering」长文、Drone-Bench 作弊率下降、Muse 内装 Claude Code — 软信号/实验。 
- Oracle Fusion Claw 企业 agent runtime — 企业向，可另包。 
- Codex/Claude 额度体感切换 — **续** 09-27 软信号，无新硬事实则不扩写。

---

## C. 网页 补强

| 主题 | 判定 | 主链 |
| --- | --- | --- |
| dots 常驻 agent | | [openai.com/index/introducing-dots](https://openai.com/index/introducing-dots) |
| GPT-6.1 Sol | | [openai.com/index/introducing-gpt-6-1-sol](https://openai.com/index/introducing-gpt-6-1-sol) |
| DevDay 总览（20+） | | [openai.com/index/devday-2026-recap](https://openai.com/index/devday-2026-recap) |
| Ultrafast | | [developers.openai.com/.../ultrafast-mode](https://developers.openai.com/api/docs/guides/ultrafast-mode) |
| Decisions API | （预览） | Recap + [社区汇总](https://community.openai.com/t/devday-2026-announcements-and-developer-resources/1402006) |
| Claude Sonnet 5.5 | | [anthropic.com/claude-sonnet-5-5](https://www.anthropic.com/claude-sonnet-5-5) |
| GLM-5.3 网络能力扩散 | | [anthropic.com/research/glm-5-3-…](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities) |
| CAISI 对 GLM-5.3 评估 | （09-17，窗内被 Anthropic 引用） | [nist.gov/…/glm-53…](https://www.nist.gov/news-events/news/2026/09/caisis-assessment-zais-glm-53-cyber-capabilities) |
| GPT-6.1 Astra 未发 | 待核/媒体 | TechCrunch / WSJ 引述 |
| Gemini 4 Pro 泄露榜 | 待核 | 仅 Today's News / 社区 |
| Liquid d1 超 Jev | 待核（公司/News） | X News + HF 转发 |

---

## D. 窗外对照（不计入本窗新品）
- OpenAI agent 第三方数据/沙箱披露、Claude Nine Loops、Gemini Live Avatar GA、SmolDataEnvs、Epoch「思维价格」— **09-27 包主题，本窗无实质更新，不复述** 
- Claude Opus 5.5 / GPT-6 Sol·Astra / Grok 4.7 首发（约 09-21–22）— 本窗是 **Sol→6.1、DevDay 产品层、Sonnet 5.5、网络评测叙事** 
- Meta Muse（更早）— 可与 dots 对照，非本窗新发 

## E. 采集缺口
- Following 时间线近端 **2 页**主要覆盖 **09-29 晚–09-30 晨 SGT**（DevDay 后浪）；更早窗段（09-27–28）依赖官方 `search_posts_all` + News + 网页，未穷尽时间线全窗滚动（仍有 `next_token` 可再翻）。 
- `search_posts_all` 省略 `end_time`（近「现在」易 400）。 
- Anthropic **未**在检索到的官方帖中直接推送 GLM-5.3 文（以官网研究页为准）；Sonnet 5.5 有官方帖。 
- Google/DeepMind 本查询组合下无与 DevDay 同级的新 frontier 文本模型帖；Google Arts / Gemini 3.8 Flash TTS 等偏产品小更，未列入主条。 
- Liquid d1 缺稳定官方长文 URL（WebSearch 未命中 liquid.ai 专文）；标 待核。 
- WebFetch 对部分 openai.com 返回 403；已用 `curl` + 搜索摘要交叉核验。 

## F. 建议站内扩写候选（约 3–5）
1. **OpenAI dots**（常驻 agent：权限、云电脑、与 Muse 对照） 
2. **GPT-6.1 Sol**（近 Astra 性价比、缓存价、Work/Codex 可用边界；附 Astra 6.1 未发背景） 
3. **Claude Sonnet 5.5**（中端速度/成本与 Terminal-Bench 跃迁） 
4. **Anthropic GLM-5.3 网络能力报告**（开源权重 + 弱防护 vs Glasswing 限量） 
5. **Decisions API / Ultrafast / Pro 500**（开发者 SKU 与决策原语；可与 Liquid d1 短对照） 

可选略写：Codex Security Cloud、Marketplace、Gemini 4 Pro 泄露（仅待核追踪）


---

## 三、GitHub 素材

# GitHub 素材 · 2026-09-30

窗口：2026-09-27 09:00 → 2026-09-30 09:11（Asia/Singapore）

## 条目

### Ollama v0.35.0：本地 Decision Models（SystemOne）
- **人话一句：** Ollama 正式发布 v0.35.0，新增基于 TypeSafe Jev API 的 `/v1/systemone` Decision Models，返回选项、概率与置信度而非文本。
- **为何重要：** 把「分类 / 路由 / 工单分流」从生成式文本解析改成结构化概率输出，本地可跑（现提供 Nimble、Tev1），是本地 LLM 基建的新能力面。
- **对谁有用 / 深读建议：** 本地推理、Agent 路由、客服/工单分流；对照 release notes 里的三种题型（`choice` / `noul` / `score`）与库模型页。
- **证据：** [Release v0.35.0](https://github.com/ollama/ollama/releases/tag/v0.35.0)（published 2026-09-28 21:23 UTC ≈ 2026-09-29 05:23 SGT）· [Repo](https://github.com/ollama/ollama)

### Anthropic SDK：接入 Claude Sonnet 5.5 与 between_tools thinking
- **人话一句：** anthropic-sdk-python v1.9.0（及 TypeScript sdk-v0.129.0）同步加入 `claude-sonnet-5-5`、`between_tools` thinking，以及工具调用可与流式回复并行。
- **为何重要：** SDK 层正式暴露新模型与新 thinking 类型，是应用侧立刻可跟进的 API 契约变更；cache diagnostics 也标为 GA。
- **对谁有用 / 深读建议：** Anthropic 应用开发者、多工具 Agent；优先读 Python/TS changelog 中 Features 段，并核对模型 ID 与 thinking 类型。
- **证据：** [Python v1.9.0](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.9.0)（2026-09-28 18:03 UTC ≈ 2026-09-29 02:03 SGT）· [TypeScript sdk-v0.129.0](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/sdk-v0.129.0)

### OpenAI 新仓 mcp-extensions：ChatGPT 原生级 MCP 插件扩展
- **人话一句：** OpenAI 新建官方仓库 `openai/mcp-extensions`，提供把 MCP 插件做成 ChatGPT「一等公民」能力的 SDK 与规范（侧栏入口、文件扩展处理器、Composer @ 提及、扩展表单等）。
- **为何重要：** 官方把 ChatGPT 插件/MCP 扩展面开源成可安装的 TS/Python SDK，是平台侧插件生态的关键基建信号。
- **对谁有用 / 深读建议：** ChatGPT 插件 / MCP 开发者；从 README Showcase 进 `docs/spec.md`，再看 typescript/python 安装说明。
- **证据：** [Repo](https://github.com/openai/mcp-extensions)（created 2026-09-29 00:45 UTC ≈ 2026-09-29 08:45 SGT，窗口内约 225★）

### OpenAI Codex 0.159.0：可中途打断的终端编程 Agent
- **人话一句：** Codex 发布 rust-v0.159.0，新增可选 `instant_interrupt`，可在模型回复或长 code-mode 调用中用新输入改道，并改进欢迎屏、警告查看器与 Mermaid 渲染。
- **为何重要：** 终端编码 Agent 交互从「等跑完」升级为可实时改道，Windows 控制台/沙箱与 TLS 修复也偏生产向。
- **对谁有用 / 深读建议：** Codex / 本地 coding agent 用户；读 New Features 段与 full changelog 对比 `rust-v0.158.0...rust-v0.159.0`。
- **证据：** [Release 0.159.0](https://github.com/openai/codex/releases/tag/rust-v0.159.0)（2026-09-29 08:05 UTC ≈ 2026-09-29 16:05 SGT）· [Repo](https://github.com/openai/codex)

### firelex/jeff：Decision Model 微调开源仓（窗口内破千星）
- **人话一句：** 新仓 `firelex/jeff` 发布面向零样本分类的 Qwen3.5 / Gemma 4 小模型微调（Jev 同款请求格式），约一天内冲到 ~1033★。
- **为何重要：** 与 Ollama SystemOne / Decision Models 浪潮同窗出现，说明「小模型做结构化决策」正从闭源 API 扩散到可本地 fine-tune 的开源栈。
- **对谁有用 / 深读建议：** 本地分类/路由、想自训决策头的团队；对照 README 的 `/v1/systemone` 示例与 HF 上 Jeff-Qwen3.5-* 权重。
- **证据：** [Repo](https://github.com/firelex/jeff)（created 2026-09-28 16:18 UTC ≈ 2026-09-29 00:18 SGT）· 窗口末约 1033★ / 39 forks

### KKKKhazix/AIHOT：自托管 AI 热点日报框架（异常星标飙升）
- **人话一句：** 新仓 `KKKKhazix/AIHOT`（把信源与精选标准换成自己的就能做行业热点站）在创建约一天内冲到 ~3156★、908 forks。
- **为何重要：** 窗口内最显眼的 GitHub 星标异常；题材贴近 AI 资讯自动化，适合作为「社区热点」而非厂商 release 的对照项。
- **对谁有用 / 深读建议：** 想自建 AI/行业日报站的人；先读仓库描述与 topics（ai / llm / mcp / news-aggregator / rss / self-hosted），再核 README 架构。
- **证据：** [Repo](https://github.com/KKKKhazix/AIHOT)（created 2026-09-28 23:40 UTC ≈ 2026-09-29 07:40 SGT）· 窗口末约 3156★ / 908 forks



---

## 四、Hugging Face / 模型素材

# Hugging Face / 模型雷达素材包

- **窗口（Asia/Singapore）**: 2026-09-27 09:00 → 2026-09-30 09:11 SGT 
 （UTC 约 2026-09-27 01:00 → 2026-09-30 01:11）
- **火线日**: 2026-09-30 AI行业动态
- **采集时间**: 2026-09-30 09:14 SGT
 - `
 - `/workspace/daily-2026-09-30/packs/model.md`
- **原始证据**: ` HTML、org API、逐模型 `/api/models/{id}` JSON、README 摘录）

> 本包只给素材与可核验事实；**不编造**榜单分数。likes/downloads 为采集时刻 API 快照。卡片自称指标一律标 待核。 
> 相对上一火线包（`上一火线模型包`）：原「本窗更新」项若本窗无新的 `lastModified`，一律降为 **热度延续**，勿当头条。

---

## 本窗高信号（优先）

本窗内**官方新发稀少**：最硬的新发是小米 MiMo-V2.6 的 **MOPD 升级权重**；其余高信号主要是 **本窗更新**（TeleOCR、Ming-flash-omni、NVFP4 量化、决策分类器）。约 **4** 条可作主线。

### 1. [XiaomiMiMo/MiMo-V2.6-Flash-MOPD](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-MOPD)（及 [Pro-MOPD](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-MOPD)）— 本窗新发 · MiMo MOPD2 升级

- **人话一句**: 小米对已发布的 MiMo-V2.6-Flash/Pro-RL 再发 **MOPD** 检查点：多教师 on-policy 蒸馏（MOPD2）+ 专项压低 agent 场景下的 **tool-call 重复调用**。
- **为何重要**: 这是本窗少见的**大厂官方权重新卡**（非量化/Comfy 包装）；承接上一窗「MiMo-V2.6 家族刚发」叙事，从 RL 基座推进到可部署修复版。Flash 为 309B total / 15B active MoE；Pro 为 1.02T / 42B active（卡内宣称）。
- **对谁有用 / 深读建议**: Agent / 多模态长上下文产品、跟进小米开源路线的研究与评测。先读卡内 Technical Report §5.6 PDF 与 tool-call 技术博客；对照上一版 RL 卡的重复率图。
- （API 快照 2026-09-30 09:14 SGT）:
 - **Flash-MOPD**: createdAt `2026-09-27T04:01:00.000Z`（2026-09-27 12:01 SGT）← **本窗新发**；lastModified `2026-09-27T16:59:08.000Z`（2026-09-28 00:59 SGT）
 - likes: **42** · downloads: **2820** · pipeline: `text-generation` · license: `mit`
 - **Pro-MOPD**: createdAt `2026-09-27T03:58:00.000Z`（2026-09-27 11:58 SGT）← **本窗新发**；lastModified `2026-09-27T16:58:58.000Z`
 - likes: **20** · downloads: **763** · license: `mit`
 - 基座指向: [MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL) / [MiMo-V2.6-Pro-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)（窗前发布，见热度延续）
- 待核: 卡内 MoE 参数量、1M 上下文、重复率下降幅度、各 agent harness 对比；Technical Report / blog 中的数字。
- **链接**:
 - Flash: [huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-MOPD](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-MOPD)
 - Pro: [huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-MOPD](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-MOPD)
 - Tech report PDF（卡内）: [huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/bl…](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/main/MiMo_V2_6_technical_report.pdf)
 - Blog（卡内）: [mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repe…](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition)
 - GitHub（卡内）: [github.com/XiaomiMiMo/MiMo](https://github.com/XiaomiMiMo/MiMo)

### 2. [XingChen-AGI/TeleOCR](https://huggingface.co/XingChen-AGI/TeleOCR) — 本窗更新 · 轻量文档解析 VLM

- **人话一句**: 星尘/电信系开源的 ~1.2B 文档解析 VLM（原 NaviDC-OCR 更名），统一数字 PDF 与拍摄文档；本窗 Trending 前列且仓库有更新。
- **为何重要**: 本窗更新项里 **likes/曝光最高的非包装官方卡之一**；OCR/版面解析是 RAG 与办公自动化刚需，且有 arXiv + GitHub 可核。
- **对谁有用 / 深读建议**: 文档智能、财报/合同解析、手机拍题。对照 OmniDocBench / Wild_OmniDocBench；**卡宣称 SOTA 分数一律待核**。
- :
 - createdAt: `2026-08-14T06:15:03.000Z`（2026-08-14 14:15 SGT）
 - lastModified: `2026-09-29T00:30:57.000Z`（2026-09-29 08:30 SGT）← **落窗**
 - likes: **870** · downloads: **30354**
 - pipeline_tag: `image-text-to-text` · license: `apache-2.0`
 - tags: ocr, arxiv:2608.12898, transformers, safetensors
- 待核: 卡内各 benchmark / Dr.DocBench 名次与分数；「1.2B」参数与吞吐。
- **链接**:
 - 模型卡: [huggingface.co/XingChen-AGI/TeleOCR](https://huggingface.co/XingChen-AGI/TeleOCR)
 - arXiv（卡内标签）: [arxiv.org/abs/2608.12898](https://arxiv.org/abs/2608.12898)
 - GitHub（卡内）: [github.com/caipeng328/TeleOCR](https://github.com/caipeng328/TeleOCR)

### 3. [inclusionAI/Ming-flash-omni-2.0](https://huggingface.co/inclusionAI/Ming-flash-omni-2.0) — 本窗更新 · 开源 Omni MoE

- **人话一句**: inclusionAI 的 Ming-flash-omni 2.0（Ling-2.0 MoE：卡称 100B total / 6B active）仓库本窗有更新；定位多模态理解 + 语音/图像生成一体。
- **为何重要**: 相对「再发一个 chat LLM」，omni 合成线仍稀缺；与同系 Ming-Image 包装热度形成对照——本条是**原仓**而非 Comfy 重打包。
- **对谁有用 / 深读建议**: 多模态产品原型、音视频对话。读 GitHub Ming + arXiv；注意模型体积与部署成本。
- :
 - createdAt: `2026-02-10T06:57:15.000Z`（2026-02-10 14:57 SGT）
 - lastModified: `2026-09-29T03:43:27.000Z`（2026-09-29 11:43 SGT）← **落窗**
 - likes: **276** · downloads: **4929**
 - pipeline_tag: `any-to-any` · license: `mit`
 - tags: arxiv:2506.09344, arxiv:2510.24821, bailingmm_moe_v2_lite
- 待核: 卡/微信稿宣称的 SOTA 与各模态能力边界；与 Preview 的差异清单。
- **链接**:
 - 模型卡: [huggingface.co/inclusionAI/Ming-flash-omni-2.0](https://huggingface.co/inclusionAI/Ming-flash-omni-2.0)
 - arXiv: [arxiv.org/abs/2506.09344](https://arxiv.org/abs/2506.09344)
 - GitHub: [github.com/inclusionAI/Ming](https://github.com/inclusionAI/Ming) · [github.com/inclusionAI/Ling-V2](https://github.com/inclusionAI/Ling-V2)

### 4. [nvidia/GLM-5.3-Flash-NVFP4](https://huggingface.co/nvidia/GLM-5.3-Flash-NVFP4) — 本窗更新 · GLM Flash 官方 NVFP4 量化

- **人话一句**: NVIDIA Model Optimizer 对 [zai-org/GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) 的 NVFP4 预量化权重；面向 vLLM/SGLang 部署。
- **为何重要**: 本窗 downloads 过五万，是「大 MoE 多模态底座 → 可上线量化层」的典型信号；非新架构，但是**生产旁线**强证据。
- **对谁有用 / 深读建议**: 推理解耦、Agent/RAG 降本。对照 zai 原卡与 Model-Optimizer recipe；勿把量化卡当新模型头条。
- :
 - createdAt: `2026-09-02T20:37:17.000Z`（2026-09-03 04:37 SGT）
 - lastModified: `2026-09-29T21:30:12.000Z`（2026-09-30 05:30 SGT）← **落窗**
 - likes: **124** · downloads: **54435**
 - pipeline_tag: `image-text-to-text` · license: `mit`
 - tags: quantized, FP4, base_model:quantized:zai-org/GLM-5.3-Flash
 - 卡内宣称: 320B total / 18B activated（待核）
- 待核: 量化后精度掉点、吞吐对比、与 BF16 原卡的任务对齐。
- **链接**:
 - 量化卡: [huggingface.co/nvidia/GLM-5.3-Flash-NVFP4](https://huggingface.co/nvidia/GLM-5.3-Flash-NVFP4)
 - 原卡: [huggingface.co/zai-org/GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)
 - GitHub: [github.com/NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer)

---

## 次要 / 可并入旁线

### 本窗更新（垂直 / 中热度）

- **[fastino/GLiNER2.5-Decide](https://huggingface.co/fastino/GLiNER2.5-Decide)** — 340M 级「任意标签集」英文分类/路由（intent、sentiment、policy 等），非生成式；Trending 有曝光。 
 - createdAt `2026-09-23T14:56:12.000Z`；lastModified `2026-09-28T00:59:04.000Z`（2026-09-28 08:59 SGT）← **落窗** 
 - likes **241** · downloads **29199** · license `apache-2.0` · pipeline `token-classification` 
 - arXiv（卡内）: [arxiv.org/abs/2507.18546](https://arxiv.org/abs/2507.18546) · GitHub: [github.com/fastino-ai/GLiNER2](https://github.com/fastino-ai/GLiNER2) 
 - 待核: 卡内 fast-decisions 各域 exact-match；与 LLM 分类基线对比。

- **[microsoft/colipri](https://huggingface.co/microsoft/colipri)** — 胸部 CT 三维视觉–语言预训练；相对上一包再次更新。 
 - lm `2026-09-28T08:19:00.000Z`（2026-09-28 16:19 SGT）；likes **65** · downloads **3201** · license `mit` 
 - arXiv: [arxiv.org/abs/2608.00345](https://arxiv.org/abs/2608.00345) · **分数待核**。

- **[Qwen/Qwen3Guard-Stream-{0.6B,4B,8B}](https://huggingface.co/Qwen/Qwen3Guard-Stream-8B)** — 流式安全审核；三仓 lm 同落在窗初 `2026-09-27T02:00:*Z`（约 10:00 SGT）。热度低，适合安全旁线。 
 - 8B: likes **41** · dl **686** · license `apache-2.0` · GitHub: [github.com/QwenLM/Qwen3Guard](https://github.com/QwenLM/Qwen3Guard)

### 本窗新发（弱 · LoRA / 低下载）

- **[Lightricks/LTX-2.5-22b-IC-LoRA-Restore](https://huggingface.co/Lightricks/LTX-2.5-22b-IC-LoRA-Restore)** / **[…-Refine-Details](https://huggingface.co/Lightricks/LTX-2.5-22b-IC-LoRA-Refine-Details)** 
 - createdAt 落窗（09-27）；likes ≈10–11 · downloads **2**；IC-LoRA 视频修复/细节，基座标签指向 LTX-2.x。 
 - **信号弱**，可并入 LTX-2.5 视频旁线，勿当独立头条。README 主分支当时返回 401，细节待卡面补齐。

### 窗前刚发、近窗旁线（勿写成今日新发）

- MiMo-V2.6-*-RL / Distill：见热度延续表（窗前 09-21/22）。
- [apple/LensVLM-9B](https://huggingface.co/apple/LensVLM-9B)、[black-forest-labs/flux-3-action-base](https://huggingface.co/black-forest-labs/flux-3-action-base)：日期仍在窗外。
- [SupersonicLabs/Julia-1](https://huggingface.co/SupersonicLabs/Julia-1)：决策小模型，lm `2026-09-26T22:03:07Z` **未入本窗**；卡内自报准确率 待核。

---

## 热度延续（非本窗新发，勿当头条）

仍在 Trending / 高曝光，但 createdAt 与 lastModified **均在窗外**；含上一包已作「本窗更新」、本窗无新 lm 的项：

| ID | createdAt (UTC) | lastModified (UTC) | likes | downloads | 备注 |
|---|---|---|---:|---:|---|
| [Edge0/Audio8-ASR-Infinite](https://huggingface.co/Edge0/Audio8-ASR-Infinite) | 2026-09-21T15:03:21Z | 2026-09-24T03:39:57Z | 1528 | 23674 | 上包高信号 → 本窗降为延续 |
| [nvidia/Nemotron-3-Diarization](https://huggingface.co/nvidia/Nemotron-3-Diarization) | 2026-09-01T13:16:57Z | 2026-09-24T05:52:51Z | 519 | 30931 | 同上 |
| [Viggle/Qwen-Image-2.1-viggle-turbo](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo) | 2026-09-22T04:14:56Z | 2026-09-25T05:43:45Z | 425 | 190649 | 同上 |
| [Contrastive-LM/CLM-v0.1-8B](https://huggingface.co/Contrastive-LM/CLM-v0.1-8B) | 2026-09-21T20:09:04Z | 2026-09-24T21:37:19Z | 530 | 1910 | 同上 |
| [Qwen/Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1) | 2026-09-14T03:47:26Z | 2026-09-21T04:50:49Z | 2656 | 64362 | 图像主干 |
| [deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) | 2026-09-10T02:17:58Z | 2026-09-10T08:18:10Z | 3894 | 690388 | 多模态 MoE |
| [XingChen-AGI/Xing4.0-29B-A4B](https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B) | 2026-09-16T06:44:40Z | 2026-09-18T09:49:55Z | 1808 | 46557 | Trending 残留 |
| [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | 2026-08-05T08:22:59Z | 2026-08-14T15:00:01Z | 16565 | 7020239 | 长期热度 |
| [Qwen/Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | 2026-08-24T08:24:59Z | 2026-08-27T05:03:36Z | 5776 | 1222192 | 长期热度 |
| [Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) | 2026-07-23T07:55:24Z | 2026-09-01T06:29:03Z | 5563 | 1589098 | 视频主干；旁线靠新 IC-LoRA |
| [TaichuAI/ZDTaichu5.0-9B](https://huggingface.co/TaichuAI/ZDTaichu5.0-9B) | 2026-09-04T02:55:48Z | 2026-09-20T08:25:39Z | 1948 | 11836 | 多模态 |
| [Altworld/Hemmingway-1](https://huggingface.co/Altworld/Hemmingway-1) | 2026-09-20T12:10:31Z | 2026-09-22T16:48:00Z | 773 | 7880 | 创意写作微调 |
| [XiaomiMiMo/MiMo-V2.6-Pro-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL) | 2026-09-21T15:39:33Z | 2026-09-22T03:52:00Z | 600 | 78135 | MOPD 基座 |
| [XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL) | 2026-09-21T15:39:51Z | 2026-09-22T03:52:25Z | 519 | 39625 | MOPD 基座 |
| [XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B) | 2026-09-21T18:18:40Z | 2026-09-22T03:52:45Z | 571 | 11131 | 蒸馏旁线 |
| [apple/LensVLM-9B](https://huggingface.co/apple/LensVLM-9B) | 2026-09-21T18:18:20Z | 2026-09-22T21:06:26Z | 266 | 1956 | 文档 VLM |
| [yandex/AliceAI-Foundation-80B-A3B-Base](https://huggingface.co/yandex/AliceAI-Foundation-80B-A3B-Base) | 2026-09-12T10:32:07Z | 2026-09-22T11:12:04Z | 358 | 3876 | MoE base |
| [unsloth/Qwen-Image-2.1-GGUF](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF) | 2026-09-21T13:04:48Z | 2026-09-22T22:34:12Z | 299 | 251937 | 量化包装 |

---

## 刻意降权

| ID | 原因 | 快照 likes / downloads |
|---|---|---:|
| [abenzerps/Qwen-Image-2.1-Uncensored-GGUF](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF) | Uncensored / 魔改 GGUF；本窗有更新但不当头条 | 2439 / 1152523 |
| [pottokao/Qwen-Image-2.1-Text-Encoder-Heretic-GGUF](https://huggingface.co/pottokao/Qwen-Image-2.1-Text-Encoder-Heretic-GGUF) | Heretic GGUF | 322 / 168249 |
| [DavidAU/…Heretic-Uncensored…GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF) | Heretic/Uncensored 超长名社区 GGUF | 1281 / 1726231 |
| [prism-ml/Ternary-Bonsai-2-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf) | 三值量化社区包；卡宣称「intelligence %」等 待核 | 2267 / 3581027 |
| [convaiinnovations/laya](https://huggingface.co/convaiinnovations/laya) | likes 极高但 **downloads=0** | 4511 / 0 |
| [akhilaaa3/Jev-Omni](https://huggingface.co/akhilaaa3/Jev-Omni) | 社区合并决策叙事；下载偏低 | 310 / 923 |
| [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) / [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) | Comfy 包装仓；累计 downloads 常虚高 | 853 / 4.7M · 2049 / 22M |
| nvidia/SOMA-X · Kumo-* · cbottle · Tennis 等 | 本窗 touch 但 likes/dl 过低或 dl=0 | — |
| 全局个人 ckpt / likes≈0 | 噪声，已忽略 | — |

---

## 数据集（一笔带过）

轻扫 [datasets?sort=trending](https://huggingface.co/datasets?sort=trending) + 抽样 API：

- **[LocalLLaMA/typed-decisions](https://huggingface.co/datasets/LocalLLaMA/typed-decisions)** — lastModified `2026-09-29T20:55:13.000Z` ← **落窗**；likes **69** · downloads **17946**。与决策/路由模型旁线同题。
- **[FineEnvs/SmolDataEnvs](https://huggingface.co/datasets/FineEnvs/SmolDataEnvs)** — lm `2026-09-27T07:52:52.000Z` ← **落窗**；likes **60** · dl **2965**。
- **[XiaomiMiMo/MiMo-V2.6-RL-oss](https://huggingface.co/datasets/XiaomiMiMo/MiMo-V2.6-RL-oss)** — Trending 高曝光，但 created/lm 在 **09-25/26（窗外）**；likes **547** · dl **40036** — 可作 MiMo 旁线数据，**勿标本窗新发**。
- 其余 recent `sort=lastModified` 多为 likes=0 噪声仓，不展开。

---

## 采集备注

- 来源: HF Trending HTML（30 条 model article）+ 40 个重点 org 的 `api/models?author=&sort=lastModified&limit=15` + 逐 ID `GET /api/models/{id}`（本包引用 ID 均 HTTP 200）。
- 窗口判定仅用 API 的 `createdAt` / `lastModified`（UTC），文中附 SGT。
- THUDM / CohereForAI 列表 API 返回空数组（size≈2），无候选。
- Lightricks 两条 IC-LoRA 的 `/raw/main/README.md` 返回 401，描述仅依 API cardData/tags。
- 未编造任何 benchmark；卡内自称数字统一 待核。
- 证据目录: ` `orgs/*.json`, `models/*.json`, `api-snapshot.json`, `readme-snippets.json`, `datasets-*.json`）。


---

## 附录 A · arXiv 原始摘录

# arXiv raw pack — 2026-09-30 (SGT)

**Window:** announce ~Sun Sep 27 / Mon Sep 28 / Tue Sep 29 2026 (cs.AI / cs.CL / cs.LG) 
**Scraped:** Wed Sep 30 ~09:12–09:16 SGT 
**Prior pack:** Thu Sep 24 + Fri Sep 25 (excluded) 
**Selection:** 宁缺毋滥 — big-lab OR high-impact (RSI / agents / coding agents / frontier evals / scaling / safety). Affiliations checked on abs + HTML.

---

## Coverage note

| Source | What showed (Wed ~09:14–09:16 SGT) |
|--------|-------------------------------------|
| **`/list/.../new` (cs.AI)** | Still **Tuesday, 29 Sep 2026** only: New 456 / Cross 516 / Replacements 474. **Wed Sep 30 not announced yet** (do not include Wed). |
| **RSS `rss.arxiv.org/rss/cs.AI`** | `lastBuildDate` Tue 29 Sep 2026 05:12:51 +0000 (= **13:12 SGT**); `pubDate` Tue 29 00:00 −0400; **`skipDays`: Saturday + Sunday** → no weekend announce. |
| **`export.arxiv.org` Atom/API** | Used for id→`published` + metadata; aligned with pastweek day buckets (Mon batch often has Atom `published` ~Fri Sep 25 UTC = weekend queue → Mon announce). |
| **pastweek cs.AI** | **Tue 29:** 972 · **Mon 28:** 201 · **Fri 25:** 260 · (Sun 27 empty) |
| **pastweek cs.CL** | **Tue 29:** 392 · **Mon 28:** 89 · **Fri 25:** 126 |
| **pastweek cs.LG** | **Tue 29:** 1012 · **Mon 28:** 202 · (Fri not fully walked this pass) |
| **Sun Sep 27** | Empty (weekend; RSS skipDays). |

**Focus for picks:** Mon 28 + Tue 29. Wed 30 skipped (not visible before ~09:11).

---

## Picks (5)

### 1. 2609.35618 — From cacophony to hierarchy: a principled framework for assessing AI consciousness
- **Announce:** Tue Sep 29, 2026 (submitted 28 Sep 2026)
- **Authors / affiliations (HTML-verified):** Shamil Chandaria, Arvo Muñoz Morán, Fernando Rosas, Anil Seth, Henry Shevlin, **Marcus Hutter**, **Thore Graepel**, Adam Bales, Iulia Comsa, **Murray Shanahan**, Ruben Laukkonen, Morten Kringelbach, Chris Frith, **Shane Legg** — multiple authors marked **Google DeepMind / DeepMind Institute**, plus Oxford / Sussex / Cambridge / ANU / UCL / Imperial / etc.
- **人话一句：** DeepMind 一票意识/哲学+AI 大佬把「AI 有没有意识」从吵成一团的理论，收成可操作的五层功能描述层级，先谈映射问题再谈 hard problem。
- **Why important:** Rare big-lab + star-author (Legg / Shanahan / Hutter / Graepel) stance paper on AI consciousness assessment; frames pre-emptive governance/philosophy in an engineering-usable hierarchy (extends Marr).
- **Who should deep-read:** Safety/governance, consciousness/interpretability bridges, product policy on “AI sentience” claims.
- **Key metrics:** 概念框架论文，无标准 benchmark 分数 — （无定量主结果）· 五层 supervenience hierarchy / hard vs mapping problem — **官方自报（框架主张）**
- **Link:** [arxiv.org/abs/2609.35618](https://arxiv.org/abs/2609.35618)

### 2. 2609.35741 — Shockingly Simple Self-retrospection Improves Agentic Models Without RL
- **Announce:** Tue Sep 29, 2026 (submitted 28 Sep 2026)
- **Authors / affiliations (HTML-verified):** Jonathan Light (RPI; corr.), Christopher Zhang Cui (**UC San Diego**), Jeonghye Kim (**KAIST**), Roger Creus Castanyer / Emiliano Penaloza (**Mila**), Zhengyan Shi, Alessandro Sordoni, Marc-Alexandre Côté, Xingdi Yuan, Minseon Kim — **Microsoft Research**
- **人话一句：** 不要 RL：agent 做错/做对事后只写「回顾说明」，用回顾文本做 next-token 微调（ROFT），编码 agent 也能涨点还更省训。
- **Why important:** Minimal alternative to RL for agentic improvement; isolates explanation-only training; direct SWE-bench Verified/Pro numbers vs GRPO with less wall-clock.
- **Who should deep-read:** Coding-agent / SWE post-training teams; anyone comparing RLVR vs cheaper online fine-tunes.
- **Key metrics:**
 - SWE-bench Verified **49.2%** @ 20 ROFT updates vs GRPO **48.0%** @ 40 updates; SWE-bench Pro **29.0%** vs GRPO **25.3%** — **官方自报**
 - ~**63% less training time** than GRPO; 10-update ROFT **49.0%** Verified in **1.29 h** vs GRPO 40-update 48.0% — **官方自报**
 - 无 verifier 依赖（文中强调）— **官方自报** · 外推到他模型/他 bench — 待核
- **Link:** [arxiv.org/abs/2609.35741](https://arxiv.org/abs/2609.35741)

### 3. 2609.35706 — Reinforcing Agentic Creativity in Scientific Ideation with Night Science
- **Announce:** Tue Sep 29, 2026 (submitted 28 Sep 2026)
- **Authors / affiliations (HTML-verified):** Priyanka Kargupta (**UIUC**; *work completed while interning at Microsoft*), Silviu Cucerzan, Shweti Mahajan (**Microsoft**), Allen Herring, Jiawei Han (UIUC), Ryen W. White, Sujay Kumar Jauhar (**Microsoft Research**; corr. `sjauharmicrosoft.com`)
- **人话一句：** 微软把「夜科学」做成 RL 教出来的 ideation agent，故意离开低熵套路，让科研点子更野、更好引、更新。
- **Why important:** Big-lab agentic science ideation + RL for *creative departure* (not just correctness); ties cognitive “night science” to measurable citation/originality proxies.
- **Who should deep-read:** Research-agent / AI-for-science builders; eval designers worried about homogeneous LLM ideas.
- **Key metrics:**
 - vs base：研究意向多样性方向 **+27.8%**、贡献类型 **+14.9%** — **官方自报**
 - predicted citation impact 最高约 **+32.0 pp**；originality 最高约 **+66.2 points**（14B 档约 +32.03 / +66.15）— **官方自报**（代理指标，非真实引用）
 - 代理模型 citation 预测准确率等细节 — 待核（依赖其 citation predictor）
- **Link:** [arxiv.org/abs/2609.35706](https://arxiv.org/abs/2609.35706)

### 4. 2609.30652 — Recursive Self-Improvement via On-Policy Distillation for Reasoning
- **Announce:** Mon Sep 28, 2026 (Atom `published` 2026-09-25 — weekend queue → Mon list; primary cs.CL)
- **Authors / affiliations (HTML-verified):** Shangjian Yin, Zehao Zhao (*work done at Meta*), **Kavosh Asadi**, Rui Liu, Yuchen Lu, Shike Mei, Hang Cui, Luke Simon, Zhouxing Shi (UCR), **Hamed Firooz** — **Meta AI** + UC Riverside
- **人话一句：** Meta 用「自己当特权老师」的 on-policy 自蒸馏（再加 DCE+SRCL）做推理侧 RSI，不必死抱外部大老师。
- **Why important:** Explicit RSI framing from Meta FAIR-orbit; dense token-level self-distill path that claims huge lifts over OPSD/GRPO on math Avg12.
- **Who should deep-read:** Post-training / RSI / distillation for reasoning; teams allergic to heavy RL compute.
- **Key metrics:**
 - Qwen3-8B：**DCE+SRCL 65.97% Average12** vs **OPSD 30.35%** vs **GRPO 20.28%**；输出长度约 **−7.80%** vs OPSD — **官方自报**
 - Qwen3-4B：SRCL 等亦有增益（文中 60→61.88% 等）— **官方自报** · 是否泛化到非 math / 更大模型 — 待核
- **Link:** [arxiv.org/abs/2609.30652](https://arxiv.org/abs/2609.30652)

### 5. 2609.35606 — TCSAlgBench: Benchmarking Automated Proving for Research-Level Theoretical Computer Science
- **Announce:** Tue Sep 29, 2026 (submitted 28 Sep 2026)
- **Authors / affiliations (HTML-verified):** Chutong Yang (UT Austin; Amazon internship), Xiyuan Zhang (corr., **Amazon**), Yu Huang (Wharton; Amazon internship), Boran Han, Soonho Kong, Shuai Zhang, Vihang Prakash Patil, Zhen Han, Michael Bohlke-Schneider, Bernie Wang — **Amazon**
- **人话一句：** Amazon 用 STOC/COLT 2026 真论文定理做「研究级」自动证明与可核查评测，前沿模型五跑覆盖仍只有两成多。
- **Why important:** Frontier eval for research-level TCS proofs (not contest math); stress-tests discussion/sampling; exposes ceiling even for top proprietary configs.
- **Who should deep-read:** Frontier eval / autoformalization / theorem-proving agent teams; TCS+LLM researchers.
- **Key metrics:**
 - **398** theorem-level challenges from **138 STOC & COLT 2026** papers — （benchmark 规模，作者构建）
 - **GPT-5.6 Sol max** 十轮讨论后五跑 verifier-accepted coverage **23.6%**（94/398）；seed-1 **18.8%** — **官方自报**
 - 与 GPT-5.5 xhigh 等对比、题型诊断 — **官方自报** · 外部复现与 verifier 严格性 — 待核
- **Link:** [arxiv.org/abs/2609.35606](https://arxiv.org/abs/2609.35606)

---

## Near-misses（简记）

| id | note |
|----|------|
| **2609.35561** RSI-Master | 高相关 RSI + PostTrainBench **54.49 vs 46.53**、hacking **0%**、35B LiveCodeBench-v6 **41.21 vs Instruct 37.36**（官方自报）；单位 SJTU/CMU/Waterloo，非超大厂 — 主题强但本 pack 已有 Meta RSI + MSR agent，故近失。 |
| **2609.35641** VVR / RLVVR | UW（Zettlemoyer/Tsvetkov 线）可核查图像奖励；高影响题但非 big-lab。 |
| **2609.35692** Progressive Disclosure of Agent Skills | **Workday AI Research** — 中厂 agent skills，信号中等。 |
| **2609.31186** Evolutionary Safety of RSI | Mon 列表学术 taxonomy/风险；安全向但无大厂。 |
| **2609.30297** Spotify conversational rec agents | Spotify 大厂 + 线上 A/B（+14% listening 等，官方自报）；Atom published **Sep 16**，更像旧文进 Mon 列表/交叉，**不当作本窗口新 announce**。 |
| **2609.31076** 等 coding-agent 学术文 | 主题贴但 lab/冲击力未过线。 |

---

## Pack hygiene

- Affiliations：各文 HTML author/affiliation 块核对；DeepMind / MSR / Microsoft / Meta AI / Amazon 均有明文。
- Metrics：标 / **官方自报** / 待核；未把代理指标当真实引用。
- Wed 30：`/new` 仍为 Tue → 未收录。


---

## 附录 B · 实验室/官博原始摘录

# Labs Raw Notes — Window 2026-09-27 09:00 → 2026-09-30 09:11 Asia/Singapore (≈72h)

**Scanner:** executor subagent | **Written:** 2026-09-30 ~09:20 SGT 
**Prior pack (2026-09-27) already covered (do not re-include):** Gemini 3.8 Live Avatar; coherent long-form video / Co-Director; Project Suncatcher. That window had OAI/Anthropic/Meta/MSR ZERO.

**Method:** OpenAI news + RSS (`openai.com/news/rss.xml`); Anthropic newsroom; DeepMind blog + RSS; Google AI / innovation-and-ai / research.google/blog + RSS; Meta AI blog; MSR blog (WebSearch + curl, page 403); NVIDIA blogs.nvidia.com + developer.nvidia.com/blog. URLs verified HTTP 200 unless noted.

---

## 1. OpenAI

**Checked:** [openai.com/news/](https://openai.com/news/) (200), [openai.com/blog](https://openai.com/blog) (403 via WebFetch; news covers same), RSS [openai.com/news/rss.xml](https://openai.com/news/rss.xml) (200). DevDay 2026 = 2026-09-29 (Fort Mason / livestream).

### HIT — DevDay 2026 Recap (umbrella, 20+ launches)
- **Title:** DevDay 2026 Recap
- **URL:** [openai.com/index/devday-2026-recap](https://openai.com/index/devday-2026-recap) *(200)*
- **Date (SGT):** 2026-09-29 18:00 SGT (RSS `Tue, 29 Sep 2026 10:00:00 GMT`)
- **1-line CN:** DevDay 2026 一口气发布 20+ 项：Dots 常驻智能体、GPT-6.1 Sol、Ultrafast、Agents/Decisions API、Codex Cloud、ChatGPT Space/Pages、Private Intelligence、Pro 500 等。
- **Why it matters:** 年度开发者大会主发布；把「常驻 agent + 低价近旗舰模型 + 协作空间 + 企业私有推理」捆成一条产品线，是本窗口最高密度官方信号。
- **Key numbers:**
 - 20+ major announcements — **官方自报**
 - ChatGPT ~1.2B weekly users（开放插件分发面）— **官方自报**
 - Ultrafast：Codex 上最高约 **8×** 更快 token 生成（**300 tok/s**）；API 上最高约 **6×** — **官方自报**
- **Evidence quotes:**
 - “DevDay 2026 is our biggest yet, with more than 20 major announcements across ChatGPT, Codex, our models, and entirely new forms of working with AI.”
 - “Ultrafast offers up to 8× faster token generation (300 tokens per second) in Codex and up to 6x in the API.”

### HIT — Introducing GPT-6.1 Sol（模型发布）
- **Title:** Introducing GPT-6.1 Sol
- **URL:** [openai.com/index/introducing-gpt-6-1-sol](https://openai.com/index/introducing-gpt-6-1-sol) *(200)*
- **Date (SGT):** 2026-09-29 18:00 SGT (RSS `10:00:00 GMT`)
- **1-line CN:** GPT-6.1 Sol：在 agentic coding / computer use / 专业工作上接近 Astra，标准 I/O 价约为 Astra 的 1/5；API `$2/$10` per 1M in/out，缓存输入 `$0.10`。
- **Why it matters:** 把近旗舰能力下沉到工作负载默认价位；与 Anthropic Sonnet 5.5 同周对打「高性价比主力模型」。
- **Key numbers:**
 - 标准 API：`$2` / `$10` per 1M input/output；cached input `$0.10`（相对标准输入 **-95%**，相对 GPT-6 Sol 缓存价 **-50%**）— **官方自报**
 - DeepSWE v1.1：匹配 Astra、成本约 1/5；相对 GPT-6 Sol 最佳分 **+6.4 pp**（更低 reasoning effort）— **官方自报**
 - AutomationBench：相对 Opus 5.5 **+2.2 pp**（medium），约 1/3 成本；相对 GPT-6 Sol 同设置 **+4.8 pp** — **官方自报**
 - OSWorld 2.0 offline：相对 GPT-6 Sol **+7 pp**（max effort）；距 Astra **−2.1 pp**、约 1/7 成本 — **官方自报**
 - Terminal-Bench Science 0.1：max effort 均本 `$5.47`/task vs Opus 5.5 `$23.21` / Astra `$23.80`；Astra 仍最高分 **68.1%** — **官方自报**
 - 事实性（低 effort）：含事实错误回答占比 **11.4% → 7.7%**（约 **-32%**）— **官方自报**
 - API id：`gpt-6.1-sol`；ChatGPT Work/Codex 对 Plus/Pro/Business/Enterprise/Edu；**尚未进 Chat** — **官方自报**
- **Evidence quotes:**
 - “an upgrade to GPT‑6 Sol that nearly matches GPT‑6 Astra’s intelligence on agentic coding, computer use, and professional work at one-fifth of Astra’s standard input and output token prices.”
 - “Cached input costs just $0.10 per million tokens —95% less than standard input pricing…”

### HIT — Addendum: GPT-6.1 Sol Safety（系统卡附录）
- **Title:** Addendum to GPT-6 Astra System Card: GPT-6.1 Sol
- **URL:** [deploymentsafety.openai.com/gpt-6-1-sol](https://deploymentsafety.openai.com/gpt-6-1-sol) *(200)* 
 （新闻页亦有 “Addendum: GPT‑6.1 Sol Safety”，指向 Deployment Safety Hub）
- **Date (SGT):** Published **September 29, 2026**（页内；与 Sol 同日）
- **1-line CN:** 将 GPT-6.1 Sol 按预备框架定为网络安全 **Critical**、生化学 **High**，沿用 Astra 同款 safeguards 栈。
- **Why it matters:** 官方安全分级与评估附录；解释「低价近旗舰」仍走 Critical cyber 管控。
- **Key numbers / labels:** Cyber **Critical**；Bio/Chem **High**；safeguards = Astra stack — **官方自报**
- **Evidence quotes:**
 - “Under our Preparedness Framework, we are treating GPT-6.1 Sol as Critical in cybersecurity and High for Biological and Chemical capability.”
 - “GPT-6.1 Sol uses the same safeguards stack as GPT-6 Astra…”

### HIT — Introducing dots（常驻 Agent 产品）
- **Title:** Introducing dots
- **URL:** [openai.com/index/introducing-dots](https://openai.com/index/introducing-dots) *(200)*
- **Date (SGT):** 2026-09-29 08:00 SGT (RSS `Tue, 29 Sep 2026 00:00:00 GMT`)
- **1-line CN:** Dots：由 GPT-6 Astra 驱动的 always-on 智能体，自带云电脑，可连 4000+ 应用；先向 Pro / Business Premium / Enterprise（合规市场）滚动开放。
- **Why it matters:** OpenAI 消费/企业侧「常驻 agent」主赌注；与 Agents API / Space 形成闭环。
- **Key numbers:**
 - Powered by **GPT-6 Astra**；own cloud computer — **官方自报**
 - Plugins 生态 **4,000+** apps — **官方自报**
 - 可用性：Pro、Business Premium、Enterprise（eligible markets）；specialist dots preview — **官方自报**
- **Evidence quotes:**
 - “Dots are remarkably capable, always-on agents… Powered by GPT‑6 Astra, they have their own cloud computer…”
 - “Through our ecosystem of plugins, they can readily connect to over 4,000 apps…”

### HIT — Towards safety cases for frontier AI training（安全研究/流程）
- **Title:** Towards safety cases for frontier AI training
- **URL:** [openai.com/index/towards-safety-cases-for-fro…](https://openai.com/index/towards-safety-cases-for-frontier-ai-training) *(200)*
- **Date (SGT):** 2026-09-29 03:00 SGT (RSS `Mon, 28 Sep 2026 19:00:00 GMT`；页标 September 28, 2026)
- **1-line CN:** 主张继续做前沿 RL 训练前应具备结构化安全文档，并向「safety case」标准演进；覆盖 alignment / containment / monitoring。
- **Why it matters:** 把 pacing / 训练期治理写成可共享的最佳实践框架（非单次模型卡）。
- **Key numbers:** 定性框架为主；强调不可让自动 grader 看见 CoT（防监控规避）— **官方自报**
- **Evidence quotes:**
 - “We believe we are entering a new era in which structured safety documentation should be required before continuing any frontier reinforcement learning training run.”
 - “Prevent training on chain-of-thought: Do not let automated graders see the chain-of-thought in reinforcement learning…”

### SKIP（窗内但低信号）
- How we will do better for Australia（Company, Sep 28/29）— 地区政策沟通 
- Lenfest AI Collaborative expansion（Sep 28）— 公益资助 
- Are you a Codex Original?（form）— 营销征集 
- Basis tax workbook customer story（Sep 28）— 客户故事 

---

## 2. Anthropic

**Checked:** [www.anthropic.com/news](https://www.anthropic.com/news) *(200)*

### HIT — Introducing Claude Sonnet 5.5
- **Title:** Introducing Claude Sonnet 5.5 / Claude Sonnet 5.5
- **URL:** [www.anthropic.com/claude-sonnet-5-5](https://www.anthropic.com/claude-sonnet-5-5) *(200)*；新闻索引 [www.anthropic.com/news](https://www.anthropic.com/news)
- **Date (SGT):** **September 28, 2026**（页内日期；无精确到小时的 RSS）
- **1-line CN:** Claude 5.5 家族第二款：相对 Sonnet 5 输出更快约 30%+、多数工作最高可省约 30% 成本；价位仍 `$2/$10`；Terminal-Bench 4.0 **70.6%** vs Sonnet 5 **10.3%**。
- **Why it matters:** 主力「日常/中等复杂度」模型大幅跃升；首个带 cyber safeguards 的 Sonnet；与同周 OAI Sol 构成中端价位军备赛。
- **Key numbers:**
 - 定价：`$2` / `$10` / cache read `$0.20` per 1M（与 Sonnet 5 同价）— **官方自报**
 - 输出速度 **30%+** 快于 Sonnet 5；任务成本最高约 **-30%** — **官方自报**
 - Terminal-Bench 4.0：**70.6%** vs Sonnet 5 **10.3%**；Opus 5.5 **66.4%**（Xhigh）— **官方自报**
 - FrontierCode 1.1 Main：Max **46.2%** / Xhigh **52.1%** vs Sonnet 5 **42.4%** / Opus 5.5 **54.4%** / GPT-6 Sol **49.3%** — **官方自报**
 - CursorBench 4.0：**55.5%** vs Sonnet 5 **34.1%** / Opus 5.5 **57.8%** — **官方自报**
 - GDPval-AA v2.1：**1844** ≈ Opus 5.5 **1846**；Sonnet 5 **1449**；GPT-6 Sol **1487** — **官方自报**（注脚称预发布 structured-output bug 可能略低估）
 - OSWorld 2.1 partial：**80.1%** vs Sonnet 5 **57.0%** / Opus 5.5 **81.8%** — **官方自报**
 - API：`claude-sonnet-5-5`；AWS / GCP / Azure；ZDR — **官方自报**
 - Haiku 5.5「coming weeks」— **官方自报**
- **Evidence quotes:**
 - “It’s a clear upgrade over Claude Sonnet 5, runs 30%+ faster, and costs up to 30% less for most work.”
 - “Sonnet 5.5 scores 70.6% on Terminal-Bench 4.0… compared to Sonnet 5’s 10.3%.”
 - “it’s the first Sonnet model to launch with cyber safeguards and fallbacks like those we’ve developed for our most capable models.”

### OUT OF WINDOW（已见索引，不计入）
- Claude Opus 5.5 — Sep 22 
- Claude enzyme / CRISPR-like — Sep 23 
- Threat intel report — Sep 10 

---

## 3. Google DeepMind / Google AI / Google Research

**Checked:** 
- [deepmind.google/blog/](https://deepmind.google/blog/) *(200)* + RSS `deepmind.google/blog/rss.xml` 
- [blog.google/technology/ai/](https://blog.google/technology/ai/) *(200)* + [blog.google/innovation-and-ai/](https://blog.google/innovation-and-ai/) + [blog.google/rss/](https://blog.google/rss/) 
- [research.google/blog/](https://research.google/blog/) *(200)* + RSS `research.google/blog/rss`

### DeepMind blog — ZERO（窗内）
- RSS 窗内无新帖。最近：Live Avatar **2026-09-25 00:20 SGT**（prior pack）、Private AI memory **Sep 24**、TTS **Sep 23**、AlphaGenome Atlas **Sep 8**（[deepmind.google/blog/alphagenome-atlas-a-pred…](https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/）)。

### blog.google / technology/ai / innovation-and-ai — ZERO 高信号
窗内多为营销/客户故事（跳过）：Gemini 3.8 Flash builders（Sep 28/29）、grocer+Gemini、XPRIZE trailer、Arts & Culture、DV360、Henry Cavill Googlebook 等。无新模型/论文主发布。

### HIT — Google Research: Diffusion Controller
- **Title:** How Diffusion Controller unifies and simplifies AI image generation
- **URL:** [research.google/blog/how-diffusion-controller…](https://research.google/blog/how-diffusion-controller-unifies-and-simplifies-ai-image-generation/) *(200)*
- **Date (SGT):** 页标 **September 29, 2026**；RSS `Tue, 29 Sep 2026 18:38:27 +0000` → **2026-09-30 02:38 SGT**（仍在窗口截止 09:11 前）
- **1-line CN:** 提出 Diffusion Controller「转向阻尼」侧网络：冻结主干即可增强文生图 prompt 对齐；white-box 联合版对基线 HPS-v2 约 **90%** win rate。
- **Why it matters:** 统一 inference guidance 与 adapter 微调的控制论框架；可挂到灰盒/闭源图模。
- **Key numbers:**
 - White-box unlocked 版相对基线 **~90%** win rate — **官方自报**
 - 灰盒 Diffusion Controller 在 SFT/RWL 上可超过 LoRA（HPS-v2）— **官方自报**
 - Backbone 实验：Stable Diffusion v1.4；指标 HPS-v2 — **官方自报**
- **Evidence quotes:**
 - “a lightweight ‘steering damper’ network that precisely steers image generation to achieve significantly better prompt alignment.”
 - “its fully unlocked version… achieved a 90% win rate over the baseline model.”

**Note:** MarkTechPost 等报道 Google Cloud AI Research 开源 **RRSI**（agent harness 自改进，arXiv:2609.24972）约 Sep 29，但 **research.google/blog 无对应官方博文**；本 pack 不单列 lab 命中（可归 arxiv 渠）。

---

## 4. Meta AI

**Checked:** [ai.meta.com/blog/](https://ai.meta.com/blog/) *(200)*

### ZERO（窗内）
最新博文仍为 2026-07（Muse Spark 1.1 Jul 9、assistive robotics Jul 27、Genesis Mission Jul 21 等）。研究页另有 Sep 6/7/24 论文，但均 **早于** 窗口起点，且非 blog 主发布。

---

## 5. Microsoft Research

**Checked:** [www.microsoft.com/en-us/research/blog/](https://www.microsoft.com/en-us/research/blog/) — curl **403**；WebSearch 索引。

### ZERO 高信号（窗内）
- 索引可见 **Sep 28, 2026**「One year in: MSRA – Singapore…」周年综述（非模型/论文主发布）→ **跳过**。 
- RetroChimera（Sep 21）、Physical AI offload inference（Sep 23）→ **窗外**。 
- 无法稳定抓取 listing HTML；结论：窗口内无高信号研究/产品主帖。

---

## 6. NVIDIA

**Checked:** [blogs.nvidia.com/](https://blogs.nvidia.com/) *(200)* — 窗内无更新的 Featured（最新约 Sep 21–22 企业/展会稿）。 
[developer.nvidia.com/blog/](https://developer.nvidia.com/blog/) *(200)* — 多条高信号技术博。

### HIT — NVIDIA Open Agent Safety Platform
- **Title:** NVIDIA Open Agent Safety Platform: A Reference for Continuous In-Silicon Agent Monitoring
- **URL:** [developer.nvidia.com/blog/nvidia-open-agent-s…](https://developer.nvidia.com/blog/nvidia-open-agent-safety-platform-a-reference-for-continuous-in-silicon-agent-monitoring/) *(200)* 
 配套新闻稿：[investor.nvidia.com/news/press-release-detail…](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Launches-Open-Agent-Safety-Platform-to-Secure-Agents-From-Testing-to-Deployment/default.aspx) *(200)*
- **Date (SGT):** `datePublished` **2026-09-28T08:56:55+00:00** → **2026-09-28 16:56 SGT**；PR 标 September 28, 2026
- **1-line CN:** 开源 OpenShell（Vera CPU）+ BlueField-4 上 NVIDIA Sentry 的分层 Agent 安全参考架构：沙箱、策略证明、线速旁路监控。
- **Why it matters:** 硬件/运行时层面对「agent 逃逸与漂移」的产业级回应；与同周 OAI safety cases / DevDay 叙事共振。
- **Key numbers / labels:** OpenShell **Apache 2.0**；BlueField-4 位于节点通往模型的唯一路径上做 out-of-band 观测 — **官方自报**
- **Evidence quotes:**
 - “NVIDIA OpenShell (Apache 2.0) is an open source secure runtime for executing autonomous AI agents in sandboxed environments with kernel-level isolation.”
 - “In NVIDIA Vera Rubin POD systems, BlueField-4 DPUs sit on the node's only path to the model…”

### HIT — Add Runtime Controls… NVIDIA OpenShell 0.1.0
- **Title:** Add Runtime Controls to AI Agents with NVIDIA OpenShell
- **URL:** [developer.nvidia.com/blog/add-runtime-control…](https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/) *(200)*
- **Date (SGT):** `datePublished` **2026-09-28T08:55:00+00:00** → **2026-09-28 16:55 SGT**
- **1-line CN:** OpenShell 0.1.0：无需改写 agent 即可在工作负载外强制沙箱、服务访问、凭证隔离与形式化策略校验；兼容 Codex / Claude Code 等。
- **Why it matters:** OASP 的可落地运行时层；企业采纳叙事（Cadence / Slack / Gecko）。
- **Key numbers:** 版本 **0.1.0**；多租户 workspace；Docker/K8s drivers — **官方自报**
- **Evidence quotes:**
 - “NVIDIA OpenShell 0.1.0 is an open-source runtime for defining and enforcing which systems and data an agent can access.”
 - “It supports Codex, Claude Code, Pi, Hermes, and future frameworks…”

### HIT — DSX MaxLPS（AI Factory 功耗/吞吐）
- **Title:** How NVIDIA DSX MaxLPS Maximizes AI Factory Throughput and Efficiency
- **URL:** [developer.nvidia.com/blog/how-nvidia-dsx-maxl…](https://developer.nvidia.com/blog/how-nvidia-dsx-maxlps-maximizes-ai-factory-throughput-and-efficiency/) *(200)*
- **Date (SGT):** 列表标 Sep 27；`datePublished` **2026-09-28T01:00:00+00:00** → **2026-09-28 09:00 SGT**（落在窗口内）
- **1-line CN:** 策略化功率共享：同一批准功耗预算下最多可多部署约 **40%** GPU；Nscale 实测归一化总吞吐 **+49.2%**。
- **Why it matters:** 算力厂「瓦特→有效吞吐」基建信号，非营销故事。
- **Key numbers:**
 - 最高约 **+40%** GPUs / 同预算 — **官方自报**
 - 评测：GB300 NVL72 @ Nscale Verne；静态 **140** GPU → MaxLPS **192** GPU；功耗预算 **264.4 kW** — **官方自报**
 - 归一化聚合吞吐 **+49.2%**；tok/s/W **4.10 → 6.12**；P99 TTFT **+17%** — **官方自报**
- **Evidence quotes:**
 - “enabling customers to deploy up to 40% more GPUs within the same approved power budget.”
 - “DSX MaxLPS increased normalized aggregate throughput by 49.2%…”

### SKIP（窗内偏工程手册）
- AI Native by Design: TensorRT Model Connect（Sep 29） 
- VSS Blueprint 3.3 降本（Sep 29） 
- 更早：NV-Reason-CT（Sep 23）、Confidential Computing inference（Sep 22）等窗外或边缘 

---

## Curated shortlist（宁缺毋滥，7）

| # | Lab | Item | Date (SGT) | One-liner |
|---|-----|------|------------|-----------|
| 1 | OpenAI | **GPT-6.1 Sol** (+ DevDay Recap) | 09-29 18:00 | 近 Astra 智能、约 1/5 标准价；DevDay 枢纽模型 |
| 2 | OpenAI | **dots** | 09-29 08:00 | Astra 驱动常驻 agent + 云电脑 |
| 3 | Anthropic | **Claude Sonnet 5.5** | 09-28 | 中端主力大跃升；首个 cyber-safeguarded Sonnet |
| 4 | NVIDIA | **Open Agent Safety Platform / OpenShell 0.1.0** | 09-28 | 软硬一体 agent 运行时与旁路监控参考栈 |
| 5 | OpenAI | **Safety cases for frontier RL training** | 09-29 03:00 | 训练期结构化安全论证框架 |
| 6 | Google Research | **Diffusion Controller** | 09-30 02:38 (页 09-29) | 灰盒可控文生图侧网络；~90% win vs baseline |
| 7 | NVIDIA | **DSX MaxLPS** | 09-28 09:00 | 同功耗预算最高 +40% GPU；实测吞吐 +49.2% |

**未入 shortlist 但仍记 raw：** Sol Safety Addendum（并入 #1 安全侧）。

---

## Lab status summary

| Lab | In-window high-signal | Notes |
|-----|----------------------|-------|
| OpenAI | **YES** (DevDay cluster) | RSS+news 已核 |
| Anthropic | **YES** (Sonnet 5.5) | newsroom |
| Google DeepMind | **ZERO** | RSS 最近 09-25 Live Avatar（prior） |
| Google AI blog | **ZERO** high-signal | 仅营销/客户稿 |
| Google Research | **YES** (Diffusion Controller) | RSS |
| Meta AI | **ZERO** | blog 停在 7 月 |
| Microsoft Research | **ZERO** high-signal | 403；周年文跳过 |
| NVIDIA | **YES** (OASP/OpenShell/DSX) | developer blog |

**Hit count (high-signal raw entries above):** **10**（OAI×5 + Anthropic×1 + Google Research×1 + NVIDIA×3） 
**Curated shortlist:** **7** 
**Output path:** `/workspace/daily-2026-09-30/packs/labs-raw.md`
