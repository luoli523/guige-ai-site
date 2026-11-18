# 2026-11-18 AI行业动态：全量原始素材

本期信息窗口从 2026 年 11 月 15 日 09:00 起，至 11 月 18 日各来源的实际采集截止，时区为 Asia/Singapore。本文保留四路采集到的全量原始摘要与来源链接，不是深读成稿，也不意味着所有候选均已独立复现。正文另见[本期深读](https://guige.ai/guige-ai-site/daily/2026-11-18/)。

- 研究与官博：官博约截止 11 月 18 日 08:58，arXiv 约截止 09:06；包括研究汇总、官方原文摘录和论文候选三份材料。arXiv 11 月 16 日、17 日两批列表完整；11 月 15 日周日按常规无批；11 月 18 日那批在截止时只陆续出现部分编号、列表页尚未切换，属于未放完，不是“无更新”。Apple Machine Learning Research 另有两篇标注为 11 月 10 日的补录，不是本期新发。Thinking Machines 窗口内无新博文。
- X 公开动态：约截止 08:50；首页时间线只覆盖约 11 月 18 日 00:13 之后，此前时段以官方账号检索、公开检索与官方页面补齐，不代表全量时间线。
- GitHub 项目与发行：榜单与仓库快照约为 08:50–08:52；日榜、周榜不等于本期净增。
- 模型与数据集：HF 统计快照约为 08:59，热榜读取约 08:51，LMArena 读取约在 08:54–08:56；保留模型卡、权重提交、许可、榜单与同名仓库记录，下载量为 HF 近 30 天口径。

原始材料之间可能保留不同取舍，以下说明用于避免误读：Anthropic 在采集时点（约 11 月 18 日 08:50，即美东 11 月 17 日 19:50）尚未定价、未开盘，$70–78 为招股文件中的预计区间，约 1.4 万亿美元估值为媒体推算，待核，不是定价或市值；GPT-6.2 价格以 OpenAI 官方为准，OpenAI SDK 中的 GPT-6.2 仅为目录标识，不是权重；Qwen4-Max、Sage S2.1 Flash、vLLM、Nemotron 等的成绩与倍数多为厂商或作者自报，Nemotron 3.5 Bolt 的 2.74 倍与 1.21 倍基线不同，不能合并；Sage S2.1 Flash 是在 GLM-5.3-Flash 上后训练的模型，不是新基座，其 arXiv 列表摘要误作“S1.5 Flash”，以 PDF 为准；苹果 FastFrames 为仅限非商用研究的许可，不是开源，SenseNova-Loop-9B 为 Apache-2.0；Inkling 2 Small 本窗口只改了 config.json 中的一项推理参数，权重未变，影响待核。冒名仓库与假权重（如 Gemini-Config-Checker 克隆、gylive/google-ultra、借 Gemini 4 名义的“泄露权重”）只作安全提醒，原材料中的相关记录照录，不构成推荐；合法转存的非官方仓库不等于冒名。

除去内部协作名称、个人隐私、内部本地证据路径、来源标记和不宜公开的安全操作细节，正常来源与候选保留；未读、待核、自报与不收录理由照录。以下材料不是投资、上线或商业授权建议。


## 研究与官博

### 研究汇总

#### 研究素材包 · 2026-11-18（窗口 2026-11-15 09:00 → 11-18 ~08:58 Asia/Singapore）

> 官博 4 条 + arXiv 5 条（共 9 真重点）。数字标 来源记录 / 官方自报 / 作者自报 / 待核。原始摘录见同目录 labs-raw.md、arxiv-raw.md。
> arXiv：Asia/Singapore **11/16、11/17** 批新稿+交叉列表完整（pastweek / catchup 为 showing N of N）；**11/15（周日）无批**（常规日程，来源记录）。扫描宇宙自 **2611.17338** 起。Asia/Singapore **11/18** 批截至约 **09:06 Asia/Singapore** 列表与 catchup 仍未切换，但 abs 探测自 09:01 起已有 **2611.21612+** 陆续 200——**不得写成该批无更新**。续扫 **2611.21612+** 与周三正式 listing。
> 网络安全、生物与对齐条目只写结论与官方/作者数字，不写利用/合成/实验步骤。数字均保留设定与基线，**勿**无条件跨模型、跨硬件、跨基准比较。GPT‑6.2 系统卡与 Hydrogen 安全报告均只读了概述/执行摘要，未逐表深读，引用须带这一层。

##### 官博

###### 1. OpenAI：GPT-6.2 Astra 与 Sol
把 GPT‑6.x 线换成新的前沿档 Astra 与日常档 Sol：主打更难的专业工作、更少输出 token、更低单价，并同时放出完整系统卡。是本窗口最大的官方模型发布，也是要不要从 GPT‑6 Astra / 6.1 Sol 换上去的硬参考。
- News RSS `Tue, 17 Nov 2026 17:45:00 GMT` → **2026-11-18 01:45 Asia/Singapore**（来源记录）。系统卡文首日期 **2026-11-17**，119 页；Hub 列表亦标 Nov 17。变更日志称 11-17 对「AI Self-Improvement / High 阈值」表述有过措辞修订。价（官方自报，每百万 token）：Astra **$8** 输入 / **$0.40** 缓存输入 / **$40** 输出，相对 GPT‑6 Astra 输入/输出降 **20%**、缓存输入再打 **60%** 折；Sol 沿用 GPT‑6.1 Sol 的 **$2 / $0.10 / $10**。即日起 ChatGPT Work 与 Codex 向 Plus、Pro、Enterprise、Edu 开放（Enterprise / Edu 需管理员开启）；API 为 `gpt-6.2-astra`、`gpt-6.2-sol`。Pro 500 可用两模型 Ultrafast；首次把 Ultrafast 扩到 Pro 200，先从 Sol 开始。榜多为相对分、**文中常不给绝对分，勿补**（官方自报）：Agents' Last Exam 上 Astra 称创新高，比 GPT‑6 Astra 高 **5.2** 分、成本不到三分之一，比 Claude Fable 5.2 高 **5.5** 分、成本约 **5%**——脚注写明 Fable 5.2 的榜排除了用后备模型的 **9** 道题。Terminal-Bench-Science 0.1：比 GPT‑6 Astra 高 **9** 个百分点，成本不到三分之一；脚注提醒 Fable 5.2 在 Artificial Analysis 的 mini-swe-agent 与 Anthropic 自报 Claude Code **74.6%**（max）不是同一套件。FrontierCode 2.0：Sol 在 max 下距 Astra 约 **0.5** 分，成本约五分之一。LifeVal：Sol 分高于 GPT‑6 Astra，成本约七分之一。Harvey LAB‑AA v1.1：Astra 称 SOTA，通过率超过 Fable 5.2 的两倍，成本约六分之一。内部 GDPval v2：Astra 比 GPT‑6 Astra 高 **6.2** 个百分点，输出 token 少 **22%**；Sol 比 GPT‑6.1 Sol 高 **5.3** 分。AA‑AnalystAgent：Astra 在「五次独立尝试全部正确」口径下答对 **62.5%**。对齐仅结论：多数评测与 GPT‑6 Astra 相近，模拟职场任务中不当行动更少，但在两项测试中更常不提及挡住工作的障碍（如缺失文件、搜索工具不可用）；称已在 Codex 加指令显著减少这类遗漏，仍在调查。安全阈值（系统卡/发布文，仅高层）：两模型在 Preparedness Framework 下均达网络安全 **Critical**、生物/化学 **High**；Astra 另外达到 AI Self-Improvement **High**，Sol **未达到**。系统卡称 Astra 是其「对外发布的模型里第一个」达到该 Self-Improvement High 阈值。默认收紧更高风险网安协助。发布文中的网安基准明确是**关闭网安防护与分类器**的内部配置，不可当成线上系统表现。系统卡概述另外写到（官方自报，仅结论）：非对抗条件下两模型在最低 reasoning 档推理痕迹更短、更难只靠 CoT 监控；对抗测试中 Astra 在部分设定上更会规避 CoT 监控，但监控者若同时看到行动，成功的破坏/逃逸很少不被发现。评估察觉：Astra 比 GPT‑6 Astra 更常表示怀疑自己在被测，相关迹象标为不到 **3%** 的回合；Sol 低于 GPT‑6 Astra 与 GPT‑6.1 Sol。并称加强了防未授权蒸馏。系统卡 119 页**只读了概述与发布文已交叉的结论，未逐表抄录**。
- 对谁有用 / 深读：要换模型或做成本核算的应用方；对齐/安全读者应读系统卡概述与第 2、4 节，不要只看发布文榜。配读同窗产品向的 [Astra for Law](https://openai.com/index/astra-law-6-2)（LAB‑AA 全文达标 20.8% vs 基础 Astra 15.0%，官方自报）。与上期 CoT 可监控性文是同一监督问题的后续观察，不可把「不到 3% 回合」读成已解决监控。
- [官博](https://openai.com/index/introducing-gpt-6-2-astra-sol)（RSS **11-18 01:45 Asia/Singapore**）· [系统卡 PDF](https://deploymentsafety.openai.com/gpt-6-2-astra-sol/gpt-6-2-astra-sol.pdf)

###### 2. Google DeepMind：Gemini 4 Hydrogen Safety & Security Report
上期 Hydrogen 发布文只给出模型卡摘要，并写完整安全报告即将发布。本窗该 78 页报告已上线，执行摘要给出与 Carbon / Argon / 3.8 Flash 对照的官方阈值结论。这是上期最大模型发布的实质补完，不是新模型。
- 报告封面只写 **November 2026**（月级）。GCS `Last-Modified: Tue, 17 Nov 2026 15:41:41 GMT` → **11-17 23:41 Asia/Singapore**（来源记录，文件时间，不一定等于对外宣布时刻）。DeepMind 博客 RSS **没有**单独公告。模型卡同期已改文案：上期卡（`Last-Modified` 2026-11-12 18:00:14 GMT）写「即将发布 / coming soon」；本期卡 `Last-Modified: Mon, 16 Nov 2026 13:02:01 GMT` → **11-16 21:02 Asia/Singapore**，改为「Please see the full Safety & Security Report … here」。执行摘要写明：除非另注，评测关了模型外生产防护、也没有搜索接地，测的是模型层；线上另有推理时防护。前沿安全（官方自报，仅高层）：Material Capability Change 评估称 Hydrogen 能力相对 Gemini 4 Argon **总体下降**，因此未要求完整一套临界能力评测。但因不能排除 Argon / Carbon 已达生物信息 CBRN CCL 与网络安全 CCL，对 Hydrogen 做了这两域的针对性评估：**未达到** CBRN 或网络安全 CCL，但**达到了两域的 CCL 警戒阈值**，并继续叠防护。从 Argon 沿用：未达化学/放射/核的 CBRN TCL，也未达有害操纵 CCL 与 ML R&D CCL。未测 Stealth / Situational Awareness TCL，但按「已达 TCL」的保守假设部署缓解。内容与智能体误用：禁止内容评测称匹配或优于 3.8 Flash、与 Carbon 相当；Antigravity 套件里面对恶意工具请求的安全行动率显著高于 3.8 Flash、与 Carbon 相当，但对良性提示的拒答也多于两者。对齐与交互：健康评测多数优于 3.8 Flash；智能体诚实基准通过 **94%**；称迄今 Gemini 模型中表面迎合分最低。间接注入：称显著强于 3.8 Flash，红队评估中多数智能体能力上接近更大的 Carbon——执行摘要未给单一倍数，**不要把上期发布文里的 2.3× 在未核本节表格前直接搬过来**。防御向网安效用（仅结论）：CWE-bench v2（250 题、185 个 CWE、六类语言）上 Hydrogen Pass@1 **68.1%**，高于 Argon **65.0%**，单次 rollout 成本约降三分之二。进攻性利用基准数字不转写。78 页报告**只读了执行摘要与 CCL 结论，未逐节复核表格**。不要把「未达 CCL、达警戒阈值」写成「已达临界能力」。
- 对谁有用 / 深读：要引用 Hydrogen 安全结论、或对照 GPT‑6.2 系统卡阈值口径的人。与本窗官博 #1、arXiv #8 Soteria 都在谈「安全地干活」，但分别是模型层阈值、实验室系统卡与形式化运行时执行层，不可把 CCL、Critical 与「零违规」读成同一套标准。
- [报告 PDF](https://storage.googleapis.com/deepmind-media/gemini/gemini_4_hydrogen_safety_report.pdf) · [已更新的模型卡](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Hydrogen-Model-Card.pdf)

###### 3. OpenAI：第一阶段嵌入式评估
与 Apollo Research、METR、Transluce、Goodfire 签订第一阶段「嵌入式评估」协议，让独立评估方在较长时间里进入内部模型、训练与监控系统，评估对齐和防护是否站得住，并服务其安全论据。这是程序与承诺文，还不是评估结论；把第三方评测从发布前点测推进到可进内部系统的安排。
- RSS `Mon, 16 Nov 2026 08:00:00 GMT` → **2026-11-16 16:00 Asia/Singapore**（来源记录）。视评估需要，评估方可获得部分与内部研究同类的资源：检查点、源码、训练/评测数据、监控系统、技术文档，以及责任工程师的说明（官方自报）。分工：Apollo 分阶段看训练是否激励颠覆、评测与红队能否引出、内部使用中是否已出现、相关推理是否可被发现。Goodfire 做内部可解释性与训练监控，主要服务内部研究者，并计划公开阶段性发现。METR 第一阶段聚焦其迄今最大的前沿 RL 训练，评估既有测试与监控可能漏掉的错位；另有范围待双方确认的监控评估。Transluce 先评估训练后对齐评测的质量与覆盖，并意向在 2027 年初做约 8 周后续评估。披露：Apollo 与 Goodfire 接受付费但报酬不与结论挂钩；METR 与 Transluce 不接受评估酬劳，但可接受评估期内的 API/算力。安全委员会（SSC）可见未删节报告。脚注承认 METR 本阶段范围小于 METR 自己提案里的广泛错位普查。
- 对谁有用 / 深读：安全治理、政策与评测设计。注脚里 METR 先前约 3 周监控演练是更早材料，不当新发。可与官博 #1 系统卡对照读：一边是实验室自报阈值，一边是独立方将要进内部核查的范围。
- [官博](https://openai.com/index/our-first-phase-of-embedded-assessments)（RSS **11-16 16:00 Asia/Singapore**）

###### 4. Microsoft Research：TokenEconomizer
不改智能体、也不改底层模型，从同一仓库的历史会话里学习，给后续会话减 token 浪费（微技能笔记、裁掉很少用的工具、在失败打转时插入提示）。把「同一仓库里反复开工」写成可插拔的黑盒省钱方法，并给出跨组合的成本区间。开源插件来自 UC Berkeley、Microsoft Research 与 Microsoft Security，不要写成「MSR 单独论文」。
- feed `Mon, 16 Nov 2026 17:01:35 +0000` → **2026-11-17 01:01 Asia/Singapore**（来源记录）。页面 Published November 16（美国日历日）。画像（Claude Code、SWE-Bench 60 题、按仓顺序，官方自报）：仓内至少 5 个完成任务后，**30%** 的工具调用重复该仓更早动作，只有 **7%** 与其他仓历史匹配；每轮下发 23 个工具说明，其中 16 个从未被调用；失败的 **17%** 任务占了 **32%** 花费。主结果：277 个真实修 bug 任务、五个智能体–模型组合，平均每任务成本降 **18.4–30.9%**，所测每个仓库成本都下降；Pass@1 在其中四个组合上升。Web-Bench 顺序 Web 开发成本降 **16.0–21.2%**。安全审计（每题新仓库、经验更难迁移）成本降 **6.4–19.6%**。开源插件称不需要自己的 API key，所学留在开发者机器上。「四个组合 Pass@1 上升」不是统一的质量提升保证；安全审计数字不要解读成攻防能力。
- 对谁有用 / 深读：在同一仓库里反复跑编码智能体、关心 token 账单的人。与同窗 arXiv #7 都在「同一环境里积累经验」，但本条是不改智能体的黑盒省钱插件，#7 是在同一在线协议下比较上下文适应与权重更新；**不可**把 18.4–30.9% 成本下降与 51.6% 成功率混读。
- [官博](https://www.microsoft.com/en-us/research/blog/tokeneconomizer-learning-from-experience-to-make-ai-coding-agents-more-efficient/)（feed **11-17 01:01 Asia/Singapore**）· [论文页](https://www.microsoft.com/en-us/research/publication/tokeneconomizer-experience-driven-black-box-cost-control-for-coding-agents/) · [代码](https://github.com/microsoft/TokenEconomizer)

##### arXiv

###### 5. 2611.21003 K2-Horizon（Institute of Foundation Models / MBZUAI）
MBZUAI 基础模型研究所一次放出六款完全开放的语言模型（0.9B 稠密到 375B-A23B MoE），并把中间检查点、预训练数据、训练日志和流水线代码按 LLM360 标准一起公开。这是本窗体量最大的开放模型发布：四款模型共用一份 22T token 的预训练配方，还把通常不公开的数据与训练流水线一并交出。
- Submitted 16 Nov 2026；**Asia/Singapore 归属 11/17**（Tue 新稿）。机构以 PDF 首页为准（HTML 机构栏转换残缺，来源记录）：K2 Team, Institute of Foundation Models；Mohamed bin Zayed University of Artificial Intelligence。文中 LLM360、NVIDIA TensorRT-LLM、Diffusion Gemma / Nemotron 等是开放定义、工具或对照，**不是**作者单位。作者自报：36B-A4B 使用 MoVA 与 softplus attention gating，在**同一数据**上接近 32B 稠密模型，激活参数约为其 **1/7**。Uno 是无损 diffusion adapter，无需单独草稿模型，解码最高约 **2.2×**（摘要未写明硬件与并发）。流水线产出约 **10T** 合成预训练 token；四款模型共享 **22T** token 语料。PDF 首页还列出 6 个模型、380 个检查点、23 个量化构建、21.6 TB 训练数据、58 次训练运行、17 个代码库。摘要只说在 agent / 代码基准上「领先或具有竞争力」，**未**给出具体分数，不能与 Nemotron / Sage / GPT‑6.2 横比。
- 对谁有用 / 深读：开源复现、MoE / 注意力变体、合成预训练数据、推理加速（Uno）、agent / 代码模型选型。
- [论文](https://arxiv.org/abs/2611.21003) · [项目](https://ifm.ai/k2/)

###### 6. 2611.20771 Nemotron 3.5 Bolt E4B 4GB（NVIDIA）
NVIDIA 把 Gemma-4-E4B-it 再后训练成一款约 4GB 内存的小模型，面向本地语音助手、角色和边缘/机器人接口，并配上 DFlash 草稿器来加快解码。本窗唯一的大厂小模型官方报告，数字把「准确率」和「速度口径」拆得很清楚，可直接对照要不要从 Gemma-4-E4B 或同尺 Qwen 换过去。Gemma-4-E4B-it 是继续后训练的**底座模型**（Google），不是作者单位；文中 Gemini 3.8 Flash、Claude Sonnet 5.5 只是图 1 的云端 TTFT 参照，不是准确率对照集。
- Submitted 16 Nov 2026；**Asia/Singapore 归属 11/17**（Tue 新稿，主类 cs.CL）。机构：NVIDIA（来源记录）。作者自报：在 21 项基准上，相对 **Gemma-4-E4B-it** 与 **Qwen3.5-4B**，推理与非推理两种模式都是「平均准确率最高、平均输出 token 最少」。配 DFlash 后，相对**同一模型、无投机解码、concurrency 1**，每用户解码速度为 **2.74×**；相对 **Gemma-4-E4B-it + MTP、batch size 1**，生成吞吐为 **1.21×**。这两条加速**不是**同一基线，不能合成一个「快 2.74 倍且准」的笼统结论。图 1 本地点为 RTX 5090、Q4_K_M 量化、输入/输出约 3000/50 token。
- 对谁有用 / 深读：端侧 / 语音 agent 部署、投机解码、NVIDIA NIM、小模型后训练。不要与同窗 K2 的 Uno「最高约 2.2×」或官博 #1 的成本比混用。
- [论文](https://arxiv.org/abs/2611.20771) · [博客](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB/)

###### 7. 2611.19700 测试时适应应写在上下文、权重，还是两者都要（UC San Diego 一作 work done at Apple + Apple）
智能体反复待在同一仓库、数据库或应用套件里时，经验可以留在上下文里，也可以写成权重更新；这篇在同一在线协议下把头对头比清楚。把 ICL、GRPO 和自蒸馏（SDPO）放进同一套「先评再学、只用自己的尝试和环境反馈」的协议，并指出 ICL 会偷懒跳过检查，加 GRPO 能补回来。机构应写成 **UC San Diego（Parsa Mirtaheri，work done at Apple）+ Apple（其余作者）**，不要写成单一的 Apple 论文。Qwen3.5-9B 是被测模型，不是作者单位。
- Submitted 15 Nov 2026；**Asia/Singapore 归属 11/17**（Tue 新稿）。作者自报：用 Qwen3.5-9B，在 SWE-bench Verified、AppWorld、ScienceWorld、BIRD-Critic-SQLite 抽出的 **109** 个任务、每环境 **5** 种任务顺序上，比较 14 种适应机制与无状态基线。跨环境平均成功：无状态 **28.8%**，最强 ICL 单独到 **49.4%**，再加 GRPO 到 **51.6%**（最高）。在每一种 ICL 策略上加 GRPO 都会抬高总平均；SDPO 则有好有坏。这些是该模型、这四类环境上的均值，不能外推到其他底座或环境。
- 对谁有用 / 深读：长期驻留 agent、上下文管理、可验证奖励 RL、测试时适应。与官博 #4 TokenEconomizer 的差异见上，勿把成功率与成本下降横比。
- [论文](https://arxiv.org/abs/2611.19700)

###### 8. 2611.17880 Soteria（Princeton University + Snowflake 一人）
先把智能体的多步工具计划做成可形式化验证的分层方案，执行时再按规范拦截，而不是在「安全」和「把活干完」之间只选一头。NeurIPS 2026 Oral；在报告的设定里做到零策略违规的同时，任务成功率仍高于最强基线。机构应写成 **Princeton University + Snowflake（Ankush Desai）**，不要写成单一的 Princeton 或 Snowflake 论文。只写结论，不写拦截或利用步骤。
- Submitted 13 Nov 2026；**Asia/Singapore 归属 11/16**（Mon 新稿）。作者自报：相对各设定下的**最强基线**，平均任务成功率为其 **1.7 倍**，策略规范**零违规**；各模型–基准对上的成功率为最强基线加 **4.7–43.9** 个百分点（平均即上述 1.7 倍）。正文还写基线符合率最高约 **93%**，对照为四种基线、四个模型。摘要未列基准名称与绝对成功率；1.7 倍不能脱离「相对最强基线、该套工具任务」来读。
- 对谁有用 / 深读：工具调用 agent 的策略合规、运行时守护、形式化规划。与官博 #1、#2 的模型层阈值不是同一层，不可把「零违规」读成已达或不达 CCL / Critical。
- [论文](https://arxiv.org/abs/2611.17880)

###### 9. 2611.20144 HEAMS（Mila – Quebec AI Institute + Mozilla 一人）
记忆系统不能只看任务分和延迟；HEAMS 把性能、效率、安全、隐私和用户主权放在同一套评测里，并加了一层可套在任意记忆系统上的治理包装。上期刚集中讨论过记忆设计与 KV 复用；这篇把「记对了就能用」改写成「还要能改、能删、不能被投毒」，并给出可复现的开源评测。机构应写成 **Mila – Quebec AI Institute + Mozilla（Matt Harris）**。Siva Reddy 在 HTML 中只署 Mila，**不要**按惯例外加 McGill。只写结论，不写投毒或攻击步骤。
- Submitted 15 Nov 2026；**Asia/Singapore 归属 11/17**（Tue 新稿）。作者自报：没有单一「谁最高」的总分——**没有任何记忆系统在所有性能基准上领先**；性能强的系统仍可能在隐私、用户主权和安全上很差。召回策略能降低不当披露，但会牺牲一些有用性；召回与保留策略都能提高对投毒的抵抗。文中有原型 MilaMem。具体分数见表，摘要未给可单独引用的准确率。
- 对谁有用 / 深读：agent 记忆产品、隐私与投毒评测、记忆治理策略。与同窗备选 CarryOn / AdMem 都在谈记忆与上下文取舍，但本条是跨系统的评测与治理框架，不是又一种记忆模块。
- [论文](https://arxiv.org/abs/2611.20144) · [代码](https://github.com/milatechtransfer/heams)

##### 备选

- NVIDIA Vera Rubin NVL72 的 [MLPerf Training v6.1](https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-achieves-up-to-2x-blackwell-ultra-performance-in-mlperf-training-v6-1/) 与 [Endpoints v1.0](https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-leads-agentic-inference-performance-on-mlperf-endpoints-v1-0/)（两篇 published 16:00Z → **11-17 00:00 Asia/Singapore**，来源记录）。训练：七项中六项称最快 time-to-train，每 GPU 相对高度优化的 GB300 NVL72 基线最高约 **2×**；DeepSeek-V3 671B MoE 在 1024 GPU 上 **4.14** 分钟，对照同规模 GB300 的 **8.03** 分钟；第七项绝对最快时间来自 10,240 GPU 的 **GB300** 集群（官方自报）。Endpoints 文明确写 **provisional**：共享最低端到端交互性 50 token/s/用户下，每千瓦吞吐相对 GB300 NVL72 超过 **10×**；按模型为 Kimi K3 **10× / 3×**、DeepSeek-V4.1-Flash **9× / 5×**、Qwen3.6-35B-A3B **5× / 3×**（吞吐/kW，及匹配并发下的交互性）。不要与 Google Cloud [Ironwood TPU 的同轮提交](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/training-performance-benchmarks-tpus/)（8192 颗 Ironwood 预训练 **1.70** 分钟等，官方自报）做未经声明的横比。
- OpenAI [Science at the Frontier](https://openai.com/index/science-at-the-frontier)（11-16 20:00 Asia/Singapore）：1,819 名科学家、580,186 条科学消息的使用研究；自报同样质量工作没有 AI 约需 **1.9** 倍时间，250 人中 **98%** 预期加快发现。生产力是自报、发现是预期，不建立因果。完整论文 PDF URL **待核**。配读 [科学博客开张](https://openai.com/index/our-new-blog-for-science) 与客座文 [格点上的标准模型候选定义](https://openai.com/index/step-toward-defining-the-standard-model)（均为 11-16 06:00 Asia/Singapore；后者是 Nathaniel Craig 的作者叙述，不宜写成「OpenAI 证明了标准模型」）。
- Apple [Split-and-Scale Latent 3D Representations](https://machinelearning.apple.com/research/split-scale-latent-3d)（列表/RSS **2026-11-16**，`00:00 GMT`，时刻待核）。推理时把预训练 tokenizer 用到场景的任意小区域以提高细节。arXiv [2611.16126](https://arxiv.org/abs/2611.16126) 落在上期已扫完的 2611.14520–17337 批，**论文本身可能上期已在 arXiv 出现**；本期新的是 Apple 官网挂出。
- [2611.21072 Sage S2.1 Flash](https://arxiv.org/abs/2611.21072)（多机构合作，含上海 AI Lab、复旦等，不要写成单一实验室；列表摘要误作 S1.5，以 PDF 标题 **S2.1 Flash** 为准）：3200 亿参数 MoE 技术报告。作者自报在其 33 项、七个领域、相对五个基线的对照上，OfficeQA Pro **72.2**、MLE-bench Lite **90.3 HumanRank** 等为第一，OSWorld-Verified **85.2** 等为第二。不能与 K2、Nemotron 或 Gemini 4 / GPT‑6.2 无条件横比。
- [2611.18642](https://arxiv.org/abs/2611.18642)（Yibo Liu，北京邮电大学；提交较早、Asia/Singapore 11/17 才放批）：交接笔记只能交出当时已想明白的东西，反复压缩的损失比换一个智能体更大。另有记忆/上下文备选 [2611.17808 CarryOn](https://arxiv.org/abs/2611.17808)、[2611.20605 AdMem](https://arxiv.org/abs/2611.20605)，可与 #9 HEAMS 配读。
- Anthropic [缩短协调漏洞披露窗口](https://www.anthropic.com/research/coordinated-vulnerability-disclosure-timelines)（列表 Nov 16，日级，时刻待核）：高危/严重 90→30 天，其余 45 天；正在被利用的仍是 7 天；不适用于未经人工复核的 AI 发现报告。政策文，仅高层。blog.google 的 EmbeddingGemma 2 [技术报告帖](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2-technical-report/)（11-18 01:00 Asia/Singapore）指向 arXiv 2610.37364；模型本身已在 **2026-10-06** 发布，不是本期新模型。

##### Apple 补录备忘（不是本期新发）

对照上期全列表 1189 条，本期 `/research` 全列表为 **1192** 条。除上面 Split-and-Scale（11-16，可作本期候选）外，多出的两条 slug 在上期 HTML 中不存在，但 `published` 标为 **2026-11-10**（日级，早于 11-15 09:00 起点），**不当本期新发**：
- [Toward a Theory of Evaluability](https://machinelearning.apple.com/research/theory-evaluability)（Kunal Talwar；arXiv [2611.10996](https://arxiv.org/abs/2611.10996)，亦落在上期 arXiv 批）
- [Understanding Private Evolution as Learning-Augmented Clustering](https://machinelearning.apple.com/research/private-evolution-clustering)（Audra McMillan, Kunal Talwar, Felix Zhou†；arXiv [2609.36678](https://arxiv.org/abs/2609.36678) 为 9 月稿）

上期已补录的 Nov 10/12 四条（Theoretical Limits of Language Model Alignment 等）不再重复。

##### 覆盖缺口

- OpenAI `/news`、`/news/research/` 与 `/index` 详情页 curl **403**，发布文等改用 WebFetch；科学家使用研究文内「完整论文」的 PDF URL 未解析出，**待核**。
- GPT‑6.2 系统卡（119 页）与 Hydrogen Safety & Security Report（78 页）**只读了概述/执行摘要，未逐表深读**。
- blog.google 主 RSS 只有 20 条，最旧一条为 11-16 22:00 Asia/Singapore；已用分类 RSS 补扫，未见 11-15 09:00 至 11-16 22:00 之间额外的研究长文，但消费类短帖在该空隙仍可能被挤出。
- arXiv：Asia/Singapore **11/18** 批截至约 09:06 Asia/Singapore **未放全**（catchup 0 条、`/new` 仍为周二横幅，abs 已见 2611.21612+ 但不连续）。续扫 **2611.21612+** 与周三正式 listing，须等 showing N of N 后再精选。**不得写成该批无更新**。11/16、11/17 新稿+交叉已完整；替换稿未当新条目精读。
- 未把缺访问写成无更新。Amazon Science 上期两条、Antigravity `/teamwork` 子结果仍未在本窗逐篇复核。DeepMind 博客 RSS、Google Research、Meta research / engineering.fb、Anthropic Newsroom / Engineering / Alignment、Thinking Machines、Amazon Science、OpenAI Alignment 窗内已成功访问、无新研究长文（非缺访问）。

### 官方原文摘录

#### Labs Raw Excerpts — 2026-11-18

- **窗口**: 2026-11-15 09:00 Asia/Singapore → **2026-11-18 08:58 Asia/Singapore**（Asia/Singapore, UTC+8；采集截止以本机 `date` 为准）
- **采集时间**: 2026-11-18 约 08:51–08:58 Asia/Singapore
- **说明**: 原始摘录；关键数字标「官方自报 / 来源记录 / 待核」。网络安全与生物仅写结论与官方数字，不写利用/合成/实验步骤、攻击轨迹或提示构造。已在上期主包或窗口外的条目不作为本期重点重复。
- **去重参照**: （内部证据存档）、`research.md`。上期已报勿重复：Gemini 4 Hydrogen 发布文、Antigravity `/teamwork` 汇编、Thinking Machines 端到端 4-bit 训练、OpenAI Fuzzy Robustness、Anthropic 安全评测方法文、Apple 补录 4 条（Theoretical Limits of Language Model Alignment、Evaluating the Evaluators、On the Importance of Gating、Weighted State Souping）。上期备选 NVIDIA cuBLAS FP64、SOMA Retargeter、GLM-5.3 + vLLM，以及更早各期主包，不当新条目重报。上期数字不在此复述。
- **专项跟进**: 上期标「即将发布」的 Gemini 4 Hydrogen Safety & Security Report，本窗内已上线，按实质新进展收录。

---

##### OpenAI

**源查证**: [openai.com 来源](https://openai.com/news/rss.xml)（curl + Chrome UA，HTTP 200，1406 条）；[openai.com 来源](https://openai.com/news/) 与 `/news/research/`、`/index/` 详情页 curl **403**，正文用 WebFetch 核。辅以 [alignment.openai.com 来源](https://alignment.openai.com/) 与 [alignment.openai.com 来源](https://alignment.openai.com/rss.xml)（均 200）。系统卡不在 News RSS 里单独成条，由发布文指向的 Deployment Safety Hub 取到官方 PDF。

###### 1) Introducing GPT-6.2 Astra and Sol — **建议进主包（前沿模型发布）**
- **日期**: News RSS `Tue, 17 Nov 2026 17:45:00 GMT` → **2026-11-18 01:45 Asia/Singapore**（来源记录）
- **URL**: [openai.com 来源](https://openai.com/index/introducing-gpt-6-2-astra-sol)
- **系统卡 PDF（官方）**: [deploymentsafety.openai.com 来源](https://deploymentsafety.openai.com/gpt-6-2-astra-sol/gpt-6-2-astra-sol.pdf)（标题 *GPT-6.2 Astra and Sol system card*，文首日期 **2026-11-17**；119 页。Hub 列表亦标 Nov 17, 2026。变更日志称 11-17 对「AI Self-Improvement / High 阈值」表述有过措辞修订。）
- **人话**: OpenAI 发布 GPT‑6.2 Astra（面向最难专业项目的前沿档）与 GPT‑6.2 Sol（日常执行档），主打「更难的专业工作、更少输出 token、更低单价」。Astra API 价相对 GPT‑6 Astra 输入/输出降 **20%**，缓存输入再打 **60%** 折；Sol 沿用 GPT‑6.1 Sol 的价。
- **要点**（均为官方自报，除非另注；许多头条只给相对分、不给绝对分，**勿补绝对值**）:
  - 定价（来源记录，发布文口径，每百万 token）: Astra **$8** 输入 / **$0.40** 缓存输入 / **$40** 输出；Sol **$2** / **$0.10** / **$10**。
  - 可用性（官方自报）: 即日起 ChatGPT Work 与 Codex 向 Plus、Pro、Enterprise、Edu 开放；API 为 `gpt-6.2-astra`、`gpt-6.2-sol`。Pro 500 可用两模型的 Ultrafast；首次把 Ultrafast 扩到 Pro 200，先从 Sol 开始。Enterprise / Edu 需工作区管理员开启。
  - Agents' Last Exam: Astra 称创新高，比 GPT‑6 Astra 高 **5.2** 分、成本不到三分之一；比 Claude Fable 5.2 高 **5.5** 分、成本约 **5%**。脚注：Fable 5.2 的榜把用了后备模型的 **9** 道题排除在外（官方自报，引用须带此限制）。
  - Terminal-Bench-Science 0.1: Astra 称创新高，比 GPT‑6 Astra 高 **9** 个百分点，成本不到三分之一。脚注说明 Fable 5.2 在 Artificial Analysis 的 mini-swe-agent 与 Anthropic 自报的 Claude Code **74.6%**（max）不是同一套件，不可混用。
  - 另称在 Vals Science Index 创新高（未在发布文给出绝对分）。FrontierCode 2.0：Sol 在 max 设定下距 Astra 约 **0.5** 分，成本约五分之一。LifeVal：Sol 分高于 GPT‑6 Astra，成本约七分之一（均无绝对分）。
  - Harvey LAB‑AA v1.1：Astra 称 SOTA，通过率超过 Fable 5.2 的两倍，成本约六分之一；Astra for Law 配置更高（详见另文）。内部 GDPval v2：Astra 比 GPT‑6 Astra 高 **6.2** 个百分点，输出 token 少 **22%**；Sol 比 GPT‑6.1 Sol 高 **5.3** 分。AA‑AnalystAgent：Astra 在「五次独立尝试全部正确」口径下答对 **62.5%** 的问题。
  - 对齐（发布文与系统卡一致，仅结论）: 多数对齐评测上与 GPT‑6 Astra 相近，模拟职场任务中不当行动更少；但在两项测试中更常不提及挡住工作的障碍（如缺失文件、搜索工具不可用）。称已在 Codex 加指令，显著减少这类遗漏，仍在调查。
  - 安全阈值（系统卡 / 发布文，仅高层）: 两模型在 Preparedness Framework 下均达网络安全 **Critical**、生物/化学 **High**；Astra 另外达到 AI Self-Improvement **High**，Sol **未达到**。系统卡称 Astra 是其「对外发布的模型里第一个」达到该 Self-Improvement High 阈值。默认收紧了更高风险网安协助；授权防御测试走 Daybreak，并称将努力把 6.2 接入 Daybreak。发布文中的网安基准明确是**关闭网安防护与分类器**的内部配置，不可当成线上系统表现。
  - 系统卡概览另外写到（仅结论，官方自报）: 非对抗条件下两模型在最低 reasoning 档推理痕迹更短、更难只靠 CoT 监控；对抗测试中 Astra 在部分设定上更会规避 CoT 监控，但监控者若同时看到行动，成功的破坏/逃逸很少不被发现。评估察觉：Astra 比 GPT‑6 Astra 更常表示怀疑自己在被测，相关迹象标为不到 **3%** 的回合；Sol 的评估察觉低于 GPT‑6 Astra 与 GPT‑6.1 Sol。并称加强了防未授权蒸馏。
- **局限**: 厂商发布文；多项「新高」只有相对分；跨厂商成本比依赖其计价与套件。系统卡 119 页，此处只摘概述与发布文已交叉的结论，未逐表抄录。网安/生物评测细节不转写。
- **为何重要**: 本窗口最大的官方模型发布，补上 6.x 线的新前沿档与日常档，并同时给出价、可用范围和完整系统卡（含 Self-Improvement High）。
- **对谁有用 / 深读**: 要换模型或做成本核算的应用方；对齐/安全读者应读系统卡概述与第 2、4 节，而不是只看发布文榜。配读 Astra for Law 配置文（产品向）。
- **标注**: 来源记录（RSS 时刻、价、系统卡 URL/页数）/ 官方自报 / 安全仅高层。

###### 2) Our first phase of embedded assessments — **建议进主包（独立安全评估机制）**
- **日期**: RSS `Mon, 16 Nov 2026 08:00:00 GMT` → **2026-11-16 16:00 Asia/Singapore**（来源记录）。页面亦标 November 16, 2026。
- **URL**: [openai.com 来源](https://openai.com/index/our-first-phase-of-embedded-assessments)
- **人话**: OpenAI 宣布与四家独立评估方签订第一阶段「嵌入式评估」协议：Apollo Research、METR、Transluce、Goodfire，在较长时间里深入其内部模型与系统，评估对齐和防护是否站得住，并服务其安全论据（safety cases）。也对接白宫 Super Intelligence 协议里的独立评估承诺。
- **要点**（官方自报）:
  - 视评估需要，评估方可获得部分与内部研究同类的资源：检查点、源码、训练/评测数据、监控系统、技术文档，以及责任工程师的说明。
  - 分工：Apollo 分阶段评估训练是否激励颠覆、评测与红队能否引出、内部使用中是否已出现、相关推理是否可被发现。Goodfire 做内部可解释性与训练监控，主要服务内部研究者，并计划公开阶段性发现。METR：第一阶段聚焦其迄今最大的前沿 RL 训练，评估既有测试与监控可能漏掉的错位；另有范围待双方确认的监控评估（文称此前有过约 3 周的监控红队演练）。Transluce 先评估训练后对齐评测的质量与覆盖，并意向在 2027 年初做约 8 周的后续评估。
  - 披露：Apollo 与 Goodfire 接受付费但报酬不与结论挂钩；METR 与 Transluce 不接受评估酬劳，但可接受评估期内的 API/算力。评估独立性、现场办公与设备、安全委员会（SSC）可见未删节报告、发表前可红acted 机密并请求负责任披露窗口，均有程序说明。脚注承认 METR 本阶段范围小于 METR 自己提案里的广泛错位普查。
- **为何重要**: 把「第三方评测」从发布前点测推进到可进内部训练与监控系统的嵌入式安排，并公开范围、限制和利益冲突。
- **对谁有用 / 深读**: 安全治理、政策与评测设计读者；注脚里的 METR 先前监控演练是更早材料，不当新发。
- **标注**: 来源记录 / 官方自报。这是程序与承诺文，还不是评估结论。

###### 窗口内其他 OpenAI（科学向可作候选；产品/事务不挤研究主包）

- **A step toward defining the Standard Model on a lattice**（RSS `Sun, 15 Nov 2026 22:00:01 GMT` → **11-16 06:00 Asia/Singapore**，来源记录）: 新开的科学博客首篇客座。UCSB / KITP 的粒子理论学者 Nathaniel Craig（文称 OpenAI visiting scientist）叙述他与 GPT‑6 Astra 合作，把一套候选的格点（lattice）标准模型非微扰定义写成构造与证明；指向 2026 年 10 月预印本。文内明确：这是候选定义，连续时空上的相互作用理论仍开放；并提到 OpenAI 近期 Yang-Mills 存在性证明是相关拼图。科学结果以作者叙述为准，不宜写成「OpenAI 证明了标准模型」。[openai.com 来源](https://openai.com/index/step-toward-defining-the-standard-model)
- **Our new blog for science**（同批 `22:00:00 GMT` → **11-16 06:00 Asia/Singapore**）: 宣布科学博客，回顾近月数学/物理/生物合作（Navier–Stokes、quasi-Riemann、QFT 基础、PerturbAI × Scripps 等），均为更早工作的索引，不当新结果。[openai.com 来源](https://openai.com/index/our-new-blog-for-science)
- **Science at the Frontier: How scientists use ChatGPT**（`Mon, 16 Nov 2026 12:00:00 GMT` → **11-16 20:00 Asia/Singapore**）: Economic Research 团队分析 Academic Researchers 夏季试点中 **1,819** 名科学家的 **580,186** 条科学消息（2026-08-20 至 09-22），并调查 **251** 人。分类器用隐私保护分类，研究团队称未阅读原文。调查口径：同样质量的工作，受访者估计没有 AI 要花约 **1.9** 倍时间；回答发现时间线的 250 人里 **98%** 预期 AI 会加快其领域发现。68% 的科学家至少用 ChatGPT 发展研究想法（采用定义见文）。生产力是自报、发现是预期，**不建立因果**。文末「完整论文 / 要点」链接因 `/index` 资源链未解析出 PDF URL，**PDF 地址待核**。[openai.com 来源](https://openai.com/index/science-at-the-frontier)
- **Broadening access to AI for scientists**（`Mon, 16 Nov 2026 17:00:00 GMT` → **11-17 01:00 Asia/Singapore**）: 把 ChatGPT for Academic Researchers 扩到目标 **20 万** 名研究者；下轮 11-23 起先到先得发放 **5 万** 份新资助（含最多两名合作者，新资助改为 Plus 而非 Pro）。产品/项目文，可作上述研究的配读。[openai.com 来源](https://openai.com/index/expanding-chatgpt-for-academic-researchers)
- **Astra for Law leads in legal intelligence**（RSS `Tue, 17 Nov 2026 00:00:00 GMT` → 若按字面 **11-17 08:00 Asia/Singapore**；`00:00:00 GMT` 也可能是日级占位，**时刻待核**）: GPT‑6.2 Astra 的法律配置。Harvey LAB‑AA：全文达标 **20.8%**，高于 GPT‑6.2 Astra **15.0%** 与 Muse Wonder Full **13.1%**；物质性幻觉每题 **0.03**，与 GPT‑6 并列最低（对比文内 Claude Opus 5.5 的 0.59）。Vals Legal Research Bench 11-16 评测：208 题中 112 题全文达标（**53.8%**），9 月约 46%。法律检索库称相对 9 月扩 **34%**，现约 **3.10 亿** URL。产品配置文，数字官方自报。[openai.com 来源](https://openai.com/index/astra-law-6-2)

**产品 / 事务（不建议挤研究主包）**: Introducing ChatGPT for Sales（11-17 16:00 Asia/Singapore）；ChatGPT for Healthcare 与医疗计算机使用智能体（均 11-16 14:00 Asia/Singapore）；LVMH 传媒合作（11-16 17:00 Asia/Singapore）；Introducing OpenAI for Chile、The King's Trust £1m 合作（后者 RSS `00:00 GMT`，时刻待核）；客户故事 Revolut、Holiday Extras。

**安全/政策（仅高层，不进研究主条）**:
- Strengthening NATO and allied cyber defenses with AI（RSS `Tue, 17 Nov 2026 00:00:00 GMT`，时刻待核）: 与北约及盟国网络机构合作，协助授权防御方找漏洞、测修复。[openai.com 来源](https://openai.com/index/strengthening-nato-allied-cyber-defences-ai)
- Strengthening the fight against online child sexual abuse with new tools and support（11-17 01:00 Asia/Singapore）: 称将提供新工具、指南与合作，用于预防、发现和应对线上性剥削。只记存在，不转写工具细节。[openai.com 来源](https://openai.com/index/strengthening-online-child-safety)

**alignment.openai.com**: 窗内无新帖（已成功访问列表与 RSS）。最新仍是上期已报的 Fuzzy Robustness（11-12）。

---

##### Anthropic

**源查证**: [anthropic.com 来源](https://www.anthropic.com/research)、`/news`、`/engineering`（curl 200）。无带时区的公开 RSS（`/rss.xml`、alignment `/rss.xml` 均 404）。研究页多为「Nov N, 2026」日级；部分 `article:published_time` 为当日 `00:00:00.000Z`（日级占位，时刻待核）。辅以 [alignment.anthropic.com 来源](https://alignment.anthropic.com/)（200，窗内无新帖）。

###### 3) Updating our coordinated vulnerability disclosure policy timelines — **建议作候选或边注（安全政策，非研究长文）**
- **日期**: 研究列表 **Nov 16, 2026**（日级，**时刻待核**）。属 Frontier Red Team 条目。
- **URL**: [anthropic.com 来源](https://www.anthropic.com/research/coordinated-vulnerability-disclosure-timelines)
- **人话**: Anthropic 缩短协调漏洞披露（CVD）窗口：高危/严重从 **90** 天改为 **30** 天，其余改为 **45** 天；正在被积极利用的漏洞仍是 **7** 天披露窗口（官方自报）。
- **要点**（官方自报，仅高层）: 难以及时修复的基础设施或需改规范/RFC 的缺陷，将与厂商另商时间表。该更新**不适用于**未经人工复核的、由 AI 发现的报告。称会继续附带可操作建议，并在向同一项目大量报送前协商节奏；同时提到面向关键开源维护者的扫描与 Claude Ultra 资助等支持计划。
- **为何重要**: 反映模型辅助找洞加速后，实验室把自己的披露时钟也拧紧了。
- **标注**: 来源记录（列表日）/ 官方自报 / 时刻待核。不写报送格式或漏洞细节。

**Newsroom**: 「Latest news November 18, 2026」只是页面当日抬头；列表最新新闻仍是 Nov 10 的 IPO roadshow 与 Nov 9 的 Fable / Mythos 5.2，**窗内无新新闻稿**（非缺访问）。
**Engineering**: 最新仍是上期已报的 Nov 13 安全评测方法文，窗内无新工程长文。
**更早已报、勿重复**: Building strong safety evaluations（Nov 13）、electronics design、Fable/Mythos 5.2 等。

---

##### Google DeepMind / blog.google

**源查证**: [deepmind.google 来源](https://deepmind.google/blog/rss.xml)（200，窗内无新博文，最新仍是 11-13 02:00 Asia/Singapore 的 Hydrogen 发布文）。[blog.google 来源](https://blog.google/rss/)（20 条，全部落在窗内）、`/innovation-and-ai/rss/` 及 models / developer-tools / cloud 分类 RSS（均 200）。Hydrogen 安全报告未出现在 DeepMind RSS，由**已更新的模型卡**内链取到官方 PDF。GCS `Last-Modified` 用于判断上线时间。

###### 4) Gemini 4 Hydrogen Safety & Security Report — **建议进主包（上期预告的完整安全报告，仅高层）**
- **日期**: 报告封面只写 **November 2026**（月级）。GCS `Last-Modified: Tue, 17 Nov 2026 15:41:41 GMT` → **2026-11-17 23:41 Asia/Singapore**（来源记录，文件时间，不一定等于对外宣布时刻）。模型卡 PDF 同期已改文案：上期（卡 `Last-Modified` 2026-11-12 18:00:14 GMT）写「完整报告即将发布 / coming soon」；本期卡 `Last-Modified: Mon, 16 Nov 2026 13:02:01 GMT` → **11-16 21:02 Asia/Singapore**，改为「Please see the full Safety & Security Report … here」，并链到下述 PDF。DeepMind 博客 RSS **没有**单独公告帖。
- **URL**: [storage.googleapis.com 来源](https://storage.googleapis.com/deepmind-media/gemini/gemini_4_hydrogen_safety_report.pdf)（78 页，HTTP 200，约 6.96 MB）
- **模型卡（已更新，非新模型）**: [storage.googleapis.com 来源](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Hydrogen-Model-Card.pdf)
- **人话**: 谷歌补上了 Gemini 4 Hydrogen 的完整 Safety & Security Report。执行摘要写明：除非另注，评测关了模型外生产防护、也没有搜索接地，测的是模型层，对照 Carbon 与 3.8 Flash；线上另有推理时防护。
- **要点**（官方自报，仅高层结论）:
  - 前沿安全：Material Capability Change 评估称 Hydrogen 能力相对 Gemini 4 Argon **总体下降**，因此未要求完整一套临界能力评测。但因不能排除 Argon / Carbon 已达生物信息 CBRN CCL 与网络安全 CCL，对 Hydrogen 做了这两域的针对性临界评估：**未达到** CBRN 或网络安全 CCL，但**达到了两域的 CCL 警戒阈值**，并继续叠防护。从 Argon 沿用：未达化学/放射/核的 CBRN TCL，也未达有害操纵 CCL 与 ML R&D CCL。未测 Stealth / Situational Awareness TCL，但按「已达 TCL」的保守假设部署 AI 控制与安全缓解。
  - 内容与智能体误用：禁止内容评测上称匹配或优于 3.8 Flash、与 Carbon 相当。Antigravity 智能体套件里，面对恶意工具请求的安全行动率显著高于 3.8 Flash、与 Carbon 相当，但对良性提示的拒答也多于两者。
  - 对齐与交互：健康评测多数优于 3.8 Flash；智能体诚实基准通过 **94%**；称迄今 Gemini 模型中表面迎合（sycophancy）分最低。间接注入：称显著强于 3.8 Flash，红队评估中多数智能体能力上接近更大的 Carbon（无在执行摘要给出单一倍数；上期发布文里的 2.3× 等数字不要在未核本节表格前直接搬过来）。
  - 防御向网安效用（仅结论与官方数字）: CWE-bench v2（250 题、185 个 CWE、六类语言）上 Hydrogen Pass@1 **68.1%**，高于 Argon **65.0%**，单次 rollout 成本约降三分之二。进攻性利用基准数字不转写。
- **局限**: 78 页报告此处只读执行摘要与 CCL 结论，未逐节复核表格；评测口径是关生产防护的模型层。不要把「未达 CCL、达警戒阈值」写成「已达临界能力」。
- **为何重要**: 兑现上期 Hydrogen 发布时欠缺的完整安全报告，给出与 Carbon/Argon 对照的官方阈值结论。
- **标注**: 来源记录（PDF 可取、GCS 时间、模型卡文案相对上期已变）/ 官方自报 / 报告发布时刻以文件时间为准、无博客公告。

###### blog.google 窗口内其他（研究相关可作候选；产品不挤主包）

- **Read the EmbeddingGemma 2 technical report**（jsonld `datePublished` **2026-11-17T17:00:00+00:00** → **11-18 01:00 Asia/Singapore**，来源记录）: 指向技术报告，介绍其把文本/图像/音频/视频映射到同一向量空间、并压缩骨干。模型本身的发布文在 **2026-10-06**（`datePublished` 2026-10-06T16:00:00+00:00，来源记录），**不是本期新模型**。技术报告链到 arXiv **2610.37364**（10 月稿）。可作文档补录，不宜写成新模型发布。[blog.google 来源](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2-technical-report/)
- **New AI training performance benchmarks for Google TPUs**（`2026-11-16T16:00:00+00:00` → **11-17 00:00 Asia/Singapore**，来源记录；`dateModified` 19:35 UTC）: Google Cloud 在 MLPerf Training v6.1 Closed 组公布 10 条结果（文内给了 6.1-0017–0026 编号）。官方口径：8192 颗第七代 Ironwood TPU 预训练到目标质量 **1.70** 分钟，扩到 4096 芯时效率 **96%**；640 颗 Ironwood 做新的智能体 RL 项，18.02 分钟达到目标准确率（0.765 vs 目标 0.69），训练芯等待不到 3%。Google Cloud A4X Max 上 256 颗 GB300 预训练 **31.96** 分钟。厂商/云提交，绑定具体 workload 与规模，勿与下面 NVIDIA 的 Vera Rubin 提交做未声明的横比。[blog.google 来源](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/training-performance-benchmarks-tpus/) 对照 [mlcommons.org 来源](https://mlcommons.org/2026/11/mlperf-training-v6-1-results/)
- **How genome mapping can help researchers better understand disease**（`2026-11-17T22:00:00+00:00` → **11-18 06:00 Asia/Singapore**）: 「Ask a Scientist」科普，解释已发布的 AlphaGenome / Atlas，**不是新模型或新论文宣布**。上期已报 AlphaGenome 2，本篇不当新进展。[blog.google 来源](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-disease-research/)

**产品 / 活动（不挤研究主包）**: Gemini 应用任务与免费新功能、地区口音、Notebook 交互站、Search 临时线程、Ask Maps 欧洲与假期功能、Flow/Vids/Wallet/Home、10 州免费 AI 培训、Play 年度榜、Carbon 开发者案例等。GTIG「AI threat tracker Q4 2026」为云安全威胁追踪产品文，仅高层记下，不转写手法。

---

##### Google Research

**源查证**: [research.google 来源](https://research.google/blog/rss/)（200，100 条）。窗内**无新帖**。最新仍是上期已报的 Antigravity `/teamwork` 汇编（RSS 2026-11-14 04:47 Asia/Singapore）。非缺访问。

---

##### Meta（research.meta.ai / about.fb.com / engineering.fb.com）

**源查证**: 未打开易坏的 ai.meta.com 主页。`research.meta.ai/blog/`（200）、`about.fb.com/news/` + `/news/feed/`（200）、`engineering.fb.com` + `/feed/`（200）。

- **research.meta.ai/blog/**: 已成功访问。列表最新仍是 November 9 的 Muse Ember 与 November 6 的 Specialized Models——均上期已报或更早，**窗内无新研究博文**（非缺访问）。
- **engineering.fb.com**: 最新仍是上期已报的 Cuttlefish on Mac（published 11-14 01:00 Asia/Singapore），窗内无新工程博文。
- **about.fb.com 窗内产品/地区新闻（不进研究主包）**: Muse 登陆澳大利亚（feed **11-18 02:00 Asia/Singapore**）；Instagram 印度推荐更新（11-17 11:58 Asia/Singapore）；Direct 聊天应用（11-17 09:00 Asia/Singapore）；新加坡中小企业 AI 培训调研（11-16 14:25 Asia/Singapore）。

---

##### Microsoft Research

**源查证**: [microsoft.com 来源](https://www.microsoft.com/en-us/research/feed/)（Chrome UA，200；feed 仍只展示约 10 条，已用博客列表交叉）。

###### 5) TokenEconomizer: Learning from Experience to Make AI Coding Agents More Efficient — **建议进主包或强候选（智能体成本 / 经验复用）**
- **日期**: feed `Mon, 16 Nov 2026 17:01:35 +0000` → **2026-11-17 01:01 Asia/Singapore**（来源记录）。页面 Published November 16, 2026（美国日历日）。
- **URL**: [microsoft.com 来源](https://www.microsoft.com/en-us/research/blog/tokeneconomizer-learning-from-experience-to-make-ai-coding-agents-more-efficient/)
- **论文页**: [microsoft.com 来源](https://www.microsoft.com/en-us/research/publication/tokeneconomizer-experience-driven-black-box-cost-control-for-coding-agents/)
- **代码**: [GitHub microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer) ；项目页 [tokeneconomizer.github.io 来源](https://tokeneconomizer.github.io)
- **人话**: UC Berkeley、Microsoft Research 与 Microsoft Security 的开源插件：不改智能体、也不改底层模型，从同一仓库的历史会话里学习，给后续会话减 token 浪费（微技能笔记、裁掉很少用的工具、在失败打转时插入提示）。
- **要点**（官方自报）:
  - 画像（Claude Code、SWE-Bench 60 题、按仓顺序）: 仓内至少 5 个完成任务后，**30%** 的工具调用重复该仓更早动作，只有 **7%** 与其他仓历史匹配；每轮下发 23 个工具说明，其中 16 个从未被调用；失败的 **17%** 任务占了 **32%** 花费。
  - 主结果：277 个真实修 bug 任务、五个智能体–模型组合，平均每任务成本降 **18.4–30.9%**，所测每个仓库成本都下降；Pass@1 在其中四个组合上升。Web-Bench 顺序 Web 开发成本降 **16.0–21.2%**。安全审计（每题新仓库、经验更难迁移）成本降 **6.4–19.6%**。开源插件称不需要自己的 API key，所学留在开发者机器上。
- **局限**: 作者自报、绑定 SWE-Bench / Web-Bench 与所述组合；「成功率和缓稳定、四个组合 Pass@1 上升」不是统一的质量提升保证。安全审计数字不要解读成攻防能力。
- **为何重要**: 把「同一仓库里反复开工」写成可插拔的黑盒省钱方法，并给出跨组合的成本区间。
- **标注**: 来源记录 / 官方自报。作者单位以博文署名（含 Berkeley 的 Ion Stoica、Bin Yu 等）为准，不要写成「MSR 单独论文」。

**其他**: 播客 *Can AI help build a healthier future?*（feed 11-18 00:52 Asia/Singapore）不作为研究长文。

---

##### NVIDIA

**源查证**: Atom [developer.nvidia.com 来源](https://developer.nvidia.com/blog/feed)（用 **`published`**，不用 `updated`）；[blogs.nvidia.com 来源](https://blogs.nvidia.com/feed/)。上期 cuBLAS FP64 / cuPhoton / cuDLA / GLM-5.3+vLLM / SOMA Retargeter 的 `published` 仍在窗前，不因 `updated` 重报。本窗正逢 SC26，开发者博客与公司博客都有一批新帖。

###### 6) NVIDIA Vera Rubin NVL72：MLPerf Training v6.1 与 Endpoints v1.0 — **建议作强候选（训练 / 智能体推理基准，厂商提交）**
- **日期**: 两篇开发者博文 published `2026-11-16T16:00:00Z` → **2026-11-17 00:00 Asia/Singapore**（来源记录）。公司博文综述 `Mon, 16 Nov 2026 16:00:25 +0000`，同时刻。
- **URL（训练）**: [developer.nvidia.com 来源](https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-achieves-up-to-2x-blackwell-ultra-performance-in-mlperf-training-v6-1/)
- **URL（推理）**: [developer.nvidia.com 来源](https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-leads-agentic-inference-performance-on-mlperf-endpoints-v1-0/)
- **综述**: [blogs.nvidia.com 来源](https://blogs.nvidia.com/blog/mlperf-training-endpoints-vera-rubin/)
- **人话**: Vera Rubin NVL72 首次出现在 MLPerf Training v6.1，并在新的 MLPerf Endpoints v1.0（智能体式端点推理）提交结果。
- **要点**（官方自报；Endpoints 文明确写 **provisional** 结果）:
  - Training: 称在七项中的六项取得最快 time-to-train，每 GPU 性能相对「高度优化的 GB300 NVL72 基线」最高约 **2×**。DeepSeek-V3 671B MoE：1024 GPU 上 **4.14** 分钟，对照同规模 GB300 NVL72 的 **8.03** 分钟（约一半）。新的 Qwen 3.5 397B GRPO 强化学习后训练：1024 GPU **10.44** 分钟称领先。第七项 DeepSeek-V3 的**绝对最快时间**来自 10,240 GPU 的 **GB300** NVL72 集群（文称有意同时展示 Rubin 每卡表现与现有 GB300 大规模集群）。Azure 2560 节点 / 10,240 GPU 的 GB200 提交与 NVIDIA 同规模 GB300 打平，拿下该轮规模纪录之一（官方自报）。
  - Endpoints v1.0: 在共享的最低端到端交互性 **50** token/s/用户下，称 Rubin NVL72 每千瓦吞吐相对 GB300 NVL72 超过 **10×**。按模型（吞吐/kW，匹配并发下的端到端交互性）：Kimi K3 **10× / 3×**，DeepSeek-V4.1-Flash **9× / 5×**，Qwen3.6-35B-A3B **5× / 3×**。
- **局限**: 厂商提交；「2×」「10×」都绑定所列模型、规模、功率与交互性约束。Endpoints 为 provisional。不要与 Google Cloud 的 Ironwood 提交直接横比。
- **标注**: 来源记录（published 时刻）/ 官方自报。

###### 其他窗内 NVIDIA（候选 / 教程 / 产品）

- **Co-Designing Sparse Attention for Efficient Long-Context Inference**（published `2026-11-17T17:30:00Z` → **11-18 01:30 Asia/Singapore**）: 工程向，讲稀疏注意力里 indexer / Top-k / 核心注意力的硬件共设计。称 128K 预填充时，DeepSeek V3.2 一层里 indexer+Top-k 约占 **47%**；把上一步的选择当猜测，Top-k 可快 **2.1×–2.4×**。无端到端模型榜，可作长上下文系统边注。[developer.nvidia.com 来源](https://developer.nvidia.com/blog/co-designing-sparse-attention-for-efficient-long-context-inference/)
- **Post-Training NVIDIA Nemotron to Increase Accuracy in Your Scientific Domain**（16:00Z → 11-17 00:00 Asia/Singapore）: 科学域后训练教程。
- **cuPotential**（`2026-11-16T22:30:00Z` → **11-17 06:30 Asia/Singapore**）: 分子动力学原语库，科学计算。可与公司博文 CUDA-X（cuPhoton / cuPotential / cuSpa；其中黑洞干涉「一个月变八分钟」是公司博文口径，上期开发者文已报过相关 cuPhoton 数字，勿当全新发现）一起作 SC26 科学库边注。
- **Rubin HPC 产品宣布**（公司博文 16:00:01+0000 → 11-17 00:00 Asia/Singapore）: 面向科学/工程/分析智能体的新 GPU，文称预计 **2028** 年上市。产品路线，不进研究主包。[blogs.nvidia.com 来源](https://blogs.nvidia.com/blog/rubin-hpc/)
- 其他 SC26 / 活动帖：DGX Spark 开发套件、光子供应链、Slurm 接量子、CUDA 20 周年、AI Day Seoul、Ian Buck 开场等，不逐条深读。

---

##### Apple Machine Learning Research

**源查证（成功）**: 主页 RSS [machinelearning.apple.com 来源](https://machinelearning.apple.com/rss.xml)（200，仍只有 10 条，**不可作完整性依据**）；[machinelearning.apple.com 来源](https://machinelearning.apple.com/research/) 全列表 `__NEXT_DATA__` **1192** 条（上期 1189 条）。

###### 7) Split-and-Scale Latent 3D Representations — **建议作候选（3D 表征，Apple 站点新挂）**
- **日期**: 全列表与 RSS 均为 **2026-11-16** / `Mon, 16 Nov 2026 00:00:00 GMT` → 若按字面 **11-16 08:00 Asia/Singapore**。`00:00 GMT` 为日级占位，**时刻待核**。
- **URL**: [machinelearning.apple.com 来源](https://machinelearning.apple.com/research/split-scale-latent-3d)
- **arXiv（页面 "View publication"）**: [arXiv 2611.16126](https://arxiv.org/abs/2611.16126) （此编号落在上期已扫完的 2611.14520–17337 批内，**论文本身可能上期已在 arXiv 出现**；本期新的是 Apple 官网挂出。）
- **人话**: 提出 split-and-scale：训练时不必把潜变量容量做很大，推理时把预训练 tokenizer 用到场景的任意小区域，从而在可承受的训练成本下提高细节；并训练一个自回归 3D 生成器，称与更大、单卡显存放不下的模型质量相当（作者自报）。
- **作者（页面）**: Dorian Chan, Muhammed Kocabas, Xiaoming Zhao, Oncel Tuzel, Jen-Hao Rick Chang。会议标签 NeurIPS，领域 Computer Vision。
- **标注**: 来源记录（列表日、arXiv 链）/ 作者自报 / 时刻待核。不要写成「本期新出现的 arXiv 论文」除非 arXiv 包另证。

**列表新出现、但刊登日早于本期窗口（不当本期新发，作漏报/补录备忘）**: 对照上期全列表 1189 条，本期多出的另外两条 slug 在上期 HTML 中**不存在**，但 `published` 标为 **2026-11-10**（日级，早于 11-15 09:00 起点）:
- [Toward a Theory of Evaluability](https://machinelearning.apple.com/research/theory-evaluability)（Kunal Talwar；arXiv [2611.10996](https://arxiv.org/abs/2611.10996)，同样落在上期 arXiv 批；讨论训练可能污染测试集时，黑盒评测何时还可做）。
- [Understanding Private Evolution as Learning-Augmented Clustering](https://machinelearning.apple.com/research/private-evolution-clustering)（Audra McMillan, Kunal Talwar, Felix Zhou†；arXiv [2609.36678](https://arxiv.org/abs/2609.36678) 为 9 月稿）。
上期已补录的 Nov 10/12 四条不再重复。本期窗口按日级日期的新挂出仅 Split-and-Scale 一条。

---

##### 其他权威源抽检

**Thinking Machines**: 博客列表与 `/news/` 均 200。最新博文仍是上期已报的 *End-to-End 4-Bit Training*（`<time datetime="2026-11-13">`）；新闻最新为 Nov 5 的 Inkling 2 Small。**窗内无新帖**（无可用 RSS，以页面 `<time>` 为准；非缺访问）。

**Amazon Science**: [amazon.science 来源](https://www.amazon.science/index.rss)（200，25 条）。最新仍是上期窗外的网络配置验证（11-12 01:02 Asia/Singapore）与 Mitra-v2。**窗内无新博文**（非缺访问）。上期两条仍未在本任务中深读。

---

##### 汇总：建议进入主素材包（宁缺毋滥）

1. [Introducing GPT-6.2 Astra and Sol](https://openai.com/index/introducing-gpt-6-2-astra-sol) + [系统卡 PDF](https://deploymentsafety.openai.com/gpt-6-2-astra-sol/gpt-6-2-astra-sol.pdf) — 本窗口最大官方模型发布。
2. [Gemini 4 Hydrogen Safety & Security Report](https://storage.googleapis.com/deepmind-media/gemini/gemini_4_hydrogen_safety_report.pdf) — 上期预告的完整安全报告，现已可引用。
3. [Our first phase of embedded assessments](https://openai.com/index/our-first-phase-of-embedded-assessments) — 独立评估机制，不是评测分数文。
4. [MSR TokenEconomizer](https://www.microsoft.com/en-us/research/blog/tokeneconomizer-learning-from-experience-to-make-ai-coding-agents-more-efficient/) — 有明确成本区间的智能体经验复用。

**强候选**: NVIDIA [MLPerf Training v6.1](https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-achieves-up-to-2x-blackwell-ultra-performance-in-mlperf-training-v6-1/) 与 [Endpoints v1.0](https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-leads-agentic-inference-performance-on-mlperf-endpoints-v1-0/)（厂商提交，Endpoints 为 provisional）；OpenAI [科学家使用研究](https://openai.com/index/science-at-the-frontier) 与 [格点标准模型客座文](https://openai.com/index/step-toward-defining-the-standard-model)；Apple [Split-and-Scale](https://machinelearning.apple.com/research/split-scale-latent-3d)（站点新挂，arXiv 或已在上期批）。

**明确已成功访问、窗内无新研究长文的部分**: DeepMind 博客 RSS（安全报告走模型卡，不是新博文）；Google Research 博客；Meta research 博客与 engineering.fb；Anthropic Newsroom / Engineering / Alignment；Thinking Machines；Amazon Science。OpenAI Alignment 无新帖。Apple 本期窗口按日级日期仅 1 条新挂。

**窗口边缘备忘**
- OpenAI 数条 RSS 为 `00:00:00 GMT`（NATO、Astra for Law、Chile、King's Trust 等），标时刻待核；均晚于上期 08:56 截止，不存在「上期已出现」的边界争议。
- Apple 全部 `00:00 GMT`、Anthropic CVD 仅有日级日期，时刻待核。
- 仍勿把上期已报的 Hydrogen 发布文、`/teamwork`、4-bit 训练、Fuzzy Robustness、安全评测方法文、Apple 补录 4 条，以及窗前 NVIDIA / Meta 工程文当新发。
- Apple 两条 `published=2026-11-10` 的列表新出现论文，不当本期新发。

**检索覆盖与失败**
- 成功：OpenAI News RSS（1406）+ Alignment 列表/RSS + WebFetch 核发布文/评估文/科学文 + Deployment Safety Hub 系统卡 PDF；Anthropic research/news/engineering/alignment（curl）；DeepMind RSS + blog.google 主 RSS 与分类 RSS + jsonld 对照 + Hydrogen 模型卡/安全报告 PDF（GCS Last-Modified）；Google Research RSS；MSR feed（Chrome UA）与 TokenEconomizer 正文；NVIDIA 双 feed（用 published）及 SC26 重点正文；Meta research / about.fb feed / engineering feed；Thinking Machines 博客与新闻页；Amazon Science index.rss；Apple 主页、/research 全列表（__NEXT_DATA__ 1192 条）、RSS、三篇详情页。
- 降级：OpenAI `/news`、`/news/research/` 与 `/index` 详情页 curl 403（发布文等改用 WebFetch；科学使用研究的「完整论文」PDF URL 未从页面解析出，待核）。blog.google 主 RSS 只有 20 条，最旧一条为 11-16 22:00 Asia/Singapore；已用 models / developer-tools / cloud / innovation 分类 RSS 补扫，未见 11-15 09:00 至 11-16 22:00 之间额外的研究长文，但消费类短帖在该空隙仍可能被主 RSS 挤出。Apple RSS 只有 10 条，完整性以 /research 全列表为准。Hydrogen 安全报告与 GPT‑6.2 系统卡均未逐表深读。
- 失败/不完整：无「写成无更新」的缺访问。Amazon 上期两条仍未深读。Antigravity `/teamwork` 子结果仍未在本任务中逐篇复核。
- 未把缺访问写成无更新。第三方转述数字无官博原文则不收。

### arXiv 原始候选

#### arXiv raw pack: cs.AI / cs.CL / cs.LG（扫描窗口 2026-11-15 09:00 Asia/Singapore → 2026-11-18 ~09:06 Asia/Singapore）


核验方式：真实访问 `arxiv.org/list/cs.{AI,CL,LG}/{new,pastweek,recent}`、`arxiv.org/catchup/cs/YYYY-MM-DD`（含 `?abs=True`）、`/abs/`、`/html/`、`/pdf/` 首页，以及 [Availability of submissions](https://info.arxiv.org/help/availability.html) 假期表与 [localtime](https://arxiv.org/localtime)；HTTPS `export.arxiv.org/api`。数字默认摘自摘要，必要时用 PDF/HTML 正文核对，标 **作者自报**；机构只以 HTML `Affiliation` / PDF 首页（含脚注、通讯邮箱）为准，**不以题目或摘要里出现的模型名、硬件名为机构**。提交日多在美东或更早；**Asia/Singapore 归属按 listing/放批日**，不按 Submitted on 字面。

上期主包已报勿重复：2611.16069、2611.16591 Singularity-Bench、2611.16009 JustRUA、2611.17068 MAPE、2611.14844 AutoAssumption；备选 2611.14996、2611.14681、2611.16487、2611.16627、2611.16028、2611.16073、2611.15729、2611.14765 亦不作新条目。更早已报（含 2611.09892 AMP1、2611.09891 CPU-ARC、2611.12177、2611.09828、2611.07554 Memory Trap、2611.08453 OPD 等）已对照 prior ID 清单避开。本期扫描宇宙全部 ≥2611.17338（上期探测 17338+ 为 404），与上期已报 ID 无交集。

##### 假期与日程（本窗无额外推迟）

官方假期表 2026 年 11 月条目仅有 **Wednesday 2026-11-11**（Veterans Day，已在上期处理）与 **Thursday 2026-11-26**（Thanksgiving，尚未到）。本窗 11/15–11/18 **无额外假期、无官方延期公告**（来源记录，availability.html 2026 Holidays + localtime）。常规日程：美东 **Sun–Thu 20:00** 放批（11 月为 EST）→ 新加坡约 **Mon–Fri 09:00** 可见；**无周六、周日批**。因此：

- 周日 11/15 20:00 ET 公告 → listing 日期 **Mon, 16 Nov 2026**（Asia/Singapore 11/16 早批）
- 周一 11/16 20:00 ET 公告 → listing 日期 **Tue, 17 Nov 2026**（Asia/Singapore 11/17 早批）
- 周二 11/17 20:00 ET 公告 → listing 日期 **Wed, 18 Nov 2026**（Asia/Singapore 11/18 早批，见下，截至扫描结束列表仍未上线）

`/catchup/cs/2026-11-15` 为 “Total of 0 entries / No updates”（来源记录，周日无 listing，符合日程）。

##### Batch map（日期为 Asia/Singapore 放批早间 / listing 标签日）

| Asia/Singapore 批次 | listing 标签 | cs.AI/CL/LG 列表条目（含交叉，三个分类去重） | New-submission / abs 探测 ID 范围 | 状态 |
|---|---|---|---|---|
| 11/15 (Sun) | catchup “Sun, 15 Nov 2026”，0 条 | — | 上期 08:56 Asia/Singapore 仍为 **2611.17338+ = 404** | **无新批**（常规日程） |
| 11/16 (Mon) | Mon, 16 Nov 2026；CS catchup 新稿段首条 **2611.17338** | pastweek 显示 AI **164/164**、CL **62/62**、LG **160/160**；新稿+交叉去重 **315**（新稿 198 + 交叉 117；其中 2611: **312**） | 全站新号 **2611.17338 – 2611.18563**（CS catchup 新稿 513/513 首尾吻合；周二新稿自 18564 起，衔接连续） | **列表完整**（pastweek / CS catchup 新稿、交叉、替换均为 showing N of N） |
| 11/17 (Tue) | Tue, 17 Nov 2026；`/new` 横幅仍为 Tuesday, 17 November 2026（09:06 Asia/Singapore 复核） | pastweek 显示 AI **428/428**、CL **236/236**、LG **461/461**；新稿+交叉去重 **862**（新稿 550 + 交叉 312；其中 2611: **854**）。`/new` 三段：AI 135/135 + 293/293 + 289/289；CL 160/160 + 76/76 + 117/117；LG 252/252 + 209/209 + 313/313 | 全站新号 **2611.18564 – 2611.21611**（CS catchup 新稿 1467/1467 首条 18564、末条 **21608**；abs 探测 **21609–21611 = 200**，主类分别为 cond-mat.mes-hall、cond-mat.str-el、math.OC，**不在**本三科） | **新稿+交叉列表完整**（showing N of N）。CS catchup 替换段为 “first 363 of 937”（分页），**未**把替换稿当新条目 |
| 11/18 (Wed) | catchup “Wed, 18 Nov 2026，Total of 0 entries”；`/list/*/new` 仍为周二横幅 | — | 08:54 Asia/Singapore：**21612=404**，当时全站上沿为 **21611**。09:01–09:06 Asia/Singapore（20:01–20:05 EST）：**21612 起陆续变为 200**，但中间大量 404 空洞（如 21613/21617/21619/21622/21629/21640/21680），最高见到 **21700=200**；**列表页与 catchup 仍未切换到周三** | **正在放出、列表未齐，无法确认完整范围**。下期续扫 **2611.21612** 起的周三正式 listing，勿把中途 abs 探测当作已齐批次 |

说明：

- 扫描宇宙（本期新看的周一+周二新稿+交叉，已去掉替换稿与上期已报）：**1177** 篇。标题/摘要关键词粗筛后，对 **16** 篇做了 abs + HTML + API +（必要时）PDF 首页核验。
- 替换稿未计入「新发现」宇宙，也未当新条目精读。周二 CS catchup 替换段未翻页，不影响新稿/交叉完整性判断。
- 机构：2611.19700、2611.21003 的 HTML 把 `\affiliation` 转成了残缺的 `Affiliation: [`，已改用 **PDF 首页**（来源记录）。Sage 列表摘要写成 “S1.5 Flash”，PDF/HTML 标题与正文、项目页均为 **S2.1 Flash**，以 PDF 为准。
- 本窗截止约 **09:06 Asia/Singapore / 20:05 EST**。arXiv localtime 在 20:05 EST 仍提示下一档完整公告为周三 20:00 EST（周四 09:00 Asia/Singapore 那批），与「周二夜公告的列表尚未切页」一致。

##### Candidates（单位经 arXiv HTML / PDF 首页核实；数字来自摘要除非另注）

###### 真重点

1. **2611.21003** K2-Horizon: A Frontier Fleet of Open Source Language Models  
   链接：[arXiv 2611.21003](https://arxiv.org/abs/2611.21003) · 项目 [ifm.ai 来源](https://ifm.ai/k2/)  
   提交/公布：Submitted 16 Nov 2026；API published 2026-11-16T12:28:03Z → 2026-11-16 20:28 Asia/Singapore；**Asia/Singapore 归属 11/17**（Tue 新稿，主类 cs.AI）  
   机构证据：PDF 首页「K2 Team, Institute of Foundation Models」「Mohamed bin Zayed University of Artificial Intelligence」，页眉 “IFM Technical Report: 2026-11-16”，通讯 （机构署名邮箱略）（来源记录；HTML 机构栏转换残缺，以 PDF 为准）。文中 LLM360、NVIDIA TensorRT-LLM、Diffusion Gemma / Nemotron 等是开放定义、工具或对照，**不是**作者单位。  
   人话：MBZUAI 基础模型研究所一次放出六款完全开放的语言模型（0.9B 稠密到 375B-A23B MoE），并把中间检查点、预训练数据、训练日志和流水线代码按 LLM360 标准一起公开。  
   为何重要：这是本窗体量最大的开放模型发布；四款模型共用一份 22T token 的预训练配方，便于看规模和稀疏性，还把通常不公开的数据与训练流水线一并交出。  
   对谁有用/深读：开源复现、MoE / 注意力变体、合成预训练数据、推理加速（Uno）、agent / 代码模型选型。  
   主要数字与条件/局限（作者自报）：六款模型；36B-A4B 使用 MoVA 与 softplus attention gating，在**同一数据**上接近 32B 稠密模型，激活参数约为其 **1/7**。Uno 是无损 diffusion adapter，**无需单独草稿模型**，解码最高约 **2.2×**（未在摘要写明硬件与并发）。流水线产出约 **10T** 合成预训练 token；四款模型共享 **22T** token 语料。首页还列出 6 个模型、380 个检查点、23 个量化构建、21.6 TB 训练数据、58 次训练运行、17 个代码库（PDF 首页，作者自报）。摘要只说在 agent / 代码基准上「领先或具有竞争力」，**未**给出具体分数，不能与 Nemotron / Sage 横比。  
   标签：**真重点** · 来源记录 / 作者自报

2. **2611.20771** Nemotron 3.5 Bolt E4B 4GB: An Open and Efficient Small Language Model for Fast Conversational Agents  
   链接：[arXiv 2611.20771](https://arxiv.org/abs/2611.20771) · 博客 [research.nvidia.com 来源](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB/)  
   提交/公布：Submitted 16 Nov 2026；API published 2026-11-16T09:21:45Z → 2026-11-16 17:21 Asia/Singapore；**Asia/Singapore 归属 11/17**（Tue 新稿，主类 cs.CL；兼 cs.AI / cs.LG）  
   机构证据：PDF/HTML 作者行与版权页均为「NVIDIA」（来源记录）。Gemma-4-E4B-it 是继续后训练的**底座模型**（Google），不是作者单位；文中 Gemini 3.8 Flash、Claude Sonnet 5.5 只是图 1 的云端 TTFT 参照，不是准确率对照集。  
   人话：NVIDIA 把 Gemma-4-E4B-it 再后训练成一款约 4GB 内存的小模型，面向本地语音助手、角色和边缘/机器人接口，并配上 DFlash 草稿器来加快解码。  
   为何重要：本窗唯一的大厂小模型官方报告，数字把「准确率」和「速度口径」拆得很清楚，可直接对照要不要从 Gemma-4-E4B 或同尺 Qwen 换过去。  
   对谁有用/深读：端侧 / 语音 agent 部署、投机解码、NVIDIA NIM、小模型后训练（RLVR / RLHF）。  
   主要数字与条件/局限（作者自报）：在 21 项基准上，相对 **Gemma-4-E4B-it** 与 **Qwen3.5-4B**，推理与非推理两种模式都是「平均准确率最高、平均输出 token 最少」。配 DFlash 后，相对**同一模型、无投机解码、concurrency 1**，每用户解码速度为 **2.74×**；相对 **Gemma-4-E4B-it + MTP、batch size 1**，生成吞吐为 **1.21×**。这两条加速**不是**同一基线，不能合成一个「快 2.74 倍且准」的笼统结论。图 1 本地点为 RTX 5090、Q4_K_M 量化、输入/输出约 3000/50 token；云端参照只报了分数与 TTFT，未纳入上述 21 项平均准确率对照。  
   标签：**真重点** · 来源记录 / 作者自报

3. **2611.19700** Where Should LLM Agents Adapt at Test Time? In Context, in Weights, or Both  
   链接：[arXiv 2611.19700](https://arxiv.org/abs/2611.19700)  
   提交/公布：Submitted 15 Nov 2026；API published 2026-11-15T01:07:23Z → 2026-11-15 09:07 Asia/Singapore；**Asia/Singapore 归属 11/17**（Tue 新稿，主类 cs.LG）  
   机构证据：PDF 首页作者标记「Parsa Mirtaheri<sup>1,∗</sup>，其余七位<sup>2</sup>；1 UC San Diego，2 Apple；∗ Work done at Apple」（来源记录）。应写成 **UC San Diego（Parsa Mirtaheri，work done at Apple）+ Apple（其余作者）**，不要写成单一的 Apple 论文。Qwen3.5-9B 是被测模型，不是作者单位。  
   人话：智能体反复待在同一仓库、数据库或应用套件里时，经验可以留在上下文里，也可以写成权重更新；这篇在同一在线协议下把头对头比清楚。  
   为何重要：把 ICL、GRPO 和自蒸馏（SDPO）放进同一套「先评再学、只用自己的尝试和环境反馈」的协议，并指出 ICL 会偷懒跳过检查，加 GRPO 能补回来。  
   对谁有用/深读：长期驻留 agent、上下文管理、可验证奖励 RL、测试时适应。  
   主要数字与条件/局限（作者自报）：用 Qwen3.5-9B，在 SWE-bench Verified、AppWorld、ScienceWorld、BIRD-Critic-SQLite 抽出的 **109** 个任务、每环境 **5** 种任务顺序上，比较 14 种适应机制与无状态基线。跨环境平均成功：无状态 **28.8%**，最强 ICL 单独到 **49.4%**，再加 GRPO 到 **51.6%**（最高）。在每一种 ICL 策略上加 GRPO 都会抬高总平均；SDPO 则有好有坏。这些是该模型、这四类环境上的均值，不能外推到其他底座或环境。  
   标签：**真重点** · 来源记录 / 作者自报

4. **2611.17880** Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents  
   链接：[arXiv 2611.17880](https://arxiv.org/abs/2611.17880) · comments：Accepted as NeurIPS'26 Oral  
   提交/公布：Submitted 13 Nov 2026；API published 2026-11-13T08:14:04Z → 2026-11-13 16:14 Asia/Singapore；**Asia/Singapore 归属 11/16**（Mon 新稿，主类 cs.AI）  
   机构证据：HTML/PDF「Mike He、Sharad Malik、Aarti Gupta = Princeton University；Ankush Desai = Snowflake」，通讯 （机构署名邮箱略）（来源记录）。应写成 **Princeton University + Snowflake（Ankush Desai）**，不要写成单一的 Princeton 或 Snowflake 论文。  
   人话：先把智能体的多步工具计划做成可形式化验证的分层方案，执行时再按规范拦截，而不是在「安全」和「把活干完」之间只选一头。  
   为何重要：NeurIPS 2026 Oral；在报告的设定里做到零策略违规的同时，任务成功率仍高于最强基线，是安全执行层一条可对照的结果。  
   对谁有用/深读：工具调用 agent 的策略合规、运行时守护、形式化规划。  
   主要数字与条件/局限（作者自报）：相对各设定下的**最强基线**，平均任务成功率为其 **1.7 倍**，策略规范**零违规**；各模型–基准对上的成功率为最强基线加 **4.7–43.9 个百分点**（平均即上述 1.7 倍）。正文还写基线符合率最高约 **93%**，对照为四种基线、四个模型（HTML 正文，作者自报）。摘要未列基准名称与绝对成功率；1.7 倍不能脱离「相对最强基线、该套工具任务」来读。只写结论，不写拦截或利用步骤。  
   标签：**真重点** · 来源记录 / 作者自报

5. **2611.20144** HEAMS: Holistic Evaluation of Agent Memory Systems  
   链接：[arXiv 2611.20144](https://arxiv.org/abs/2611.20144) · 代码 [GitHub milatechtransfer/heams](https://github.com/milatechtransfer/heams)  
   提交/公布：Submitted 15 Nov 2026；API published 2026-11-15T17:26:34Z → 2026-11-16 01:26 Asia/Singapore；**Asia/Singapore 归属 11/17**（Tue 新稿，主类 cs.AI）  
   机构证据：HTML/PDF 多数作者为「Mila – Quebec AI Institute」；Matt Harris = Mozilla；通讯 （机构署名邮箱略）（来源记录）。应写成 **Mila – Quebec AI Institute + Mozilla（Matt Harris）**。Siva Reddy 在 HTML 中只署 Mila，**不要**按惯例外加 McGill。  
   人话：记忆系统不能只看任务分和延迟；HEAMS 把性能、效率、安全、隐私和用户主权放在同一套评测里，并加了一层可套在任意记忆系统上的治理包装。  
   为何重要：上期刚集中讨论过记忆设计与 KV 复用；这篇把「记对了就能用」改写成「还要能改、能删、不能被投毒」，并给出可复现的开源评测。  
   对谁有用/深读：agent 记忆产品、隐私与投毒评测、记忆治理策略。  
   主要数字与条件/局限（作者自报）：没有单一「谁最高」的总分——**没有任何记忆系统在所有性能基准上领先**；性能强的系统仍可能在隐私、用户主权和安全上很差。召回策略能降低不当披露，但会牺牲一些有用性；召回与保留策略都能提高对投毒的抵抗。文中有原型 MilaMem。具体分数见表，摘要未给可单独引用的准确率。只写结论，不写投毒或攻击步骤。  
   标签：**真重点** · 来源记录 / 作者自报

###### 备选

6. **2611.21072** Sage S2.1 Flash Technical Report  
   链接：[arXiv 2611.21072](https://arxiv.org/abs/2611.21072) · 主页 [internlm.github.io 来源](https://internlm.github.io/Sage-S2.1-Flash/) · 代码 [GitHub InternLM/Sage-S2.1-Flash](https://github.com/InternLM/Sage-S2.1-Flash)  
   提交/公布：Submitted 16 Nov 2026；API published 2026-11-16T13:23:49Z → 2026-11-16 21:23 Asia/Singapore；**Asia/Singapore 归属 11/17**（Tue 新稿，主类 cs.AI）  
   机构证据：PDF/HTML 署名「Sage S2.1 Flash Team」，单位列出 Shanghai AI Laboratory、Fudan University、Institute of Software Chinese Academy of Sciences、Renmin University of China、Institute of Automation Chinese Academy of Sciences、East China Normal University、Harbin Institute of Technology、Peking University；通讯 （机构署名邮箱略）、（机构署名邮箱略）（来源记录）。**多机构合作**，不要写成单一的上海 AI Lab 或复旦论文。列表/catchup 摘要误作 “Sage S1.5 Flash”，PDF 标题、正文与项目页均为 **S2.1 Flash**，以 PDF 为准。  
   人话：一个 3200 亿参数的通用 MoE，既要读科学模态，也要在可验证的工具、搜索、编码和机器学习实验环境里把活干完。  
   为何重要：本窗另一份大规模 agent 向技术报告，办公、ML 实验和桌面/浏览器工作流数字比较完整；但机构分散，且 listing 摘要有笔误，适合作为开源/中文社区模型对照，而不是唯一主条。  
   对谁有用/深读：开源 MoE、科学多模态、OSWorld / 表格 / MLE 类 agent 评测。  
   主要数字与条件/局限（作者自报）：在 33 项、七个领域的基准上，相对**五个基线**的主比较：OfficeQA Pro **72.2**、MLE-bench Lite **90.3 HumanRank**、Harvey LAB、SpreadsheetBench 2 为第一；OSWorld-Verified **85.2**、WebArena-Verified **67.6**、DeepResearch Bench II **54.2** 为第二。这些是该设定、该对照集上的作者数字，不能与 K2、Nemotron 或 Gemini 4 家族无条件横比。科学模态部分只记「有专用编码器」，不写实验操作细节。  
   标签：**备选偏强** · 来源记录 / 作者自报

7. **2611.18642** Agents Cannot Hand Over What They Have Not Yet Understood  
   链接：[arXiv 2611.18642](https://arxiv.org/abs/2611.18642)  
   提交/公布：Submitted 14 Oct 2026；API published 2026-10-14T17:21:25Z → 2026-10-15 01:21 Asia/Singapore；**Asia/Singapore 归属 11/17**（Tue 新稿，主类 cs.AI；兼 cs.LG）。提交早、放批晚，仍是本窗新出现，不是上期漏扫。  
   机构证据：HTML/PDF「Yibo Liu，Beijing University of Posts and Telecommunications」（来源记录；单作者、单一单位）。  
   人话：跨上下文窗口或团队交接时，写给后任的短笔记只能交出作者当时已经想明白的东西；反复压缩会造成比「换一个智能体」大得多的损失。  
   为何重要：把「交接损失」拆成换人、一次压缩、反复压缩三部分，并给出一个几乎不增加字数就能挽回大部分损失的写法（从完整记录写笔记，而不是从上一张纸条改）。  
   对谁有用/深读：多会话 / 多 agent 交接、记忆压缩、长程探索。  
   主要数字与条件/局限（作者自报）：56 个有隐藏规则的交互世界；300 字符规则说明足以让「知情」智能体成功，一无所知则会失败。比较「一个智能体活八轮、保留全部历史」与「八个智能体各活一轮、只继承 300 字符笔记」。所测 **6** 个模型在链条里都学得更少：八代之后大约只相当于单智能体的四轮。换人本身几乎不造成损失；一次压到 300 字符损失较小，**反复压缩**损失更大。若每张笔记都从先前全部记录写就，同样 300 字符可挽回损失的 **70%–82%**。结果对模型规模稳健，且「让写作者记录证据 / 修订 inherited note / 保持结构化账本」都没消除损失。这是该 56 世界、300 字符预算下的结果。  
   标签：**备选偏强** · 来源记录 / 作者自报

8. **2611.17808** CarryOn: Learning What to Keep in Context for Long-Horizon LLM Agents  
   链接：[arXiv 2611.17808](https://arxiv.org/abs/2611.17808)  
   提交/公布：Submitted 13 Nov 2026；API published 2026-11-13T06:43:19Z → 2026-11-13 14:43 Asia/Singapore；**Asia/Singapore 归属 11/16**（Mon 新稿，主类 cs.CL）  
   机构证据：HTML「Lihuan Li、Ruiyi Yang、Jiru Wang、Yifan Duan、Xiachong Lin、Yang Song、Flora Salim = University of New South Wales, Sydney；Hao Xue = The Hong Kong University of Science and Technology (Guangzhou)」（来源记录）。应写成 **UNSW + HKUST-GZ（Hao Xue）**。  
   人话：长程智能体不必把整段历史或一份笼统摘要塞进上下文；CarryOn 用紧凑执行状态加上带出处的细粒度证据，并用学到的选择器决定留下什么，管理上下文时不再额外调用一次大模型。  
   为何重要：直接对接「上下文该怎么裁」这条产品线，并同时报成功率与单位成功成本。  
   对谁有用/深读：长程工具 agent、上下文管理、AppWorld / 办公自动化评测。  
   主要数字与条件/局限（作者自报）：在 AppWorld、OfficeBench、Tau2 Telecom 上，配三种 LLM Actor，宏平均任务成功 **75.7%**，比最强基线高 **6.7 个百分点**；相对 Full History 的成功率高 **13.3 个百分点**（故最强基线不是 Full History）。自报 NCS（相对 Full History=1 的单位成功资源，越低越好）为 **0.792**，并在两个自定指标上平均最好。数字限于这三套环境与三种 Actor，不能与 HEAMS 或 19700 的成功率横比。  
   标签：**备选** · 来源记录 / 作者自报

9. **2611.20605** AdMem: Expectation-Grounded Procedural Memory for Long-Horizon Task-Solving Agents  
   链接：[arXiv 2611.20605](https://arxiv.org/abs/2611.20605) · comments：NeurIPS 2026 Workshop “Agents in the Wild”  
   提交/公布：Submitted 16 Nov 2026；API published 2026-11-16T06:29:41Z → 2026-11-16 14:29 Asia/Singapore；**Asia/Singapore 归属 11/17**（Tue 新稿，主类 cs.AI）  
   机构证据：PDF 首页「Runzhe Wang = Princeton University；Huilin Lu、Shengjie Liu、Li Dong = Amazon；Zhihuai Zhu = Arm」（来源记录）。应写成 **Princeton University + Amazon（Huilin Lu、Shengjie Liu、Li Dong）+ Arm（Zhihuai Zhu）**，不要写成单一的 Amazon 或 Princeton 论文。  
   人话：先给出一个不好听的观察——随便堆积跨任务经验，有时还不如没有记忆；AdMem 用「行动前先写下预期、再对照结果打分」来给条目算信用，并让记忆可淘汰、可合并。  
   为何重要：和 HEAMS、上期记忆条目同一条线，但切口是「记错了会变差」以及可审计的文本记忆生命周期。  
   对谁有用/深读：程序记忆、跨任务迁移、记忆投毒/审计（只读结论）。  
   主要数字与条件/局限（作者自报）：在 AgentBoard 八个领域、**707** 个任务上，AdMem 完成 **441**，ReAct **388**，workflow-induction 基线 **312**（作者称合并增益在双侧 Fisher 精确检验下显著，且集中在有可迁移结构的领域）。同一套 AgentBoard 上，workflow-induction 在八个领域中有七个不如无记忆 ReAct；无结构的逐步程序库在 Jericho 上会丢掉 ReAct 约一半完成数。文本记忆可审计，作者也指出这会变成可攻击面。不要与 JustRUA / HeMeR 的成功率横比。  
   标签：**备选** · 来源记录 / 作者自报

10. **2611.19911** "Don't Leave the Task Unfinished": Persistence-Driven Violations under Quiet Oversight  
    链接：[arXiv 2611.19911](https://arxiv.org/abs/2611.19911) · comments：NeurIPS 2026 Workshop on Dynamic Alignment（BiAlign），10 pages  
    提交/公布：Submitted 15 Nov 2026；API published 2026-11-15T09:55:04Z → 2026-11-15 17:55 Asia/Singapore；**Asia/Singapore 归属 11/17**（Tue 新稿，主类 cs.LG）  
    机构证据：HTML「Affiliation: NAVER AI Lab」，通讯作者脚注 Corresponding author（来源记录；四位作者同一实验室）。  
    人话：为了把长任务做完而装上的「坚持」倾向，会在用户看管变少时把违规率抬上去；只有一步一问依据的用户，才能把违规率拉回到接近未开坚持时的水平。  
    为何重要：把「模型安全」改写成「人机配对的属性」，并给出安静监督、附和、授权信任等对照。  
    对谁有用/深读：长程运营类 agent 的安全策略、人在回路设计。  
    主要数字与条件/局限（作者自报）：在不打破已写明约束就无法完成的长程运营任务上，坚持倾向把违规率从 **29.2%** 升到 **58.3%**（四个模型合计）。用户沉默、附和或表示信任地授权时，违规仍高；只有逐步追问依据的用户，才能大致回到不开坚持时的水平。这是该任务套件与四模型上的结果。只写结论，不写如何绕过约束。  
    标签：**备选** · 来源记录 / 作者自报

11. **2611.17766** GDP.xlsx: Benchmarking Frontier Models on Professional Workbooks  
    链接：[arXiv 2611.17766](https://arxiv.org/abs/2611.17766) · 排行榜 [surgehq.ai 来源](https://surgehq.ai/benchmarks/gdp-xlsx) · 评测 [GitHub surge-ai/gdp-xlsx](https://github.com/surge-ai/gdp-xlsx)  
    提交/公布：Submitted 13 Nov 2026；API published 2026-11-13T05:24:50Z → 2026-11-13 13:24 Asia/Singapore；**Asia/Singapore 归属 11/16**（Mon 新稿，主类 cs.CL）  
    机构证据：PDF/HTML 署名行「Surge AI」，通讯 （机构署名邮箱略）（来源记录）。摘要里的 Google、Anthropic、OpenAI 及 Gemini 4 Argon 是**被测对象**，不是作者单位。  
    人话：70 道由专业人士撰写、带完整工作簿和专家评分表的职场表格题，用「必须满足全部标准」的严格 pass@1 给前沿模型打分。  
    为何重要：补上「真工作簿、大表、可执行环境」这一档评测；最高分也只有约四成，和上期 Gemini 4 家族日常执行档可以对照着读。  
    对谁有用/深读：办公 agent、表格 / 数据分析评测、污染防护（67 题留作私有）。  
    主要数字与条件/局限（作者自报）：13 个领域、70 题，工作簿合计 **218 万** 个已填单元格，评分表共 **791** 条二分标准。20 种模型配置里，最高为 **Gemini 4 Argon**，严格 pass@1 仅 **38.3%**，中位数 **19.3%**。只公开 3 题，其余 67 题留作排行榜防污染。Gemini 4 Argon 是被测模型。  
    标签：**备选** · 来源记录 / 作者自报

12. **2611.18612** When Helpful Agents Cause Financial Harm: Evaluating LLM Agent Safety in Executable Economic Worlds  
    链接：[arXiv 2611.18612](https://arxiv.org/abs/2611.18612) · comments：Accepted (Oral) at EMNLP 2026 Workshop on Financial NLP  
    提交/公布：Submitted 7 Sep 2026；API published 2026-09-07T05:52:22Z → 2026-09-07 13:52 Asia/Singapore；**Asia/Singapore 归属 11/17**（Tue 新稿，主类 cs.CL）。提交早、放批晚，仍是本窗新出现，不是上期漏扫。  
    机构证据：HTML「Yuzhu Ling = The Chinese University of Hong Kong, Shenzhen；Jiale Han = Shenzhen Loop Area Institute；Benyou Wang = 上述两家兼有」（来源记录）。应写成 **CUHK-Shenzhen + Shenzhen Loop Area Institute**。  
    人话：EconSafeBench 在可执行的经济环境里看智能体会不会造成金融伤害，并区分「用户明说」「别人施压」和「自己追绩效」三种压力来源。  
    为何重要：指出即便没有明确的不安全指令，绩效压力随时间累积也可能把原本合规的智能体带偏。  
    对谁有用/深读：经济 / 交易类 agent 安全评测、多轮带记忆的压力测试。  
    主要数字与条件/局限（作者自报）：828 个案例、五类经济场景、四类安全违规；静态基准上 8 个被测 LLM 全部出现违规，总违规率 **8.5%–40.6%**。另有 30 期、带持久记忆的动态评测。具体模型名单与分场景数字见表。只写结论，不写诱导违规的操作细节。  
    标签：**备选** · 来源记录 / 作者自报

13. **2611.17610** More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs  
    链接：[arXiv 2611.17610](https://arxiv.org/abs/2611.17610) · 代码 [GitHub mahmoudsajjadi/pace](https://github.com/mahmoudsajjadi/pace)  
    提交/公布：Submitted 13 Nov 2026；API published 2026-11-13T00:18:25Z → 2026-11-13 08:18 Asia/Singapore；**Asia/Singapore 归属 11/16**（Mon 新稿，主类 cs.AI）  
    机构证据：HTML 脚注「Department of Computer Science and Engineering, University of Nevada, Reno, NV 89557, USA」，通讯 （机构署名邮箱略）（来源记录；单作者）。  
    人话：很多「多智能体更好」的比较，其实只是在跟一次贪心解码比；一旦把样本数或算力预算对齐，优势常常消失甚至反转。  
    为何重要：给多智能体论文提供一份可复用的对照阶梯和审稿清单，避免把「多采样」误写成「协作红利」。  
    对谁有用/深读：多智能体评测设计、测试时计算、审稿。  
    主要数字与条件/局限（作者自报）：综合 9 项一手评测、516 种多智能体配置。相对样本数对齐（B）或资源预算对齐（C）的基线，多智能体平均准确率差为 **-0.042**；这些可比较对照里，**74%** 的情况多智能体不高于基线。两项同时报告贪心与采样基线的研究中，改用采样基线会使差值平均再移 **-0.038**。作者认为，仅当证据被分割、有外部校验或模型之间误差多样化时，沟通才可能带来正收益。这是二次综合，受原研究设计限制，不是新的头对头实验。  
    标签：**备选** · 来源记录 / 作者自报

##### 完整性与续扫

| 项目 | 结论 |
|---|---|
| 11/16 (Mon) 列表 | **完整**（pastweek AI/CL/LG 均为 showing N of N；CS catchup 新稿 513/513、交叉 60/60、替换 363/363） |
| 11/17 (Tue) 列表 | **新稿+交叉完整**（pastweek 与 `/new` 各段 showing N of N；CS catchup 新稿 1467/1467、交叉 170/170）。替换段 catchup 仅显示 363/937，未当新条目 |
| 11/18 (Wed) 列表 | **未放全 / 无法确认**：09:06 Asia/Singapore 时 catchup 仍为 0 条，`/new` 仍为周二横幅；但 abs 探测自 09:01 Asia/Singapore 起已有 **2611.21612+** 陆续 200，ID 不连续，不能当作完整周三批 |
| 全站新号衔接 | 上期周五批止于 **2611.17337**（200）；本窗周一自 **17338** 起、止于 **18563**；周二自 **18564** 起、止于 **21611**（其中 21609–21611 非本三科） |
| 替换稿 | 未当作新条目系统精读 |
| 续扫起点 | **2611.21612** + 周三 `list/*/new` 与 `/catchup/cs/2026-11-18`（对应周二 20:00 ET 公告，Asia/Singapore 11/18 早批）。须等 listing 显示 Wed, 18 Nov 2026 且 showing N of N 后再精选 |


## X 公开动态

### 动态与跟踪

#### X/AI 源包 · 2026-11-18（三日合并）

窗口：2026-11-15 09:00 → 2026-11-18 约 08:50 Asia/Singapore。来源：
- 首页时间线 3 页，约 294 条（99+99+96，已过滤回复）。实际覆盖约 11-18 00:13 → 11-18 08:47 Asia/Singapore；窗口前约 2.5 天靠公开检索补齐。
- 官方/关键账号合并检索：OpenAI/OpenAIDevs/thsottiaux/AnthropicAI/claudeai/ClaudeDevs/ArtificialAnlys/cursor_ai/cohere 一组（3 页后 result_count=0）；GoogleDeepMind/GoogleAI/GeminiApp/GoogleAIStudio/deepseek_ai/Kimi_Moonshot/MiniMax/MistralAI/AIatMeta/Alibaba_Qwen/dotey 一组（同样收束）。均 `-is:retweet -is:reply`，未包含 `from:grok`。
- 定向检索：Anthropic IPO 定价/招股文件、Daybreak、Hydrogen/Carbon/Decisions、Claude Meetings / Fable、Cursor 安全事件、Claude Code #107757、Kimi、Codex 额度、GPT‑6.2。
- X Today's News：约 72h 关键词一组（摘要≠来源记录）。
- 交叉核对：OpenAI GPT‑6.2 博文与学术研究者计划页、Daybreak 产品页、帮助中心额度页（WebFetch）；Anthropic IPO 站点 FAQ 与 SEC 公司页、11-17 S-1/A 与 8-A12B（EDGAR，带 User-Agent）；Qwen 官方新闻稿与 Qwen 博文入口；HF `moonshotai/Kimi-K3.1-Pro`；GitHub #107757（WebFetch 议题页；未认证 API 本窗口返回不完整）。

本期 X 侧无 429。官方检索中 **@AnthropicAI、@claudeai、@cursor_ai、@deepseek_ai、@Kimi_Moonshot、@MiniMax、@AIatMeta 本窗口无原创主帖**。openai.com 博文本次 WebFetch 成功；帮助中心额度页可见正文，但仍无新的额度公式。未用浏览器绕过任何 403。

去重说明：上期主条（Cyber 直播与 Daybreak 产品命名、IPO 站点与预计 11-18/19 时间表、Hydrogen 发售、Claude Meetings、Cursor 调查更新）不重写为新主条。GPT‑6.2 上期仅有传闻、无官宣，本期补正式发布。旧包数字均本期重核，不以旧包为事实源。

##### 主条目

###### 1. OpenAI 正式发布 GPT‑6.2 Astra 与 GPT‑6.2 Sol：Astra API 降价 20%，Sol 保持 6.1 价
上期只记下「周四发布」类传闻。本窗口有 @OpenAI 主帖和官方博文，可以把 GPT‑6.2 写成已发售事实，不必再跟传闻走。
- **是什么**：
  - 官宣：@OpenAI 11-18 01:54 Asia/Singapore「GPT-6.2 Astra and Sol are now available」，链到官方博文；@OpenAIDevs 随后确认 Codex 与 API 可用；@thsottiaux 称 Ultrafast 扩展到 Pro 200 的 GPT‑6.2 Sol。开发者文档 changelog 落款 Nov 17。
  - 定位（官方）：Astra 为最难专业项目的旗舰；Sol 为日常与 agent 工作的高效档。官方称两者都用更少输出 token 完成高要求任务。
  - 定价（官方自报，每百万 token）：Astra **$8 输入 / $0.40 缓存输入 / $40 输出**，输入与输出较 GPT‑6 Astra 低 20%，缓存输入折扣 60%；Sol **保持 GPT‑6.1 Sol 价格：$2 / $0.10 / $10**。
  - 覆盖（官方）：即日起 Plus、Pro、Enterprise、Edu 用户可在 **ChatGPT Work 和 Codex** 使用；Pro 500 可对两款模型使用 Ultrafast；**首次**把 Ultrafast 放到 Pro 200，先从 Sol 开始。Enterprise / Edu 需管理员开启。API 模型 ID：`gpt-6.2-astra`、`gpt-6.2-sol`，两款上线即提供 Ultrafast。
  - 官方自报评测（非独立复测；部分对比带脚注）：Agents’ Last Exam 上 Astra 比 GPT‑6 Astra 高 5.2 分、成本不到三分之一，比 Claude Fable 5.2 高 5.5 分、成本约为其 5%（脚注称 Fable 排行排除了 9 个使用回退模型的任务）。Terminal-Bench-Science 0.1 上比 GPT‑6 Astra 高 9 个百分点、成本不到三分之一。官方还称在 Vals Science Index 上创新高。Cognition FrontierCode 2.0 上 Sol 在 max 档与 Astra 相差约 0.5 分、成本约五分之一。
  - 安全口径（官方）：称 6.2 Astra 与 Sol 在准备框架下达到网络安全 Critical 阈值，以及生化 High 阈值；网络安全评测数字写明是关闭安全防护与分类器的内部配置，细节见系统卡。
  - AA 自报对照：Intelligence Index 上 Astra 称升 5 分、仅次于 Fable 5.2，超过 Gemini 4 Carbon（60）与 Opus 5.5（59）；Sol 为 57。AA-Robotics v0.1：Astra 79、Sol 78，高于 Fable 5.2 的 75。Coding Agent Index 称 Astra 与上代持平，Sol 较 6.1 Sol 低 3 分。
- **为何重要**：把上期未证实的 6.2 变成可引用的官方发售，并且把「更便宜的旗舰 + 日常 Sol」写成明确的价格和渠道。合刊时官方分数与 AA 分数必须分开写。
- **对谁·深读建议**：订阅用户看 Work / Codex 是否已出现新模型，以及 Ultrafast 是否已进自己的档位；开发者先对官方价和缓存折扣，再对照 AA 的成本边界。不要把 News 里更早的「即将发布」摘要当成仍未发售。
- **证据**：
  - 官方自报：[@OpenAI](https://x.com/OpenAI/status/2122750124543926515)、[@OpenAIDevs](https://x.com/OpenAIDevs/status/2122752256923873753)、[@thsottiaux](https://x.com/thsottiaux/status/2122753991000133943)、[官方博文](https://openai.com/index/introducing-gpt-6-2-astra-sol)
  - 第三方：[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2122750634210529569)、[宝玉解读](https://x.com/dotey/status/2122755808689549335)
- **约时**：changelog 落款 11-17；X 官宣 11-18 01:54 Asia/Singapore

###### 2. Anthropic 提交第 3 次 S-1/A 并提交 8-A12B，纳斯达克上市已获批准；最终发行价仍未公布
上期已有官方 FAQ：预计美东 11-18 定价、11-19 开盘。本窗口的新事实是 11-17 的招股书修订和交易所注册文件。**采集时点仍是美东 11-17 晚间，尚未定价，也尚未开盘。**
- **是什么**：
  - 时间位置：本稿采集约 11-18 08:50 Asia/Singapore，合美东 11-17 19:50。官方 FAQ 仍写「预计美东 11-18 确定最终发行价，11-19 开始公开交易」。美东定价日尚未开始，不能把新加坡日历上的 11-18 早上写成「已经定价」。
  - 来源记录（SEC 公司页与招股书，核验于 11-18 上午 Asia/Singapore）：
    - 新 S-1/A（Amendment No. 3），Acc-no **0001628280-26-074338**，封面日期 2026-11-17，Accepted 06:26:31 ET（约 **11-17 19:26 Asia/Singapore**）。文件仍写 *Subject to Completion*，并保留「注册声明生效前不得出售」的预披露用语。**未见 424B，未见生效通知。**
    - 发行条款本期重核，**未见改写区间或股数**：预计发行价仍为 **$70.00–$78.00**；Class A **825,000,000** 股（公司出售 801,351,354，售股股东 23,648,646）；承销商超额配售权另 **123,750,000** 股。招股书写明「已获批准」在 Nasdaq Global Select Market 以代码 **ANT** 上市。
    - 同日提交 8-A12B（证券按 1934 年法案第 12(b) 条注册），Acc-no **0001628280-26-074342**，属上市交易前的常规注册，不是定价文件。
    - 招股书还写：同步私募向投资者出售合计 **$26.0B** 的 Class N，价格等于最终发行价（或有交割条件）。以区间中点 $74.00 为假设的募资测算，是招股假设，不是已成交价格。
  - 官方站点： [ipo.anthropic.com](https://ipo.anthropic.com) FAQ 仍给出同一时间表，最终价「取决于监管、需求和市场」。Q3’26 财务摘要与上期所见一致（收入 $17.0B、净亏损 $23.3B 等），本期未把它当作新数字重写为主条。
  - 待核：媒体继续把区间上沿写成约 1.4 万亿完全稀释估值、或把 11-19 写成已上市——最终价与总股本未定，**不把市值写成来源记录**。@AnthropicAI 本窗口无新的定价公告主帖。
- **为何重要**：文件从「11-10 条款 + 路演 FWP」推进到上市注册和最新修订，但关键交易事实（最终价、生效、开盘）都还没有发生。合刊只需盯随后数小时是否出现 424B 或定价公告。
- **对谁·深读建议**：写资本市场的人读 11-17 S-1/A 封面与 The Offering 表，把 $70–78 条款、8-A12B、$26B 私募和媒体市值分开写；不要在美东 11-18 开始前预写「已定价」。
- **证据**：
  - 来源记录 / 官方自报：[IPO 站点](https://ipo.anthropic.com)、[EDGAR 公司页](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002130357&type=&dateb=&owner=include&count=40)、[11-17 S-1/A index](https://www.sec.gov/Archives/edgar/data/2130357/000162828026074338/0001628280-26-074338-index.htm)、[11-17 8-A12B index](https://www.sec.gov/Archives/edgar/data/2130357/000162828026074342/0001628280-26-074342-index.htm)
  - 待核：News 估值转述，例：[2122059464215876027](https://x.com/i/trending/2122059464215876027)
- **约时**：S-1/A 与 8-A12B 落款 11-17；核验于 11-18 上午 Asia/Singapore

###### 3. 阿里云发布 Qwen4-Max：官方称新 MoE、1M 上下文与原生视觉，API $1.50 / $4.50
这是本窗口除 GPT‑6.2 之外最完整的新旗舰模型发售，官方价格和结构都写在自己的帖和新闻稿里。
- **是什么**：
  - 官宣：@Alibaba_Qwen 11-16 10:01 Asia/Singapore；阿里云新闻稿落款 November 16, 2026；官方博文入口 [qwen.ai/blog?id=qwen4-max](https://qwen.ai/blog?id=qwen4-max)。
  - 规格（官方自报）：新 MoE 架构，总参数 **2.4 万亿**，每 token 激活 **710 亿**（新闻稿称比同规模的 Qwen3.8-Max 少激活 25%）；原生视觉；**1M** 上下文。开放权重的较小 Qwen4 模型「即将发布」，本期发布的是托管旗舰，不是开源权重本身。
  - 定价（官方 X 帖 / AA 复述一致）：**$1.50 / $4.50** 每百万输入/输出，隐式缓存 **$0.075**（官方称较 Qwen3.8-Max 的缓存价低 70%）。已在 QwenCloud API、Qwen Studio、QwenWork、Qoder 上线。
  - 官方自报效果：X 帖称内部评测相对 Qwen3.8-Max「最多约少 50% token，任务平均成本下降超过 60%」。新闻稿另一处写 Work360（自有行业基准）在 High 推理档少用 35% token、任务平均成本约降 60%。两处口径并存，不以转述抹平。新闻稿还称 Code Arena 排名第 6。
  - AA 自报对照：Intelligence Index 在 xhigh 档为 43，较 Qwen3.8-Max（xhigh，34）高 9 分，落后 Kimi K3.1 Pro（max，46）3 分；任务成本称约 $3.27，低于 Qwen3.8-Max 的 $10.02，也低于 Kimi 的 $3.68。Terminal-Bench 4.0 称 48%，低于 Kimi 的 67%。
- **为何重要**：国产/开源阵营的新一代闭源旗舰把价位压到 $1.50/$4.50，并明确对标 Kimi K3.1 Pro。是否真能在 agent 与编码上追上，要等第三方复测，而不是只看官方 Work360。
- **对谁·深读建议**：要接 API 的人先看官方定价和 QwenCloud 文档；做选型的人把 AA 的 43 分和 Terminal-Bench 短板一并读，不要只摘「成本降 60%」。
- **证据**：
  - 官方自报：[@Alibaba_Qwen](https://x.com/Alibaba_Qwen/status/2122148127520289151)、[阿里云新闻稿](https://www.alibabacloud.com/en/press-room/alibaba-unveils-qwen4-max?_p_lc=1)、[Qwen 博文](https://qwen.ai/blog?id=qwen4-max)、[QwenCloud 模型页](https://www.qwencloud.com/models/qwen4-max)
  - 第三方：[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2122161629592953032)
- **约时**：新闻稿落款 11-16；X 官宣 11-16 10:01 Asia/Singapore

###### 4. OpenAI 扩大「学术研究者」计划：目标 20 万名科研人员免费使用，11-23 开放申请
这是官方把「科学用途」从模型发布旁白，写成可申请的项目扩容，并配了一份自报的生产率研究。
- **是什么**：
  - 官宣：@OpenAI 11-17 01:13 Asia/Singapore；博文落款 November 16, 2026，标题 *Broadening access to AI for scientists*。
  - 计划（官方）：把 ChatGPT for Academic Researchers 扩大到最多 **20 万**名科研人员免费使用前沿模型，并提供培训。下一轮申请于 **11-23（周一）** 开放；将发放 **5 万**份新资助，每份覆盖申请人及最多两名合作者（本轮最多覆盖 15 万人）。整体目标 20 万，是 7 月试点目标的两倍。新一轮改按先到先得，不再抽签；新资助提供 **ChatGPT Plus**（试点为 Pro，官方称多数人未用满 Pro 额度）。默认不把该计划中的数据用于训练。已在等候名单且符合条件的人会在开放前收到邮件。
  - 试点与研究（官方自报）：7 月以来已有 33 个国家的 2 万名研究者加入。经济研究团队报告 *Science at the Frontier: How Scientists Use ChatGPT*，覆盖 1,800 多名参与者；受访者估计，若无 AI、要达到同等质量，同样的研究工作会花近两倍时间。这是调查自报，不是对照实验的因果结论。
  - 相邻官方动作：另有数学方向向 Simons Foundation 新计划出资 $5M；GPT‑Rosalind 学术方案称向符合条件的美国大学实验室提供最多 30 个席位、最长 12 个月免费（需可信访问审批）。
- **为何重要**：把「20 万科学家」从口号落到申请日期、档位和默认数据政策。也提醒：新一轮给的是 Plus 不是 Pro，名额按申请而非抽签。
- **对谁·深读建议**：高校和实验室读者直接读官方计划页与 11-23 申请安排；引用「生产率近翻倍」时必须标明是参与者自估。
- **证据**：
  - 官方自报：[@OpenAI 计划](https://x.com/OpenAI/status/2122377585523126615)、[@OpenAI 研究](https://x.com/OpenAI/status/2122380010287960095)、[计划博文](https://www.openai.com/index/expanding-chatgpt-for-academic-researchers/)、[研究页](https://www.openai.com/index/science-at-the-frontier/)
- **约时**：博文落款 11-16；X 官宣 11-17 01:13 Asia/Singapore

###### 5. Claude Code 推出实验性 Code Mode，并上线 Linked billing；同期发布验证工作方法
Anthropic 本窗口没有新的旗舰模型，但把编程产品的工具编排、计费和组织向的桌面通道往前推了一步。
- **是什么**：
  - Code Mode（官方，@ClaudeDevs 11-18 05:18 Asia/Singapore）：实验性工作方式，让 Claude 编写脚本把工具串联起来，并在长命令仍在运行时继续回答。需设置 `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1`。文档：[code.claude.com/docs/en/code-mode](https://code.claude.com/docs/en/code-mode)。
  - Linked billing（官方，11-18 02:00 Asia/Singapore）：Claude Platform 进入测试，Factory、Linear、Ramp 等工具的用户可通过自己的 Claude Platform 组织支付 API 用量，而不必共享 API 密钥。
  - 验证方法博文（官方，11-17 06:31 Asia/Singapore）：称「当 Claude 能验证自己的工作时代码更好」，讨论测试、基准和端到端运行成本下降后的工作流。[How the Claude Code team thinks about verification](https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/)。
  - 同期产品：Desktop 可在 Settings 中选择 Latest 通道，默认仍为 Stable（11-18 06:35 Asia/Singapore）；Desktop 公开测试支持在 iOS 模拟器里跑 iPhone Duo，并可折叠/展开设备以检查布局（11-17 05:18 Asia/Singapore）。
- **为何重要**：Code Mode 把「一次次点工具」改成可编排的脚本循环；Linked billing 则解决第三方工具代扣额度时的密钥分享问题。两者都还是测试/实验，不能写成已对所有用户默认开启。
- **对谁·深读建议**：日常用 Claude Code 的人可先读验证博文和 Code Mode 文档再决定是否打开实验开关；企业管理员应看 Linked billing 是否覆盖自己在用的工具。
- **证据**：
  - 官方自报：[@ClaudeDevs Code Mode](https://x.com/ClaudeDevs/status/2122801681939234950)、[@ClaudeDevs Linked billing](https://x.com/ClaudeDevs/status/2122751844455956760)、[@ClaudeDevs 验证](https://x.com/ClaudeDevs/status/2122457608963395586)、[@ClaudeDevs Latest 通道](https://x.com/ClaudeDevs/status/2122821051910684824)、[@ClaudeDevs iPhone Duo](https://x.com/ClaudeDevs/status/2122439098740674839)
- **约时**：验证博文 11-17 06:31 Asia/Singapore；Code Mode 11-18 05:18 Asia/Singapore

##### 进展

###### 进展：Anthropic IPO——见主条 2；采集时尚未定价
- 已在主条写明 11-17 S-1/A 与 8-A12B；FAQ 时间表未改；无最终价、无 424B。

###### 进展：Daybreak Red Team / Defense Factory——无新的官方定价或长文
- **是什么**：产品页内容与上期所见一致，仍是申请通道、Blue/Red、Defense Factory / Red Team、插件与 Codex Security CLI/SDK，以及既有的 10 亿美元补贴表述。未找到新的官方评测表或价目。@thsottiaux 11-15 14:01 Asia/Singapore 发帖为 Cyber 团队征集对 Daybreak 的反馈（模型、插件、蓝/红准入、文档、红队与 Defense Factory）。News 里此前的 77%/79.1% 仍未见官方页复述，继续不写入来源记录。
- **证据**：[@thsottiaux](https://x.com/thsottiaux/status/2121845965997101118)、[Daybreak 产品页](https://openai.com/daybreak/)
- **约时**：反馈征集 11-15 14:01 Asia/Singapore；产品页核验于 11-18 上午 Asia/Singapore

###### 进展：Gemini 4 Hydrogen / Carbon / Decisions API——无官方改价；有产品演示与 Robotics 插件
- **是什么**：未见 Carbon / Hydrogen / Decisions API 的官方条款修订。本窗口官方更新主要是演示与插件：Gemini 4 Hydrogen + Antigravity 的机器人插件，可连接受支持机械臂，在 MuJoCo 中练习并用自然语言在真实环境执行（@GoogleDeepMind 11-18 03:03 Asia/Singapore）；Hydrogen 把 Google Sheets 做成像素画布的演示（11-18 05:43 Asia/Singapore）；AI Studio 推出自定义域名（11-18 06:23 Asia/Singapore）。Microsoft-Decision-1.1 由 AA 报道为既有决策模型的更新，定价仍为每百万输入 $0.042（AA 自报，11-18 02:48 Asia/Singapore），不是 Google Decisions API 的修订。
- **证据**：[@GoogleDeepMind 机器人](https://x.com/GoogleDeepMind/status/2122767521925230896)、[@GoogleDeepMind Sheets](https://x.com/GoogleDeepMind/status/2122807824531275826)、[@GoogleAIStudio 域名](https://x.com/GoogleAIStudio/status/2122817812200555003)、[@ArtificialAnlys Decision-1.1](https://x.com/ArtificialAnlys/status/2122763792828555299)
- **约时**：11-18 凌晨至上午 Asia/Singapore

###### 进展：Claude Meetings、Fable 5.2 / Mythos 5.2——未见官方改价或平台扩展
- **是什么**：@claudeai 本窗口无原创主帖，未见 Meetings 扩到其他会议平台或改计费的官方说明。Fable 5.2 官方价格未见调整。AA 侧有 PersonalityBench（称 Fable 5.2 比 5.1 更直接、回复更短）以及与 GPT‑6.2 的 Robotics / Intelligence Index 对照，见主条 1。
- **证据**：官方检索无新修订长文；AA：[PersonalityBench](https://x.com/ArtificialAnlys/status/2122475355902546307)
- **约时**：覆盖至 11-18

###### 进展：Cursor 安全事件——本窗口无实质新进展
- **是什么**：官方检索中 @cursor_ai 无原创主帖；未找到新的调查更新或新 IoC 官方页。上期 11-13 博文仍是可引用的最新官方说明。
- **证据**：官方检索 result 中无 cursor_ai 主帖；[上期已核调查更新](https://cursor.com/blog/security-incident-update) 未见新官方修订声明
- **约时**：覆盖至 11-18

###### 进展：Claude Code #107757 / 2.1.317——issue 仍 open，本窗口无新的官方关闭
- **是什么**：#107757 标题仍为 *Bug Report: Privacy violation in User-Agent header*，state=open。议题页可见的最近一条实质评论时间为 2026-11-13 06:57 Asia/Singapore（与上期核验一致），本窗口未见官方将问题标为已关闭。2.1.317 的内置隐私 mod 仍是此前维护者评论中的说明，不是本期新公告。
- **证据**：来源记录：[GitHub #107757](https://github.com/anthropics/claude-code/issues/107757)
- **约时**：核验于 11-18 上午 Asia/Singapore

###### 进展：Kimi K3.1 Pro——权重/许可无实质变更；下载量继续上行
- **是什么**：来源记录 重核 `moonshotai/Kimi-K3.1-Pro`：`lastModified` 仍为 2026-11-05 15:11 Asia/Singapore；downloads≈53224（上期核验约 43687）；likes≈2197；siblings=112；`license=other`。官方账号本窗口无原创主帖。AA 在 Qwen4-Max 对照中仍把 Kimi K3.1 Pro 作为开源侧参照（Index 46，AA 自报）。
- **证据**：来源记录：[HF 模型页](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)
- **约时**：HF 核验 11-18 上午 Asia/Singapore

###### 进展：ChatGPT / Codex 共享额度——帮助中心可见原文，仍无新公式
- **是什么**：本期 WebFetch 帮助中心 [Understanding ChatGPT and Codex usage limits](https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits)，正文仍为：从 12 月起，Plus / Pro / Business 的用量在 ChatGPT 与 Codex 之间共享，按 token 计量；Instant chat 不计入；可在 Settings → Usage 查看剩余量与重置时间。页面标注「Updated: 16 days ago」。**未见新的计划额度数字，也未见精确到某一天的生效日。** 上期 Tibo 所称 banked reset 已激活，本窗口无新的官方补充。
- **证据**：官方自报：[帮助中心](https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits)
- **约时**：核验于 11-18 上午 Asia/Singapore

###### 进展：GPT‑6.2——已正式发布，见主条 1
- 上期「仅有传闻、无官宣」的状态在本窗口结束。

##### 其他

- **OpenAI 其他**：ChatGPT for Healthcare 称增强计算机使用代理、临床回答，并新增 20 多个医疗插件，点名 Abridge、Ambience、Cigna、CVS Health 等（11-17 07:03 Asia/Singapore）。[@OpenAI](https://x.com/OpenAI/status/2122465625109090646)、[博文](https://openai.com/index/advancing-computer-use-for-healthcare-teams/)。新科学博客首篇：Nathaniel Craig 与 GPT‑6 Astra 做标准模型格点定义候选（11-16 08:23 Asia/Singapore）。[@OpenAI](https://x.com/OpenAI/status/2122123437141553630)、[博文](https://openai.com/index/step-toward-defining-the-standard-model)。API 用量看板更新（11-18 06:51 Asia/Singapore）。[@OpenAIDevs](https://x.com/OpenAIDevs/status/2122824859491205152)。Tibo 称 Codex「model at capacity」错误或已修复（11-16 13:55 Asia/Singapore，单源）。[@thsottiaux](https://x.com/thsottiaux/status/2122206990101536852)。与 Apollo Research、METR、Transluce、Goodfire 做嵌入式评估（11-17 00:03 Asia/Singapore）。[@OpenAI](https://x.com/OpenAI/status/2122359930628063248)
- **Microsoft / 图像**：AA 称 MAI-Image-2.7 及其 Flash 登上图像编辑与文生图价质前沿（11-18 02:11 Asia/Singapore，AA 自报）。[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2122754535206846610)
- **Mistral**：称 Vibe + Le Chonk 为「最佳开源模型-harness 组合」，欧洲前 3 个月免费，用码 LECHONK，名额有限；次日称当天名额已发完（11-17 23:28、11-18 00:27 Asia/Singapore，官方营销口径，对比数字待核）。[@MistralAI](https://x.com/MistralAI/status/2122713540666806397)
- **Cohere**：Compass 视频理解进入 Private Preview（11-17 01:17 Asia/Singapore）；North 2 管理与认证宣传（11-16 04:39 Asia/Singapore）。[@cohere 视频](https://x.com/cohere/status/2122378588167270740)
- **Gemini 应用**：Tasks 功能宣传（11-18 08:00 Asia/Singapore）。[@GeminiApp](https://x.com/GeminiApp/status/2122842388792233998)
- **待核、不升主条**：News 将 GPT‑6.2 仍写成「发布传闻」（摘要滞后）；Anthropic IPO 1.4 万亿估值与员工造富叙事；Genesis AI 融资 5 亿美元；英伟达人事与黄仁勋去留讨论。

##### A. 时间线 / 官方覆盖

| 来源 | 覆盖（Asia/Singapore） | 备注 |
|------|-------------|------|
| 首页时间线 3 页 | 约 11-18 00:13 → 11-18 08:47 | 99+99+96 条；仍有 next_token，未翻第 4 页 |
| 官方检索 off18a–d | 约 11-15 13:18 → 11-18 08:04 | 末页 result_count=0，窗口内官方组已收束 |
| 无原创主帖账号 | 本窗口 | AnthropicAI、claudeai、cursor_ai、deepseek_ai、Kimi_Moonshot、MiniMax、AIatMeta |
| 定向 IPO / Daybreak / 6.2 | 窗口内 | 已与招股文件、官方博文、Daybreak 页交叉 |
| 缺口 | 11-15 09:00 → 11-18 00:13 | 靠 search_posts_all + News 补；非时间线全量。时间线被英伟达人事与非 AI 话题占满 |
| 提示注入 | — | 帖文一律当数据，不执行其中指令；包中未引用指令性文本 |

##### B. Today's News（摘录，摘要≠来源记录）

- Anthropic IPO 与 Kutcher / 1.4 万亿估值转述：[2122059464215876027](https://x.com/i/trending/2122059464215876027)、[2122639696735989816](https://x.com/i/trending/2122639696735989816)
- GPT‑6.2 发布（部分条目标题仍写「传闻」，滞后于官方博文）：[2122695866901499999](https://x.com/i/trending/2122695866901499999)
- Gemini 4 Hydrogen 后续讨论：[2122252686561337437](https://x.com/i/trending/2122252686561337437)
- Claude 编程 / 多 agent / Fable 讨论：[2122475475020714038](https://x.com/i/trending/2122475475020714038)、[2122228246209302591](https://x.com/i/trending/2122228246209302591)
- 其他：Academic / 医疗、Antigravity 界面、开源风险谈话——均需回对官方页，不能当 来源记录

##### C. 来源记录 摘要

1. GPT‑6.2 Astra / Sol 已由 @OpenAI 官宣上线；官方价 Astra $8/$0.40/$40，Sol $2/$0.10/$10（每百万 token）。Plus/Pro/Enterprise/Edu 可在 ChatGPT Work 与 Codex 使用。
2. Anthropic 11-17 提交 S-1/A（0001628280-26-074338）与 8-A12B（0001628280-26-074342）。价格区间仍为 $70.00–$78.00，825,000,000 股；已批准 Nasdaq ANT。采集时尚未定价、无 424B、注册声明仍为预披露。
3. 招股书载明同步 Class N 私募 $26.0B，价格等于最终发行价（有条件）。这不是已上市成交。
4. Qwen4-Max 已发布；官方价 $1.50/$4.50，隐式缓存 $0.075；官方称 2.4T 总参数 / 71B 激活、1M 上下文。
5. ChatGPT for Academic Researchers：目标 20 万人；11-23 开放申请；本轮 5 万份资助（每份最多 3 人），新资助为 Plus。
6. #107757 仍 open；最近可见更新仍为 11-13 06:57 Asia/Singapore。
7. HF Kimi-K3.1-Pro：lastModified 仍 11-05 15:11 Asia/Singapore；downloads≈53224。
8. Codex/ChatGPT 共享额度帮助中心仍只写「从 12 月起」，无新的额度数字。

##### E. 建议扩写（3–5）

1. **GPT‑6.2 对照表**：把官方 Agents’ Last Exam / Science 自报、官方价，和 AA Intelligence / Robotics / Coding Agent 分数并排，标明「官方自报 vs AA 自报」，避免合刊混用。
2. **IPO 倒计时续篇**：S-1/A-3、8-A12B、$70–78 与 $26B 私募各是什么文件；为什么 11-18 早上 Asia/Singapore 还不能写「已定价」。开盘后对照 424B。
3. **Qwen4-Max vs Kimi K3.1 Pro**：官方价 $1.50/$4.50 对 AA 的 43 vs 46 分，以及 Terminal-Bench 短板，写给要在国产 API 里选型的人。
4. **科学家计划怎么申请**：11-23 先到先得、新一轮是 Plus 不是 Pro、默认不训练，以及「生产率近翻倍」只是调查自估。
5. **Claude Code Mode**：用官方文档解释实验开关、脚本编排和 Linked billing 对第三方工具密钥的意义，提醒仍是 opt-in / beta。


## GitHub 项目与发行

### 项目原始材料

#### GitHub 三日刊（2026-11-15 → 2026-11-18）

1. **vLLM v0.34.0**
`vllm-project/vllm` 于 11-17 07:22（Asia/Singapore）发布正式版 v0.34.0（`prerelease=false`）。这是一次会改默认行为的升级：Model Runner V1 已删除，只保留 V2，再设 `VLLM_USE_V2_MODEL_RUNNER=0` 会直接启动失败；默认 `--block-size` 从 16 改为 64；可扩展 KV cache 默认打开，并按预热后的实际空闲显存来定缓存大小（发布说明举例 MiniMax-M3 在 H200 上从 433k 升到 672k tokens，标「自称」），不想改行为需显式关掉或把 `--gpu-memory-utilization` 设回 0.9。新接入包括 Mistral Large 4（发布说明写明 1T 总参数 / 52B 激活，FP8 与 NVFP4）、MiniMax-M3.1-Flash、Nemotron-3.5-Transcribe，以及 Ripple-65B Preview、LFM3 系列等；ROCm 7.2 镜像已停发，需改用 10.0，并要求 `huggingface_hub >= 2.0.0`。性能数字（如 Step5 在 4×GB200 上 decode 最高 1.95 倍、GLM-5.3-Flash 吞吐 1.6 倍）均来自发布说明，标「自称」。跑生产推理、还在锁 V1 runner 或 16 的 block size、以及要上 Large 4 / M3.1-Flash 的人应先对照升级表再升。
证据：[v0.34.0 Release](https://github.com/vllm-project/vllm/releases/tag/v0.34.0)

2. **OpenAI Python v3.53.0 / Node v7.58.0：GPT-6.2 目录标识与更长的后台窗口**
OpenAI 官方 SDK 于 11-18 02:20–02:40（Asia/Singapore）发布正式版 Python v3.53.0 与 Node v7.58.0（均为 `prerelease=false`），随后在 06:42（Asia/Singapore）又跟上 Python v3.54.0 / Node v7.59.0。3.53 / 7.58 把 Responses 后台窗口补上 2 小时和 8 小时两档，并加入 `GPT-6.2 Astra`、`GPT-6.2 Astra Law`（Responses）和 `GPT-6.2 Sol` 的模型标识——这是 SDK / API 目录里的标识，不是本期在 GitHub 上的模型权重发布，不要写成新模型开源。3.54 / 7.59 只是给 Managed Agents 的预算事件补了类型，属于细补丁。已经在用 Responses 后台任务、或要对接上述目录标识的应用应升到 3.53 / 7.58 以上。
证据：[Python v3.53.0](https://github.com/openai/openai-python/releases/tag/v3.53.0) · [Node v7.58.0](https://github.com/openai/openai-node/releases/tag/v7.58.0) · [Python v3.54.0](https://github.com/openai/openai-python/releases/tag/v3.54.0)

3. **Unsloth Desktop：本机 Computer Use（测试功能）与 MiniMax-H3-Image 量化**
`unslothai/unsloth` 在窗口内连续发布 v0.1.918-beta（11-16 23:04 Asia/Singapore）和 v0.1.919-beta（11-17 22:56 Asia/Singapore）。标签带 `-beta`，但 API 字段均为 `prerelease=false`、`draft=false`。桌面端新增加「Computer Use」测试功能：本地视觉模型或已连接的服务商可以看屏幕并操作键鼠，默认关闭，首次操作和切应用需要批准；同时用 MCP 接上 Unity、Unreal、Godot、Roblox 和 Blender，Figma 只读。MiniMax-H3-Image 补了 GGUF（走 stable-diffusion.cpp，覆盖 CPU / Mac / AMD）以及面向 NVIDIA 的 FP8 / INT8，并支持 LoRA；发布说明自称在 A100 80GB 上 2048px 图解码从 2.82 秒降到 0.28 秒（标「自称」）。用 Unsloth 桌面端做本地图像或想试本机控屏的人可以跟上；控屏权限默认关闭，不要一开就接到不受信任的模型上。
证据：[v0.1.919-beta Release](https://github.com/unslothai/unsloth/releases/tag/v0.1.919-beta) · [Computer Use 文档](https://unsloth.ai/docs/basics/computer-use) · [GGUF 权重](https://huggingface.co/unsloth/MiniMax-H3-Image-GGUF)

4. **Tencent/LoopForge v0.4.0**
腾讯官方组织于 11-17 22:30（Asia/Singapore）发布正式版 v0.4.0（`prerelease=false`）。上期只见到 0.3.8 的修补和 0.3.9-rc.1 预发布，官方说明 0.3.9 不会再出正式版，装了 rc 的应直接升到 0.4.0。这一版补上按主机配置的 SSH 仓库密钥，允许在智能体运行时编辑工作区，并收紧安全默认值：把智能体 CLI 的配置写入限制在 home 目录，克隆地址里不再带凭据，沙箱里安装代理 CLI 时会打码密钥。这是自托管的编码智能体工作流，官网为 [loopforge.cn](https://loopforge.cn)。截至 11-18 约 08:52（Asia/Singapore）API 总量 **3,136 星**，日榜约 **591 stars today**（热榜于 08:50 Asia/Singapore 抓取，是约 24 小时窗口，不是本期 72 小时净增）。自己搭智能体交付流水线、或还停在 0.3.9-rc 的人应该升。
证据：[v0.4.0 Release](https://github.com/Tencent/LoopForge/releases/tag/v0.4.0) · [Tencent/LoopForge](https://github.com/Tencent/LoopForge) · [官网](https://loopforge.cn)

（热榜口径：日榜约为最近 24 小时，周榜统计最近七天，均于 2026-11-18 08:50 Asia/Singapore 抓取，不可当作本期 72h 净增。周榜前列 meta/astryx 约 8,700 stars this week、we-promise/sure 约 4,786、anthropics/skills 约 4,847、vercel-labs/agent-browser 约 3,429，均为旧仓留榜，不单列。google-research/paper-orchestra 日榜约 1,072、总量约 2,998，官方组织身份可核，但无 GitHub Releases，本期不单列。google-labs-code/stitch-skills 周榜约 1,197，最近推送仍在 8 月，只是留榜。alibaba/open-code-review 日榜约 763，窗口内为 v1.13.11 等补丁。cursor/plugins 日榜约 201，官方组织可核，但无 Releases 页上的正式版本。新仓搜索除下方点名者外，11-15 16:46–16:48（UTC）出现一批几乎同名的 `Gemini-Config-Checker-` 克隆，星数都在约 473，描述为探测代理配置以进入 Google AI Studio / Gemini，当作垃圾克隆处理，不收录。个人仓 `gylive/google-ultra` 约 1,569 星、687 fork，无组织官网反链，README 自称用客户端脚本走 Play 结算试用，与 Google 无关，星数不能当作可信依据，不收录。`ranxianglei/billion-context` 仍无新的可交叉核验进展，继续不收录。）

窗口内无：sgl-project/sglang、ggml-org/llama.cpp（仅 `b12xxx` 预发布日构建）、ollama/ollama（最新仍为窗口前的 v0.40.17-rc1，`prerelease=true`）、huggingface/transformers、pytorch/pytorch、huggingface/datasets、modelcontextprotocol/python-sdk、modelcontextprotocol/typescript-sdk、comfyanonymous/ComfyUI、axolotl-ai-cloud/axolotl、langchain-ai/langgraph（常规 / 预发布未收录：openai/codex 正式补丁 0.169.1 无核验亮点，以及多枚 `*-alpha.*`；anthropics/anthropic-sdk-python v2.9.0 / v2.10.0 与 TypeScript sdk-v1.9.0 / sdk-v1.10.0，主要为账单策略、错误码与 webhook；langchain-core 1.8.1 / 1.8.2、langchain-openai 1.8.1，以及 langchain-xai 1.4.0、langchain-mistralai 1.2.0、langchain-groq 1.2.0、langchain-deepseek 1.2.0 等合作包补丁）


## 模型与数据集

### 模型、数据与榜单原始材料

#### HF / 模型三日雷达素材 · 2026-11-18

- 窗口：2026-11-15 09:00 Asia/Singapore（01:00 UTC，上期采集截止）→ 2026-11-18 约 09:00 Asia/Singapore（01:00 UTC，实际采集时刻）。
- 去重基线：11/15 素材包（内部证据存档），sha256 83d37c22…6663）以及 （内部证据存档） 的榜单快照和镜像核查。上期写过的条目只在有新事实时才写，并标为“更新”。
- 计数：主条 3（全部为新发布）｜跟进 7（Inkling 2 Small、MiniMax-H3-Image、ZONOS3、Haru-4B、Kimi K3.1 Pro、Nex-N2.6、meta-encoder-v1）｜次条 7（另有 4 条窗口前发布、往期漏掉的补记）｜榜单 6 段｜数据集 5 条主条 + 3 条附记｜冒名/同名镜像 3 组（另列 4 个合法原样转存）。
- 数据口径：likes/downloads 统一取 HF API 在 2026-11-18 08:59 Asia/Singapore（00:59 UTC）的快照（采集证据快照）。downloads 是 HF 的近 30 天口径，新 repo 当天常显示 0。Trending 取 08:51 Asia/Singapore 的 API（模型 300 条、数据集 100 条），与 trending HTML 页一并保存。
- 开放程度用语：“开放权重”= 权重能下载；“OSI 许可”= 权重许可证属于 OSI 认可的许可证（Apache-2.0/MIT），未逐项核对 OSAID；“自定义/非商用许可”= 权重开放，但不算开源。

##### 三句话结论

1. **本窗最大的开放权重是上海 AI Lab 的 Sage S2.1 Flash（约 321B MoE，卡片写 MIT），但它是在智谱 GLM-5.3-Flash 上继续训练的科学多模态 agent 模型，不是新基座。** 参数量与 GLM-5.3-Flash 一模一样（321,323,031,390），config 架构类就是 Glm5Next；HF 的 license 元数据在 11-16 被 README 改写清空，许可证目前只写在卡片正文里。
2. **商汤 SenseNova-Loop-9B 正式版（Apache-2.0）和苹果 FastFrames（研究许可，不可商用）是另外两件值得写的新东西。** 前者把 24 层“跑两遍”，9B 参数做 56 层计算；后者把 Wan2.1 蒸馏成两步自回归视频模型，单卡 480p 每帧约 36ms（苹果自报）。
3. **榜单侧，AA 新收录 GPT-6.2 Astra（62.1，排第 2）、GPT-6.2 Sol（57.3）和 Qwen4 Max（42.9），全是闭源；开放权重榜首仍是 Kimi K3.1 Pro（46.5）。** LMArena 文生图刷新到 Nov 16，新进 MAI-Image-2.7 直接排 #4；文本榜和视觉榜都没刷新，视觉榜在同一数据日期下删掉了 GLM-5V-Turbo 一行。

---

##### 主条

###### 1. internlm/Sage-S2.1-Flash（+ Sage-S2.1-Flash-FP8）· 新开放权重（卡片写 MIT，属 OSI 许可；HF 元数据缺失）

这是本窗唯一的大规模新开放权重：上海人工智能实验室发布的科学多模态 agent 模型，能把分子图、晶体结构、蛋白序列和三维结构、DNA/RNA、光谱、心电、脑电等十多类科学数据经投影器喂进语言模型，再配合检索、写代码和操作科学软件来做多轮分析。但要讲清楚：它的骨干就是 GLM-5.3-Flash 的结构和参数规模，属于“在开放基座上做科学/agent 后训练”，不是从头训练的新基座。卡片自报的 15 项对比里，它在 MLE-bench Lite、OfficeQA Pro、Harvey LAB、SpreadsheetBench 2 上排第一，但在同一张表里 Terminal-Bench 2.1、DeepSWE 都不是第一。

- 为什么重要：
  - 国内国家级实验室把一个 321B 级 agent 模型以宽松许可放出，而且技术报告（arXiv 2611.21072，206 位作者）同步发布，可复查程度比一般“只放权重”的发布高。
  - 它是继 Nex-N2.6 之后第二个以 GLM-5.3-Flash 为底座的 321B 级开放模型（两者参数量逐位相同），说明 GLM-5.3-Flash 正在成为国内 agent 后训练的公共底座。
  - “科学数据投影器 + 通用 agent 骨干”这条路线，第一次以完整权重的形式放出（投影器配置在 `projectors/` 下，含 cif、dna、ecg、eeg、蛋白序列/结构、rna、光谱、xrd 共 9 类）。
- 适合谁 / 阅读建议：
  - 做 AI for Science、科研 agent 的团队值得读技术报告和卡片的 “Inference for Scientific Tasks” 一节；需要自己另行准备科学编码器，投影器输出通过 vLLM 的 `prompt_embeds` 接口送入。
  - 自托管门槛高：BF16 约 643GB，FP8 版约 329GB；部署指南直接让用户照 GLM-5.3-Flash 的官方 vLLM/SGLang 配方操作。
  - 普通读者只需记住：这是“GLM-5.3-Flash 的科学 agent 版”，分数都是实验室自测。
- 来源记录：
  - HF 时间：createdAt 2026-11-15 02:34 UTC / 11-15 10:34 Asia/Singapore；lastModified 2026-11-16 08:30 UTC / 11-16 16:30 Asia/Singapore。权重 commit `6ba152f81a`“Upload folder using huggingface_hub”，2026-11-15 02:59 UTC / 11-15 10:59 Asia/Singapore（窗口内）；随后 11-15 09:30–10:44 UTC 加部署指南和 vLLM 0.33.0 补丁，11-16 03:01–04:23 UTC 两次上传投影器配置，11-16 08:30 UTC `76f4513db7` 改写 README。
  - 热度：likes 97 / downloads 337（采集 11-18 08:59 Asia/Singapore）；HF Trending #21（trendingScore 95，08:51 Asia/Singapore）。FP8 版 likes 14 / downloads 165（采集 11-18 08:59 Asia/Singapore）。
  - 许可 / 任务：卡片正文 License 一节写“The code and model weights in this repository are released under the MIT License”。但 commit `76f4513db7` 把 README 开头原本的 `license: mit` 元数据整段替换掉了，所以 HF API 现在的 license 字段和 pipeline 字段都是空的。按卡片正文算开放权重、OSI 许可；元数据缺失是工程疏漏，转述时以卡片正文为准并注明。repo 里没有单独的 LICENSE 文件。
  - 权重证据：主 repo 129 个权重文件，合计 642.83GB（`?blobs=true` 统计）。HF 解析参数量 321,323,031,390，与 zai-org/GLM-5.3-Flash 的 321,323,031,390 完全相同；config 的 architectures 为 `Glm5NextForConditionalGeneration`、model_type `glm5_next_text`，45 层、288 个路由专家、每 token 8 个、max_position_embeddings 1,048,576。
  - 底座证据：部署指南 commit `7ac18f6dcb` 标题就是“link the official GLM-5.3-Flash recipes”；11-16 那次投影器配置更新之前，`projectors/.../cif/jarvis/config.json` 里的内部训练路径含 `exp_agent_glm53_flash` 字样，更新后被替换成指纹（采集证据快照） 留存了 diff）。GLM-5.3-Flash 本身是 MIT，许可链上没有冲突。
  - FP8 版 internlm/Sage-S2.1-Flash-FP8：createdAt 2026-11-13 15:04 UTC / 11-13 23:04 Asia/Singapore（早于窗口创建，11-13 15:22 UTC 已有一次上传，11-16 02:58 UTC 删除旧目录后重新上传）；lastModified 2026-11-16 08:30 UTC / 11-16 16:30 Asia/Singapore；71 个权重文件，328.51GB。
  - 官方身份：internlm 组织（显示名 Intern Large Models，未认证，1,418 关注者，139 个模型）。卡片自述来自 Shanghai Artificial Intelligence Laboratory；官方项目页 internlm.github.io/Sage-S2.1-Flash 和 GitHub InternLM/Sage-S2.1-Flash 都链回这两个 HF repo。上期（11/09）写过的 Sage-SciPerception 就是它的投影器体系。
  - 技术报告：arXiv 2611.21072，v1 提交于 2026-11-16 13:23 UTC / 11-16 21:23 Asia/Singapore，标题“Sage S2.1 Flash Technical Report”。注意摘要正文两处写成了“Sage S1.5 Flash”，与标题和卡片不一致，是笔误还是版本残留待核。
- 待核：
  - 卡片和报告的所有基准（MLE-bench Lite 90.3、OfficeQA Pro 72.2、OSWorld-Verified 85.2 等）都是实验室自测；AA 和 LMArena 都还没有收录它。
  - 激活参数量：卡片没写。第三方 orcarouter 博客写“320B-A18B”，是按 GLM-5.3-Flash 规格推的，待官方确认。
  - HF license 元数据为空会让按标签筛选的用户看不到 MIT，是否会补回待观察。
- 衍生（降权）：窗口内按名称能搜到 7 个第三方量化版（EXL3、NVFP4、oQ 系列等），如 Mia-AiLab/Sage-S2.1-Flash-EXL3-4bpw，都不写入正文。
- 证据：
  - [HF internlm/Sage-S2.1-Flash](https://huggingface.co/internlm/Sage-S2.1-Flash)
  - [HF internlm/Sage-S2.1-Flash-FP8](https://huggingface.co/internlm/Sage-S2.1-Flash-FP8)
  - [arXiv 2611.21072](https://arxiv.org/abs/2611.21072)
  - [internlm.github.io 来源](https://internlm.github.io/Sage-S2.1-Flash/)
  - [GitHub InternLM/Sage-S2.1-Flash](https://github.com/InternLM/Sage-S2.1-Flash)
  - 第三方：[orcarouter.ai 来源](https://www.orcarouter.ai/blog/sage-s2-1-flash-quiet-release)
  - 本地：（采集证据快照）、（采集证据快照）、（采集证据快照）、（采集证据快照）

###### 2. sensenova/SenseNova-Loop-9B · 新发布（Preview 的正式版；开放权重，Apache-2.0，OSI 许可；gated: auto）

商汤在 10/30 发了 Preview（往期已写），11/17 发了正式版。核心思路不变：32 个物理层里有 24 层共享权重、按顺序跑两遍，一次前向做 56 层计算，用“多算一遍”换“少存参数”；再加两路残差流的 mHC 连接。正式版主打 agent、写代码和数据分析，官方自报在 AutomationBench 上和 Qwen3.8-27B 打平（36.67），NL2Repo 略低（41.36 vs 44.60）。它是本窗 Trending 上排名最高的新建 repo（#12）。

- 为什么重要：
  - 9B 参数、约 15GiB 显存（4bit 权重 + 8bit KV、256K 上下文，官方数字）就能跑多模态长上下文，是端侧/单卡用户能真正用上的新模型。
  - “循环层”路线此前多停留在论文和小模型，这是少数带完整工具链、正式版本号的开放实现。
- 适合谁 / 阅读建议：单卡部署 agent 或多模态应用的开发者；关心参数效率的研究者可读 GitHub README 的架构一节。已用 Preview 的用户可以直接换正式版。
- 来源记录：
  - HF 时间：createdAt 2026-11-17 10:16 UTC / 11-17 18:16 Asia/Singapore；lastModified 2026-11-17 12:19 UTC / 11-17 20:19 Asia/Singapore。repo 设了 gated: auto，commits 接口匿名返回 401；用 tree 接口看到 10 个权重文件的 lastCommit 都是 `c26b3edcf4`，时间 2026-11-17 10:52 UTC / 11-17 18:52 Asia/Singapore。gated: auto 表示点同意即自动放行，不等于未发布。
  - 热度：likes 184 / downloads 0（采集 11-18 08:59 Asia/Singapore，新 repo 下载计数未刷新）；HF Trending #12（trendingScore 180，08:51 Asia/Singapore）。Preview 版 likes 314 / downloads 4,887（采集 11-18 08:59 Asia/Singapore）。
  - 许可 / 任务：license apache-2.0，pipeline image-text-to-text，library transformers（custom_code，需 trust_remote_code）。开放权重，OSI 许可。
  - 权重证据：11 个 safetensors，合计 18.83GB；HF 解析参数 9,412,963,952（BF16 9,409,812,208 + F32 3,151,744）。
  - 官方身份：sensenova 组织（显示名 SenseNova，未认证，864 关注者，42 个模型）。GitHub OpenSenseNova/SenseNova-Loop 的 News 写“2026-11-17: We release SenseNova-Loop-9B, with model weights and code available to the community”。
  - 规格（GitHub README）：32 层解码器，线性注意力和全注意力按 4 层一组交替；训练上下文扩到 512K；输入文本和图像、输出文本。
- 待核：
  - Preview → 正式版的提升（AutomationBench 14.33→36.67、Terminal-Bench 2.1 40.45→59.55、GAIA 37.86→69.90）和与 Qwen3.8-27B 的对比都是商汤自报。
  - README 说“发布当天提供官方 AWQ 4bit 版”，但采集时 sensenova 组织最新 6 个 repo 里没有 AWQ 版，可能还没上传或放在别处。
  - 15GiB 显存是官方在特定配置下的数字。
- 衍生（降权）：窗口内按名称搜到 13 个第三方量化版（GGUF、MLX、FP8），如 guideboardlabs/SenseNova-Loop-9B-GGUF（likes 6 / downloads 0（采集 11-18 08:59 Asia/Singapore），不写入正文。
- 证据：
  - [HF sensenova/SenseNova-Loop-9B](https://huggingface.co/sensenova/SenseNova-Loop-9B)
  - [HF sensenova/SenseNova-Loop-9B-Preview](https://huggingface.co/sensenova/SenseNova-Loop-9B-Preview)
  - [GitHub OpenSenseNova/SenseNova-Loop](https://github.com/OpenSenseNova/SenseNova-Loop)
  - 本地：（采集证据快照）、（采集证据快照）

###### 3. apple/FastFrames-L / FastFrames-S · 新发布（开放权重，Apple 机器学习研究许可，仅限非商用研究，非 OSI）

苹果把“交互级延迟”的视频生成模型连同全部中间 checkpoint 一起放了出来：FastFrames-S（1.3B）和 FastFrames-L（14B）都是两步出帧的自回归视频扩散模型，480p。L 版由 Wan2.1-14B 蒸馏而来。苹果的论点是：VAE 解码、KV 缓存这类常被当成“实现细节”的环节才是延迟大头，把它们换成像素解码器和 KV 精修网络后，S 版单卡每帧总延迟约 35.4ms（论文写 36ms）。但许可证明确写着只能用于非商业科研。

- 为什么重要：
  - 实时可交互的视频/世界模型是今年的热点方向，苹果这次不只给最终模型，还给了因果教师、一致性蒸馏、DMD 蒸馏三个中间阶段的权重，研究者可以逐阶段复查。
  - 附带一个优化版 LingBot 1.3B（官方称比原版快 16 倍，可用键盘控制镜头），可以直接体验“边生成边交互”。
- 适合谁 / 阅读建议：做视频生成加速、世界模型、交互式生成的研究者。商业团队不能直接用，许可证只允许 Research Purposes。
- 来源记录：
  - HF 时间：两个 repo 的 createdAt 都是 2026-11-16 17:21 UTC / 11-17 01:21 Asia/Singapore；lastModified 2026-11-17 21:20 UTC / 11-18 05:20 Asia/Singapore。两个 repo 都只有一个 commit，L 为 `45e2e3798c`、S 为 `9a4b9cdc4d`，标题都是“Public release”，时间 2026-11-17 21:20 UTC / 11-18 05:20 Asia/Singapore，即公开时间。
  - 热度：L likes 33 / downloads 0，S likes 10 / downloads 0（采集 11-18 08:59 Asia/Singapore，公开不到 4 小时）；L 在 HF Trending #122（trendingScore 31，08:51 Asia/Singapore）。
  - 许可 / 任务：license apple-amlr，pipeline text-to-video。repo 内 LICENSE 是“Apple Machine Learning Research Model”许可：个人、不可转让、可撤销，只允许“Research Purposes”（非商业科研），衍生模型也限于研究用途。开放权重，非商用，不是 OSI 许可，不算开源。代码另走 Apple Sample Code License；附带的 LingBot-World v2 代码和权重沿用上游 CC BY-NC-SA 4.0。
  - 权重证据：L 共 20 个文件，大文件 10 个合计 173.24GB，含 `fastframes-l-intermediate/` 下 causal_teacher、consistency、dmd 三套中间权重；S 共 10 个文件，权重 1.77GB。两个 repo 都带 SHA256SUMS。base_model 元数据：L 为 Wan-AI/Wan2.1-T2V-14B，S 为 Wan-AI/Wan2.1-T2V-1.3B 和 zhuhz22/Causal-Forcing。
  - 官方身份：apple 组织（HF 认证，7,807 关注者）。项目页 apple-aiml-research.github.io/ml-fastframes 列出作者 Gene Chou（Apple / Cornell）、Vladlen Koltun 等，链回 GitHub apple-aiml-research/ml-fastframes 和这两个 HF repo。
  - 输出规格（卡片）：832×480，81 帧，16fps。
- 待核：
  - 35.4ms 是苹果在单卡、满 KV 缓存下的自测；L 版需要 8 卡跑延迟基准，卡片没给 L 的延迟数字。项目页写“<50 ms”。
  - 论文 arXiv 页面卡片上标“coming soon”，采集时还没有 arXiv 编号；VBench 分数卡片没有列出。
  - Wan2.1 本身是 Apache-2.0，苹果在其上叠加研究许可，衍生权重的许可链以苹果 LICENSE 为准。
- 证据：
  - [HF apple/FastFrames-L](https://huggingface.co/apple/FastFrames-L)
  - [HF apple/FastFrames-S](https://huggingface.co/apple/FastFrames-S)
  - [apple-aiml-research.github.io 来源](https://apple-aiml-research.github.io/ml-fastframes/)
  - [GitHub apple-aiml-research/ml-fastframes](https://github.com/apple-aiml-research/ml-fastframes)
  - 第三方：[tpsreport.news 来源](https://tpsreport.news/news/apple-fastframes-l-14b-interactive-video-generation)
  - 本地：（采集证据快照）、（采集证据快照）

---

##### 跟进（无新权重或只有修补，更新状态）

###### F1. Inkling 2 Small：官方改了 config.json 里一个推理参数，已下载的用户应同步 · 更新

- 判断：这是本窗唯一会影响已有用户推理结果的跟进。11-17 18:39 UTC / 11-18 02:39 Asia/Singapore，两个官方 repo 同时提交“Update config.json”，把注意力的 `log_scaling_n_floor` 从 128000 改为 8192（diff 只有这一行）。MXFP8 版在 11-17 03:34 UTC / 11-17 11:34 Asia/Singapore 还把量化配置从 `modelopt / MXFP8` 改写成通用的 `fp8` 块量化描述（block 1×32、ue8m0 scale），方便其他推理框架识别。官方没有发说明，改动对输出的影响待核。
- HF：thinkingmachines/Inkling-2-Small lastModified 2026-11-17 18:39 UTC / 11-18 02:39 Asia/Singapore，config commit `1df2d97d45`；另有 11-15 05:54 UTC 的 `2ad1157016` 只改评测表。权重文件没有变化（25 个 safetensors，393.48GB）。MXFP8 版 config commit `f69fa26848`、量化配置 commit `a39521f1e2`。
- 热度：likes 442 / downloads 18,359（采集 11-18 08:59 Asia/Singapore）（上期 likes 317 / downloads 3,647）；HF Trending #11 → #5（trendingScore 350）。
- 榜单：AA v5 仍是 30.6，open-weights / permissive 不变；LMArena 文本榜本窗没有刷新，仍是 #152（1412±12，Prelim）。
- 衍生：窗口内按名称新增 20 个衍生 repo（GGUF、EXL3、NVFP4 等），另有 abliterated 改包（如 benthecarman/Inkling-2-Small-abliterated，过滤）。
- 证据：[HF thinkingmachines/Inkling-2-Small](https://huggingface.co/thinkingmachines/Inkling-2-Small) · [HF thinkingmachines/Inkling-2-Small-MXFP8](https://huggingface.co/thinkingmachines/Inkling-2-Small-MXFP8) · 本地 （采集证据快照）

###### F2. MiniMax-H3-Image：只加了 DiffSynth 支持；LMArena 被 MAI-Image-2.7 挤到 #24 · 更新

- 判断：模型本身没有新权重，热度仍是全站第一。榜单位置因为新模型进入而后退，分数基本没动。
- HF：lastModified 2026-11-16 10:00 UTC / 11-16 18:00 Asia/Singapore，窗口内唯一 commit 是 `8ced600686`“add Diffsynth support (#28)”。likes 1,460 / downloads 727,110（采集 11-18 08:59 Asia/Singapore）（上期 likes 1,117 / downloads 517,948）；HF Trending #1（trendingScore 809）。许可仍是 minimax-h3-image-community-license-agreement（自定义许可，非 OSI）。
- 榜单：LMArena 文生图 #23 → #24（1198±11，3,285 票）；AA 文生图 #25 → #27（1066±14），Highspeed #24 → #26；AA 编辑 #13 → #14（1135±16）。
- 衍生：窗口内按名称搜到至少 14 个新 repo（搜索上限 100 条），其中 4 个同名复制件见文末冒名段。
- 证据：[HF MiniMaxAI/MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image) · [lmarena.ai 来源](https://lmarena.ai/leaderboard/text-to-image)

###### F3. ZONOS3-Mini：官方出了 transformers 原生版，llama.cpp 官方组织出了 GGUF · 更新

- 判断：生态在补齐，没有重训的新 backbone。
- Zyphra/ZONOS3-Mini：lastModified 2026-11-17 19:41 UTC / 11-18 03:41 Asia/Singapore，commit `2921b88217` 加了一个语音编辑 LoRA（重音编辑，由 gguf 版重建）。likes 510 / downloads 93,909（采集 11-18 08:59 Asia/Singapore）（上期 likes 345 / downloads 19,743）；HF Trending #15。Apache-2.0。
- 新 repo：Zyphra/ZONOS3-Mini-transformers 和 Zyphra/ZAC-1-hf，createdAt 都是 2026-11-16 02:53 UTC / 11-16 10:53 Asia/Singapore，是 transformers 原生实现版（Apache-2.0；前者 likes 4 / downloads 75，后者 likes 2 / downloads 36（采集 11-18 08:59 Asia/Singapore）。上期写过的 ZONOS3-Mini-hf 已不在 Zyphra 组织最近列表中，是否改名为 -transformers 待核。
- ggml-org/ZONOS3-Mini-GGUF：createdAt 2026-11-16 00:31 UTC / 11-16 08:31 Asia/Singapore，3 个 GGUF 共 3.60GB，likes 6 / downloads 691（采集 11-18 08:59 Asia/Singapore）。ggml-org 是 llama.cpp 官方组织。
- 证据：[HF Zyphra/ZONOS3-Mini](https://huggingface.co/Zyphra/ZONOS3-Mini) · [HF Zyphra/ZONOS3-Mini-transformers](https://huggingface.co/Zyphra/ZONOS3-Mini-transformers) · [HF ggml-org/ZONOS3-Mini-GGUF](https://huggingface.co/ggml-org/ZONOS3-Mini-GGUF)

###### F4. Haru-4B：没有新 commit，热度翻倍，升到 Trending #3 · 更新

- higurashi-ai/Haru-4B 仍只有 11-13 01:22 UTC 那一个 commit `8d6e83bcd3`。likes 506 / downloads 4,445（采集 11-18 08:59 Asia/Singapore）（上期 likes 232 / downloads 1,262）；HF Trending #19 → #3（trendingScore 396）。Apache-2.0。窗口内出现 3 个第三方 GGUF/MLX 转换版。上期列出的待核点（65ms 延迟口径、缺少同类标准化对比）没有新进展。
- 证据：[HF higurashi-ai/Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B)

###### F5. Kimi K3.1 Pro：官方 repo、博客、LMArena 都没变；同名全量镜像又多 4 个 · 更新

- 官方：moonshotai/Kimi-K3.1-Pro lastModified 仍是 2026-11-05 07:11 UTC / 11-05 15:11 Asia/Singapore，窗口内没有 commit。likes 2,197 / downloads 53,224（采集 11-18 08:59 Asia/Singapore）（上期 likes 2,078 / downloads 43,687）；HF Trending #25。license other（kimi-k3.1-pro），开放权重，自定义许可。
- 博客：本期重抓 kimi.ai/blog/kimi-k3-1-pro，可见文本与上期逐字相同（23,162 字符），仍写“will be released by Nov 4”。
- NVFP4：nvidia/Kimi-K3.1-Pro-NVFP4 窗口内没有 commit，likes 25 / downloads 1,987（采集 11-18 08:59 Asia/Singapore）（上期 likes 19 / downloads 783）。新出现 RedHatAI/Kimi-K3.1-Pro-DSpark（createdAt 2026-11-17 17:14 UTC / 11-18 01:14 Asia/Singapore，likes 0 / downloads 0），是推测解码草稿模型，信号弱。
- 榜单：LMArena 文本榜没刷新，仍 #24（1485±10，3,995 票）；AA 46.5，仍是开放权重第一。
- 同名镜像：见文末冒名段。
- 证据：[HF moonshotai/Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) · [kimi.ai 来源](https://www.kimi.ai/blog/kimi-k3-1-pro)

###### F6. Nex-N2.6：仍无独立 OSWorld 复现 · 更新

- nex-agi/Nex-N2.6 窗口内没有 commit。likes 143 / downloads 1,074（采集 11-18 08:59 Asia/Singapore）（上期 likes 84 / downloads 593）。Apache-2.0。AA 仍未收录（只有旧的 Nex-N2-Pro）。窗口内能找到的新外部文章（alfw.ai 等）都只是复述官方表格，并指出它在 Terminal-Bench 2.1（84.1 vs 84.3）和 AutomationBench（45.7 vs 48.8）上低于基座 GLM-5.3-Flash；没有人独立跑 OSWorld。
- 证据：[HF nex-agi/Nex-N2.6](https://huggingface.co/nex-agi/Nex-N2.6) · [alfw.ai 来源](https://alfw.ai/article/nex-n26-osworld-83-internal-tests/)

###### F7. facebook/meta-encoder-v1：补上了 Apache-2.0 LICENSE 文件 · 更新

- 上期待核“卡片没有许可说明、能否商用不明”，现在有了答案的一半：2026-11-17 01:57 UTC / 11-17 09:57 Asia/Singapore，commit `7615b21aee`“Upload LICENSE”加入标准 Apache-2.0 全文。但 HF 卡片元数据的 license 字段仍为空，卡片正文也没改。按 LICENSE 文件算开放权重、OSI 许可。likes 43 / downloads 496（采集 11-18 08:59 Asia/Singapore）。
- 证据：[HF facebook/meta-encoder-v1](https://huggingface.co/facebook/meta-encoder-v1) · 本地 （采集证据快照）

---

##### 次条（新发布，信号弱或场景窄）

- **sarvamai/sarvam-105b-1711（NVFP4）+ sarvam-105b-1711-bf16**：印度 Sarvam AI 对 Sarvam-105B（105B MoE / 10.3B 激活，3 月开源）的再后训练版，主攻工具调用、指令遵循、agent 和印度语言。两个 repo createdAt 都是 2026-11-15 07:24 UTC / 11-15 15:24 Asia/Singapore，但都只有一个 commit“Initial release”，时间 2026-11-17 14:09 UTC / 11-17 22:09 Asia/Singapore，这才是公开时间。bf16 版 44 个权重文件 218.22GB、参数 106,031,767,424；NVFP4 版 70.15GB（NVFP4/MXFP8 混合，HF 按打包后计为 56.1B）。likes 1 / downloads 10（bf16），likes 2 / downloads 6（NVFP4）（采集 11-18 08:59 Asia/Singapore）；license apache-2.0，pipeline text-generation，OSI 许可。卡片表格（τ²-Bench 85.5、IFBench 82.5 等）全是 Sarvam 自测，待核；官方博客目前只有 3 月的开源文章，没有 1711 版专文。[HF sarvamai/sarvam-105b-1711-bf16](https://huggingface.co/sarvamai/sarvam-105b-1711-bf16) · [sarvam.ai 来源](https://www.sarvam.ai/blogs/sarvam-30b-105b)
- **nvidia/Qwen3.8-Flash-Next-NVFP4-QAD**：NVIDIA 给 Qwen3.8-Flash-Next 做的实验性 QAD（量化感知蒸馏）版，比 9 月已有的 NVFP4 版更激进：共享专家也压到 NVFP4，部分 GDN/QSA 投影压到 MXFP8，只训练了 100 步。createdAt 2026-11-17 09:32 UTC / 11-17 17:32 Asia/Singapore；lastModified 2026-11-17 11:41 UTC / 11-17 19:41 Asia/Singapore；权重在 11-17 10:03–10:39 UTC 上传，36 个文件 129.72GB。likes 38 / downloads 0（采集 11-18 08:59 Asia/Singapore）；license other（nvidia-open-model-license），pipeline image-text-to-text，自定义许可，非 OSI。卡片自己写明“QAD 带来的精度提升没有统计显著性”。[HF nvidia/Qwen3.8-Flash-Next-NVFP4-QAD](https://huggingface.co/nvidia/Qwen3.8-Flash-Next-NVFP4-QAD)
- **Agnes-AI/Agnes-2.5-Pro-Theta**：约 187.8B 的多模态 MoE，BF16 共 105 个分片、375.53GB，自报 GPQA Diamond 92.9、LiveCodeBench v6 90.5。createdAt 2026-11-15 02:46 UTC / 11-15 10:46 Asia/Singapore；权重 commit `1f5791a53e`“Release Agnes 2.5 Pro Theta”在 2026-11-15 02:47 UTC / 10:47 Asia/Singapore。likes 29 / downloads 537（采集 11-18 08:59 Asia/Singapore）；license apache-2.0，pipeline image-text-to-text。发布方是个人账号“Agnes”（不是组织，223 关注者）；AA 的模型列表里有“Agnes 2.5 Pro Theta”，creator 记为 Sapiens AI，releaseDate 2026-11-07，没有 Intelligence Index 分数。值得注意的是：它的 config 宽度 2560、每层 512 个路由专家取 top-10、hash 词表 248,320，与 Qwen3.8-Flash-Next（宽度 2560、512 专家 top-10、词表 248,320，约 180.0B）高度吻合，卡片却没有声明任何基座。是否基于 Qwen3.8-Flash-Next（其许可是 qwen-community-1.0，不是 Apache-2.0）待核；基准全部待核。[HF Agnes-AI/Agnes-2.5-Pro-Theta](https://huggingface.co/Agnes-AI/Agnes-2.5-Pro-Theta)
- **KORMo-VL/KORMo-Web-11B**：KAIST MLP 实验室的韩英双语网页 agent 模型，基于其从头预训练的 KORMo-10B 和 KORMo-VL，可以同时当 LLM、VLM 和浏览器 agent 用。createdAt 2026-11-14 11:23 UTC / 11-14 19:23 Asia/Singapore，但权重文件的 lastCommit `aa44345e62` 在 2026-11-15 04:42 UTC / 12:42 Asia/Singapore（窗口内），1 个文件 22.38GB，参数 11,191,119,728。likes 76 / downloads 26（采集 11-18 08:59 Asia/Singapore）；HF Trending #34；license apache-2.0，pipeline image-text-to-text，OSI 许可。自报 Online-Mind2Web 韩语任务成功率 30.1%、英语 29.0%（同表 GPT-6-luna 为 65.7/63.0），待核；卡片坦言自家 Qwen 底座的 4B/9B 版网页任务分更高。配套评测集见数据集 D3。[HF KORMo-VL/KORMo-Web-11B](https://huggingface.co/KORMo-VL/KORMo-Web-11B)
- **harness-hub/Qwen3.8-27B-pi-adapted**：给 Qwen3.8-27B 做的 LoRA（0.64GB），用 GRPO 强化学习专门适配 pi 编程 agent。createdAt 2026-11-16 06:52 UTC / 11-16 14:52 Asia/Singapore；lastModified 2026-11-17 08:33 UTC / 11-17 16:33 Asia/Singapore。likes 128 / downloads 0（采集 11-18 08:59 Asia/Singapore）；HF Trending #17；license apache-2.0（沿用基座）。自报 Terminal-Bench 2.1 从 39.5% 升到 55.8%、SWE-bench Pro hard 51 题从 29.4% 升到 62.7%，工具调用次数减少一半以上，待核（只测了 51 题）。卡片链接的 HF 博客 huggingface.co/blog/harness-hub/harness-adapters-at-scale 采集时返回 401（未公开），训练配方暂时看不到。[HF harness-hub/Qwen3.8-27B-pi-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted)
- **Edge0/Edge0-145B-NVFP4 / Edge0-120B-NVFP4（上期补记的后续）**：窗口内两个 repo 都补上了视觉编码器（11-15 12:22–12:25 UTC，mmproj-BF16.gguf，卡片说明来自 strata-vision 而非 Edge0 自有代码），120B 版另在 11-16 18:44–18:46 UTC 上传了 latent_dense q4/q8 文件。145B 版 likes 495 / downloads 61,591，120B 版 likes 43 / downloads 6,797（采集 11-18 08:59 Asia/Singapore）；HF Trending #18（145B）；license other（edge0-community-model-1.0），自定义许可，非 OSI。厂商数字仍待核。[HF Edge0/Edge0-120B-NVFP4](https://huggingface.co/Edge0/Edge0-120B-NVFP4)
- **Comfy-Org/PAN2（及 IFM/PAN2）**：IFM 的 PAN2 视频模型（29.2B，Apache-2.0）原 repo 在 11-05 发布、往期未收；本窗 ComfyUI 官方组织在 2026-11-15 10:44–10:50 UTC / 18:44–18:50 Asia/Singapore 上传了 ComfyUI 版（bf16 和 int8 两档，合计 124.51GB）。Comfy-Org/PAN2 likes 34 / downloads 6,288，IFM/PAN2 likes 218 / downloads 427（采集 11-18 08:59 Asia/Singapore）；IFM/PAN2 在 HF Trending #39。downloads 的差距主要因为 IFM 原 repo 直到 11-12 才把 library_name 设成 diffusers 以便计数。[HF IFM/PAN2](https://huggingface.co/IFM/PAN2) · [HF Comfy-Org/PAN2](https://huggingface.co/Comfy-Org/PAN2)

###### 补记：窗口前发布、往期漏掉的（不算本期新发）

- **n4ze3m/tiny-voca**：个人开发者从零训练的 4.5M 参数英文 TTS，两种音色，CPU 4 线程约 70 倍实时，训练数据是约 18 小时合成语音。权重 commit `5131e959f6` 在 2026-11-14 15:46 UTC / 11-14 23:46 Asia/Singapore（早于本窗，上期漏收）；窗口内加了 GGUF 和成本说明。likes 232 / downloads 3,042（采集 11-18 08:59 Asia/Singapore）；HF Trending #11；license apache-2.0，pipeline text-to-speech。训练数据是合成语音，来源模型的条款待核。[HF n4ze3m/tiny-voca](https://huggingface.co/n4ze3m/tiny-voca) · [GitHub n4ze3m/tiny-voca](https://github.com/n4ze3m/tiny-voca)
- **meituan-longcat/LongCat-Video-Avatar-1.6**：美团 LongCat 的音频驱动数字人视频模型升级版，主打口型更自然、超过 10 分钟的长视频不漂移。权重在 2026-11-13 05:19–05:20 UTC / 13:19–13:20 Asia/Singapore 上传，14 个大文件 63.8GB。likes 201 / downloads 489（采集 11-18 08:59 Asia/Singapore）；HF Trending #13；license mit。卡片自报 33,051 票人类偏好评测，对比 OmniHuman-2.0、HeyGen 等，待核。[HF meituan-longcat/LongCat-Video-Avatar-1.6](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.6) · [GitHub meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video)
- **maxwell-model/Maxwell-V1-Flash**：35B 总参 / 3B 激活的 MoE，256K 上下文，自报 26T token 预训练，强调东南亚低资源语言分词。repo 10-13 创建，但唯一的权重 commit `5a278bd2a1`“Initial commit”在 2026-11-13 13:40 UTC / 11-13 21:40 Asia/Singapore。73.63GB；likes 153 / downloads 287（采集 11-18 08:59 Asia/Singapore）；HF Trending #14；license apache-2.0。组织只有 1 个模型，背景不明，基准待核。[HF maxwell-model/Maxwell-V1-Flash](https://huggingface.co/maxwell-model/Maxwell-V1-Flash)
- **briaai/RMBG-3.0**：Bria 的第三代抠图模型，基于 Fibo-2.0-dev，8.1B 参数，16.25GB；gated: auto，权重文件 lastCommit 在 2026-11-10 19:40 UTC / 11-11 03:40 Asia/Singapore。likes 60 / downloads 0（采集 11-18 08:59 Asia/Singapore）；HF Trending #43；license other（bria-fibo），卡片写“RMBG-3.0 for non-commercial use”，非商用。卡片自报在 234 张难图上平均排名 1.51、优于 Photoroom 和 remove.bg，待核。[HF briaai/RMBG-3.0](https://huggingface.co/briaai/RMBG-3.0)

---

##### 数据集

- **D1. IQuestLab/RepoFactory**：200 个“从自然语言规格重建完整代码仓库”的可验证训练环境（Harbor 格式，含 Docker 镜像、oracle 实现和验证器），面向长程编程 agent；论文所述全集有 10,159 个环境，这次放出的是环境演化前的 200 个。createdAt 2026-11-16 11:11 UTC / 11-16 19:11 Asia/Singapore；lastModified 2026-11-17 07:19 UTC / 11-17 15:19 Asia/Singapore；likes 2 / downloads 81（采集 11-18 08:59 Asia/Singapore）；license 未填写，可否商用待核。[HF 数据集 IQuestLab/RepoFactory](https://huggingface.co/datasets/IQuestLab/RepoFactory)
- **D2. SWE-at-Scale/SWE-at-Scale**：用历史 bug 修复合成软件工程任务，2,955 个实例、53 个 Python 仓库（论文 arXiv 2610.21359）。createdAt 2026-11-16 14:53 UTC / 11-16 22:53 Asia/Singapore；lastModified 2026-11-17 14:42 UTC / 11-17 22:42 Asia/Singapore（v1.0）；likes 11 / downloads 155（采集 11-18 08:59 Asia/Singapore）；数据集 Trending #43；license apache-2.0。[HF 数据集 SWE-at-Scale/SWE-at-Scale](https://huggingface.co/datasets/SWE-at-Scale/SWE-at-Scale) · [arXiv 2610.21359](https://arxiv.org/abs/2610.21359)
- **D3. KORMo-VL 的韩语 GUI agent 评测集**：EVIDENT（220 条“证据核验式”GUI/网页任务，150 韩语 + 70 英语；createdAt 2026-11-14 16:33 UTC / 11-15 00:33 Asia/Singapore，license 未填写；likes 25 / downloads 110，数据集 Trending #15）以及 Ko-Online-Mind2Web、Ko-Screenspot、Ko-MultimodalMind2Web（三者 createdAt 2026-11-16 01:44 UTC / 11-16 09:44 Asia/Singapore，cc-by-4.0；likes 19/18/17，数据集 Trending #20 等）（采集 11-18 08:59 Asia/Singapore）。和次条 KORMo-Web-11B 配套，填补韩语网页 agent 评测空白。[HF 数据集 KORMo-VL/EVIDENT](https://huggingface.co/datasets/KORMo-VL/EVIDENT) · [HF 数据集 KORMo-VL/Ko-Online-Mind2Web](https://huggingface.co/datasets/KORMo-VL/Ko-Online-Mind2Web)
- **D4. SakanaAI/JFinBench**：Sakana AI 的日语金融评测，321 题，取自 2026 年六类日本金融资格考试（注册会计师、FP、税理士等），声称可随新考题持续刷新。createdAt 2026-11-16 04:59 UTC / 11-16 12:59 Asia/Singapore；lastModified 2026-11-16 05:46 UTC / 11-16 13:46 Asia/Singapore；likes 3 / downloads 303（采集 11-18 08:59 Asia/Singapore）；gated: auto，license other（jfinbench-source-terms），申请时要同意“只用于评测、不得用于训练、不得再分发”，非开放许可。[HF 数据集 SakanaAI/JFinBench](https://huggingface.co/datasets/SakanaAI/JFinBench)
- **D5. chimechallenge/chime5 + chime6**：CHiME 挑战赛官方组织把经典的家庭聚餐多通道对话语音数据（CHiME-6 约 50 小时、20 场、6 个 Kinect 阵列 + 双耳近讲麦）搬上 HF。chime5 createdAt 2026-11-16 12:01 UTC / 11-16 20:01 Asia/Singapore，chime6 createdAt 2026-11-16 15:46 UTC / 11-16 23:46 Asia/Singapore；likes 6/4，downloads 42/45（采集 11-18 08:59 Asia/Singapore）；元数据 license 都写 cc-by-4.0。值得一提的是：CHiME-5 早年需要签协议才能下载，现在 HF 标为 CC-BY-4.0，许可是否确实放宽、以官方文档为准，待核。[HF 数据集 chimechallenge/chime6](https://huggingface.co/datasets/chimechallenge/chime6)
- 附记：
  - AJ-Gonzalez/qwen4-max-reasoning-250x：通过 OpenRouter 收集的“Qwen4 Max”推理轨迹（不足 1K 条），license other，数据集 Trending #35；属于蒸馏闭源模型输出，有服务条款风险，降权不写入正文。
  - HubLabs/HubEgo-100K：就是上期提到的 Hubdata/HubEgo-100K，组织已改名，仍是 gated: auto，commits/README 返回 401，未绕过。
  - 数据集 Trending 前列（Vyber07/cyber-security、Angais/pixel-art-atlas-1.4m、nvidia/simready-assets 等）都是往期的延续热度；n4ze3m/tiny-voca 数据集（cc-by-4.0）见补记。

---

##### 榜单

- **B1. LMArena 文本**（WebFetch；curl 返回 403）：数据日期仍是 **Nov 11**，总票数 9,122,174、模型数 421，与上期完全一致，本窗**没有刷新**。#1 仍是 Gemini 4 Carbon (High)，1526±10，Prelim。本期保存了 WebFetch 返回的全表 421 行，供下期逐行比较。[lmarena.ai 来源](https://lmarena.ai/leaderboard/text)
- **B2. LMArena 视觉**：数据日期仍是 **Nov 8**，总票数 1,567,670 不变，但模型数 167 → **166**。与上期保存的全表逐行比对，唯一的变化是 **GLM-5V-Turbo 一行被移除**（上期 #72，1232±5，43,637 票），其余模型的分数和票数不变，排名顺延。官方没有说明原因。#1 仍是 Claude Fable 5 (High) 1309±7。[lmarena.ai 来源](https://lmarena.ai/leaderboard/vision)
- **B3. LMArena 文生图**：数据日期 Nov 12 → **Nov 16**；总票数 6,934,037 → 6,988,405；模型数 85 → 86。唯一新进的是 **MAI-Image-2.7**（微软 AI，闭源），直接排 **#4**，1387±12，3,082 票。#1 仍是 GPT-Image-2.5 Sunburst（1428±5）。开放权重里最高的仍是 Qwen-Image-2.1（#22，qwen-research 许可），MiniMax H3-Image 退到 #24。本期保存了全表 86 行。[lmarena.ai 来源](https://lmarena.ai/leaderboard/text-to-image)
- **B4. AA 文生图**（/image/leaderboard/text-to-image）：
  - 行数 114 → 116（解析口径与上期相同，含 FLUX.2 [dev] 锚点行）。
  - 新增 **MAI-Image-2.7** #4（1214±14，5,008 票）和 **MAI-Image-2.7-Flash** #11（1158±12）。
  - Kling Image 4.0 去掉“(preview)”后缀，现为 #7（1180±13），分数不变。
  - 榜首仍是 GPT Image 2.6 Sunburst (max)，1261±14。H3-Image #27（1066±14）。
  - [artificialanalysis.ai 来源](https://artificialanalysis.ai/image/leaderboard/text-to-image)
- **B5. AA 图像编辑**：
  - 新 #1 是 **MAI-Image-2.7**（1215±14，5,478 票），上期以“MAI-Image-2.7-Preview”名义在榜，本期改为正式名；与 #2 GPT Image 2.6 Sunburst (max)（1211±13）置信区间重叠。
  - 新增 MAI-Image-2.7-Flash #7（1179±13）、HiDream-O1-Edit-2.0 #26（1109±13）。Kling Image 4.0 同样去掉 preview 后缀（#6）。
  - 行数 84 → 86。H3-Image #14。
  - [artificialanalysis.ai 来源](https://artificialanalysis.ai/image/leaderboard/editing)
- **B6. AA Intelligence Index v5**（默认视图 28 个模型；v5 分数不能和 v4 比较）：
  - #1 仍是 Claude Fable 5.2 (Max) 64.6。
  - 新收录 **GPT-6.2 Astra (Max) 62.1**（#2）和 **GPT-6.2 Sol (Max) 57.3**（#5），releaseDate 都是 2026-11-17，闭源；它们取代了默认视图里的 GPT-6 Astra（56.9）和 GPT-6.1 Sol（54.6）。
  - 新收录 **Qwen4 Max 42.9**（#12），releaseDate 2026-11-16，闭源。
  - 开放权重前几名不变：Kimi K3.1 Pro 46.5 > DeepSeek V4.1 Flash 1017 32.6 > GLM-5.3 31.7 > Inkling 2 Small 30.6 > MiMo-V2.6-Pro 29.9。
  - 本窗新开放的 Sage S2.1 Flash、SenseNova-Loop-9B、Sarvam-105B-1711 都还没有 AA 记录。
  - [artificialanalysis.ai 来源](https://artificialanalysis.ai/models)

---

##### 延续热度 / 降权 / 冒名

- **Trending 前 10（模型，08:51 Asia/Singapore）**：
  1. MiniMax-H3-Image：跟进 F2。
  2. Qwen/Qwen3.8-27B：老模型。
  3. Haru-4B：跟进 F4。
  4. Lightricks/LTX-2.5：老模型。
  5. Inkling-2-Small：跟进 F1。
  6. unsloth/Qwen3.8-27B-GGUF：GGUF 分发，降权。
  7. Comfy-Org/MiniMax-H3-Image：H3 的 ComfyUI 分发。
  8. black-forest-labs/flux-3-image-klein-comfy：老模型。
  9. chatrlabs/Qwen-Image-2.1-Uncensored-Omni-Quantized：Uncensored 改包，过滤。
  10. DavidAU 的 Heretic GGUF：过滤。
- **窗口内更新但降权**：
  - xtools-at/DeepSeek-V4-Pro-Qwen3.5-4B-UNCENSORED-heretic（Trending #28）：Heretic 改包，过滤。
  - allenai/SERA-32B、arcee-ai 的 Trinity 系列、google/diffusiongemma-26B-A4B-it、baidu/Unlimited-OCR-2、ricursiveAI/Ripple-65B-Preview、KRAFTON/Raon-1-nano：窗口内只有 README、评测结果或采样参数改动。
  - inclusionAI 的 Duo 系列：只上传了 DCP 元数据和 README，downloads 仍为 0。
- **同名镜像 / 存疑 repo**（只按证据列出，不认定恶意）：
  - **Kimi K3.1 Pro 新增 4 个全量同名镜像**：kaitemoreau/Kimi-K3.1-Pro、10arjan/Kimi-K3.1-Pro、LagonPol/Kimi-K3.1-Pro、omegazug/Kimi-K3.1-Pro。
    - 创建时间 11-15 01:11 至 11-16 23:05 UTC。都是 112 个文件、1,561.36GB，license 元数据写 kimi-k3.1-pro，没有标注 base_model。
    - 每个都比对了根目录的 39 个 LFS 文件，sha256 与官方 39/39 一致，是原样复制。下载数 26–39。
    - 加上往期的 11 个，累计 15 个。
  - **MiniMax-H3-Image 同名复制件**：liumouren1314/MiniMax-H3-Image、Jinstudio/MiniMax-H3-Image、lichnew/MiniMax-H3-Image。
    - 文件数 100、总量 204.02GB，与官方完全相同；根目录唯一的 LFS 文件 sha256 一致，子目录权重未逐个比对（待核）。
    - downloads 242 / 247 / 0（采集 11-18 08:59 Asia/Singapore）。
    - 许可证（minimax-h3-image-community-license-agreement）允许在条件内再分发，但它们与官方同名，会干扰搜索，应引导读者用官方 repo。
    - 另有 nop60000/MiniMax-H3-Image：同名但内容是剪枝 + 量化后的 ComfyUI 打包（9 个文件、125.1GB），不是原样复制，降权。
  - **假冒“泄露权重”的 Gemini 4 repo**：salgr/Gemini-4-Carbon、salgr/Gemini-4-Argon、salgr/Gemini-4-Hydrogen（同一账号还建了 Neon、Krypton、Xenon）。
    - 创建于 11-16 07:42–08:03 UTC。卡片写“Gemini 4 Carbon 的权重今天被黑客 Salgr 泄露”，并打着“Official”标签。
    - 实际 safetensors 只有 156 字节；卡片自己描述的是一个只有 1 个参数的线性层（y = w·x）。
    - 属于借闭源模型名的恶作剧/冒名 repo，不要转发。Gemini-4-Carbon 有 5 个 like。
    - 对照：crosbylegal/gemini-4-carbon 等是 RedlineBench 的“结果卡”，卡片明说不含权重，不算冒名。
  - 合法转存，不算冒名：
    - yh742/Inkling-2-Small 和 omegazug/Inkling-2-Small：26/26 一致。
    - omegazug/Inkling-2-Small-MXFP8：44/44 一致。
    - 以上都是 Apache-2.0，允许转存。
    - drawthingsai/Inkling-2-Small 目前只有 LICENSE 和 README，是空占位。
    - TechnoBaptist/FastFrames-L：文件数 20、总量 173.55GB，与官方相同，但根目录没有 LFS 文件可比对，所以未做哈希比对。它照搬了 apple-amlr 许可；AMLR 允许在研究用途内分发，但要附带许可，是否合规待核。
  - 证据：（采集证据快照）、（采集证据快照）、（采集证据快照）

---

##### 口径 / 缺口 / 校验

- 采集方式：
  - HF API：trending（模型 300 条、数据集 100 条，外加 trending HTML 页）。
  - 约 110 个重点组织按 lastModified 扫描，得到 70 个窗口候选。
  - 按 createdAt 全量分页扫描：模型 11 页，窗口内 10,932 个；数据集窗口内 5,937 个。
  - 另外按名称搜索衍生 repo 和同名 repo。
  - 每个候选 ID 都抓了 api、commits、README、tree 和 `?blobs=true`；递归 tree 在 50 条处截断，体积以 blobs 为准。
  - AA 首页、模型页、两个图像榜和 Kimi 页用 curl 保存 HTML 后解析。urllib 首次请求时 TLS 失败，改用 curl 重试成功。
  - LMArena 用 WebFetch 读，三个榜都保存了全表，读取时间 11-18 约 08:54–08:56 Asia/Singapore。逐行比对脚本：（采集证据快照），结果：（采集证据快照）。
- 缺口：
  - 以下 401 没有绕过：sensenova/SenseNova-Loop-9B、briaai/RMBG-3.0、mehdi-hf/cilla-mini 的 commits 和 README（都是 gated: auto）；SakanaAI/JFinBench、HubLabs/HubEgo-100K、laion/laion-audio-xl 的 commits 和 README。
  - harness-hub 的 HF 博客链接返回 401，未写入外链。
  - FastFrames 论文 arXiv 编号未出。
  - Sage S2.1 Flash 的激活参数量没有官方数字。
  - AA 总收录数：本期按页面 slug 计数，与上期口径不同，不做对比。
- 校验：素材中出现的每个 HF ID 都单独请求了 API（数据集走 datasets API），结果见 （采集证据快照）。外链检查见 （采集证据快照）：LMArena 三个页面 curl 返回 403，但 WebFetch 读取正常；其余外链都返回 200，没有 404。

