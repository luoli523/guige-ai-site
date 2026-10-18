# 2026-10-18 AI行业动态 · 原始素材整理稿

这是 2026-10-18 一期的素材附件，信息窗口约 3 天：2026-10-15 09:16 → 2026-10-18 09:18（Asia/Singapore）。

下面是各路信源采回、经初步交叉核对的全量原始素材，比正文多、也更粗糙，不是深读正文，供想自己核对的读者下载查阅。标注「待核」的条目请以原始链接为准，厂商和论文数字除特别说明外均为官方自报。上期（10-15）已写过的 Gemini 4 Argon 开放、Meta Muse Wonder、Anthropic 反蒸馏、Scion 等，只在有新进展时出现。

- **官方博客与 arXiv**：Anthropic、Meta、NVIDIA、Google、Google Research、Microsoft Research、OpenAI 等官博条目，以及 cs.AI / cs.CL / cs.LG 中大厂署名或高信号的预印本。
- **X**：主要实验室官方账号原帖、AI 讨论和 X 新闻摘要。
- **GitHub**：重要 Release 与关键组织新仓库。
- **Hugging Face**：Trending 与重点组织的新模型卡、数据集和榜单快照。

---

# 一、官方博客与 arXiv（精选）
窗口：2026-10-15 09:16 → 2026-10-18 09:18 SGT。官博 9 条 + arXiv 5 篇（另 1 篇附注）。数字多为官方/论文自报，标注见各条。

## 官博

### Meta：Muse Spark Open（10/15，精确时刻待核）
Meta 发布开放权重多模态 MoE，816B 总参、42B 激活、1M 上下文，主打编程与 agent，自称"迄今最强美国开放权重模型"（官方自报）。本窗最大模型发布，开放权重格局要重新看。
[Muse Spark Open](https://research.meta.ai/blog/muse-spark-open)

### NVIDIA：Nemotron 3.5 Super VL + 端侧 Bolt（10/15 23:00 SGT）
120B 开放多模态 agent 模型，另有 24GB 与 4GB 两款端侧模型，权重、数据集、训练配方全开。和 Meta 同周发，开放模型竞争明显升温。
[Nemotron 3.5 Super VL](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/)

### Anthropic：独立评估方更新（10/16 01:20 SGT）
给 6 名 METR 人员接近员工级的内部访问，METR 可独立发布风险评估，Anthropic 无否决权；另与 SecureBio、Accenture 合作评估。第三方评估从"给 API"走向"进内部"，是治理上的实质一步。
[An update on independent evaluators](https://www.anthropic.com/news/an-update-on-independent-evaluators)

### Anthropic：用 Claude 设计更高效的量子电路（10/17 01:29 SGT）+ 论文 2610.22367
Claude 基本自主地设计出优于已发表最佳方案的量子电路，部分门数少 17 倍（官方自报）。配套论文（Harvard/Anthropic/QuEra，含 Lukin）8 个任务中 7 个刷新 Toffoli 数与 qubit 数（论文自报，降幅待查表）。AI 做科研从"辅助"到"出新结果"的一个硬例子。
[Designing more efficient quantum circuits with Claude](https://www.anthropic.com/research/designing-efficient-quantum-circuits) · [arXiv 2610.22367](https://arxiv.org/abs/2610.22367)

### Google Quantum AI：magic state cultivation（10/16 02:00 SGT）
在 Willow 上实验证明 magic state cultivation 可行，误差降约 40 倍，T 态保真度 99.99%，登 Science（官方自报）。容错量子计算关键瓶颈之一有了实验进展。
[Magic state cultivation](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/magic-state-cultivation-quantum-computing/)

### MSR：Magnetar 通用 zkVM（10/16 00:00 SGT）
可直接证明 Rust/Go/C 程序的零知识虚拟机，比现有最快系统平均快 10–39 倍，验证约 12ms（官方自报）。可验证计算离实用更近。
[Magnetar](https://www.microsoft.com/en-us/research/blog/proof-based-general-purpose-computing-with-magnetar/)

### Anthropic：Claude 还原 ECDSA 曲线来源（10/17 01:02 SGT）
Claude 查出 NIST P 曲线种子来自用时间戳初始化的普通伪随机数生成器。官方明确不是漏洞，反而降低了"后门"嫌疑。只写结论。
[Claude reveals ECDSA curve origins](https://www.anthropic.com/research/ecdsa-curve-origins)

### Anthropic：经济研究三篇（10/17 00:21–00:45 SGT）
Anthropic 内部初级技术岗招聘占比 27% 降到 9%；8 月 agent 工时是员工的 6 倍；"2030 前出现诺奖级 AI 发现"员工 91% 认同、公众仅 39%（官方自报）。AI 对就业的影响开始有一手公司数据。
[Employment at Anthropic](https://www.anthropic.com/research/employment-at-anthropic)

### Google Research：自主湿实验室（10/17 02:11 SGT，偏弱）
VERID 框架让 agent 驱动真实实验机器人做闭环分子设计，得到单位数纳摩尔级蛋白结合物（官方自报）。只写结论。
[Autonomous wet labs](https://research.google/blog/grounding-ai-agents-in-biological-reality-building-blocks-for-autonomous-wet-labs/)

备选未收：OpenAI GPT-Rosalind 学术访问计划、RTX Spark 开售、DeepMind 用 Antigravity 筛抗菌肽。OpenAI 本窗无新模型；Meta 本窗经核对仅 1 条。

## arXiv（Thu 10/15、Fri 10/16 两批；周末无批次）

1. **NVIDIA agentic midtraining 配方** [2610.22019](https://arxiv.org/abs/2610.22019)：公开为 agent 后训练打底的 midtraining 配方，同 SFT 下 SWE-bench Verified 60.7→64.5（论文自报）。和 Nemotron 3.5 发布可以连读。
2. **Athanor** [2610.21055](https://arxiv.org/abs/2610.21055)（ByteDance 等）：4 个 Claude Opus 5.5 agent 跑 104 小时，自主后训练 Qwen3-4B-Base，略超官方 Instruct 版（论文自报）。AI 自动做 AI 研发的又一个实证。
3. **Screwtape** [2610.20941](https://arxiv.org/abs/2610.20941)（Redwood Research）：红队改写真实 agent 轨迹，得到 35 个绕过监控器的攻击，6 个也绕过一家前沿开发者的监控器。只写结论，说明 agent 监控仍然脆弱。
4. **饱和基准后的能力评估** [2610.20667](https://arxiv.org/abs/2610.20667)（LASR Labs / UK AISI 等）：用做对的轨迹两两评判，预测误差比只看饱和分数低 5.3 倍（论文自报）。
5. 量子电路论文 [2610.22367](https://arxiv.org/abs/2610.22367) 已并入上方 Anthropic 量子电路条。

附注：TheoPhysEval [2610.16733](https://arxiv.org/abs/2610.16733)（含 DeepMind 作者）最佳 agent 在 50 道研究级理论物理题上 98%（自报），但 10/09 已提交，以交叉列表进入本窗，非首发。
近失：ReproBAIT（UK AISI/SecureBio）、Meta TreeFlex / CoPE、MSR AgentCIScope 等。

---

# 二、官方博客（全量）
窗口：2026-10-15 09:16 → 2026-10-18 09:18 SGT
时间均为 Asia/Singapore（UTC+8）。标注：已核 = 可在一手页面、模型卡或论文直接核到；官方自报 = 官方给出的数字，未独立核实；待核 = 信息不全或时间不精确。

---
## 短名单（建议入选）

### 1. Meta：Introducing Muse Spark Open, The Most Capable US Open-Weight Model to Date
- 时间：2026-10-15（官方页只给日期，精确时刻**待核**；Reuters 报道为美国时间 10-15 周四发布，NVIDIA 配套开发者稿 10-16 02:00 SGT → 按美国当天发布推断落在窗口内）
- URL：[Meta 研究博客](https://research.meta.ai/blog/muse-spark-open) （模型卡 [HF 模型卡](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B) ；NVIDIA 配套稿 [NVIDIA 开发者博客](https://developer.nvidia.com/blog/scale-agentic-coding-workflows-with-metas-muse-spark-open-on-nvidia-gb300-nvl72/) ）
- 一句话：Meta Superintelligence Labs 开放 Muse Spark 的权重：原生多模态 MoE，主打编程和 agent，可用两台 M5 Ultra Mac Studio 在本地运行。
- 关键数字：
  - 816B 总参数 / 42B 激活，256 个专家、每 token 选 8 个，1M 上下文，BF16 + NVFP4 两种权重（已核，HF 模型卡）
  - 自称"迄今最强的美国开放权重模型"（官方自报；官方页未给出可直接引用的具体分数，待核）
  - Helion kernel 提速 1.03–3.95×；AMD MI350 端到端 +3%（官方自报）
  - GB300 NVL72 上最高 50K tok/s/GPU、600 tok/s/用户（NVIDIA 自报）
  - 许可证为 Muse Model License，商用条款有限制；做了额外安全后训练，按 Meta Superintelligence Scaling Framework 评估后"达到发布门槛"，完整评估报告"即将发布"（官方自报）
- 进短名单：**是**。大厂发布的前沿级开放权重新模型，信号最强。以 research.meta.ai 和 HF 页面为准。

### 2. NVIDIA：Nemotron 3.5 Super VL + Bolt 系列开放模型
- 时间：2026-10-15 23:00 SGT（blogs.nvidia.com）；开发者技术稿 2026-10-16 02:01 SGT
- URL：[NVIDIA 博客](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/) ；[NVIDIA 开发者博客](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/)
- 一句话：NVIDIA 发布 120B 开放多模态 agent 模型 Super VL，以及两款端侧模型 Bolt 74B-A9B（24GB，原生 2-bit）和 Bolt E4B（4GB），并开放权重、数据集和训练配方。
- 关键数字：
  - Super VL 120B 参数（官方自报）；准确率与 NVIDIA 最大推理模型相当，参数约为其 1/5（官方自报）
  - Artificial Analysis 上同级吞吐最高快 5×（官方自报，待核）
  - Dynamo 部署下用户数最多 8×、延迟降低 85%（官方自报）
  - Bolt 74B-A9B：PinchBench 同级开放模型第 1、BrowseComp 第 2（官方自报，待核）
  - Super VL 和 Bolt 74B 现已上线；Bolt E4B 10-23 上线（以官方页为准）
- 进短名单：**是**。新的开放模型家族，覆盖从数据中心到端侧。

### 3. Anthropic：An update on independent evaluators
- 时间：2026-10-16 01:20 SGT
- URL：[Anthropic：an-update-on-independent-evaluators](https://www.anthropic.com/news/an-update-on-independent-evaluators)
- 一句话：Anthropic 给 METR 团队"类员工级"内部访问权限，METR 将发布独立风险评估，Anthropic 无否决权，只能按预设类别要求删改；另与 SecureBio、Accenture 合作评估，并在与 Hugging Face 等早期接洽。
- 关键数字：已接入 6 名 METR 员工（官方自报）；评估方访问权限分三级（官方自报）；文中提到已签署 White House Accord on Super Intelligence（官方自报）
- 进短名单：**是**。安全治理方面的实质进展，外部评估方被嵌入公司内部，并拥有独立发布权。

### 4. Anthropic：Designing more efficient quantum circuits with Claude
- 时间：2026-10-17 01:29 SGT
- URL：[Anthropic：designing-efficient-quantum-circuits](https://www.anthropic.com/research/designing-efficient-quantum-circuits)
- 一句话：给 Claude 8 个量子电路的自然语言规格和一个自动评分器，Claude 基本自主地设计出优于已发表最佳方案的电路，部分提升一个数量级以上（与哈佛 Yelin、Lukin/QuEra 合作，论文已上 arXiv）。
- 关键数字：8 个电路任务；椭圆曲线点加法中有一款设计 qubit 多 12%、门数少 17×；DQI 解码器门数减少 12×；椭圆曲线设计来自一次 53 小时运行（均为官方自报，论文待核）
- 进短名单：**是**。AI 自主做科研的重要成果，也与量子密码迁移时间表相关。

### 5. Google Quantum AI（blog.google）：Bringing the magic: Google breaks open a bottleneck in quantum computing
- 时间：2026-10-16 02:00 SGT
- URL：[Google 博客](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/magic-state-cultivation-quantum-computing/)
- 一句话：在 Willow 处理器上首次实验证明"magic state cultivation"可行，攻克通用容错量子计算的关键瓶颈，成果发表于 Science。
- 关键数字：误差约降低 40×；T 态逻辑保真度 99.99%（官方自报，Science 论文待核）；"magic state 生产最多可能占用 95% 算力"是引用的既有估计，不是本次结果
- 进短名单：**是**。重要研究，与第 4 条（Claude 量子电路）可以合并成"量子"主题。

### 6. Microsoft Research：Proof-based general-purpose computing with Magnetar
- 时间：2026-10-16 00:00 SGT（可能只精确到日期）
- URL：[Microsoft Research](https://www.microsoft.com/en-us/research/blog/proof-based-general-purpose-computing-with-magnetar/)
- 一句话：MSR 的通用零知识证明 zkVM Magnetar，可直接证明 Rust/Go/C 程序，只依赖标准哈希函数（具备抗量子长期安全性），速度比现有最快的同类系统高一个数量级。
- 关键数字：在 15 个基准上平均快 10–39×；笔记本上 7.2–8.7M 指令/秒（优化版 9.5–12.8M）；验证约 12ms；某基准比另两款系统快 300×以上（均为官方自报）
- 进短名单：**是**。重要系统/密码学研究，文中明确提到可用于给 AI agent 的行为合规出证明。

### 7. Anthropic（Frontier Red Team）：Claude reveals ECDSA curve origins
- 时间：2026-10-17 01:02 SGT
- URL：[Anthropic：ecdsa-curve-origins](https://www.anthropic.com/research/ecdsa-curve-origins)
- 一句话：内部研究模型在半小时内查明 NIST P-192/224/256/384/521 曲线种子的来源：由时间戳初始化的普通伪随机数生成器产生，而不是哈希。官方明确表示这不是攻破或漏洞，反而降低了"后门"的可能性，也无需任何处置。
- 关键数字：耗时不到 30 分钟，覆盖 5 条曲线（官方自报；结论可由社区复现，待核）
- 进短名单：**是**（只写结论）。困扰密码学界数十年的谜题被解开，也展示了模型能力。不写具体复现步骤。

### 8. Anthropic（Economics，3 篇合并）：How employment is changing at Anthropic / The AI expectations gap / Working at the frontier shapes expectations for the future
- 时间：2026-10-17 00:21 / 00:26 / 00:45 SGT
- URL：[Anthropic：employment-at-anthropic](https://www.anthropic.com/research/employment-at-anthropic) ；[Anthropic：ai-expectations-gap](https://www.anthropic.com/research/ai-expectations-gap) ；[Anthropic：expectations-for-the-future](https://www.anthropic.com/research/expectations-for-the-future)
- 一句话：Anthropic 披露内部就业变化：初级技术岗招聘占比明显下降，agent 工时已超过人类；同时问卷对比员工与约 11,000 名美国成年人对 AI 的预期，差距很大。
- 关键数字（均为官方自报）：
  - 技术部门初级员工占比 21%→14%；初级技术岗招聘占比 27%→9%；技术部门占比 61%→56%
  - 2026 年 3 月 agent 工时首次超过人类；8 月 agent 工时是员工的 6×；工程师人均提交量是半年前的 5×
  - 预期"2030 年前 AI 能做出诺奖级发现"：员工 91%，美国成年人 39%
  - 预期"2030 年 AI 能做自己 ≥80% 的工作"：员工过半，美国工人 5%
- 进短名单：**是**（作为一条）。前沿实验室首次给出内部就业和 agent 替代的数据，信号强。

### 9. Google Research：Grounding AI agents in biological reality: Building blocks for autonomous wet labs
- 时间：2026-10-17 02:11 SGT
- URL：[Google Research](https://research.google/blog/grounding-ai-agents-in-biological-reality-building-blocks-for-autonomous-wet-labs/)
- 一句话：Google Research 推出 VERID（湿实验室的语义数字孪生加安全校验层），让 AI agent 驱动真实实验机器人完成闭环分子设计，得到针对癌症靶点的单位数纳摩尔级蛋白结合物。
- 关键数字：适配体靶上命中率 33.5%（肌红蛋白）、42.1%（α-凝血酶）；表位切除让结构预测提速 8.6×（官方自报，论文待核）
- 进短名单：**是（偏弱，可作为备选）**。自主实验室方向的重要研究；属于生物方向，只写结论。

---
## 备选（信号中等，不建议主推）

- **OpenAI：Bringing GPT-Rosalind to academic research labs**。2026-10-16 03:00 SGT。[OpenAI](https://openai.com/index/introducing-the-rosalind-academic-plan)
  一句话：Rosalind Academic Plan 向美国高校实验室提供免费席位，GPT-Rosalind 须经可信访问审核后开通。关键数字：每个实验室最多 30 个 Business Standard 席位，0 美元，最长 12 个月，不含 API（官方自报，数字建议再核）。理由：是访问计划，不是新模型，所以不进短名单。
- **NVIDIA：RTX Spark Ignites Global Celebration as New Windows PCs Arrive**。2026-10-18 05:00 SGT。[NVIDIA 博客](https://blogs.nvidia.com/blog/local-ai-rtx-spark-windows-laptops-celebration/)
  一句话：RTX Spark 笔记本开售，ASUS/Dell/HP/Lenovo/Microsoft/MSI 均有机型。关键数字：起售价 2,399 美元，最高 128GB 统一内存，最高 1 PFLOP AI 算力（官方自报）。理由：硬件之前已发布，这次只是开售，正文多为活动报道。
- **Google DeepMind：Accelerating the search for antimicrobial peptides with Google Antigravity**。2026-10-16 00:08 SGT。[Google DeepMind](https://deepmind.google/blog/accelerating-antimicrobial-discovery/)
  一句话：用 Antigravity 加 ProtNLM 在 UniProt 未注释序列中筛出抗菌肽候选，目前正在湿实验验证。理由：本质是平台的技术演示/教程，暂无验证结果。

---
## 丢弃项
- OpenAI，How Itaú is building generative AI…（10-17 03:00 SGT）：客户稿
- OpenAI，Stack Overflow for Agents triples signups…（10-16 08:00）：客户稿
- OpenAI，Benefit Street Partners…Codex（10-16 08:00）：客户稿
- OpenAI，Teaching students to think and learn through questions（10-15 21:00）：教育/节日稿
- NVIDIA，Be There for the Beginning: RTX Spark launch event invite（10-16 01:00）：活动邀请
- NVIDIA，DLSS 4.5 Controls on GeForce NOW（10-15 21:00）：游戏常规更新
- NVIDIA，EC scientific computing pledge（10-15 18:00）：政策/合作稿
- NVIDIA，Nordics technology ecosystem（10-15 13:00）：区域生态稿
- NVIDIA dev，Code, Test, and Deploy on One Machine with RTX Spark（10-17 01:00）：教程
- NVIDIA dev，Muse Spark Open on GB300 NVL72（10-16 02:00）：已并入第 1 条 Meta
- blog.google，3 tips to study smarter with Gemini Notebook（10-17 00:00）：教程
- blog.google，Circle to Search 识别诈骗短信（10-16 01:30）：小功能更新
- blog.google，Crisis resilience white paper（10-16 00:00）：白皮书/公益稿
- blog.google，Android 地震预警覆盖 200+ 地区（10-16 00:00）：已有功能扩大覆盖
- blog.google，News AI pilot 合作出版物达 400 家（10-16 00:00）：合作进度
- blog.google，More ways to connect with the web from Search（10-16 00:00）：搜索小更新
- blog.google，Pixel repair（10-15 23:00）、Universal cart（10-15 21:00）、Holiday shopping（10-15 21:00）：消费产品/购物稿
- blog.google，SynthID 入选 TIME 2026 最佳发明（10-15 21:00）：荣誉稿

窗口外（边界核对后排除）：
- OpenAI Sullivan & Cromwell（10-15 08:00）
- Google Research 的 Research@ 2026、Earth AI geospatial agents（不复读）、Deep Review（均为 10-15 00:14）
- NVIDIA dev NeMo Gym chip design（10-15 00:10）
- Anthropic 10-14 发布的 2026 US midterms、Singapore office/MOU（10-14 16:30 SGT）
- Anthropic Self-replicating AI、Distillation defenses（10-12，不复读）
- Meta Muse Wonder（10-12）、Muse health data science（10-14）

不复读清单内的主题：本窗口未见 Anthropic Cyber 系列、unintended model actions、Argon、MDDI、EmbeddingGemma 2、GPT-6 for everyone、Vera Rubin、Run:ai 有新进展。

---

# 三、arXiv（全量）
窗口：2026-10-15 09:16 → 2026-10-18 09:18 SGT

范围：cs.AI、cs.CL、cs.LG 三个类别的最新列表，标题、摘要、提交日期和作者机构均对照 arXiv 原页与论文首页核对。

## 批次状态
| 批次（announce） | cs.AI | cs.CL | cs.LG | 状态 |
|---|---|---|---|---|
| Thu 2026-10-15 | 280 | 182 | 305 | 已出，已扫 |
| Fri 2026-10-16 | 286 | 177 | 306 | 已出，已扫 |
| Sat 10-17 / Sun 10-18 | — | — | — | 无批次（正常） |
三个类别去重后共 1129 条，其中 2610.* 有 1120 条（另有 9 条旧 id 交叉列表，跳过）。Wed 10-14 及更早的批次没有重扫。
初筛：按大厂与重点机构署名筛选，再人工看标题与摘要。
上期已写过的论文（如 2610.12822、2610.17637、2610.14423、2610.13015 等）及 2609.* 均已排除。

标注：已核 = 论文原文可直接核到的事实（作者、机构、日期、规模）；官方自报 = 论文摘要里的结果数字，未独立复现；待核 = 尚未核实。

---

## 短名单（6）

### 1. 2610.22019 — Priming Base Models for Agentic Post-Training: An Open Midtraining Recipe
- 作者/机构：Soumye Singhal, Joseph Jennings, Ka Shun Shum, Alexander Bukharin … Mostofa Patwary（14 人）/ **NVIDIA**（论文首页已核）
- announce：Fri 2026-10-16（cs.CL primary，交叉列表 cs.AI/cs.LG；提交 10-15）
- abs：[arXiv 2610.22019](https://arxiv.org/abs/2610.22019)
- 贡献：公开一套 midtraining 配方，介于预训练与 SFT 之间：256K 上下文，数千亿 token，以真实软件工程数据（仓库、PR、commit、构建日志）为主，掺少量 agent 轨迹，用来提升后续 agentic 后训练的效果。
- 关键数字（官方自报）：Nemotron 3.5 Lightning 做 500B token midtraining，在相同 SFT 下 SWE-bench Verified 60.7→64.5、Multilingual 55.8→62.8、Pro 32.0→35.5；Nemotron 3.5 Super 做 280B token，DeepSWE 11.7→15.7、SWE-bench Verified 72.9→74.3。另外报告 base-model 代理指标与后训练结果相关性不可靠。
- 入选理由：大厂署名；少见地公开了 midtraining 阶段的细节，同时给出消融与评测协议。

### 2. 2610.22367 — Discovering state-of-the-art quantum circuits with large language models
- 作者/机构：Andi Gu, Alek H. Kemeny, Susanne F. Yelin, Mikhail D. Lukin / Harvard Quantum Initiative & Harvard Physics；**Anthropic**（Kemeny）；Anthropic STEM Fellows Program（Gu）；QuEra Computing（Lukin）（论文首页已核）
- announce：Fri 2026-10-16（quant-ph primary，交叉列表 cs.AI；提交 10-15）
- abs：[arXiv 2610.22367](https://arxiv.org/abs/2610.22367)
- 贡献：一个进化式框架：LLM 提出量子电路设计，独立评估器负责验证和打分；覆盖数值计算、化学、优化、量子模拟、数论 8 类任务。
- 关键数字（官方自报）：8 个任务中有 7 个的 Toffoli 数和 qubit 数都显著低于 SOTA；第 8 个任务找到一种新的素域模逆可逆架构，使 divsteps 算法在可逆计算中变得可行。具体降幅比例待核（需看正文表格）。
- 入选理由：Anthropic 署名，作者含 Lukin；属于“LLM 搜索 + 验证器做科学发现”的硬结果，可验证性强。

### 3. 2610.21055 — Athanor: An Agent-Native System for Autonomous Post-Training Research
- 作者/机构：Yufa Zhou, Yichen Wang, Jiakun Fan, Ziqi Shu, Zhichao Liu, Anru R. Zhang, Neiwen Ling, Zijun Wei / **ByteDance**、Duke、UChicago、Virginia Tech（论文首页已核）
- announce：Fri 2026-10-16（cs.AI，交叉列表 cs.CL/cs.LG；提交 10-15）
- abs：[arXiv 2610.21055](https://arxiv.org/abs/2610.21055)
- 贡献：开放的 agent-native 系统，让前沿 agent 在真实 GPU 上自主完成 base 模型后训练研究（AutoPostTrain），用来衡量弱形式的“递归自我改进”。系统提供冻结评测、去污染数据，以及 agent 不可见的 held-out 套件。
- 关键数字（官方自报）：4 个 Claude Opus 5.5 agent，每个配 8 卡节点，跑 104 小时，不给研究建议；Qwen3-4B-Base 开发套件 15.9→67.3，held-out 9.2→48.2，官方 Qwen3-4B-Instruct-2507 为 66.5 / 47.9。作者称这是首次看到 agent 团队把 raw base 后训练到持平或超过官方 instruct 版。
- 入选理由：自动化 AI 研究 / RSI 话题热度高，有 held-out 对照，数字可传播；大厂（ByteDance）署名，但不在优先名单内。

### 4. 2610.20941 — Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming  〔安全｜只写结论级〕
- 作者/机构：Gosha Kozhevnikov, Tyler Tracy / **Redwood Research**（论文首页已核）
- announce：Fri 2026-10-16（cs.CR primary，交叉列表 cs.AI；提交 10-14）
- abs：[arXiv 2610.20941](https://arxiv.org/abs/2610.20941)
- 贡献：一套用 LLM 改写真实 agent 轨迹的红队流水线，并由 LLM 验证器过滤，用来找出只看动作的 agent 监控器的盲区。
- 关键数字（官方自报，结论级）：基于 94 条 Claude Code / Codex 轨迹跑了 252 次，得到 35 个通过验证且绕过自家监控的反例；其中 6 个经人工确认后，也绕过了一家前沿开发者提供的 held-out 监控器。
- 入选理由：控制 / 监控安全评测；说明外部红队即使拿不到开发者基础设施，也能找到生产级监控器的确认失效。本条不写具体方法细节。

### 5. 2610.20667 — Evaluating Model Capabilities After Benchmark Saturation  〔安全评测方法〕
- 作者/机构：Morio Hamada, Jehyeok Yeon, Matteo Migliarini, Justin Olive, Magda Dubois / LASR Labs、ELLIS Tübingen / MPI-IS / Tübingen AI Center、Sapienza、Generality Labs、**UK AISI**（论文首页已核）
- announce：Fri 2026-10-16（cs.AI，交叉列表 cs.LG；提交 10-14）
- abs：[arXiv 2610.20667](https://arxiv.org/abs/2610.20667)
- 贡献：基准饱和后，从“做对的轨迹”里继续提取能力信号。作者用历史基准和模型做回溯模拟，比较两两评判、单条打分、特征/嵌入预测等协议。
- 关键数字（官方自报）：两两评判效果最好，预测误差比只用饱和分数的基线低 5.3×；信号集中在推理和 tool-call 通道；泛化不总成立。
- 入选理由：直接服务于 safety case 和前沿政策评测，有 UK AISI 参与。

### 6. 2610.16733 — TheoPhysEval: Assessing AI agents at autonomous theoretical physics problem solving
- 作者/机构：A. Ramesh Chandra … Praneeth Netrapalli, Suvrat Raju（35 人）/ ICTS、TIFR、UT Austin、Kavli IPMU、Harvard、UPenn、IISc、KU Leuven 等，以及 **Google DeepMind**（Netrapalli，通讯作者之一）（论文首页已核）
- announce：Thu 2026-10-15 进入 cs.AI 列表（hep-th primary 的交叉列表）。⚠ 提交日期是 2026-10-09，hep-th 主类大概率更早已 announce；对 cs.AI 是新进，但不算“首发”。
- abs：[arXiv 2610.16733](https://arxiv.org/abs/2610.16733)
- 贡献：50 道未公开的研究级理论物理题，答案可验证；评测现成 agent 在不给提示的条件下自主解题。
- 关键数字（官方自报）：最佳 agent 为 GPT-6-Astra（Codex harness），准确率 98%，平均每题成本 < 3 美元；关掉搜索和背景论文后准确率变化很小，作者解读为可能存在大量文献记忆。
- 入选理由：高热话题（AI 做科研），数字醒目，有 DeepMind 署名。需注意首发时间早于窗口，可降为备选。

---

## 近失（Near-miss）
- 2610.19810 ReproBAIT（UK AI Security Institute + SecureBio；10-15 批）：评测 coding agent 能否在离线沙箱里复现生物 AI 工具（ProteinMPNN、RFdiffusion3、一个闭源分子设计工具）。结论级：部分工具复现能力相当强，最复杂的工具能力有限；有中等程度的证据指向记忆。没进短名单：生物双用途敏感，摘要里没有可直接引用的汇总数字；若要用，只写结论。
- 2610.20334 TreeFlex（Meta AI，Yuandong Tian；10-15 批）：agent 自己导航搜索树，配合 tree-aware GRPO。4B 模型在 deep-research 基准 48.8% vs 41.5%（官方自报）。没进：属于小规模 RL，增量性质。
- 2610.20563 Scaling Discovery Requires Forgetting（UC Berkeley / Stanford / Bespoke Labs，Zaharia、Dimakis；10-15 批）：周期性丢弃搜索状态，从当前最优解重启，比并行 agent 最多 +15%，比单 agent 最多 +39%（官方自报）。没进：非优先机构；想法简洁，可做备选。
- 2610.20456 The COUNT（UW / Ai2；10-15 批）：用主机内存存 n-gram 计数，构造免训练的 n-gram 嵌入。在 1B 预训练上的效果相当于多用 57% 算力（官方自报），推理时可换领域表、无需训练即可适配。没进：非优先机构，规模较小。
- 2610.19158 AgentCIScope（UChicago / Microsoft Research / UIUC；10-15 批）：agent 情境完整性隐私评测，12 个 agent、936 个任务，单次泄露率 32.5%–94.4%，重复 5 次再增 4–19pp（官方自报）。没进：同类隐私基准较多。
- 2610.20597 CoPE（UIUC / UCSD / Meta AI；10-15 批，v2）：多步动作预测作为辅助目标，在 5 个 agent 基准上优于 GRPO，样本效率最高 2.0×。没进：增量。
- 2610.22201 / 2610.20587（Google DeepMind 系，Gemp / Trivedi / Eisenstein；10-16 / 10-15 批）：agent 市场的序贯拍卖与一价拍卖 PoA 理论。没进：偏理论，传播面窄。
- 2610.22130 DropKV（NVIDIA / IBM 等；NeurIPS 2026）：KV 驱逐有常数近似保证，评分 kernel 加速 19.8×，端到端 prefill 最多 +9.9%。没进：工程增量。
- 2610.22155 Realtime-Bench（NVIDIA 等）：实时交互基准，最佳成功率 44%、Pass^3 36%。没进：基准常规。
- 2610.20399 Cortex（ZJU 系）：上下文固化进参数记忆，14B 模型连续 50 次编辑后恢复 88.9% 增益、保留 99.8%。没进：非优先机构。

## 丢弃（代表性）
- 上期已写过的论文及 2609.*：排除。
- 9 条旧 id 交叉列表（2603/2605/2606/2507/2512/2412/2609.*）：不是本窗口新文。
- 其余大厂署名命中、但属于常规增量或领域应用的：2610.21597（Apple iOS 定位流量分析，单作者，Apple 只是研究对象而非署名机构）、2610.19068（Apple 署名的工具发现架构研究）、2610.19302 DTDD（Google）、2610.20922（Google，Bengio 合著的组合结构理论）、2610.21404 多奖励 hacking（Amazon）、2610.22350 FDE-Gym（Microsoft 等，26 人；最佳 0.56 分、95 题只解 14 题，近失边缘）、2610.19129（DeepMind 系 offline RL），以及 Amazon / Microsoft / Google 一批 OPD / 检索 / 时序 / 机器人论文。
- 2610.16733 首发早于本窗口，严格按首发计应视为丢弃（见第 6 条 ⚠）。

## 待核
- 入选理由里的“高热”为主题判断，待核。
- 2610.22367 的具体 Toffoli / qubit 降幅要看正文表格。

---

# 四、X

窗口：2026-10-15 09:16 → 2026-10-18 09:18 SGT。来源：X 上的 AI 讨论、主要实验室官方账号原帖、X Today's News，以及针对 DeepSeek、Muse Spark Open、Beam、OpenCode、出口管制、Fable 5.5、Decart、REA 的定向检索，并用网页报道交叉核对。

## 主条目

### 1. DeepSeek 发布 V4.1-Flash-1017，同时把自家搜索引擎做成 Search / Fetch API 开卖
本窗口中文圈最热的一条，官方帖 3 万赞。这次虽然只是 Flash 的小版本更新，但自报分数全面提升、输出更短；更值得注意的是 DeepSeek 第一次把自建搜索引擎单独拿出来卖，等于给 agent 开发者提供了"模型 + 联网"的一站式方案，矛头指向 Claude Code / Codex 用户。
- **是什么**：10-17 上线网页、App 与 API（模型名仍是 `deepseek-flash`，旧名自动路由到新模型）；Hugging Face 已放出权重，MIT 许可，页面显示 763B 参数。官方表格：DeepSWE v1.1 77.0（旧版 74.2，Opus 5 为 74.0）、Terminal-Bench 4.0 42.3（旧版 31.2，Opus 5 为 51.8）、Automation-Bench 60.5；HLE 无工具 42.6，明显落后 Opus 5（56.3）。Search / Fetch API 每千次成功请求 $0.75（国内价 5 元），各 5 QPS；通过 DeepSeek Harness、Claude Code、Codex 走服务端工具的调用 11-01 00:00（北京时间）前免费。针对 DeepSeek Harness、腾讯 CodeBuddy、WorkBuddy 做了优化。
- **为何重要**：对比对象选的是 Opus 5 和 GPT-5.6 Sol（都是上一代），不是 Opus 5.5 / GPT-6.1 Sol，"超越 Opus"的说法要打折。社区实测基本认为能用、便宜，但细节和创意仍不如 Opus 5.5。Ollama、OpenRouter（$0.15/$0.6 每百万 token，转述）、OpenCode 当天就接入。搜索 API 主打过滤 SEO/GEO 垃圾，这是中文开发者真正缺的东西。
- **对谁·深读建议**：做 agent / 编码工具、用中转站或国内模型的开发者；读 HF 模型卡与 API 更新日志，搜索 API 文档值得细看计费细则。
- **证据**：官方自报 — [DeepSeek 官方帖](https://x.com/deepseek_ai/status/2111375640717033777)、[Hugging Face 模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)、[API 文档](https://api-docs.deepseek.com/)；已核（媒体）— [MarkTechPost](https://www.marktechpost.com/2026/10/17/deepseek-just-released-v4-1-flash-1017-scores-77-0-on-deepswe-opens-search-api/)；中文解读 [X 原帖](https://x.com/dotey/status/2111487902869832182)、[X 原帖](https://x.com/shao__meng/status/2111436190612349384)、[X 原帖：实测](https://x.com/op7418/status/2111427699520749951)、[X 原帖：谈搜索 API](https://x.com/tvytlx/status/2111463240488427560)；接入 [Ollama 官方帖](https://x.com/ollama/status/2111576482879553726)；待核 — 参数规模说法不一（HF 显示 763B，MarkTechPost 写 552B 主干 + 196B Engram），OpenRouter 价格仅见转述。
- **约时**：2026-10-17 16:35 SGT

### 2. 美国开放权重一周三连：Meta Muse Spark Open 领衔，Reflection Beam、Nvidia Nemotron 3.5 跟上
三天内三个美国大号开放权重模型，这是"美国开源追中国开源"叙事第一次有了实际分量。Meta 的最强，但许可有附加条件；真正 Apache 2.0 的是 Reflection 的 Beam。
- **是什么**：**Muse Spark Open**（10-15 美国时间）：816B 总参 / 42B 激活 MoE，1M 上下文，输入支持文本/图像/视频/音频，输出文本；和 Apple 合作，NVFP4 版本可在两台 512GB M5 Ultra Mac Studio 上用 MLX 跑；HF、SageMaker、Vertex、Foundry 可下载，Together、Fireworks、Groq、OpenRouter 等可调用。**Beam**（10-16）：Reflection 首个模型，501B / 23B 激活，1M 上下文，纯文本，Apache 2.0，附带 DFlash2 草稿模型和 Rust harness。**Nemotron 3.5 Super VL**：Artificial Analysis 称其智能指数 26，一度是美国开放权重第一（120B / 12B 激活）。
- **为何重要**：Muse Spark Open 用的是"Muse Model License"：界面要显示 "Built with Muse Spark Open"，年收入超 2,000 万美元的模型服务商需另签协议，比 Qwen 的 Apache 2.0 紧得多。Arena 称其 Max 版在 Code Arena WebDev 拿到美国开源第一（1511 分，转述）。Beam 自称推理能力与中国头部开源模型相当，但算力只用三到四分之一。对中国开源模型来说，这是第一次在"开放 + 规模"上面对正面竞争。
- **对谁·深读建议**：本地部署、私有化、模型选型的团队；读 Meta 博客 + HF 模型卡（许可条款），Beam 读 HF 博客（架构写得细）。
- **证据**：官方自报 — [Meta 官方帖](https://x.com/AIatMeta/status/2110779754274292212)、[Meta 研究博客](https://research.meta.ai/blog/muse-spark-open)、[HF 模型卡](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)、[Reflection 官方帖](https://x.com/reflection_ai/status/2111079965529968798)、[Reflection 博客](https://reflection.ai/blog/beam-is-available)、[HF Beam 博客](https://huggingface.co/blog/reflection-beam)；已核（第三方）— [Artificial Analysis：Nemotron 3.5 Super VL](https://x.com/ArtificialAnlys/status/2110760441240752399)、[VentureBeat（含 Muse 许可条款）](https://venturebeat.com/technology/reflections-beam-aims-to-undercut-chinese-open-models-with-fewer-tokens-not-cheaper-tokens)；许可解读 [X 原帖](https://x.com/Ldataengineer/status/2110793697457787101)；待核 — Code Arena 排名仅见转述 [X 原帖](https://x.com/ppmmzzcn/status/2111346579731017991)。
- **约时**：Muse Spark Open 2026-10-16 01:08 SGT；Beam 10-16 21:01 SGT；Nemotron 评测 10-15 23:51 SGT

### 3. 商务部、科技部拟将 23 项 AI 技术列入出口禁限目录，即日起实施出口前登记
中国第一次把大模型、智能体写进技术出口管制目录。目前还是征求意见稿，但"出口前登记"已经生效；开源和已发表论文的技术明确排除在外，对开源模型影响有限，影响最大的是闭源技术的海外转让、授权和股权变更。
- **是什么**：10-16 发布 2026 年第 48 号公告，拟在《中国禁止出口限制出口技术目录》中新增 40 项技术：AI 23 项（大模型、智能体、算力集群、信息处理），生物医药 5 项，光伏 12 项。征求意见至 11-15。登记范围包括向境外转让技术所有权、授权境外使用、技术所有权人或实际控制人变成境外主体。
- **为何重要**：多方转述称"禁止 14 项、限制 26 项"，禁止类包括 AI 驱动的恶意代码生成，限制类包括 AI 辅助漏洞挖掘、用国内核心数据训练的大模型（以附件为准，待核）。路透称提案保留了通过 API / SaaS 向海外提供服务的空间。对出海公司、海外并购或融资、"中国团队 + 境外主体"的架构，都需要重新评估。
- **对谁·深读建议**：出海 AI 公司、投资和法务、关注中美科技博弈的读者；必读商务部原文和附件 1。
- **证据**：已核（官方原文）— [商务部公告](https://www.mofcom.gov.cn/zfxxgk/gkml/art/2026/art_ccd0391072a94c809ae7e820abe2536b.html)；X 侧 [X 原帖：摘要](https://x.com/prolibertine/status/2111034701662285880)、[X 原帖：附件细节](https://x.com/NFT_Chen/status/2111077892721647866)、[X 原帖：解读](https://x.com/shao__meng/status/2111268686103494921)；待核 — "禁 14 / 限 26"、"两万亿参数门槛"等细节仅见转述，未逐条核对附件。
- **约时**：2026-10-16 16:00 SGT（北京时间同）

### 4. OpenCode Console 被入侵，1.4% 用户存的第三方 API key 泄露，官方定性为"大规模蒸馏攻击"
这是"蒸馏"从模型厂商的政策问题变成开发者真金白银损失的第一起公开事件：攻击者盗走 key，用受害者的额度去调用前沿模型、收集输出，有用户报告被扣几百美元。
- **是什么**：OpenCode 10-17 晚在 X 上披露，被入侵的是一个"正在下线的旧系统"，影响的是在 Console 工作区里存了 OpenAI / Anthropic / Google key 的部分用户；已发邮件通知（标题 "Action Required: Potential provider key breach"），没收到邮件就是没受影响。联合创始人称普通 OpenCode 客户端里的 key 不经过公司服务器。Google AI Studio 负责人称已封禁泄露的 Gemini key；据报道 Anthropic 也已吊销受影响的 Claude key。事件仍在处理中。
- **为何重要**：聚合类工具把多家 key 集中存放，风险也跟着集中；被盗 key 直接打到模型厂商，不会出现在 OpenCode 的用量报表里，只能去各家后台查。这和 Anthropic 上周公开的反蒸馏防御正好对上：前门收紧后，压力转到了中间商。
- **对谁·深读建议**：用过 OpenCode Console 或任何托管 key 的聚合工具的开发者，立刻轮换 key、查账单；The Latent 和 TechCity 的报道就够。
- **证据**：官方自报 — [OpenCode 官方帖](https://x.com/opencode/status/2111519637049319818)、[Google AI Studio 负责人 Evan Otero](https://x.com/EvanOtero/status/2111591525876474100)；已核（媒体）— [The Latent](https://thelatent.co/models/opencode-says-breach-tied-to-distillation-attack-exposed-users-ai-provider-keys)、[TechCity Authority](https://www.techcityauthority.com/2026/10/opencode-breach-provider-keys-exposed.html)、[Notebookcheck](https://www.notebookcheck.net/OpenCode-hacked-users-urged-to-revoke-their-API-keys.1426957.0.html)；中文 [X 原帖](https://x.com/dotey/status/2111553994867028409)；待核 — 攻击者身份、受影响人数、个别用户被扣 $400 的说法。
- **约时**：2026-10-18 02:08 SGT

### 5. Anthropic 公开 Claude Code 团队的代码审查做法：九成代码由 Claude 写，合并 PR 翻倍、回滚率降四成
继 Scion 之后又一份"AI 写代码之后人干什么"的一手材料，而且这次给出了质量指标，不只是吞吐量；同期 Code Review 产品转正、Opus 5.5 快速模式取消等候名单，形成一套完整的产品组合。
- **是什么**：官方称 Claude 写了 Claude Code 约 90% 的代码；6–9 月合并 PR 翻了一倍多，需要回滚的比例下降超过 40%。做法是多层 AI 审查（找 bug 的 agent + 验证真假的 agent + 安全扫描），只有计费、自动更新、CI 等高风险改动才必须由人看，人审查的是"证据"（测试输出、截图）而不是逐行代码。同期：Code Review 面向 Team / Enterprise 正式可用，可按仓库选 Quick / Standard / Deep 三档；Opus 5.5 快速模式 GA，最高提速 2.5 倍，价格 $8/$40（标准价的两倍），Azure Foundry 已上线；Claude Code 每轮对话 gzip 压缩传输，云端会话边打字边启动。
- **为何重要**：回滚率下降是这类帖子里少见的质量数据（官方自报）。中文圈转发很多（单条中文解读约 445 赞），说明工程负责人正在找可以照搬的流程。
- **对谁·深读建议**：工程负责人、DevEx 团队；精读 claude.dev 博客，配合上期的 Scion 一起读。
- **证据**：官方自报 — [Claude 开发者账号 代码审查](https://x.com/ClaudeDevs/status/2111168901723906176)、[claude.dev 博客](https://claude.dev/blog/solving-code-review-at-anthropic/)、[Claude 开发者账号 Code Review GA](https://x.com/ClaudeDevs/status/2110866210573386065)、[Claude 开发者账号 快速模式](https://x.com/ClaudeDevs/status/2110825294655562048)、[Claude 开发者账号 gzip/云会话](https://x.com/ClaudeDevs/status/2111209208012210409)；中文 [X 原帖](https://x.com/dotey/status/2111384189656252712)、[X 原帖](https://x.com/shao__meng/status/2111274173192638932)、[X 原帖](https://x.com/Gorden_Sun/status/2111472904148058121)。
- **约时**：博客 10-15（美国时间）；X 帖 2026-10-17 02:54 SGT；Code Review GA 10-16 06:51、快速模式 10-16 04:09 SGT

## 进展

### 进展：Anthropic Q3 营收之后，IPO 估值预期被下调到约 1.5 万亿美元
上期写了 168 亿美元营收；新的信息是增速放缓已经开始影响定价：路透称部分投资者讨论把 11 月 IPO 估值从约 2 万亿降到约 1.5 万亿美元，没有官方确认。同时 Replit CEO 在 TC Disrupt 表示 Agent 的首选合作方已换成 OpenAI（仍可选 Claude），这是 Anthropic 编码生态里第一个公开转向的大客户。
- **是什么**：Reuters 10-15 独家（Q2 约 116 亿→Q3 168 亿，环比 +45%）；X News 汇总另称 Anthropic 在寻求约 600 亿美元的芯片债务融资（待核）。Replit：Amjad Masad 澄清"仍然模型中立，OpenAI 是基于性能、成本、合作关系的首选伙伴"。
- **为何重要**：IPO 叙事从"增长无上限"变成"增速放缓 + 客户被分流"；Fable 5.5 何时发布（见"其他"）会直接影响定价。
- **对谁·深读建议**：投资、行业分析读者。
- **证据**：待核（媒体援引消息人士）— [Reuters via US News](https://money.usnews.com/investing/news/articles/2026-10-15/exclusive-investors-temper-anthropic-ipo-valuation-expectations-over-revenue-growth-slowdown-sources-say)、[X News](https://x.com/i/trending/2111395890850316325)；已核 — [Replit CEO 澄清](https://x.com/amasad/status/2111494912562888939)、[TechCrunch](https://techcrunch.com/2026/10/17/replit-is-no-longer-working-with-anthropic-ceo-says/)。
- **约时**：Reuters 10-15；Masad 澄清 2026-10-18 00:29 SGT

### 进展：Codex 额度战继续——Day 10–13 两次重置，加上缓存复用提升"有效用量"
上期的"简单计划让大家用量显著增加"有了具体内容：不是直接加额度，而是子 agent 之间复用上下文、延长缓存时间、改路由以提高缓存命中率。外加两次全局重置，以及缓解 "model at capacity" 报错。
- **是什么**：Day 10 重置（10-15）；Day 11 增加算力，大幅减少 "Selected model is at capacity"，出现时会自动继续；Day 12 Codex 与 Work 的有效用量提升（上下文复用 / 缓存 / 路由）；Day 13 再次重置（1.36 万赞）。
- **为何重要**：OpenAI 连续两周"每日上新 + 送额度"，和 Claude Code 的提速节奏对位；"有效用量"属于官方自报，没有给数字。
- **对谁·深读建议**：Codex 重度用户；扫原帖即可。
- **证据**：已核 — [Day 10](https://x.com/thsottiaux/status/2110595484180214059)、[Day 11](https://x.com/thsottiaux/status/2110750421367287996)、[Day 12](https://x.com/thsottiaux/status/2111244596131111253)、[Day 13](https://x.com/thsottiaux/status/2111492673890824348)。
- **约时**：2026-10-15 12:55 → 10-18 00:20 SGT

### 进展：REA 冲到约 30.6 万 star，Perplexity Computer 已集成
热度还在涨（上期约 23.9 万）。新的信息是 Perplexity 把它做成 Computer 里的 /reverse-engineer 技能，10-31 前免费；木马仿冒和"增益有限"的提醒仍然有效。
- **证据**：已核 — [GitHub](https://github.com/morluto/rea)、[gitstars](https://gitstars.io/repo/github/morluto/rea)；[X News](https://x.com/i/trending/2111095140282667215)；待核 — Perplexity 集成细节见 [reaguide](https://reaguide.com/perplexity-computer/)（第三方站点）。
- **约时**：持续至 2026-10-18

### 进展：Gemini 4 Argon 上线后的动作——Pro 用户可在 AI Studio 使用，4 个 agent 27 小时通关 Minecraft
上期主条目的后续都是演示和放量，没有新的模型或价格变化。值得一提的是 DeepMind 的 Minecraft 实验：4 个 Argon agent 只用代码和文本，写了 2,783 个程序，靠聊天分工，27 小时打败末影龙。
- **证据**：官方自报 — [Google DeepMind 官方帖 Minecraft](https://x.com/GoogleDeepMind/status/2111127991401247033)、[Gemini App 官方帖 Canvas](https://x.com/GeminiApp/status/2111147479248855484)；[X 原帖：Pro 用户额度](https://x.com/Gorden_Sun/status/2111449510266458301)；LangChain deepagents 已支持（[X 原帖：转推](https://x.com/hwchase17/status/2111470721398604012)）。
- **约时**：2026-10-17 00:11 SGT 起

### 进展：Amazon × Decart 仍无确认
窗口内没有新报道、没有官宣，报价仍停留在 55–70 亿美元区间。
- **证据**：待核 — [WSJ](https://www.wsj.com/business/deals/amazon-in-talks-to-buy-ai-startup-decart-for-around-7-billion-9433abad)、[GeekWire](https://www.geekwire.com/2026/why-amazon-might-pay-billions-for-decart-a-3-year-old-ai-startup-that-hasnt-disclosed-its-revenue/)（均为窗口前报道）。

## 其他
- **OpenAI 升级 ChatGPT 里的 GPT-6 Pro / GPT-6 Astra Pro**：响应更快，插件和工具调用更稳，新增多 agent 并行分工，可以逐个查看进度（Pro 用户）。[OpenAI 官方帖](https://x.com/OpenAI/status/2111192259073094035) · [Help Center](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) · 2026-10-17 04:27 SGT
- **Anthropic 给 METR 团队"类员工"访问权限**做第三方安全评估（6 人进驻，可发布报告，但 Anthropic 可要求删去客户数据、模型架构等内容；SecureBio 权限较低）。[Anthropic 官方帖](https://x.com/AnthropicAI/status/2110784662071398807) · [TechCrunch](https://techcrunch.com/2026/10/15/anthropic-is-letting-metr-researchers-look-under-the-hood-with-employee-level-access/) · 2026-10-16 01:27 SGT
- **Claude Mythos 5 设计的量子电路超过已发表的最优结果**，部分任务门数减少一个数量级（如可逆椭圆曲线方法门数约为原来的 1/17，官方自报）。[Anthropic 官方帖](https://x.com/AnthropicAI/status/2111152183240511640) · 2026-10-17 01:47 SGT
- **OpenAI、Anthropic 各出 500 万美元资助 Simons 基金会的数学 + AI 计划**；陶哲轩同期称数学"浪漫时代"结束。[OpenAI 官方帖](https://x.com/OpenAI/status/2110741355739963884) · [Anthropic 官方帖](https://x.com/AnthropicAI/status/2110846112152105136) · [X News](https://x.com/i/trending/2110885636634824900) · 10-15 22:35 / 10-16 05:31 SGT
- **待核：Claude Fable 5.5 泄露持续**——Azure 目录出现条目、Cursor 3.25.6 为 fable-5.5 模型名加了特判、有人称 Opus 5.5 部分请求已路由到新模型；有爆料称下周发布。Anthropic 未表态。[X 原帖](https://x.com/aitrackerbot/status/2111333514398290262) · [X News](https://x.com/i/trending/2110028039782551624)
- **GPT-Live-1.1**：ChatGPT / Codex / dots 语音新增法、德、印地、墨西哥西语、韩、日语音色，API 稍后上线。[OpenAI 官方帖](https://x.com/OpenAI/status/2110797830361436604) · 2026-10-16 02:19 SGT
- **GPT-Rosalind 推出学术计划**，为符合条件的美国大学实验室提供赞助访问。[OpenAI 官方帖](https://x.com/OpenAI/status/2110841898076418336) · 2026-10-16 05:15 SGT
- **Mistral × CERN 合作"大物理模型"**（用数十亿次模拟碰撞训练）；另称 Mistral Large 4 在 STEMBench 工程和天文类得分靠前（自报）。[Mistral 官方帖：CERN](https://x.com/MistralAI/status/2110684732103041474) · [Mistral 官方帖：STEMBench](https://x.com/MistralAI/status/2111056939841163336) · 10-15 18:50 / 10-16 19:29 SGT
- **Hark Pro 免费披萨活动跑通端到端 agent 下单**：Brett Adcock 称跑了 20.35 万次浏览器会话、送出数千份披萨，期间后端两次宕机，约 30 分钟误扣费（承诺退还）；登上美区 App Store 生活类第 1（自报）。[Brett Adcock 原帖](https://x.com/adcock_brett/status/2111355199520694642) · 2026-10-17 15:14 SGT
- **待核：Jack Clark 把"AI 自我改进研究"的时间点从 2028 提前到 2027**（中文转述，未找到原文）。[X 原帖](https://x.com/KKaWSB/status/2111398310611198092)

## B Today's News
- **DeepSeek 发布 V4.1-Flash-1017，编码能力大幅提升** — 与主条目一致（News 摘要里的"763B"与 HF 一致）。[X News](https://x.com/i/trending/2111316973992788359)
- **Meta 发布 Muse Spark Open，为 Mac Studio 优化**。[X News](https://x.com/i/trending/2110781576766271604)
- **Claude 承担 Anthropic 九成代码与大部分 PR 审查**。[X News](https://x.com/i/trending/2111580584107462778)
- **Opus 5.5 快速模式向所有开发者开放**。[X News](https://x.com/i/trending/2110914330774688202)
- **Anthropic 估值受审视：营收放缓 + Replit 转向 OpenAI**。[X News](https://x.com/i/trending/2111395890850316325)
- **Fable 5.5 现身 Azure 目录**（传闻）。[X News](https://x.com/i/trending/2110028039782551624)
- **Claude Mythos 5 设计更高效的量子电路**。[X News](https://x.com/i/trending/2111157202203426827)
- **OpenCode 免费提供 DeepSeek V4.1 Flash 与 GLM 5.3 Flash**（200k 上下文）。[X News](https://x.com/i/trending/2110599474716213421)
- **REA 突破 30 万 star，Perplexity Computer 集成**。[X News](https://x.com/i/trending/2111095140282667215)
- **陶哲轩：数学进入"工业时代"；OpenAI / Anthropic 资助数学界**（News 称合计 1,500 万美元，含 Simons 自有资金，待核）。[X News](https://x.com/i/trending/2110885636634824900)
- **Altman 承认 AI 对经济的冲击比预期慢**（播客）。[X News](https://x.com/i/trending/2111074178766090411)
- **多家企业在出错和成本压力下收缩 AI 部署**（Meta 收缩 agent 计划、微软警告"AI slop 死循环"等，综合报道）。[X News](https://x.com/i/trending/2110850870489252305)
- **研究者与腾讯云上的"游荡 agent"对话**：9-28 至 10-8 期间 2,600 余次访问高德，腾讯方面称是第三方模型评测。[X News](https://x.com/i/trending/2110391953447879144)
- **Google Quantum AI 在 Willow 上实现魔术态培育**（Science，逻辑保真度 99.99%）；**NVIDIA GEAR 开源 ASPIRE 机器人框架**；**OpenUI 1.0 发布**。[量子](https://x.com/i/trending/2110806655235760294) · [ASPIRE](https://x.com/i/trending/2111166917532684350) · [OpenUI](https://x.com/i/trending/2110753248026284494)
- 其余为 vibe coding、AI 艺术争议、"LLM 是否理解"等泛话题，不列。

## C 要点摘要
- DeepSeek-V4.1-Flash-1017：10-17 上线，MIT 权重（HF 显示 763B），DeepSWE 77.0 / TB4.0 42.3（自报）；Search/Fetch API 每千次 $0.75，服务端工具调用 11-01 前免费。
- Muse Spark Open：816B / 42B 激活，1M 上下文，Muse Model License（需署名，营收超 2,000 万美元的服务商另签协议）；两台 M5 Ultra Mac Studio 可本地跑。
- Reflection Beam：501B / 23B 激活，Apache 2.0，10-16 放出权重。
- 中国第 48 号公告：40 项技术（AI 23 项），征求意见至 11-15，出口前登记即日生效，开源 / 已公开论文的技术排除在外。
- OpenCode：1.4% 的 Console 用户存储的 provider key 可能泄露；Google 已封禁泄露的 key。
- Claude Code：约 90% 代码由 Claude 写；6–9 月合并 PR 翻倍以上，回滚比例降 40% 以上（自报）；Code Review GA；Opus 5.5 快速模式 $8/$40 GA。
- Anthropic IPO 估值讨论下调到约 1.5 万亿美元（Reuters 消息源，未官宣）；Replit 首选伙伴改为 OpenAI。
- Codex：Day 10 / Day 13 两次重置，Day 12 通过缓存复用提升有效用量。
- REA 约 30.6 万 star。Decart 仍未确认。

## E 建议扩写
1. 开放权重的分水岭一周：DeepSeek 1017（MIT）、Muse Spark Open（附条件许可）、Beam（Apache）、Nemotron 3.5——按参数、许可、硬件门槛、自报分数做一张表，回答"中国开源的护城河还剩什么"。
2. 第 48 号公告逐条读：哪些 AI 技术会被禁、被限，开源豁免的边界在哪，对出海、融资、境外架构有什么实际影响。
3. 蒸馏战争蔓延到开发者钱包：从 Anthropic 反蒸馏防御到 OpenCode 泄露 key，聚合工具和中转站的风险清单与自查步骤。
4. AI 写九成代码之后的代码审查：Claude Code 团队的多层"奶酪"模型 + Scion，能直接照搬什么。
5. （可选）DeepSeek 卖搜索：模型公司为什么被逼着自己做搜索引擎，对 Kimi / 智谱 / 国内搜索 API 市场意味着什么。

---

# 五、GitHub

1. **llama.cpp v0.7.0：MoE 专家 GPU 缓存 + 新投机解码**
继 v0.6.0 之后，这是一次分量很重的正式版。最实用的是新增 `--moe-cache-mib`：MoE 专家放在内存里时，用 LRU 缓存把常用专家搬到 GPU 上跑，官方称解码最高快约 2.2 倍，而且可以跨多卡共享。显存不够、只能把专家卸载到内存跑大 MoE 的人，最该先试这个参数。投机解码方面新增了 LiliCorr，以及 GLM5-Next 的 MTP。新模型支持一大批，包括 K2 Horizon、Prism Bonsai 2 27B 三值模型、EmbeddingGemma-2、MiniCPM-V 4.7、Nemotron Super 3.5 VL 和几款决策模型。注意 server 的默认端口改成了 9931，脚本里写死 8080 的要改。
证据：[v0.7.0 Release](https://github.com/ggml-org/llama.cpp/releases/tag/v0.7.0) · [MoE 缓存 PR #29887](https://github.com/ggml-org/llama.cpp/pull/29887)

2. **Transformers v5.20.0：Meta Muse Spark Open 等新模型入库**
这一版的重点是新模型。最大的是 Meta 的 Muse Spark Open：多模态 MoE，总参数 816B、每 token 激活 42B，上下文最长 1,048,576 token，主打多文件编辑、调试和工具调用这类 agentic 编码任务，提供 BF16 和 NVFP4 两种权重。同时原生支持 InclusionAI 的 Ling 3.0 Flash（混合 KDA 与 MLA 注意力，不再需要 `trust_remote_code`），以及 Aleph Alpha 主攻德语和英语的推理模型 Kolibri 1。想研究开源 agentic 编码大模型、或者关注新型混合注意力架构的人可以从文档入手。v5.20.1 是随后的补丁版。
证据：[v5.20.0 Release](https://github.com/huggingface/transformers/releases/tag/v5.20.0) · [Muse Spark 文档](https://huggingface.co/docs/transformers/main/en/model_doc/muse_spark) · [v5.20.1](https://github.com/huggingface/transformers/releases/tag/v5.20.1)

3. **Axolotl v0.21.0：单节点 QLoRA 微调 501B MoE，原生扩散语言模型训练**
继 v0.20.0 之后的这一版，主打在单台 8×H200 上用 QLoRA 微调 Reflection 的 Beam（总参数 501B、激活 23B 的 MoE），并附带 FSDP2 配置和 B200 上的专家并行 LoRA 配方。另一个新方向是原生支持扩散语言模型微调，Nemotron-Labs-Diffusion、Dream、DiffusionGemma 都在列，只要在配置里加 `diffusion_lm:` 块、照常用对话数据集就行。DPO、KTO、GRPO 现在也能跑图像数据集。想低成本微调超大 MoE、或者想入门扩散 LM 的人值得看。注意现在要求 `vllm>=0.30.0`。
证据：[v0.21.0 Release](https://github.com/axolotl-ai-cloud/axolotl/releases/tag/v0.21.0) · [Beam 指南](https://docs.axolotl.ai/docs/models/beam.html) · [Diffusion LM 文档](https://docs.axolotl.ai/docs/diffusion_lm.html)

4. **OpenAI Codex CLI 0.163.0：回复中途插话纠偏，只读工具并行**
上期提到 0.163 还在 alpha，这次正式版发布。体验上最大的变化是：Codex 还在回复时，你就可以发消息直接纠偏，不用等它说完；只读工具（技能、记忆、历史检索）可以并行执行；新的 `/config` 页面能搜索并即时修改设置；`/daemon` 可以重启后台服务。安全方面，网络代理会在 DNS 查询前先检查权限，并拒绝重复的 `Host` 头。内置文档里新增了迁移到 GPT-6 系列的指引。日常用 Codex 的人建议升级。
证据：[rust-v0.163.0](https://github.com/openai/codex/releases/tag/rust-v0.163.0)

5. **Tencent-Hunyuan/Hy-Memory：腾讯混元开源的 LLM Agent 记忆引擎**
腾讯混元 10/15 开源的这个仓库，是一套给 agent 用的长期记忆引擎和 Python SDK（PyPI 包 `hy-memory`，已到 2.0.3 版）。它按场景分了三条管线：Chat 用分层长期记忆，Working 用“事实 + 可复用经验”两层记忆，Coding 用版本演化的差异链。基于它还做了本地优先的 MemHub，可以把 Claude Code、Cursor、Codex 等工具的对话和编码记录统一管理、跨应用召回。README 还提到同步开源了 Hy-Memory-30B-A3B 模型和技术报告。在给 agent 做记忆层、或者想把多个编码助手的上下文打通的开发者，可以先看 MemHub。
证据：[Tencent-Hunyuan/Hy-Memory](https://github.com/Tencent-Hunyuan/Hy-Memory) · [MemHub](https://github.com/Tencent-Hunyuan/Hy-Memory/blob/main/memhub/README.md) · [Hy-Memory-30B-A3B](https://huggingface.co/tencent/Hy-Memory-30B-A3B)

6. **mistralai/Timestral：Mistral 的时间序列基础模型**
Mistral 10/15 开源了 Timestral 系列时间序列基础模型，有 5M、28M、123M、209M 四个尺寸。它支持多变量联合预测和协变量（历史、已知未来、类别），每步输出 21 个分位数，上下文最长 32,768 步，CPU 上就能推理。官方称 209M 版在发布时于 GIFT-Eval、TIME、fev-bench 三个公开基准的预训练和零样本榜单上排第一。代码是 Apache 2.0，权重另用修改版 MIT 许可。做销量、负载、指标预测的人可以拿它和 Chronos、TimesFM 这类模型对比一下。
证据：[mistralai/timestral](https://github.com/mistralai/timestral) · [官方博客](https://mistral.ai/news/timestral) · [HF 集合](https://huggingface.co/collections/mistralai/timestral)

7. **chenglou/handwired：把普通 JS 代码“编译”成神经网络**
这是 10/15 新建的实验项目，几天约 1700 星。思路很巧：把程序里的 if-else、循环和状态，全部改写成矩阵乘法加 ReLU 类运算，得到一个不用训练、结果精确、又完全可微的“神经网络”，可以在 JS 或 WebGPU 上跑。作者设想的玩法包括解冻这些权重接着训练，或者把固定程序接到普通网络上端到端训练。它不是生产工具，但很适合用来理解“程序与神经网络的等价性”。对可解释性和神经网络编译感兴趣的人值得读 README 里的例子。
证据：[chenglou/handwired](https://github.com/chenglou/handwired)

窗口内无：vllm-project/vllm、sgl-project/sglang、pytorch/pytorch、huggingface/datasets、modelcontextprotocol/python-sdk、modelcontextprotocol/typescript-sdk（另有例行更新未收录：ollama v0.40.6、ComfyUI v0.41.0（新增 Flux3-image 支持）、Anthropic SDK Python v1.15.0 / TS sdk-v0.135.0、openai-python v3.32.0–v3.35.1、openai-node v7.35.0–v7.38.0、unsloth v0.1.908-beta、langchain-core / langgraph 补丁版）。

---

# 六、Hugging Face 与模型

- 窗口：2026-10-15 09:16 → 2026-10-18 09:18 SGT。
- 扫描范围：HF Trending 模型和数据集（前 100 名）；每个 org 按最近更新取前 30 个仓库：openai, google, meta-llama, microsoft, nvidia, Qwen, deepseek-ai, black-forest-labs, Cloudflare, XiaomiMiMo, tencent, ByteDance-Seed, CohereLabs, mistralai, ibm-granite, apple, amazon, stabilityai, Aleph-Alpha, autotrust, allenai, Lightricks, moonshotai, zai-org, MiniMaxAI, HuggingFaceTB, LiquidAI，另外补扫了 facebook、meta-models、openbmb、reflection。所有数字取自 10/18 约 09:20–09:25 SGT 的快照，所有仓库 id 均已核对存在。
- 本期判断：这一期比上期热闹，有 5 个真正的新发布。DeepSeek 的 V4.1-Flash-1017 换了新权重，上线就排 Trending 第 1。Reflection 放出首个开源权重模型 Beam 1.0，501B 总参。BFL 发布 FLUX 3 Image Klein，5.6B 参数，开源权重。NVIDIA 正式发布 Nemotron 3.5 Super VL 和 Bolt，又在 10/16 发了循环结构的小模型 Dory1.0-4B。其他大厂本窗没有新权重：openai、google、meta-llama、Qwen、moonshotai、MiniMaxAI、HuggingFaceTB、ByteDance-Seed、apple 在窗内都没有 lastModified；zai-org、openbmb、Aleph-Alpha 只做了维护性更新。

## 1. deepseek-ai/DeepSeek-V4.1-Flash-1017：本窗新发，新权重，Trending 第 1
DeepSeek 在 V4.1-Flash 上做了一次小版本更新，权重是完整的一套新 checkpoint（48 个 safetensors 分片，约 763B 参数，跟原版同一个尺寸），MIT 许可。官方说法是分数更高、任务完成更快、输出更短，并称这是一次“帕累托改进”。仓库里没有 Jinja chat template，改为提供 Python 编码参考实现（encoding/），另外开源了 Rust 写的 deepseek-recipe，用来处理 Messages、Chat Completions、Responses 三种 API 的格式转换。同一天 DeepSeek 还开放了 Search 和 Fetch API，每个端点每 1000 次调用收费 0.75 美元。
- 为何重要：这是本窗唯一一家头部开源厂的新权重。它主打便宜的 agent 编码：官方成本图显示 DeepSWE v1.1 拿到 77.0，每个任务成本不到 0.2 美元，上一版是约 0.5 美元。
- 对谁有用：自己部署大 MoE 做代码 agent 的团队、DeepSeek API 用户（会被自动切到新版）、做开源模型对比评测的人。
- 已核：createdAt 2026-10-17 10:40 SGT（10-17 02:40:38Z）；lastModified 2026-10-17 13:46 SGT（05:46:55Z）。likes 951，downloads 显示 0，是因为下载统计还没刷新，不代表没人下载。license MIT；pipeline image-text-to-text；没有 gated。原版 V4.1-Flash 在 10/16 17:27 SGT 有一次提交，看起来只是改卡（加了指向新版的说明），没有出现新权重。
- 待核：卡面的对比数字都是厂商自测，包括 Terminal-Bench 4.0 从 31.2 到 42.3、ProgramBench 从 20.3 到 29.1、HLE（无工具）从 36.8 到 42.6，还有和 Opus 5、GPT-5.6 Sol 的比较。The Decoder 也写明独立评测还没出来。截至快照时间，LMArena 和 Artificial Analysis 首页都还没收录 1017 版。
- 链接：[HF 仓库](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) · [DeepSeek 官方公告](https://api-docs.deepseek.com/news/news261017/) · [The Decoder 报道](https://the-decoder.com/deepseek-v4-1-flash-1017-beats-larger-rivals-in-agentic-tasks-while-once-again-massively-cutting-per-task-costs/) · [deepseek-recipe](https://github.com/deepseek-ai/deepseek-recipe)

## 2. reflection/Beam-1.0-501B-A23B：本窗正式放出权重，Reflection 的第一个开源模型
美国实验室 Reflection 的首个开源权重模型，Apache 2.0 许可。总参 501B，每个 token 激活约 23B，256 个专家；只支持文本，上下文 1M。同时提供 BF16、FP8、NVFP4 三种精度，外加一个 DFlash2 投机解码草稿模型。主打写代码、跑 agent，以及用更少的推理 token 完成任务。Reflection 在 10/5 先发了介绍文章，10/16 的“Beam is now available”才说“今天把权重放上 Hugging Face”。HF 官方博客也是 10/16 发的。
- 为何重要：这是目前少见的、宽松许可证下的美国开源大模型。Artificial Analysis 在 10/16 给出 Intelligence Index 30 分，说它在美国开源模型里排第二，仅次于 Meta 的 Muse Spark Open（39），在所有开源模型里排第十。AA 的结论是 token 效率高，但幻觉率也高（47%），Terminal-Bench 4.0 只有 3.0%。
- 对谁有用：想在自己的硬件或云上部署大模型、并且要自己再训练的团队（HF 博客给了 SFT 和 RL 的配方），还有关注美国开源模型进展的人。
- 已核：主仓 createdAt 2026-10-08 03:52 SGT（10-07 19:52:01Z），早于正式发布，应该是提前建好的；lastModified 2026-10-16 21:22 SGT（13:22:56Z）。likes 131 / downloads 1,148；license apache-2.0；pipeline text-generation；safetensors 约 501.3B。FP8 版 likes 25 / dl 760，NVFP4 版 likes 30 / dl 1,427。社区的 unsloth/Beam-1.0-501B-A23B-GGUF 是 10/16 17:11 SGT 建的，likes 10 / dl 777。Trending 排第 42。
- 待核：卡面数字是厂商自测，比如 SWE-bench Verified 81.6%、Terminal Bench v2.1 80.1%、AIME 2026 97.7%。Terminal Bench v2.1 这个数和 AA 测的 Terminal-Bench 4.0 只有 3.0% 差得很远，两者版本不同，不能直接比。技术报告卡面写“coming”，还没出。仓库 10/7 到 10/16 之间是不是公开的，查不到。
- 链接：[HF 仓库](https://huggingface.co/reflection/Beam-1.0-501B-A23B) · [Reflection：Beam is now available](https://reflection.ai/blog/beam-is-available) · [HF 博客](https://huggingface.co/blog/reflection-beam) · [Artificial Analysis 评测](https://artificialanalysis.ai/articles/reflection-beam)

## 3. black-forest-labs/flux-3-image-klein：本窗正式发布，仓库是上一窗口建的
BFL 发布了 FLUX 3 Image Klein，5.6B 参数的开源权重图像模型，文生图、图像编辑、最多 10 张参考图的多参考生成都能做。它支持原生 4K，可以用边界框控制元素放在哪里。这次一起放出的有 Base（用来微调）、步数蒸馏版（低延迟）、Comfy 打包版（含 FP8/INT8/NVFP4，和 NVIDIA 合作做的），还有一个 9B 的提示词扩写模型 klein-pup，是基于 Qwen3.5-9B 微调的，Apache 2.0。官方说 Klein 前面必须接一个扩写器，直接喂短提示效果会很普通。
- 时间说明：几个主仓 10/13 到 10/14 就建了，但官方博客的 datePublished 是 2026-10-15T15:00Z（10/15 23:00 SGT），在本窗内，所以算本窗发布。上期素材包没有写它，只写了 flux-3-action。
- 为何重要：在小尺寸开源生图模型里，它的能力覆盖面最全。Trending 上 Comfy 版排第 6，主仓排第 10。
- 对谁有用：ComfyUI 和本地生图玩家、要做图像编辑功能的产品团队、做微调的人。
- 已核：主仓 createdAt 2026-10-13 18:58 SGT（10:58:40Z）；lastModified 2026-10-16 12:58 SGT（04:58:03Z）；likes 455 / dl 46,123。Base 版 likes 133 / dl 29,448。Comfy 版 lastModified 2026-10-17 15:10 SGT（07:10:12Z），likes 651 / dl 224,108。pup 版 createdAt 10-15 04:40 SGT（10-14 20:40:29Z），likes 47 / dl 2,498。主仓 license 是 other（flux-kommunity-license），pipeline image-to-image，gated: auto，也就是点同意就能下载，不算没发布。
- 待核：博客说在内部评测里文生图、多参考和编辑三项都排第一，还超过了 Ideogram V4.5 和 FLUX.2 [pro]，这是厂商自评。截至快照时间，LMArena 生图榜（页面标注 10/7 更新）还没收录。FLUX Kommunity License 具体的商用条款要再核。主仓 README 需同意条款后才能查看，本次未读原文。
- 链接：[HF 主仓](https://huggingface.co/black-forest-labs/flux-3-image-klein) · [Base](https://huggingface.co/black-forest-labs/flux-3-image-klein-base) · [Comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy) · [Prompt Upsampler](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup) · [BFL 官方博客](https://bfl.ai/blog/flux-3-image-klein)

## 4. NVIDIA Nemotron 3.5 Super VL 120B-A12B 和 Bolt 74B-A9B 24GB：卡面写明 10/15 正式发布
NVIDIA 在 Nemotron 3.5 里加了两个多模态模型，两张卡的 Release Date 都写着 10/15/2026。Super VL 是 120B 总参、12B 激活的视觉语言模型，结构是 Mamba-2、MoE 和 attention 混合，视觉编码器用 C-RADIO，上下文 1M，自带 MTP 投机解码。Bolt 是 74B 总参、9B 激活的视觉语言模型，原生 2-bit 量化感知训练，整个模型打包后 24GB，目标是一张 24GB 显卡就能跑本地 agent。两个模型都用 OpenMDW-1.1 许可，允许商用。
- 时间说明：仓库在 10/07 到 10/12 就建了，但卡面和 Artificial Analysis 的文章（10/15）都把 10/15 当作发布日。上期素材包把 nvidia 归为维护性更新，漏掉了这两个。本窗内两个系列都还在持续提交（最近一次 10/17 07:39 SGT）。
- 为何重要：Bolt 走的是“24GB 显存跑 74B MoE”的路线，做端侧的人会关心。Super VL 在 AA Intelligence Index 拿到 26.5，已经上了 LMArena 文本榜，第 138 名，1416±12，标着 Preliminary。
- 对谁有用：只有单卡 24GB 的本地 agent 用户（看 Bolt）、做文档和视频理解的企业（看 Super VL）。
- 已核：Super VL BF16 版 createdAt 2026-10-12 23:32 SGT（15:32:06Z），lastModified 2026-10-17 07:39 SGT（10-16 23:39:54Z），likes 69 / dl 7,865；NVFP4 版 likes 132 / dl 5,715，Trending 排第 43。Bolt 24GB 版 createdAt 2026-10-08 01:50 SGT（10-07 17:50:42Z），lastModified 2026-10-16 02:09 SGT（10-15 18:09:19Z），likes 117 / dl 4,640；GGUF 版 likes 91 / dl 51,629。pipeline image-text-to-text。
- 待核：Bolt 卡上的数字，比如 GPQA-Diamond 89.52、SWE-bench Verified 71.10。仓库在 10/15 以前是否已经公开，查不到；Bolt GGUF 的下载量偏高，说明它可能更早就能下载了。
- 链接：[Super VL BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16) · [Super VL NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4) · [Bolt 24GB](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB) · [Artificial Analysis 文章](https://artificialanalysis.ai/articles/nemotron-3-5-super-and-bolt)

## 5. nvidia/NVIDIA-Nemotron-Labs-Dory1.0-4B-BF16：本窗新发，循环结构的 4B 模型
Nemotron Labs 新出的实验性小模型，采用循环（latent-recurrent）结构。层分三段，输入 8 层、可重复执行的循环块 20 层、输出 8 层，同一份权重可以选择循环 1、2 或 4 次。循环越多，每个 token 算得越多、结果越准，但生成的 token 反而更少。它还支持只缓存最后一轮循环的 KV，这样循环次数增加也不会多占显存。预训练前 4.5T token 直接用 NVFP4，总共训练 6T token，上下文 256K，只支持英文。同时放出 BF16、MXFP8、NVFP4 和 GGUF Q5_K_M 四个版本。
- 为何重要：用同一个 checkpoint 就能按任务调算力，这个思路本身新；又是 NVFP4 原生预训练的公开样本，研究价值高于马上能用的价值。
- 对谁有用：研究推理期扩展、循环 Transformer 的人；想在小模型上用算力换精度的端侧开发者。
- 已核：BF16 版 createdAt 2026-10-17 02:25 SGT（10-16 18:25:29Z），lastModified 2026-10-17 07:54 SGT（10-16 23:54:11Z），likes 90 / dl 674；GGUF 版 likes 29 / dl 461。license 是 OpenMDW-1.1；pipeline text-generation；卡面 Release Date 写 2026-10-16。
- 待核：卡面数字都是自测，比如循环 4 次时 SWE-bench Verified 73.4（带 † 标记）、GPQA Diamond 85.35。vLLM 和 llama.cpp 的支持还在 PR 里（vllm#60149、llama.cpp#30306），还没合并进主线。目前没有找到单独的博客或论文。
- 链接：[HF 仓库](https://huggingface.co/nvidia/NVIDIA-Nemotron-Labs-Dory1.0-4B-BF16) · [GGUF](https://huggingface.co/nvidia/NVIDIA-Nemotron-Labs-Dory1.0-4B-GGUF) · [HF Collection](https://huggingface.co/collections/nvidia/nemotron-labs-dory)

## 旁线（本窗新发或更新，但信号较弱或比较垂直）
- **tencent/Hy-Memory-30B-A3B**：本窗新发。腾讯混元做的长期记忆专用模型，约 3B 激活，用来替换 Mem0、MemOS 这类记忆框架里负责写入记忆的那个 LLM，决定该记什么、怎么改。训练分两步，先在策略蒸馏（OPD），再做归因强化学习。卡面称它在 4 种框架上平均 55.49，Opus 5 是 54.62（只在 20% 的子样本上测，待核）。createdAt 2026-10-15 17:52 SGT（09:52:00Z），lastModified 10-16 16:12 SGT，likes 160 / dl 736，apache-2.0，Trending 排第 31。FP8 版 10/16 新建，10/18 08:06 SGT 还在更新，dl 0。[HF](https://huggingface.co/tencent/Hy-Memory-30B-A3B) · [arXiv 2610.22196](https://arxiv.org/abs/2610.22196) · [GitHub](https://github.com/Tencent-Hunyuan/Hy-Memory)
- **nvidia/Nemotron-3.5-Rerank-8B-BF16**：本窗新发。多语言、多模态的重排序模型，文档里可以有文字、页面截图、图表，基于 Ministral-3-8B，OpenMDW-1.1 许可。createdAt 2026-10-15 16:42 SGT（08:42:42Z），likes 16 / dl 851。待核：卡面 Release Date 写的是 10/20/2026，比实际上线晚，可能是笔误，也可能是计划中的正式日期。[HF](https://huggingface.co/nvidia/Nemotron-3.5-Rerank-8B-BF16)
- **tencent/Qwen3-8B-DSpine-b16**：本窗新发。投机解码用的并行草稿模型，对应论文 arXiv 2609.36173。卡面称在 Qwen3-8B 上平均接受长度 7.83，DFlash2 是 7.55（待核）。createdAt 2026-10-16 22:52 SGT，likes 21 / dl 151，apache-2.0。[HF](https://huggingface.co/tencent/Qwen3-8B-DSpine-b16) · [arXiv](https://arxiv.org/abs/2609.36173)
- **ibm-granite/granite-switch-4.1-30b 和 8b**：上一窗口末尾新建，createdAt 10-15 05:23 和 05:38 SGT，上期没写；HF 博客 10/15 发布，本窗内又更新了卡。它把 base 模型、aLoRA 适配器和语音编码器组合在一个端点里，用控制 token 在对话、决策、语音转文字之间切换。30b 版 likes 20 / dl 382，8b 版 likes 24 / dl 567，apache-2.0。[HF 30b](https://huggingface.co/ibm-granite/granite-switch-4.1-30b) · [HF 博客](https://huggingface.co/blog/ibm-granite/granite-switch-4-1)
- **OpenMOSS-Team/MOSS-Image-Base 和 MOSS-Image-SFT**：10/11 建的仓库，上期没写，本窗是热度延续。Base 和 SFT 在 Trending 排第 17、18；10/17 03:30 SGT 有更新。社区的 Comfy-Org/MOSS-Image 打包版 10/16 新建，dl 90,456。apache-2.0。[HF SFT](https://huggingface.co/OpenMOSS-Team/MOSS-Image-SFT)

## 榜单（只列实际读到的；读取时间约 2026-10-18 09:21–09:25 SGT）
- **LMArena 文本榜**（[lmarena.ai/leaderboard/text](https://lmarena.ai/leaderboard/text)）：页面标注 Oct 15, 2026，共 8,834,211 票、416 个模型。前五名：Gemini 4 Argon (High) 1524±9（Preliminary）、Muse Wonder (Max) 1509±11、Claude Opus 5.5 (High) 1508±7、Claude Fable 5 (High) 1504±4、Claude Opus 4.6 (High) 1503±3。开源权重里最高的是第 18 名 Kimi K3 (Max) 1487±5，其次是第 27 名 MiMo-V2.6-Pro 1479±9、第 28 名 GLM-5.3 (Max) 1479±5、第 38 名 DeepSeek-V4.1-Flash (Max) 1475±6。窗内新出现的有 nvidia-nemotron-3.5-super-vl-120b-a12b-nvfp4，第 138 名，1416±12，Preliminary。DeepSeek 1017 版和 Beam 还没上榜。
- **LMArena 视觉榜**（[lmarena.ai/leaderboard/vision](https://lmarena.ai/leaderboard/vision)）：页面标注 Oct 9, 2026，比本窗早，所以本窗没有更新。第一名 Claude Fable 5 (High) 1308±7，第二 Qwen3.8-Max 1301±7，第三 Claude Opus 4.6 (High) 1299±6。
- **LMArena 生图榜**（[lmarena.ai/leaderboard/text-to-image](https://lmarena.ai/leaderboard/text-to-image)）：页面标注 Oct 7, 2026，同样早于本窗、本窗没有更新。第一名 GPT-Image-2.5 Sunburst 1425±7（Preliminary），第二 GPT-Image-2.5 Flare 1398±7，第三 GPT-Image-2 (Medium) 1383±4。开源里最高的是第 19 名 Qwen-Image-2.1 1223±7（Preliminary）。FLUX 3 Image Klein 还没上榜。
- **Artificial Analysis**（[首页](https://artificialanalysis.ai/)，Intelligence Index v4.3.2；首页图表默认只显示 703 个模型中的 27 个，下面的名次只是这 27 个里的相对位置，不是全榜排名）：最高的是 Claude Opus 5.5 (Max) 57.6、Claude Sonnet 5.5 (Max) 56.0、Muse Wonder Full (Max) 55.8。开源里最高的是 MiMo-V2.6-Pro 46.3，之后是 GLM-5.3 (Max) 44.8、Step 5 Preview 43.7、Kimi K3 (Max) 43.6。AA 自己的更新日志里，本窗新增了这些评测：10/15 的 Nemotron 3.5 Super VL（26.5）、Nemotron 3.5 Bolt 74B-A9B、Muse Spark Open (Xhigh)（38.9）、Solar Pro 4，以及 10/16 的 Beam 1.0（30.3）。
- **变化判断**：手上只有当前这一份快照，没有窗口开始前的存档，所以名次升降无法确认。能确定的“窗内变化”只有两类：一是 LMArena 文本榜页面日期是 10/15，二是 AA 更新日志里写明的新增评测。
- **Open LLM Leaderboard**：Space 还在运行，但 lastModified 停在 2026-05-27，这次没有读到具体名次，所以不写。

## 热度延续（本窗没有新权重）
google/embeddinggemma-2、jialinyyzz/humanizer、openbmb/MiniCPM-V-4.7-35B-A3B（本窗只更新了量化版和 DSpark 版）、fishaudio/drama-3、meta-models/Muse-Spark-Open-816B-A42B（gated: manual，10/15 有更新）、Lightricks/LTX-2.5、LiquidAI/LFM2.5-24B-A2B（上期写过；本窗 org 里只有 d1-omni-600M-GGUF 有更新）、Qwen/Qwen-Image-2.1-Turbo、Qwen/Qwen3.8-27B、autotrust/JEV-27B-VL、Cloudflare/clef。数据集 Trending 前 30 里，没有一个是本窗新建的。排在前面的 DeepLethe/FDE-Gym（10/06）、datasocial/tiktok-5.6B-videos、FineEnvs/openai-math 都是老面孔；Qwen/BlenderWorld 是 10/14 建的，排第 18。

## 降权
- 只是维护或改卡：zai-org 的 GLM-5.3 和 GLM-5.3-Flash（10/15 06:32 到 06:53 SGT 有提交，没有新权重）、Aleph-Alpha/Kolibri-1 和 BF16 版、mistralai 的 Timestral 系列（仓库 10/14 建，属于上一窗口；本窗只改了卡；Mistral 官网的 Timestral 页面 datePublished 是 2026-07-15）、ibm-granite 的 granitelib 和 switch-preview 系列旧仓库、nvidia 的 Kumo、ARDY、GEM-X、magpie_tts 等老仓库，以及 nvidia/Muse-Spark-Open-816B-A42B-DFlash2（第三方模型的草稿模型）。
- 社区再打包或量化：autotrust/Qwen3.8-27B-NVFP4-DGX-SPARK（本窗新建，只是量化）、unsloth Beam GGUF、Comfy-Org/MOSS-Image、lodestones/MOSS-Image-SFT-8-steps-dmd。
- 魔改、Uncensored、堆名字的仓库不写：abenzerps 和 AtomicChat 的 Qwen-Image Uncensored、dealignai/DeepSeek-V4.1-Flash-UNCENSORED-FP8、orcarouter Uncensored GGUF、DavidAU Heretic、nerkyor 那个名字堆砌的 SFT 仓库。
