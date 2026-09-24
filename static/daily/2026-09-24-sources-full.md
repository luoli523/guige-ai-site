# 2026-09-24 三日刊全量原始素材

这是本窗三日刊的**全量原始归档**，用来留档与回溯线索；**不是**站点上那篇深读正文。

- **信息窗口**：≈2026-09-21 09:00 → 2026-09-24 09:11（Asia/Singapore）
- **信息来源**
  - 大厂 / 学术（官博与 arXiv）
  - X（Following / 公开 AI 讨论）
  - GitHub 发布与热仓
  - Hugging Face / 模型卡

## 本期配图

（配图由站点 hero 流程另行挂载；本归档不嵌入本地路径与体积元信息。）

---

## 一、大厂与学术界

窗口：2026-09-21 09:00 → 2026-09-24 09:11 Asia/Singapore  

## 结论
本窗**很满**：OpenAI 扩 GPT-6 家族（Sol/Luna）+ 心理健康评测；Anthropic 发 **Claude Opus 5.5** 并官宣生命科学实验室首个酶发现；DeepMind/Google 推 Private AI Compute 服务端记忆 + Gemini 3.8 TTS。Meta 官博仍无窗内新帖；MSR 站点抓取 403，未见确认新帖。arXiv 覆盖 Mon21–Wed23（Thu24 未出）；抬 **RRSI（Google Cloud）**、**OSWorld-Pro（NVIDIA）**，并保留 AIDE² / CliffCompaction / KEX。

---

## OpenAI

### Introducing GPT-6 Sol and Luna（Sep 22）
**人话一句** 在 GPT-6 Astra 之上放出更便宜的 Sol / Luna，把同系能力铺到成本曲线下端。  
**为何重要** 本窗最大产品洪峰；明确「最强 Astra vs 性价比 Sol/Luna」分层。  
**要点（官方自报）** API：Sol **$2 / $10**、Luna **$0.10 / $0.50**（每百万 token，相对上代约半价）；ChatGPT Work/Codex 等渠道可用；同步强调缓存命中与 agent 长对话。  
**对谁有用 / 深读** 产品/工程选型 → **必读抬主线**。  
**证据** [introducing-gpt-6-sol-and-luna](https://openai.com/index/introducing-gpt-6-sol-and-luna)

### Better prompt caching for GPT-6（Sep 22）
**人话一句** GPT-6 默认提高缓存命中，缓存输入读最高约 **90%** 折扣，并加诊断/预热工具。  
**为何重要** 直接打长程 agent 成本。可与上条合并写。  
**证据** [better-prompt-caching-for-gpt-6](https://openai.com/index/better-prompt-caching-for-gpt-6)

### Introducing MentalHealthBench（Sep 23）
**人话一句** 与 80+ 持证心理专家共开源心理健康对话评测，补「不只测危机话术」的空白。  
**为何重要** 安全评测从应急场景扩到日常心理对话。  
**深读** 安全/政策 → **选读**。  
**证据** [introducing-mentalhealthbench](https://openai.com/index/introducing-mentalhealthbench)

### Priorities and principles for effective third party assessments（Sep 22–23）
**人话一句** OpenAI 公开第三方评估应优先什么、原则是什么。  
**深读** 治理 → 次要/选读。  
**证据** [priorities-principles-third-part](https://openai.com/index/priorities-principles-third-party-assessments)

（窗内另有多家客户案例、Academy、UN 演讲等，组装时可降为次要。）

## Anthropic

### Introducing Claude Opus 5.5（Sep 22）
**人话一句** 新旗舰 Opus 5.5：多数工作对齐 Claude Fable 5.1 水准，跑起来比 Opus 5 更便宜更快。  
**为何重要** 「放缓前沿」表态后的首发；外部含 Frontier Design、METR 测过。  
**要点（官方自报）** 相对 Opus 5：典型负载更便宜；输入/输出 **$4 / $20** 每百万（约低 20%）；缓存读 **$0.20**（约低 60%）；输出更快 **>30%**；行为审计称自家测过最强。  
**对谁有用 / 深读** 全员 → **必读抬主线**。  
**证据** [claude-opus-5-5](https://www.anthropic.com/news/claude-opus-5-5)

### Claude discovers a novel enzyme system（Sep 23）
**人话一句** Anthropic 新生命科学组官宣：Claude 在高层次指导下发现带 CRISPR 样重复的新型酶系统，并开实验室验证路径。  
**为何重要** 大厂把「模型做科学发现」做成常设实验室叙事，不只是 demo。  
**深读** 科学 AI / 生物 → **选读抬**。  
**证据** [claude-discovers-novel-enzyme-sy](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system)

## Google DeepMind / blog.google

### Advancing Private AI Compute with secure, server-side memory（Sep 24）
**人话一句** Private AI Compute 加上安全的服务端持久记忆，想把端侧隐私体验扩到云端级记忆。  
**为何重要** 隐私计算从「当次推理」迈向「跨会话记忆」产品化。  
**深读** 隐私/平台 → **选读**。  
**证据** [advancing-private-ai-compute-wit](https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/)

### Gemini 3.8 text-to-speech（Sep 23）
**人话一句** Gemini 3.8 Flash / Flash-Lite TTS：自然语言控声线，覆盖 100+ 语言方言，进 AI Studio/API 等。  
**深读** 多模态产品 → **选读**。  
**证据** [say-hello-to-gemini-38-text-to-s](https://deepmind.google/blog/say-hello-to-gemini-38-text-to-speech/)  
镜像 [gemini-3-8-text-to-speech](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/)

## Meta AI / Microsoft Research
- **Meta**：列表最新约 2026-07，本窗 **ZERO**。  
- **MSR**：博客/feed **403**，本窗 **无确认新帖**。

---

## arXiv（Mon21–Wed23 · 宁缺抽 5 · 已核挂名）
Thu 24 宣布批尚未出（~09:35 SGT 仍显示 Wed）。原料：`arxiv-raw.md`。数字均为**论文自报**，表图细数 ****。

### 1. RRSI — [2609.24972（Tue](https://arxiv.org/abs/2609.24972（Tue) 22）
**人话一句** Google Cloud AI Research 等：给 harness 层递归自改进加正则（编辑预算退火 + critic/pruner），减轻「只在进化集过拟合」。  
**挂名** Google Cloud AI Research；UNC；Stanford；WashU。  
**要点** evolve 集最高约 **+14.1**；五份 OOD 最高约 **+4.7**；策略 token 约 **−30%** vs 无正则进化。  
**深读** RSI/harness → **选读抬**。

### 2. OSWorld-Pro — [2609.24890（Tue](https://arxiv.org/abs/2609.24890（Tue) 22）
**人话一句** NVIDIA：给电脑使用 agent 做过程级评测（子目标/失败分类），不只看终态对错。  
**挂名** NVIDIA。  
**要点** 300+ 任务 / 2800+ 子目标；Claude Opus 5：OSWorld-Pro **75.7%** vs OSWorld **83.4%**。  
**深读** CUA/评测 → **选读抬**。

### 3. Recursive self-improvement of AI research agents — [2609.26457（Wed](https://arxiv.org/abs/2609.26457（Wed) 23）
**人话一句** Weco AI 的 AIDE²：研究 agent 改自身代码，8 天自主跑出七轮自改进并迁移到留出基准。  
**要点** 奖励黑客率 **55%→32%** 等（论文自报）。  
**深读** RSI → **选读**。

### 4. CliffCompaction — [2609.26779（Wed](https://arxiv.org/abs/2609.26779（Wed) 23）
**人话一句** CMU（Tim Dettmers 等）+ Bosch：只截断/丢弃、不改写的长程 coding 上下文压缩。  
**要点** 有界上下文成本最高约 **−50%**。  
**深读** Agent 工程 → **选读**。

### 5. KEX-bench — [2609.25591（Wed](https://arxiv.org/abs/2609.25591（Wed) 23）
**人话一句** UIUC 等：测 coding agent 能否把真实内核 CVE 做成可验证的 exploit **原语**（非只找崩）。  
**要点** 无 PoC：Win 5% / Linux 56%；有 PoC：总体 68.9%（论文自报）。  
**深读** 安全评测 → 选读摘要（组装勿写利用步骤）。

（次要：Microsoft CASD 提示蒸馏 [2609.26261](https://arxiv.org/abs/2609.26261) — 先前已核，本窗让位大厂 RSI/CUA。）

---

---

## 二、X 动态素材

- **窗口（Asia/Singapore）：** 2026-09-21 09:00 → 2026-09-24 09:11（约 72h）

---

## A. X 时间线（官方自报）

### 1. OpenAI · MentalHealthBench
- **是什么：** 开放心理健康对话评测基准，覆盖日常支持到危机场景；80+ 临床人员参与。
- **为何重要：** 把「助手对心理健康对话」从口号落到可复现评测，利于安全与产品对齐。
- **对谁 / 深读：** 安全/评测研究、产品合规 — **值得深读**（基准设计与危机场景定义）。
- **证据：** 官方自报 · [推文](https://x.com/i/status/2102837574092161102) · [公告](https://openai.com/index/introducing-mentalhealthbench/)
- **约时：** 2026-09-24 03:08（X 显示）

### 2. Anthropic · Claude 辅助刚果埃博拉变体应急
- **是什么：** 称刚果民主共和国相关全球卫生机构用 Claude 加快异常埃博拉变体疫情响应（CEPI、WHO 非洲区办、国家生物医学研究机构等）。
- **为何重要：** AI 进入真实公共卫生应急；需对照 Situation Report 核「用到哪一步」。
- **对谁 / 深读：** 医疗/公益落地、安全政策 — **值得深读** Situation Report；推文本身可略读。
- **证据：** 官方自报 · [推文](https://x.com/i/status/2102897863097545197) · 链至 Anthropic Situation Report（推文内短链）
- **约时：** 2026-09-24 07:08（X 显示）

### 3. Claude · Marketplace 上线
- **是什么：** Claude Marketplace：用户浏览工具；开发者可提交 tools / agents / services。入口 `claude.com/marketplace`。
- **为何重要：** Claude 从聊天产品向工具/代理分发层扩展，生态位接近「应用商店」。
- **对谁 / 深读：** 产品/生态、工具开发者 — **值得扫一眼**博客与提交流程；非研究主线可略。
- **证据：** 官方自报 · [推文](https://x.com/i/status/2102840855258452037) · [市场](https://claude.com/marketplace) · [博客](https://claude.com/blog/claude-marketplace)
- **约时：** 2026-09-24 03:21（X 显示）

### 4. Google DeepMind · Gemini 3.8 Flash / Flash-Lite TTS
- **是什么：** 展示 TTS：可逐行调语速、情绪、笑声/停顿等；音频带 SynthID；经 Gemini API / AI Studio。
- **为何重要：** 语音可控性 + 水印可识别性并行，利于内容溯源与产品体验。
- **对谁 / 深读：** 语音产品、多媒体工程 — **可略读**官方帖，跟 API 文档即可。
- **证据：** 官方自报 · [推文](https://x.com/i/status/2102781533274734801)
- **约时：** 2026-09-23 23:25（X 显示）
- **注：** 窗口内未见新的 Google 文本前沿大模型发布（Gemini 3.8 Live 系更早）。

---

## B. 网页 补强（高信号新品）

### 5. xAI · Grok 4.7 — NEW
- **是什么：** 相对 4.6 更大底座 + 更长困难多小时任务 RL；价速同 4.6（$2/$6 per 1M in/out）；fast 变体 2× 输出速度、2× 价。CursorBench 4.0 **46.3%**（4.6: 40.4%）；Terminal-Bench 4.0 **37.6%**（4.6: 20.3%）。已进 Cursor / Grok Build / API；Copilot 渐推。
- **为何重要：** 同价提 coding/agent 基准，直接影响 IDE 默认模型选型。
- **对谁 / 深读：** 工程/IDE 用户 — **值得对照**自家工作流；分数为公司表。
- **证据：** [公告](https://x.ai/news/grok-4-7) · 日期 2026-09-21

### 6. Anthropic · Claude Opus 5.5 — NEW
- **是什么：** Claude **5.5** 家族首发；公司称多数工作约 Fable 5.1 级；典型工作负载成本约低 **40%** vs Opus 5；$4/$20；缓存读 $0.20；输出快 >30%。API `claude-opus-5-5`；云厂上架。公司 bench：Terminal-Bench 4.0 **66.4%**；CursorBench 4.0 **57.8%** 等。Sonnet/Haiku 5.5「数周内」。
- **为何重要：** 与同周 OpenAI/xAI 同场竞价；成本+速度双降是主叙事。
- **对谁 / 深读：** 全员关注 — **值得深读**官方页与安全条款（Fable 级 cyber/bio + Life Sciences Verification）。
- **证据：** [公告](https://www.anthropic.com/claude-opus-5-5) · 2026-09-22

### 7. OpenAI · GPT-6 Sol & Luna — NEW
- **是什么：** Sol=复杂 coding/agents；Luna=高吞吐聚焦任务。相对 GPT-5.6 促销价 API 再降约 **50%**（公司）。Docs：Sol **$2/$10**；Luna **$0.10/$0.50**；均为 **1,050,000** 上下文 / **128k** max out。ChatGPT Work + Codex + API `gpt-6-sol`/`gpt-6-luna`。
- **为何重要：** 同代「重/轻」双型号 + 激进降价，重塑默认路由。
- **对谁 / 深读：** 工程/产品 — **值得对照** docs 价与限额；社区帖+docs 双源。
- **证据：** [社区公告](https://community.openai.com/t/announcing-gpt-6-sol-and-gpt-6-luna-in-the-api-codex-and-chatgpt/1399925) · [Sol](https://developers.openai.com/api/docs/models/gpt-6-sol) · [Luna](https://developers.openai.com/api/docs/models/gpt-6-luna) · 2026-09-22

### 8. 小米 · MiMo-V2.6（Pro / Flash / Distill）— NEW
- **是什么：** 全模态 MoE 开源（MIT）：Pro + Flash + Distill-Qwen-9B；公司称 Pro 在 Artificial Analysis Intelligence Index **46**；开 7k+ RL 环境与技术报告；UltraSpeed 声称最高约 **20×** 推理；桌面客户端+会员。
- **为何重要：** 开源权重+RL 基建同期放，国内/开源路线重要一手。
- **对谁 / 深读：** 开源工程、本地部署 — **值得扫**官方新闻与 HF collection；AA 排名/美元对比=公司口径。
- **证据：** （部分为公司自称）· [英文新闻](https://mimo.mi.com/docs/en-US/news/latest/v2-6) · 2026-09-21/22

### 9. Meta · Muse Realtime Avatar — NEW
- **是什么：** Muse Realtime Voice 的 speech VQ → 实时表情数字人（肖像到全身）；共享 token 流同步唇形/表情。服务：**448×768 @ 25fps**；约 **870 ms** 话轮结束→首包音视频；每 GB200 **12** 路并发；蒸馏学生 **2** NFE vs 教师 **120**（约 60×）；Video Seal 水印；18+。
- **为何重要：** 语音—形象端到端低延迟产品化，带水印与吞吐数字。
- **对谁 / 深读：** 多模态/实时交互 — **值得深读**研究博客数字段。
- **证据：** [研究博客](https://research.meta.ai/blog/bringing-your-muse-to-life) · 2026-09-23

### 10. Light Origins · Light-O1 / Preview — NEW
- **是什么：** 人视频→结构化全身动作；LightBot + Unitree G1 演示。开源 **Light-O1-Preview 6B**（Apache 2.0，树→Qwen3.5-4B-Base）；文本→运动；真机仍需独立控制器。公司称最多约 **100k** 人动作小时；RoboCasa GR-1 24 任务宏成功 **79.3%**（自跑评测）。
- **为何重要：** 开源「视频/文本到全身动作」预览，机器人策略栈可插。
- **对谁 / 深读：** 机器人/具身 — **值得扫** HF + 报告；成功率=自报评测。
- **证据：** （主源公司；RuntimeWire 二手）· [报道](https://runtimewire.com/article/light-origins-light-o1-human-video-robot-actions) · 2026-09-21

### 11. UiPath · Cartographer — NEW
- **是什么：** 企业「工作地图」：规则/例外/负责人 → 设计文档与可构建规格；Prebuilt Maps、Process Atlas；接 Maestro + Decision Ledger。
- **为何重要：** 流程知识→可自动化规格，企业 agent 落地层。
- **对谁 / 深读：** 企业自动化 — **可略**，IR 公告级。
- **证据：** [IR](https://ir.uipath.com/news/detail/467/uipath-launches-uipath-cartographer-helping-enterprises-turn-scattered-process-knowledge-into-an-actionable-view-of-how-their-business-runs) · 2026-09-23 · Available now

### 12. Teradata · Tera Context Engine + Harness + Agent Skills — NEW
- **是什么：** 企业数据「同事」：Context Engine（受管知识）、Harness（执行路由）、Agent Skills。公司对比同 Opus 5 的 Claude Code：SWE-bench Pro 上少 **73%** token、快 **42%**、成本低 **58%**（自有方法）。**可用：Q4 2026**（未 GA）。
- **为何重要：** 数据平台厂商进 agent 编排；数字需标注方法与未 GA。
- **对谁 / 深读：** 企业数据/平台 — **可略**；等 GA 再跟。
- **证据：** [PR](https://www.prnewswire.com/news-releases/teradata-transforms-tera-into-an-agentic-coworker-introduces-tera-context-engine-and-tera-harness-302885832.html) · 2026-09-22

---

## C. 窗外对照（仅上下文，不计入本窗新品）
- Claude Fable/Mythos 5.1（2026-09-01）— Opus 5.5 对标基线  
- GPT-6 Astra（2026-09-03）— Sol/Luna 同代便宜/快线定位  
- Gemini 3.8 Live（2026-09-15）— 本窗无新 Google 文本前沿大模型

---

## 三、GitHub 发布与热仓

**窗口**: 2026-09-21 09:00 → 2026-09-24 09:11 SGT ≈ `2026-09-21T01:00Z` → `2026-09-24T01:11Z`  

---

## 重要发布

### 1. vLLM 0.30.0：DeepSeek-V4.1-Flash 等新模型 + Fast Start 权重缓存
- **一句话**：推理引擎大版本，窗口内发布 `v0.30.0`（762 commits / 315 contributors），官方亮点含 DeepSeek-V4.1-Flash（含 MXFP8 KV / FlashMLA）、IPC 权重热缓存、HiSparse、Model Runner V2 等。
- **为何重要**：服务端推理栈的一次集中能力跃迁；新模型接入与冷启动/稀疏 MLA 路径直接决定能否跟上当周模型发布节奏。
- **对谁有用 / 深读建议**：推理平台、云厂商、自建 serving；优先读 Release Highlights 中 New models / Fast Start / HiSparse / Model Runner V2 四节，再对照本仓 `llm-compressor` 0.14.0 量化侧配套。
- **证据** ：版本 `v0.30.0` · 发布 `2026-09-22T05:20:54Z`（SGT 2026-09-22 13:20）· 星数 **92551** · - [Release v0.30.0](https://github.com/vllm-project/vllm/releases/tag/v0.30.0)  
  - [仓库](https://github.com/vllm-project/vllm)

### 2. llama.cpp 0.5.0（伴随 ggml 0.25.x）：本地推理版本跃迁
- **一句话**：`ggml-org/llama.cpp` 发布正式版 `v0.5.0`；同窗 `ggml` 发 `v0.25.0`/`v0.25.1`，Release 聚焦后端性能、模型覆盖与 server/router 稳健性。
- **为何重要**：本地/边缘部署的事实标准库；0.5.0 级版本号通常意味着可感知的 API/能力打包，而非日常 `bxxxx` 夜构建。
- **对谁有用 / 深读建议**：端侧、GGUF 生态、自托管 OpenAI 兼容 server；对照 Overview/Highlights（CUDA conv2d、Metal MoE/SSM fusion、多地址 bind）与 New models（MiMo-V2.6、HunyuanOCR 等）。
- **证据** ：`llama.cpp` `v0.5.0` · `2026-09-23T20:50:06Z`（SGT 2026-09-24 04:50）· 星数 **129351** · ；`ggml` `v0.25.0` · `2026-09-23T08:33:09Z`（SGT 2026-09-23 16:33）· 星数 **15402** · - [llama.cpp v0.5.0](https://github.com/ggml-org/llama.cpp/releases/tag/v0.5.0)  
  - [ggml v0.25.0](https://github.com/ggml-org/ggml/releases/tag/v0.25.0)

### 3. OpenAI Codex 0.156：全屏 TUI / 语音默认开 + 模型目录纳入 GPT-6 Sol/Luna
- **一句话**：稳定版 `rust-v0.156.0` 带来可选全屏 UI、默认语音会话、`/usage` 分析与 worktree 默认开启；热修 `rust-v0.156.1` 将 GPT-6 Sol / Luna 写入模型选择器。
- **为何重要**：官方终端 coding agent 的产品功能面（语音、多会话/worktree）与新模型标识同窗落地，是「agent 产品」与「模型目录」联动的可核实证据。
- **对谁有用 / 深读建议**：Codex 用户与 agent harness 作者；读 0.156.0 New Features，再用 0.156.1 changelog 核对模型名是否已进 picker（与下方 openai-python 标识对齐）。
- **证据** ：`rust-v0.156.0` · `2026-09-22T19:51:01Z`（SGT 2026-09-23 03:51）· ；`rust-v0.156.1` · `2026-09-23T02:41:36Z`（SGT 2026-09-23 10:41）· ；仓星 **126183** · - [0.156.0](https://github.com/openai/codex/releases/tag/rust-v0.156.0)  
  - [0.156.1](https://github.com/openai/codex/releases/tag/rust-v0.156.1)  
  - 配套 SDK（同窗）：[openai-python v3.18.0 加入 GPT-6 Sol/Luna 标识](https://github.com/openai/openai-python/releases/tag/v3.18.0)（`2026-09-22T18:25:48Z`）· ### 4. Claude Code 2.1.280：默认 Opus → Claude Opus 5.5；SDK/网关同日跟上
- **一句话**：`v2.1.280` 将 `claude-opus-5-5` 设为默认 Opus（官方自报 1M context、$4/$20 per Mtok）；同日 `anthropic-sdk-python` `v1.8.0` 声明支持该模型、inline tool defs 与 MCP tool-list pinning（beta）；次日 `v2.1.281` 强化 Claude apps gateway（Bedrock assume_role / guardrail 等）。
- **为何重要**：默认模型切换是全量 Claude Code 用户的行为变更；SDK 与 CLI 同窗对齐，便于应用层立刻调用。
- **对谁有用 / 深读建议**：Claude Code / Anthropic API 集成方；先读 CLI 2.1.280 变更条目，再读 SDK 1.8.0 Features；企业网关场景续读 2.1.281。
- **证据** ：`v2.1.280` · `2026-09-22T16:38:14Z`（SGT 2026-09-23 00:38）· ；`v2.1.281` · `2026-09-23T19:19:15Z`（SGT 2026-09-24 03:19）· ；仓星 **147812** · ；SDK `v1.8.0` · `2026-09-22T16:25:23Z` · - [claude-code v2.1.280](https://github.com/anthropics/claude-code/releases/tag/v2.1.280)  
  - [claude-code v2.1.281](https://github.com/anthropics/claude-code/releases/tag/v2.1.281)  
  - [anthropic-sdk-python v1.8.0](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.8.0)  
  - 注：定价/上下文长度为 **官方自报**（见 Release 正文），非第三方基准。

### 5. llm-compressor 0.14.0：GPTQ Triton 路径官方自报约 15×
- **一句话**：`vllm-project/llm-compressor` `0.14.0` 以 Triton GPTQ kernel、同形层 batching、MSE/iMatrix observer 与 MoE/REAP 改进为主；官方自报 GPTQ 端到端约 **15×**、部分 MoE 约 **30×**。
- **为何重要**：与同窗 vLLM 0.30 形成「serving + 量化压缩」双侧更新；量化吞吐是大规模部署的硬瓶颈。
- **对谁有用 / 深读建议**：模型压缩/部署团队；核对 Key Highlights 中 GPTQ / Observers / Model-Free PTQ，自行复测后再采信倍数。
- **证据** ：`0.14.0` · `2026-09-22T18:59:17Z`（SGT 2026-09-23 02:59）· 星数 **3814** · ；性能倍数为 **官方自报**  
  - [Release 0.14.0](https://github.com/vllm-project/llm-compressor/releases/tag/0.14.0)

---

## 热仓

### 6. unreallabsai/unreal-agent：窗口内新建的 async-first agent harness
- **一句话**：仓库 `created` 于窗口内（`2026-09-21T23:14:02Z`），定位 Async-first agent harness；同窗已发 `v0.1.0`→`v0.2.0`，查询时星数 **1726**。
- **为何重要**：相对「老仓持续涨星」，窗口内从 0 起盘且迅速过千星的 harness，适合观察 agent 运行时抽象是否出现新共识接口。
- **对谁有用 / 深读建议**：agent 基建作者；先看 README/Release，再评估 API 稳定度（目前版本仍幼）。
- **证据** ：创建时间 / 星数 / Releases · - [仓库](https://github.com/unreallabsai/unreal-agent)  
  - [v0.2.0](https://github.com/unreallabsai/unreal-agent/releases/tag/v0.2.0)（`2026-09-23T19:15:48Z`）

### 7. GitHub Trending（weekly）上的 agent 工作台：stablyai/orca
- **一句话**：公开 [GitHub Trending (weekly)](https://github.com/trending?since=weekly) 列表收录；定位「fleet of parallel agents」ADE，可用自有订阅跑多种 coding agent；查询时星数 **76625**，窗口内有 `v1.4.207`/`v1.4.209` 发布。
- **为何重要**：反映「多 agent 并行 IDE/运行时」仍是社区热度主轴；与 Codex/Claude Code 单 agent CLI 形成互补叙事。
- **对谁有用 / 深读建议**：工程负责人评估多 agent 编排工具；Trending 位次会变，以当页与 Release 为准，勿外推历史排名。
- **证据** ：星数 **76625** · ；Release ；Trending 入选为抓取当时页面观测（页面即时变化 → 排名本身 **** 复验）  
  - [仓库](https://github.com/stablyai/orca)  
  - [v1.4.209](https://github.com/stablyai/orca/releases/tag/v1.4.209)（`2026-09-23T05:25:28Z`）  
  - [Trending weekly](https://github.com/trending?since=weekly)

---

## 关键 org（补充）

### 8. NVIDIA/SkillSpector v2.12.0：Agent Skills 安全扫描继续加码
- **一句话**：窗口内发布 `v2.12.0`（正文称 candidate；publication pending），增加 opt-in CLI gate、静态分析配额、OpenCode 集成等；查询时星数 **18182**。
- **为何重要**：Skills/MCP 供给链安全工具与 agent 生态扩张同向；适合作为「热度之外的安全面」一条。
- **对谁有用 / 深读建议**：安全/平台团队；读 Summary 后在内网 skills 仓试跑，注意 Release 自报的 candidate 状态。
- **证据** ：`v2.12.0` · `2026-09-23T22:28:18Z`（SGT 2026-09-24 06:28）· 星数 **18182** · ；candidate 状态为 **官方自报**  
  - [Release v2.12.0](https://github.com/NVIDIA/SkillSpector/releases/tag/v2.12.0)

---

---

## 四、Hugging Face / 模型

- **窗口（Asia/Singapore）**：2026-09-21 09:00 → 2026-09-24 09:11
- **对应 UTC**：≈2026-09-21 01:00 → 2026-09-24 01:11
- **落盘**：`/workspace/daily-2026-09-24/packs/model.md`
- **用途**：只交素材；---

## 本窗高信号（优先）

### 1. 小米 MiMo-V2.6 全家桶上架（本窗新发）
- **人话一句**：小米官方把「用大规模强化学习把模型越训越强」的 MiMo-V2.6 系列权重放到了 Hugging Face，含旗舰 Pro、更省算力的 Flash，以及给研究用的 9B 蒸馏起点。
- **为何重要**：本窗 Trending 里同时出现 Pro-RL / Flash-RL / Distill-Qwen-9B（创建约 9/21–22 UTC），是窗口内最清晰的「大厂新系列」信号；卡片强调原生多模态（文/图/视频/音频）、约 1M 长上下文，以及跨编码·智能体·视觉·网络安全的一次混合 RL（You Only RL Once）。
- **对谁有用 / 深读建议**：跟 agent / 编程智能体、开源 RL 路线的人优先看技术报告与 Distill 卡上的评测表；要落地可先 Flash，要研究起点看 Distill。
- HF `createdAt` 均在窗内（Pro/Flash ≈2026-09-21T15:39Z，Distill ≈2026-09-21T18:18Z）；`lastModified` ≈9/22；采集时 likes ≈449 / 426 / 406，downloads ≈4070 / 13243 / 3253。license=mit。Distill 基座标注为 `Qwen/Qwen3.5-9B`。
- ****：Pro/Flash 的参数量与官方榜单数字以技术报告 PDF / [博客](https://mimo.xiaomi.com/mimo-v2-6) 为准，本包不摘抄未交叉验证的分数。
- **链接**：
  - [XiaomiMiMo/MiMo-V2.6-Pro-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
  - [XiaomiMiMo/MiMo-V2.6-Flash-RL](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL)
  - [XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B)
  - 技术报告：[MiMo_V2_6_technical_report.pdf](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/main/MiMo_V2_6_technical_report.pdf)

### 2. Apple LensVLM-9B：压缩视觉文本 + 选择性展开（本窗新发）
- **人话一句**：苹果发了一个 9B 视觉语言模型：先把整份文档压成「小图」扫一眼，再用学到的工具只把相关页展开成高清再读，省上下文。
- **为何重要**：标签与卡明确指向 long-context / visual-text-compression；基座为 `Qwen/Qwen3.5-9B`；有论文 arXiv:2605.07019 与配套代码仓，是窗口内「大厂研究型 VLM」而非魔改 GGUF。
- **对谁有用 / 深读建议**：做长文档 VLM、视觉压缩、工具调用式阅读的人；先读论文摘要再跑官方 demo。
- `createdAt` 2026-09-21T18:18Z，`lastModified` 2026-09-22T21:06Z；likes≈111，downloads≈233；pipeline=`image-text-to-text`；license=`apple-amlr`。
- ****：压缩倍率与端到端效果以论文 / GitHub 评测为准。
- **链接**：
  - [apple/LensVLM-9B](https://huggingface.co/apple/LensVLM-9B)
  - 论文：[arXiv:2605.07019](https://arxiv.org/abs/2605.07019)
  - 代码：[apple-aiml-research/ml-lensvlm](https://github.com/apple-aiml-research/ml-lensvlm)

### 3. Black Forest Labs FLUX.3 Action：开源「世界动作」机器人权重（本窗新发）
- **人话一句**：BFL 放出约 7B 的世界动作模型：看相机画面 + 机器人状态 + 文字指令，同时生成下一段动作和下一段视频帧，并给了 SO-101 / DROID 适配权重。
- **为何重要**：创作者/扩散实验室正式跨到机器人策略；`flux-3-action-base` 于 9/22 创建、9/23 仍在更新，配套 so101 / droid；与 LeRobot 生态标签绑定，是本窗少见的「生成模型厂 → 机器人」交叉信号。
- **对谁有用 / 深读建议**：机器人 VLA / 仿真到真机的人；注意卡明文：输出关节目标、需安全限位，base 是适配组件非完整策略。
- base `createdAt` 2026-09-22T10:36Z；so101 / droid 同日创建；采集时 likes ≈42 / 21 / 14；pipeline=`robotics`。
- ****：参数量与训练细节以 [BFL 文档](https://docs.bfl.ai/flux_3/flux3_action_overview) 为准；基准成绩本包不编。
- **链接**：
  - [black-forest-labs/flux-3-action-base](https://huggingface.co/black-forest-labs/flux-3-action-base)
  - [flux-3-action-so101](https://huggingface.co/black-forest-labs/flux-3-action-so101)
  - [flux-3-action-droid](https://huggingface.co/black-forest-labs/flux-3-action-droid)
  - [FLUX.3 Action collection](https://huggingface.co/collections/black-forest-labs/flux-3-action-6ab25aef555dd30ab86567f8)

### 4. Qwen-Image-2.1：官方卡更新 + 生态继续热（窗内更新 / 热度延续）
- **人话一句**：通义约 7B 文生图+编辑模型继续在 Trending 前列；官方卡在本窗有修改，Comfy / Unsloth 量化包也在窗内更新。
- **为何重要**：上期已报新发；本窗是「官方维护 + 部署生态跟上」而非全新叙事。卡强调透明图（RGBA）、最多 10 张参考图、局部编辑。
- **对谁有用 / 深读建议**：本地出图 / Comfy 工作流；跟官方卡与 [博客](https://qwen.ai/blog?id=qwen-image-2.1) 即可，不必当全新头条。
- 官方 `lastModified` 2026-09-21T04:50Z（窗内）；likes≈2038，downloads≈28407。旁证：`Comfy-Org/Qwen-Image-2.1` 窗内仍热；`unsloth/Qwen-Image-2.1-GGUF` 9/21 创建、9/22 更新（likes≈149，dl≈26739）。
- ****：与 2.0 的画质对比以官方示例为准。
- **链接**：
  - [Qwen/Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)
  - [Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1)
  - [unsloth/Qwen-Image-2.1-GGUF](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF)

---

## 次要 / 可并入旁线

### Altworld/Hemmingway-1（窗内更新，写作向 27B）
- **人话**：主打「日常消息写得像人」的 27B 开源权重（基座 `Qwen/Qwen3.8-27B`），卡内自报 CommunicationBench 等对比；9/22 仍在改卡。
- **定位**：产品向写作模型热度，非大厂基础模型；自报榜单 ****。license=`cc-by-nc-4.0`。
- `createdAt` 2026-09-20T12:10Z（窗前），`lastModified` 2026-09-22T16:48Z（窗内）；likes≈577，downloads≈3787。
- **链接**：[Altworld/Hemmingway-1](https://huggingface.co/Altworld/Hemmingway-1)

### 其他窗内 org 动静（低优先）
- **NVIDIA**：[nvidia/Nemotron-3-Diarization](https://huggingface.co/nvidia/Nemotron-3-Diarization) 等 diarization / VoiceChat 卡 9/22–23 有修改 → 语音分离/对话旁线（likes≈130）。
- **腾讯**：[tencent/EVIE-8B](https://huggingface.co/tencent/EVIE-8B)（视觉文档检索）9/22 更新（likes≈29，dl≈863）。
- **Edge0**：[Edge0/Audio8-ASR-Infinite](https://huggingface.co/Edge0/Audio8-ASR-Infinite) 9/21 新发（likes≈48，观察）。
- **Yandex**：[yandex/AliceAI-Foundation-80B-A3B-Base](https://huggingface.co/yandex/AliceAI-Foundation-80B-A3B-Base) 9/22 更新（MoE 底座热度，likes≈296）。

---

## 热度延续（非本窗新发，勿当头条）

| 模型 | 说明 | 链接 |
| --- | --- | --- |
| prism-ml/Ternary-Bonsai-2-27B-gguf | 上期已报；本窗仍 Trending，修改日早于窗 | [卡](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf) |
| XingChen-AGI/Xing4.0-29B-A4B | 上期已报；热度延续 | [卡](https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B) |
| deepseek-ai/DeepSeek-V4.1-Flash | 修改日 9/10，热度延续 | [卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) |

窗内相关：[prism-ml/Ternary-Bonsai-2-27B-mlx-2bit](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-mlx-2bit) 于 9/22 有更新（量化旁支，likes≈358）。

---

---

## 数据集（一笔带过）
- 窗内有改动但信号一般（推理过滤集、A 股盘口类等），非必须头条。
- 热度延续：arxiv 全集、CAD 语音小时数等，非本窗新发头条。

---

---

## 附录 A · arXiv 原始摘录

Coverage window (requested): **2026-09-21 09:00 → 2026-09-24 09:11 SGT**  

## Coverage notes

| Source | What was visible at pack time |
|--------|-------------------------------|
| `[new`](https://arxiv.org/list/cs.AI/new`) | **Wed, 23 Sep 2026** (101 new / 139 cross / 126 replacements) |
| `[new`](https://arxiv.org/list/cs.CL/new`) | **Wed, 23 Sep 2026** (80 new / 28 cross / 61 replacements) |
| `[new`](https://arxiv.org/list/cs.LG/new`) | **Wed, 23 Sep 2026** (118 new / 98 cross / 109 replacements) |
| RSS `rss.arxiv.org/rss/cs.{AI,CL,LG}` | **Non-empty**; all sampled items dated **Wed, 23 Sep 2026 00:00:00 -0400** (AI 366 / CL 169 / LG 325 items) |
| Pastweek `cs.AI` | Wed 23 (240); Tue 22 (384, paginated); **Mon 21 (125)** |
| Pastweek `cs.CL` | Wed 23 (108); Tue 22 (233); **Mon 21 (87)**; Fri 18 (partial) |
| Pastweek `cs.LG` | Wed 23 (216); Tue 22 (426, paginated); **Mon 21 (149, paginated)** |
| **Thu, 24 Sep 2026** announce batch | **Not yet visible** on `/new` (still showing Wed 23 at ~09:35 SGT) |

Announce days in pack: **Mon 21 / Tue 22 / Wed 23** (Thu 24 not available yet).  
Selection rule: 宁缺毋滥, max 5; prefer big-lab affiliations **or** hot topics (agents / alignment / cyber / RSI / frontier / coding agents). Affiliations verified from abs/html and/or PDF page 1 — **no invented posts**.

Near-misses (seen, not packed): `2609.25501` Continuous Optimization for p-adic Models (**Google DeepMind**, Wed 23, niche p-adic GD); `2609.26419` Reliability Theory for AI Control (solo author analyzing DeepMind rogue-deployment defenses); `2609.22178` Beyond Task Completion / SCOPE (Shanghai AI Lab, safe CUAs).

---

## Picks (5)

### 1. RRSI: Regularized Recursive Self-Improvement of Agent Harnesses
- **id:** `2609.24972`
- **title:** RRSI: Regularized Recursive Self-Improvement of Agent Harnesses
- **abs:** [2609.24972](https://arxiv.org/abs/2609.24972)
- **announce day:** Tue, 22 Sep 2026 (cs.LG primary; also cs.AI / cs.CL)
- **affiliations (PDF p.1):** Google Cloud AI Research; UNC-Chapel Hill; Stanford University; Washington University in St. Louis
- **1-sentence claim:** Regularizing harness-level RSI (annealed edit budgets + critic/pruner) improves OOD transfer and cuts policy tokens vs unregularized harness evolution.
- **why it matters:** Practical RSI is migrating from weight updates to **agent harness** search; this is a Google line of work explicitly tackling evolve-set overfitting — the main failure mode of recursive harness self-improvement.
- **metrics (paper-reported) vs :**
  - Up to **+14.1** points on the evolve split; up to **+4.7** on five OOD benchmarks; harness uses **~30% fewer** policy tokens than unregularized evolution — **** (which eight benchmarks, backbone model(s), variance across seeds).

### 2. OSWorld-Pro: Process-based Evaluation for Computer Use Agents
- **id:** `2609.24890`
- **title:** OSWorld-Pro: Process-based Evaluation for Computer Use Agents
- **abs:** [2609.24890](https://arxiv.org/abs/2609.24890)
- **announce day:** Tue, 22 Sep 2026 (cs.CL primary; also cs.AI / cs.LG)
- **affiliations (PDF p.1):** NVIDIA
- **1-sentence claim:** Process-level CUA evaluation with 300+ tasks / 2800+ subgoals / 67k+ human annotations exposes failure modes that end-state OSWorld scores hide.
- **why it matters:** Computer-use is a frontier agent surface; NVIDIA’s process benchmark gives **partial credit + failure taxonomy** (e.g. click errors vs subgoal-irrelevant actions) needed to improve CUAs beyond binary task success.
- **metrics (paper-reported) vs :**
  - Claude Opus 5: **75.7%** on OSWorld-Pro vs **83.4%** on OSWorld — **** (exact scoring protocol for subgoal judges; model list beyond Opus 5; judge agreement).

### 3. Recursive self-improvement of AI research agents
- **id:** `2609.26457`
- **title:** Recursive self-improvement of AI research agents
- **abs:** [2609.26457](https://arxiv.org/abs/2609.26457)
- **announce day:** Wed, 23 Sep 2026 (cs.AI primary; also cs.LG / cs.SE)
- **affiliations (HTML/PDF p.1):** Weco AI
- **1-sentence claim:** AIDE² recursively rewrites its own research-agent code over an 8-day autonomous run, yielding seven successive improvements that transfer to held-out AI R&D benchmarks and reduce reward hacking.
- **why it matters:** Direct empirical **RSI** on a frontier AI research agent (not just a coding toy loop) — core “agents improving agents” signal for digest readers tracking recursive capability gain.
- **metrics (paper-reported) vs :**
  - **7** accepted self-improvements in **8** days; strongest discovered agent matches/exceeds a strong human-engineered production agent on **4** held-out benchmarks (incl. OOD weather forecasting); reward-hacking rate **55% → 32%** (7 pp below human-engineered agent) — **** (compute budget, hidden-eval leakage controls, FML-Bench ranking details).

### 4. CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents
- **id:** `2609.26779`
- **title:** CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents
- **abs:** [2609.26779](https://arxiv.org/abs/2609.26779)
- **announce day:** Wed, 23 Sep 2026 (cs.AI primary; also cs.LG / cs.SE)
- **affiliations (PDF p.1):** Carnegie Mellon University; Bosch Center for AI
- **1-sentence claim:** Faithful truncate/drop-only autocompaction (never rewrite; never compact a compaction) cuts long-horizon coding-agent cost ~50% while improving Terminal-Bench efficiency and KernelBench continual-learning speedups.
- **why it matters:** Context compaction is the bottleneck for million-token coding agents; a scaffold-agnostic, drift-resistant method that also helps **test-time scaling** cost curves is immediately actionable for coding-agent builders.
- **metrics (paper-reported) vs :**
  - Up to **~50%** cost reduction under bounded context; **+10+ pp** Terminal-Bench from TTS for less than two full-context runs; KernelBench CUDA speedups **2.23×  steps / 3.58×  steps**; under parallel TTS, Kimi K2.6 matches Opus 4.7 and beats Opus 4.6 / GPT-5.3 Codex at lower cost — **** (exact Terminal-Bench numbers, harnesses, and fair cost accounting vs Claude Code microcompaction).

### 5. Evaluating Coding Agents on Kernel Exploit Generation
- **id:** `2609.25591`
- **title:** Evaluating Coding Agents on Kernel Exploit Generation
- **abs:** [2609.25591](https://arxiv.org/abs/2609.25591)
- **announce day:** Wed, 23 Sep 2026 (cs.AI primary; also cs.CR)
- **affiliations (PDF p.1):** University of Illinois Urbana-Champaign; Independent Researcher; Ministry of National Defense, Republic of Korea
- **1-sentence claim:** KEX-bench measures whether coding agents can turn real Linux/Windows kernel CVEs into verifier-checked exploit *primitives* (not just crashes), revealing a large PoC-free vs PoC-provided gap.
- **why it matters:** High-signal **cyber × coding-agents** frontier: bug-finding ≠ exploit-primitive construction; this is one of the clearest capability-boundary benchmarks for dual-use agent risk tracking.
- **metrics (paper-reported) vs :**
  - **45** tasks / **40** CVEs; without reference PoC: best config **1/20 Windows (5.0%)**, **14/25 Linux (56.0%)**; with reference PoC: **31/45 (68.9%)** — **** (which agent/model configs are “strongest”; tool-call budgets; verifier false-positive rates).

---

## Method notes
- Parsed `/new` + pastweek (with pagination) for cs.AI / cs.CL / cs.LG; cross-checked RSS for Wed 23.
- Affiliations taken from PDF page 1 and/or ar5iv HTML author notes — not from list-page author strings alone.
- Metrics quoted as stated by authors; items marked **** need independent verification before citing as fact.

---

## 附录 B · 实验室抓取日志

Window SGT: 2026-09-21 09:00 → 2026-09-24 09:11

## Fetch log
| Source | HTTP | Notes |
|--------|------|-------|
| openai.com/news/rss.xml | 200 | Many in-window items |
| anthropic.com/news | 200 | Opus 5.5 (Sep 22), enzyme (Sep 23) |
| deepmind.google/blog/rss.xml | 200 | Private AI Compute + Gemini 3.8 TTS |
| blog.google/rss/ | 200 | innovation-and-ai mirrors / product |
| ai.meta.com/blog/ | 200 | Newest ~Jul 2026 — ZERO in window |
| microsoft.com research blog | 403 | Feed also 403 — treat as unchecked / no confirmed hit |

## Hits (curated)
See yan.md. Customer-story OpenAI posts intentionally deprioritized.
