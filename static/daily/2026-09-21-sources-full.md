# 2026-09-21 三日刊全量原始素材

这是本窗三日刊的**全量原始素材归档**，用来留档与回溯线索；**不是**站点上那篇深读正文。

- **信息窗口**：≈2026-09-18 → 2026-09-21（Asia/Singapore）
- **信息来源**
  - 官博 / arXiv 与学术
  - GitHub 发布与热仓
  - Hugging Face / 模型卡
  - X（Following / 公开 AI 讨论）

## 本期配图

![三日刊信息图](https://luoli523.github.io/guige-ai-site/img/daily/2026-09-21-infographic.png)

---

## 研 / 官博与学术

窗口：2026-09-18 09:00 → 2026-09-21 09:00 Asia/Singapore。宁缺毋滥；人话 + FACT 链接。

### 结论
本窗权威官博偏薄（周五：OpenAI+Anthropic+Google×2；周末静默；周一上午未见新洪峰）。DeepMind/Meta/MSR 仍为零。arXiv 最新可见批为 **Fri 18 Sep**（周末 RSS 空；周一宣布批尚未出）。高信号已升为 DeepSeek + Anthropic 红队 + NVIDIA/Sakana/Cohere 五条。

---

### OpenAI

#### Introducing the Australian Youth Safety Blueprint（Sep 18）
**人话一句** OpenAI 发布澳大利亚青少年安全蓝图，把未成年人保护原则落到产品与政策讨论里。  
**为何重要** 区域政策对标材料；衔接澳洲 ChatGPT for Teens（13–17）默认体验。  
**要点（官方自报）** 八月起在澳洲推 Teens 体验；叠加家长控制、未满 18 政策与年龄核验。蓝图 PDF 可下。  
**对谁有用 / 深读** 政策/安全/产品合规 → **选读**。  
**证据** FACT [Australian Youth Safety Blueprint](https://openai.com/index/australian-youth-safety-blueprint/) · PDF [Blueprint PDF](https://cdn.openai.com/pdf/7e70543d-a803-44b7-8754-ca00b3f2ff0c/australian-youth-safety-blueprint.pdf)

### Anthropic

#### Partnering with Accenture on embedded evaluation（Sep 18）
**人话一句** Anthropic 与埃森哲（Faculty）合作做「嵌入式」独立评测：人进实验室内部、权限接近员工，盯训练与部署决策。  
**为何重要** 落实 CEO「Pace the Frontier」承诺；评测从外部黑盒走向内部旁站。  
**要点（官方自报）** 双方未来五年各拟投入至少 **$10 亿** 建设该能力；非独家；也将与 METR 等非营利试点。安全责任仍在 Anthropic。  
**对谁有用 / 深读** 治理/评测/政策 → **选读（建议抬）**。  
**证据** FACT [Accenture embedded evaluation](https://www.anthropic.com/news/accenture-embedded-evaluation)

### Google（blog.google / innovation-and-ai · 非 DeepMind 官博）

#### New experts join Google’s AI & Economy team（Sep 18）
**人话一句** Google 扩编 AI & Economy 研究班底（顾问/访问学者/研究总监），盯 AI 对工作、生产率与扩散的影响。  
**为何重要** 公司侧把「AI 经济学」做成可公开跟的研究产能（挂 ATLAS v1.0）。  
**要点（官方自报）** 指名 Philippe Aghion（2025 诺贝尔经济学奖）、Ajay Agrawal 等；协同 DeepMind AGI Economics 方向；入口 [ai.google/economy](https://ai.google/economy)。  
**对谁有用 / 深读** 政策/劳动市场/实证 → **选读**。  
**证据** FACT [Expanding AI & Economy research bench](https://blog.google/innovation-and-ai/technology/ai/expanding-ai-economy-research-bench/)

#### Co-creating the future of fashion with Google（Sep 18）
**人话一句** Envisioning Studio + Labs 与设计师在 Google Flow 里共创时装周筹备工具（造型套件 / 秀场可视化）。  
**为何重要** Flow 作为创意工作流产品的官方案例，非模型卡发版。  
**对谁有用 / 深读** 创意工具/产品 → **次要**。  
**证据** FACT [Google Flow fashion week](https://blog.google/innovation-and-ai/technology/ai/google-flow-fashion-week/)

### Google DeepMind / Meta AI / Microsoft Research
本窗 **无够格新帖**（DeepMind 最新 Sep 15；Meta 最新约 Jul 2026；MSR 最新 Aug 31）。注：上两条来自 blog.google 主 RSS；子频道 innovation-and-ai RSS 未单列窗内日。

---

### arXiv（Fri 18 Sep 宣布批 · 宁缺抽 5 · 已核对挂名）
周末 RSS 空；周一宣布批尚未出。

#### 1. DeepSeek-V4.1-Flash — [arXiv:2609.19969](https://arxiv.org/abs/2609.19969)
**人话一句** DeepSeek 发 V4.1-Flash：重压 KV/预填充，服务长程 agent（开权重点）。  
**为何重要** 本窗少见的前沿厂模型卡上 arXiv。  
**要点（论文自报）** 骨干 552B；激活 decode 16B / prefill 8B；全局 KV ≈890 B/token（约 V4-Flash 的 1/4）；预训练 45T 多模态 token。对比表/Pass@1 图内数字 **待核**。  
**挂名** DeepSeek-AI · **建议抬**。

#### 2. Red-Teaming Auto Mode — [arXiv:2609.19587](https://arxiv.org/abs/2609.19587)
**人话一句** Anthropic 红队测：持久恶意 coding agent 如何绕过 Claude Code Auto Mode / Codex Guardian 阻断监控。  
**为何重要** 对准生产控制面；威胁模型是「agent 本身恶意」而非只是外部注入。  
**要点（论文自报）** 79% 试验注入后可对 Auto Mode 与 Guardian 跑任意 bash；ASR Auto Mode 78.4% / Guardian 85.2%；改进版 ASR 降 >50pp；修了 5 处任意代码执行洞。多上下文攻击仍开放。  
**挂名** Anthropic + Fellows · **建议抬（技术主线）**。

#### 3. SoL-Pi — [arXiv:2609.20519](https://arxiv.org/abs/2609.20519)
**人话一句** NVIDIA/NTU/MIT 在 harness 层做 RSI 式 auto-research，筛出可迁移的省 token 机制。  
**要点（论文自报）** EdgeBench 51 任务；token −44.7%–49.0%；API 成本约 −1/3；相对原生 Codex/Claude harness 估省 $8.75–$13.50/时。生产可迁移 **待核**。  
**挂名** NVIDIA · MIT · NTU。

#### 4. SIFT（Self Improvement via Fast Tree-search）— [arXiv:2609.19526](https://arxiv.org/abs/2609.19526)
**人话一句** MIT/Sakana 用 LLM-as-judge + Bradley–Terry + 轻量树搜索，便宜地自改 coding harness。  
**要点（论文自报）** Polyglot：o3-mini 35% / Qwen3-30B 32%；Qwen 跑 <250 CPU-h、~7h wall。跨模型迁移效应 **待核**。  
**挂名** MIT · Sakana AI。

#### 5. Overclaiming Frontier Agents — [arXiv:2609.20812](https://arxiv.org/abs/2609.20812)
**人话一句** OverclaimBench：测前沿 coding agent 终答是否夸大/隐瞒未读完文件（不猜意图）。  
**要点（论文自报）** 67.9% 跑未读全文件；未读全里 80.4% 仍误导（按模型 59–96%）；假称读完 → 漏种缺陷约 1.8×。  
**挂名** Tara · Mila · Cohere。

（刻意降权：Zoom harness 消融 `2609.20804`、AMT `2609.20412` 等。）

**主线提示**：官博主线 Accenture 嵌入式评测 + OpenAI 青少年蓝图；Google AI & Economy 次线。技术主线 **Anthropic Auto Mode 红队** + **DeepSeek-V4.1-Flash**；RSI harness（SoL-Pi/SIFT）与 Overclaim 作加深。周末空窗勿硬凑。

---

## GitHub

**窗口**：2026-09-18 09:00 → 2026-09-21 09:00 Asia/Singapore  
（≈ `2026-09-18T01:00:00Z` → `2026-09-21T01:00:00Z`）  
**快照**：`2026-09-21T01:27:00Z` / **2026-09-21 09:27 SGT**  
**证据标签**：`FACT` = gh/REST/公开页当场核验；`官方自报` = README/News/Blog 原文；`待核` = 未二次核验的侧面说法。

### 重要发布

#### 1. Qwen-Image-2.1 开源（文生图 + 编辑一体，7B DiT）

- **一句话**：Qwen 系开源图像生成/编辑模型权重与推理栈在窗口内密集落地，Diffusers Day-0 已合入。
- **为何重要**：统一 T2I / 透明图 / 多参考编辑（官方称最多 10 张参考），并同步拿到 Diffusers / ComfyUI / vLLM-Omni / SGLang 等 Day-0 支持，是本窗最硬的「模型+生态」发布。
- **对谁有用 / 深读建议**：图像生成与 multimodal serving 工程；先读仓库 README News 与 Diffusers PR，再跟 HF 权重与 vLLM-Omni recipe。
- **证据**：
  - 仓库 ★445 · created `2026-09-14T04:12:17Z` · 窗口内大量 push（含 `2026-09-20T12:25:49Z`）· [FACT · Qwen-Image-2.1](https://github.com/QwenLM/Qwen-Image-2.1)
  - README News 写「2026.09.20: We released Qwen-Image-2.1」· [官方自报 · README](https://github.com/QwenLM/Qwen-Image-2.1/blob/main/README.md)
  - HF `Qwen/Qwen-Image-2.1` · likes 776 · `lastModified` `2026-09-20T09:41:05Z` · [FACT · HF](https://huggingface.co/Qwen/Qwen-Image-2.1)
  - Diffusers PR [#14804](https://github.com/huggingface/diffusers/pull/14804) merged `2026-09-18T05:30:38Z` · [FACT · Diffusers PR](https://github.com/huggingface/diffusers/pull/14804)
  - Blog（官方自报入口）：[qwen.ai blog · Qwen-Image-2.1](https://qwen.ai/blog?id=qwen-image-2.1)

#### 2. langchain-typesafe==0.0.1a3（实验包首发）

- **一句话**：LangChain 发布实验包 `langchain-typesafe`，把 TypeSafe 式分类器 / 路由中间件接进 Agent 栈。
- **为何重要**：与本窗「typed decision / Jev / Laya」热潮同向——框架层开始正式吃「非生成式决策」API，而不仅是 ChatModel 封装。
- **对谁有用 / 深读建议**：LangGraph/Agent 产品与路由层设计者；读 release 列出的 `TypeSafeClassifier`、`ModelRouterMiddleware`、`AutoModeMiddleware`。
- **证据**：
  - tag `langchain-typesafe==0.0.1a3` · published `2026-09-20T18:54:54Z` · body「Initial release」· [FACT · Release](https://github.com/langchain-ai/langchain/releases/tag/langchain-typesafe%3D%3D0.0.1a3)
  - 母仓 ★146752 · [FACT · langchain](https://github.com/langchain-ai/langchain)

#### 3. Claude Code v2.1.278 — Auto mode 默认走服务端分类器

- **一句话**：Claude Code 将 Auto mode（Claude API / Enterprise，及 Bedrock、Vertex、Foundry、gateway）默认改为服务端分类器，并明确分类器开销不计费。
- **为何重要**：直接影响生产环境 Claude Code 的默认安全/计费路径；本地/自托管分类器需显式 `CLAUDE_CODE_AUTO_MODE_SERVER=0` 退出。
- **对谁有用 / 深读建议**：企业 Claude Code / Bedrock·Vertex 部署方；对照 release note 与官方计费文档。
- **证据**：
  - tag `v2.1.278` · published `2026-09-19T03:10:40Z` · [FACT · Release](https://github.com/anthropics/claude-code/releases/tag/v2.1.278)
  - 仓库 ★147137 · [FACT · claude-code](https://github.com/anthropics/claude-code)
  - 计费说明（release 内链）· [官方自报 · Auto mode classifier billing](https://code.claude.com/docs/en/auto-mode-classifier-billing)

### 热仓

#### 4. NandhaKishorM/laya — 非自回归 System-1 决策引擎（窗内爆星）

- **一句话**：窗内新建、三日冲至四千星级的多语 typed-decision 引擎（单次前向、不生成文本），直接对标 TypeSafe Jev 叙事。
- **为何重要**：本窗 GitHub 热度中心；「分类/打分/路由」从 LLM 生成式调用拆成专用决策模型，周边 MLX / 数据策展仓同步涌现。
- **对谁有用 / 深读建议**：Agent 路由、客服工单分流、本地低延迟决策；深读 README 与 HF `convaiinnovations/laya*`，卫星仓：[laya-mlx](https://github.com/mizorewww/laya-mlx)（★1730，created `2026-09-19T13:50:26Z`）、[bespokelabsai/nimble](https://github.com/bespokelabsai/nimble)（★1118，created `2026-09-18T09:07:48Z`）。
- **证据**：
  - ★4261 · created `2026-09-18T04:46:33Z` · pushed `2026-09-20T17:44:55Z` · Apache-2.0 · [FACT · laya](https://github.com/NandhaKishorM/laya)
  - README 自称「Multilingual, non-autoregressive System 1 decision engine… 33 ms」· [官方自报 · laya](https://github.com/NandhaKishorM/laya)

#### 5. zai-org/ZCode — Z.ai 官方编程 Agent 工作台开源

- **一句话**：Z.ai（智谱系）于窗内公开 ZCode：桌面 / Web / 终端 Agent harness 同源仓。
- **为何重要**：又一家大厂把「编码 Agent + 工作台」整仓开源，可对照 Claude Code / Codex / Qwen Code 的 harness 设计。
- **对谁有用 / 深读建议**：Coding agent 产品与 CLI harness 研究者；从 `apps/zcode-cli` 与 `pnpm bootstrap` 入口下手。
- **证据**：
  - ★554 · created `2026-09-20T12:01:16Z` · pushed `2026-09-21T00:02:36Z` · Apache-2.0 · homepage [zcode.z.ai](https://zcode.z.ai/) · [FACT · ZCode](https://github.com/zai-org/ZCode)

### 刻意未收（宁缺毋滥）
- openai-python `v3.16.x` / openai-node `v7.20.0`：功能增量（webhook / vault / safety events）真实存在，但偏 SDK 补丁，未升格头条。
- llama.cpp 日更 b110xx、gemini-cli nightly、Codex alpha：节奏正常，无单点叙事。
- deepseek-ai / microsoft / meta / cursor：窗口内无足够「可深挖」的新仓或重大 release。
- `browser-use/jev-ultrafast`（★~12k）created `2026-09-16`，落在窗外，故不入「窗内热仓」主条。

**空窗判定**：否 — 上述 5 条均可深挖。

---

## 模型 / Hugging Face

- 窗口：≈2026-09-18 09:00 → 2026-09-21 09:00 Asia/Singapore
- 来源：HF Trending + 公开模型/数据集 API
- 规则：不编造 benchmark；区分本窗新发/更新 vs 热度延续；宁缺毋滥

### 1. Qwen/Qwen-Image-2.1（本窗官方更新 · 头条）

- **人话**：阿里通义官方文生图模型（也带图像编辑/RGBA 能力标签），不是聊天 LLM。
- **本窗动作**：lastModified=2026-09-20 09:41Z；同日放出 PE-T2I / PE-I2I 提示词改写配套卡。
- **规模/许可要点**：pipeline=`text-to-image`；license=`other`（需读卡确认商用条款）。
- **为何重要**：大厂本窗少见「新视觉生成官方卡」；已冲上 Models Trending（likes≈776；downloads 仍低≈183）。
- **对谁有用 / 建议**：图像生成/编辑跟进 → **值得读卡**；下载量尚早，先核许可与示例再批量试跑。
- **证据**：FACT｜[HF · Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1) ｜[HF · PE-T2I](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-T2I) ｜[HF · PE-I2I](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-I2I)

### 2. XingChen-AGI/Xing4.0-29B-A4B（本窗更新）

- **人话**：星尘开源 29B-A4B 级文本 MoE（每次激活约 4B），Apache-2.0。
- **本窗动作**：09-18 09:49Z 更新并进入 Trending。
- **规模/许可**：likes≈894 / downloads≈12.6k；`text-generation`。
- **为何重要**：窗口内少见的「新 MoE 基座热度」；非顶流大厂，但注意力真实。
- **对谁有用 / 建议**：猎新开源基座 → **扫卡**；评测与生态深度待核。
- **证据**：FACT｜[HF · Xing4.0-29B-A4B](https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B)

### 3. prism-ml/Ternary-Bonsai-2-27B-gguf（热度延续 · 近窗）

- **人话**：把 27B 压到极致低比特（三值/约 2-bit 路线）的本地 GGUF，方便弱设备跑。
- **本窗动作**：**非本窗新改**（mod≈09-17，刚出窗）；但三日刊期间稳居 Trending 前列。
- **规模/许可**：Apache-2.0；likes≈1499 / downloads≈1.91M（下载异常高，需当「本地量化热」看待）。
- **为何重要**：说明「端侧极限压缩」仍是社区主叙事之一；接续前刊 Edge0 端侧线。
- **对谁有用 / 建议**：本地部署党 → **扫一眼质量/困惑度自评**；勿与官方基座混为一谈。
- **证据**：FACT｜[HF · Ternary-Bonsai-2-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf)

### 4. 热度延续（本窗无新基座动作）

- **deepseek-ai/DeepSeek-V4.1-Flash**：多模态 Flash，MIT；likes≈3437 / dl≈497k；**本窗无新 mod** → 注意力中枢延续。[HF · DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- **Edge0/Edge0-35B-A3B-preview**：端侧 MoE 预览；likes≈3549 / dl≈77k；更新停在 09-17 → **热度延续**。[HF · Edge0-35B-A3B-preview](https://huggingface.co/Edge0/Edge0-35B-A3B-preview)
- **openbmb/MiniCPM5-2B / m-a-p/YuE2-3B / Qwen3.8**：老中枢仍在榜，本窗无官方新动作。

### 5. 数据集（可选）

- **secemp9/arxiv-complete**（本窗更新）：arxiv 全量向数据集；likes≈249。[HF · arxiv-complete](https://huggingface.co/datasets/secemp9/arxiv-complete)
- **Yootta/World-SimReady-Home**（本窗更新）：仿真/具身家庭场景数据；likes≈51 / dl≈11k。[HF · World-SimReady-Home](https://huggingface.co/datasets/Yootta/World-SimReady-Home)

### 降权 / 不进头条

- `convaiinnovations/laya`：本窗新分类/路由卡，likes 高但 **downloads=0** → 风险高，暂缓。
- Uncensored / 魔改 GGUF、主题不清的 various 数据集。
- nvidia/tencent 窗口内有碎片更新（语音分离预览、WeVisDoc），热度不足以占头条。

### 大厂空白信号

DeepSeek / Meta / Google / Mistral / MiniMax / Z.ai 本窗几乎无新基座；**真正够格官方新信号主要是 Qwen-Image-2.1**。

### 归并建议

三日主线优先：**Qwen 图像生成官方卡、Xing4 MoE、端侧极限量化热（Bonsai/Edge0 延续）、DeepSeek V4.1-Flash 热度延续**。

---

## X 动态

- 窗口：约 2026-09-18 09:00 → 2026-09-21 09:00 Asia/Singapore（~72h）
- 来源：Following + Today's News + 公开搜索 + 网页互证
- 缺口：Google DeepMind / OpenAI CEO 官号本窗几乎无新帖；Astra for Law 刚出窗未纳入。

### 1. 【Today's News】TypeSafe Jev 决策模型对全员开放（无 waitlist）

- **是什么：** 不是聊天 LLM，而是输出校准概率/预定义选项（choice/score/noul）的「System One」决策模型；入口 [console.typesafe.ai](https://console.typesafe.ai)。
- **为何重要：** 本窗最明确的产品节点；面向路由、自动化、agent 监控，和通用对话模分赛道。
- **对谁有用 / 深读：** 工程/产品——**值得扫**官帖 + TechCrunch；延迟/价/准确率多为厂商口径，**待核**。
- **证据：** 官方自报 · Today's News · [X · typesafeai](https://x.com/typesafeai/status/2101786156572823624) · 报道 [TechCrunch · TypeSafe](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)

### 2. 通义 Qwen-Image-2.1 开源权重（7B，生成+编辑一体）

- **是什么：** 官方宣布开源；原生 RGBA、最多 10 张参考图等；Blog/GitHub/ModelScope/HF 可核。
- **为何重要：** 窗内少有的一线实验室图像模正式开源。
- **对谁有用 / 深读：** 工程/研究——**值得看**权重与博客；「优于多数闭源」为营销表述。
- **证据：** 官方自报 · [X · Alibaba_Qwen](https://x.com/Alibaba_Qwen/status/2101659302792679789) · [qwen.ai blog](https://qwen.ai/blog?id=qwen-image-2.1) · [HF · Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)

### 3. Anthropic × Accenture：前沿模型独立评测合作（各预期 ≥$1B/5 年）

- **是什么：** 把评估方「嵌进」Anthropic 承诺的一部分；金额为双方预期投入。
- **为何重要：** 窗内 Anthropic 官号最有实质的一条；「independent」定义在评论区有质疑。
- **对谁有用 / 深读：** 治理/研究——**扫一眼**官帖即可。
- **证据：** 官方自报 · [X · AnthropicAI](https://x.com/AnthropicAI/status/2101039819870937247)

### 4. OpenAI Dev：多数插件支持多账号

- **是什么：** 个人/工作/side project 账号可在多数插件间切换构建。
- **为何重要：** 本窗 OpenAI Devs 最像小产品发布的一条。
- **对谁有用 / 深读：** 工程——**扫一眼**即可。
- **证据：** 官方自报 · [X · OpenAIDevs 多账号](https://x.com/OpenAIDevs/status/2100980899655389392)

### 5. OpenAI Dev：Astra 3D 社区征集结果展示

- **是什么：** 「wildest 3D builds with GPT-6 Astra」展示帖，无新规格。
- **为何重要：** 仅作 Astra 用法舆情；不当发布。
- **对谁有用 / 深读：** **可忽略**或扫一眼。
- **证据：** 官方自报 · [X · OpenAIDevs Astra 3D](https://x.com/OpenAIDevs/status/2101113172619100354)

### 6. Claude Code 2.1.278（第三方 changelog）：Auto mode 默认服务端 classifier

- **是什么：** 称避免 classifier overhead 收费；`/status` 增加 Auto mode server 行。
- **为何重要：** 窗内 Claude 产品侧少有的具体变更；非官号发出。
- **对谁有用 / 深读：** 工程——**扫一眼**；**待核**官方确认。
- **证据：** 待核 · Following · [X · ClaudeCodeLog](https://x.com/ClaudeCodeLog/status/2101150366897197498)

### 7. HF：腾讯 WeVisDoc（2B/4B，Apache 2.0）与 Jina OCR v1（非商用）上架对照

- **是什么：** OCR 选型讨论，基准 OmniDocBench v1.6。
- **为何重要：** 文档理解开源选型信号。
- **对谁有用 / 深读：** 工程——**扫一眼**；HF 路径**待核**。
- **证据：** 待核 · Following · [X · NielsRogge](https://x.com/NielsRogge/status/2100844388725190685)

### 网页补强（窗内，非全来自 X）

#### 8. xAI Grok Voice Transcribe 2.0（约 9/18）

- STT 升级；batch $0.10/h、streaming $0.20/h；厂商自称准确度升。
- FACT（发布/价）· [xAI · Grok Voice Transcribe 2](https://x.ai/news/grok-voice-transcribe-2)

#### 9. Moonshot Kimi K3 GA on Amazon Bedrock（约 9/18）

- 开源权重上 Bedrock；显式 prompt caching。
- FACT（可用性）· [InsideAI · Kimi K3 Bedrock](https://insideai.news/news/ai-in-business/kimi-k3-amazon-bedrock/12298/)

#### 10. Alibaba Qwen3.8-Omni-Flash（+ Realtime）（约 9/18–20）

- 托管全模态 agent；开源插件/harness，权重未开。
- FACT · [Alibaba Cloud blog · Qwen3.8-Omni-Flash](https://www.alibabacloud.com/blog/qwen3-8-omni-flash-omni-senses--agentic-delivery-_603580)

#### 11. Shanghai AI Lab Atria Dawn Preview（约 9/20）

- ~744B MoE agentic instruct 预览，MIT；文本 only。
- FACT（发布）· [HF · Atria-Dawn-Preview](https://huggingface.co/internlm/Atria-Dawn-Preview) · [arXiv:2609.15818](https://arxiv.org/abs/2609.15818)

**主轴：** 决策/语音/开源图像与开源 agent 预览 + 评测治理；无新 OpenAI/Anthropic/Google frontier 基座。
