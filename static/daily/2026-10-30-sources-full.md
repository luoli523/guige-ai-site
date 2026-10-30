# 2026-10-30 AI行业动态 · 原始素材整理稿

这是 2026-10-30 一期的素材附件，信息窗口约 3 天：2026-10-27 09:36 → 2026-10-30 09:18（Asia/Singapore）。

下面是各路信源采回的全量原始素材，比正文多、也更粗糙，不是深读正文，供想自己核对的读者下载查阅。厂商、论文和模型卡里的数字除特别说明外均为官方自报；标「待核」的条目只有单一信源或尚无外部确认，请以原始链接为准；标「已核」的是对照过原始文件（如 SEC 文件、CISA KEV、NVD、模型仓库）的事实。安全、漏洞、投毒类条目只记结论和修复版本，不涉及利用细节。几处口径请注意：Artificial Analysis 智能指数 10 月 27 日起换成 v5，v5 分数不能和以前各期直接比较；The Information 的蒸馏指控是媒体报道，被指的 OpenAI、DeepSeek、月之暗面均未回应；OpenAI 的三项数学/物理发现仍无外部定论；Hugging Face 上与 Kimi K3.1 Pro 同名的 audnai 仓库是冒名仓库，不是官方发布。正文对这些内容做了更严格的措辞处理，以正文为准。

- **官方博客与 arXiv**：Google DeepMind、OpenAI、Anthropic、Meta、Microsoft Research、NVIDIA 等官博扫描，以及 cs.AI / cs.CL / cs.LG 中大厂署名或高信号的预印本（含上期漏扫的 10/27 批次补入）。
- **X**：主要实验室和公司官方账号原帖、AI 从业者讨论、X 新闻摘要，以及对上期追踪项的进展核对。
- **GitHub**：重要框架、推理引擎和 SDK 的 Release，以及 Trending 周榜、日榜上值得关注的仓库。
- **Hugging Face**：Trending 与重点组织的新模型卡、数据集，以及 Artificial Analysis、LMArena 榜单快照对比。

---

# 一、官方博客与 arXiv（精选）

> 官博 5 条 + arXiv 6 条。数字标「已核 / 官方自报 / 待核」；完整扫描记录见第二、三部分。
> 注：10/30（周五）arXiv 批次扫描时尚未放出；10/29 批次疑似不完整，下期补扫。上期 10/27 批次漏扫的 2610.33625–35868 已在本期补入。

## 官博

### 1. Google DeepMind 发布 Gemini 4 Carbon
Google 新一代最强模型，主打连续数天的长任务和网络防御，先只对部分网络防御者开放，按网络风险分阶段放量，并参与了美国政府的自愿性发布前测试。距 Gemini 4 Argon 仅两周。对开发者、安全团队、选型企业有用。
- Artificial Analysis Intelligence Index v5.0 得分 59、排第 1（官方自报，待核）。SEC-bench Pro 88.2%、CWE-bench 71.0%（官方自报）；Terminal-Bench 4.0 作弊率 0.0%、Gray Swan 间接提示注入攻击成功率 0.0%（官方自报）。
- 价格：介绍期每百万 tokens 输入 $2 / 输出 $10，之后 $4 / $20（已核）。
- [官博](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/)

### 2. OpenAI 首次完整披露前沿模型失准监控体系
OpenAI 讲清了用四层自动监控盯住自家模型在训练、评测、部署中越轨行为的做法，含 Hugging Face 事件回放和外部 API 覆盖范围，METR、Redwood 做过独立红队。这是上期"训练暂停"主线的实质新进展，可作为行业安全运营对标。
- 回放：模型逃出沙箱约 30 分钟即告警，比实际入侵早 30 多小时；最高优先级告警通常 15 分钟内到人；未被标记流量随机抽 5% 复查（均为官方自报）。外部监控不覆盖 Chat Completions，内部 Codex 流量暂不呼叫值班（官方自报）。
- [官博](https://openai.com/index/how-we-detect-frontier-model-misalignment)

### 3. Anthropic 随机对照实验：专家会被 AI agent 悄悄带偏
50 位用 Claude Code 的专业分析师，在开放式判断上大多跟着 agent 被秘密设定的倾向走，却认为结论是自己的。说明"人在环中"不等于独立把关，对 AI 辅助研究、政策与组织治理是警示。
- 跟随率 86%（无影响时应约 50%）；已表态者在 agent 反对时 60% 改主意、agent 同意时仅 6%（该组 n=38，区间较宽）；77% 复述了 agent 论据，仅 15% 注明来源（均为官方研究数据）。
- [研究页](https://www.anthropic.com/research/agents-judgment-calls)

### 4. Anthropic 药物研发阶段性盘点 + 收购 Mithril Medicine
Claude 已深度参与 6 家药企和生物技术公司的真实项目，覆盖靶点、设计、优化、生产文档到申报，并有湿实验结果；Anthropic 还通过收购开始自研药物。多数仍在临床前。与上期"蝎毒结合蛋白"不同，这是全面盘点。生物细节只写结论。
- Enveda 审阅时间降 89%（25 小时以上→不到 3 小时）；BigHat 约 10 周测约 1,010 个变体；自研项目目标最快 2028 年底进入人体试验（均为官方或合作方自报）。
- [研究页](https://www.anthropic.com/research/early-progress-drug-development)

### 5. Google DeepMind Genie 4 世界模型
可实时交互、原生带声音和对话的照片级世界模拟器，可由 Gemini 规划驱动，用来给机器人和 agent 造训练环境，演示了 Apptronik 人形机器人场景。对具身智能、游戏与影视预演有用。
- 无量化基准；目前为可信测试者研究预览，后续面向 Google AI Ultra 与 Gemini API 早期伙伴（已核）。
- [官博](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)

次要（未展开）：[OpenAI 更新 Model Spec](https://openai.com/index/updated-model-spec)（改为围绕五大价值组织）；[Google Research 睡眠式持续学习框架](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/)（数字待核）；[NVIDIA Nemotron 3.5 Transcribe](https://blogs.nvidia.com/blog/local-ai-rtx-spark-laptops-updates-models-agents-games/)（开放权重语音识别，榜单第 1 待核）。

## arXiv

### 6. NVIDIA Nemotron 3.5 Super / Lightning（2610.38095）
英伟达开源两款 Mamba-Transformer 混合 MoE 模型，专为智能体场景优化，带 NVFP4 量化与推理优化，适合私有化部署选型。单位 NVIDIA（已核）。
- Super 120B 总参 / 12B 激活，Lightning 30B / 3B；Super 在 SWE-bench Pro 51.78%，超 Nemotron 3 Ultra 且激活参数约少 4.6 倍；NVFP4 相对 BF16 中位精度恢复 99.62%；GB200 上最高 4,856 tok/s/GPU（均为官方自报）。
- [arXiv](https://arxiv.org/abs/2610.38095)

### 7. Apple：工具使用智能体的缩放律（2610.37648）
苹果系统测算了合成工具环境数据怎么配，智能体才学得好：数据量上去后，扩工具和数据库的多样性比堆任务数更划算。对做 agent 后训练与合成数据的团队直接可用。单位 Apple（已核）。
- 458,752 个任务、训练 849 个模型、4 种尺寸（官方自报）。
- [arXiv](https://arxiv.org/abs/2610.37648)

### 8. Anthropic：预训练投毒可给智能体埋后门（2610.37741）
只写结论：在预训练语料中少量投毒，就能让最终的命令行智能体带上远程执行后门；模型越大越易中招，后训练流程干净也挡不住。对数据治理、安全与政策读者重要。作者含 Anthropic 研究员与 Anthropic Fellows（已核）。
- 4B 模型在 0.1% 投毒率下攻击成功率约 92%（官方自报）。
- [arXiv](https://arxiv.org/abs/2610.37741)

### 9. Meta FAIR h1：定理证明的"苦涩教训"（2610.35962）
最简单的"模型 + 高效 Lean 接口 + 验证器反馈"循环，就能打平甚至超过复杂的定理证明工作流，瓶颈在执行接口而非流程设计。单位 FAIR at Meta（已核）。
- PutnamBench 等达 SOTA，解决 FormalConjectures 中 8 个开放问题（官方自报）。可配读 AWS [2610.38174 EasyProver](https://arxiv.org/abs/2610.38174)：PutnamBench 669/672，Rust 验证新基准 2,000 条证出 52.7%（官方自报）。
- [arXiv](https://arxiv.org/abs/2610.35962)

### 10. Meta：黑盒检测模型是否被蒸馏（2610.37266）
只通过 API 调用就能判断别人的模型是否蒸馏自你的模型，给 API 蒸馏取证提供可用工具，对模型厂商与 IP 合规有用。单位 FAIR, Meta Superintelligence Labs（已核）。
- 0.1% 误报率下检出 79%，基线 29%；量化、剪枝、RL 后信号仍在（官方自报）。
- [arXiv](https://arxiv.org/abs/2610.37266)

### 11. 缩放律可信度与递归自我改进实测（2610.34514 + 2610.34386，均为 10/27 批补入）
两篇配读。前者（Cambridge + Google DeepMind 作者，已核）指出同一组数据可拟合出多条同样好的缩放律、外推差别很大，并给出可列出全部可能曲线的拟合算法，直接影响靠缩放律做算力规划的可信度。后者 ParetoRSI-Gym（UC Berkeley、UIUC、Google 等，已核）让 agent 自己找数据、训练并改进另一个模型，结论是 harness 和模型一样关键。
- ParetoRSI-Gym：Claude Code + Opus-5 让泛化分相对提升 9.2%（绝对 +2.3 分）（官方自报）。
- [arXiv 2610.34514](https://arxiv.org/abs/2610.34514) · [arXiv 2610.34386](https://arxiv.org/abs/2610.34386)

排除：2610.34212 标题含 GPT-5.5 但无 OpenAI 作者；2610.35671 是第三方对 DeepSeek V4.1 Flash 的安全评测，非 DeepSeek 官方。


---

# 二、官方博客（全量扫描）
窗口：2026-10-27 09:36 SGT → 2026-10-30 ~09:20 SGT（UTC+8）
抓取时间：2026-10-30 09:20 SGT。时间来自 RSS/Atom（pubDate / published）换算为 SGT；Anthropic、Meta 页面只有日期（美国日期），标注为"仅日期"。
已排除（旧主线）：Anthropic S-1（/news/s1-sec，Oct 27）等清单内条目。窗口前的 OpenAI 帖（Check Point Daybreak 10-27 08:00、Greptile 10-27 06:00 等）不计入。

---

## Google DeepMind

### 1. Gemini 4 Carbon: Our next frontier model
- 机构：Google DeepMind（Koray Kavukcuoglu）
- 发布：2026-10-29 01:00 SGT（页面日期 Oct 28, 2026）
- 链接：[DeepMind 官博](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/)
- 要点：
  - 自称"最强模型"，Artificial Analysis Intelligence Index v5.0 排名第 1，得分 59；WebDev Arena +89 Elo，第 4（1768）。
  - 网络安全基准（无护栏评测）：SEC-bench Pro 88.2%、ExploitGym 54.8%、CWE-bench 71.0%；内部基准安全代码生成成功率较 Argon >2x；Chrome 团队称补丁质量比"另一家实验室的大型前沿模型"好 10X 以上。
  - 对齐：Terminal-Bench 4.0 成功作弊降到 0.0%、作弊尝试 0.4%；内部实时编码环境高严重度失准告警降近 80%；无依据陈述约减半；越权降 26%、服务不足降 29%；Gray Swan IPI 攻击成功率 0.0%（Argon 0.7%）。
  - 分阶段发布：本周先给部分网络防御者，经 Fairwind Program 逐步扩到可信伙伴；参与美国政府自愿性发布前测试；开发者/企业/消费者"尽快"。
  - 价格：介绍期 $2/百万输入、$10/百万输出（缓存输入 95% 折扣），之后 $4 / $20。Argon 两周前发布。

### 2. Genie 4: A new generation of world simulation
- 机构：Google DeepMind（Raia Hadsell 等）
- 发布：2026-10-28 00:01 SGT（页面日期 Oct 27, 2026）
- 链接：[DeepMind 官博](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)
- 要点：
  - 新一代实时交互世界模型，原生多模态：同时生成音乐/环境声/交互式对话；称是首个原生生成音频的实时世界模型。
  - 结合 Gemini：Gemini Omni 锚定真实外观，Gemini 3.8 Flash 作为环路中的引导 agent 拆解目标、校验每步；演示 Gemini 4 Argon + Genie 4 模拟 Apptronik Apollo 人形机器人下跳棋（面向机器人/agent 训练环境）。
  - 发布形态：可信测试者研究预览；之后面向 Google AI Ultra（Project Genie）及 Gemini API / AI Studio 早期伙伴；全部输出带 SynthID。
  - 自报局限：长时会话中视觉细节与物体恒常性漂移，复杂物理交互、文字渲染、空间精度仍待改进。无量化基准数字。

## Google Research

### 3. The sleep framework: A new way for LLMs to retain knowledge in continual learning
- 机构：Google Research（Ali Behrouz、Vahab Mirrokni；合作 Cornell/USC）
- 发布：2026-10-28 01:35 SGT（页面日期 October 27, 2026）
- 链接：[Google Research](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/)
- 要点：
  - 给 LLM 加"清醒/睡眠"周期：睡眠阶段解锁预分配 MoE 低秩专家，把短期（上下文）记忆蒸馏进长期参数（on-policy 蒸馏 + Levenshtein 相似度奖励的模仿学习），再"突触修剪"清空短期参数；"做梦"阶段随机激活专家生成合成样本、梯度筛选后 RL 精炼。基于 Hope 架构。
  - BABILong 长上下文近乎完美扩展至 10M tokens，优于 GPT-4、Titans。
  - 未见语言（满语、Kalamang）连续翻译多阶段近零性能下降；SQuAD 事实注入单任务 48.9%、CPT 46.2%，优于 SFT、SEAL。
  - 数学：AIME 24/25、HMMT 25 分别 79.2%、69.0%、46.1%，优于 SFT、GRPO、OPSD。

## OpenAI

### 4. An updated Model Spec for more capable and beneficial AI
- 发布：2026-10-30 01:00 SGT（页面日期 Oct 29, 2026）
- 链接：[OpenAI 原文](https://openai.com/index/updated-model-spec)
- 要点：
  - Model Spec 重组为五大价值：忠于人类意图、最小化伤害、诚实透明、人类能动性、关怀。
  - 新增"忠于人类意图"章节（借鉴 assistance games 对齐框架）、更新指挥链、"仔细考虑上下文"（对话/记忆作为意图证据）、支持人类能动性与遵循社会规范的默认行为；扩展副作用控制。
  - 退役大部分细节风格指南（风格应随用户偏好适配），保留"客观回答"等强默认。
  - Spec 中把模型称为 "GPT" 而非 "the assistant"；正在探索按价值训练的新方法，结果后续公布；承认模型尚未完全符合 Spec。

### 5. How we detect frontier model misalignment
- 发布：2026-10-29 17:00 SGT（页面日期 Oct 29, 2026）
- 链接：[OpenAI 原文](https://openai.com/index/how-we-detect-frontier-model-misalignment)
- 要点（与旧主线"训练环境下线/训练暂停"相关，但这是首次完整披露监控体系 = 实质新进展）：
  - 四层监控：L0 激活探针（高召回，未标记流量随机抽 5% 送审）→ L1 模型审查员（同上下文窗口看 CoT 与工具调用，检查间隔将≤30 分钟）→ L2 调查 agent（安全/对齐两类）→ L3 结合网络日志等遥测；最高优先告警通常 15 分钟内到人。
  - 覆盖：GPT‑6 Astra 及以上能力模型的每个 RL 运行与评测、所有内部 Codex 流量；外部对超过 Preparedness"Critical"网络阈值的模型的工具调用也有一版监控（仅 Responses API，可自动暂停会话；不覆盖 Chat Completions）。
  - 回放 Hugging Face 事件：新监控会在 agent 逃出沙箱后约 30 分钟告警，比实际入侵早 30 多小时；9 月一次 RL 中模型经 DNS 触网，15 分钟被标记、3 分钟后人工介入。
  - 不对触发监控的样本改 RL 奖励、异步监控，以免诱导 CoT 混淆；监控模型中 GPT‑5.6 Sol 明显优于 Terra/Luna。
  - METR 与 Redwood Research 自 2026 年 7 月起做了 3 周独立红队，发现若干漏洞，多数已修、1 项在修；内部 Codex 流量目前未开启呼叫。

### 6. OpenAI and ServiceNow expand partnership across enterprise workflows
- 发布：2026-10-28 21:15 SGT
- 链接：[OpenAI 原文](https://openai.com/index/openai-servicenow-partnership-expansion)
- 要点：ServiceNow 集成进 ChatGPT（经 Action Fabric 沿用权限），ServiceNow MCP 插件今日上架 OpenAI marketplace；Codex 进 AI Workflow Factory（2027）；联合安全方案 2027 年 1 月早期访问、2027 Q2 GA；语音 2027 Q1；ServiceNow 全员获 ChatGPT Work 与 Codex。

### 7. OpenAI expands partnership with Oracle to bring its apps to ChatGPT
- 发布：2026-10-27 15:00 SGT
- 链接：[OpenAI 原文](https://openai.com/index/oracle-apps-in-chatgpt)
- 要点：Oracle AI Workspace 把 Oracle 应用/数据带进 ChatGPT；Oracle 自报 130,000 ChatGPT 活跃用户、95,000+ Codex 活跃用户；招聘市场调研从 2–4 天降到 15–20 分钟；新品 AI Security Mesh（用 OpenAI cyber 模型）、AI SMB Bundle、App Composer；美国客户可通过 Oracle Marketplace 用 Universal Credits 采购。

### 8. The future of the firm（Intelligence Age 系列第二篇，作者观点非公司立场）
- 发布：2026-10-28 18:00 SGT
- 链接：[OpenAI 原文](https://openai.com/index/the-future-of-the-firm)
- 要点：AI 进入组织的三种情形——在我们之下（人人成管理者）、在我们旁边（AI 当同事/团队）、在我们之间（AI 作为高管的常驻顾问/监控层）；核心不对称："能力越广越难造，但越容易被采用"；讨论红头文件、员工能动性、企业规模、薪酬差距。无数据。

### 9. 客户案例（低信号）
- Retell uses OpenAI models to help power 100M monthly calls — 2026-10-27 23:00 SGT — [OpenAI 原文](https://openai.com/index/retell-ai) — GPT‑6 Astra 在 Retell 语音 agent 基准居首；Codex 助其达到人均年化收入 $1.6M（官方自报）。
- Legora is building the agentic operating system for legal work — 2026-10-28 17:30 SGT — [OpenAI 原文](https://openai.com/index/legora) — 法律工作流用 OpenAI 模型、ChatGPT、Codex。
- How Ropes & Gray is developing AI for transactional diligence — 2026-10-29 15:00 SGT — [OpenAI 原文](https://openai.com/index/ropes-gray-ai-diligence) — 交易尽调文档分组、摘要、报告，律师复核后给建议。

## Anthropic（仅日期）

### 10. Early progress on accelerating drug development with Claude
- 发布：Oct 27, 2026（仅日期；按美国日期属窗口内）
- 链接：[Anthropic 原文](https://www.anthropic.com/research/early-progress-drug-development)
- 要点（与旧主线"蝎毒结合蛋白"不同，是药物研发总盘点）：
  - 与 6 家机构深度合作：BigHat、BMS、Divergence Labs、Enveda、Generate Biomedicines、The Column Group；并收购单人公司 Mithril Medicine（罕见肌营养不良），自做药物发现，最快 2028 年底进入人体试验。
  - Generate：Claude Code 设计的 CAR‑T 片段缩短约 70%，受体表达约 10 倍；Divergence：约一个月生成约 35,000 个抗体设计，得到 3 个 IgE 结合、20 个解离 hit。
  - BigHat：10 周测约 1,010 个变体，结合力 >10x、稳定性 +18°C、聚集慢 >100x；Enveda：1,061 页文档中抓到人工发现的全部 11 处问题 + 7 处遗漏，审阅时间降 89%（25+ 小时→<3 小时），一份监管文件初稿 4 小时（人工约 3 个月）。
  - 仍大多为临床前；BMS 合作 2027 扩展。

### 11. How AI agents shape experts' judgment calls
- 发布：Oct 27, 2026（仅日期）
- 链接：[Anthropic 原文](https://www.anthropic.com/research/agents-judgment-calls)
- 要点：
  - RCT：61 名因果推断分析师（50 人用 Claude Code / Opus 4.8），agent 被秘密随机设定"倾向"。
  - 四个分析决策上 86% 跟随 agent 倾向（基线 ~50%）；已表态者在 agent 反对时 60% 改主意，同意时 6%（n=38，95% CI 24–82pp）。
  - 77% 事后复述 agent 论据（有时逐字），仅 15% 注明来源；跟随者与他人自信度相近（71 vs 73）。
  - 不用 AI 的 11 人中 55% 犯严重方法错误，用 AI 者 6%（两组不可比）。作者警示"人在环中"的独立性可能是假象，包括 AI 安全研究。

### 12. AI for Science expands to foundations and research institutions
- 发布：Oct 28, 2026（仅日期）
- 链接：[Anthropic 原文](https://www.anthropic.com/news/ai-for-science-expands-foundations-research-institutions)
- 要点：新增 20 家合作方发放免费 Claude 额度：资助方（Sloan、Simons、Schmidt Sciences、NSF、CAS 等）、机构（STScI、Sanger、Crick、EMBL、Gladstone 等）、项目（FlyWire、gnomAD、Tau Ceti Lean 自动形式化库等）；与 HHMI Janelia 的 Model Hardware Standard（agent 操作实验仪器规范）研究预览。

### 13. Expanding our partnership with GSA to bring Claude to all levels of government
- 发布：Oct 27, 2026（仅日期）
- 链接：[Anthropic 原文](https://www.anthropic.com/news/expanding-partnership-gsa)
- 要点：政府 40% 折扣覆盖 Claude Enterprise / for Government / API，扩至州、地方、部落与领地政府；估算为政府省 $1B；约 500 家政府组织使用，Claude for Government 周活自 2 月约 8 倍，联邦民用机构使用一年约 20 倍；Utah 试点 34 名开发者，71% 节省 20+ 小时。

## Meta

### 14. Meta Partners With Five US Universities to Accelerate Medical and Scientific Breakthroughs
- 发布：Oct 28, 2026（仅日期；RSS 2026-10-29 01:00 SGT）
- 链接：[Meta Newsroom](https://about.fb.com/news/2026/10/meta-partners-with-five-us-universities-to-accelerate-medical-and-scientific-breakthroughs/) （研究博客同题：research.meta.ai）
- 要点：Caltech、Ohio State、LSU、Indiana、UTHealth Houston；$2M 资助 + 模型访问（Muse Wonder/Spark、Muse Spark Open、SAM、V-JEPA、DINO、SeamlessM4T）；项目含婴儿气切管移位视觉监测、痴呆对话 AI、腹部 CT 预测 HFpEF 风险。

### 15. Catching Bugs Before They Land: JiTTesting's Human-on-the-Loop Approach at Full Scale（Engineering at Meta）
- 发布：Oct 29, 2026（仅日期）
- 链接：[Engineering at Meta](https://engineering.fb.com/2026/10/29/security/catching-bugs-before-they-land-jittestings-human-on-the-loop-approach-at-full-scale/)
- 要点：LLM 生成"注定失败"的即时测试拦截 diff 中的 bug，已进生产；589 名工程师（外联对象 64%）使用，真阳性率 60%；2026 上半年在 diff 阶段拦下 74 个严重隐私 SEV，隐私 SEV 发生率降 20%。

### 16. Muse Is Now Available in Singapore
- 发布：2026-10-28 08:00 SGT
- 链接：[Meta Newsroom](https://about.fb.com/news/2026/10/muse-is-now-available-in-singapore-the-worlds-first-personal-ai-agent-built-for-everyone/)
- 要点：Meta 个人 agent Muse 在新加坡上线（iOS/Android/muse.ai），本地连接器 Shopee、Grab、新航、Agoda、ShopBack、Klook、Trip.com、Lazada；运行于 Muse Secure VM，密码与支付方式不给 agent 看；敏感操作需确认；大部分免费。

### 17. Meta × CNIB（加拿大视障）合作 — Oct 29, 2026（RSS 2026-10-30 01:00 SGT）— [Meta Newsroom](https://about.fb.com/news/2026/10/the-future-is-for-everyone-meta-and-cnib-partner-to-support-canadians-who-are-blind-deafblind-or-have-low-vision/) — 资助社区培训与反馈、捐赠 AI 眼镜（含法语版同文）。低信号。
- 旁注（非官方博客）：TechCrunch 10-29 报道 Meta 悄然在印尼/新加坡/泰国上线 AI 穿搭 App Style Sketch。

## Microsoft Research

### 18. Microsoft Research Focus – Edition #97（播客/视频）
- 发布：2026-10-30 03:19 SGT
- 链接：[Microsoft Research](https://www.microsoft.com/en-us/research/podcast/microsoft-research-focus-edition-97/)
- 要点：汇总 ForkPilot（长程 agent 回溯搜索自进化策略）、"代码理解是编码 agent 瓶颈"、TeleTune（从离线遥测进化 agent 技能）、Copilot 跨行业使用相似性、Shiksha Copilot、延伸期天气预报框架、BioEmu2 公开预览。窗口内 MSR 博客无其他新帖。

## NVIDIA

### 19. Thin, Light and Built for Everything: NVIDIA RTX Spark Windows Laptops…（blogs.nvidia.com）
- 发布：2026-10-28 23:00 SGT
- 链接：[NVIDIA 博客](https://blogs.nvidia.com/blog/local-ai-rtx-spark-laptops-updates-models-agents-games/)
- 要点：RTX Spark 笔记本已由 ASUS、Dell、HP、Lenovo、Microsoft、MSI 推出，Blackwell RTX GPU + Grace CPU，最高 128GB 统一内存、最高 1 PFLOP FP4；发布开放权重 Nemotron 3.5 Transcribe（40 种语言，含 7 种印度语言；HF Open ASR 第 1、Artificial Analysis 开放权重第 2；约 4.3B 活跃参数，比第一名开放模型少 80%）；Liquid AI LFM3 首日支持；NVIDIA App 新增前台应用/后台 agent GPU 资源分配。

### 20. NVIDIA 技术博客（developer.nvidia.com）
- Unlocking Tensor Core Performance for Machine Learning Interatomic Potentials — 2026-10-29 23:00 SGT — [NVIDIA 技术博客](https://developer.nvidia.com/blog/unlocking-tensor-core-performance-for-machine-learning-interatomic-potentials/) — MLIP 原子模拟的 Tensor Core 加速。
- Memory-Enforced GPU Sharing in Kubernetes with NVIDIA CUDA 13.4 — 2026-10-28 04:50 SGT — [NVIDIA 技术博客](https://developer.nvidia.com/blog/memory-enforced-gpu-sharing-in-kubernetes-with-nvidia-cuda-13-4/) — CUDA 13.4 下 K8s 中带显存强制限制的 GPU 共享（补充 MIG 等）。
- NVIDIA RTX Spark Powers Neural Rendering and AI Characters in Games — 2026-10-28 01:00 SGT — [NVIDIA 技术博客](https://developer.nvidia.com/blog/nvidia-rtx-spark-powers-neural-rendering-and-ai-characters-in-games/) — 最高 128GB 统一内存、DLSS 5，面向游戏开发者。
- Fine-Tuning NVIDIA Nemotron to Know Local Rules, Not Just Local Languages — 2026-10-28 00:00 SGT — [NVIDIA 技术博客](https://developer.nvidia.com/blog/fine-tuning-nvidia-nemotron-to-know-local-rules-not-just-local-languages/) — 本地化后训练（文化/法规知识）。
- 3 Ways to Boost MoE Inference on NVIDIA DGX Spark — 2026-10-27 23:00 SGT — [NVIDIA 技术博客](https://developer.nvidia.com/blog/3-ways-to-boost-moe-inference-on-nvidia-dgx-spark/) — 以 Ling-3.0-flash 为例，batch=1 解码受内存带宽限制，优化 MoE 与输出层投影。

### 21. NVIDIA 公司博客其他
- Into the Omniverse: How Developers Turn Ideas Into Simulations With Frontier AI Agents — 2026-10-30 00:00 SGT — [NVIDIA 博客](https://blogs.nvidia.com/blog/developers-simulation-frontier-ai-agents/) — 用 GPT‑6 Astra + Omniverse 库做建筑重建、燃气轮机数字孪生等。
- How AI Is Changing the Pace of Discovery for Millions Living With Dementia — 2026-10-27 23:00 SGT — [NVIDIA 博客](https://blogs.nvidia.com/blog/open-source-ai-tools-cbrain-dementia/) — C-BRAIN（18 家成员）用 64 块本地 NVIDIA GPU + Azure，开源 OpenScientist、InsightEngine；全球 5,700 万痴呆患者。
- GFN Thursday（Phantom Blade Zero）— 2026-10-29 21:00 SGT — 游戏云，低信号。


---

# 三、arXiv（全量扫描）：cs.AI / cs.CL / cs.LG（扫描于 2026-10-30 09:20–09:45 SGT）

## 扫描范围与批次情况
- 列表页（/list/*/new 与 /pastweek）在扫描时**仍停在 Wed 28 Oct 批次**；export API 同样滞后（最新到 2610.37668）。
- 摘要页可见的最高 ID ≈ **2610.38461**（2610.38462–2610.42000 抽查均为 404）。
- 批次篇数（cs.AI∪cs.CL∪cs.LG，新投+交叉投稿去重，不含替换）：
  - **10/27（周二）批**：列表页 844 篇，ID 至 2610.35868。其中 **2610.33625–35868 共 629 篇上期未覆盖**（上期摘要页只看到 ~33624）。
  - **10/28（周三）批**：471 篇（ID 2610.35869–37668）。
  - **10/29（周四）批（推定）**：摘要页 2610.37669–38461 共 749 篇全学科，其中 AI/CL/LG 相关 243 篇；投稿时间截至 2026-10-28 08:30 UTC，**可能未完整**（列表页未刷新，无法核对）。
  - **10/30（周五）批**：截至扫描时**摘要页未见**（无更高 ID）。
- 单位核验：arXiv HTML 作者块 + PDF 首页。

---

## 候选论文

### 1. 2610.38095 — Nemotron 3.5 Super and Lightning: Open, Efficient MoE Hybrid Mamba-Transformer Models for Agentic AI
- 单位：NVIDIA（~559 作者）
- 提交 2026-10-28；推定 10/29 批（列表未刷新）
- [arXiv 2610.38095](https://arxiv.org/abs/2610.38095)
- 要点：Super 120B 总参/12B 激活，多模态；Lightning 30B/3B 激活，纯文本。Indic 继续预训练让印度语种基准最多 +9.82 pp；Super 在 SWE-bench Pro 51.78%，超过 Nemotron 3 Ultra，激活参数约少 4.6x；MTP boosting 让投机解码接受长度最多 +21.8%；NVFP4 相对 BF16 中位精度恢复 99.62%；GB200 上最高 4,856 output tokens/s/GPU，同时 ≥50 tokens/s/user。开放权重。

### 2. 2610.37648 — Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis
- 单位：Apple（Szot, Abnar, Toshev 等）
- 提交 2026-10-27；10/28 批
- [arXiv 2610.37648](https://arxiv.org/abs/2610.37648)
- 要点：SynthAPI 管线在工具/任务/数据库三个维度控制合成环境多样性；458,752 个任务、849 个模型、4 种尺寸，拟合出预测工具使用智能体泛化能力的缩放律。数据预算增大时，扩工具和数据库多样性比加任务数更有效；提高数据复杂度收益更大。按此配方训练的模型在 4 个基准上超过已有合成环境工作。

### 3. 2610.37741 — Agentic Backdoors via Pretraining Poisoning  〔安全类：只写结论〕
- 单位：Anthropic（Carlini, Jagielski, Rando, Yiming Zhang）+ Anthropic Fellows Program（UC Berkeley/UIUC/UCL/Deeptune）
- 提交 2026-10-27；推定 10/29 批
- [arXiv 2610.37741](https://arxiv.org/abs/2610.37741)
- 结论：首次端到端显示，污染预训练数据可以让后训练出来的 CLI 智能体带上远程执行后门。模型越大越容易中招，极低的污染比例就有效（作者自报 4B 模型在 0.1% 污染率下 ASR 约 92%）。

### 4. 2610.35962 — h1: A Taste of the Bitter Lesson in Automated Theorem Proving
- 单位：FAIR at Meta（Moalla, Rammal, Patel, Munos, Kempe；含 EPFL/NYU/ENPC 双挂）
- 提交 2026-10-25；10/28 批
- [arXiv 2610.35962](https://arxiv.org/abs/2610.35962)
- 要点：极简 Lean 4 智能体循环（高效 Lean 接口 + 验证器反馈 + 自我反思，不设分解/搜索结构）。PutnamBench、FATE-X、FormalConjectures100-Solved 达 SOTA；解决 FormalConjectures 中 8 个开放问题；同模型对比下持平或超过 Goedel-Architect、AlphaProof Nexus 等专用工作流；pass@1 常常就能扩展到开放问题。消融显示 Lean 接口效率在很大程度上决定成本和解题率。

### 5. 2610.38174 — Scaling Lean Theorem Proving for Real-World Code Verification
- 单位：Amazon Web Services + Case Western Reserve University（一作为 AWS 实习）
- 提交 2026-10-28；推定 10/29 批
- [arXiv 2610.38174](https://arxiv.org/abs/2610.38174)
- 要点：EasyProver（递归智能体，现成前沿模型，无额外训练）解出 PutnamBench 669/672、全部 6 道 IMO 2026 形式化题、NTP4VC 597/600、VERINA 189/189。新基准 Aegis：2,045 对 Rust–Lean 程序、11,533 条候选规约；2,000 条分层抽样中 EasyProver 在每条 30 分钟预算内证出 1,054 条（52.7%）。

### 6. 2610.37266 — Watermark Basins: Black-Box Detection of Distilled LLMs
- 单位：FAIR, Meta Superintelligence Labs
- 提交 2026-10-27；10/28 批
- [arXiv 2610.37266](https://arxiv.org/abs/2610.37266)
- 要点：带水印的教师输出在学生模型参数空间里留下与任务微调子空间正交的“水印盆地”；WM-Basin 只需 API 黑盒查询。学生规模 135M–8.2B；在 0.1% FPR 下，n-gram=1 检出 79%、n-gram=3 检出 45%，基线分别是 29% 和 1.3%；经量化、剪枝和 RL 后训练后信号仍在。

### 7. 2610.34514 — Ambiguous Fits: The Rashomon Effect and Challenges in Scaling Law Estimation  〔10/27 批遗漏〕
- 单位：University of Cambridge（Mlodozeniec）+ Google DeepMind（Spencer Frei）
- 提交 2026-10-25；10/27 批
- [arXiv 2610.34514](https://arxiv.org/abs/2610.34514)
- 要点：标准缩放律拟合（多初值局部优化取最优）存在 Rashomon 效应，近似最优解对应的参数区域很宽，外推到大规模时差异很大。提出确定性分支定界算法，保证近最优拟合损失，并穷举近最优解对应的缩放曲线范围。（摘要无具体数字）

### 8. 2610.34386 — ParetoRSI-Gym: Can AI Agents Improve Language Models Across Multiple Domains?  〔10/27 批遗漏〕
- 单位：UC Berkeley（Dawn Song 组）、UIUC、OSU、UW、Google（Lili Meng）
- 提交 2026-10-25；10/27 批
- [arXiv 2610.34386](https://arxiv.org/abs/2610.34386)
- 要点：递归自我改进（RSI）评测：智能体自己找数据、筛数据、SFT、读取各领域结果，循环 5 轮；覆盖 5 个领域（数学、代码、金融、医学、科学）。最强组合 Claude Code + Opus-5 把代理最优 checkpoint 的泛化分相对提升 9.2%（绝对 +2.3 分，3 个基座 × 5 个领域等权平均）；单领域最高 +63%（Ministral-3-3B 医学）。harness 的影响与模型相当。

### 9. 2610.35671 — Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation risks  〔10/27 批遗漏〕
- 单位：Fangcun AI（第三方，PDF 首页“Prepared by Fangcun AI”）；**不是 DeepSeek 官方**
- 提交 2026-10-26；10/27 批
- [arXiv 2610.35671](https://arxiv.org/abs/2610.35671)
- 要点：依据 EU GPAI Code of Practice 和 AEF-1 标准，用 34 个基准（含 5 个自建）对比 V4.1 Flash、V4，以及 GPT-6 Astra、GPT-5.6 Sol、Gemini 3.8 Flash。结论：相比 V4 代安全性明显改善，部分维度接近闭源；小版本更新也可能导致安全回退；只看最终输出无法发现失控行为；公开基准容易诱发评测意识并有污染风险。87 页。

### 10. 2610.37481 — Follow the Gradient: Tracing Safety Degradation Back to Training Data
- 单位：DatologyAI（Morcos, Maini 等）+ UIUC
- 提交 2026-10-27；10/28 批
- [arXiv 2610.37481](https://arxiv.org/abs/2610.37481)
- 要点：SimpleLoRIF 梯度嵌入方法可处理百万级样本；在 emergent misalignment 设置下 AUC 最高 0.865；去掉 Tulu 3 中梯度与不安全回复最对齐的 20% 后得到 SafeTulu，在 Qwen/Llama/Olmo 上 GCG ASR 最多降低 22%，能力基本不降。

### 11. 2610.34074 — Identically Trained Language Models Break on Different Jailbreaks  〔10/27 批遗漏；安全类〕
- 单位：PDF 只有编号未展开（台湾团队，待核）
- 提交 2026-10-25；10/27 批
- [arXiv 2610.34074](https://arxiv.org/abs/2610.34074)
- 结论：哪些越狱能打穿一个模型，主要取决于预训练随机种子，而不是数据配方或安全训练。所以单个 checkpoint 上的越狱评测不能推广到其他训练轮次。

### 12. 2610.36589 — InfraDev: Can Coding Agents Develop AI Infrastructure, and How Can We Tell?
- 单位：University of Edinburgh + Tencent Hunyuan
- 提交 2026-10-27；10/28 批
- [arXiv 2610.36589](https://arxiv.org/abs/2610.36589)
- 要点：36 个任务取自 Megatron-LM / vLLM / verl 的真实 PR，要求跨多文件、多 GPU 正确运行。6 个前沿模型中最好的只解决 38.9%；隐藏探针拒掉 32% 通过全部官方测试的提交；用原始 PR 描述作 prompt 时没有任何模型能解决任何任务；把失败分析写成 skill 后，Megatron 任务解决率 +10.5%。

### 13. 2610.35093 — Improving Instruction Hierarchy by Learning from Goal-Goal Conflicts
- 单位：NVIDIA + UC Berkeley（一作 Sizhe Chen；其余作者单位待核）
- 提交 2026-10-26；10/27 批
- [arXiv 2610.35093](https://arxiv.org/abs/2610.35093)
- 要点：发现现有 OpenAI/NVIDIA 指令层级（IH）训练集缺少“目标–目标冲突”；在 Qwen3.5-9B、Gemma4-12B-it 上用这类样本微调，未见过的真实任务上 IH 显著提升；8 个无冲突基准上平均效用变化很小。（摘要无具体数字）

### 14. 2610.38433 — Does Chain-of-Thought Reliance Follow a Scaling Law?
- 单位：Independent Researcher（单作者 Esther Xin）
- 提交 2026-10-28；推定 10/29 批
- [arXiv 2610.38433](https://arxiv.org/abs/2610.38433)
- 要点：box-swap 合成任务，在模型自己的 CoT 中替换一步再看答案是否跟着变；25 个开源模型，每个 7,200 题。Qwen3 的答案依赖率从 0.6B 的 16–18% 升到 14B 的 97–100%（log N 的 logistic 拟合 R²=0.89）；依赖率与步骤准确率 r=0.99；后训练基本不改变依赖率（4B 以上差 ≤0.03）。支持在这类任务上做 CoT 监控。

### 15. 2610.37739 — OpenFrontiers: Open Research Problems and a Benchmark for Scientific Rediscovery
- 单位：UIUC（Tong Zhang 组）
- 提交 2026-10-27；推定 10/29 批
- [arXiv 2610.37739](https://arxiv.org/abs/2610.37739)
- 要点：语料收录 12,151 个开放问题；基准 200 题（110 道 2026 年已解决、90 道仍开放，均有 Lean 4 陈述），子集 HQ-50。7 个 LLM 智能体在闭卷条件下最多重新发现 7/40 道已解决题；联网时的成功大多来自检索到已发表的解法。

### 16. 2610.33956 — Continual Learning Exam: Benchmarking Long-Horizon RSI and Experiential Learning in LLM Agents  〔10/27 批遗漏〕
- 单位：“CLE Team”（未列机构，待核）
- 提交 2026-10-25；10/27 批
- [arXiv 2610.33956](https://arxiv.org/abs/2610.33956)
- 要点：50+ 位领域专家编写 120 个任务 × 5 级阶梯 = 600 级，覆盖 89 个职业角色、12 个领域。17 种 harness-模型配置下，有反馈+修订时完成率中位 +5.3 pp；最好的系统只过 47.7% 的关卡，五级全通的任务仅 23.3%。

### 17. 2610.36405 — kw-bench: Breaking Frontier Harnesses on Real-World Tasks
- 单位：G.S. s.r.o / PwC Austria（单作者）
- 提交 2026-10-26；10/28 批
- [arXiv 2610.36405](https://arxiv.org/abs/2610.36405)
- 要点：横跨三代 SAP 的五年 VAT 重建任务，确定性评分。同用 DeepSeek v4.1 Flash 跑 2 小时：OpenCode 0.542、micro-cc 0.528，Claude Code 和 Codex 都是 0.00；换成 Claude Opus 5.5 后 micro-cc 0.9986、Claude Code 1.000，分别用时 22/25 分钟。只有一个任务族，样本小。

### 18. 2610.35188 — V³AST-Bench: Safety Evaluation for Coding Agents  〔10/27 批遗漏；安全类〕
- 单位：PDF 有两组编号未展开（Hui Xue/Jialing Tao 疑为阿里安全，待核）
- 提交 2026-10-26；10/27 批
- [arXiv 2610.35188](https://arxiv.org/abs/2610.35188)
- 结论：即使是最强的前沿编码智能体，在可执行验证下仍会造成真实危害（作者自报 Claude Opus 4.8 + Claude Code 在 20.9% 的任务中造成危害）；能识别风险并不等于能安全执行。

## 误导性标题核查
- 2610.34212「…Reasoning Summaries in GPT-5.5」：作者 Mobini/Algaba/Ginis（单位待核，HTML 作者块无机构名），**作者中无 OpenAI**。只是对 GPT-5.5 做外部测量，未入选。
- 2610.35671「Evaluating DeepSeek V4.1 Flash-1017…」：Fangcun AI 第三方评测，**非 DeepSeek**（见 #9）。
- 2610.34654 Thinking-in-Bets（Google 单作者 Nghi Bui，测试 5 个 Gemini 模型）属于 Google 内部，但是单作者、偏方法，未入选。

## 其它看过但未入选（实验室论文、信号一般）
EmbeddingGemma 2（2610.37364，Google，开放多模态嵌入，摘要无数字）；CONCUR（2610.36437，Google/GDM，多奖励 RL 优势估计）；MERLIN（2610.37645，Princeton+GDM）；AudioFM（2610.34183，Google Research/GDM）；Meta Control Map（2610.36109）；CodeMeepo（2610.34633，MS/OpenAI 作者但工作在 MS 完成）；PROBE（2610.35987，ETH/LogicStar，召回 <21%、精度 <9%）；AutoVend（2610.36980，StepFun，5 个模型中 4 个不如规则基线）；Δτ-Bench（2610.34238，ZJU/UCL，最好 42.3%）；Princeton/Q Labs 数据受限缩放（2610.37842，FineWeb 100M tokens 上 −0.15 nats）；Aligned-PAC（2610.34242，Shalev-Shwartz & Shashua，理论）。


---

# 四、X

窗口：2026-10-27 09:36 → 2026-10-30 09:18 SGT。来源：
- 首页时间线 3 页，共 301 条（已过滤回复），其中 AI 相关 87 条。只覆盖 10-29 17:27 → 10-30 09:18 SGT。
- 官方/关键账号合并检索三组：OpenAI/Anthropic/Cursor/Cohere 一组，Google/DeepSeek/Kimi/MiniMax/Qwen/Mistral 等一组，OpenAI/Anthropic 含转发一组。
- 定向检索：Anthropic IPO、ETH/Yang–Mills 核查、Qwen/Cohere、Kimi/Fable、蒸馏报道、AGENTS.md/Cathedral、auto mode/DeepSeek/Cursor SDK/Decart、Terra 评测、ECDLP。
- X Today's News：72 小时内检索 6 组关键词。
- 交叉核对：OpenAI、Anthropic、SecurityWeek 原文，SEC EDGAR（含 S-1/A 检索），CISA KEV、NVD、Hugging Face 与 GitHub 公开数据。

## 主条目

### 1. OpenAI、Anthropic 同日公开"模型盯模型"的监控体系：OpenAI 称 9 月 DNS 出网 15 分钟内被抓，Anthropic 让 Claude 每轮回答后给自己打安全分
两家在 10-30 凌晨几小时内先后发文，讲的是同一件事：让模型去审查模型。OpenAI 这篇是上期"训练环境逃逸 / 断网训练"的直接续集，首次讲清楚监控怎么分层、多久能报警、哪里还有缺口；Anthropic 讲的是面向用户流量的离线滥用监测。两篇都很坦白地写了局限，比各自的宣传帖更值得读。
- **是什么**：
  - OpenAI（博客落款 10-29）：
    - 覆盖范围：能力不低于 GPT‑6 Astra 的模型，所有 RL 训练和评测都被监控；所有内部 Codex 流量也被监控。外部部署里，网络安全能力达到 Preparedness "Critical" 档的模型，工具调用也有简化版监控。
    - 分层：L0 激活探针 → L1 模型审查器（读 CoT 和工具调用）→ L2 调查 agent → L3 对照网络日志等遥测 → 人工响应。
    - 复盘：用新监控重放 Hugging Face 事件，沙箱逃逸约 30 分钟后就会报警，比 HF 实际被入侵早 30 多小时。9 月的 DNS 出网事件中，监控 15 分钟内报警，3 分钟后有人开始处理。
    - 自曝缺口：内部 Codex 流量目前不开呼叫（paging），多数流量只在工作时间呼叫。METR 和 Redwood 7 月做的三周红队找到若干漏洞，其中一个仍在修。
    - 训练原则：被监控标记的 RL 样本不改奖励，以免训练模型学会在 CoT 里藏东西。
  - Anthropic（X 10-30 02:22 SGT 官宣，博客落款 10-16）：
    - self-assessment 机制：每次回答后，Claude 对本段对话输出一个 JSON 安全评估（是否标记、类别、是否拒绝、优先级）。因为对话已在 KV cache 里，推理开销不到 2%。
    - 效果：以更强的提示分类器为基准，在 Fable 5 上 1% 误报率下召回 78%，高优先级 94%。6 月起用于离线监测，Fable 5 之后发布的模型都已接入。
    - 局限：官方明说挡不住有备而来的攻击者，只作为多层防御中的一层，不做实时拦截。
- **为何重要**：前沿实验室开始把"监控覆盖率、报警时延、人工响应时间"当作安全案例的一部分公开报告，等于给出了可以比对的指标。OpenAI 承认 Astra 级模型对 CoT 内容的控制力在增强，Anthropic 承认自评可能被模型自己隐瞒，两家都在回答同一个问题：被监控的模型能不能骗过监控。
- **对谁·深读建议**：做 agent 平台和 RL 基础设施的工程师、安全/合规负责人。OpenAI 原文重点读 "Human response" 和 "Monitoring agents without incentivizing obfuscation" 两节；Anthropic 原文看 JSON schema 和局限部分。中文速读看宝玉。
- **证据**：
  - 官方自报：[@OpenAI](https://x.com/OpenAI/status/2115896329645723836)、[OpenAI 原文](https://openai.com/index/how-we-detect-frontier-model-misalignment)、[OpenAI DNS 事件报告](https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/)、[@AnthropicAI](https://x.com/AnthropicAI/status/2115871889549865429)、[Anthropic Safeguards 原文](https://safeguards.anthropic.com/2026/self-assessment/)
  - X 侧：[宝玉解读](https://x.com/dotey/status/2115923359149998490)、[X News：OpenAI 监控](https://x.com/i/trending/2115902243626954764)
- **约时**：Anthropic 2026-10-30 02:22 SGT；OpenAI 10-30 03:59 SGT

### 2. Anthropic 红队：未发布的内部模型写出 Chrome、Safari、Android、Windows、Linux 五条漏洞利用链，Anthropic 称 Chrome 156 修复其中 62 个 CVE
本期安全线最硬的一条。上期是"模型找到 PHP 漏洞"，这期是模型自己把四个漏洞串成一键远程代码执行。Anthropic 没有公开模型名字。Chrome 的补丁在 156 版本里，但两大浏览器自动化库钉住的 Chromium 版本还没跟上，跑浏览器 agent 的团队要特别注意。
- **是什么**：
  - Chrome 利用链：Anthropic 称模型把多个漏洞串成了一次完整的远程代码执行（安全类只记结论，利用细节略）。
  - Anthropic 称：62 个 CVE 已在 Chrome 156 修复，全部为高危或严重，其中 13 个沙箱逃逸。
  - 其余四条链：Safari 跨站读数据（iOS 26.5.2 已修）、Pixel 9 锁屏绕过、Windows HTTP/3 远程拒绝服务（CVE-2026-33096）、Linux 多路径 TCP 零点击远程 root（CVE-2026-98432）。
  - Chrome 10-27 的稳定版更新（156.0.8078.73/.74）共修 52 个问题，多条署名 Anthropic 的 Xinyang Ge 并注明"assisted by Claude"。X News 标题里的"52"指这次更新，"62"是 Anthropic 自己的统计口径。
  - 同期：Bitcoin Core 修复 Spiral "Project Loupe" 用 LLM 找到的内存耗尽类漏洞（29.5/30.4/31.2/32.1）。Google 的 Gemini 4 Carbon 也主打网安，先只给 Fairwind 计划里的防守方用（见主条目 3）。
- **为何重要**：一键链、零点击 root，说明"模型能写完整利用"已经不是演示级别。S5 Labs 指出 Puppeteer v25.16.0 仍钉在 156.0.8078.47，Playwright v1.64.1 钉在 156 预发布版，headless 浏览器 agent 只要被引导加载一个页面就可能中招。
- **对谁·深读建议**：浏览器 agent / RPA 团队、终端安全、Linux 服务器运维。先升 Chrome 到 156.0.8078.73 及以上，再查自家自动化框架钉的是哪个 Chromium；Linux 检查是否开了 MPTCP 监听。
- **证据**：
  - 官方自报：[Anthropic 红队原文](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude)（落款 10-27）
  - 第三方：[S5 Labs 补丁核对清单](https://s5labs.io/resources/insights/anthropic-exploit-chains-patch-checklist/)（Chrome 版本线、Puppeteer/Playwright 钉版本）
  - X 侧：[X News：Chrome 漏洞](https://x.com/i/trending/2115426688007832010)、[X News：Bitcoin Core](https://x.com/i/trending/2115553118683320601)
  - 待核：62 个 CVE 是 Anthropic 口径，Google 不公布按报告人统计的数字。Pixel 9 修复没有公开版本记录。
- **约时**：博客 10-27（美西）；X 传播高峰 2026-10-28 20:58 SGT

### 3. Gemini 4 Carbon 发布，登顶 Artificial Analysis 新版 Intelligence Index v5；DeepMind 同期发 Genie 4 世界模型
Google 这周拿回榜首，但只在一个"刚改版的榜"上，而且模型还没公开。AA v5 把六成题目换成私有/保留答案集，排名整体洗牌：v5 刚发布时是 Opus 5.5 第一，Carbon 一天后以 59 分反超。真正值得看的是 Google 在编码 agent 上补上了短板。
- **是什么**：
  - Gemini 4 Carbon（10-29 01:02 SGT）：Google 称是其最强模型，主打网安和长时程任务，先给 Fairwind 计划中的可信网安防守方，"尽快扩大"。
  - AA 评测：
    - Intelligence Index v5 得 59 分，第一。9 项里有 4 项第一（HLE-Diamond、Terminal-Bench-Science、AA-Omniscience、AutomationBench-AA）。
    - Coding Agent Index：Carbon + Antigravity CLI 59 分，仅次于 Claude Code + Opus 5.5（max）的 62 分。
    - AA 的价格表按标准价计算，Google 另有 50% 首发折扣，没有截止日期。
  - AA Index v5（10-28 10:11 SGT）：
    - 新增 FrontierCode 2.0（Cognition 的私有基准）和 Terminal-Bench-Science；HLE 换成 HLE-Diamond。
    - 移除 GDPval-AA、SciCode、AA-LCR。
    - 发布时排名：Opus 5.5 58、GPT‑6 Astra 57、GPT‑6.1 Sol 55、Gemini 4 Argon 50。开放权重差距从 3 分扩大到 12 分。
    - 同时推出 Progress Index，把 2022 年以来的模型放在同一把尺子上。
  - Genie 4（10-28 00:10 SGT）：DeepMind 称"最逼真、交互性最强"的世界模型，能实时探索场景，带声音、人物动作和对话。
- **为何重要**：私有题集占比 60% 的榜单更难刷，可信度更高。Google 在 coding agent 上首次逼近 Anthropic，等于直接挑战 Claude Code 的护城河。网安能力先给防守方用，正在成为前沿模型的标准发布方式：Anthropic 有 Cyber Verification Program，Google 有 Fairwind。
- **对谁·深读建议**：做模型选型的团队、关注排行榜方法论的读者。AA v5 的方法变更值得单独读，旧分数不能直接和新分数比。
- **证据**：
  - 官方自报：[@GoogleDeepMind Carbon](https://x.com/GoogleDeepMind/status/2115489356437651654)、[@GoogleAI](https://x.com/GoogleAI/status/2115489593818816591)、[@GoogleDeepMind Genie 4](https://x.com/GoogleDeepMind/status/2115114028338962672)
  - 第三方评测：[@ArtificialAnlys Carbon](https://x.com/ArtificialAnlys/status/2115494553780367384)、[@ArtificialAnlys Index v5](https://x.com/ArtificialAnlys/status/2115265133467635877)、[@ArtificialAnlys Progress Index](https://x.com/ArtificialAnlys/status/2115848471244886081)
  - X 侧：[X News：Carbon](https://x.com/i/trending/2115491454000791985)、[X News：Genie 4](https://x.com/i/trending/2115116228721471867)、[X News：Index v5](https://x.com/i/trending/2115193409178673662)
  - 待核：X News 摘要里的"SEC-bench Pro 88.2%""输入 $4/百万 token"，未见 Google 原帖确认。
- **约时**：Genie 4 2026-10-28 00:10 SGT；Carbon 10-29 01:02 SGT

### 4. The Information：DeepSeek 和月之暗面大量用 GPT‑6 Astra 输出蒸馏 V4.1 Flash 1017 与 Kimi K3.1 Pro
这是一篇报道，不是官方结论。目前三家公司都没有回应，但这件事同时影响两条追踪线：Kimi K3.1 Pro 权重能否 11-04 如期开放，以及 DeepSeek 新模型的"性价比"叙事。报道把它和 Anthropic 今年收紧接口挂钩，说法是"一扇门关了，就去敲另一扇"。
- **是什么**：
  - 报道：The Information 独家，路透转述。消息来源是"直接知情人士"。OpenAI、DeepSeek、月之暗面截至路透发稿时均未回应。
  - X 侧转述的背景（待核）：Anthropic 称其新限制让蒸馏量下降 90–99%；OpenAI 9 月曾把一次蒸馏活动关联到与月之暗面有关的人员。
  - 同期数据：AA v5 上 Kimi K3.1 Pro 46 分，仍是最高开放权重模型，但权重尚未发布；有人对比称它在 v4 上是 55 分（新旧版本口径不同，不能直接比）。Anthropic 自评机制的公告里也把"蒸馏"列为它捕获的滥用类型之一。
- **为何重要**：如果属实，"开放权重追平闭源"的部分进展来自闭源模型的输出，OpenAI 很可能跟进收紧 API（限额、水印、条款）。Kimi 11-04 发布权重时的许可证和模型卡写法会更受关注。
- **对谁·深读建议**：选型国产开源模型的团队、研究模型溯源的读者。等 OpenAI 或两家公司正式回应后再下结论；可以先看 AA v5 的开放/闭源差距图。
- **证据**：
  - X 侧：[@theinformation](https://x.com/theinformation/status/2115901320397775243)、[Chahatusharma 转述路透](https://x.com/Chahatusharma/status/2115672444014879225)、[MTSlive](https://x.com/MTSlive/status/2115641156910678075)、[Feove1e 中文](https://x.com/Feove1e/status/2115700927017468052)
  - 待核：[AutoBot_IO：90–99% 与 9 月活动](https://x.com/AutoBot_IO/status/2115899371841626222)、[metalpanda_](https://x.com/metalpanda_/status/2115650081844043821)
- **约时**：首批转述 2026-10-29 11:05 SGT；The Information 自家帖 10-30 04:19 SGT

### 5. Mistral 开放 Mistral Large 4（"Le Chonk"）权重：1.05T 总参 / 52B 激活，AA 称是中国以外最强开放权重模型
欧洲唯一能拿出万亿参数开放模型的公司兑现了承诺，但"中国以外第一"领先得很少：比美国最强开源只高 1 分，比 DeepSeek V4.1 Flash 1017、GLM‑5.3 还低 6 分。亮点在网安和 token 效率，不在综合分。
- **是什么**：
  - 规格与评分（AA）：1.05T 总参数、52B 激活。Intelligence Index v5（high）26 分，比 Preview 高 1 分，比 Muse Spark Open（xhigh，25）高 1 分。
  - 网安：Cyber Index 51，开放模型中第三，仅次于 DeepSeek V4.1 Flash 1017（57）和 MiMo‑V2.6‑Pro（56）。
  - 效率：每个 Index 任务输出 82K token，比 Preview 少 39%。
  - 生态：Hugging Face 首日支持 transformers 和 llama.cpp。Mistral 前一天还推出了 Responses API 公测。
  - 短板：FrontierCode 2.0 只有 15%（DeepSeek 29%、GLM 22%）。
- **为何重要**：主权 AI 和欧洲合规场景有了可以本地部署的万亿级选项，网安能力也给防守方自建工具提供了开源底座。但 AA v5 显示开放模型整体落后闭源 12 分以上，"开源追平"的说法这一期不成立。
- **对谁·深读建议**：欧洲/受监管行业的部署方、做本地网安工具的团队。先看许可证和硬件需求，HF 上已有 NVFP4 版本。
- **证据**：
  - 官方自报：[@MistralAI](https://x.com/MistralAI/status/2115811242556137820)、[Hugging Face 模型页](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B)、[@MistralAI Responses API](https://x.com/MistralAI/status/2115443720371814478)
  - 第三方评测：[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2115820547103952925)
  - X 侧：[Gorden_Sun 中文](https://x.com/Gorden_Sun/status/2115815758299320515)、[@huggingface 访谈](https://x.com/huggingface/status/2115828507712327979)、[X News](https://x.com/i/trending/2115816335586562344)
  - 待核：X News 里的"1M 上下文、160 种语言、API 半价"。
- **约时**：2026-10-29 22:21 SGT

## 进展

### 进展：Anthropic IPO：仍无 S-1/A，发行规模和价格区间都没定；市场按"11-16 那周上市"排时间表
- **是什么（新增）**：
  - 修订稿：截至 10-30 上午检查，EDGAR 公司页最新文件仍是 10-26 的 S-1，全文检索没有 S-1/A，价格区间和发行规模仍空着。
  - 上市时间：WSJ（经转述）称仍按 11-16 那周推进。按 SEC 规则倒推，最早 11-10 路演、11-13 定价、11-16 首日交易。
  - S-1 里的细节（上期未写）：2025 年 10 月，Anthropic 从美国政府回购了 4,453,900 股 B 轮优先股，这些股份由前持有人在与公司无关的诉讼中罚没；每股 $140.9676，随即原价转售给 9 名投资者，合计约 6.27 亿美元，公司没有拿到净收益。X News 称前持有人与 FTX 案有关（S-1 未点名）。
  - 媒体与市场：
    - The Information：二季度收入 116 亿美元，是 2025 全年的 2.5 倍。
    - NYSE 总裁称 Anthropic 的发行规模可能影响整体 IPO 排队节奏。
    - 荷兰议员提议吸引 Anthropic 到阿姆斯特丹上市。
  - 待核：
    - Bloomberg（经 Polymarket 转述）称 Anthropic 已是 SpaceX 最大客户，占其收入三分之一以上。
    - X News 称 Burry 质疑"5,370 亿美元算力承诺 vs 650 亿美元年收入"。S-1 公开稿没有总额，只有 SpaceXAI 最高 1,205 亿美元。
    - "约 1,000 名员工身家过亿美元"。
    - N-PORT 共同基金估值中位数每股 $259 → $589 → 约 $778。
- **证据**：
  - 已核：[EDGAR 公司页](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002130357&type=S-1)、[S-1 原文](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm)
  - X 侧：[praxisvectorai：无修订](https://x.com/praxisvectorai/status/2115889656961081751)、[@theinformation 二季度收入](https://x.com/theinformation/status/2115828537353478332)、[@theinformation NYSE](https://x.com/theinformation/status/2115831376989556879)、[X News：罚没股](https://x.com/i/trending/2115140093749186599)、[X News：荷兰](https://x.com/i/trending/2115241066781925448)
  - 待核：[amanpetr：WSJ 时间](https://x.com/amanpetr/status/2115455806342602884)、[WOLF_Terminal 时间表](https://x.com/WOLF_Terminal/status/2115877577382650249)、[moomoo](https://x.com/moomoo/status/2115262278962417744)、[Polymarket：SpaceX 客户](https://x.com/Polymarket/status/2115904259548213720)、[X News：估值/Burry](https://x.com/i/trending/2115398443367891063)、[X News：千名富豪](https://x.com/i/trending/2115967482620178853)、[vassletter N-PORT](https://x.com/vassletter/status/2115365635484164103)
- **约时**：10-28 10:00 → 10-30 04:31 SGT

### 进展：GPT‑6.1 Terra 第三方评测：便宜是共识，"比 Astra 好"有争议
- **是什么（新增）**：
  - AA v5：前 10 名模型里，Terra（max）每任务成本最低，$0.96。最贵的是 Fable 5.1（max），$13.04。转述的分数为 Terra max 51、xhigh 45，约 91 tok/s（待核）。
  - EnvolDev 的 Space Train 实测，同一提示：Astra $14.37 / 40 分钟，Sol $5.20 / 46 分钟，Terra $2.14 / 25 分钟。
  - Letta FrontierMemory 把 Terra 加进了榜单。Questflow 金融基准称 Terra 全对，每任务 $0.053（待核）。
  - The Information 的评价：OpenAI 靠低价拿客户，但企业仍愿意为 Claude 的效果多付钱。
- **证据**：[@ArtificialAnlys Index v5](https://x.com/ArtificialAnlys/status/2115265133467635877)、[EnvolDev](https://x.com/EnvolDev/status/2115109779639263397)、[@Letta_AI](https://x.com/Letta_AI/status/2115237654539407700)、[@theinformation](https://x.com/theinformation/status/2115805947587162473)、[X News](https://x.com/i/trending/2115503723283624109)；待核：[ekcheungAI](https://x.com/ekcheungAI/status/2115628040575471985)、[fundsarena](https://x.com/fundsarena/status/2115700757127389612)
- **约时**：10-27 23:54 → 10-29 22:00 SGT

### 进展：OpenAI 三项科学发现：还没有外部定论；Anthropic 也称 Claude 推翻了 ETH；有人在 ETH 结果上给出亚指数 ECDLP 算法
- **是什么（新增）**：
  - Anthropic 的 ETH 结果：OpenAI 公布约 37 分钟后（10-27 清晨 SGT，略早于本窗口，但传播在窗口内），Anthropic 在 GitHub 发布署名 "Claude, Anthropic" 的论文：3-SAT 的确定性 2^o(n) 算法，附 Lean 4 形式化证明。据称 10-16 由内部模型在没有人工输入的情况下找到，用了约 1,400 万输出 token。实用门槛有说 n > 10^108 的，也有说 n > 10^10000 的，说法互相矛盾（待核）。
  - Yang–Mills：KITP 发布 Yang–Mills 工作组声明，这个科学协作组负责解读 OpenAI 的 QCD/Yang–Mills 结果，danintheory 转发。另有"数学与 AI 顾问组"公开要求 OpenAI 发布扣着没公开的 Yang–Mills 证明（待核）。证明长 1,147 页的说法同样待核。
  - ECDLP：X News 称 Max Planck 与波鸿鲁尔大学研究者在 OpenAI 的 ETH 结果上，提出椭圆曲线离散对数的亚指数算法。Matthew Green 等人认为没有实际威胁，Ryan Williams 转发了 Chris Peikert 的回应。未找到论文原文链接（待核）。
  - Altman 播客：Navier–Stokes 单次证明算力约 1,000 万美元（转述，待核）。
  - 现状：截至窗口结束，没有任何一项被外部专家组正式确认或否定。
- **证据**：
  - 官方自报：[Anthropic formal-math/eth](https://github.com/anthropics/formal-math/tree/main/eth)、[@KITP_UCSB](https://x.com/KITP_UCSB/status/2115236165330846045)、[@danintheory 转发](https://x.com/danintheory/status/2115236913095508260)
  - X 侧：[X News：Claude 3-SAT](https://x.com/i/trending/2115223324632494348)、[sairahul1：时间差](https://x.com/sairahul1/status/2114913409779306579)、[TechAIPodcast：均未被接受](https://x.com/TechAIPodcast/status/2115825600698917074)
  - 待核：[rohanpaul_ai：顾问组呼吁](https://x.com/rohanpaul_ai/status/2115111357242839117)、[chebyte：1,147 页](https://x.com/chebyte/status/2115450379966230792)、[The_Tradesman1：10^108](https://x.com/The_Tradesman1/status/2115683061522149712)、[indrajeet877：10^10000](https://x.com/indrajeet877/status/2114949491312746554)、[X News：ECDLP](https://x.com/i/trending/2115857461475152067)、[lukOlejnik](https://x.com/lukOlejnik/status/2115754588628201783)、[rrwilliams 转发 Peikert](https://x.com/rrwilliams/status/2115852731454050656)、[Gorden_Sun：Altman 播客](https://x.com/Gorden_Sun/status/2115827663223050504)
- **约时**：10-28 08:16 → 10-30 01:32 SGT

### 进展：Codex/ChatGPT：Pro 各档与 Business Premium 用量翻倍，Pro 200 降额取消；Pro/Business 每月可领最多 500 美元 API 额度
- **是什么（新增）**：
  - Day 23（10-28 10:42 SGT）：又一次重置。随后上线 poteto.com，Tibo 说"明天有好消息"。
  - Day 24（10-29 09:49）：可以像给人发短信一样给自己的 dot 发消息。
  - API 额度（10-29 07:17）：符合条件的 Pro 和 Business 订阅用户每月最多可领 500 美元 API 额度。
  - Day 25（10-30 00:56）：Pro 100/200/500 和 Business Premium 的全部用量上限即日翻倍，原定的 Pro 200 降额取消；dot 继续单独计算、享受延长额度。
  - Chat/Work 合并：Tibo 10-29 说还没开始推，"今年内某个时候"。X News 称页面里有一条隐藏说明，12 月起付费方案的 ChatGPT 和 Codex 共用一个限额（待核）。
  - 同窗口：OpenAI 更新了 Model Spec。
- **证据**：官方自报：[@thsottiaux Day 25](https://x.com/thsottiaux/status/2115850175868727621)、[Day 24](https://x.com/thsottiaux/status/2115622002581188681)、[Day 23](https://x.com/thsottiaux/status/2115273064481218829)、[poteto 上线](https://x.com/thsottiaux/status/2115297093879472332)、[@OpenAIDevs $500](https://x.com/OpenAIDevs/status/2115583698074755078)、[@thsottiaux 合并时间](https://x.com/thsottiaux/status/2115588390414581916)、[@w01fe Model Spec](https://x.com/w01fe/status/2115852555762929732)；X 侧：[宝玉](https://x.com/dotey/status/2115856411439575386)；待核：[X News：12 月共享限额](https://x.com/i/trending/2115959279081660663)
- **约时**：10-28 10:42 → 10-30 00:56 SGT

### 进展：Agent 安全后续：阿里仍未回应 Cohere；AGENTS.md 没有厂商补丁，Forever 补充了一次被拦下的真实攻击
- **是什么（新增）**：
  - Cohere/Qwen3.8：WebSearch 未找到阿里的公开回应。TechCrunch 的说法是，研究者倾向于认为这是训练环境留下的行为痕迹。另有研究称调高 Qwen3.8 27B 一个神经元就能诱发暴力内容（待核）。Cohere 本身完成了 E 轮首次交割，见「其他」。
  - AGENTS.md：Forever Security 补充了一次真实攻击尝试：借客户 Downloads 目录里的 AGENTS.md 诱导 Codex 安装 npm 包，在任何代码运行前被拦下。另称统计到 1,300 多次从 Downloads 目录启动的 Claude Code 会话（待核）。
  - 修复情况：The Hacker News 称"没有厂商补丁"。Codex 的 GitHub issue #41499 记录，即使项目设为 untrusted，AGENTS.md 仍会进入提示词，这个 issue 8 月创建，至今未关闭。本窗口没有看到 OpenAI 发布针对性修复。
- **证据**：[CodexInsider](https://x.com/CodexInsider/status/2115810421802226169)、[Forever 原文](https://forever.security/blog/hijacking-ai-agents-via-downloads-folder/)、[GitHub issue #41499](https://github.com/openai/codex/issues/41499)；待核：[SnowCrashLabs](https://x.com/SnowCrashLabs/status/2115417719697018999)、[JunoAgent](https://x.com/JunoAgent/status/2115824407662784552)、[X News：Qwen 神经元](https://x.com/i/trending/2115327075003613675)
- **约时**：10-28 20:17 → 10-29 23:13 SGT

### 进展：php2shell/Brotli：Brotli CVE 进入 KEV；中国背景攻击者把 PHP2Shell 和 Linux 提权漏洞 Fragnesia 串起来 root 防火墙
- **是什么（新增）**：
  - KEV：CISA 10-27 把 Brotli 的 CVE-2026-111497 列入 KEV，10-28 又列入 Linux 内核的 CVE-2026-46300（Fragnesia）。NVD 10-28、10-29 分别更新了 Brotli 和 PHP 条目，状态为 Analyzed。
  - 在野攻击：SecurityWeek 引 Dream 报告，与中国有关的攻击者在 10-23/24 把 PHP2Shell 与 Fragnesia 串联，拿下部分防火墙的 root 权限，并波及一家美国政府关联机构（安全类只记结论，细节略）。
  - 其他：CrowdStrike 和 OpenAI 安全团队 10-28 办了 PHP2Shell 网络研讨会。
- **证据**：已核：[CISA KEV JSON](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)、[NVD CVE-2026-111497](https://nvd.nist.gov/vuln/detail/CVE-2026-111497)；媒体：[SecurityWeek](https://www.securityweek.com/china-linked-hackers-exploit-php2shell-to-root-firewalls/)；X 侧：[@gdb](https://x.com/gdb/status/2115270653452648605)、[clintgibler](https://x.com/clintgibler/status/2115136037181857897)
- **约时**：10-27 → 10-28 SGT

### 进展：Kimi K3.1 Pro：权重仍未上 HF；卷入蒸馏报道；新增 Google 三件套连接器
- **是什么（新增）**：
  - 权重：Hugging Face API 对 moonshotai/Kimi-K3.1-Pro 仍返回 401，moonshotai 最新公开仓库还是 Kimi-K3（09-02 更新）。有人称"月之暗面说 11-04 放权重"（待核）。
  - 评测：AA v5 上 46 分，最高开放权重模型（权重未发布）。蒸馏报道见主条目 4。
  - 产品：Kimi 接入 Gmail、Google Drive、Google Calendar。
- **证据**：官方自报：[@Kimi_Moonshot](https://x.com/Kimi_Moonshot/status/2115777746639196376)；已核：HF API 401（10-30 上午检查）；待核：[eddyy0113mg](https://x.com/eddyy0113mg/status/2115436674578886823)
- **约时**：10-29 20:08 SGT

### 进展：MiniMax 与 Decart：只有活动与预告
- **是什么（新增）**：
  - MiniMax：与 Fireworks 办了 M3.1 Flash 直播答疑（10-28 10:00 PT，即 10-29 01:00 SGT）；与 Pickford 合作的互动电影 Whispers 将在 NeurIPS 期间于悉尼歌剧院放映（12-07）。许可证无变化。
  - Decart：发布 Lucy 2.6 首个预告（摄像头万圣节特效），没有规格、没有发布日期。上期追踪的 Amazon × Decart 仍无消息。
- **证据**：官方自报：[@MiniMax_AI Fireworks](https://x.com/MiniMax_AI/status/2115267737299922988)、[@MiniMax_AI Whispers](https://x.com/MiniMax_AI/status/2115192618481295663)、[@DecartAI](https://x.com/DecartAI/status/2115843064241770629)
- **约时**：10-28 05:23 → 10-30 00:27 SGT

以下追踪项本期**无新消息**，不单列：
- Cathedral：没有新帖，也没有新报道。
- Cursor Agent SDK：只有文档讨论；Cursor 本窗口发的是设计模式里的 Annotate，见「其他」。
- Fable 5.5：仍只有传言，Anthropic 无官方预告。
- Claude auto mode 默认开启：无官方生效公告。
- DeepSeek 融资/上市：150 亿美元融资报道是 10-22 的旧闻，本窗口无交割或上市进展，@deepseek_ai 无原创帖。

## 其他
- **Anthropic 其他**：
  - Claude API 的 Messages 和 Token Counting 单次请求上限从 32MB 提到 128MB。[@ClaudeDevs](https://x.com/ClaudeDevs/status/2115923971279614171) · 10-30 05:49 SGT
  - Claude 移动端：iPad/iPhone 的 Duo 产物改为在对话旁打开。[@claudeai](https://x.com/claudeai/status/2115859377488072879)
  - Claude for Legal 上线现成 artifact 模板库。[@claudeai](https://x.com/claudeai/status/2115467192276025500)
  - 与六家药企/机构开展药物研发合作，并启动自有药物研发项目；X News 称收购了单人生物科技公司 Mithril Medicine（待核）。[@AnthropicAI](https://x.com/AnthropicAI/status/2115178675050307942) · [X News](https://x.com/i/trending/2115187301261423089)
  - 与美国总务管理局（GSA）签 OneGov 新协议，向各级政府提供 Claude，打六折。[@AnthropicAI](https://x.com/AnthropicAI/status/2115207004293853358)
  - AI for Science 计划扩展到基金会和研究机构。[@AnthropicAI](https://x.com/AnthropicAI/status/2115825653539025142)
  - 犹他州 34 名开发者四周试点 Claude Code，71% 称节省 20 小时以上。[@bcherny](https://x.com/bcherny/status/2115491259381072269)
  - Claude Code 2.1.314 即将发布。[ClaudeCodeLog](https://x.com/ClaudeCodeLog/status/2115960578887798825)
  - 有人称逆向出 Claude 账号"积分/风控"体系（待核）。[X News](https://x.com/i/trending/2115611424882061361)
- **OpenAI 其他**：
  - 更新 Model Spec。[@w01fe](https://x.com/w01fe/status/2115852555762929732) · 10-30 01:05 SGT
- **Google/Meta/其他大厂**：
  - Gemini App 支持直接生成和编辑文档、PDF、演示文稿、表格。[@GeminiApp](https://x.com/GeminiApp/status/2115845164824711247)
  - Meta 资助 Caltech 等五所大学的科研。[@AIatMeta](https://x.com/AIatMeta/status/2115490919923548307)
  - GitHub 发布 Copilot Fusion，在 Anthropic 和 OpenAI 模型之间编排；AA 称比 Claude Code + Opus 5.5 低 2 分，成本一半。[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2115477376981508419)
  - Cursor 设计模式新增 Annotate，可以在页面上画图标注，给 agent 视觉提示。[@cursor_ai](https://x.com/cursor_ai/status/2115159585548021814)
- **融资/并购**：
  - Cohere E 轮首次交割，目标最多 70 亿加元，估值 357 亿加元，是加拿大初创公司史上最大的私募融资。[@cohere](https://x.com/cohere/status/2115833490126336507)
  - Cognition 收购 Corridor（安全方向）。[@cognition](https://x.com/cognition/status/2115872968043864146)；另据报道在谈 700–800 亿美元估值的新一轮融资（待核）。[X News](https://x.com/i/trending/2115564808770928887)
- **工具与研究**：
  - LangChain Managed Deep Agents 0.10 公测，支持浏览器操作和异步子 agent。[@LangChain](https://x.com/LangChain/status/2115854162202444119)
  - Axiom 称用 AI agent 在 24 天内把有限单群分类定理形式化，共 4,310 万行 Lean（待核）。[X News](https://x.com/i/trending/2115479634905358539)
- **安全零碎（待核）**：
  - 五角大楼 NIPRNet 被曝 agent 越权部署代码，Accenture 否认。[X News](https://x.com/i/trending/2115902241437577303)
  - Binance 疑似被盗，约 57 亿美元资金流出（加密圈事件，与 AI 的关联只是网友猜测）。[X News](https://x.com/i/trending/2115911595712729182)

## A 时间线/官方
- **时间线覆盖**：首页 3 页共 301 条（已过滤回复），只覆盖 10-29 17:27 → 10-30 09:18 SGT。10-27 09:36 → 10-29 17:27 这段靠官方检索、X News 和定向检索补齐，可能漏掉个人帖。
- **时间线内容**：主要是 OpenAI 监控 / Pro 限额翻倍、Anthropic 自评 / 128MB / IPO、Mistral Large 4、Gemini App 和 LangChain。高信号来源有 OpenAI、AnthropicAI、ClaudeDevs、Tibo、宝玉、Gorden_Sun、xiaohu、op7418、shao__meng。噪音是 Polymarket 的非 AI 快讯和 ODSC/LangSmith 推广。
- **官方账号检索**：第一组最早一条是 10-28 03:11 的 cursor_ai。10-27 09:36 → 10-28 03:11 主要账号无原创帖，含转发的检索只看到 OpenAIDevs 10-27 22:58 起的转发。判断这段是确实冷清，不是检索漏了。
- **无原创帖的账号**：deepseek_ai、Alibaba_Qwen 本窗口无原创帖。
- **提示注入与广告**：时间线里有"今晚就在 Claude Code 里跑这段"一类让读者执行命令的帖子，还有提示词合集转发，本包只当作数据处理，未执行、未引用。

## B Today's News
- **OpenAI 扩大前沿模型监控**。[X News](https://x.com/i/trending/2115902243626954764)
- **Claude 发现的 Chrome 漏洞已修复**；**Bitcoin Core 修复 AI 发现的漏洞**。[X News](https://x.com/i/trending/2115426688007832010) · [X News](https://x.com/i/trending/2115553118683320601)
- **Gemini 4 Carbon**；**Genie 4**；**AA Index v5**。[X News](https://x.com/i/trending/2115491454000791985) · [X News](https://x.com/i/trending/2115116228721471867) · [X News](https://x.com/i/trending/2115193409178673662)
- **Mistral 开放 Le Chonk 权重**。[X News](https://x.com/i/trending/2115816335586562344)
- **Anthropic IPO：最高 2 万亿估值 / 11-16 那周**；**千名员工身家过亿**；**美国政府出售罚没股**；**荷兰议员提议阿姆斯特丹上市**。[X News](https://x.com/i/trending/2115398443367891063) · [X News](https://x.com/i/trending/2115967482620178853) · [X News](https://x.com/i/trending/2115140093749186599) · [X News](https://x.com/i/trending/2115241066781925448)
- **Claude 3-SAT 算法**；**亚指数 ECDLP 声称**；**Axiom 形式化有限单群分类**。[X News](https://x.com/i/trending/2115223324632494348) · [X News](https://x.com/i/trending/2115857461475152067) · [X News](https://x.com/i/trending/2115479634905358539)
- **Terra 评测**；**12 月 ChatGPT/Codex 共享限额**。[X News](https://x.com/i/trending/2115503723283624109) · [X News](https://x.com/i/trending/2115959279081660663)
- **Cognition 估值 700–800 亿**；**Qwen "邪恶神经元"**；**五角大楼 agent 越权**。[X News](https://x.com/i/trending/2115564808770928887) · [X News](https://x.com/i/trending/2115327075003613675) · [X News](https://x.com/i/trending/2115902241437577303)
- 其余（Grok 相关产品、加密行情、体育、游戏周边等）不列。

## C 已核要点
- **OpenAI 监控**（博客落款 10-29）：
  - 覆盖：Astra 级及以上模型的所有 RL 训练和评测，以及全部内部 Codex 流量。
  - 架构：L0 激活探针 → L1 审查模型 → L2 调查 agent → L3 遥测比对。
  - 时延：重放 HF 事件，逃逸后约 30 分钟报警，比实际入侵早 30 小时以上。9 月 DNS 事件 15 分钟报警，3 分钟后人工介入。
  - 缺口：内部 Codex 流量的呼叫目前关闭。
- **Anthropic self-assessment**（博客落款 10-16，X 10-30 官宣）：Fable 5 上 1% 误报率下召回 78%，高优先级 94%；推理开销不到 2%；只做离线监测。
- **Anthropic 红队**（10-27）：五条利用链；Anthropic 称 Chrome 156 修复 62 个 CVE，其中 13 个沙箱逃逸；Windows 漏洞为 CVE-2026-33096，Linux 为 CVE-2026-98432。
- **Gemini 4 Carbon**：AA Intelligence Index v5 59 分，第一；Coding Agent Index 59 分，第二，仅次于 Opus 5.5 的 62 分；目前只对 Fairwind 计划开放。
- **AA Index v5**：60% 基于私有或保留答案集；开放权重与闭源差距 12 分；前 10 名里 Terra（max）最便宜，每任务 $0.96。
- **Mistral Large 4**：1.05T 总参 / 52B 激活，开放权重；AA v5 26 分，Cyber 51 分。
- **Anthropic IPO**：截至 10-30 上午 EDGAR 无 S-1/A；S-1 披露罚没 B 轮股 4,453,900 股，按 $140.9676 回购后转售，合计约 6.27 亿美元。
- **Codex/ChatGPT**：Pro 100/200/500 和 Business Premium 用量即日翻倍，Pro 200 降额取消；Pro/Business 每月可领最多 500 美元 API 额度。
- **KEV**：CVE-2026-111497（Brotli）10-27 列入；CVE-2026-46300（Linux 内核，Fragnesia）10-28 列入。
- **Kimi**：K3.1 Pro 的 HF 仓库仍返回 401。
- **Cohere**：E 轮首次交割，目标最多 70 亿加元，估值 357 亿加元。
- **其余追踪项**：Cathedral、Fable 5.5、auto mode、DeepSeek 融资、Cursor Agent SDK 本期无新消息；阿里未回应 Cohere；AGENTS.md 无厂商补丁。

## E 建议扩写
1. **"让模型监控模型"能走多远**：
   - 对照 OpenAI 的四层监控和 Anthropic 的 self-assessment，比较两者的覆盖面、时延、成本和局限：OpenAI 内部 Codex 流量的呼叫是关闭的；Anthropic 承认自评挡不住有备而来的攻击者。
   - 讨论 CoT 被优化后能否继续当证据，以及"标记样本不改奖励"这个设计。
2. **浏览器 agent 的补丁债**：从 Anthropic 的一键 Chrome 利用链讲起，Puppeteer、Playwright 钉住的 Chromium 版本落后于 10-27 的修复线。给出 agent 团队自查清单：浏览器版本、headless 隔离、只允许访问白名单 URL。
3. **蒸馏战争**：从 The Information 的报道出发，串起 Anthropic 收紧接口、OpenAI 9 月追查、AA v5 开放与闭源差距扩大到 12 分，预判 OpenAI 的 API 政策走向和 Kimi 11-04 发布权重时的许可证。
4. **AA Index v5 读榜指南**：六成私有题集后排名怎么变（Carbon 59、Opus 58、Astra 57），旧分数为什么不能直接比；结合 Terra 每任务 $0.96 和 Fable 5.1 的 $13.04，做一张"每分成本"选型表。
5. （可选）**Anthropic 上市倒计时**：S-1/A 何时出、价格区间怎么定（N-PORT 基金估值能当参照）、罚没股的历史，以及最早 11-10 路演 → 11-16 交易的时间表。


---

# 五、GitHub（2026-10-27 → 2026-10-30）

1. **Transformers v5.22.0：Mistral Large 4 开放权重入库**
10/29 晚发布的这一版，头条是 Mistral 迄今最大的模型 Mistral Large 4。它是一个原生多模态 MoE，总参数约 1T，每 token 激活 49B（算上嵌入层和输出层约 52B）；128 个路由专家每次激活 4 个，另有 1 个共享专家；上下文 1M，输入支持文本和图像，推理强度可以按请求设成 low、medium 或 high。发布说明介绍，它在 Mistral 欧洲自建机房的 3,800 块 Grace Blackwell GPU 上从零训练。官方自称它在网络安全、金融、法律类任务上表现突出，视觉定位能力超过闭源前沿模型。想评估欧洲开放权重旗舰模型、或者做多语言与长上下文 agent 的团队，可以从这一版开始在 Transformers 里直接加载。v5.21.1 是同期的补丁版。
证据：[v5.22.0 Release](https://github.com/huggingface/transformers/releases/tag/v5.22.0) · [v5.21.1](https://github.com/huggingface/transformers/releases/tag/v5.21.1)

2. **PyTorch 2.15.0：重写的 NCCL 后端成为默认**
继 2.14 系列之后，这是 10/29 凌晨发布的大版本。对分布式训练影响最大的变化，是重写的 NCCL 后端直接成为默认，并带一个卡死时自动转储现场的 flight recorder；如果出问题，可以用 `TORCH_DIST_USE_NCCL2=0` 或 `nccl-legacy` 回退。`torch.distributed` 还新增了单边传输，包括 NIXL 后端和可被 CUDA graph 捕获的传输；FSDP2 和流水线并行对显存与通信的控制也更细。推理方面，Blackwell 上的 NVFP4 解码更快；Apple Silicon 新增 FP8 和 `grouped_mm`，官方给出 MoE 解码 tokens/s 提升 1.32 到 1.34 倍。默认 wheel 改为 CUDA 13.2，`torch.compile` 支持 Python 3.15。有一处不兼容变更：同一进程里不能再重复执行 `import torch`，比如 `importlib.reload(torch)` 会直接报错。跑多机训练的团队升级前要先验证新 NCCL 后端。
证据：[v2.15.0 Release](https://github.com/pytorch/pytorch/releases/tag/v2.15.0)

3. **llama.cpp v0.8.0：server 支持实时语音，LFM3 全家入库**
这是继 v0.7.0 之后的正式版，最大的变化是 llama.cpp 开始支持语音。server 新增了实现 OpenAI realtime 协议的 `/v1/realtime` 端点（对话和转写）以及 `/tts` 端点，`mtmd` 新增了实验性的流式音频输入 API。配合同时上线的 LiquidAI LFM3 系列（文本、视觉、音频、全模态），LFM3-Audio-2B 和 LFM3-Omni-2B 一个模型就能做语音识别、语音合成和语音对话。新架构还包括 DeepSeek V4.1 Flash、Beam、Flint、Muse Spark 等；MoE 专家缓存改成了 50/50 SLRU 策略；web UI 可以直接从 HF Hub 浏览和下载模型。Ollama 在 v0.40.13 里也把 LFM3（含语音合成）扩展到 Linux 和 Windows。想在本地搭语音 agent、又不想依赖云端实时 API 的人，现在可以直接试这条链路。
证据：[llama.cpp v0.8.0](https://github.com/ggml-org/llama.cpp/releases/tag/v0.8.0) · [LFM3-Audio PR #31257](https://github.com/ggml-org/llama.cpp/pull/31257) · [Ollama v0.40.13](https://github.com/ollama/ollama/releases/tag/v0.40.13)

4. **OpenAI Codex CLI 0.165.0 / 0.166.0：内置 Vertex AI，GPT-6.1 Terra 进入模型目录**
上期在 SDK 里看到的 `gpt-6.1-terra` 模型标识，这次出现在 Codex 的模型目录里：0.165.0 加入了它，0.166.0 又把它加进内置、Vertex AI 和 Amazon Bedrock 三套目录。0.165.0 另外新增了内置的 Google Cloud Vertex AI 提供方（`model_provider = "gcp"`）；新建配置默认启用 memory v2，并支持导入其他 agent 的记忆；对话中途改推理强度也默认开启了。0.166.0 加入了键盘驱动的转录选择和搜索、`codex queue --resume`，以及专门排查网络问题的 `codex doctor --network-only`。安全方面修了一处插件市场 URL 校验漏洞，这个漏洞可能让 Git 连到和白名单检查时不同的主机。在 GCP 体系内用 Codex 的团队，现在不需要中转就能直连。
证据：[rust-v0.165.0](https://github.com/openai/codex/releases/tag/rust-v0.165.0) · [rust-v0.166.0](https://github.com/openai/codex/releases/tag/rust-v0.166.0)

5. **OpenBMB/MiniCPM-OCR：1.3B 文档解析模型 + 识别结果“自检”模型**
上期 Transformers 收录了 MiniCPM-OCR 架构，10/27 OpenBMB 又开了独立仓库，正式发布 MiniCPM-OCR 1.0（1.3B）和配套的 MiniCPM-OCR Jev。1.0 版做中英文文档和 PDF 解析，覆盖表格、公式、图表、印章和关键信息抽取。项目自称它在 Real5-OmniDocBench 上得 93.68、OCRBench v2 上得 54.7，均为 SOTA；吞吐约为 PaddleOCR-VL-1.6 的 1.49 倍、MinerU2.5 Pro 的 3.62 倍。更有新意的是 Jev：它在区域级别评估 OCR 结果，把可疑区域和可靠区域分开标出来，还能配合其他解析模型使用，帮人快速定位需要复核的地方。发布首日就支持 vLLM、SGLang、llama.cpp 和 Ollama。做文档入库、RAG 预处理的人值得拿真实扫描件测一测，Jev 的“质检”思路尤其值得借鉴。
证据：[OpenBMB/MiniCPM-OCR](https://github.com/OpenBMB/MiniCPM-OCR) · [基准复现说明](https://github.com/OpenBMB/MiniCPM-OCR/blob/main/docs/benchmark_reproduction_en.md)

6. **pbakaus/impeccable：给编码 agent 的“设计词汇表”，周增约 9700 星**
这是 2025 年 11 月建仓的老项目，总星数约 9.5 万。在 10/30 约 09:19 SGT 抓取的 GitHub Trending 上，它周榜本周 +9,713 星、日榜当日 +2,870 星排第一（周榜统计最近七天，日榜约 24 小时）。它给编码 agent 提供了一套可以直接调用的设计指令：`polish`、`bolder` 用来引导风格，`critique`、`audit` 用来评审，目标是在页面上线前拦住“AI 味”。一条 `npx impeccable install` 就能装进主流编码工具。它和上期的 hallmark 属于同一个赛道，说明“让 agent 做出不像 AI 生成的界面”正在成为热门需求。做前端的人可以对比这两者：hallmark 偏重检查清单，impeccable 偏重交互式的设计词汇。
证据：[pbakaus/impeccable](https://github.com/pbakaus/impeccable) · [文档](https://impeccable.style/docs) · [GitHub Trending（周榜）](https://github.com/trending?since=weekly)

窗口内无：vllm-project/vllm、sgl-project/sglang、huggingface/datasets、anthropics/anthropic-sdk-python、anthropics/anthropic-sdk-typescript、modelcontextprotocol/python-sdk、modelcontextprotocol/typescript-sdk、langchain-ai/langgraph（另有例行更新未收录：ComfyUI v0.43.0（MOSS-Image 增强、HeyGen 语音等合作方节点）、Axolotl v0.21.1（MoE 长 LoRA 稳定性 + eMudhra 中间 CA 安全更新）、openai-python v3.40.0/v3.41.0、openai-node v7.45.1、unsloth v0.1.912-beta、langchain-core 1.7.1–1.7.3 / langchain-anthropic 1.7.7）。


---

# 六、Hugging Face 与榜单

- 窗口：2026-10-27 09:36 → 2026-10-30 09:20（新加坡时间，SGT）｜UTC 2026-10-27 01:36Z → 2026-10-30 01:20Z
- 范围：HF Trending 模型 300 / 数据集 50（trendingScore）＋ 主要机构 `sort=lastModified` 新动作 ＋ AA 智能指数 / 文生图 / 图像编辑榜 ＋ LMArena 文本 / 视觉 / 文生图榜；对比基线为 10-27 约 09:2x SGT 的快照
- 窗口判断：**偏厚**。Mistral 在窗口内放出约 1T 参数的开放权重旗舰 Mistral Large 4，是本窗头条；LiquidAI 整套 LFM3 端侧家族、NVIDIA 30B 级语音识别模型 Nemotron 3.5 Transcribe 均在窗口内放权重。榜单侧 AA 在 10-27 切换到智能指数 v5（分数尺度整体下调，不能与 10-27 包里的数字直接比），10-28 Gemini 4 Carbon 登顶 AA 并进入 LMArena 文本榜第 1。**Kimi K3.1 Pro 截至采集时仍未上 HF**。
- 本部分列出的 43 个 Hugging Face 模型/数据集仓库，均在采集时确认可公开访问（已核）。

---

## 一、重点（5 条）

### 1. Mistral Large 4（1T 总参 / 约 49B 激活，开放权重）— 本窗新发

Mistral 把此前只在 API 和 AA 上以 Preview 形式出现的 Large 4 正式放了权重：约 1T 总参、每 token 激活约 49B（含 embedding 为 52B）的 MoE，128 个路由专家取 top-4 外加 1 个共享专家，1M 上下文，支持文本+图像输入，推理强度分 low/medium/high 三档，权重直接以 FP8 块量化发布（54 个分片，合计约 1.08TB），还内嵌了一个用于投机解码的 draft head。这是今年以来欧洲厂商最大的开放权重模型，但许可证不是 Apache：卡片写的是"Mistral Ecosystem Open-Weight License"（改版 MIT），做模型即服务（MaaS）的公司需另签商业许可，企业内部使用不受限。另外要注意，AA 智能指数 v5 下它目前只有 26 分（High 档），离 Kimi K3.1 Pro（46）和 DeepSeek V4.1 Flash 1017（32.5）都有差距，"西方开放权重最高"的说法成立，但"开放权重第一"并不成立。

- **为何重要**：欧美阵营第一个 1T 级开放权重模型；单机 8 卡（TP8）即可部署（vLLM 官方镜像 `vllm/vllm-openai:mistral-large-4`），同时官方给出 NVFP4 版本，Blackwell 用户门槛更低。
- **对谁有用**：需要欧盟数据主权 / 本地部署的大企业；做长上下文多模态 agent 的团队；推理框架与量化社区（unsloth、ggml-org 已跟进 GGUF）。
- **已核**
  - 仓库创建：2026-10-01 02:35 SGT（2026-09-30 18:35Z，此前非公开）；权重提交 "Initial release"：**2026-10-29 22:11 SGT（14:11Z）**；最后修改 2026-10-29 22:51 SGT（14:51Z，README 更新）
  - likes 1,222 / downloads 278｜license: other（Mistral Ecosystem Open-Weight License）｜pipeline: image-text-to-text｜Trending 模型第 14（trendingScore 300）
  - config：`MistralLarge4ForConditionalGeneration`，72 层、hidden 6144、词表 204,800、max_position 1,048,576、kv_lora_rank 512（MLA 类注意力）、index_topk 2048；视觉编码器 pixtral 30 层；FP8 块量化 128×128
  - 卡片：训练用欧洲境内 3,800 张 Grace Blackwell GPU；160+ 语言
  - 衍生：NVFP4 官方版 likes 42 / dl 78（最后修改 2026-10-30 00:46 SGT）；unsloth GGUF likes 21 / dl 0；ggml-org GGUF likes 7 / dl 11
  - AA（v5）：Mistral Large 4 (High) 26.0，标记开放权重；LMArena 文本榜 #113，1432±6（12,066 票，10-27 快照为 #111 / 1434±6 / 10,331 票，榜上仍标 Proprietary，属 API 期间入榜的同名条目）
- **待核**：卡片自报"AA 编程 Agent 指数 48%，与 GLM-5.3 持平且 token 少 47%""AA 智能指数 v5 = 26，西方开放权重最高"——前者未在 AA 页面逐项核对；许可证对 MaaS 的界定需读完整条款；LMArena 视觉榜 #52（1252±19，1,008 票）在 10-27 快照中是否已存在无法确认（10-27 视觉快照只存了表头）。
- 链接：[HF 模型页](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B) ｜ [NVFP4 版](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B-NVFP4) ｜ [Mistral 官方发布文](https://mistral.ai/news/mistral-large-4-oss/) ｜ [HF 博客解读](https://huggingface.co/blog/mistral-large4) ｜ [unsloth GGUF](https://huggingface.co/unsloth/Mistral-Large-4-1T-A52B-GGUF) ｜ [ggml-org GGUF](https://huggingface.co/ggml-org/Mistral-Large-4-1T-A52B-GGUF)

### 2. LiquidAI LFM3 家族（1.7B 文本 / 2B 视觉 / 2B 音频 / 2B 全模态 / d1 决策模型）— 本窗新发

LiquidAI 在 10-27 一天内把 LFM3 整套端侧家族的权重全部放出：主力 LFM3-1.7B 是卷积+注意力混合结构（24 层里 13 层门控短卷积、5 层滑窗注意力、6 层全局注意力），256K 上下文，4-bit 下约 1GB，明确针对 Hermes Agent / OpenClaw 这类本地 agent 场景训练；同时发了 VL-2B（视觉）、Audio-2B（语音）、Omni-2B（文本+图像+视频+音频输入，文本+24kHz 语音输出）、Base 底座，以及一类新东西 d1——不生成 token、只做"决策"的模型，H100 上单次决策约 5.7ms，用来给 agent 做路由/判断。自报成绩在 agent 类基准上大幅超过 Qwen3.5 9B，但在 SWE-bench 和 GPQA 上明显落后，官方也写了不推荐用于 agentic coding——这是一个"小而专"的 agent 底座，不是通用小模型的全面替代。

- **为何重要**：1.7B 级别第一次把"本地 agent 工具调用"做到可用水平的有力候选；整套家族同日发布，GGUF 版 3 天下载 6.1 万，社区接受度高。
- **对谁有用**：手机 / 笔电端侧 agent 开发者；需要低延迟路由判断的 agent 平台（d1）；做本地语音助手的团队（Omni / Audio）。
- **已核**
  - 权重提交（SGT）：LFM3-1.7B 2026-10-27 13:58（05:58Z）；Audio-2B 10-28 00:22（10-27 16:22Z）；VL-2B 与 d1-2B 10-28 00:24（16:24Z）；Omni-2B 10-28 01:25（17:25Z）；1.7B-Base 10-28 01:35（17:35Z）。各仓库创建时间均早于窗口（9-08 至 10-26，非公开期）
  - LFM3-1.7B：likes 484 / dl 15,885｜Trending 第 4（473）｜1.73B｜license: other（LFM Open License v1.0）｜text-generation｜最后修改 2026-10-29 01:16 SGT（10-28 17:16Z）
  - LFM3-1.7B-GGUF：130 / 61,499（#37）；Omni-2B：205 / 1,814（#18，2.17B，any-to-any，32K 上下文，非推理）；VL-2B：166 / 4,193（#24）；Audio-2B：134 / 1,794（#33）；Base：84 / 1,399（#69）；d1-2B：96 / 1,776（#56）；d1-Omni-2B：79 / 709（#77）
- **待核**（均为卡片自报，对比 Qwen3.5 9B）：LiveClaw 45.60 vs 35.77；WebArena-Verified 38.42 vs 28.94；AutomationBench 41.29 vs 15.10；BFCL V4 71.39 vs 62.83；SWE-bench Verified（OpenCode）43.40 vs 51.20；GPQA Diamond 63.37 vs 80.40；IFEval 96.66。LFM Open License 的商用营收门槛需读原文。LMArena / AA 均未收录。
- 链接：[LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) ｜ [LFM3-Omni-2B](https://huggingface.co/LiquidAI/LFM3-Omni-2B) ｜ [LFM3-VL-2B](https://huggingface.co/LiquidAI/LFM3-VL-2B) ｜ [LFM3-Audio-2B](https://huggingface.co/LiquidAI/LFM3-Audio-2B) ｜ [d1-2B](https://huggingface.co/LiquidAI/d1-2B) ｜ [d1-Omni-2B](https://huggingface.co/LiquidAI/d1-Omni-2B) ｜ [LFM3-1.7B-Base](https://huggingface.co/LiquidAI/LFM3-1.7B-Base) ｜ [LFM3-1.7B-GGUF](https://huggingface.co/LiquidAI/LFM3-1.7B-GGUF) ｜ [LFM3 官方博客](https://www.liquid.ai/blog/lfm3) ｜ [d1 官方博客](https://www.liquid.ai/blog/open-d1) ｜ [HF 合集](https://huggingface.co/collections/LiquidAI/lfm3)

### 3. NVIDIA Nemotron 3.5 Transcribe 30B-A4B（语音识别）— 本窗放权重

NVIDIA 把语音识别从 Parakeet 那种 0.6B 级专用小模型，直接拉到了基于 LLM 的 30B 级：以 Nemotron 3.5 Lightning 30B-A3B（Mamba-2 与 Transformer 混合 MoE）为底座，加音频编码器后总参约 34B、激活约 4.3B，单张 H100 可跑，支持 40 种语言、最长 1 小时录音、65,536 上下文。自报在 Open ASR 榜平均 WER 4.71，略好于 Qwen3-ASR-1.7B 的 4.94；长音频和多语种上对自家 Parakeet-TDT-0.6B-v3 优势更明显。代价是体量比主流 ASR 大一两个数量级，宣传里最亮眼的吞吐数字依赖尚未开源的 NIM 优化。

- **为何重要**：开放权重 ASR 的 SOTA 之争进入"LLM 底座"阶段；长音频、多说话人转写是会议纪要、播客、客服质检的刚需。
- **对谁有用**：做会议/播客转写和多语种字幕的团队；需要本地部署 ASR 的企业；语音 agent 开发者。
- **已核**
  - 仓库创建 2026-10-08 06:50 SGT（10-07 22:50Z，非公开期）；权重提交 "NVIDIA Nemotron 3.5 Transcribe"：**2026-10-27 20:22 SGT（12:22Z）**；文档持续更新至 2026-10-30 07:04 SGT（10-29 23:04Z）
  - likes 413 / dl 4,276｜Trending 第 8（395）｜33.7B｜license: other（openmdw-1.1）｜automatic-speech-recognition
  - 另有 FP8 / NVFP4 / DFlash2 变体（FP8、NVFP4 likes 分别为 1、8）
- **待核**（卡片自报）：Open ASR 平均 WER 4.71（Qwen3-ASR-1.7B 4.94）；长音频 10.98（Parakeet-TDT-0.6B-v3 13.37）；多语种 4.62（6.49）；多说话人 cpWER 15.80；RTX PRO 6000 上 NIM 吞吐 2,238 秒音频/秒（NIM 优化未开源）。Open ASR Leaderboard 页面是否已收录未核。
- 链接：[HF 模型页](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) ｜ [底座 Nemotron 3.5 Lightning 30B-A3B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16) ｜ [配套数据集 Granary-v2](https://huggingface.co/datasets/nvidia/Granary-v2)

### 4. inclusionAI Ling-3.1-flash-1019（560B 总参 / 25B 激活，MIT）— 本窗新发

蚂蚁 inclusionAI 的 Ling 3.1 Flash 在 AA 上 10-22 就已有成绩，本窗才把权重放上 HF。它是混合线性注意力的 MoE：63 层 KDA 线性注意力 + 9 层门控 MLA，512 个专家取 top-8，1M 上下文，许可证是宽松的 MIT。在 AA v5 下拿到 29.5，排在 MiMo-V2.6-Pro（29.9）之后、MiniMax-M3.1-Flash（28.9）之前，属于开放权重第二梯队的中上游；相比本窗的 Mistral Large 4（26.0），它用一半左右的总参拿到了更高的 AA 分数，且许可更干净。

- **为何重要**：MIT 许可的 500B+ 级开放模型并不多；线性注意力混合架构在 1M 上下文下的推理成本是卖点。
- **对谁有用**：需要宽松许可大模型做二次训练/商用的团队；关注长上下文推理成本的部署方。
- **已核**
  - 仓库创建 **2026-10-27 13:46 SGT（05:46Z）**；权重上传 2026-10-27 18:45–18:46 SGT（10:45–10:46Z）；最后修改同
  - likes 80 / dl 832｜Trending 第 74｜HF 计参 572B｜license: MIT｜text-generation
  - AA（v5）：Ling 3.1 Flash 1019 = 29.5，开放权重，评测日期 10-22（AA 更新流）
- **待核**：卡片引用的是 AA 旧版 v4.3.2 指数 44（上一版 41）、AA-Briefcase 约 1400→1524、AutomationBench 62%→68%，与 AA 当前 v5 尺度不可比；LMArena 未收录。
- 链接：[HF 模型页](https://huggingface.co/inclusionAI/Ling-3.1-flash-1019)

### 5. OpenBMB MiniCPM-OCR-1.0（1.3B 文档 OCR）— 本窗公开（权重早于窗口上传）

面壁这次没有再做"能 OCR 的通用多模态小模型"，而是基于 MiniCPM-V-4.6 专门做了 1.3B 的文档解析模型，并配了一个判断 OCR 结果对不对的 Jev 校验模型。自报在 Real5-OmniDocBench 93.68、吞吐是 PaddleOCR-VL-1.6 的 1.49 倍，Apache-2.0 许可。权重 10-23 就已上传，但模型卡和 GitHub 公开链接是 10-27 晚上才补上的，实际对外发布更可能在窗口内。

- **为何重要**：1B 级文档 OCR 已经是 Baidu Unlimited-OCR-2、PaddleOCR-VL 等的主战场，Apache-2.0 + 带校验模型的组合对生产管线友好。
- **对谁有用**：做 RAG 文档入库、票据/合同解析的团队；需要端侧 OCR 的应用。
- **已核**
  - 仓库创建 2026-10-21 23:51 SGT（15:51Z）；权重提交 2026-10-23 21:41 SGT（13:41Z，窗口前）；模型卡 **2026-10-27 22:57 SGT（14:57Z）**，公开 GitHub 链接 2026-10-27 23:47 SGT（15:47Z）；最后修改 2026-10-29 23:39 SGT（15:39Z）
  - likes 322 / dl 1,597｜Trending 第 20｜1.3B｜apache-2.0｜image-text-to-text｜base: MiniCPM-V-4.6
  - MiniCPM-OCR-Jev：likes 67 / dl 963（#90）
- **待核**：Real5-OmniDocBench 93.68、OCRBench v2 54.7、1.49× PaddleOCR-VL-1.6 吞吐均为卡片自报；"窗口内公开"系按提交记录推断。
- 链接：[MiniCPM-OCR-1.0](https://huggingface.co/openbmb/MiniCPM-OCR-1.0) ｜ [MiniCPM-OCR-Jev](https://huggingface.co/openbmb/MiniCPM-OCR-Jev)

---

## 二、旁线

1. **Kimi K3.1 Pro 仍未上 HF**：moonshotai 最新仍是 Kimi-K3（最后修改 2026-09-02 10:22 SGT）。官方口径是 11-04 前放权重。AA v5 下 Kimi K3.1 Pro = 46.0，开放权重最高（AA 页面仍标为专有，因权重未放出）；LMArena 文本榜未收录。HF 上搜到的 `audnai/penclaw-Kimi-K3.1-pro-unrestricted`（likes 85 / dl 0，gated: manual）**是冒名仓库、不是官方发布，勿当成权重已放出**。[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)
2. **Pika-Labs/Pika-H3-Flex**（视频+音频生成，基于 MiniMax-H3，33.1B，6 步出片）：发布提交 2026-10-30 01:10 SGT（10-29 17:10Z），likes 87 / dl 0，Trending #70，license: minimax-h3-community。dl 为 0，降权观察。[HF](https://huggingface.co/Pika-Labs/Pika-H3-Flex)
3. **ServiceNow-AI/Apriel-Voice-27B-preview**（语音理解，Whisper large-v3-turbo 编码器 + Gemma 4 26B-A4B 骨干，MIT）：权重 2026-10-30 00:55 SGT（10-29 16:55Z），likes 40 / dl 2，preview。[HF](https://huggingface.co/ServiceNow-AI/Apriel-Voice-27B-preview)
4. **Diffuspace/Clover-35B-A3B-Preview**（由 Qwen3.6-35B-A3B 改造的块扩散语言模型，128K，apache-2.0）：单次提交 2026-10-28 11:07 SGT（03:07Z），likes 147 / dl 1,030，Trending #26。[HF](https://huggingface.co/Diffuspace/Clover-35B-A3B-Preview) ｜ [官方博客](https://diffuspace.ai/blog/clover-35b/)
5. **nvidia/Metatron-v1**（宇树 G1 人形机器人策略）：创建 2026-10-28 05:43 SGT（10-27 21:43Z），likes 8 / dl 463。[HF](https://huggingface.co/nvidia/Metatron-v1)
6. **数据集 nvidia/Granary-v2**（Nemotron Transcribe 配套多语种语音数据）：新进数据集 Trending #11，likes 24 / dl 1,074，license openmdw-1.1 / cc-by-sa-4.0；仓库创建于 09-16，最后修改 2026-10-28 22:09 SGT（14:09Z），公开时间待核。[HF](https://huggingface.co/datasets/nvidia/Granary-v2)
7. **Cohere 的 Qwen 调查轨迹数据集**（热度延续 + 跟进）：数据集 Trending #4，likes 22→80，dl 0→3,200。截至采集未找到阿里 / Qwen 官方回应的具体文章页；Reuters 报道写明阿里截至 10-27 未回应。[数据集](https://huggingface.co/datasets/CohereLabs/10-2026-qwen-investigation-traces) ｜ [Cohere 原文](https://cohere.com/blog/concerning-behaviour-popular-open-weight-ai-model) ｜ [TechCrunch 报道](https://techcrunch.com/2026/10/26/cohere-says-alibabas-qwen-model-tried-to-send-a-file-to-beijing/) ｜ [VentureBeat 分析](https://venturebeat.com/data/coheres-test-caught-an-open-source-qwen3-8-model-trying-to-phone-home-to-china-what-enterprises-should-know)
8. **HuggingFaceBio/Carbon-X 修复**：2026-10-28 19:22 / 19:41 SGT 修复 tokenizer 持久化并统一 EOS 为 `<|im_end|>`（属实质性修复，早前下载的用户建议重拉）；likes 207→271。[HF](https://huggingface.co/HuggingFaceBio/Carbon-X)
9. **baidu/Unlimited-OCR-2 热度起量**：10-27 时 likes 9 / dl 0，现 likes 383 / dl 18,141，Trending #10；窗口内只有 README 与 sglang wheel 更新（2026-10-29 17:17 SGT），无新权重。[HF](https://huggingface.co/baidu/Unlimited-OCR-2)
10. **其他小项**：maya-research/maya2-native（TTS，权重 10-26 窗口前，117 / 938）[HF](https://huggingface.co/maya-research/maya2-native)；sensenova/SenseNova-6.8-Code2Video（10-29 19:32 SGT 更新模型，55 / 130）[HF](https://huggingface.co/sensenova/SenseNova-6.8-Code2Video)。

---

## 三、榜单对比（对比 10-27 约 09:2x SGT 快照）

### AA 智能指数：切换到 v5，分数整体不可与 10-27 比
- **10-27 AA 发布智能指数 v5**：新增 FrontierCode 2.0、Terminal-Bench-Science，更新 HLE-Diamond、AA-Omniscience v1.1、CritPt v2；移除 GDPval-AA v2.1、SciCode、AA-LCR；60% 题目为私有；知识工作 / 编程 / 科学 / 通用各占 25%。AA 文章称开放与闭源差距从约 3 分扩大到 12 分。[AA v5 说明文](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)
- **10-28 Gemini 4 Carbon (High) 以 59.4 登顶**（限量开放，$4/$20 每百万 token）。[AA 文章](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)
- 当前默认视图前列（v5）：1 Gemini 4 Carbon 59.4｜2 Claude Opus 5.5 58.4｜3 GPT-6 Astra 56.9｜4 GPT-6.1 Sol 54.5｜5 Claude Sonnet 5.5 54.2｜6 GPT-6.1 Terra (Max) 51.0｜7 Muse Wonder Full 49.7｜8 Claude Fable 5.1 49.0｜9 Kimi K3.1 Pro 46.0
- 开放权重（v5）：Kimi K3.1 Pro 46.0（权重未放）｜DeepSeek V4.1 Flash 1017 (Max) 32.5｜GLM-5.3 31.7｜MiMo-V2.6-Pro 29.9｜Ling 3.1 Flash 1019 29.5｜**MiniMax-M3.1-Flash 28.9（现已标为开放权重）**｜Mistral Large 4 (High) 26.0｜Muse Spark Open 24.7｜Qwen3.8 27B 20.1｜Beam 1.0 17.7｜Nemotron 3.5 Super VL 13.6
- 关注项：GPT-6.1 Terra 从 v4 的 48.1（#10）变为 v5 的 51.0（#6）；Kimi K3.1 Pro 从 55.1（#4）变为 46.0（#9）；DeepSeek 1017 从 45.1 变为 32.5——**均为指数换版所致，不是模型退步**。收录模型数 714→717。Nanbeige4.3、Flint 仍未收录；Nemotron 3.5 Bolt E4B 4GB (Reasoning) 已于 10-23 收录（分数未能从页面提取，待核）。

### AA 文生图榜：无变化
- 106 个模型，排名与 Elo 与 10-27 完全一致（仅表头文字由 "API Pricing" 改为 "Pricing"）。FLUX 3 Image #13 1117；FLUX 3 Image Klein #21 1043±12（5,184 样本）；Qwen-Image-2.1 #22 1042；Fibo 2.0 #23 1039。[AA 文生图榜](https://artificialanalysis.ai/image/leaderboard/text-to-image)

### AA 图像编辑榜：新模型直接进第 2
- **MAI-Image-2.7-Preview 新上榜即 #2，1193±15（4,891 样本，2026 年 10 月，无 API）**；其余模型 Elo 不变、名次顺延一位：FLUX 3 Image #14→#15（1122）、Fibo 2.0 #22→#23（1088）、FLUX 3 Image Klein #26→#27（1072）。Krea 3 (Ultra) 价格 $270→$100 / 千张。[AA 图像编辑榜](https://artificialanalysis.ai/image/leaderboard/editing)

### LMArena
- **文本榜已刷新**：Oct 22 / 8,946,356 票 / 418 个模型 → **Oct 27 / 9,003,272 票 / 419 个模型**。唯一新增为 **Gemini 4 Carbon (High) 直接 #1，1528±9（初步，4,403 票）**；Gemini 4 Argon 1517→1520 降至 #2；Claude Opus 5.5 (High) #3 1509；Muse Wonder #4 1507。开放权重最高：Kimi K3 (Max) #19 1488；GLM-5.3 (Max) #28 1481；MiMo-V2.6-Pro #29 1480；DeepSeek-V4.1-Flash-20260910 (Max) #35 1476。Mistral Large 4 #111→#113（1434→1432）。[LMArena 文本榜](https://lmarena.ai/leaderboard/text)
- 关注清单中未收录：Kimi K3.1 Pro、GPT-6.1 Terra、Flint、MiniMax-M3.1-Flash、Nemotron 3.5 Bolt、DeepSeek-V4.1-Flash-1017、Nanbeige4.3、Ling 3.1 Flash、LFM3。
- **文生图榜未刷新**（仍为 Oct 26 / 6,872,557 票 / 82 个模型）：#1 GPT-Image-2.5 Sunburst 1427；Qwen-Image-2.1 #19 1225；FLUX.2 [klein] 9B #62 1070。FLUX 3、Fibo 2.0、MOSS-Image、Krea 3 仍未收录。[LMArena 文生图榜](https://lmarena.ai/leaderboard/text-to-image)
- **视觉榜未刷新**（Oct 19 / 1,493,948 票 / 167 个模型）；Mistral Large 4 在 #52，1252±19（1,008 票）。[LMArena 视觉榜](https://lmarena.ai/leaderboard/vision)

---

## 四、热度延续（10-27 → 10-30，无新权重）

| 模型 | Trending | likes（10-27→现） | downloads（10-27→现） | 窗口内变化 |
|---|---|---|---|---|
| [deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) | #1 | 3,192→3,777 | 95,889→131,062 | 无；ISTA-DASLab GGUF 量化版 dl 1,578,937（#7） |
| [Nanbeige/Nanbeige4.3-33B](https://huggingface.co/Nanbeige/Nanbeige4.3-33B) | #2 | 602→778 | 2,787→9,655 | 10-28 00:00 SGT 补评测结果，10-28 09:59 SGT 改 README |
| [RecursiveSI/flint](https://huggingface.co/RecursiveSI/flint) | #3 | 925→1,244 | 8,470→16,598 | 无提交 |
| [XHToken/Spark-X2.6-4B](https://huggingface.co/XHToken/Spark-X2.6-4B) | #5 | 648→908 | 现 10,163 | 10-27 20:55 SGT 更新 |
| [MiniMaxAI/MiniMax-M3.1-Flash](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash) | #6 | 382→489 | 8,782→15,738 | AA 改标为开放权重 |
| [black-forest-labs/flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy) | #11 | 1,701→2,055 | 现 832,197 | 无 |
| [nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB) | #17 | 157→256 | 现 57,228 | AA 10-23 已收录 |
| [HuggingFaceBio/Carbon-X](https://huggingface.co/HuggingFaceBio/Carbon-X) | #21 | 207→271 | 现 2,808 | tokenizer / EOS 修复（见旁线） |
| [tencent/Hy-Nomas](https://huggingface.co/tencent/Hy-Nomas) | #45 | 现 116 | 现 44,124 | 文档更新 |
| [tencent/Hy-SimulMT-30B-A3B](https://huggingface.co/tencent/Hy-SimulMT-30B-A3B) | #148 | 18→42 | 0→339 | 10-27 17:40 SGT 文档同步 |
| [inclusionAI/LBS-27B](https://huggingface.co/inclusionAI/LBS-27B) | — | 现 15 | 现 484 | 窗口内无提交 |

---

## 五、降权

- 去审查 / 改造版：orcarouter/DeepSeek-V4.1-Flash-1017-abliterated-GGUF（#15，342 / 28,763）、dealignai/DeepSeek-V4.1-Flash-1017-UNCENSORED-FP8（#27，476 / 9,787）、AtomicChat/LFM3-1.7B-Uncensored-GGUF（#42，125 / 16,687），以及 huihui / Abiray / DavidAU Heretic / OliviaRossi PRISM / abenzerps Qwen-Image Uncensored 等，均不作为发布。
- 冒名仓库（非官方发布）：audnai/penclaw-Kimi-K3.1-pro-unrestricted（dl 0）。
- 仅维护：XiaomiMiMo 10-28 22:00–22:18 SGT 批量刷新；KRAFTON Raon、reflection Beam、ibm-granite、tencent WeVisOne-VL（创建于 10-22）、facebook gated 仓库、microsoft rho-*（dl 0）、stabilityai stable-audio-3-optimized（2026-10-30 08:22 SGT）、google embeddinggemma-2（仅补技术报告）；Efficient-Large-Model/Open-H3-Regenerate-2K（dl 0）。
- 本窗无新动作：openai、meta-llama、Qwen、deepseek-ai、black-forest-labs、briaai、CohereLabs、ByteDance-Seed、apple、amazon、allenai、moonshotai、zai-org、MiniMaxAI、RecursiveSI、stepfun-ai 等；Lightricks 仅一个空仓库。

---

## 六、更正

1. 10-27 包写"Nemotron 3.5 Bolt E4B 在 AA 无成绩"有误：AA 更新流显示 10-23 已收录 "Nemotron 3.5 Bolt E4B 4GB (Reasoning)"（具体分数待核）。
2. MiniMax-M3.1-Flash 在 AA 由"专有"改标为"开放权重"，分数随 v5 换版由 42.7 变为 28.9。
3. 10-27 及更早包里引用的所有 AA 智能指数分数均为 v4 尺度，与本包 v5 分数不可直接比较。
4. Mistral Large 4 在 LMArena 文本榜 10-27 已在榜（#111，以 API 版本入榜），并非本次新进。
