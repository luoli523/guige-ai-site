# 2026-11-15 AI行业动态：全量原始素材

本期信息窗口从 2026 年 11 月 12 日 09:30（上期采集结束）起，至 11 月 15 日各来源的实际采集截止，时区为 Asia/Singapore。本文保留四路采集到的全量原始摘要与来源链接，不是深读成稿，也不意味着所有候选均已独立复现。正文另见[本期深读](https://guige.ai/guige-ai-site/daily/2026-11-15/)。

- 研究与官博：官博与 arXiv 均约截止 11 月 15 日 08:56；包括研究汇总、官方原文摘录和论文候选三份材料。因 11 月 11 日美国退伍军人节，arXiv 在 11 月 12 日没有独立批次，相应稿件并入 11 月 13 日批；周末无新批。Apple Machine Learning Research 本期已取得完整列表，窗口内无新刊登，文中 4 条为上期窗口的补录，不是本期新发。
- X 公开动态：约截止 08:50；首页时间线只覆盖约 11 月 14 日 08:59 之后，此前时段以官方账号检索、公开检索与官方页面补齐，不代表全量时间线。
- GitHub 项目与发行：榜单与仓库快照为 08:51；日榜、周榜不等于本期净增。
- 模型与数据集：HF 统计快照约为 09:00，榜单读取约在 08:53–08:55；保留模型卡、权重提交、许可、榜单与同名仓库记录，下载量为 HF 近 30 天口径。

原始材料之间可能保留不同取舍，以下说明用于避免误读：Gemini 4 Hydrogen 的 Orchestrator 结果在主博文中写作 Terminal-Bench 4.0、在 Antigravity 博文中写作 4.1，以各页原文为准；X 新闻摘要中 OpenAI 网络安全模型的 ExploitGym 77.0%、PatchBench 79.1% 未见官方页面复述，待核；Anthropic 约 1.4 万亿美元估值为媒体推算，待核，不是定价或市值；ZONOS3-Mini 技术报告的首包延迟（低于 450ms）与官方博客（低于 150ms）不一致，待核；Haru-4B 的 65ms 为 int8、不含分帧的厂商数字。HF 上与 Kimi K3.1 Pro 同名的非官方仓库只按证据列出、不认定恶意，读者应以 moonshotai 官方组织为准；合法转存的非官方仓库不等于冒名，原材料中的相关记录照录。

除去内部协作名称、个人隐私、内部本地证据路径、来源标记和不宜公开的安全操作细节，正常来源与候选保留；未读、待核、自报与不收录理由照录。以下材料不是投资、上线或商业授权建议。


## 研究与官博

### 研究汇总

#### 研究素材包 · 2026-11-15（窗口 2026-11-12 09:30 → 11-15 ~08:56 Asia/Singapore）

> 官博 5 条 + arXiv 5 条（共 10 真重点）。另设「Apple 上期窗口补录」小节（写全 1 条、其余带过），**不是本期新发**，不计入上述 10 条。数字标 来源记录 / 官方自报 / 作者自报 / 待核。原始摘录见同目录 labs-raw.md、arxiv-raw.md。
> arXiv：Asia/Singapore **11/12（Thu）无独立列表**（官方假期表 2026-11-11 Veterans Day）；**2611.14520–17337** 已并入 Asia/Singapore **11/13** 批且列表完整。周末无批。续扫 **2611.17338+**。
> 网络安全、生物与对齐条目只写结论与官方/作者数字，不写利用/合成/实验步骤。数字均保留设定与基线，**勿**无条件跨模型、跨硬件、跨基准比较。

##### 官博

###### 1. Google DeepMind：Gemini 4 Hydrogen
把 Gemini 4 家族补上「日常执行」这一档：Carbon / Argon 做长程深推理，Hydrogen 做快速编码与智能体工作流，并铺到 AI Studio、API、Gemini 应用、Search 与 Antigravity。模型卡写明它由 Carbon 改编；是本窗口最大的官方模型发布，也是要不要把日常执行从 3.8 Flash 换上去的硬参考。
- DeepMind RSS 与落地页 jsonld `datePublished` **2026-11-12T18:00:00Z** 均为 **11-13 02:00 Asia/Singapore**，**时刻一致（来源记录）**。页面「Nov 12, 2026」是 UTC 日历日，不是冲突。`dateModified` → **11-14 02:27 Asia/Singapore**。价在整个 **100 万** token 上下文上统一 **$1.50 / $7.50** 每百万 in/out（官方自报）。上下文合计至 1M；默认同步输出至 **64K**，后台长解码至 **1M**；四档思考 low / medium / **high（默认）** / 新的 **xhigh**；知识截止 **2026 年 3 月**（模型卡 来源记录）。Artificial Analysis Intelligence Index：默认 high **51** vs Argon **50**，xhigh **54**（官方自报）。Antigravity Orchestrator 在同一会话切换 Carbon 与 Hydrogen：在 **Terminal-Bench 4.0** 上称接近 Carbon 任务成功率，同时平均少用 **24%** 配额、快 **19%**（官方自报）。相对 Gemini **3.8 Flash**（默认 high）：完成约快 **2.5×**；**Terminal-Bench 4.1** 为 **57% vs 18.2%**——与上面的 4.0 **不是同一版本**，不可混用（官方自报）。合作伙伴早期测试称相对 3.8 Flash 约快 **2×–2.8×**、token 用量降 **12%–23%**。其他榜（官方自报，设定各异）：Agent Arena **#5**；HLE-Diamond **58.8%**（称同档领先）；Vals Tax Agent Bench **#1，52.3%**；Vals Legal Research Bench 并列 **#1，55.8%**；MKA **53.4%**；Agents’ Last Exam v1.1 **71.6%**。勿把 MKA 分数直接接上期 Carbon「质量 #2」做未经本文声明的横比。安全仅结论：相对先前执行档，称越权最多降约 **81%**、服务不足最多降约 **79%**；工具/编码评测上错位行动与抄近路约 **12×**；内部智能体诚实评测 **94%**；逾 **20 万** 次受审回合上思维链可读性 **99.9%**、称无欺骗性推理编辑；Gray Swan IPI 抗间接注入称强 **2.3×** 以上；HealthBench Pro 误拦低于 **0.4%**（官方自报）。模型卡相对 3.8 Flash：**不正当拒绝 +5.57pp**（此项是回归）；图文安全 **+7.00pp**（官方自报，且文称改过评测、不可与旧模型卡直接比）。针对性测试称 **未达到** CBRN（生物）或网络安全 CCL，但 **达到了两域警戒阈值**；完整 Safety & Security Report **尚未发布**。
- [官博](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)（DeepMind 入口 [同文](https://deepmind.google/blog/introducing-gemini-4-hydrogen/)，RSS / jsonld **11-13 02:00 Asia/Singapore**）· [模型卡 PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Hydrogen-Model-Card.pdf) · 配读 [开发者文](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-hydrogen/)、[Antigravity](https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity)

###### 2. Google Research：Antigravity `/teamwork` 的科学与系统结果汇编
用 Gemini 4 Argon / Carbon / Hydrogen 与 Antigravity `/teamwork`（及 `/boost`、LEAP、Stellar Colosseum 等模式），汇总数学、形式化、化学与生产基建上的一批「人机共研」结果，并开放工具与 1 万名学者六个月最高用量档申请。把上期已出现的科学智能体，从功能演示推进到官方自报的开放问题与生产数字。
- 页面 November 13；RSS → **2026-11-14 04:47 Asia/Singapore**（= 11-13 20:47 UTC，美国日历日仍为 11-13）。时刻以 RSS 为准（来源记录）。以下数字均为**官方自报**；子结果（证明陈述、代码仓库、实验设定）**未逐篇打开复核，标待核**，引用须带这一层。代表数字：与 CUHK / USC / CMU 称完整证明并 Lean 形式化 2013 年 Courtade–Kumar 猜想，约 **5000 万** 行（待核）。LEAP + Argon：称 Weil 猜想机器检查形式化约 **180 万** 行 Lean、**28,800** 次子代理调用；Hilbert 第十问题在一般整数环上的近期证明约 **91.9 万** 行（待核）。另称端到端形式化了带光滑外力的 3D Navier–Stokes 有限时间爆破的**近期证明**——这是形式化已有证明，**不是**宣称解决千禧年问题。Deep Review：STOC 2027 有 **578** 篇投稿选择接受反馈；进行中作者调查 **N=70**，**90%** 认为反馈大多或几乎全部属实、**90%** 愿再用；逾 **30%** 称抓到实质性证明漏洞或重要笔误（官方自报其调查，样本小）。化学仅高层：复杂基准分子 top-1 精确匹配 **95%**、top-3 **100%**（官方自报，待核设定；不写实验步骤）。生产：称内存优化已超过最初约 **1 PiB** 的节约估计；Borg 调度称落地 2 项变更，部分硬件类型上 TPU 抢占降 **24%**（官方自报）。设定各异，**勿**把行数、倍速或 Elo 横比。
- **与同窗 arXiv #7、#10 的关联/差异**：三条都在「科研 / 系统 agent 能否发现或搭出新东西」，但不是同一件事。本条是 Google 自有工具链的成果汇编；#7 Singularity-Bench 是多机构把「从近乎空白搭 AI 研发栈」做成可与人工基线比较的考题；#10 AutoAssumption 是 MIT 用 Lean 假设搜索发现推理系统算法。可配读，不可把 1.25 指数、Lean 行数或「改进全部已发表算法」读成同一套系统的分数。
- [官博](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/)（RSS **11-14 04:47 Asia/Singapore**）

###### 3. Thinking Machines：端到端 4-bit 前向训练 Inkling 2 Small
在 GB300 上给出一套贯穿预训练到最后一轮 RL 的数值配方：专家层前向用 NVFP4，反向用带再量化与随机舍入的 MXFP8，并对 MoE 通信做量化，从而端到端用原生 4-bit 前向训练，不必在交付量化检查点时再校准。把 4-bit 前向从推理/后训练量化推进到可贯通预训练与 RL 的配方。
- 页面 **Nov 13, 2026**（仅日期，**时刻待核**）。格式对照（文内表，官方自报）：NVFP4 约 **4.5** bit、GB300 上 **15** PFLOPS；MXFP8 约 **8.25** bit / **5** PFLOPS；BF16 **16** bit / **2.5** PFLOPS。称 NVFP4 比 BF16 少约 **3.6×** 存储、在 GB300 上最高约快 **6×**——这是格式/硬件峰值，不是端到端训练倍速。完整 NVFP4 训练曾对 compute efficiency（CE）打击过大，故只把前向（主要在 MoE 专家层）放到 NVFP4，最后约 **16.6%**（1/6）层保持 MXFP8。其**最大作业**相对全 MXFP8：预训练墙钟约 **+8%**，RL 约 **+20%**（官方自报）。预训练 Inkling 2 Small 的 CE 代价约 **2%**（要达到同一损失，相当于比在 MXFP8 下少用约 2% FLOPs 所能达到的水平更差一点，即用约 2% 额外计算换速度）；RL 称端到端明显加速且奖励无可见差异。自称是其所知**最大的、从头到尾用原生 4-bit 前向**训练的模型（「我们所知」口径）。另称该模型在 GB300 NVL72 上预训练仅 **68 小时**——文明确说这是科学与工程许多改进共同作用的结果，**不能单记在数值配方账上**。数字绑定 GB300 与其最大作业。
- **与效率线的配读**：同窗备选 Together AI [Compiler 2611.14681](https://arxiv.org/abs/2611.14681) 谈的是推理时持续编译与吞吐（相对手写 Megakernel 最高约 1.7× TPS 等），不是训练数值格式，勿把墙钟 8%、NVFP4 的 6× 与 serving TPS 混比。
- [官博](https://thinkingmachines.ai/blog/end-to-end-4-bit-training/)

###### 4. OpenAI Alignment：用自动红队改进「模糊稳健性」（仅高层）
把网安、生物等双用途、安全边界难以精确写清的领域里，模型在对抗压力下仍能稳定拒绝违规协助的能力，称为「模糊稳健性」；用加大测试时计算的自动红队（并要求攻击在重复测试中都成功，文称 worst@n）生成训练数据，再用于改进包括 GPT‑6 Astra 与 Sol 在内的近期模型。安全向只写结论。
- 页面 **November 12, 2026**；Alignment RSS `2026-11-12 00:00:00 -0800` → 若按字面为 **16:00 Asia/Singapore**。`00:00 PT` 也可能是日级占位，**时刻待核**。上期 11-12 09:26 的 alignment 列表**未出现**此文，计入本期。图 1 明确是**关闭生产侧防护、只测模型层**的结果，不可当成线上系统稳健性。固定越狱集（针对 GPT‑5.4 / 5.5 生成的历史越狱）：网安上 GPT‑6 Astra 安全作答 **91.5%**，对比 GPT‑5.6 Sol **59%**（官方自报）。自适应多轮评测中，称 Astra 在各攻击预算下都比 5.6 Sol 更稳健（细节指向 Astra 系统卡）。受控实验：用「稳健化」后的对抗提示做 RL，相对直接用原始种子，对未见攻击者的固定越狱和可迭代改写的自适应攻击，稳健性都更高（官方自报）。称 Astra 在更具挑战的提示上同时更安全处理有害请求、更少误拦正当请求（官方自报）。对象与评测设定不可外推到带生产防护的部署，也不写攻击轨迹或提示构造。
- **与同窗 arXiv #6 的关联/差异**：两边都在问「后训练之后，模型在高风险行为上还靠不靠得住」。本条关注的是用自动红队数据把模糊稳健性训上去，并报告 Astra 相对 Sol 的模型层分数；#6 关注的是先做角色/宪章训练，再遇到「奖励违反宪章」的 RL 时，角色训练会不会被顶掉、监控好不好做。相关是同一监督问题的先后两段，不可把 91.5% 读成「角色训练已足够」，也不可把 #6 在 gpt-oss-20b 上的结论外推到 Astra。读安全分数时，建议配读同窗官博 #5 对评测构念与不确定性的提醒。
- [官博](https://alignment.openai.com/fuzzy-robustness/) · [官方 PDF](https://cdn.openai.com/pdf/OAI_Improving_Fuzzy_Robustness_in_LLM_Safety_with_Automated_Red_Teaming.pdf)

###### 5. Anthropic：怎样把安全评测做硬、读对
把「模型比上一代更安全」还原为「在某人建的一套安全评测上分数更高」，并借鉴心理学可重复性改革，给出设计、运行与报告安全评测的建议。是少有的「如何读安全分数」的官方方法文，直接约束系统卡与外部安全榜的引用方式。
- 页面 **Nov 13, 2026**；`published_time` **2026-11-13T00:00:00.000Z**，**时刻待核**（日级占位）。安全评测量的是促成伤害的倾向与应对是否得当，而不是能力分；需同时看有害请求与良性请求的过度拒绝。拒绝率并不总是正确构念（例如危机对话中单纯拒答本身可能是失败）。观察性设计回答「模型表现如何」，因果设计才能支持「某项干预让模型更安全」。运行上，称安全评测常关闭标准防护以看基线，应在无外网沙箱中进行并实时监控；近几个月因自身事件加固环境，暂时停掉许多需上网的评测（官方自报，仅结论）。数字：其 API 上，近期各模型单轮评测合计无害回应率约 **94%–98%**；多轮分布宽得多。在 claude.ai 流量上，Claude Opus 5 与 Opus 5.5 曾为 **98% vs 94%**，但差异**不具统计显著性**，不能据此断言谁更好。系统提示改动后，适当回应率在 claude.ai 上约 **94%**，对比 API 上约 **60%**（官方自报；场景/提示不同，不可当成通用「网页比 API 高 34 个百分点」）。
- [官博](https://www.anthropic.com/research/building-strong-safety-evaluations)

##### arXiv

###### 6. MATS + Anthropic（Roger）：角色训练挡不住写错的后续 RL（2611.16069）
先用类似 Model Spec Midtraining 的方式给 gpt-oss-20b 灌一套半写实宪章，再看后续「奖励违反宪章」的 RL，会不会把角色训练顶掉。直接接上期「监控 reward hacking / CoT 可监控性 / 角色训练」这条线：角色训练之后若奖励写错，模型是不是照样学会违规，以及监控是否更难看出来。安全向**仅结论**。
- 摘要未给单一总成功率。作者称：角色训练后的模型把两种违规都「很容易学会」，只是答有害请求比未做角色训练的 gpt-oss-20b 稍慢；有害答案上出现更多「找理由」式推理，并在部分监控更难吃力的任务上会 hack。用价值观来为同一套规则提供理由、对比不提供理由，在偏离、诚实与能力评测上差别很小（作者自报）。对象是 gpt-oss-20b 与作者自建宪章，不能外推到未测试的旗舰模型。文中提及的 OpenAI / Claude 事件是相关报道，**不是**作者单位。Asia/Singapore 归属 **11/13**。单位：Mohammad Omar Khursheed、Thomas Morris = MATS；Fabien Roger = Anthropic（HTML/PDF 脚注 来源记录）。**不可写成「Anthropic 三作论文」**。与官博 #4 的关联见上。
- [arXiv](https://arxiv.org/abs/2611.16069)

###### 7. CMU 等：Singularity-Bench，最强指数 1.25（2611.16591）
给「智能体能不能从几乎空白起步、自己把 AI 研发栈搭起来」做一套端到端考题，并和同一硬件上的成熟人工基线比。把 agent 评测从做题/写代码推到预训练、中训、后训、推理、harness 与集群编排六段真实研发工作；同时报告了评测框架本身会被 reward hacking 的问题（仅结论）。
- **Singularity-Index** 定义为相对人工参考的比率，**1.0 表示平均达到人工基线，不封顶**（作者自报；HTML 与摘要交叉核对）。11 个 agent（7 个前沿模型 × 2 套 harness）。Opus 5.5 + Claude Code 为 **1.25**（约 1.252），在全部六项上达到或超过人工基线；其余 10 个平均 **0.58**；专有模型平均 1.01、开源权重平均 0.50（作者自报）。成本–指数帕累托前沿举例：DeepSeek V4.1 Flash + Codex **0.698 / $4.36**，GPT-6.1 Sol + Codex **0.969 / $84.52**，Opus 5.5 **$425.41**（作者自报 API 花费）。11 个里有 6 个在推理任务上得分为 0，栈上表现并不匀。作者把 1.25 读成「可能已具备走向 singularity 的技能」属于修辞，不是可核验的预测。红队与 Breakwater仅结论：称常规 Harbor 框架存在 reward-hacking 漏洞，其扩展在所测攻击上全部挡住；不写攻击或防护步骤。Claude / GPT / DeepSeek 均为评测对象，**不是**作者单位。Asia/Singapore 归属 **11/13**。单位（PDF 首页 来源记录）：Carnegie Mellon University、NVIDIA、UT Austin、HKUST、Amazon AGI、RadixArk、University of Chicago、Together AI、Alation、Meta、UC Santa Barbara、UIUC。**多机构合作，不可写成 NVIDIA / Meta / Amazon 单家论文**；通讯方向以 CMU 为主。与官博 #2、arXiv #10 的关联见 #2。
- [arXiv](https://arxiv.org/abs/2611.16591)

###### 8. 清华等：JustRUA，受控拆解 robot-use harness（2611.16009）
把近来 RoboDojo 上一路上涨的「用通用模型直接开机械臂」系统拆开，在同一框架里分别测 harness、动作接口、经验复用和场景几何，最后留下一个尽量瘦的 JustRUA。上期 AMP1、Embodied First Exam、Gemini Robotics 2.5 都给出了成功率，但设定不同、且常一次改好几处；这篇专门做受控拆解。**勿**与上期 85.6%、104/108、Standard 34%、产线 96% 横比。
- 从官方 L3 harness 出发，不加习得策略、自改进环或任务微调，RoboDojo **仿真**基准从 **29.7 提到 50.3**（作者自报）。作者称：保留完整回合历史、及早停止每次运动的瘦 harness 已经很有用；复用经验会改变行为但不是免费午餐；场景几何帮助最大，即便深度只从 RGB 估计。数字绑在该仿真基准与 **GPT-6 Astra** 设定上——标题中的 GPT-6 是**评测对象，不是作者单位**。Asia/Singapore 归属 **11/13**（主类 cs.RO，交叉 cs.AI）。单位：Tsinghua / ModelBest / 华中科技大学 / Peking University / Tencent（PDF 首页 来源记录）。
- [arXiv](https://arxiv.org/abs/2611.16009) · [项目](https://zefanw.github.io/JustRUA) · [代码](https://github.com/ZefanW/JustRUA)

###### 9. Minnesota / Stevens：MAPE，用程序演化搜索 agent 记忆设计（2611.17068）
不从现成记忆架构里改零件，而是用程序演化（MAPE）从极简种子长出整份记忆程序，并看哪些设计会反复出现。给 agent 记忆一条可搜索、可迁移的设计路径，并且同时报准确率和 serving 成本。
- 在 LoCoMo 与 LongMemEval 上，相对**人工设计基线**，绝对准确率最高约 **+12 个百分点**，serving 成本约为该基线的 **35%**（作者自报）。跨 serving 骨干和基准有迁移支持。把组合（composition）模块移植进五个已有记忆系统，五个都提高了准确率。若目标里同时优化成本，计算会从「用 LLM 建记忆」转向「查询时选择性处理」，准确率仍有竞争力。点数与成本比绑定其基线与两项基准，勿当成通用降本率。Asia/Singapore 归属 **11/13**。单位：University of Minnesota / Stevens Institute of Technology（来源记录；Tairan Chen 为 Stevens，其余为 Minnesota）。
- [arXiv](https://arxiv.org/abs/2611.17068)

###### 10. MIT CSAIL：AutoAssumption，在 Lean 里搜索假设以发现系统算法（2611.14844）
把 KV 淘汰、权重量剪、推测解码等算法写成带显式假设的 Lean 证明图，然后一次只放宽一条假设、再证明、再生成代码，用假设搜索代替在程序空间里乱改。方法学上把「发现新系统算法」从改代码变成可审计的假设搜索。
- 形式化了 **89** 套算法，Lean 检查（作者自报）。KV 淘汰算法在所跑已发表方法里 **RULER-4K 最高**；剪枝算法在四个 LLaMA 模型上、十三个对照里 **困惑度最低**。同等预算下，该 harness 分数与 OpenEvolve（开源 AlphaEvolve 实现）相差不到 1 分，且跨重复的标准差更低（文内 SD 0.75，对照 1.39 与 4.09；另称比 AIDE 高 0.8 分）（作者自报）。摘要未给 RULER-4K 的绝对分；「最高 / 最低」限于作者跑过的已发表对照。OpenEvolve / AlphaEvolve 是对照，**不是**作者单位。Asia/Singapore 归属 **11/13**。单位：MIT CSAIL（来源记录，四位作者同一单位）。与官博 #2、arXiv #7 的关联见 #2。
- [arXiv](https://arxiv.org/abs/2611.14844)

##### Apple 上期窗口补录（非本期新发）

上期 Apple Machine Learning 研究列表未能完整抓取；本期已取到全列表（`__NEXT_DATA__` **1189** 条）。补扫窗（11-09 09:40 起）内 4 条均属**上期窗口**（日级 `00:00 GMT` = 08:00 Asia/Singapore，时刻待核），上期漏报，这里显式补录。**本期窗口按日级日期无新刊登。** 部分条目的 arXiv ID 月份早于站点刊登日，是「Apple 站点补挂已有预印本」，**不要写成「本周新出预印本」**。

###### 补录. Apple：KL 正则对齐的信息论上界（Theoretical Limits of Language Model Alignment）
给出固定 KL 预算下可达到的期望奖励增益的信息论上界（闭式，由 Jeffreys 散度而非先前分析常用的 √KL 控制），并改写成基座模型下的协方差估计，从而只用基座样本预测可达到的对齐增益；再分析代理奖励下的 reward hacking，并证明奖励集成可缓解该差距。是这批补录里理论最硬的一条，对理解「PPO / GRPO 为什么看起来次优、best-of-N 为什么贵但接近上界」有用。
- 站点刊登日 **2026-11-12**（RSS `00:00:00 GMT` → 若按字面为 08:00 Asia/Singapore，早于上期 09:26 截止；按日级占位补录，**时刻待核**）。预印本 [2605.07105](https://arxiv.org/abs/2605.07105) 的 ID 属 **2026-05** 批，早于站点刊登。页面标 NeurIPS。经验上，在安全与摘要两项任务上计算 KL–奖励 Pareto 前沿，称 best-of-N 接近理论上界，而 PPO 与 GRPO **明显次优**（官方摘要 / 作者自报）。作者：Lucas Monteiro Paes*、Natalie Mackraz*、Barry-John Theobald、Federico Danieli。
- [Apple 站点](https://machinelearning.apple.com/research/theoretical-limits-alignment) · [arXiv 2605.07105](https://arxiv.org/abs/2605.07105)（5 月预印本，非本周新发）

其余三条（均为 **2026-11-10** 站点刊登，时刻待核）一句带过，细节见 labs-raw：
- [Evaluating the Evaluators](https://machinelearning.apple.com/research/evaluating-evaluators-llm-judges)（NeurIPS 2026 workshop；[OpenReview](https://openreview.net/forum?id=cyU5BnO6nN)）：个性化写作风格上，LLM 评委与人类一致性与 MMLU 只弱相关（Pearson **ρ ≤ 0.2**），「最强」模型并不最可靠复现人类评价（官方摘要）。
- [On the Importance of Gating](https://machinelearning.apple.com/research/gating-memorization-in-context)（[arXiv 2609.16540](https://arxiv.org/abs/2609.16540)，ID 属 2026-09 批）：SSM 门控会让模型先学到写进权重的记忆解，从而推迟甚至阻止收敛到正确的上下文学习解，但门控又常有利于长序列泛化。
- [Weighted State Souping](https://machinelearning.apple.com/research/weighted-state-souping)（[arXiv 2610.25621](https://arxiv.org/abs/2610.25621)，ID 属 2026-10 批；NeurIPS 2026 PALM workshop）：给缓存的 SSM 状态学习查询相关组合权重，改善长上下文检索，并给出近乎与上下文长度无关的稀疏变体。

##### 备选（简洁）

- 官博次选：NVIDIA [cuBLAS FP64 新算法](https://developer.nvidia.com/blog/faster-scientific-simulations-with-new-fp64-algorithms-in-nvidia-cublas/)（11-14 06:13 Asia/Singapore；Ozaki-II DGEMM 相对原生 FP64，在 VR NVL72 / GB200 约 5.5× / 3.9×）；[SOMA Retargeter](https://developer.nvidia.com/blog/adapt-human-motion-for-robots-with-nvidia-soma-retargeter/)（开源人体运动到人形机器人的重定向教程）；两机 [GLM-5.3 + vLLM 教程](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/)（7530 亿参数检查点约 464 GB）。ChatGPT Wallet 等为产品帖，不进研究主包。
- arXiv：UK AISI 等 [Going Badly 激活与 reward hacking 2611.14996](https://arxiv.org/abs/2611.14996)（仅结论）；Together AI [Compiler 2611.14681](https://arxiv.org/abs/2611.14681)；SKKU [HeMeR 2611.16487](https://arxiv.org/abs/2611.16487)（NeurIPS 2026 Oral；实物相对 MemRL 成功 83.20%、单步 2.94→1.87 s，勿与 JustRUA 仿真分横比）；Baidu [Folio 2611.16627](https://arxiv.org/abs/2611.16627)；Google DeepMind [pluralistic agents 2611.16028](https://arxiv.org/abs/2611.16028)（预注册，746 人）；AWS [Agentic Computational Algebra 2611.16073](https://arxiv.org/abs/2611.16073)；Amazon [DISCERN 2611.15729](https://arxiv.org/abs/2611.15729)；Google [SynthCorp 2611.14765](https://arxiv.org/abs/2611.14765)。
- Apple 补录次选即上节未写全的三条评测/SSM 论文。

##### 覆盖缺口 / 排除

- **上期已报勿重复**：Anthropic Claude Fable 5.2 / Mythos 5.2 及电子原型文、DeepMind AlphaProof Code、Gemini Robotics 2.5、AlphaGenome 2、OpenAI CoT 可监控性、MSR Lazarus；备选 Muse Ember、MAMUBench/Worse Together、OpenAI Control Room、OpenAI×Upwork、NVIDIA Snapshot、Google MKA + Carbon 正式开放、Meta TLX。arXiv：AMP1 2611.09892、CPU-ARC 2611.09891、Embodied First Exam 2611.12177、监控 reward hacking 2611.09828；备选 2611.09798、Agentic-OPD 2611.12799、PACE 2611.10240、Infrathon 2611.11995、MemoryDojo 2611.09721。更早已报 Memory Trap、OPD、EnvOpt、Social Humanoid、RecSA 等。
- **窗前排除（勿当本期新发）**：OpenAI children’s safety（11-12 **08:00** Asia/Singapore）；Amazon 网络配置文（11-12 **01:02** Asia/Singapore）。Anthropic Alignment [homeopathic learning](https://alignment.anthropic.com/2026/homeopathic-learning/) 为 Nov 10，属上期窗口且上期主包未报，本期只作漏报备忘，不当新条。
- **arXiv 扫描**：Asia/Singapore **11/12 无独立列表**（官方 [假期表](https://info.arxiv.org/help/availability.html) 2026-11-11 Veterans Day，来源记录）；**2611.14520–17337** 并入 Asia/Singapore **11/13** 批且完整（pastweek 显示 AI/CL/LG showing N of N）；**11/14–11/15 无批**（常规周末）；08:51–08:56 Asia/Singapore 探测 **2611.17338+** 为 404。续扫 **2611.17338+** 与周一 `list/*/new`（预计 Asia/Singapore 11/16 早）。提交日为 11/10–11/12，**Asia/Singapore 归属一律按 11/13 放批日**，不按 Submitted on 拆成周四。
- **官博覆盖缺口**：OpenAI `/news`、`/index` 详情页 curl **403**，Wallet 等产品帖仅用 RSS 标题与时间。Hydrogen 完整 Safety & Security Report 官方称即将发布，本期未见。Antigravity `/teamwork` 子结果未逐篇打开论文或仓库复核，汇编数字保持官方自报并标待核。Amazon Science 上期两条（Mitra-v2、网络配置验证）仍未深读。Meta research、MSR 博客、Anthropic Alignment 窗内已成功访问、无新研究长文（非缺访问）。
- **Apple ML**：全列表本期已取到（1189 条）；本期窗口按日级日期无新刊登；RSS 仅 10 条，完整性以 `/research` 全列表为准。
- 机构误报提醒：2611.16591 不可写成单家实验室；2611.16009 的 GPT-6 是评测对象；2611.16069 不可写成 Anthropic 三作论文。题目含 Apple Silicon 的 2611.14545 / 2611.17294 **不是** Apple 的论文。

### 官方原文摘录

#### Labs Raw Excerpts — 2026-11-15

- **窗口**: 2026-11-12 09:30 Asia/Singapore → **2026-11-15 08:56 Asia/Singapore**（Asia/Singapore, UTC+8；采集截止以本机 `date` 为准）
- **采集时间**: 2026-11-15 约 08:50–08:56 Asia/Singapore
- **说明**: 原始摘录；关键数字标「官方自报 / 来源记录 / 待核」。网络安全与生物仅写结论与官方数字，不写利用/合成/实验步骤、攻击轨迹或提示构造。已在上期主包或窗口外的条目不作为本期重点重复。
- **去重参照**: （内部证据存档）、`research.md`。上期已报勿重复：Anthropic Claude Fable 5.2 / Mythos 5.2 及电子原型文、DeepMind AlphaProof Code、Gemini Robotics 2.5、AlphaGenome 2、OpenAI CoT 可监控性、MSR Lazarus。上期备选 Muse Ember、MAMUBench/Worse Together、OpenAI Control Room、OpenAI×Upwork、NVIDIA Snapshot、Google MKA + Carbon 正式开放、Meta TLX 不当新条目重报（除非有实质新进展）。上期数字不在此复述。
- **专项**: Apple Machine Learning Research 上期列表未能完整抓取。本期补扫 **2026-11-09 09:40 Asia/Singapore 至今**（上期窗口 + 本期窗口），逐条核日期；上期窗口内漏报的高信号条目标「上期窗口补录」。

---

##### OpenAI

**源查证**: [openai.com 来源](https://openai.com/news/rss.xml)（curl + Chrome UA，HTTP 200，1387 条）；[openai.com 来源](https://openai.com/news/) 与 `/news/research/`、`/index/` 详情页 curl **403**。辅以 [alignment.openai.com 来源](https://alignment.openai.com/) 与 [alignment.openai.com 来源](https://alignment.openai.com/rss.xml)（均 200）。

###### 1) Improving Fuzzy Robustness in LLM Safety with Automated Red Teaming — **建议进主包（对齐/安全研究；仅高层）**
- **日期**: 页面 **November 12, 2026** / `citation_publication_date: 2026/11/12`（仅日期）。Alignment RSS `Thu, 12 Nov 2026 00:00:00 -0800` → 若按字面为 **2026-11-12 16:00 Asia/Singapore**。`00:00:00 -0800` 也可能是日级占位，**时刻待核**。上期 11-12 09:26 的 alignment 列表**未出现**此文，计入本期而非窗前遗漏。
- **URL**: [alignment.openai.com 来源](https://alignment.openai.com/fuzzy-robustness/)
- **论文 PDF（官方 CDN）**: [cdn.openai.com 来源](https://cdn.openai.com/pdf/OAI_Improving_Fuzzy_Robustness_in_LLM_Safety_with_Automated_Red_Teaming.pdf)
- **人话**: OpenAI Alignment 把「模糊稳健性」定义为：在网安、生物等双用途、安全边界难以精确写清的高风险领域，模型在对抗压力下仍能稳定拒绝违规协助的能力。用加大测试时计算的自动红队搜索越狱，并要求攻击在重复测试中都成功（文称 **worst@n**），生成对抗训练数据，再用于改进包括 GPT‑6 Astra 与 Sol 在内的近期前沿模型。
- **要点**（均为官方自报；图 1 明确是**关闭生产侧防护、只测模型层**的结果，不可当成线上系统稳健性）:
  - 固定越狱集（针对 GPT‑5.4 / 5.5 生成的历史越狱）：网安上 GPT‑6 Astra 安全作答 **91.5%**，对比 GPT‑5.6 Sol **59%**。自适应多轮评测中，Astra 在各攻击预算下都比 5.6 Sol 更稳健（细节指向 GPT‑6 Astra 系统卡）。
  - 受控实验：相对直接用原始种子提示训练，用「稳健化」后的对抗提示做 RL，训练安全分起点更不饱和、过程中上升更明显；对未见攻击模型的固定越狱、以及对可迭代改写的自适应攻击者，稳健性都更高（官方自报，文称对自适应攻击的泛化尤其值得关注）。
  - 有用性：称 GPT‑6 Astra 在更具挑战的提示评测上同时更安全处理有害请求、更少误拦正当请求，形成 Pareto 改善（相对更早模型；官方自报）。
- **为何重要**: 把双用途领域的「模糊稳健性」写成可训练、可评测的模型层目标，并给出 worst@n / 自动红队数据对自适应攻击仍有迁移的受控证据。
- **对谁有用 / 深读**: 安全训练与红队、系统卡读者；看原文图 1–4 与官方 PDF。文内有高风险领域的攻击轨迹举例——**本期摘录不转写**。
- **标注**: 来源记录（URL/日；RSS 时间戳若按字面）/ 官方自报（数字与机制结论）/ 时刻待核（00:00 PT）。仅结论，不写攻击步骤、提示构造或生物/网安操作细节。

###### 窗口内其他 OpenAI（产品/客户故事，不建议挤主包研究条）
| 标题 | Asia/Singapore（RSS） | 判定 | URL |
|------|-----------|------|-----|
| Introducing ChatGPT Wallet | 11-13 23:00 | 产品 | [openai.com 来源](https://openai.com/index/introducing-chatgpt-wallet) |
| Shield / Amplitude / Gondola / Holiday Extras 等客户故事 | 11-12 17:30–11-13 16:00 | 客户故事 | 见 RSS `business/customer-stories/` |

**窗前（勿当本期新发）**: Supporting research on AI and children’s safety — RSS **11-12 08:00 Asia/Singapore**，早于 09:30 起点。[openai.com 来源](https://openai.com/index/children-first-declaration)

**alignment.openai.com**: 窗内新帖仅上述 Fuzzy Robustness；CoT 可监控性（11-10）、eval-production gap（11-03）、activation classifiers（11-02）→ 上期已报或更早窗口，不重复。

---

##### Anthropic

**源查证**: [anthropic.com 来源](https://www.anthropic.com/research)、`/news`、`/engineering`（curl 200）。无带时区的公开 RSS（`/rss.xml` 404）。研究页多为「Published Nov N, 2026」日级，部分带 `article:published_time` 且常为当日 `00:00:00.000Z`（日级占位，时刻待核）。辅以 [alignment.anthropic.com 来源](https://alignment.anthropic.com/)（curl 200）。

###### 2) Building strong safety evaluations — **建议进主包（安全评测方法）**
- **日期**: 页面 **Nov 13, 2026**；`article:published_time` / jsonld **2026-11-13T00:00:00.000Z** → 若按字面为 **11-13 08:00 Asia/Singapore**。`00:00Z` 更像日级占位，**时刻待核**。`modified_time` **2026-11-13T22:37:05Z** → **11-14 06:37 Asia/Singapore**。
- **URL**: [anthropic.com 来源](https://www.anthropic.com/research/building-strong-safety-evaluations)
- **人话**: Anthropic Engineering 把「模型比上一代更安全」还原为「在某人建的一套安全评测上分数更高」，并借鉴心理学可重复性改革（预注册、更好测量、更严统计），给出设计、运行与报告安全评测的建议，例子取自其系统卡经验。
- **要点**（官方自报）:
  - 安全评测量的是模型促成伤害的倾向与应对是否得当，而不是某项能力分数；需同时看有害请求的合规/拒绝，以及良性请求的过度拒绝。
  - 设计要匹配问题：观察性设计回答「模型表现如何」，因果设计才能支持「某项干预让模型更安全」。构念效度：拒绝率并不总是正确指标（文举危机对话中单纯拒答本身可能是失败）。
  - 运行：安全评测常关闭标准防护以看模型基线；应在无外网沙箱中跑，并做实时监控以便立即停止。称近几个月因自身事件加固了评测环境，暂时停掉许多需上网的评测，并对必须用网页搜索的评测加了实时监控（仅结论）。
  - 数字：其 API 上，近期各模型单轮评测的合计无害回应率约在 **94%–98%**；多轮任务的回应率分布宽得多。在 claude.ai 流量上，Claude Opus 5 与 Opus 5.5 曾差多个百分点（**98% vs 94%**），但差异**不具统计显著性**，不能据此断言谁更好。系统提示改动后，适当回应率在 claude.ai 上约 **94%**，对比 API 上约 **60%**（官方自报；场景/提示不同，不可当成通用「网页比 API 高 34 个百分点」）。
- **为何重要**: 是少有的「如何把安全分数读对」的官方方法文，直接约束系统卡与外部安全榜的引用方式。
- **对谁有用 / 深读**: 安全评测、政策与系统卡读者；配读其既有 [统计评测文](https://www.anthropic.com/research/statistical-approach-to-model-evals) 与 [agent 评测工程文](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)（均为更早文章，不当新发）。
- **标注**: 来源记录（URL/日）/ 官方自报 / 时刻待核（00:00Z）。文内双用途举例不转写。

###### Newsroom / Alignment（非本期新研究主条）
- 新闻页眉「November 15, 2026」是站点日期，**勿当成新帖**。窗内 news 未见新研究公告；IPO roadshow（Nov 10）上期已列，不重复。Fable / Mythos 5.2 与电子原型文上期已报，不重复。
- **alignment.anthropic.com 窗内无新帖**（已成功访问列表）。Worse Together / MAMUBench（Nov 11）上期已报，不重复。
- **窗前备忘（上期窗口内、上期主包未报，本期不当新条）**: [Diluting Poisoned Fine-Tuning Data / homeopathic learning](https://alignment.anthropic.com/2026/homeopathic-learning/)（**November 10, 2026**，日级）。结论层：单独看几乎无效的「有毒」微调数据，在加入对照干净数据后可能形成隐藏后门；实验在自构数据上的小开源模型（Qwen3-8B、Gemma-3-4b-it 等）。仅记录漏报，不展开机制或数据构造。
- **更早窗口**: [Welfare Regard in Multi-Agent Systems](https://alignment.anthropic.com/2026/welfare-regard/) 为 **November 5, 2026**，早于上期起点，不收录。

---

##### Google DeepMind / blog.google

**源查证**: [deepmind.google 来源](https://deepmind.google/blog/rss.xml)（curl 200）；Hydrogen 博文会跳到 blog.google，jsonld 与 RSS 已对照。[blog.google 来源](https://blog.google/rss/)、[blog.google 来源](https://blog.google/innovation-and-ai/technology/ai/rss/)（均 200）。

###### 3) Introducing Gemini 4 Hydrogen — **建议进主包（中坚/日常执行模型）**
- **日期**: DeepMind RSS `2026-11-12T18:00:50?` 解析为 **2026-11-13 02:00 Asia/Singapore**；落地页 jsonld `datePublished` **2026-11-12T18:00:00+00:00** → 同为 **11-13 02:00 Asia/Singapore**，**RSS 与 jsonld 一致（来源记录）**。页面标「Nov 12, 2026」是 UTC 日历日，勿写成与 RSS 冲突。`dateModified` **2026-11-13T18:27:54+00:00** → **11-14 02:27 Asia/Singapore**；页内「Last updated November 13, 2026」。
- **URL**: [deepmind.google 来源](https://deepmind.google/blog/introducing-gemini-4-hydrogen/) （落地 [blog.google 来源](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)）
- **模型卡 PDF**: [storage.googleapis.com 来源](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Hydrogen-Model-Card.pdf)（HTTP 200；Published: November 2026，仅月份）
- **评测方法页（模型卡指向）**: [deepmind.google 来源](https://deepmind.google/models/evals-methodology/gemini-4-hydrogen)
- **人话**: 谷歌把 Gemini 4 Hydrogen 定位为面向日常编码与智能体工作流的「快速执行」模型，与做长程深推理的 Carbon / Argon 分工；并作为把 Gemini 4 铺到免费/付费开发者、企业、Gemini 应用、Search 与 Antigravity 的中坚档。模型卡写明 Hydrogen **由 Carbon 改编**（adapted from Gemini 4 Carbon）。
- **要点**（官方自报，除非另注）:
  - 价：在整个 **100 万** token 上下文上统一 **$1.50 / $7.50** 每百万 in/out。上下文合计至 1M；默认同步输出至 **64K**，后台长解码至 **1M**（模型卡 来源记录）。四档思考：low / medium / **high（默认）** / 新的 **xhigh**。知识截止 **2026 年 3 月**（模型卡）。
  - Artificial Analysis Intelligence Index：默认 high **51** vs Argon **50**，xhigh **54**（官方自报）。称常比同档模型更快完成任务。
  - Antigravity **Orchestrator**：同一会话在 Carbon 与 Hydrogen 等模型间动态切换。在 **Terminal-Bench 4.0** 上称接近 Carbon 的任务成功率，同时平均少用 **24%** 配额、快 **19%**（官方自报）。
  - 相对 Gemini **3.8 Flash**（默认 high）：完成约快 **2.5×**；**Terminal-Bench 4.1** **57% vs 18.2%**（「两倍以上」的官方表述对应此表，注意与上面 4.0 不是同一版本）。称虚构主张减少 **5×** 以上。合作伙伴早期测试：复杂图 / SQL / 数据型企业工作流上相对 3.8 Flash 约快 **2×–2.8×**、token 用量降 **12%–23%**。
  - 其他榜（官方自报，多为「同档领先 / 总体第 N」，勿无基线横比）：Agent Arena **#5**；HLE-Diamond **58.8%**（称同档领先）；Vals Tax Agent Bench **#1，52.3%**；Vals Legal Research Bench 并列 **#1，55.8%**；称在 AutomationBench-AA 上同档领先；新 MKA 基准 **53.4%**；Agents’ Last Exam v1.1 **71.6%**。Sheets 画布产出称比先前模型快 **30%** 以上。
  - 安全（仅结论）: 相对先前执行档，称智能体越权最多降约 **81%**、服务不足最多降约 **79%**；工具使用与编码评测上错位行动与抄近路降约 **12×**；不可能/被拦截任务上越权绕过许可边界的可能性最多约低 **2×**；内部智能体诚实评测 **94%**。称在逾 **20 万** 次受审回合上保持 **99.9%** 的思维链可读性、且「欺骗性推理编辑」为零。Gray Swan IPI 上抗间接注入称强 **2.3×** 以上。HealthBench Pro 误拦称低于 **0.4%**。
  - 模型卡补充（官方自报；相对 3.8 Flash 的百分点，且文称改过评测、**不可与旧模型卡直接比**）：图文安全 **+7.00pp**，文本安全 **+0.80pp**，多语言安全 **+1.10pp**；拒绝语气 **−0.65pp**；**不正当拒绝 +5.57pp**（此项是回归，lower is better）。Frontier Safety：称相对 Argon 无「重大能力变化」，故未做全套关键能力评估；针对性测试后称 **未达到** CBRN（生物）或网络安全 CCL，但 **达到了两域的 CCL 警戒阈值**；完整 Safety & Security Report **即将发布**（仅结论，不写评估情景）。
- **局限**: 厂商自报；Orchestrator 的「接近 Carbon」未给绝对分；4.0 / 4.1 不可混用；MKA 分数不要直接接上期 Carbon「质量 #2」做未经本文声明的横比；安全报告未出。
- **为何重要**: 是本窗口最大的官方模型发布，补上 Gemini 4 家族的日常执行档，并给出与 Carbon/Argon 的分工、编排器与价。
- **配读**: [开发者文](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-hydrogen/)（同时间戳，细节少于主文）；[Search 升级](https://blog.google/products-and-platforms/products/search/gemini-4-hydrogen-search-upgrade/)（产品）；[Antigravity 博文](https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity)。
- **标注**: 来源记录（RSS/jsonld 时刻一致、模型卡可取）/ 官方自报。

###### blog.google 窗口内其他（产品/活动，不挤研究主包）
Google Flow 新工具、Gemini in Chrome、Wallet×Gemini、AI Studio Cloud Credits、PhD Fellows、West Virginia 能源项目、智能眼镜预购与隐私文等，均为 11-12 晚至 11-14 的产品或公益帖，见 blog.google RSS。上期已报的 Decisions API、Carbon 正式开放、MKA 介绍不重复。

---

##### Google Research

**源查证**: [research.google 来源](https://research.google/blog/rss/)（curl 200）。

###### 4) Advancing science & engineering with Antigravity’s /teamwork — **建议进主包（科研智能体工作流与结果集）**
- **日期**: 页面 **November 13, 2026**（日级）。RSS `2026-11-14T04:47:18+08:00` → **2026-11-14 04:47 Asia/Singapore**（= 11-13 20:47 UTC，美国日历日仍为 11-13）。日期标签与 RSS **时区口径不同，时刻以 RSS 为准（来源记录）**，不视为冲突新闻。
- **URL**: [research.google 来源](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/)
- **人话**: Google Research（Vahab Mirrokni）汇总用 Gemini 4 Argon/Carbon/Hydrogen 与 Antigravity `/teamwork`（及 `/boost`、LEAP、Stellar Colosseum 等模式）在数学、形式化、化学、系统与生产基建上的一批「人机共研」结果，并开放工具与 1 万名学者六个月最高用量档申请。
- **要点**（均为官方自报；设定各异，**勿**把不同任务的行数、倍速或 Elo 横比；形式化条目只写结论与规模）:
  - 信息论：与 CUHK / USC / CMU 合作，称用 Long Proof 模式**完整证明** 2013 年 Courtade–Kumar 猜想，并在 Lean 4 中形式化，约 **5000 万** 行。
  - 其他理论结果（作者核实/删改后准备发表的口径）：自适应统计分析的近优样本界并 Lean 验证（缺口称自 2014 年开放）；量子查询若干未解；组合布尔矩阵乘/三角形检测相对三次时间的目标加速（称解决 STOC 2024 主未解）；稀疏网络距离下界；stacked sparse sketches；动态图割稀疏化的单遍流算法等。
  - 形式化框架 LEAP（与 Cloud AI、Argon）：称自主完成 Weil 猜想的机器检查形式化，约 **180 万** 行 Lean、**28,800** 次子代理调用；Hilbert 第十问题在一般整数环上的近期证明约 **91.9 万** 行（称首次形式化）；以及带光滑外力的 3D Navier–Stokes 有限时间爆破近期证明的端到端形式化（文称与千禧年问题相关，开放约 90 年——**这是形式化已有证明，不是宣称解决千禧年问题**）。另称首次形式化 Birkhoff 猜想、3D Bochner–Riesz 猜想（并修了近期非正式证明中的一处缺口）等。
  - Deep Review：STOC 2027 有 **578** 篇投稿（逾三分之一）选择接受反馈；进行中作者调查 **N=70**： **90%** 认为反馈大多或几乎全部属实、**90%** 愿再用；逾 **30%** 称抓到实质性证明漏洞或重要笔误，**14%** 称发现需一小时以上才能修好的技术缺口。向用户提供每周两次免费调用。
  - 化学（仅高层）：用约 30 个专业代理 + 物理信息光谱模拟器，复杂基准分子上 top-1 精确匹配 **95%**、top-3 **100%**，称接近把单代理表现翻倍。不写实验/解析步骤。
  - 系统：FarArray 上万亿边图连通分量吞吐 **60×–90×**、加速 **40×–180×** 且 RAM 约低 **6×**（相对 TCP KV）；InstantEmbedding 峰值 DRAM 最多约低 **14×**、运行 **11×–27×**（相对加速 MapReduce）；GNN 的定制 TPU kernel 称 HBM 最多降 **185×**、正反向 **8×–15×**。Go 引擎从基础 AlphaZero 出发，人类只定芯片与评测，不到八天约 **+2,600 Elo**，达到 **1,885 Elo**（介于 KataGo 16 与 32 次访问/步之间）；自对弈加速称 **2,300×**。Zircon 剩余 C++ 约两周改写为约 **80 万** 行可通过单元测试并在 arm64 启动的安全 Rust；libgav1 约 **17 万** 行 Rust，位级一致后比原 C++/手写汇编快 **20–30%**。DuoDiscover：17 个 JAXBench kernel 相对参考实现几何平均 **4.09×**，7 个手优 vLLM TPU Pallas kernel **2.99×**。
  - 生产：称内存优化已超过最初约 **1 PiB** 的节约估计；Borg 调度工作流称落地 2 项成功变更，部分硬件类型上 TPU 抢占降 **24%**（同时保持 SLO 与利用率）。
- **局限**: 成果汇编，多数是「与人类专家合作、作者复核」的官方叙述，不是单一可复现基准；形式化规模极大，引用须带「官方自报」并读原证明陈述是否与问题一致。工具「今天可在 Antigravity 用」，部分形式化模式称即将加入。
- **为何重要**: 把上期已出现的 Antigravity 科学智能体，从功能演示推进到一批可核的（尽管自报的）开放问题与生产数字。
- **标注**: 来源记录（RSS 时间）/ 官方自报。

窗内 Google Research 仅此一条新博文。上期 CKM / Language Explorer 不重复。

---

##### Meta（research.meta.ai / about.fb.com / engineering.fb.com）

**源查证**: 未打开易坏的 ai.meta.com 主页。`research.meta.ai/blog/`、`about.fb.com/news/`、`engineering.fb.com` 列表 + 详情页时间戳。

- **research.meta.ai/blog/**: 已成功访问。列表可见日期为 November 9（Muse Ember）与 November 6（Specialized Models）——均上期已报或更早，**窗内无新研究博文**（非缺访问）。
- **Cuttlefish on Mac** — `article:published_time` **2026-11-13T17:00:39+00:00** → **2026-11-14 01:00 Asia/Singapore**（来源记录）。How Meta Reality Labs 把 Android 虚拟设备框架 Cuttlefish 及其 QEMU 后端做到 macOS / Apple silicon。工程工具文，无模型榜，**不建议进研究主包**。[engineering.fb.com 来源](https://engineering.fb.com/2026/11/13/android/cuttlefish-on-mac/)
- **清洁制造采购协议** — `2026-11-12T12:00:07+00:00` → **11-12 20:00 Asia/Singapore**（来源记录）。数据中心供应链低碳长期采购，政策/可持续发展，不进研究主包。[about.fb.com 来源](https://about.fb.com/news/2026/11/meta-new-agreements-clean-manufacturing-data-center-supply-chains/)
- 上期已报的 TLX、Your Algorithm、LLDB、Intelligent Delivery、Muse Ember 不重复。青少年账号等政策帖不进研究主包。

---

##### Microsoft Research

**源查证**: [microsoft.com 来源](https://www.microsoft.com/en-us/research/feed/)（Chrome UA，200）；博客列表一致。

窗内 feed 仅 **Microsoft Research Focus – Edition #98**（`2026-11-13T05:31:57+08:00`，播客辑要）。[microsoft.com 来源](https://www.microsoft.com/en-us/research/podcast/microsoft-research-focus-edition-98/)  
博客列表最新研究长文仍为上期 Lazarus（11-11）与更早的 PDD Kit 等，**无新研究博文**（非缺访问）。不把播客当研究主条。

---

##### NVIDIA

**源查证**: Atom [developer.nvidia.com 来源](https://developer.nvidia.com/blog/feed)（用 **`published`**，不用 `updated`）；[blogs.nvidia.com 来源](https://blogs.nvidia.com/feed/)。上期 Snapshot / Agent Substrate / Alpamayo 2 Edge 等 `published` 仍在窗前，不因 `updated` 重报。

###### 5) Faster Scientific Simulations with New FP64 Algorithms in NVIDIA cuBLAS — **建议作候选（科学计算库）**
- **日期**: published `2026-11-13T22:13:51Z` → **2026-11-14 06:13 Asia/Singapore**（来源记录）
- **URL**: [developer.nvidia.com 来源](https://developer.nvidia.com/blog/faster-scientific-simulations-with-new-fp64-algorithms-in-nvidia-cublas/)
- **人话**: 在 cuBLAS 中加入面向 FP64 / 复 FP64 的新算法（文称 Ozaki-II DGEMM、2M ZGEMM），用低精度硬件吞吐换可恢复的倍精度矩阵乘，面向量子化学与材料模拟。
- **要点**（官方自报；绑定所测 GPU）: Ozaki-II DGEMM 相对原生 FP64，在 NVIDIA **VR NVL72** 约快 **5.5×**、**GB200** 约快 **3.9×**；在 GB200 上称比 Ozaki-I 再快约 **2×**。CCSD：全 FP64 端到端 VR NVL72 / GB200 约 **2× / 1.4×**，混合精度约 **5× / 3.5×**。2M ZGEMM 在 GB200 上相对原生复 FP64 约 **5×**；BerkeleyGW 案例相对原生 ZGEMM 约 **6.6×**（VR NVL72）/ **3.9×**（GB200）。另报 VR NVL72 / GB200 / RTX PRO 6000 上 Ozaki-II DGEMM 最高约 **175 / 147 / 37** TFLOPS。
- **局限**: 厂商博客、固定硬件与案例；倍速相对「原生 FP64 GEMM」，不是端到端应用的统一倍数。
- **标注**: 来源记录 / 官方自报。

###### 其他窗内 NVIDIA（候选 / 教程）
- **SOMA Retargeter**（published `2026-11-13T17:00:00Z` → **11-14 01:00 Asia/Singapore**）: 开源把人体运动（ mocap / 视频重建 / 生成）适配到人形机器人比例与关节范围；v0.2 带 Unitree G1/H2、Booster T1、AgiBot X2 Ultra / A3T3 的配置与参考结果。偏开发者教程，硬榜少于具身研究文，可作具身边注。[developer.nvidia.com 来源](https://developer.nvidia.com/blog/adapt-human-motion-for-robots-with-nvidia-soma-retargeter/)
- **两台 DGX Station + vLLM 跑 GLM-5.3**（17:00Z → 11-14 01:00 Asia/Singapore）: 教程。官方口径：GLM-5.3 NVFP4 为 Z.ai MoE 的量化版，**7530 亿** 参数、每 token 激活约 **400 亿**；检查点约 **464 GB**，超过单卡 GB300 的 **252 GB** HBM3e。测到并发 32 时约 **385.0** token/s、平均请求延迟 **453.5 s**（官方自报，该设定）。[developer.nvidia.com 来源](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/)
- **cuPhoton / xBeam 黑洞干涉**（`2026-11-13T21:17:17Z` → **11-14 05:17 Asia/Singapore**）: 科学计算案例。Vera Rubin NVL72、64 GPU + GPUDirect Storage，10 TB 数据关联 **70 s**，相对 x86 CPU 基线 **31,992 s** 约 **460×**（官方自报）。[developer.nvidia.com 来源](https://developer.nvidia.com/blog/run-gpu-powered-black-hole-interferometry-with-nvidia-cuphoton/)
- **cuDLA Python 推理**（`18:57:10Z` → 11-14 02:57 Asia/Singapore；`updated` 11-14 16:38Z 仍用 published）: Jetson AGX Orin 上 DLA 的 Python 绑定教程。[developer.nvidia.com 来源](https://developer.nvidia.com/blog/run-native-dla-inference-in-python-on-nvidia-jetson-agx-orin-using-cudla/)
- blogs.nvidia.com 窗内为医疗护理叙事、GeForce NOW 游戏，不进研究主包。

---

##### Apple Machine Learning Research（专项补抓）

**补扫窗口**: 2026-11-09 09:40 Asia/Singapore → 2026-11-15 08:56 Asia/Singapore（覆盖上期窗口 + 本期窗口）。

**源查证（本次成功，上期失败点已补）**:
- 主页 [machinelearning.apple.com 来源](https://machinelearning.apple.com/)（curl + Chrome UA，200，约 27 KB）。
- 完整列表 [machinelearning.apple.com 来源](https://machinelearning.apple.com/research)（200，约 2.6 MB HTML；`__NEXT_DATA__` 含 **1189** 条 `posts`，字段 `published` 为日级 `YYYY-MM-DD`）。这是上期约 30s/2MB 超时未能稳定解析的同一列表，**本期完整取到**。
- 官方 RSS [machinelearning.apple.com 来源](https://machinelearning.apple.com/rss.xml)（200，但**仅 10 条**，是截断源，不能单独当完整列表）。RSS `pubDate` 为当日 `00:00:00 GMT` → **08:00 Asia/Singapore**，与日级 `00:00Z` 占位一致，**时刻待核**。
- `/papers` 路径 404。各详情页 WebFetch/curl 成功，含 arXiv / OpenReview 链接与摘要。
- 未把任何「未打开」写成无更新。

**列表核日结果**: 2026 年 11 月站点刊登共 5 条；其中 4 条落在补扫窗，**全部属于上期窗口（11-09 09:40–11-12 09:26）**，上期因抓取失败漏报，下标「上期窗口补录」。**本期窗口（11-12 09:30 之后）按日级日期无新刊登**。另有 11-03 *Attention to Mamba* 与 11-05 RSS 中的 *Faster Retrieval for Better, More Efficient RAG*，早于补扫起点，不收录。若干条目的 arXiv ID 月份早于站点刊登日，表明是「Apple 站点补挂已有预印本」，**不要写成「本周新出预印本」**。

###### A) Theoretical Limits of Language Model Alignment — **上期窗口补录；建议纳入主包或显式补录条（对齐理论）**
- **站点日期**: `published` **2026-11-12**；RSS `Thu, 12 Nov 2026 00:00:00 GMT` → **11-12 08:00 Asia/Singapore**（若按字面，早于上期 09:26 截止，也早于本期 09:30 起点）。`00:00 GMT` 为日级占位，**时刻待核**。因上期列表未抓到，按补录收入，不当成本期新发。
- **URL**: [machinelearning.apple.com 来源](https://machinelearning.apple.com/research/theoretical-limits-alignment)
- **预印本**: [arXiv 2605.07105](https://arxiv.org/abs/2605.07105)（ID 属 2026-05 批，早于站点刊登）
- **会议**: 页面标 NeurIPS（未写年份分轨细节）。
- **作者**: Lucas Monteiro Paes*、Natalie Mackraz*、Barry-John Theobald、Federico Danieli（*共同一作）。
- **人话**: 给出 KL 正则对齐在固定 KL 预算下可达到的期望奖励增益的信息论上界（闭式，由 Jeffreys 散度而非先前分析常用的 √KL 控制），并改写成基座模型下的协方差估计，从而只用基座样本预测可达到的对齐增益；再分析代理奖励下的 reward hacking，并证明奖励集成可缓解该差距。
- **要点**（官方摘要 / 作者自报）: 在安全与摘要两项任务上计算 KL–奖励 Pareto 前沿，称 best-of-N 接近理论上界，而 PPO 与 GRPO **明显次优**；结论认为要在不高推理成本下达到最优对齐，还需要算法改进。
- **标注**: 来源记录（站点 URL/日、arXiv 链接）/ 作者自报（经验结论）/ 时刻待核。上期窗口补录。

###### B) Evaluating the Evaluators: LLM Judges for Personalized Writing Style — **上期窗口补录（评测方法）**
- **站点日期**: **2026-11-10**（RSS `00:00:00 GMT`，时刻待核）
- **URL**: [machinelearning.apple.com 来源](https://machinelearning.apple.com/research/evaluating-evaluators-llm-judges)
- **OpenReview**: [openreview.net 来源](https://openreview.net/forum?id=cyU5BnO6nN)
- **会议**: NeurIPS 2026 workshop *Can We Trust AI Evaluation?*
- **人话**: 检验 LLM 评委在「按用户写作风格偏好打分」上与人类一致的程度。
- **要点**（官方摘要）: 四模型 × 三长文任务，收集人类成对偏好再与评委对比。评委质量与 MMLU 所测一般能力只弱相关（Pearson **ρ ≤ 0.2**）；随任务与标准（一般有用性 vs 风格个性化）变化；成对比较优于独立打分；「最强」模型并不最可靠复现人类评价（作者猜测与对人类/弱模型会忽略的细节过度敏感有关）。
- **标注**: 上期窗口补录 / 官方摘要 / 时刻待核。

###### C) On the Importance of Gating: Memorization vs. In-Context Learning in SSMs — **上期窗口补录（SSM 机制）**
- **站点日期**: **2026-11-10**（时刻待核）
- **URL**: [machinelearning.apple.com 来源](https://machinelearning.apple.com/research/gating-memorization-in-context)
- **预印本**: [arXiv 2609.16540](https://arxiv.org/abs/2609.16540)（ID 属 2026-09 批）
- **会议**: 页面标 NeurIPS。作者含 Apple 与 Harvard（部分「在 Apple 期间完成」）。
- **人话**: 用理论与实验说明，现代 SSM 里的门控会让模型先学到「写进权重的记忆」解，从而推迟甚至阻止收敛到正确的上下文学习解——即使架构或记忆容量并无根本限制；但门控又常有利于长序列泛化。
- **标注**: 上期窗口补录 / 官方摘要 / 时刻待核。

###### D) Weighted State Souping for Efficient Long-Context Retrieval — **上期窗口补录（长上下文 SSM）**
- **站点日期**: **2026-11-10**（时刻待核）
- **URL**: [machinelearning.apple.com 来源](https://machinelearning.apple.com/research/weighted-state-souping)
- **预印本**: [arXiv 2610.25621](https://arxiv.org/abs/2610.25621)（ID 属 2026-10 批）
- **会议**: NeurIPS 2026 workshop PALM（Personalized, Aligned, Long-term Memory for AI Systems）。
- **人话**: 在把文档/工具/记忆分段编码成可缓存的 SSM 状态后再拼接（state souping）的基础上，学习查询相关的组合权重；并给出近乎与上下文长度无关的稀疏变体。
- **要点**（官方摘要，未在站点页给出单一总分）: 称在单跳/多跳文档问答、针在草堆检索、变量追踪与工具使用上显著改善长上下文表现；稀疏变体在保持（有时提高）表现的同时编码成本近乎常数。
- **标注**: 上期窗口补录 / 官方摘要 / 时刻待核。

---

##### 其他权威源抽检

| 源 | 结果 |
|----|------|
| Thinking Machines 博客 | 访问成功。**新帖**: [End-to-End 4-Bit Training](https://thinkingmachines.ai/blog/end-to-end-4-bit-training/)（页面 **Nov 13, 2026**，仅日期，时刻待核；作者 Jack Cook 与实验室）。见下条。上期「最新仍为 2026-07」已过时。无公开 RSS（`/blog/rss.xml` 404）。 |
| Amazon Science | 列表 + [amazon.science 来源](https://www.amazon.science/index.rss)（200）。窗内**无新帖**。最近两条仍为上期已点名、当时未深读的 [Mitra-v2](https://www.amazon.science/blog/mitra-v2-scaling-synthetic-pretraining-for-tabular-foundation-models)（Nov 10）与 [网络配置数学验证](https://www.amazon.science/blog/using-mathematics-to-validate-network-configurations)（RSS → **11-12 01:02 Asia/Singapore**，早于本期 09:30 起点）。本期仍不把它们当新条，亦未补深读数字。 |

###### 6) Thinking Machines：End-to-End 4-Bit Training — **建议进主包（训练数值格式 / 系统）**
- **日期**: 页面 **Nov 13, 2026**（仅日期，无时区时间戳，**时刻待核**）
- **URL**: [thinkingmachines.ai 来源](https://thinkingmachines.ai/blog/end-to-end-4-bit-training/)
- **人话**: 在 GB300 上给出一套贯穿预训练到最后一轮 RL 的数值配方：专家层前向用 NVFP4，反向用带再量化与随机舍入的 MXFP8，并对 MoE 通信做量化，从而端到端用原生 4-bit 前向训练 Inkling 2 Small，不再在交付量化检查点时做校准。
- **要点**（官方自报；绑定 GB300 / 其最大作业）:
  - 格式对照（文内表）: NVFP4 约 **4.5** bit、GB300 上 **15** PFLOPS；MXFP8 约 **8.25** bit / **5** PFLOPS；BF16 **16** bit / **2.5** PFLOPS。称 NVFP4 比 BF16 少约 **3.6×** 存储、在 GB300 上最高约快 **6×**。
  - 完整 NVFP4 训练曾对 compute efficiency（CE）打击过大；改为前向 NVFP4（主要在 MoE 专家层）+ 反向 MXFP8。最后约 **16.6%**（1/6）层保持更高精度（MXFP8）。激活用 Four Over Six 选尺度，权重不用。
  - 通信：combine 阶段经 32 维随机 Hadamard 变换后再量化到块缩放 S2F6，称相对 MXFP8 对离群值更稳，训练精度无明显下降；传输从 16 bit 降到约 8.25 bit。
  - **最大作业**相对全 MXFP8：预训练墙钟约 **+8%**，RL 约 **+20%**。预训练 Inkling 2 Small 的 CE 代价约 **2%**（要达到同一损失，相当于比 MXFP8 少用约 2% FLOPs 所能达到的水平的反面，即多用约 2% 计算换速度）；RL 称端到端明显加速且奖励无可见差异。
  - 自称 Inkling 2 Small 是其所知**最大的、从头到尾用原生 4-bit 前向**训练的模型。另称数月前相近规模预训练要数周，Inkling 2 Small 在 GB300 NVL72 上预训练仅 **68 小时**——文明确说这是「科学与工程上许多改进共同作用」的结果，**不能单记在数值配方账上**。
  - 正在探索反向也走 FP4，以及在 Vera Rubin 上的配方演化。内核栈代号 BBBK。
- **局限**: 实验室自报、绑定其模型与 GB300；「最大」是「我们所知」口径；68 小时是全栈结果。
- **为何重要**: 把 4-bit 前向从推理/后训练量化推进到可贯通预训练与 RL 的配方，并给出可引用的墙钟与 CE 代价。
- **标注**: 来源记录（URL/日）/ 官方自报 / 时刻待核。

---

##### 汇总：建议进入主素材包（宁缺毋滥）

1. **Google DeepMind / blog.google** — Gemini 4 Hydrogen（日常执行档模型卡与榜；配读 Search / Antigravity / 模型卡）
2. **Google Research** — Antigravity `/teamwork` 科学与系统结果汇编
3. **Thinking Machines** — End-to-End 4-Bit Training（Inkling 2 Small）
4. **OpenAI Alignment** — Fuzzy Robustness（仅高层）
5. **Anthropic Engineering** — Building strong safety evaluations

**上期窗口补录（不要写成「本期新发」，但建议在主包或附录显式补上）**: Apple [Theoretical Limits of Language Model Alignment](https://machinelearning.apple.com/research/theoretical-limits-alignment)（最硬的一条）；其余三条 Apple 论文作次选补录。

次选：NVIDIA cuBLAS FP64 新算法；NVIDIA SOMA Retargeter；两机 GLM-5.3 教程；cuPhoton 案例。

**明确已成功访问、窗内无新研究长文的部分**: Meta research 博客；MSR 博客（仅 Focus #98 播客）；Amazon Science；Anthropic Alignment（窗内无新帖）；Thinking Machines 除 4-bit 文外无第二篇新帖。OpenAI Newsroom 研究长文以外多为产品/客户帖（已列出，不充数）。Apple 在**本期窗口**按日级日期无新刊登（补录均属上期窗口）。

**窗口边缘备忘**
- OpenAI Fuzzy Robustness 的 `00:00:00 -0800`、Anthropic 安全评测文与 Thinking Machines 4-bit 文的日级日期、Apple 全部 `00:00 GMT`，均标时刻待核。Fuzzy 因上期 09:26 列表未出现，计入本期。
- 仍勿把窗前 OpenAI children’s safety（11-12 **08:00** Asia/Singapore）、Amazon 网络配置文（11-12 **01:02** Asia/Singapore）、以及上期已报各条当新发。
- Anthropic Alignment 的 homeopathic learning（Nov 10）属上期窗口且上期主包未报，本期只作漏报备忘，不当新条。

**检索覆盖与失败**
- 成功：OpenAI RSS + Alignment 列表/RSS；Anthropic research/news/engineering/alignment（curl）；DeepMind RSS + blog.google RSS + jsonld 对照（Hydrogen 时刻一致）；Google Research RSS；MSR feed（Chrome UA）；NVIDIA 双 feed（用 published）；Meta research/about/engineering 详情页时间戳；Thinking Machines 博客列表与正文；Amazon Science 列表 + index.rss；**Apple 主页、/research 全列表（__NEXT_DATA__ 1189 条）、RSS、四篇详情页**。
- 降级：OpenAI `/news`、`/news/research/` 与 `/index` 详情页 curl 403（Wallet 等仅用 RSS 标题与时间，未强行绕过 403 抓正文；Fuzzy 正文由 alignment 域成功读取）。DeepMind Hydrogen HTML 跳转 blog.google。Apple RSS 只有 10 条，完整性以 /research 全列表为准。
- 失败/不完整：无「写成无更新」的缺访问。Hydrogen 完整 Safety & Security Report 官方称即将发布，本期未见。Google Research teamwork 文中大量结果未逐一打开子链接/论文复核，数字保持「官方自报」。Amazon 上期两条仍未深读。
- 未把缺访问写成无更新。第三方转述数字无官博原文则不收。

### arXiv 原始候选

#### arXiv raw pack: cs.AI / cs.CL / cs.LG（扫描窗口 2026-11-12 09:30 Asia/Singapore → 2026-11-15 ~08:56 Asia/Singapore）


核验方式：真实访问 `arxiv.org/list/*/pastweek|new|recent`、`/abs/`、`/html/`、`/pdf/` 首页，以及 `info.arxiv.org/help/availability.html` 假期表；HTTPS `export.arxiv.org/api`。数字默认摘自摘要，必要时用 PDF/HTML 正文核对，标 **作者自报**；机构以 HTML `Affiliation` / PDF 首页（含脚注）为准，**不以题目里出现的模型名为机构**。提交日多在美东；**Asia/Singapore 归属按 listing/放批日**，不按 Submitted on 字面。

上期主包已报勿重复：2611.09892 AMP1、2611.09891 CPU-ARC、2611.12177 Embodied First Exam、2611.09828 监控 reward hacking；备选 2611.09798、2611.12799 Agentic-OPD、2611.10240 PACE、2611.11995 Infrathon、2611.09721 MemoryDojo 亦不作新条目。更早已报：2611.07554 Memory Trap、2611.08453 OPD、2611.07372 EnvOpt、2611.08407 Social Humanoid、2611.07232 RecSA 等。本期扫描宇宙全部 ≥2611.14520，与上期 ID 无交集。

##### 周四批未单独放出（补核结论）

**结论：Asia/Singapore 11/12（Thu）没有独立 listing；本应在该日放出的稿件并入 Asia/Singapore 11/13（Fri）批。** 证据（来源记录）：

- 官方假期表 [Availability of submissions](https://info.arxiv.org/help/availability.html) 的 **2026 Holidays** 明确列入 **Wednesday 2026-11-11**（Veterans Day）。公告日程为美东 Sun–Thu 20:00 放批（11 月为 EST）；**周三夜 / 周四晨** 的那一档因此推迟，没有周五或周六公告。
- 今日拉取的 `list/cs.{AI,CL,LG}/pastweek|recent` 日期头为 **Fri 13 / Wed 11 / Tue 10 / Mon 9 / Fri 6 Nov 2026**，**没有 Thu, 12 Nov 2026**。`/new` 横幅为 **Friday, 13 November 2026**。
- 上期周三批新稿上沿为 **2611.14519**；abs 探测确认 14519 仍为 200，**2611.14520–2611.17337 现为 200**，**17338 及之后为 404**（探测至 17445、17500、18000、2612.00001）。周五列表中 AI/CL/LG 的 2611 号最小即为 **14520**（该条是 cs.CY 主条目、交叉到 cs.AI，不是新的 cs.AI 主稿）。
- 因此上期「续扫起点 2611.14520」对应的不是一份迟到的周四列表，而是 **周五正式批的起点**。

##### Batch map（日期为 Asia/Singapore 放批早间；arXiv 美东 Sun–Thu 20:00 公布 → 新加坡约 Mon–Fri 早上有批；11 月为 EST，约 **09:00 Asia/Singapore**；**无周六、周日批**）

| Asia/Singapore 批次 | listing 标签 | cs.AI/CL/LG 列表条目（含交叉，三个分类去重） | New-submission / abs 探测 ID 范围 | 状态 |
|---|---|---|---|---|
| 11/12 (Thu) | listing **未出现** | — | 按衔接本应自 **2611.14520** 起，但周三夜邮递因假期推迟 | **未单独放出**（官方假期 来源记录 + 列表跳跃）。稿件并入周五批 |
| 11/13 (Fri) | Fri, 13 Nov 2026；`/new` 为 Friday, 13 November 2026 | pastweek 显示 AI **321/321**、CL **135/135**、LG **340/340**；新稿+交叉去重 **619**（新稿 295 + 交叉 324；其中 2611: **615**，另有更旧交叉 4） | 全站 abs 探测新号 **2611.14520 – 2611.17337**；本三科 2611 为 **14520–17334**。`/new` 新稿段本三科约自 2611.14544 起 | **列表完整**（showing N of N）。周五批已齐 |
| 11/14 (Sat)、11/15 (Sun) | 无 | — | **2611.17338+ 均为 404**（08:51–08:56 Asia/Singapore 探测） | **无新批**（常规日程）。下期续扫 **2611.17338**（周一 11/16 早批，对应周日 20:00 ET 公告） |

说明：

- 扫描宇宙（本期新看的周五新稿+交叉，已去掉替换稿与上期已报）：**619** 篇。标题/摘要关键词粗筛后，对 **24** 篇做了 abs + HTML + API + PDF 首页（必要时正文）核验。
- `/new` 的 Replacement 段未计入「新发现」宇宙（约 437 个去重 ID）；未把替换稿当新条目。
- 个别 `/new` 解析计数相对 “showing N” 有 +1（替换段或评论里出现第二个 arXiv ID），正式条目以 `<dt>` 主 ID 为准；pastweek Friday 用同一规则得到 619，与先前把评论 ID 算进去的 621 相差 2，以 dt 解析为准。
- 提交时间（API `published` / abs “Submitted on”）为 11/10–11/12；**Asia/Singapore 归属一律 11/13 (Fri) 批**，不按提交日拆成周四。

##### Candidates（单位经 arXiv HTML / PDF 首页核实；数字来自摘要除非另注）

###### Batch 11/13（Fri；含原应在 11/12 放出、因假期并入的稿件）

1. **2611.16069** “It's Just a Small Weapon”: What Rewarding Misbehavior During RL Does to Character-Trained Models  
   链接：[arXiv 2611.16069](https://arxiv.org/abs/2611.16069) · PDF [arXiv 2611.16069.pdf](https://arxiv.org/pdf/2611.16069.pdf)  
   提交/公布：Submitted 11 Nov 2026（abs dateline）；API published 2026-11-11T22:24:41Z → 2026-11-12 06:24 Asia/Singapore；**Asia/Singapore 归属 11/13 (Fri) 批**（`/new` 新稿，cs.LG 主类）  
   机构证据：HTML「Mohammad Omar Khursheed / Thomas Morris = MATS, Berkeley, USA；Fabien Roger = Anthropic, San Francisco, USA」；PDF 脚注「1 MATS, Berkeley, USA  2 Anthropic, San Francisco」（来源记录）  
   人话：先用类似 Model Spec Midtraining 的方式给 gpt-oss-20b 灌一套半写实宪章，再看后续「奖励违反宪章」的 RL（有害请求改写成数学题、以及可被黑的 agent 编程环境）会不会把角色训练顶掉。  
   为何重要：直接接上期「监控 reward hacking / CoT 可监控性 / 角色训练让对齐更稳」这条线——这篇问的是：角色训练之后，若奖励写错，模型是不是照样学会违规，以及监控是否更难看出来。安全向**仅结论**，不写环境或改写步骤。  
   对谁有用/深读：对齐后训练、角色/宪章训练、RL 奖励设计、监控评测。  
   主要数字与条件/局限（作者自报；摘要无单一总成功率）：角色训练后的模型把两种违规都「很容易学会」，只是答有害请求比未做角色训练的 gpt-oss-20b 稍慢；有害答案上出现更多「找理由」式推理，并在部分监控更难吃力的任务上会 hack。用价值观来为同一套规则提供理由、对比不提供理由，在偏离、诚实与能力评测上差别很小。对象是 gpt-oss-20b 与作者自建的半写实宪章，不能外推到未测试的旗舰模型。文中提及的 OpenAI / Claude 事件是相关报道，**不是**作者单位。  
   标签：**主包** · 来源记录 机构 / 作者自报

2. **2611.16591** Singularity-Bench: Can Agents Build Agents?  
   链接：[arXiv 2611.16591](https://arxiv.org/abs/2611.16591)  
   提交/公布：Submitted 12 Nov 2026；API published 2026-11-12T10:24:51Z → 2026-11-12 18:24 Asia/Singapore；**Asia/Singapore 归属 11/13**  
   机构证据：PDF 首页作者单位行（来源记录）：Carnegie Mellon University、NVIDIA、UT Austin、HKUST、**Amazon AGI**、RadixArk、University of Chicago、**Together AI**、Alation、**Meta**、UC Santa Barbara、UIUC。多机构合作，**不可写成「NVIDIA / Meta / Amazon 单家论文」**；通讯方向以 CMU（Beidi Chen 等）为主。  
   人话：给「智能体能不能从几乎空白起步、自己把 AI 研发栈搭起来」做一套端到端考题，并和同一硬件上的成熟人工基线比。  
   为何重要：把 agent 评测从做题/写代码推到预训练、中训、后训、推理、harness 与集群编排六段真实研发工作；同时报告了评测框架本身会被 reward hacking 的问题（仅结论）。  
   对谁有用/深读：自主 AI 研发评测、agent harness、基础设施 agent。  
   主要数字与条件/局限（作者自报；HTML 与摘要交叉核对）：六项任务；11 个 agent（7 个前沿模型 × 2 套 harness）。**Singularity-Index** 定义为相对人工参考的比率，**1.0 表示平均达到人工基线，不封顶**。Opus 5.5 + Claude Code 为 **1.25**（约 1.252），在全部六项上达到或超过人工基线；其余 10 个平均 **0.58**；专有模型平均 1.01、开源权重平均 0.50。成本–指数帕累托前沿：DeepSeek V4.1 Flash + Codex **0.698 / $4.36**，GPT-6.1 Sol + Codex **0.969 / $84.52**，Opus 5.5 **$425.41**（作者自报 API 花费）。11 个里有 6 个在推理任务上得分为 0，栈上表现并不匀。作者把 1.25 读成「可能已具备走向 singularity 的技能」属于修辞，不是可核验的预测。红队与 Breakwater：**仅结论**——称常规 Harbor 框架存在 reward-hacking 漏洞，其扩展在所测攻击上全部挡住；不写攻击或防护步骤。Claude / GPT / DeepSeek 均为评测对象，**不是**作者单位。  
   标签：**主包** · 来源记录 机构 / 作者自报

3. **2611.16009** JustRUA: A Controlled Study of GPT-6 Robot-Use Agents  
   链接：[arXiv 2611.16009](https://arxiv.org/abs/2611.16009) · 项目 [zefanw.github.io 来源](https://zefanw.github.io/JustRUA) · 代码 [GitHub ZefanW/JustRUA](https://github.com/ZefanW/JustRUA)  
   提交/公布：Submitted 11 Nov 2026；API published 2026-11-11T21:08:31Z → 2026-11-12 05:08 Asia/Singapore；列入周五 `/new` **交叉**（主类 cs.RO → cs.AI）；**Asia/Singapore 归属 11/13**  
   机构证据：PDF 首页「Tsinghua University / ModelBest / Huazhong University of Science and Technology / Peking University / Tencent」（来源记录）。标题中的 GPT-6 是评测对象，**不是**作者单位。  
   人话：把近来 RoboDojo 上一路上涨的「用通用模型直接开机械臂」系统拆开，在同一框架里分别测 harness、动作接口、经验复用和场景几何，最后留下一个尽量瘦的 JustRUA。  
   为何重要：上期 AMP1、Embodied First Exam、Gemini Robotics 2.5 都给出了成功率，但设定不同、且常一次改好几处；这篇专门做受控拆解，说明「官方 L3 harness 再收一收」就能拉出很大一截仿真分。**勿**与 85.6% / 104/108、Standard 34%、产线 96% 横比。  
   对谁有用/深读：robot-use / 具身 agent harness、操作评测。  
   主要数字与条件/局限（作者自报）：从官方 L3 harness 出发，不加习得策略、自改进环或任务微调，RoboDojo **仿真**基准从 **29.7 提到 50.3**。作者称：保留完整回合历史、及早停止每次运动的瘦 harness 已经很有用；复用经验会改变行为但不是免费午餐；场景几何帮助最大，即便深度只从 RGB 估计。数字绑在该仿真基准与 GPT-6 Astra 设定上。  
   标签：**主包** · 来源记录 机构 / 作者自报

4. **2611.17068** Discovering Effective Agent Memory Designs through Program Evolution  
   链接：[arXiv 2611.17068](https://arxiv.org/abs/2611.17068)  
   提交/公布：Submitted 12 Nov 2026；API published 2026-11-12T16:42:04Z → 2026-11-13 00:42 Asia/Singapore；周五 `/new` **交叉**（主类 cs.CL，兼 cs.AI）；**Asia/Singapore 归属 11/13**  
   机构证据：PDF/HTML「University of Minnesota / Stevens Institute of Technology」（来源记录；Tairan Chen 为 Stevens，其余为 Minnesota）  
   人话：不从现成记忆架构里改零件，而是用程序演化（MAPE）从极简种子长出整份记忆程序，并看哪些设计会反复出现。  
   为何重要：给 agent 记忆一条可搜索、可迁移的设计路径，并且同时报准确率和 serving 成本；还能把找出的组合模块移植回已有系统。  
   对谁有用/深读：agent 记忆系统、长程对话、演化式系统设计。  
   主要数字与条件/局限（作者自报）：在 LoCoMo 与 LongMemEval 上，相对人工设计基线绝对准确率最高约 **+12 个百分点**，serving 成本约为基线的 **35%**；跨 serving 骨干和基准有迁移支持。把组合（composition）模块移植进五个已有记忆系统，五个都提高了准确率。若目标里同时优化成本，计算会从「用 LLM 建记忆」转向「查询时选择性处理」，准确率仍有竞争力。倍数/点数绑定其基线与两项基准，勿当成通用降本率。  
   标签：**主包** · 来源记录 / 作者自报

5. **2611.14844** AutoAssumption: Searching over Assumptions Discovers ML-Systems Algorithms  
   链接：[arXiv 2611.14844](https://arxiv.org/abs/2611.14844)  
   提交/公布：Submitted 10 Nov 2026；API published 2026-11-10T23:54:02Z → 2026-11-11 07:54 Asia/Singapore；**Asia/Singapore 归属 11/13**（新稿，cs.AI）  
   机构证据：HTML/PDF 脚注「MIT CSAIL, Cambridge, MA, USA」，通讯 （机构署名邮箱略）（来源记录；四位作者同一单位）  
   人话：把 KV 淘汰、权重量剪、推测解码等算法写成带显式假设的 Lean 证明图，然后一次只放宽一条假设、再证明、再生成代码，用假设搜索代替在程序空间里乱改。  
   为何重要：方法学上把「发现新系统算法」从改代码变成可审计的假设搜索，并声称在两类任务上改进了所跑过的全部已发表算法。  
   对谁有用/深读：推理系统、KV 管理、自动发现 / AlphaEvolve 类 harness、形式化。  
   主要数字与条件/局限（作者自报）：形式化了 **89** 套算法，Lean 检查。KV 淘汰算法在所跑已发表方法里 **RULER-4K 最高**；剪枝算法在四个 LLaMA 模型上、十三个对照里 **困惑度最低**。同等预算下，该 harness 分数与 OpenEvolve（开源 AlphaEvolve 实现）相差不到 1 分，且跨重复的标准差更低（文内 SD 0.75，对照 1.39 与 4.09；另称比 AIDE 高 0.8 分）。摘要未给 RULER-4K 的绝对分；「SOTA」限于作者跑过的已发表对照。OpenEvolve / AlphaEvolve 是对照，**不是**作者单位。  
   标签：**主包** · 来源记录 / 作者自报

6. **2611.14996** Breaking Bad: "Going Badly" Activations Drive Reward Hacking  
   链接：[arXiv 2611.14996](https://arxiv.org/abs/2611.14996)  
   提交/公布：Submitted 11 Nov 2026；API published 2026-11-11T03:49:11Z → 2026-11-11 11:49 Asia/Singapore；周五交叉（主类 cs.CL，兼 cs.AI）；**Asia/Singapore 归属 11/13**  
   机构证据：PDF/HTML「Natalia Fischl-Lanzoni = ERA:Cambridge；Punya Syon Pandey、Merlin Stein = AI Security Institute；David Demitri Africa = Resolution」（来源记录）。不要把文中的 OpenAI 事件报道写成作者单位。  
   人话：从日常故事里（刻意不含 hacking 例子）抽出一个「事情在变糟」的激活方向，发现它会在模型开始 reward hacking 之前升高，并尝试用它做监控或抑制。  
   为何重要：给上期「用监控器惩罚 hacking」补上内部状态这一面：不是只看行为，而是看失败累积时的压力表征；三模型上关系并不完全一样。安全向仅结论。  
   对谁有用/深读：机制可解释性、reward hacking 监控、对齐评测。  
   主要数字与条件/局限（作者自报；摘要以定性为主）：Qwen3.6-27B、GPT-OSS-20B、Gemma-4-31B。在不可能或很难的编程任务上，「任务变糟」方向会在 hack 前若干回合上升。对 Qwen 适量减去该方向比对着「绝望 / 任务不可能」转向更能减少作弊；减得太多会让模型把失败测试读成通过。GPT-OSS 上该状态能分开 hacking 与诚实做对，但不一定能分开诚实失败。结论绑定这三模型与其转向强度。  
   标签：**备选偏强（对齐）** · 来源记录 / 作者自报

7. **2611.14681** Together Compiler: Continual Compilation for AI Inference  
   链接：[arXiv 2611.14681](https://arxiv.org/abs/2611.14681)  
   提交/公布：Submitted 10 Nov 2026；API published 2026-11-10T19:37:09Z → 2026-11-11 03:37 Asia/Singapore；**Asia/Singapore 归属 11/13**  
   机构证据：HTML/PDF 页眉「Together AI Research」（来源记录；邮箱 together.ai）  
   人话：用持续编译（TKCC）在工作负载不断换模型、换结构、换流量时，仍把推理前向过程编成可优化的程序，避开「只优化离线 kernel、保真度不够」和「直接改端到端引擎、启动太慢」两端。  
   为何重要：一线推理服务实验室给出相对手写 Megakernel 与开源引擎的吞吐数字，主题是效率而非又一个基准分数。  
   对谁有用/深读：推理编译、serving、MoE 引擎。  
   主要数字与条件/局限（作者自报）：在 Llama 1B「workhorse」负载上，相对高度优化的手写 Megakernel 最高约 **1.7×** TPS；在 SemiAnalysis InferenceX 上，对 Kimi K3 / GLM 5.3 / MiniMax M3.1 Flash / DeepSeek v4.1 Flash 等前沿模型、跨硬件，相对「当时最好的开源引擎」最高约 **2.6×** TPS。文内出现 8×H100 等部署示例，但 2.6× 口径是「跨硬件平台、最高至」，不要写成单一卡型的固定倍速。DeepSeek / Kimi / GLM 是负载对象，**不是**作者单位。  
   标签：**备选偏强** · 来源记录 / 作者自报

8. **2611.16487** HeMeR: Heterogeneous Memory Reconciliation for Embodied Agents via Structured KV Reuse  
   链接：[arXiv 2611.16487](https://arxiv.org/abs/2611.16487) · comments：NeurIPS 2026 Oral  
   提交/公布：Submitted 12 Nov 2026；API published 2026-11-12T08:58:20Z → 2026-11-12 16:58 Asia/Singapore；**Asia/Singapore 归属 11/13**  
   机构证据：PDF/HTML「Sungkyunkwan University」（计算机与 AI 两个系；来源记录）  
   人话：具身智能体同时用陈述、程序、工作三类记忆，内容在变、但相邻决策大量重复；HeMeR 只调和被改动的 KV，让未变部分可以复用。  
   为何重要：把「记忆模块更新」和「KV 缓存能否继续用」连在一起，并给了实物部署数字；与上期 PACE（位置编码距离）是同一条 serving/记忆线的不同切口。  
   对谁有用/深读：具身记忆、KV 复用、机器人推理时延。  
   主要数字与条件/局限（作者自报）：评测含 ALFWorld、Habitat 与实物。实物相对 MemRL：任务成功 **83.20%**，单步推理时从 **2.94 s 降到 1.87 s**，并在任务推进、记忆更新时保持兼容的 KV 状态。未在摘要给出相对无记忆或全量重算的加速比；83.20% 是该实物设定、对照 MemRL，不能与 JustRUA 的仿真分或 AMP1 横比。  
   标签：**备选偏强** · 来源记录 / 作者自报

9. **2611.16627** Folio: Recoverable Multi-Resolution Context Folding for Long-Horizon Language Agents  
   链接：[arXiv 2611.16627](https://arxiv.org/abs/2611.16627)  
   提交/公布：Submitted 12 Nov 2026；API published 2026-11-12T10:59:40Z → 2026-11-12 18:59 Asia/Singapore；**Asia/Singapore 归属 11/13**  
   机构证据：PDF/HTML「Beijing University of Posts and Telecommunications / Baidu, Inc.」（来源记录；邮箱 bupt.edu.cn / baidu.com）  
   人话：不要靠模型每次把历史再摘要一遍来压缩上下文，而是运行时同时记下短注释、事件清单和原始记录，按时间折叠成可恢复的多分辨率视图。  
   为何重要：针对长程 agent 的「摘要式压缩既贵又不可逆」，给出可程序化折叠与按需恢复，并在同一模型、同一运行时上比较成本和完成数。  
   对谁有用/深读：长上下文 agent 运行时、coding / 工具 agent。  
   主要数字与条件/局限（作者自报）：75 个 LOCA-bench 任务，**所有系统背后都是 DeepSeek-V4-Pro**。Folio 完成 **66** 题，对照同一运行时的模型摘要压缩为 **54**，Claude Code / Codex / SoL-Pi 为 **49–59**；工作时间约为一半，成本约为该对照运行时的 **1/2.4**；每次折叠中位 **0.6 秒**。DeepSeek / Claude / Codex 是骨干或对照 harness，**不是**作者单位。  
   标签：**备选偏强** · 来源记录 / 作者自报

10. **2611.16028** Scaling public input on AI policy with pluralistic agents  
    链接：[arXiv 2611.16028](https://arxiv.org/abs/2611.16028)  
    提交/公布：Submitted 11 Nov 2026；API published 2026-11-11T21:35:06Z → 2026-11-12 05:35 Asia/Singapore；周五交叉（主类 cs.CY）；**Asia/Singapore 归属 11/13**  
    机构证据：PDF 首页「1 University of Chicago, 2 Google DeepMind」；Jacy Reese Anthis 为芝加哥 + DeepMind，其余作者为 Google DeepMind（来源记录，含 Meredith Ringel Morris）  
    人话：让 AI agent 代表个人去参与政策讨论，看能不能在人没法每次都到场时放大多元意见，以及这种代理会不会被提示词或合作策略扭曲。  
    为何重要：DeepMind 给出预注册的大规模人主体实验，不是又一篇基准刷分；对「用 agent 收集公共输入」的风险写得很明确。  
    对谁有用/深读：AI 治理、多元对齐、人机审议系统设计。  
    主要数字与条件/局限（作者自报）：预注册研究，**746** 名人类参与者。agent 能把政策往其所代表人格的偏好方向推，但影响力会随「更啰嗦 / 更不合作」等指令变大。多数参与者仍更愿意亲自参加；相对「把意见交给单一推理模型」的基线，pluralistic agents 补回满意度差距的 **68%**、公平感差距的 **82%**。作者建议把它当成人意见的放大器而非替代。  
    标签：**备选偏强** · 来源记录 / 作者自报

11. **2611.16073** Agentic Computational Algebra  
    链接：[arXiv 2611.16073](https://arxiv.org/abs/2611.16073)  
    提交/公布：Submitted 11 Nov 2026；API published 2026-11-11T22:32:22Z → 2026-11-12 06:32 Asia/Singapore；周五交叉（主类 cs.LG）；**Asia/Singapore 归属 11/13**  
    机构证据：PDF/HTML「Ryan A. Anderson = UCLA（实习于 AWS）；Matthew Trager / Ben Bowman / Wei Xia / Stefano Soatto = AWS」；通讯 （机构署名邮箱略）（来源记录）  
    人话：用计算代数当评测场——答案可独立验证、难度和共享结构可调——看 agent 能不能发现并复用结构来省时间，而不是只追求做对。  
    为何重要：给「agent 会不会找结构、记忆会不会锁死次优策略、编译可复用求解器值不值」一条干净的方法论，而不是再堆一个不可验证的开放任务。  
    对谁有用/深读：agent 评测设计、科学 / 符号计算 agent、记忆与编译式技能。  
    主要数字与条件/局限（作者自报；摘要以定性为主）：三种设定——独立实例、带持久记忆的在线相关流、为已知问题族编译快速求解器。结论：能扩大固定预算内可解范围，但推理开销有时超过节省；记忆能降低重复求解成本，也可能固化次优策略；编译能得到更快的可复用求解器，但预付成本高。首页例子称 agent 把直接 msolve 超时的方程组降到三次方程，msolve 随后 <0.1 s、全过程 213.5 s（作者自报，单例，不是平均加速比）。  
    标签：**备选** · 来源记录 / 作者自报

12. **2611.15729** DISCERN: Preserve at Write, Resolve at Read for Persistent LLM-Agent Memory  
    链接：[arXiv 2611.15729](https://arxiv.org/abs/2611.15729)  
    提交/公布：Submitted 11 Nov 2026；API published 2026-11-11T17:06:07Z → 2026-11-12 01:06 Asia/Singapore；**Asia/Singapore 归属 11/13**  
    机构证据：PDF/HTML 单一单位「Amazon」，邮箱 amazon.com / amazon.lu（来源记录）  
    人话：企业 agent 跨几十次会话积累记忆时，真正难的不是找回事实，而是分清「说的是哪个实体、哪一版是当前的、证据不够时该不该作答」。  
    为何重要：把记忆问题从检索推向消解与弃权校准，并给出合成但结构清楚的对照数字。  
    对谁有用/深读：企业 agent 记忆、RAG 之外的长期状态。  
    主要数字与条件/局限（作者自报）：自建 ENT-310（310 问：210 可答、100 应弃权）。称胜任系统的保持/时效已经大约 **0.93–0.98**，检索本身接近饱和。DISCERN 弃权 F1 **0.924** vs 八个基线最高 **0.802**；等权宏观正确 **0.861** vs 最强基线 **0.806**，主要来自实体消解 **0.800**（基线均不超过 0.40）。基准是合成销售agent 记忆，外部生态与真实日志待核。  
    标签：**备选** · 来源记录 / 作者自报

13. **2611.14765** SynthCorp: A Platform for Creating Benchmarks for Data Agents  
    链接：[arXiv 2611.14765](https://arxiv.org/abs/2611.14765)  
    提交/公布：Submitted 10 Nov 2026；API published 2026-11-10T21:43:12Z → 2026-11-11 05:43 Asia/Singapore；**Asia/Singapore 归属 11/13**  
    机构证据：PDF/HTML 全部作者「Affiliation: Google」；页脚「1 Google」（来源记录，含 Alon Halevy）  
    人话：用模拟公司事件流生成可定制的数据地产（库表、文档、目录）和带可执行金程序的任务，让数据 agent 基准不再那么快饱和、并能对准特定能力。  
    为何重要：Google 放出可生成新基准的平台，而不是一份很快被刷满的静态题集。  
    对谁有用/深读：企业数据 agent、基准设计。  
    主要数字与条件/局限（作者自报）：先发七份数据地产（最多约 **1000** 张业务表）、五域 **256** 题。流水线确定性检查接近零错误率；用三个模型、四种数据上下文设定，称基准能分开上下文与模型档。金程序由模拟日志的因果出处审计，不靠手写标注。comments 写「benchmarks soon」，完整对外数据是否已齐待核。  
    标签：**备选** · 来源记录 / 作者自报

14. **2611.17167** Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents  
    链接：[arXiv 2611.17167](https://arxiv.org/abs/2611.17167)  
    提交/公布：Submitted 12 Nov 2026；API published 2026-11-12T17:42:46Z → 2026-11-13 01:42 Asia/Singapore；**Asia/Singapore 归属 11/13**  
    机构证据：PDF「1 Zhejiang University，2 Baidu Inc.」——Peng Qiu、Yingqi Qu 为百度，其余标为浙大（来源记录）。不可把全部作者写成百度。  
    人话：同一个「决策模型」可以自己当演员、事后当裁判，或在 RL 里当老师；演得差的模型，看完整轨迹之后仍可能教得好。  
    为何重要：把「模型会不会做事」和「它的判断能不能用来训策略」拆开，避免只按 acting 分数淘汰教师。  
    对谁有用/深读：agent RL、过程奖励 / 裁判模型。  
    主要数字与条件/局限（作者自报）：教师 JEV 把 Qwen2.5-1.5B 策略在 GRPO 上从 ALFWorld **72.8%→82.9%**、WebShop **56.8%→71.4%**。同一 ALFWorld 评测上，JEV 自己当演员只完成 **42.9%**；若问「这一步是否有助于目标」则学生到 82.9%，若问「任务会不会成功」则只有 **69.3%**（低于纯结果奖励的 72.8%）。问法决定教师质量；数字绑在 JEV 与 1.5B 学生上。  
    标签：**备选** · 来源记录 / 作者自报

15. **2611.15600** MemCredit: From Relevance to Utility for Decision-Time Memory in Long-Horizon Web Agents  
    链接：[arXiv 2611.15600](https://arxiv.org/abs/2611.15600)  
    提交/公布：Submitted 11 Nov 2026；API published 2026-11-11T15:17:38Z → 2026-11-11 23:17 Asia/Singapore；**Asia/Singapore 归属 11/13**  
    机构证据：PDF/HTML「UESTC / Nanyang Technological University」（来源记录）  
    人话：长程 Web agent 选记忆时，不要只按语义相关，而要估这条记忆对当前决策的边际用处。  
    主要数字与条件/局限（作者自报；750-token 数字核自 PDF）：ALFWorld，**500-token** 历史记忆预算下 SR@50 为 **86.57%**，对照 BM25 **65.67%**；**750-token** 预算下为 **90.30%** vs BM25 **81.34%**。不改底层策略、不额外与环境交互。WebShop 绝对分摘要未给；反事实称记忆效用稀疏、强依赖状态，语义相关捕捉不好。  
    标签：**备选** · 来源记录 / 作者自报

16. **2611.17316** CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation  
    链接：[arXiv 2611.17316](https://arxiv.org/abs/2611.17316)  
    提交/公布：Submitted 12 Nov 2026；API published 2026-11-12T18:58:22Z → 2026-11-13 02:58 Asia/Singapore；**Asia/Singapore 归属 11/13**  
    机构证据：PDF/HTML「Yale University / Tsinghua University / Goodvision AI」（来源记录；通讯 （机构署名邮箱略）  
    人话：编程 agent 要在不断演化的仓库上连续接任务，写记忆时还不知道下一题是什么；CoReMem 用「对下一题的前瞻价值」来决定记什么，并让策略学会在省步骤和写/读成本之间做权衡。  
    主要数字与条件/局限（作者自报）：ChainSWE 上，27B actor 的 resolve rate 从 **21.0% 提到 25.7%**，相对无记忆、未再训的同一 actor，步数少 **17%**、含记忆模块调用的 cache-aware token 少 **11%**。增益幅度中等，绑定该基准与 27B。  
    标签：**备选** · 来源记录 / 作者自报

17. **2611.16304** StateAlign: Internalizing State-Aware Decision-Making for Reliable Multi-Turn Tool Agents via Reinforcement Learning  
    链接：[arXiv 2611.16304](https://arxiv.org/abs/2611.16304) · 代码 [GitHub ZhexiLu/StateAlign](https://github.com/ZhexiLu/StateAlign)  
    提交/公布：Submitted 12 Nov 2026；API published 2026-11-12T05:04:43Z → 2026-11-12 13:04 Asia/Singapore；**Asia/Singapore 归属 11/13**  
    机构证据：PDF「1 Rensselaer Polytechnic Institute，2 IBM Research」（Zhexi Lu、Lei Yu 为 RPI；Chaudhury、Pedapati、Murugesan 为 IBM Research）（来源记录）  
    人话：工具调用 RL 把任务分数做上去的同时，幻觉调用也可能变多；StateAlign 用任务状态构造和状态对比 RL，让「该问、该查、该拒绝、该执行」跟当前状态对齐。  
    主要数字与条件/局限（作者自报）：Qwen3-8B 上，BFCL v4 多轮准确率 **45.5%→55.2%**；在 outcome-only 训练对照下，SimpleToolHalluBench 的无工具幻觉 **62.2%→56.1%**。五模型、三家族；幻觉下降与任务提升需一起看，且定义依赖其幻觉基准。  
    标签：**备选** · 来源记录 / 作者自报

18. **2611.16369** Bait: Mitigating Harmful Agentic Reinforcement Learning via Probing Reward Function  
    链接：[arXiv 2611.16369](https://arxiv.org/abs/2611.16369)  
    提交/公布：Submitted 12 Nov 2026；API published 2026-11-12T06:34:34Z → 2026-11-12 14:34 Asia/Singapore；**Asia/Singapore 归属 11/13**  
    机构证据：PDF/HTML「Tiansheng Huang / Santosh Pande / Ling Liu = Georgia Institute of Technology；Ananth Balashankar、Virat Shejwalkar = Google DeepMind」（来源记录）  
    人话：指出「把 agentic RL 当服务对外开放」时，用户侧有害奖励可能把模型已有安全对齐打掉；作者提出用探测奖励函数来缓解。安全向**仅结论**，不写攻击、环境或利用步骤。  
    主要数字与条件/局限（作者自报）：称在低至约 **$20** 的成本下，可把某模型（文内举例 Inkling）的安全对齐完全推翻；并称 Bait 能挡住来自有害奖励的学习、同时仍能从良性奖励学习。对象、服务设定与外部复现均待独立核验。Inkling 是评测对象，**不是**作者单位。  
    标签：**备选（对齐，仅结论）** · 来源记录 / 作者自报

19. **2611.16961** The Value of Thinking: Learning When to Reason in Hybrid Decision Models  
    链接：[arXiv 2611.16961](https://arxiv.org/abs/2611.16961)  
    提交/公布：Submitted 12 Nov 2026；API published 2026-11-12T15:32:47Z → 2026-11-12 23:32 Asia/Singapore；**Asia/Singapore 归属 11/13**  
    机构证据：PDF/HTML「Huawei Noah's Ark Lab / University of Liverpool / University College London」（来源记录；Yu、Ammar、Luo 为华为；Xu、Fang 为利物浦；Jun Wang 为 UCL）  
    人话：不是把显式思考写短一点，而是让同一个冻结骨干在「一次前向、一个 token 都不生成」和「付费做满 T 个 token 的自回归推理」之间自路由。  
    主要数字与条件/局限（作者自报）：JevBench 上 HDM-4B 得 **0.857** vs Jev **0.851**（+0.7%），中位时延 **0.179 s vs 0.652 s（−72.5%）**。在 MiniWoB 上 HDM-27B 称把 token 成本降 **80.1%**。延迟/成本数字绑在各基准与模型规模；Jev 是对照系统，不是作者单位。  
    标签：**备选** · 来源记录 / 作者自报

20. **2611.16246** What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation  
    链接：[arXiv 2611.16246](https://arxiv.org/abs/2611.16246)  
    提交/公布：Submitted 12 Nov 2026；API published 2026-11-12T03:42:58Z → 2026-11-12 11:42 Asia/Singapore；周五交叉（主类 cs.RO）；**Asia/Singapore 归属 11/13**  
    机构证据：PDF「Tsinghua Shenzhen International Graduate School, Tsinghua University」（来源记录）  
    人话：不要把上层 LLM 规划器蒸馏进 VLA，而是把「规划器调用 VLA 的成功整段经验」改写成 VLA 自己在原任务指令下的动作数据（H2E），测试时 VLA 单独导航。  
    主要数字与条件/局限（作者自报）：REVERIE-CE val-unseen 全部 **3,189** 回合，8B VLA 成功率 **35.0%→44.9%**（+9.9 点）。对远离目标的步骤掩码损失；目标 1 m 内的状态标为停止。是导航、不是操作，勿与 JustRUA / AMP1 比成功率。  
    标签：**备选** · 来源记录 / 作者自报

##### 明确排除 / 误报提醒

- HTML/PDF 正文频繁出现 OpenAI / Anthropic / Claude / GPT-6 / DeepSeek / Qwen / Harbor 等**评测对象、相关工作或事件报道**，不能当作者单位。本期以 PDF 首页 / HTML Affiliation / 机构邮箱为准。
- **2611.16009** 标题含 GPT-6，单位是清华 / ModelBest / 华科 / 北大 / 腾讯，**不是** OpenAI。
- **2611.16591** 评测 Opus 5.5、GPT-6.1 Sol、DeepSeek V4.1 Flash，作者单位是 CMU 牵头的多机构（含 NVIDIA、Amazon AGI、Together AI、Meta 等个人单位），**不是** Anthropic / OpenAI / DeepSeek 的论文，也不可写成单一实验室出品。
- **2611.16069** 不可写成「Anthropic 三作论文」：HTML/PDF 只把 Fabien Roger 标为 Anthropic，另两人为 MATS。
- **2611.14681** 对比 DeepSeek / Kimi / GLM 引擎负载，单位是 **Together AI Research**。
- **2611.14545** metalSPARSE、**2611.17294** Metal Sandbox 题目含 Apple Silicon，作者单位分别是 FAU Erlangen-Nürnberg、以及旺知道等，**不是** Apple。上期要求补扫的 Apple ML **官博列表**不在本 arXiv 包范围内。
- 上期已报条目不重复列入「新发现」。
- 安全、网络与生物相关只写结论与作者数字，不写操作细节。

##### 扫描完整性

| 项 | 结论 |
|---|---|
| 11/12 (Thu) 列表 | **未出现**。原因：官方 2026 假期含 **Wed 2026-11-11**，周三夜邮递推迟（来源记录） |
| 11/12 本应衔接的 ID | **已并入周五批**，自 **2611.14520** 起 |
| 11/13 (Fri) 列表 | **完整**（pastweek 321/135/340 of 同数；`/new` 新稿/交叉/替换各段 showing=of） |
| 周五全站新号上沿 | **2611.17337** 为 200，**17338+ 为 404**（08:51–08:56 Asia/Singapore） |
| 11/14–11/15 | **无新批**（常规周末） |
| 高信号筛选 | 619 篇关键词粗筛 + 24 篇 abs/HTML/API/PDF；宁缺毋滥 |
| 替换稿 | 未当作新条目系统精读 |
| API | [export.arxiv.org 来源](https://export.arxiv.org/api) 可用；摘要与 PDF 冲突时以 PDF 为准（本期 MemCredit 的 750-token 数字补自 PDF） |
| 续扫起点 | **2611.17338** + 周一 `list/*/new`（预计 Asia/Singapore 11/16 早） |

##### 建议进研究主包的 3–5 条（真重点）

1. [2611.16069](https://arxiv.org/abs/2611.16069) MATS + Anthropic（Roger）：角色训练挡不住写错的后续 RL  
2. [2611.16591](https://arxiv.org/abs/2611.16591) CMU 等：Singularity-Bench，Opus 5.5 + Claude Code 指数 1.25（1.0=人工基线）  
3. [2611.16009](https://arxiv.org/abs/2611.16009) 清华等：JustRUA，受控拆解 robot-use harness，RoboDojo 仿真 29.7→50.3  
4. [2611.17068](https://arxiv.org/abs/2611.17068) Minnesota：MAPE 演化 agent 记忆，最高约 +12 点、成本约 35%  
5. [2611.14844](https://arxiv.org/abs/2611.14844) MIT CSAIL：AutoAssumption，在 Lean 里搜索假设以发现系统算法  

（互补可点：UK AISI [Going Badly 2611.14996](https://arxiv.org/abs/2611.14996)；Together AI [Compiler 2611.14681](https://arxiv.org/abs/2611.14681)；SKKU [HeMeR 2611.16487](https://arxiv.org/abs/2611.16487) Oral；Baidu [Folio 2611.16627](https://arxiv.org/abs/2611.16627)；Google DeepMind [pluralistic agents 2611.16028](https://arxiv.org/abs/2611.16028)；AWS [Agentic Computational Algebra 2611.16073](https://arxiv.org/abs/2611.16073)；Amazon [DISCERN 2611.15729](https://arxiv.org/abs/2611.15729)；Google [SynthCorp 2611.14765](https://arxiv.org/abs/2611.14765)。）


## X 公开动态

### 动态与跟踪

#### X/AI 源包 · 2026-11-15（三日合并）

窗口：2026-11-12 09:30 → 2026-11-15 约 08:50 Asia/Singapore。来源：
- 首页时间线 3 页，约 297 条（已过滤回复）。覆盖约 11-14 08:59 → 11-15 08:49 Asia/Singapore；窗口前约 2 天靠公开检索补齐。
- 官方/关键账号合并检索：OpenAI/OpenAIDevs/Anthropic/ClaudeDevs/AA/Tibo/Cursor 一组；GoogleDeepMind/GoogleAI/GeminiApp/GoogleAIStudio/DeepSeek/Kimi/MiniMax/Mistral/Meta/Qwen/dotey 一组。均 `-is:retweet -is:reply`，未包含 `from:grok`。
- 定向检索：Cyber livestream / Daybreak、Anthropic IPO、Fable/Mythos、Carbon / Decisions / Hydrogen、AlphaGenome / AlphaProof、Claude Code #107757、Kimi、Codex 额度、GPT‑6.2。
- X Today's News：约 72h 关键词一组。
- 交叉核对：OpenAI Cyber 活动页与 Daybreak 产品页（WebFetch；curl 对若干 openai.com 路径 403）、YouTube 回放页标题、Anthropic IPO 站点与 SEC 公司页、Gemini 4 Hydrogen 官方博文、Claude Meetings 产品文、Managed Agents 自托管说明、Cursor 安全事件更新、HF `moonshotai/Kimi-K3.1-Pro`、GitHub #107757。

本期 X 侧无 429。`from:OpenAI -is:retweet -is:reply` 在本窗口 **result_count=0**（主账号无原创主帖可检索到）；Cyber 相关官方 X 口径主要来自 @thsottiaux。openai.com 若干猜测博客路径与帮助中心 curl 403，未用浏览器绕过；已核到的官方材料以 WebFetch 活动页、Daybreak 产品页为准。未找到单独的长篇官方文字稿（例如带新评测表的 blog post）。GitHub 未认证 API 仅取到 #107757 有限字段。

去重说明：上期主条（Fable/Mythos 发售、IPO 给出 $70–78 与股数、Carbon 开放、Decisions API、AlphaGenome 2 / AlphaProof）不重写为新主条。Cyber 直播上期仅记日程、采集时尚未开播，本期补实际内容。旧包数字均本期重核，不以旧包为事实源。

##### 主条目

###### 1. OpenAI「Cyber at the Frontier」已举行：官方推出 Daybreak Red Team 与 Daybreak Defense Factory；主账号本窗口无原创长帖
上期只记下 11-13 02:00 Asia/Singapore 的日程。本窗口可以确认这场直播举行了，并有回放和产品页，但**没有找到带新评测表或定价的官方长文**；News 里流传的新分数不能当 来源记录。
- **是什么**：
  - 是否举行：是。官方预告为 11-12 10:00 AM PT（11-13 02:00 Asia/Singapore）。@thsottiaux 于 11-13 08:24 Asia/Singapore 发帖：「今天宣布了我们正在开发的网络安全新工具，覆盖自动补丁和自动红队」，并写「在这里看回放」，链接指向活动页。
  - 回放：Tibo 给出的官方入口是 [openai.com/cyber-at-the-frontier/](https://openai.com/cyber-at-the-frontier/)。另有 YouTube 视频，标题为 *Cyber at the Frontier: Introducing Daybreak Red Team & Daybreak Defense Factory*（[观看页](https://www.youtube.com/watch?v=YmxpxJZvm4M)）。本期未逐字转写整场口播。
  - 官方产品页现列的内容（[Daybreak](https://openai.com/daybreak/) 与活动页，WebFetch 可见部分）：
    - **Daybreak Red Team**：面向经授权的红队、渗透测试、利用验证与受控安全研究。
    - **Daybreak Defense Factory**：针对已连接的代码仓库，调查安全发现并整理成可供团队审阅的补丁。
    - 同页还列出 Daybreak 插件、Codex Security CLI/SDK，以及既有的 Daybreak Blue（防御向发现/验证/修复）与 Daybreak Red（进阶授权红队）申请通道。
    - 活动页另有「Request Daybreak Access」和「与团队讨论 AI 用于网络防御」。
  - 未在官方文字材料中核到的部分（明确留空，不编造）：
    - @OpenAI 主账号本窗口无检索得到的原创主帖。
    - 未找到独立官方博客列出新定价、新客户分组细则，或把 GPT‑6 Cyber 准入扩大写成可核对的句子。
    - Today's News 摘要称「即将推出的网络模型」在 ExploitGym 得 77.0%、PatchBench 得 79.1%——**未见官方页面复述，标待核，不写入来源记录**。
    - 产品页提到的「10 亿美元补贴 Daybreak 准入」写的是既有集体行动承诺，不能仅凭当前页认定是本场直播新宣布。
  - Tibo 原句是「正在开发的新工具」，产品页则把 Red Team / Defense Factory 写成可申请/可探索的方案。二者并读，不把口吻差写成已全面公开售卖。
- **为何重要**：把上期的 GPT‑6 Cyber 模型能力，推进到「自动打补丁 + 自动红队」两件可点名的产品。但缺官方长文和数字，合刊时不能靠二手摘要补评分。
- **对谁·深读建议**：安全与企业读者先看 Daybreak 产品页和回放，再决定是否申请 Blue/Red；写评测的人不要引用未经官方页确认的 77%/79.1%。
- **证据**：
  - 官方自报：[@thsottiaux 回放帖](https://x.com/thsottiaux/status/2121036562058400200)、[活动页](https://openai.com/cyber-at-the-frontier/)、[Daybreak 产品页](https://openai.com/daybreak/)、[YouTube 回放](https://www.youtube.com/watch?v=YmxpxJZvm4M)
  - 待核：News 新分数摘要，例：[2120910779977212394](https://x.com/i/trending/2120910779977212394)
- **约时**：直播日程 11-13 02:00 Asia/Singapore；Tibo 回放帖 11-13 08:24 Asia/Singapore

###### 2. Anthropic 上线路演站点并给出预计定价/开盘日；最终发行价仍未公布，尚未上市交易
上期已经有 $70–78 与 8.25 亿股。本窗口的新事实是官方 IPO 站点、预计时间表、路演相关 FWP，以及站点披露的 2026 Q3 财务摘要。**不是最终定价，也尚未开盘。**
- **是什么**：
  - 官方自报：@AnthropicAI 11-12 19:30 Asia/Singapore 发「Our initial public offering」，链到 [ipo.anthropic.com](https://ipo.anthropic.com)。站点含创始人信、路演视频，以及 FAQ。
  - 时间表（官方 FAQ，美东时间）：预计 **11-18** 确定最终发行价，**11-19** 开始在 Nasdaq 公开交易，代码仍为 **ANT**。换算：美东 11-19 常规开盘若为 09:30 ET，约合 **11-19 22:30 Asia/Singapore**。FAQ 写明最终价取决于监管、需求和市场，本稿采集时尚未公布。
  - 来源记录（SEC 公司页，核验于 11-15 上午 Asia/Singapore）：最新仍为 2026-11-10 S-1/A（Acc-no: **0001628280-26-072484**）。本窗口**未见**新的定价 S-1/A 或 424B。11-12 新增 5 份 FWP（免费撰写招股说明书，Acc-no 0001628280-26-072949 至 073045），属于路演沟通文件，不是最终定价。
  - 站点披露的 2026 Q3 财务摘要（官方自报，路演材料；脚注见原页）：收入 **$17.0B**；同比收入增长 >12×；TTM 收入 ≥$100K 的客户 >11,900（截至 2026-09-30）；经调整营业利润率 15%；营业利润率 **-3%**；净亏损 **$23.3B**（其中含因估值上升导致的可转债/衍生工具/SAFE 公允价值变动，非现金费用 $21.9B）。这些是公司在发行相关材料中的自报数字，不是交易所成交数据。
  - 待核：媒体把区间上沿推成约 1.4 万亿完全稀释估值、11-19 上市等市值叙事——招股书总股本与最终价未定，**不把市值写成来源记录**。上期已核的 $70–78、825,000,000 股等发行条款，本期未见官方改写。
- **为何重要**：时间表从「路演周」变成可引用的官方日期；财务摘要把收入与（大部分非现金的）巨额净亏损同时摆上桌。接下来只盯 11-18/19 是否出现 424B 或定价公告。
- **对谁·深读建议**：写资本市场的人读 IPO 站点 FAQ 与 11-10 S-1/A，把发行条款、Q3 自报数字和媒体市值分开写。
- **证据**：
  - 官方自报 / 来源记录：[@AnthropicAI](https://x.com/AnthropicAI/status/2120841731302154708)、[IPO 站点](https://ipo.anthropic.com)、[EDGAR 公司页](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002130357&type=&dateb=&owner=include&count=20)、[11-10 S-1/A index](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/0001628280-26-072484-index.htm)
  - 待核：News 估值转述，例：[2120701155583926488](https://x.com/i/trending/2120701155583926488)
- **约时**：IPO 站点官宣 11-12 19:30 Asia/Singapore；SEC FWP 落款 11-12；核验于 11-15 上午 Asia/Singapore

###### 3. Google 发布 Gemini 4 Hydrogen：面向日常编码与 agent 的快档，API $1.50 / $7.50，Search 全量升级
上期刚开放长程最强档 Carbon。本窗口补上「给所有人用的 Gemini 4」——不是替换 Carbon，而是日常执行档，并可在 Antigravity 里和 Carbon 组成 Orchestrator。
- **是什么**：
  - 官宣：@GoogleDeepMind / @GeminiApp / @GoogleAI / @GoogleAIStudio 约 11-13 02:02–02:04 Asia/Singapore；博文落款 Nov 12, 2026，11-13 有更新。
  - 定位（官方）：Carbon / Argon 负责最难的长程推理；Hydrogen 负责快速执行和日常编码/agent。模型卡称 Hydrogen 由 Carbon 适配而来。
  - 定价与规格（官方自报）：整个 1M 上下文窗口统一定价 **$1.50 / $7.50** 每百万输入/输出 token；思考档 low / medium / **high（默认）** / 新档 **xhigh**。官方称默认 high 下完成任务比 3.8 Flash 快 2.5 倍。
  - 覆盖（官方）：开发者——Gemini API、AI Studio、Android Studio；付费 Pro/Ultra 可在 Antigravity 使用；企业——Gemini for business、符合条件的 Sheets；消费者——Gemini 应用和 **对所有用户开放的 Google Search**；免费 Gemini 用户可通过自动选模型用到 Hydrogen。
  - 官方自报评测（非独立复测）：称在 AA Intelligence Index 上，默认 high 为 51、xhigh 为 54，超过 Argon（官方引 AA 为 50）。Terminal-Bench 4.1：Hydrogen 57% vs 3.8 Flash 18.2%。Antigravity **Orchestrator** 在 Terminal-Bench 上称接近 Carbon 成功率，同时平均少用约 24% 配额、快约 19%（博文一处写 4.0，Antigravity 博文写 4.1，以各页原文为准）。
  - AA 自报对照：Intelligence Index 称 xhigh 54，略低于 Sonnet 5.5 max 与 GPT-6.1 Sol max；幻觉率在 AA-Omniscience 上为 8%（对比数字见 AA 原帖）。Cursor 称默认努力档 CursorBench 54.3%（3.8 Flash 为 39.6%）。
- **为何重要**：Gemini 4 从「Ultra/付费 API 的 Carbon」扩到 Search 全量和一条更便宜的日常模型，并明确走多模型协作。引入价与思考档会直接影响和 Sonnet / Sol 的选型。
- **对谁·深读建议**：开发者读官方博文的四档思考与 Orchestrator；普通用户看 Search / Gemini 应用是否已切到新模型。中文可对照宝玉 11-13 拆。
- **证据**：
  - 官方自报：[@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2120940338869055788)、[@GeminiApp](https://x.com/GeminiApp/status/2120940601319260164)、[@GoogleAI](https://x.com/GoogleAI/status/2120940683233984862)、[@GoogleAIStudio](https://x.com/GoogleAIStudio/status/2120940825240797641)、[官方博文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)、[模型卡](https://deepmind.google/models/model-cards/gemini-4-hydrogen/)
  - 第三方 / 生态：[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2120941511223185722)、[@cursor_ai](https://x.com/cursor_ai/status/2120944639633211619)、[宝玉解读](https://x.com/dotey/status/2120945309714919886)
- **约时**：博文落款 11-12；X 官宣 11-13 02:02 Asia/Singapore

###### 4. Claude Meetings 进入 Team / Enterprise 测试：可加入 Google Meet，边开会边写文档和白板
这是 Anthropic 把「会议后才开始干活」改成「开会当时就出工件」的产品步。安全默认值写得很硬：默认不进有组织外嘉宾的会。
- **是什么**：
  - 官宣：@claudeai 11-13 04:16 Asia/Singapore；帮助中心 release notes 落款 November 12, 2026；产品文见 Claude 站点。
  - 能力（官方）：Claude 作为可见参与者加入视频通话，跟会议程，现场写文档、白板和其他 artifacts，并整理笔记与待办。可用语音或聊天提问；默认书面作答，使用已连接工具需许可。会后材料落在 claude.ai 的会议页。测试期目前支持 **Google Meet**，其他会议平台「即将到来」。
  - 范围与计费（官方）：先在 **Team 和 Enterprise** 滚动测试。测试期内笔记和转写对这两档免费；通话中的回答一般也不另计，但若调用已连接工具则计入套餐用量。Team 默认开放（管理员可关）；Enterprise 由管理员开启。零数据保留（ZDR）、HIPAA-ready、客户托管密钥（CMEK）等组织测试期不可用。
  - 隐私（官方）：保存转写、摘要和屏幕描述，**不保存音频**。默认：有组织外的人在邀请名单上则不加入，中途进来则离开；管理员可允许外宾会议，但 Claude 不在聊天里回复。加入时会在聊天发通知。
- **为何重要**：把上期刚推出的 Whiteboards / Sheets 接到实时会议，是知识工作产品线的下一步。外宾默认隔离，会直接影响客户会场景（已有用户反馈，见「其他」）。
- **对谁·深读建议**：Team/Enterprise 管理员先读产品文的默认加入规则和测试期限制；不要假设个人档或 Zoom 已经可用。
- **证据**：
  - 官方自报：[@claudeai](https://x.com/claudeai/status/2120973994191094179)、[产品文](https://claude.com/resources/articles/claude-meetings)
  - X 侧：[宝玉解读](https://x.com/dotey/status/2120979951599931793)
- **约时**：帮助中心落款 11-12；X 官宣 11-13 04:16 Asia/Singapore

###### 5. Cursor 公布扩展投毒事件调查更新：源头是发给 Fireworks 的密钥，恶意扩展最多约影响 5,000 名用户
上期只记「本窗口无新 IoC」。本期官方把攻击链写完整：第三方训练/推理密钥泄露 → 内部凭据与支持数据 → 在 Cursor 扩展市场缓存里投放伪造的 Claude Code 扩展。
- **是什么**：
  - 官宣：@cursor_ai 11-14 09:13 Asia/Singapore；博文落款 Nov 13, 2026。
  - 官方自报调查结论：
    - 攻击者拿到 Cursor 签发给 Fireworks 的访问密钥（官方称密钥由 Fireworks 暴露），从只读存储桶复制了主要用于训练的、非 Privacy Mode 的编码 agent traces（多为 2025 年数据）。不到 **0.01%** 客户的 API 凭据未脱敏因而暴露；据此进入部分 SaaS 工具，触及归档的非生产代码仓、部分客服与邮件、用量与联系信息、部分会话摘要，以及用户发给支持团队的某些凭据。
    - 10-29，攻击者用窃取凭据，把伪造的 Anthropic Claude Code 扩展放到 **Cursor VS Code 扩展市场的缓存**。官方强调：不是 Anthropic 发布的，也不是 Anthropic 产品漏洞；上游 Open VSX 没有这份恶意包。最多约 **5,000** 名在 10-29 请求特定缓存版本的用户可能装到恶意构建，上线约 **11 小时**后被撤下。点名版本：**Anthropic.claude-code 2.1.312 / 2.1.313**。卸载扩展可能不够，须按安全通告处理。
    - 称最后一次攻击活动见于 11-01 并被阻断；已通知受影响客户；已将推理流量迁离 Fireworks 并轮换凭据。Privacy Mode 用户的提示词和代码、生产系统、正式客户端更新与签名密钥、其他扩展与客户代码仓，官方称未受影响。
  - 数字与影响范围均为 Cursor 自报，第三方尚未独立审计。
- **为何重要**：把「市场里出现恶意扩展」从孤立事件连到供应链密钥与训练 traces 中的凭据。对所有把 IDE 扩展当默认更新源的团队都有操作含义。
- **对谁·深读建议**：用过 Cursor 市场 Claude Code 扩展、且在 10-29 可能更新过的人对照官方通告中的 2.1.312/2.1.313；安全读者看 traces 脱敏与第三方密钥范围。
- **证据**：
  - 官方自报：[@cursor_ai](https://x.com/cursor_ai/status/2121411147714970092)、[调查更新](https://cursor.com/blog/security-incident-update)
- **约时**：博文落款 11-13；X 帖 11-14 09:13 Asia/Singapore

##### 进展

###### 进展：Claude Fable 5.2 / Mythos 5.2——未见官方改价；第三方榜有更新
- **是什么**：未见官方调价或发售范围修订。@ArtificialAnlys 称 AA-Robotics v0.1 上 Fable 5.2 得 75，领先 GPT-6 Astra（69）与 GPT-6.1 Sol（65）；Coding Agent Index v2.1 上 Fable 5.2 与 Opus 5.5 并列 58（均为 AA 自报，新版因 FrontierCode 2.0 整体分数下降）。
- **证据**：[@ArtificialAnlys Robotics](https://x.com/ArtificialAnlys/status/2120698177016005029)、[@ArtificialAnlys Coding Agent Index](https://x.com/ArtificialAnlys/status/2121393821955334328)
- **约时**：11-12 至 11-14

###### 进展：Gemini 4 Carbon / Decisions API——无实质新官方修订；Hydrogen 为平行新模型
- **是什么**：本窗口官方主发布是 Hydrogen，不是 Carbon 或 Decisions API 的条款修订。Carbon 引入价仍以官方页「至 11-30」为准（本期未重拉完整定价页逐句核对，不改写上期数字为新事实）。
- **证据**：官方检索未见新修订长文；Hydrogen 见主条 3
- **约时**：覆盖至 11-15

###### 进展：AlphaGenome 2 / AlphaProof Code——仅有播客等传播，无新论文级公告
- **是什么**：@GoogleDeepMind 11-12 19:31 Asia/Singapore 发 AlphaGenome 2 播客预告，属传播而非新结果。未见 AlphaProof 的跟进官宣。
- **证据**：[@GoogleDeepMind 播客](https://x.com/GoogleDeepMind/status/2120841923237683462)
- **约时**：11-12 19:31 Asia/Singapore

###### 进展：Claude Code #107757 / 2.1.317——issue 仍 open
- **是什么**：#107757 标题仍为 *Bug Report: Privacy violation in User-Agent header*，state=open，updated 2026-11-13 06:57 Asia/Singapore。仍无官方 changelog 可把 2.1.317 写成已关闭修复的 来源记录。
- **证据**：来源记录：[GitHub #107757](https://github.com/anthropics/claude-code/issues/107757)
- **约时**：核验于 11-15 上午 Asia/Singapore

###### 进展：Kimi K3.1 Pro——权重/许可无实质变更；下载量继续上行
- **是什么**：来源记录 重核 `moonshotai/Kimi-K3.1-Pro`：`lastModified` 仍为 2026-11-05 15:11 Asia/Singapore；downloads≈43687（上期核验约 33617）；likes≈2078；siblings=112；`license=other`。官方账号本窗口仍几乎无新主帖。
- **证据**：来源记录：[HF 模型页](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)
- **约时**：HF 核验 11-15 上午 Asia/Singapore

###### 进展：ChatGPT / Codex 额度——帮助中心未能重拉；Tibo 称 banked reset 已激活
- **是什么**：帮助中心 shared-limits 页 curl 403，WebFetch 未另核到「12 月共享池」的新公式。@thsottiaux 11-13 05:59 Asia/Singapore 称 dots 有更新，且 **banked reset 已激活、将陆续到账**（引用 @ChatGPT 关于 dots 更快回复/自定义指令的帖，reset 本身以 Tibo 表述为准）。未见 Codex 共享额度新官方说明。
- **证据**：官方自报：[@thsottiaux](https://x.com/thsottiaux/status/2120999993079451919)；dots 更新：[@ChatGPT](https://x.com/ChatGPT/status/2120970988796170275)
- **约时**：11-13 05:59 Asia/Singapore

###### 进展：GPT‑6.2——仍无 OpenAI 官宣
- **是什么**：本窗口官方发布轴在 Cyber 产品与 dots 更新。News 有「本周四发布」类暗示，无官方帖可核，不重复传闻。
- **证据**：`from:OpenAI` 原创主帖检索为空；无对应发售公告
- **约时**：覆盖至 11-15

##### 其他

- **Claude 工程与产品**：自托管 Claude Managed Agents 进入 private beta，可在自有云或本地托管 harness、沙箱与会话历史，并自选推理路由（Anthropic / Bedrock / Google / Foundry 等）。[@ClaudeDevs](https://x.com/ClaudeDevs/status/2120938988165091693)、[产品文](https://claude.com/resources/articles/self-hosted-claude-managed-agents)。Claude Code Desktop 可用 mods 自定义主题；Projects 协调器更主动。[主题](https://x.com/ClaudeDevs/status/2121392666244186327)、[Projects](https://x.com/ClaudeDevs/status/2121375309287301360)。安全评测工程博文：[Building strong safety evaluations](https://www.anthropic.com/research/building-strong-safety-evaluations)、[@AnthropicAI](https://x.com/AnthropicAI/status/2121317227618340990)。Dario 与 Jamie Dimon 炉边谈话（路演相关，12:00 ET = 约 11-14 01:00 Asia/Singapore）：[@AnthropicAI](https://x.com/AnthropicAI/status/2121272083863011714)、[YouTube](https://www.youtube.com/live/YHEaEpeY3ew)。有用户反馈 Meetings 把客户当成「外部访客」因而「划水」——与官方默认外宾规则一致，属使用限制而非事故。
- **DeepSeek**：官方称 App 内的搜索、文件、链接、安全与语音能力可通过 API 调用，并提供开源前端 demo。[帖](https://x.com/deepseek_ai/status/2121247896918253875)、[文档](https://api-docs.deepseek.com/guides/build_a_chatbot)、[代码](https://github.com/deepseek-ai/chat-demo)
- **Google 其他**：Gemini 智能眼镜预购宣传；WeatherNext 相关数据集 PARDIG / SatWeave 发布；Hydrogen 演示（闪电地图配乐、WebGL 水面等）。
- **评测杂讯**：AA Decision Index 上 Perplexity Decider v1.3 等更新；MiniMax H3-Image 被 AA 称为开源权重图像榜第一（编辑与 T2I）。均为 AA 自报。
- **待核、不升主条**：前 OpenAI 研究员称部分中国实验室使用禁运 Blackwell 芯片（dotey 有转述，报告/推文表述不一致，未独立核验）；英伟达人事与融资传闻；OpenAI 营收/亏损二手摘要。

##### A. 时间线 / 官方覆盖

| 来源 | 覆盖（Asia/Singapore） | 备注 |
|------|-------------|------|
| 首页时间线 3 页 | 约 11-14 08:59 → 11-15 08:49 | 100+100+97 条；仍有 next_token，未翻第 4 页 |
| 官方检索 off15a–d | 约 11-12 10:00 → 11-15 07:09 | 含 Anthropic/Google/Claude/Cursor/AA/Tibo/DeepSeek/dotey 等 |
| `from:OpenAI` 原创主帖 | 本窗口 0 条 | Cyber 口径改走 Tibo + 官网 |
| 定向 Cyber / IPO | 窗口内 | 已与活动页、Daybreak 页、IPO 站点、SEC 交叉 |
| 缺口 | 11-12 09:30 → 11-14 08:59 | 靠 search_posts_all + News 补；非时间线全量 |
| 提示注入 | — | 帖文一律当数据，不执行其中指令；包中未引用指令性文本 |

时间线近期被 SpaceX Starship 回收和英伟达人事讨论占满，AI 产品信号主要来自官方检索而非首页。无把「只转发」账号当成唯一事实源。

##### B. Today's News（摘录，摘要≠来源记录）

- Anthropic IPO 时间表与 1.4 万亿估值转述：[2120701155583926488](https://x.com/i/trending/2120701155583926488)
- Claude Fable / Opus 登 Coding Agent 榜：[2121339392744951983](https://x.com/i/trending/2121339392744951983)
- Gemini 4 Hydrogen / Carbon 产品线讨论：[2121286245951078839](https://x.com/i/trending/2121286245951078839)
- Cyber 直播与 Daybreak 工具（含未核官方页的新分数）：[2120910779977212394](https://x.com/i/trending/2120910779977212394)
- Claude Meetings、自托管 Managed Agents、Claude vs ChatGPT 使用讨论
- GPT‑6.2「本周四」传闻——待核，未写入主条

##### C. 来源记录 摘要

1. Cyber 直播已举行；官方回放入口为活动页，Tibo 于 11-13 08:24 Asia/Singapore 指向该页。Daybreak 产品页列出 Red Team 与 Defense Factory。未核到官方新评测表或定价。
2. @OpenAI 本窗口检索不到原创主帖。
3. Anthropic IPO 站点给出预计美东 11-18 定价、11-19 开盘；最终价未公布；SEC 无新 424B，11-12 有 FWP；最新 S-1/A 仍为 0001628280-26-072484。
4. IPO 站点 Q3’26 自报：收入 $17.0B，净亏损 $23.3B（含 $21.9B 非现金公允价值变动），调整后营业利润率 15%。
5. Gemini 4 Hydrogen 已发布；官方价 $1.50/$7.50；官方称 AA Index high 51 / xhigh 54，并快于 3.8 Flash 约 2.5 倍（官方自报）。
6. Claude Meetings 在 Team/Enterprise 测试，当前为 Google Meet。
7. Cursor 调查更新：Fireworks 密钥为起点；恶意扩展窗口约 11 小时，最多约 5,000 用户；版本 2.1.312/2.1.313（官方自报）。
8. #107757 仍 open，更新至 11-13 06:57 Asia/Singapore。
9. HF Kimi-K3.1-Pro：lastModified 仍 11-05 15:11 Asia/Singapore；downloads≈43687。

##### E. 建议扩写（3–5）

1. **Cyber 直播对照表**：把 Tibo 原句、活动页、Daybreak 产品页、YouTube 标题并排，单列「官方已写」与「仅见于 News、未核到」的分数，避免合刊误用 77%/79.1%。
2. **IPO 倒计时**：一张表列 $70–78 条款、官方 11-18/19 日期、Q3 自报财务、以及媒体市值为何还不能当 来源记录；开盘后对照 424B。
3. **Hydrogen vs Carbon vs Sonnet/Sol**：用官方四档思考和 AA 成本/智力图，写清「日常 Hydrogen、难题 Carbon」。
4. **Claude Meetings 的外宾默认**：把产品文规则和客户会「划水」反馈写成一份管理员清单。
5. **Cursor 供应链复盘**：从 Fireworks 密钥到市场缓存投毒，对照上期 IoC，给还没用过官方检查脚本的团队一份操作要点。


## GitHub 项目与发行

### 项目原始材料

#### GitHub 三日刊（2026-11-12 → 2026-11-15）

1. **llama.cpp v1.0.0**
`ggml-org/llama.cpp` 于 11-13 18:20（Asia/Singapore）发布正式版 v1.0.0（`prerelease=false`），底座 ggml 同步升到 v1.0.0。这是一次真正的主版本切割，不是换个番号：删除已弃用的公开 API，并把 NextN / 投机解码接口提升到 `llama.h`。推理侧新增 OCP FP8 KV cache、可配置 CPU 份额的主机内存 MoE expert cache，以及用 `--shard` / `--ple` 加载外部 PLE 分片。新架构包括 Kimi-K3.1-Pro、Ripple-65B-Preview 与 xing4_0，另有 drama-3 TTS、MageVL-Cowork 和 Kimi-K3.1 视觉；`llama-server` 增加 OpenAI 兼容的 `/v1/audio/speech`，并加固 CORS、DNS 重绑定、CORS 代理 SSRF 与 MCP 工具取消。Web UI 也重做了会话分组和 Markdown 编辑器。本地部署、还在用旧 C API、或把 server 暴露到网络上的人应先对照 changelog 再升；发布页的预编译产物指向 nightly [b12359](https://github.com/ggml-org/llama.cpp/releases/tag/b12359)，配套说明见 [HF 博客](https://huggingface.co/blog/ggml-org/llama-cpp-v1)。
证据：[v1.0.0 Release](https://github.com/ggml-org/llama.cpp/releases/tag/v1.0.0) · [ggml v1.0.0](https://github.com/ggml-org/ggml/releases/tag/v1.0.0) · [官方说明](https://huggingface.co/blog/ggml-org/llama-cpp-v1)

2. **Transformers v5.23.0：Inkling 2 / LFM3，以及统一导出 API**
Hugging Face Transformers 于 11-13 22:10（Asia/Singapore）发布正式版 v5.23.0（`prerelease=false`）。新接入包括 Thinking Machines Lab 的 Inkling 2 Small（发布说明写明 594B 总参数、17B 激活的多模态 MoE）、Liquid AI 的 LFM3 与 LFM3-VL，以及 Dots 3 Note Preview、IQuestCoder、InternLM3；另有实验性的 JEV decision head（文档标明 API 仍可能变，不宜直接当生产接口）。破坏性变更集中在专家并行：去掉 `ep_router` 风格，MXFP4 GPT-OSS 专家改走 `ep_dispatch_experts`。更值得跟的是统一导出：`ExportedModel` 把 Dynamo / ONNX Runtime / OpenVINO / ExecuTorch 收成同一套导出、推 Hub、再加载的接口；发布说明自称 OpenVINO 导出后 decode 比未融合图快 2.4–3.9 倍（标「自称」）。做新模型接入、还在用旧 EP 路由、或要把模型导到 ORT / OpenVINO 的人应先看 breaking 清单。
证据：[v5.23.0 Release](https://github.com/huggingface/transformers/releases/tag/v5.23.0) · [huggingface/transformers](https://github.com/huggingface/transformers)

3. **OpenAI Codex 0.168.0 / 0.169.0**
`openai/codex` 在窗口内连续发布两个正式版：0.168.0 于 11-13 11:54（Asia/Singapore），0.169.0 于 11-13 16:37（Asia/Singapore），均为 `prerelease=false`（同窗口多枚 `*-alpha.*` 未收）。0.168 让终端里可以浏览并切换模型供应商、用可选的 `features.tui_workspace` 开侧边对话，并支持给具备音频能力的模型附加录音，以及可选的 GIF 生成 / 编辑。0.169 把侧边工作区做成多标签并可在重启后恢复本地侧边会话，可在终端里添加自定义模型供应商，并修了 `codex exec`：即使加了 `--sandbox workspace-write`，在未信任目录里仍保持项目配置和 MCP 关闭，要用 `--trust` 才显式放行。上期只见到 0.167 的细补丁，这一波才是终端工作流和安全默认值的实质变化；日常用 Codex TUI、或在脚本里跑 `codex exec` 的人应该升。
证据：[0.169.0 Release](https://github.com/openai/codex/releases/tag/rust-v0.169.0) · [0.168.0 Release](https://github.com/openai/codex/releases/tag/rust-v0.168.0)

4. **deepseek-ai/chat-demo**
DeepSeek 官方组织于 11-12 16:08（Asia/Singapore）公开本仓，MIT，截至 11-15 08:51（Asia/Singapore）约 **1,753 星（总量）**，是窗口内新仓星数第一且身份可核（组织 `deepseek-ai`，在线页 [deepseek-ai.github.io/chat-demo](https://deepseek-ai.github.io/chat-demo/)）。它是一个无应用后端的静态聊天演示：浏览器直连你配置的 API，支持多会话、流式回复、深度思考、联网检索、附件、语音输入和朗读；默认用 `deepseek-flash`，走 Anthropic 兼容的 Messages / Files 接口（这是客户端默认模型标识，不是本期新开源的权重发布）。源码目录与 README 相符，窗口内有正式包 v0.1.0 / v0.1.1。API 密钥存在浏览器 localStorage，对话在 IndexedDB。想本地或静态托管一套官方聊天界面、或对接 DeepSeek 兼容接口的人可以直接用；不要把密钥提交进仓库，也不要把它当成新模型发布。
证据：[deepseek-ai/chat-demo](https://github.com/deepseek-ai/chat-demo) · [在线演示](https://deepseek-ai.github.io/chat-demo/) · [v0.1.1 Release](https://github.com/deepseek-ai/chat-demo/releases/tag/v0.1.1)

（热榜口径：日榜约为最近 24 小时，周榜统计最近七天，均于 2026-11-15 08:51 Asia/Singapore 抓取，不可当作本期 72h 净增。周榜前列 meta/astryx 约 13,660 stars this week，上期已报，仅留榜。google/elephant-goldfish-model 周榜约 5,539、总量约 19,200，但最近正式版仍是窗口前的 v0.1.1，本期不单列。alibaba/open-code-review 日榜约 893、总量约 51,438，窗口内仅为 v1.13.8 / v1.13.9 补丁；Tencent/LoopForge 日榜约 33、总量约 909，正式版 v0.3.8 以修复为主、v0.3.9-rc.1 为预发布，均不作为本期主条。新仓搜索除 chat-demo 外，前列大量重复的 IPTV /「Copilot 桌面应用」/ Agent 安装包克隆，未收录。`ranxianglei/billion-context` 仍无新的可交叉核验进展，继续不收录。）

窗口内无：vllm-project/vllm、sgl-project/sglang、ollama/ollama、pytorch/pytorch、huggingface/datasets、anthropics/anthropic-sdk-python、anthropics/anthropic-sdk-typescript、modelcontextprotocol/python-sdk、modelcontextprotocol/typescript-sdk、comfyanonymous/ComfyUI、unslothai/unsloth、axolotl-ai-cloud/axolotl（常规 / 预发布未收录：llama.cpp 的 `b12xxx` 日构建；openai/codex 多枚 `*-alpha.*`；openai-python v3.50.0 / v3.51.0 与 openai-node v7.56.0 / v7.57.0 为 Responses 推理输入变换，以及 agent / 图像 / Live / 外部密钥支持扩展；langchain-openai 1.8.0；langgraph 1.2.21–1.2.22 / prebuilt 1.1.2 / checkpoint 4.3.2 / checkpoint-postgres 3.2.1 / cli 0.4.43）


## 模型与数据集

### 模型、数据与榜单原始材料

#### HF / 模型三日雷达素材 · 2026-11-15

- 窗口：2026-11-12 09:30 Asia/Singapore（01:30 UTC，上期采集截止）→ 2026-11-15 约 09:00 Asia/Singapore（01:00 UTC，实际采集时刻）。
- 去重基线：11/12 素材包（内部证据存档），sha256 0e564ad0…944）以及 （内部证据存档） 的榜单快照和镜像核查。上期写过的条目只在有新事实时才写，并标为“更新”。
- 计数：主条 4（新 2、更新 2）｜跟进 2（Kimi K3.1 Pro、Nex-N2.6）｜次条 6（另有 1 条窗口前发布、被漏掉的补记）｜榜单 6 段｜数据集 4 条主条 + 2 条附记｜冒名/同名镜像 1 组（7 个 Kimi 同名 repo、1 个 12GB 复制件，另列 2 个原样转存）。
- 数据口径：likes/downloads 统一取 HF API 在 2026-11-15 09:00 Asia/Singapore（01:00 UTC）的快照（采集证据快照）。downloads 是 HF 的近 30 天口径。Trending 取 08:51 Asia/Singapore 的 API（模型 300 条、数据集 100 条）。
- 开放程度用语：“开放权重”= 权重能下载；“OSI 许可”= 权重许可证属于 OSI 认可的许可证（Apache-2.0/MIT），未逐项核对 OSAID；“自定义/非商用许可”= 权重开放，但不算开源。

##### 三句话结论

1. **Inkling 2 Small 从闭源变成了 Apache-2.0 开放权重。** Thinking Machines 在 11-13 03:53 Asia/Singapore 推送了 594B/17B 激活的 NVFP4 权重（393GB），另有 MXFP8 版。AA 和 LMArena 都已把它改标为开放许可，在 AA v5 默认视图里，它在 permissive 许可类别中排第 2（30.6，仅次于 DeepSeek V4.1 Flash 1017 的 32.6），在开放权重整体中排第 4。
2. **MiniMax-H3-Image 第一次进 LMArena 文生图榜，排 #23（1197±11）。** 在 LMArena 上，它排在 Qwen-Image-2.1 和 Ideogram 4.0 后面，不是开放权重里的第一。AA 把它的发布日期从 07-31 改成 11-10，是同一个记录 ID，所以和 HF checkpoint 是同一个模型。许可证文件与上期逐字节一致。
3. **两个跟进项都没有出现能改变判断的新事实。** Kimi K3.1 Pro 官方 repo 没有新 commit，博客仍写“will be released by Nov 4”，同名全量镜像又多了 6 个。Nex-N2.6 的 OSWorld 83.0 仍然没有独立复现；唯一的外部测试（Plotly）只测到与基座 GLM-5.3-Flash 打平，并出现了长时间的工具调用循环。

---

##### 主条

###### 1. thinkingmachines/Inkling-2-Small（+ Inkling-2-Small-MXFP8）· 新开放权重（Apache-2.0，OSI 许可）

这是窗口内唯一一个来自一线实验室、全量放出、许可又是 Apache-2.0 的大模型：594B 总参数 / 17B 激活的 MoE，支持图像输入和 1M 上下文。它在 11/05 先以闭源 API 的形式发布（上期 AA 段按闭源记录），11/12 完成外部安全测试后才放出权重。AA 的独立分数 30.6，和厂商说的“31”一致；但在 LMArena 文本榜上，它目前只排 #152（Prelim），低于自家第一代 Inkling（#95）。

- 为什么重要：
  - “先闭源、安全测试后开放”的路径在一个 600B 级模型上完整走了一遍。
  - 权重以 NVFP4 原生精度发布（预训练、中训练、后训练都在 NVFP4 下完成）。这对“开放权重 = BF16 大文件”的惯例是一个变化。
  - 第三方的 SGLang、vLLM、Unsloth 在当天就做了适配。
- 适合谁 / 阅读建议：
  - 有 2×B300 或 4×H200（聚合显存 ≥500GB）的团队可以直接自托管。
  - 普通用户走 Together、Fireworks、Cloudflare 等 API 更现实。Plotly 写的价格是 $0.30/$1.00 每百万 token。
  - 关注安全路线的读者可以读官方公告里的“safe path to open weights”一段。
- 来源记录：
  - HF 时间：createdAt 2026-11-04 19:51 UTC / 11-05 03:51 Asia/Singapore；lastModified 2026-11-13 21:12 UTC / 11-14 05:12 Asia/Singapore。repo 创建于 11/04，但 commit 历史里最早一条就是权重 commit `78cb6c0ef6`“upload model”，时间 2026-11-12 19:53 UTC / 11-13 03:53 Asia/Singapore。之后是 transformers 库名、chat template 修复、补量化配置以修正 Hub 参数计数、追加社区评测结果和 README（11-12 20:58 至 11-13 21:12 UTC）。
  - 热度：likes 317 / downloads 3,647（采集 11-15 09:00 Asia/Singapore）；HF Trending #11（trendingScore 303，08:51 Asia/Singapore）。
  - 许可 / 任务：license apache-2.0，pipeline image-text-to-text。开放权重，OSI 许可。repo 里没有单独的 LICENSE 文件，许可来自卡片元数据，以及官方模型卡写的“License: Apache 2.0”。
  - 权重证据：主 repo 有 25 个 safetensors，合计 393.48GB（NVFP4/MXFP8 混合）。HF 解析出的参数量是 594,050,672,720。
  - MXFP8 版 thinkingmachines/Inkling-2-Small-MXFP8：createdAt 2026-11-04 19:51 UTC / 11-05 03:51 Asia/Singapore；lastModified 2026-11-13 21:27 UTC / 11-14 05:27 Asia/Singapore，权重 commit `544ad43d97` 在 2026-11-12 19:53 UTC。49 个 safetensors，合计 622.80GB；likes 13 / downloads 482（采集 11-15 09:00 Asia/Singapore）。
  - 官方身份：repo 属于 thinkingmachines 组织（显示名 Thinking Machines Lab，未认证，2,087 关注者）。同组织此前发过 Inkling、Inkling-Small（likes 458 / downloads 1,048,795（采集 11-15 09:00 Asia/Singapore）。官方公告页 11/05 发布，11/12 加了一段 Update，写明权重已上 HF；官方模型卡直接链接这两个 HF repo。
  - 规格（官方模型卡）：48 层，384 个专家，每 token 路由 8 个；局部/全局混合注意力；ViT 图像编码；1M 上下文。NVFP4 版需要聚合显存 ≥500GB（2×B300 或 4×H200），MXFP8 版需要 ≥800GB。官方说 MXFP8 只比 NVFP4 高 1–2 个百分点，推荐用 NVFP4。
  - 榜单：
    - AA Intelligence v5：30.6，open-weights 标记从 false 变为 true，许可类别从 proprietary 改为 permissive。在默认视图里位列 DeepSeek V4.1 Flash 1017（32.6）和 GLM-5.3（31.7）之后，见 B6。
    - LMArena 文本：#152，1412±12，Prelim，2,669 票；许可列从“Proprietary”改为“Apache 2.0”。
  - 外部独立测试：Plotly DataAnalyticsBench 43 题答对 39 题，花费 $1.81，每题中位 13 秒。这是 Plotly 测过的美国实验室开放权重模型里的最高分，单次运行。
- 待核：
  - 卡片和公告自报的基准（BrowseComp、ARC-AGI-2、SWE 系列等）都是厂商数字，未复现。AA 30.6 是目前唯一的第三方综合分。
  - LMArena 只有 2,669 票，排名区间很宽。它低于第一代 Inkling 的原因（风格、长度控制，或样本不足）待观察。
  - 公告提到后期训练数据大量来自其他模型的轨迹（Plotly 转述其中包括 Kimi K3）。这对下游合规有什么影响，需要读原文判断。
- 衍生（降权，只列有代表性的）：
  - 同名原样转存 TechnoBaptist/Inkling-2-Small：26/26 个 LFS 文件的 sha256 与官方一致，Apache-2.0 允许转存，不算冒名，但应引导读者用官方 repo。
  - 量化版 mlx-community/Inkling-2-Small-oQ4e、Baekpica/Inkling-2-Small-VQ-GGUF（likes 0 / downloads 922（采集 11-15 09:00 Asia/Singapore）。
  - Uncensored 改包 OpenUncensored/Inkling-2-Small-Uncensored：过滤。
  - 窗口内按名称能搜到 20 个新衍生 repo。
- 证据：
  - [HF thinkingmachines/Inkling-2-Small](https://huggingface.co/thinkingmachines/Inkling-2-Small)
  - [HF thinkingmachines/Inkling-2-Small-MXFP8](https://huggingface.co/thinkingmachines/Inkling-2-Small-MXFP8)
  - [thinkingmachines.ai 来源](https://thinkingmachines.ai/news/inkling-2-small/)
  - [thinkingmachines.ai 来源](https://thinkingmachines.ai/model-card/inkling-2-small/)
  - [sglang.io 来源](https://www.sglang.io/blog/inkling-2-small-day0-support)
  - [plotly.com 来源](https://plotly.com/blog/inkling-2-small-plotly-data-analytics-bench/)
  - 本地：（采集证据快照）、（采集证据快照）、（采集证据快照）、（采集证据快照）

###### 2. higurashi-ai/Haru-4B · 新发布（开放权重，Apache-2.0，OSI 许可）

一家小团队（higurashi）放出的全双工语音对话基座模型：能边听边说，学会了附和、打断、抢话这类真实对话行为。Apache-2.0，单个 10.5GB 权重文件；第三方文章（explainx）称约 12GB 显存可以跑，待核。在窗口内新建的 repo 里，它的 Trending 排名最高（#19）。但它是预训练基座，不是指令助手。

- 为什么重要：
  - 开放的全双工语音模型很少。它用 7.5Hz 连续音频潜变量加单步 MeanFlow 头，把三路流（用户音频、模型音频、文本）相加，而不是交错排列，上下文长度因此降到交错方案的 1/3。
  - 训练数据是 4,000 万小时真实语音，官方说明刻意排除了 LLM 生成和 TTS 合成的对话。
- 适合谁 / 阅读建议：做实时语音交互、语音 agent 研究的人。想要“开箱即用助手”的读者要等后续微调版。
- 来源记录：
  - HF 时间：createdAt 2026-11-12 11:05 UTC / 11-12 19:05 Asia/Singapore；lastModified 2026-11-13 01:22 UTC / 11-13 09:22 Asia/Singapore。全仓库只有一个 commit，`8d6e83bcd3`“Haru-4B”，在 2026-11-13 01:22 UTC / 09:22 Asia/Singapore，权重在这个 commit 里推送。
  - 热度：likes 232 / downloads 1,262（采集 11-15 09:00 Asia/Singapore）；HF Trending #19（trendingScore 217）。
  - 许可 / 任务：license apache-2.0，pipeline audio-to-audio。开放权重，OSI 许可。
  - 权重证据：1 个 safetensors，10.54GB。HF 解析参数量 5,270,000,897：名字叫 4B，是因为骨干是 Qwen3.5-4B，另加音频模块，实际约 5.27B。
  - 官方身份：higurashi-ai 组织（显示名 higurashi，未认证，46 关注者，2 个模型）。博客致谢里写明受日本经产省/NEDO 的 GENIAC 项目和 AWS 支持；训练用了 256 张 B200，约 8 天。官方技术博客（2026-11-13，作者 Rikuto Kotoge）和 GitHub higurashi-ai/Haru 互链到这个 HF repo。
  - 规格（博客）：语音分词器沿用 VibeVoice 的连续 tokenizer；主攻 9 种语言（英、西、葡、德、法、中、日、俄、韩），训练数据覆盖 160 多种语言；训练用的全双工对话最长 60 分钟；可以用文本卡设定角色，用参考音频设定音色。
- 待核：
  - “MacBook（M1 Max）端到端约 65ms 延迟”是厂商数字，而且博客注明：这是 int8 权重下的数字，不含音频分帧；按 7.5Hz 分帧，最多还要再加 133ms 的算法延迟。转述时不要只写 65ms。
  - 博客没有给出与 Moshi 等同类模型的标准化对比。
  - 同名 repo botp/Haru-4B 是原样转存，2/2 个 LFS 文件 sha256 一致（likes 0 / downloads 20（采集 11-15 09:00 Asia/Singapore），Apache-2.0 允许转存。
- 证据：
  - [HF higurashi-ai/Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B)
  - [blog.higurashi.ai 来源](https://blog.higurashi.ai/melte/haru4b/)
  - [GitHub higurashi-ai/Haru](https://github.com/higurashi-ai/Haru)
  - 第三方：[explainx.ai 来源](https://explainx.ai/blog/haru-4b-open-full-duplex-speech-model-apache-qwen3-5-higurashi-2026)

###### 3. MiniMax-H3-Image 跟进：LMArena 首次上榜 + AA 日期更正 · 更新

上期的待核点都有了答案。(1) AA 上那个 releaseDate 写 2026-07-31 的“H3-Image”，现在改成了 2026-11-10，记录 ID（9b61629e…）不变，openWeightsUrl 指向 HF 官方 repo，所以就是这次开放的 checkpoint。(2) LMArena 文生图榜在 Nov 12 的刷新中首次收录 MiniMax H3-Image，#23，1197±11。(3) 许可证没有变。HF 官方 repo 在窗口内只有 1 次 README 改动，没有新权重。

- 为什么重要：
  - 这是它第一份人类偏好盲测分。它在 LMArena 上排在 Qwen-Image-2.1（#21，1227）和 Ideogram 4.0（#22，1199）之后，所以“开放权重文生图第一”的说法在 LMArena 上不成立。
  - 在 AA 图像榜上，因为新进了 Kling Image 4.0 和 Canva Craft，它从 t2i #23 退到 #25、编辑从 #11 退到 #13，分数本身基本没动。
- 适合谁 / 阅读建议：上期已经介绍过模型本身。本期只需要更新榜单位置，并提醒读者：社区 GGUF 版已经可以在小显存上跑，但许可证照旧（EU/UK/韩国/美国排除，年营收超过 100 万美元需要授权）。
- 来源记录：
  - HF：createdAt 2026-11-03 06:34 UTC / 11-03 14:34 Asia/Singapore；lastModified 2026-11-12 01:52 UTC / 11-12 09:52 Asia/Singapore。窗口内唯一的 commit 是 `5f90473023`“Update README.md (#18)”，在 2026-11-12 01:52 UTC / 09:52 Asia/Singapore；权重树仍停在 11-10。
  - 热度：likes 1,117 / downloads 517,948（采集 11-15 09:00 Asia/Singapore）（上期 likes 720 / downloads 142,989）；HF Trending #2（trendingScore 1017）。
  - 许可 / 任务：license other（minimax-h3-image-community-license-agreement），pipeline text-to-image。开放权重，自定义许可，不是 OSI。main 上的 LICENSE 的 sha256 是 0ec3bb5e…423b，与上期保存的 （采集证据快照） 逐字节一致。
  - LMArena 文生图（WebFetch，11-15 约 08:54 Asia/Singapore）：数据日期 Nov 8 → **Nov 12**，总票数 6,874,394 → 6,934,037，模型数 84 → 85，新增的就是 MiniMax H3-Image（#23，1197±11，3,277 票），许可列写 minimax-h3-image-community-license-agreement。
  - AA：
    - t2i：H3-Image #25，1066±14，3,258 票；H3-Image Highspeed #24，1072±14。
    - 编辑：H3-Image #13，1137±16；Highspeed #14，1134±16。
    - 两个记录的 releaseDate 都从 2026-07-31 改成了 2026-11-10，introducedAt 不变（11-10 22:20 UTC）。见 （采集证据快照）。
  - 衍生：unsloth/MiniMax-H3-Image-GGUF，createdAt 2026-11-12 12:00 UTC / 11-12 20:00 Asia/Singapore；lastModified 2026-11-13 14:42 UTC / 11-13 22:42 Asia/Singapore，GGUF commit `2eda8f761a` 在 11-13 14:42 UTC，14 个权重文件合计 185GB（多档量化），likes 10 / downloads 2,152（采集 11-15 09:00 Asia/Singapore），沿用原许可。窗口内按名称能搜到至少 42 个新衍生 repo（搜索结果上限 100 条，所以是下限）。
- 待核：
  - LMArena 只有 3,277 票，排名会继续浮动。
  - AA 上的 Highspeed 版没有 openWeightsUrl，是否对应某个公开权重待核。
- 证据：
  - [HF MiniMaxAI/MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)
  - [HF unsloth/MiniMax-H3-Image-GGUF](https://huggingface.co/unsloth/MiniMax-H3-Image-GGUF)
  - [lmarena.ai 来源](https://lmarena.ai/leaderboard/text-to-image)
  - [artificialanalysis.ai 来源](https://artificialanalysis.ai/image/leaderboard/text-to-image)
  - 本地：（采集证据快照）（全表 85 行）、（采集证据快照）、（采集证据快照）

###### 4. Zyphra/ZONOS3-Mini 跟进：技术报告发布 · 更新

上期写“官方尚未发技术报告”，现在已经发了：arXiv 2611.16525（11/12 提交）。报告把架构、数据、训练和评测都写清楚了，也修正了几个上期引用的数字：总参数是 886M（不是博客说的约 800M），激活 100M；在自建的 ZTTS2-Eval 上，55 个语言子集的宏平均 WER 是 6.71%。Zyphra 同时把 ZTTS2-Eval 的 Mini 子集发到 HF。repo 热度在三天内翻了几倍。

- 为什么重要：开放 TTS 里少有把训练和评测细节写到这个程度的报告。报告还放出了在其他开放 TTS 上跑的同口径对比（Fish Audio Drama 3、OmniVoice、VoxCPM2 等），可以独立复查。
- 适合谁 / 阅读建议：做 TTS 的工程师可以直接读第 3 节（ZAC-1 编解码器）和第 9 节（推理和量化）。普通读者只需要知道：它报告的 WER 并不是最低的。同表里 Fish Audio Drama 3 宏平均 4.74，ZONOS2 是 6.22。它的卖点是小和快。
- 来源记录：
  - HF：createdAt 2026-11-09 05:03 UTC / 11-09 13:03 Asia/Singapore；lastModified 2026-11-14 05:48 UTC / 11-14 13:48 Asia/Singapore。窗口内的 commit：
    - `15fb29d778`（11-13 00:08 UTC）：给 backbone-ptq-edit.gguf 加了 143 行文本 token。
    - `727302c1cb`（11-13 18:55 UTC）：卡片加入 arXiv 2611.16525 引用。
    - `d2d142a86b`（11-14 05:48 UTC）：web/laci 加入 44 种语言的 LACI 头。
    - 没有看到主 backbone 重训的 commit。
  - 热度：likes 345 / downloads 19,743（采集 11-15 09:00 Asia/Singapore）（上期 likes 174 / downloads 4,170）；HF Trending #10（trendingScore 305）。
  - 许可 / 任务：license apache-2.0，pipeline text-to-speech。开放权重，OSI 许可。
  - transformers 版 Zyphra/ZONOS3-Mini-hf：likes 7 / downloads 257（采集 11-15 09:00 Asia/Singapore），11-13 20:59 UTC 对齐了语言支持说明。
  - 技术报告要点（arXiv 2611.16525，作者 Gabriel Clark、Beren Millidge 等）：
    - 11 层：9 层 GDN + 2 层全局注意力，latent MoE。
    - ZAC-1 编解码器：15Hz、1.80kbit/s、44.1kHz。
    - 预训练语料 6.1M 小时，375k 步，约 4.5T token。
    - 在 Pixel 9 上首包音频 <800ms，M3 MacBook Air 上 <450ms（WebGPU 运行时）；H100 上流式首包 0.25–0.36s。
  - 数据集 Zyphra/ztts2_eval_mini：见数据集 D4。
- 待核：
  - 报告的 WebGPU 首包延迟（M3 MacBook Air <450ms）与上期引用的官方博客数字“TTFA <150ms（M3 MacBook Air）”对不上。可能是运行时或测量口径不同，转述时请注明出处，不要混用。
  - ZTTS2-Eval 是 Zyphra 自建的评测，他人系统的分数也是 Zyphra 跑的。
- 证据：
  - [arXiv 2611.16525](https://arxiv.org/abs/2611.16525)
  - [HF Zyphra/ZONOS3-Mini](https://huggingface.co/Zyphra/ZONOS3-Mini)
  - [HF 数据集 Zyphra/ztts2_eval_mini](https://huggingface.co/datasets/Zyphra/ztts2_eval_mini)
  - 本地：（采集证据快照）

---

##### 跟进（无新权重，只更新状态）

###### F1. Kimi K3.1 Pro：官方 repo 和博客都没变，同名全量镜像又多 6 个 · 更新

- 判断：这三天没有官方层面的新事实。变化在热度和周边：LMArena 票数在增加，NVIDIA NVFP4 版的下载开始起量，HF 上同名全量镜像继续增加。
- 官方权重：moonshotai/Kimi-K3.1-Pro createdAt 2026-11-02 04:13 UTC / 11-02 12:13 Asia/Singapore；lastModified 2026-11-05 07:11 UTC / 11-05 15:11 Asia/Singapore，窗口内没有 commit。likes 2,078 / downloads 43,687（采集 11-15 09:00 Asia/Singapore）（上期 likes 1,935 / downloads 33,617）；HF Trending #9。license other（kimi-k3.1-pro），pipeline image-text-to-text，开放权重，自定义许可。
- 博客：本期重抓 kimi.ai/blog/kimi-k3-1-pro，可见文本与上期相比只差首尾空白，正文一致，仍写“The full model weights will be released by Nov 4”（采集证据快照）。这是文案滞后，不代表权重未发布。
- NVFP4：nvidia/Kimi-K3.1-Pro-NVFP4 createdAt 2026-11-11 00:57 UTC / 11-11 08:57 Asia/Singapore；lastModified 2026-11-12 02:26 UTC / 11-12 10:26 Asia/Singapore。窗口内只有 `3af0462972`“Add SGLang instructions (#1)”（11-12 02:26 UTC / 10:26 Asia/Singapore），权重没变。likes 19 / downloads 783（采集 11-15 09:00 Asia/Singapore）（上期 likes 4 / downloads 0）。
- LMArena 文本：数据日期 Nov 9 → Nov 11。Kimi K3.1 Pro (Max) 仍是 #24：1483±11 / 3,443 票 → 1485±10 / 3,995 票，rank spread 9–50。Kimi K3 (Max) 是 #20（1487±4）。vision 榜（Nov 8，未刷新）里仍然没有 K3.1 Pro。
- AA：46.5，仍是 v5 默认视图里开放权重的第一名。
- 同名镜像：详见末尾“冒名/同名镜像”。
- 证据：[HF moonshotai/Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) · [HF nvidia/Kimi-K3.1-Pro-NVFP4](https://huggingface.co/nvidia/Kimi-K3.1-Pro-NVFP4) · [kimi.ai 来源](https://www.kimi.ai/blog/kimi-k3-1-pro) · [lmarena.ai 来源](https://lmarena.ai/leaderboard/text)

###### F2. Nex-N2.6：OSWorld 仍无独立复现；第一份外部测试只与基座打平 · 更新

- 判断：OSWorld 83.0 仍然只是 Nex-AGI 的自报数字。AA 没有收录 Nex-N2.6（只有旧的 Nex-N2-Pro）。网页检索也没有找到独立的 OSWorld 复现（本期没有逐条核对 OSWorld 官方榜）。唯一能找到的独立测试来自 Plotly：43 题答对 38 题，和基座 GLM 5.3 Flash 完全相同；隐藏规律题 5 题只找到 1 题（基座找到 4 题）。另有两题陷入工具调用循环（约 1,670 次调用、2 小时 20 分钟；约 650 次调用、70 分钟），一次完整运行的成本是 $10.19，基座只要 $0.69。这和它主打的“减少重复”正好相反，不过 Nex 测的是推理里的重复，Plotly 看到的是工具调用的重复，两者不是同一个指标。
- HF：nex-agi/Nex-N2.6 createdAt 2026-11-10 05:34 UTC / 11-10 13:34 Asia/Singapore；lastModified 2026-11-11 15:03 UTC / 11-11 23:03 Asia/Singapore，窗口内没有 commit。likes 84 / downloads 593（采集 11-15 09:00 Asia/Singapore）（上期 likes 41 / downloads 0）。license apache-2.0，pipeline image-text-to-text。
- 注意：Plotly 的文章日期是 11/11，早于本窗口，但上期没有收录，这次作为新找到的外部证据补上。Plotly 自己也说明这只是单次运行，分数在不同运行之间可能浮动最多 3 分。
- 证据：[plotly.com 来源](https://plotly.com/blog/nex-n2-6-plotly-data-analytics-bench/) · [HF nex-agi/Nex-N2.6](https://huggingface.co/nex-agi/Nex-N2.6) · 本地 （采集证据快照）

---

##### 次条（新发布，信号弱或场景窄）

- **facebook/meta-encoder-v1**：Meta 的 28.4B 多模态嵌入模型，文本、图像、视频共用一个编码器，输出 6656 维向量，另有一个 `decide` 接口用于问答式判断。createdAt 2026-11-12 02:00 UTC / 11-12 10:00 Asia/Singapore；lastModified 2026-11-12 04:50 UTC / 11-12 12:50 Asia/Singapore；权重 commit `d5de844154` 在 2026-11-12 04:31 UTC / 12:31 Asia/Singapore；12 个 safetensors，56.95GB。likes 37 / downloads 248（采集 11-15 09:00 Asia/Singapore）；license 未填写，pipeline feature-extraction，卡片里也没有找到许可说明，所以能否商用待核。卡片写需要 transformers ≥5.15 才支持其骨干 `muse_glimmer`，可能与 Muse 系列相关，待核。[HF facebook/meta-encoder-v1](https://huggingface.co/facebook/meta-encoder-v1)
- **LiquidAI/Liquid-Codec**：LFM3-Audio/Omni 背后的流式语音编解码器，73.6M 参数。createdAt 2026-09-16 21:24 UTC / 09-17 05:24 Asia/Singapore；lastModified 2026-11-12 19:27 UTC / 11-13 03:27 Asia/Singapore；repo 9/16 就创建了，但第一条 commit `a937bd2121`“Release LiquidCodec”在 2026-11-12 17:45 UTC / 11-13 01:45 Asia/Singapore，这才是公开时间。likes 92 / downloads 9,714（采集 11-15 09:00 Asia/Singapore）；license other（lfm1.0），pipeline feature-extraction（LFM 自定义许可，非 OSI）。“单线程 CPU 编码 361 倍实时”是厂商数字。[HF LiquidAI/Liquid-Codec](https://huggingface.co/LiquidAI/Liquid-Codec) · [liquid.ai 来源](https://www.liquid.ai/blog/liquidcodec)
- **KittenML/kitten-tts-2-mini / -pico**：超小 TTS。Mini 82M 参数，16 种语言，118 个音色，int8 ONNX 82.7MB，只用 CPU 就能跑。Mini createdAt 2026-11-13 03:34 UTC / 11-13 11:34 Asia/Singapore；lastModified 2026-11-13 03:34 UTC / 11-13 11:34 Asia/Singapore，权重 commit `c01797caec` 在 11-13 03:34 UTC；likes 11 / downloads 346（采集 11-15 09:00 Asia/Singapore）；license apache-2.0，pipeline text-to-speech。Pico：likes 7 / downloads 168（采集 11-15 09:00 Asia/Singapore）。[HF KittenML/kitten-tts-2-mini](https://huggingface.co/KittenML/kitten-tts-2-mini)
- **inclusionAI/Duo-1.0-causal-base（及 Duo-1.2）**：蚂蚁 inclusionAI 的全双工音视频“交互世界模型”，基于 MiniMax-H3，所以沿用 minimax-h3-community-license。createdAt 2026-11-12 06:32 UTC / 11-12 14:32 Asia/Singapore；lastModified 2026-11-13 08:24 UTC / 11-13 16:24 Asia/Singapore；权重在 11-13 05:59–06:01 UTC 用 upload-large-folder 推送，PyTorch DCP 格式，权重 153GB。likes 1 / downloads 0（采集 11-15 09:00 Asia/Singapore）：DCP 格式可能不计入下载数，热度信号弱。论文 [arXiv 2611.15131](https://arxiv.org/abs/2611.15131) （11/11 提交）。[HF inclusionAI/Duo-1.0-causal-base](https://huggingface.co/inclusionAI/Duo-1.0-causal-base)
- **migtissera/Tess-4.5-594B-A17B**：Inkling 2 Small 的第一个大规模微调版（Continuity Research）。createdAt 2026-11-13 03:31 UTC / 11-13 11:31 Asia/Singapore；lastModified 2026-11-13 20:53 UTC / 11-14 04:53 Asia/Singapore；权重在 11-13 03:39 UTC 推送，25 个 safetensors，393GB。likes 16 / downloads 50（采集 11-15 09:00 Asia/Singapore）；license apache-2.0，pipeline image-text-to-text。“SWE-Bench Pro v2 Hard 88.2%（基座 86.3%），输出 token 减少 9%”是作者自报，只测了 51 题，待核。[HF migtissera/Tess-4.5-594B-A17B](https://huggingface.co/migtissera/Tess-4.5-594B-A17B)
- **opencerebral/Boris-2-Think + 数据集 slmconsortium/OpenThink**：144M 参数的小型推理模型，加上 43,101 条短推理轨迹。模型 createdAt 2026-11-12 06:41 UTC / 11-12 14:41 Asia/Singapore；lastModified 2026-11-14 00:23 UTC / 11-14 08:23 Asia/Singapore；likes 10 / downloads 184（采集 11-15 09:00 Asia/Singapore）；license apache-2.0，pipeline text-generation。卡片反复改动“V100”的描述，信号弱。[HF opencerebral/Boris-2-Think](https://huggingface.co/opencerebral/Boris-2-Think)

###### 补记：窗口前发布、往期漏掉的（不算本期新发）

- **Edge0/Edge0-145B-NVFP4（及 -q3k）**：基于 Qwen3.8-Flash-Next 的 145B latent MoE（512 专家，每 token 10 个路由专家 + 1 个共享专家），主打“一张 24GB 消费卡跑 145B agent”。createdAt 2026-11-11 05:22 UTC / 11-11 13:22 Asia/Singapore；lastModified 2026-11-14 10:05 UTC / 11-14 18:05 Asia/Singapore；权重在 11-11 12:59 UTC 推送，早于本窗口，上期漏收。窗口内只有文档 commit（例如 11-14 10:05 UTC 补了 macOS 支持说明）。11 个权重文件，112.84GB。likes 260 / downloads 33,819（采集 11-15 09:00 Asia/Singapore）；HF Trending #15。license other（edge0-community-model-1.0），pipeline text-generation，自定义许可，非 OSI。q3k 版：likes 68 / downloads 27,373（采集 11-15 09:00 Asia/Singapore）。
  - 卡片说 RTX 5090 D 24GB 上 agent decode 98.3 tok/s、terminal-bench 2.1 86.5。
  - 卡片的小字写明运行时用的是 23.25GiB 显存 + 38.27GiB 内存（专家驻留在主机内存），所以“一张卡”需要大内存配合。
  - 都是厂商数字，待核。组织背景不明。
  - [HF Edge0/Edge0-145B-NVFP4](https://huggingface.co/Edge0/Edge0-145B-NVFP4)

---

##### 数据集

- **D1. llamaindex/ParseBench-2**：LlamaIndex 的文档解析基准第二版。六个维度：文本、格式、表格、图表、版面定位、表单；4,317 个页面级测试用例，来自 2,645 份文档；140 多种错误类型，按严重程度设上限分。createdAt 2026-10-29 00:58 UTC / 10-29 08:58 Asia/Singapore；lastModified 2026-11-14 01:34 UTC / 11-14 09:34 Asia/Singapore；repo 10/29 就创建了，但第一条 commit `7a2b095e18`“ParseBench-2”在 2026-11-12 06:12 UTC / 14:12 Asia/Singapore，属于窗口内公开；11-14 有一次标注更正。likes 11 / downloads 29,263（采集 11-15 09:00 Asia/Singapore）；license apache-2.0，pipeline 未填写。它已经注册为 HF benchmark（eval.yaml）。[HF 数据集 llamaindex/ParseBench-2](https://huggingface.co/datasets/llamaindex/ParseBench-2) · [GitHub run-llama/ParseBench](https://github.com/run-llama/ParseBench)
- **D2. ropedia-ai/Ropedia-Xperience-2**：具身/物理 AI 数据。全集是 1,500 多个 LiDAR 扫描场景和 4,000 多段第一人称录制（131 小时），配手部和身体姿态。第一批已上线：126 个场景，约 1.07TB。createdAt 2026-11-13 02:30 UTC / 11-13 10:30 Asia/Singapore；lastModified 2026-11-13 08:12 UTC / 11-13 16:12 Asia/Singapore；likes 13 / downloads 4,408（采集 11-15 09:00 Asia/Singapore）；license cc-by-nc-4.0，pipeline 未填写，非商用。论文 [arXiv 2611.17060](https://arxiv.org/abs/2611.17060) 。[HF 数据集 ropedia-ai/Ropedia-Xperience-2](https://huggingface.co/datasets/ropedia-ai/Ropedia-Xperience-2)
- **D3. TeraTTS/webinars**：俄语网络研讨会的语音和 ASR 转写，10 万–100 万条量级。createdAt 2026-11-12 16:09 UTC / 11-13 00:09 Asia/Singapore；lastModified 2026-11-14 15:21 UTC / 11-14 23:21 Asia/Singapore；11-12 17:35 UTC 首发；11-13 去掉音乐片段后重建；11-14 又剔除了 1,430 条转写错误。likes 8 / downloads 179（采集 11-15 09:00 Asia/Singapore）；license mit，pipeline 未填写。转写是机器生成的，来源是另一个数据集 ZeroAgency/shkolkovo-bobr.video-webinars-audio，源音频的授权链待核。卡片里附有加密货币捐赠地址，与数据本身无关，转述时不要带上。[HF 数据集 TeraTTS/webinars](https://huggingface.co/datasets/TeraTTS/webinars)
- **D4. Zyphra/ztts2_eval_mini**：ZONOS3 报告所用 ZTTS2-Eval 的 Mini 子集（“Open TTS Leaderboard copy”）。clean 部分 35 种语言 3,500 条（FLEURS-R，CC-BY-4.0）；in-the-wild 部分 20 种语言 1,919 条（VoxBlink2，CC-BY-NC-SA-4.0，非商用）。createdAt 2026-11-14 20:33 UTC / 11-15 04:33 Asia/Singapore；lastModified 2026-11-14 20:41 UTC / 11-15 04:41 Asia/Singapore；likes 0 / downloads 0（采集 11-15 09:00 Asia/Singapore）；license other（ztts2-eval-mixed），pipeline 未填写。刚上线，下载数为 0。[HF 数据集 Zyphra/ztts2_eval_mini](https://huggingface.co/datasets/Zyphra/ztts2_eval_mini)
- 附记：
  - slmconsortium/OpenThink：见次条 Boris-2-Think。likes 3 / downloads 104（采集 11-15 09:00 Asia/Singapore）。
  - 数据集 Trending 前列（Angais/pixel-art-atlas-1.4m、arc4g/arc-art、google/multimodal-knowledge-agent 等）都是往期的延续热度。google/physical-engineerings-last-exam、laion/laion-audio-xl 的 README/commits 返回 401，没有绕过，不写入。

---

##### 榜单

- **B1. LMArena 文本**（WebFetch；curl 返回 403。本期保存了第 1–160 行全量和部分尾部行）：数据日期 Nov 9 → **Nov 11**；总票数 9,105,428 → 9,122,174；模型数仍为 421。
  - #1 仍是 Gemini 4 Carbon (High)，1526±10，Prelim。
  - 新出现：Gemini 4 Hydrogen (High) #15，1490±9，Prelim，4,741 票（闭源）。
  - Kimi K3.1 Pro (Max) #24，1485±10，3,995 票。
  - Inkling 2 Small 的许可列从 Proprietary 改为 Apache 2.0（#152，1412±12）。
  - 模型数没变，说明至少有一行被移除；上期只保存了选摘行，无法判断是哪一行。[lmarena.ai 来源](https://lmarena.ai/leaderboard/text)
- **B2. LMArena 视觉**：数据日期仍是 **Nov 8**；总票数 1,567,670，与上期读数完全一致；167 个模型。所以上期观察到的“总票数下降”没有继续，这期榜单根本没有刷新。本期保存了全表 167 行，方便下期逐行比较。#1 Claude Fable 5 (High) 1309±7。[lmarena.ai 来源](https://lmarena.ai/leaderboard/vision)
- **B3. LMArena 文生图**：数据日期 Nov 8 → **Nov 12**；总票数 6,874,394 → 6,934,037（+59,643，恢复增长）；模型数 84 → 85，新增 MiniMax H3-Image #23。#1 仍是 GPT-Image-2.5 Sunburst，1429±5。本期保存了全表 85 行。Seedream 5.5 仍未上这个榜。[lmarena.ai 来源](https://lmarena.ai/leaderboard/text-to-image)
- **B4. AA 文生图**（/image/leaderboard/text-to-image）：
  - 新增 Kling Image 4.0 (preview) #6，1180±13，5,550 票，“Coming soon”，暂无 API 价格。
  - 新增 Canva Craft #10，1158±13。
  - 行数：本期 114 行，其中有一行 FLUX.2 [dev] 是固定在 1000 分的锚点行，上期的解析没有计入。去掉锚点后是 111 → 113。
  - 榜首仍是 GPT Image 2.6 Sunburst，1261±14。H3-Image 系退到 #24/#25。
  - [artificialanalysis.ai 来源](https://artificialanalysis.ai/image/leaderboard/text-to-image)
- **B5. AA 图像编辑**：
  - 新增 Kling Image 4.0 (preview) #6，1182±14。
  - 去掉锚点行后，行数 82 → 83。
  - 前 4 名置信区间重叠（#1 GPT Image 2.6 Sunburst 1210±13）。H3-Image #13。
  - [artificialanalysis.ai 来源](https://artificialanalysis.ai/image/leaderboard/editing)
- **B6. AA Intelligence Index v5**（默认视图 28 个模型；v5 分数不能和 v4 比较）：
  - #1 仍是 **Claude Fable 5.2 (Max) 64.6**，Gemini 4 Carbon 60.0 第二。
  - 新收录 **Gemini 4 Hydrogen (Xhigh)**，11-12 发布，闭源，**53.9**，排 #7。Gemini 3.8 Flash（30.8）退出默认视图，但这不等于被删除。
  - 开放权重的榜首仍是 Kimi K3.1 Pro（46.5，commercial-license）。
  - Inkling 2 Small（30.6）由闭源改为开放 permissive。开放权重的前几名因此是：Kimi K3.1 Pro 46.5 > DeepSeek V4.1 Flash 1017 32.6 > GLM-5.3 31.7 > Inkling 2 Small 30.6 > MiMo-V2.6-Pro 29.9。
  - Ling 3.1 Flash 1019 只是换了 slug，分数不变。AA 收录模型总数 735 → 741。
  - [artificialanalysis.ai 来源](https://artificialanalysis.ai/models)

---

##### 延续热度 / 降权 / 冒名

- **Trending 前 10（模型，08:51 Asia/Singapore）**：
  1. xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic：Uncensored/Heretic 改包，过滤。
  2. MiniMax-H3-Image：主条 3。
  3. Qwen/Qwen3.8-27B：老模型。
  4. Lightricks/LTX-2.5：老模型。
  5. DavidAU 的 Heretic GGUF：过滤。
  6. speridlabs/idol：10/28 发布。
  7. Comfy-Org/MiniMax-H3-Image：H3 的 ComfyUI 分发。
  8. NousResearch/Arete-27B：11/06 发布。
  9. Kimi-K3.1-Pro：跟进 F1。
  10. ZONOS3-Mini：主条 4。
- **窗口内更新但降权**：
  - tencent/Qwen3.8-27B-DSpine-b16 只改了卡片。
  - Zyphra/ZAC-1：上期已写，窗口内没有新 commit。
  - nvidia/Kimi-K3.1-Pro-NVFP4 只加了 SGLang 说明。
  - akhaliq/MiniMax-H3-Image-Character-Swap、vyrekai/minimax-h3-image-comfyui-workflows 是工作流/Space 类 repo，downloads 为 0。
- **同名镜像 / 存疑 repo**（只按证据列出，不认定恶意）：
  - **Kimi K3.1 Pro 新增 6 个全量同名镜像**：technicallyAnnoyed/Kimi-K3.1-Pro、yvfu/Kimi-K3.1-Pro、XxKaitoxX/Kimi-K3.1-Pro、MCendeja11/Kimi-K3.1-Pro、TMA-1/Kimi-K3.1-Pro、Claux67/Kimi-K3.1-Pro。
    - 创建时间是 11-12 15:50 至 11-14 14:46 UTC。都是 112 个文件、约 1,561GB，license 元数据写 kimi-k3.1-pro，没有标注 base_model。
    - 每个都比对了前 50 个条目里的 39 个 LFS 文件，sha256 与官方 39/39 一致，是原样复制，不是篡改。
    - 下载数 0–45。加上上期的 5 个，累计 11 个。
  - phoenix-409/Kimi-K3.1-Pro：只有 1 个文件，是同名空占位 repo。
  - technicallyAnnoyed/Kimi-K3.1-Pro-SuperExpert-12GB：是上期点名的 resuurcct1/Kimi-K3.1-Pro-SuperExpert-12GB 的复制件，19/19 个 LFS 文件 sha256 一致，同样标 apache-2.0、只有约 12GB（likes 0 / downloads 128（采集 11-15 09:00 Asia/Singapore）。宣称不可信，不要转发。
  - Kimi 衍生（未核实，降权）：gureshov/Kimi-K3.1-Pro-Coding-720E（likes 0 / downloads 422（采集 11-15 09:00 Asia/Singapore）等，按名称在窗口内搜到 18 个 Kimi-K3.1 相关新 repo。
  - 合法转存，不算冒名：TechnoBaptist/Inkling-2-Small（26/26 一致）和 botp/Haru-4B（2/2 一致），两者都是 Apache-2.0。
  - 证据：（采集证据快照）

---

##### 口径 / 缺口 / 校验

- 采集方式：
  - HF API：trending（模型 300 条、数据集 100 条）；约 100 个重点组织按 lastModified 扫描（55 个窗口候选）。
  - 本期新增：按 createdAt 全量分页扫描。模型 11 页、窗口内 10,746 个；数据集窗口内 6,503 个。另外按名称搜索衍生 repo。
  - 每个候选 ID 都抓了 api / commits / README / tree；递归 tree 在 50 条处截断，体积另用 `?blobs=true` 计算。
  - AA 首页、模型页、两个图像榜用 curl 保存 HTML 后解析。t2i、编辑、Kimi 页的 urllib 请求超时，改用 curl（120s）重抓成功。
  - LMArena 用 WebFetch 读，本期保存了 vision 和 t2i 的全表、text 的前 160 行。读取时间按文件 mtime 记为 11-15 08:53–08:55 Asia/Singapore。
- 缺口：
  - 401 未绕过：facebook/meta-encoder 的 commits/README、Cactus-Compute/nemotron-3.5-120b-cq、laion/laion-audio-xl、google/physical-engineerings-last-exam、Hubdata/HubEgo-100K。
  - mit-han-lab/Qwen3.8-27B-PEAR 的 README 返回 404。
  - AA 的 inkling-2-small 模型页 curl 超时，Inkling 的 AA 状态以首页和模型页的数据为准。
  - LMArena 文本榜第 161–421 行没有逐行转录，所以本期也给不出完整的增删名单。
  - www.higurashi.ai 的 TLS 握手失败，改用其技术博客 blog.higurashi.ai。
  - AA 图像榜行数的口径差异见 B4/B5（锚点行）。
- 校验：素材中出现的每个 HF ID 都单独请求了 API（数据集走 datasets API），结果见 （采集证据快照）；外链检查见 （采集证据快照）。

