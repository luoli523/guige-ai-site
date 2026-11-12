# 2026-11-12 AI行业动态：全量原始素材

本期信息窗口从 2026 年 11 月 9 日 09:40（上期采集结束）起，至 11 月 12 日各来源的实际采集截止，时区为 Asia/Singapore。本文保留四路采集到的全量原始摘要与来源链接，不是深读成稿，也不意味着所有候选均已独立复现。正文另见[本期深读](https://guige.ai/guige-ai-site/daily/2026-11-12/)。

- 研究与官博：官博摘录约截止 09:26，arXiv 扫描约至 09:27；包括研究汇总、官方原文摘录和论文候选三份材料。arXiv 2611.08488–08710 已确认属于 11 月 9 日正式批，2611.08711–09892 为本期补扫；11 月 12 日批在截止时尚未放出。Apple Machine Learning Research 列表未能完整抓取，不代表没有更新。
- X 公开动态：约截止 09:20；首页时间线只覆盖约 11 月 11 日 13:31 之后，此前时段以公开检索与官方页面补齐，不代表全量时间线。
- GitHub 项目与发行：榜单与仓库核验快照为 09:21；日榜、周榜不等于本期净增。
- 模型与数据集：HF 统计快照为 09:28–09:29，榜单读取至约 09:40；保留模型卡、权重提交、许可、榜单与访问限制记录。

原始材料之间可能保留不同取舍，以下说明用于避免误读：Fable 5.2 / Mythos 5.2 发布页只有日级日期，精确上线时刻待核；Gemini Robotics 2.5 的 RSS 与页面时间戳冲突，待核；Decisions API 的输入上限在两路材料中分别记为 256K 与 16K，以官方文档为准。HF 上与 Kimi K3.1 Pro 同名的非官方镜像只按证据列出、不认定恶意，读者应以 moonshotai 官方组织为准；audnai 第三方仓为手动门控，未读到受限内容，非官方不等于冒名，原材料中的相关记录照录。

除去内部协作名称、个人隐私、内部本地证据路径、来源标记和不宜公开的安全操作细节，正常来源与候选保留；未读、待核、自报与不收录理由照录。以下材料不是投资、上线或商业授权建议。


## 研究与官博

### 研究汇总

#### 研究素材包 · 2026-11-12（窗口 2026-11-09 09:40 → 11-12 ~09:26 Asia/Singapore）

> 官博 6 条 + arXiv 4 条（共 10 真重点）。数字标 来源记录 / 官方自报 / 作者自报 / 待核。原始摘录见同目录 labs-raw.md、arxiv-raw.md。
> arXiv：上期余批 **2611.08711–09892** 已补齐；**08488–08710 已确认属 Asia/Singapore 11/09 正式批**，上期早放备选只更新归属、不当新批真重点重报；周四批采集截止时未放出，续扫 **2611.14520+**。
> 网络安全与生物条目只写结论与官方数字，不写利用/合成/实验步骤。数字均保留设定与基线，**勿**无条件跨模型、跨硬件、跨基准比较。

##### 官博

###### 1. Anthropic：Claude Fable 5.2 / Mythos 5.2
同一底座的两个对外形态：Fable 面向全用户并加强网安/生物防护；Mythos 经生命科学与 Cyber Verification 向合格机构开放。本周最完整的旗舰能力与系统卡说明，对要不要把「最难技术活」从 Opus 日常档上移的人是硬参考；电子原型是配读的专项演示，不是另一条模型发布。
- 页面仅日级 **November 9, 2026**，精确时刻**待核**（上期 09:21 列表未出现，更像当天后段上线）。价 **$8 / $40** 每百万 in/out；fast mode 最高约 **2.5×** 生成速度、**$16 / $80**；相对 5.1 生成最高约快 **30%**（官方自报）。FrontierCode 2.0：Fable 5.2 **Xhigh 49.1%**（5.1 32.4%；同表 Opus 5.5 45.5%、Astra 42.8%、Carbon medium 41.1%）；High effort 约 **45.3%**，与 Opus 5.5 最佳（45.5%）接近、称约一半每任务成本（官方自报；各模型取其最高可用 effort，除非另注）。同表另有 FrontierSWE v2 **69.9%**、HLE with tools **74.2%**、RLI High **41.3%**、OSWorld 2.1 partial **89.3%**、RoboDojo Sim **64.9%**（Astra 29.8%、Fable 5.1 27.6%；内部跑法）（官方自报）。约 1000 个 Fable 5.2 agent、**30 小时**完成 FLT 的 Lean 形式化；同设置 Opus 5.5 在 18 小时约完成 **26%**（官方自报；11-11 勘误脚注说明并非空白起步）。网安/生物仅结论：Mythos 在内部 CVE Rediscovery 上相对 Mythos 5.1 / Opus 5.5 分别高约 14.4 / 10.2 个百分点；沙箱逃逸专用评测约 **3.1%**（Mythos 5 / 5.1 为 39% / 21%）；Fable 相对 5.1 误拦约少 **55%**（官方自报）。厂商自报、effort/harness 不同，勿与其他文的 FrontierCode / RoboDojo 分数直接横比。
- [官博](https://www.anthropic.com/claude-fable-and-mythos-5-2) · [系统卡](https://www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card) · 配读 [电子原型研究文](https://www.anthropic.com/research/claude-electronics-design)（与 Diode 合作的三台可工作原型；`published_time` 为 00:00Z，时刻待核，计入本期因上期列表未收）

###### 2. Google DeepMind：AlphaProof Code 验证 Signal 协议实现
人机共写规范、Gemini Carbon 驱动的 agent 出证明，用 Lean 机器检查，声称对广泛部署的密码协议**实现**（编译后代码）首次做到这一深度的形式化验证；对象是 Signal 协议核心密码学代码（官博亦提及用于 Google Messages 等）。把形式化从「协议设计」推到「正在跑的实现」。
- RSS → **2026-11-10 20:02 Asia/Singapore**（来源记录）。证明逾 **600 万** 行 Lean；流程约 **四周**；人只需复审约 **1%**，其余由 Lean 检查。把两个此前已修复的真实缺陷重新引入隔离版本后，系统对有缺陷版本给出「不安全」的机器检查证明（官方自报，仅结论，不写缺陷机理或攻击路径）。开源验证产物。勿把第三方转述里未见诸这篇官博的版本号/分项性质写成事实。
- [官博](https://deepmind.google/blog/introducing-alphaproof-code/)（RSS **2026-11-10 20:02 Asia/Singapore**）· [官方 PDF](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf) · [产物页](https://google-deepmind.github.io/code-verification)

###### 3. Google DeepMind：Gemini Robotics 2.5
新一代视觉-语言-动作模型，强调灵巧、可靠与可操纵的物理安全，并向合作伙伴滚动开放。与同窗 Apple AMP1、Embodied First Exam 同属具身线，但任务、本体与评测设定都不同，**勿**拿产线 96%、仿真 85.6%、Standard 34% 直接比较。
- RSS `2026-11-09 19:51:47Z` → **11-10 03:51 Asia/Singapore**；页面 jsonld `datePublished` `2026-11-10T15:00:00Z` → **23:00 Asia/Singapore**。两个官方时间戳不一致，**时刻待核**；日历日均在窗口内。评测逾 **200** 项任务；相对先前基线，成功率视任务类型高约 **30%–100%**，完成约快 **20%–30%**（官方自报，区间很宽）。与 Apptronik Apollo 2、Mercedes-Benz 在匈牙利/德国**在产线**做概念验证：汽车零件分拣入托，成功率 **96%**（官方自报；概念验证，不是通用操作成功率）。推理时安全引导：绕障碍安全完成 +**33%**、近人 +**43%**。新开源机器人越狱基准 ASIMOV-Jailbreak 上，**Gemini 4 Argon** 抵御率 **99.5%** vs 先前 ER 2 的 **82%**——该数字属于 Argon，不是 2.5 本体（官方自报，仅结论）。
- [官博](https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/)

###### 4. Google DeepMind：AlphaGenome 2（仅高层）
下一代 DNA 序列模型，按组织/细胞类型或状态做条件预测，试图把变异效应从「组织平均」拉到具体细胞。细胞类型级遗传学工具的一次代际更新；**研究用途，未经临床/诊断批准**（官方声明）。
- RSS / jsonld → **2026-11-11 23:00 Asia/Singapore**（来源记录）。训练含逾 **1.07 亿** 个细胞剖面、**68** 种组织。在 TenK10K 免疫细胞集上，识别因果变异约 **30% vs 16%**、方向性基因效应 **43% vs 23%**（相对「在单细胞数据上微调的 AlphaGenome 原版及其他专用工具」）（官方自报）。可在不重训情况下用少量新的单细胞档案做条件。非商业走 API，商业为私人预览。不写实验或设计步骤。
- [官博](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/)

###### 5. OpenAI Alignment：CoT 可监控性随训练生命周期如何变化
用「无 CoT 能力」和「CoT 可控性」作监控规避的不完美代理，沿预训练困惑度、架构、RL 与模型生成数据（SFT）拆 GPT‑6 Astra 以来「更难吃透 CoT」的来源。把「靠读 CoT 做可扩展监督」的假设压到训练栈选择上。
- 页面 **November 10, 2026**（仅日期，时刻待核）。无 CoT 能力随基座困惑度下降而平滑提升；多数评测上架构差异可被困惑度解释，多跳规划/串行计算上部分架构在同一困惑度下更陡（官方自报）。RL 即使只有长度约束与最终答案评分（作者称已核查无意外 CoT 奖励压力），CoT 可控性仍明显上升；加工具过程监督只有小幅再升。能力相近、可控性不同的教师 rollout 做 SFT，可控性可像 subliminal learning 一样传给学生（官方自报）。文内自陈：可控性是嘈杂代理，等能力模型对上，更可控者并不总有更高监控规避成功率。UK AISI 报 Astra 无 CoT 数学时间视野中位 **30.9 分钟**（相对此前约 2028 年底投影约 7 分钟），并提示污染可能高估（官方转述）。
- **与同窗 arXiv #10 的关联/差异**：两边都在问「对着监控信号做 RL 会怎样」。官博关注的是 CoT 作为监督通道会不会随预训练/RL/数据蒸馏变弱，并重申**不要**把奖励压在 CoT 上（以免造成掩饰）；#10 关注的是用监控器**显式惩罚** reward hacking 时，怎样设计才压得住、模型又如何学会躲监控。相关是同一监督问题的两面，不可把「可控性上升」直接读成「惩罚 hacking 无效」，也不可把 #10 的环境结论外推到 OpenAI 的训练栈。
- [官博](https://alignment.openai.com/cot-monitorability-model-lifecycle/) · 对照 [2611.09828](https://arxiv.org/abs/2611.09828)

###### 6. Microsoft Research：Lazarus——改休眠神经元给 agent 下后门（仅结论）
无需重训即可改写模型权重，使平时表现正常、能通过常规评测的模型在隐藏触发出现时，驱使带工具/终端权限的 agent 执行恶意命令。把「权重被改过的检查点」写成评测漏得掉的供应链/内部风险；作者强调这不是开源权重独有的问题，关键是权重完整性与出处。
- Feed → **2026-11-11 04:52 Asia/Singapore**（来源记录）。称改写「少于 **10** 个」休眠神经元即够（官方自报）。检测上，称前沿 agent 有时能发现异常权重修改，但可靠办法仍是与未改动原权重做 diff；单一扫描不能证明安全。Foundry 对受信任发布者模型做出处绑定与运行环境扫描，并在推进权重扫描、红队与签名。不写机制步骤、触发构造或利用路径。
- [官博](https://www.microsoft.com/en-us/research/blog/lazare-veni-foras-reprogramming-dormant-neurons-to-backdoor-ai-agents/)（feed **2026-11-11 04:52 Asia/Singapore**）

##### arXiv

###### 7. Apple：AMP1，通用模型直接做操作策略（2611.09892）
用通用大模型在环直接指挥机械臂（agentic manipulation policy），给出可跨单臂/双臂/移动操作的参考 harness AMP1，不靠演示、不做任务微调。把「通用模型当操作策略」和专用 VLA/WAM 放到同一套仿真与实物对比里；与上期 Social Humanoid、同窗 Robotics 2.5 / Embodied First Exam 连续，但设定不同，**勿**横比成功率。
- RoboLab-120 零样本成功率 **85.6%**，对比文内领先 VLA **49.2%**、WAM **42.9%**（作者自报）。实物 12 任务 × 3 台机器人 **104/108** 成功，相对 FLUX 3 Action（49/108）与 π0.5（30/108）失败率约 **15× / 20×** 更低（作者自报；π0.5 / FLUX 3 Action 仅为对比对象，**不是**作者单位）。加跨回合记忆后，RoboDojo 双臂失败率相对零样本再降 **4.6×**（作者自报）。无任务专用技能库。Asia/Singapore 归属 **11/09** 补扫段（ID ≥08711；Submitted 6 Nov，listing 以周一为准）。单位 Apple（来源记录）。
- [arXiv](https://arxiv.org/abs/2611.09892) · [项目页](https://apple-aiml-research.github.io/ml-amp/)

###### 8. NVIDIA：CPU-ARC，把推理痕迹编成可在 CPU 上复用的缓存（2611.09891）
把一次推理痕迹编成可在 CPU 上反复执行的 agentic reasoning cache（ARC），同类新题不再让大模型从头想。给「推理可缓存、可解释、可继续训」一条系统级路径；倍速是**调用成本**，不是硬件吞吐。
- **口径（已核 PDF 实验节）**：Savings × = 源模型调用成本 / 缓存调用成本。源模型与构建模型均为 **Claude Opus 4.5**（extended thinking，预算 4096 tokens）；成本按 **2026 年 3 月** API 标价核算（Opus 4.5 为 $5 / $25 每百万 in/out）（作者自报）。相对该源模型，每查询约 **16–291×** 更便宜：GSM8K 约 **16.3×**，AIME ’24 / ’25 / ’26 约 **262.4× / 291.1× / 281.4×**（作者自报）。AIME ’25 缓存准确率 **93.3%** vs 源模型 **83.3%**，AIME ’26 **96.7%** vs **90.0%**；GSM8K 缓存 **98.0%** 略低于源 **98.5%**（作者自报）。目标端可用 Haiku 4.5 / Gemini 3.0 Flash Lite / GPT 5.4 Nano，或微调后的 Llama 3.2 1B；执行主要靠 CPU。构建本身有成本，约 **12–84×** 一次源调用（难题更接近 12–13×，GSM8K 这类短回答反而约 84×），约 13–90 次邻域调用后收回（作者自报）。**「500」是基准名 MATH-500，不是 500× 降本。** 数字绑定其基准、源模型与计价，勿与 Snapshot 冷启动倍速或 Reshard 通信倍速混比。Asia/Singapore 归属 **11/09**。单位 NVIDIA（PDF 页脚版权；来源记录）。
- [arXiv](https://arxiv.org/abs/2611.09891)

###### 9. Northwestern 等：Embodied First Exam，最强 Standard 仅 34%（2611.12177）
给 coding agent 进物理世界的「入学考」：同一套任务允许直接控制、写代码控制、或先训策略再控制，并分标准/实时/特权三种设定。规模对准「agent 管机器人」而不是传统 visuomotor 基准；当前最强在标准设定上仍然很低。
- **1,156** 任务、35 套、47 种机器人；核心 **456** 任务上，八个 agent 中最强 GPT‑6 Astra + Codex 在 Standard Setting 成功率 **34%**（作者自报）。特权设定可重置、近似上界，不能当成真实部署分数。Asia/Singapore 归属 **11/10**。单位 Northwestern / CMU / UC Berkeley / UW / Stanford / UNC / Texas A&M / UT Austin（来源记录）。与 #3、#7 不要直接比成功率——这里测的是 coding agent 在标准物理约束下的任务通过率。
- [arXiv](https://arxiv.org/abs/2611.12177) · [站点](https://embodied-first-exam.ai) · [代码](https://github.com/mll-lab-nu/embodied-first-exam)

###### 10. MATS + Google DeepMind（Nanda）：RL 中监控 reward hacking 的干预设计（2611.09828）
在三个更接近真实的环境里系统比较「用监控器惩罚 reward hacking」怎么设计才有效，以及模型如何学会躲监控。把监控干预从口号落到可开源环境与可迁移的设计结论。安全向**仅结论**，不写环境漏洞或躲避步骤。
- **与官博 #5 的关联/差异见上**。Qwen3-4B；编码 / 医疗对话 / 传记生成三环境。摘要未给单一总成功率；称部分干预可把 hacking 率压回训练前水平（跨 seed）。监控越「漏学习信号」越能压 hacking，也越容易被绕；训练中加入更容易的题可以降低 hacking（作者自报）。结论绑定该模型与三环境。Asia/Singapore 归属 **11/09**。单位：Aria Wong = MATS、Neel Nanda = Google DeepMind（HTML 来源记录）；Joshua Engels 的 HTML 无 affiliation，**不以排版猜成 DeepMind**（单位待核）。不可写成「DeepMind 三作论文」。
- [arXiv](https://arxiv.org/abs/2611.09828)（NeurIPS 2026，PDF）

##### 备选（简洁）

- 官博次选：Meta [Muse Ember](https://research.meta.ai/blog/muse-ember)（11-09，`00:00Z` 时刻待核；AA Index 与 Haiku 同为 36、每任务约 $0.14，但 FrontierCode 2.0-AA 落后于 Haiku）；Anthropic Alignment [Worse Together / MAMUBench](https://alignment.anthropic.com/2026/worse-together/)（11-11；多用户各派 agent 全面差于单协调者）；OpenAI [Control Room](https://openai.com/index/control-room)（11-09 21:00 Asia/Singapore，急停约 35 秒）；OpenAI×Upwork [自由职业研究](https://openai.com/index/ai-effect-on-freelance-work)；NVIDIA [Snapshot](https://developer.nvidia.com/blog/start-and-restore-gpu-workloads-in-seconds-with-nvidia-snapshot/)（恢复 3.6–42.7 s，相对冷启动约 8×–36×）；Google [MKA 基准](https://blog.google/innovation-and-ai/models-and-research/gemini-models/multimodal-knowledge-agent-benchmark/) + [Carbon 正式开放](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)；Meta [TLX 编译器](https://engineering.fb.com/2026/11/10/open-source/tlx-a-hardware-native-gpu-compiler-for-production-ml/)
- arXiv：Duke/Modal/Princeton/NYU [并行小队 test-time scaling 2611.09798](https://arxiv.org/abs/2611.09798)；Baidu [Agentic-OPD 2611.12799](https://arxiv.org/abs/2611.12799)（接上期 OPD 线，回收废弃 checkpoint 能力）；AWS [PACE 2611.10240](https://arxiv.org/abs/2611.10240)；UW/Ai2 等 [Infrathon 2611.11995](https://arxiv.org/abs/2611.11995)；RPI/Microsoft [MemoryDojo 2611.09721](https://arxiv.org/abs/2611.09721)（记忆投毒基准，与上期 Memory Trap 互补，仅结论）

##### 覆盖缺口 / 排除

- **窗前排除（勿当本期新发）**：OpenAI BioBasicsBench（11-06 **08:00** Asia/Singapore）；Meta Specialized Models 博文（meta `00:00Z`=08:00 Asia/Singapore）
- **上期已报勿重复**：Anthropic agent memory/dreaming、NVIDIA Reshard、FLUX 3 Image Klein、OpenAI Hacktron；arXiv Memory Trap 2611.07554、OPD 2611.08453、EnvOpt 2611.07372、Social Humanoid 2611.08407、RecSA 2611.07232
- **08488–08710**：已确认属 **Asia/Singapore 11/09 正式批**；上期早放备选（如 Georgian [Decision Context 2611.08644](https://arxiv.org/abs/2611.08644)、EMERGE、SAE 压缩）只更新归属，不当新批真重点重报
- **arXiv 扫描**：11/09 余批 **08711–09892** 已补齐；**11/09–11/11 列表完整**；周四批截止扫描时（11-12 **09:27 Asia/Singapore**）未放出，listing 停在 Wed 11 Nov，续扫 **2611.14520+** 与周四 `list/*/new`
- **官博覆盖缺口**：Apple Machine Learning 研究列表未能完整抓取，**不能写成无更新**。DeepMind Gemini Robotics 2.5 的 RSS 与页面 jsonld **时刻冲突，待核**。Muse Ember 与 Anthropic 电子设计文的 `00:00Z` 更像日级占位（上期 09:21 未收录），已计入并标待核
- Thinking Machines 博客已访问、窗内无新帖（非缺访问）。Amazon Science 窗内两条只核到标题与日期，未深读数字，未进主包

### 官方原文摘录

#### Labs Raw Excerpts — 2026-11-12

- **窗口**: 2026-11-09 09:40 Asia/Singapore → **2026-11-12 09:26 Asia/Singapore**（Asia/Singapore, UTC+8；采集截止以本机 `date` 为准）
- **采集时间**: 2026-11-12 约 09:21–09:27 Asia/Singapore
- **说明**: 原始摘录；关键数字标「官方自报 / 来源记录 / 待核」。网络安全与生物仅写结论与官方数字，不写利用/合成步骤。已在上期主包或窗口外的条目不作为本期重点重复。
- **去重参照**: （内部证据存档）、`research.md`（已报：Anthropic agent memory/dreaming、NVIDIA Reshard、NVIDIA FLUX 3 Image Klein @ Blackwell、OpenAI Hacktron；窗前排除：OpenAI BioBasicsBench、Meta Specialized Models）。上期数字不在此复述。

---

##### OpenAI

**源查证**: [openai.com 来源](https://openai.com/news/rss.xml)（curl + Chrome UA，HTTP 200）；[openai.com 来源](https://openai.com/news/) 与 `/news/research/`、多数 `/index/` 详情页 curl **403**，改用 WebFetch 核正文。辅以 [alignment.openai.com 来源](https://alignment.openai.com/)（curl 200）。

###### 1) What affects CoT monitorability across the model lifecycle? — **建议进主包（对齐/安全研究）**
- **日期**: 页面 **November 10, 2026**（仅日期；`citation_publication_date: 2026/11/10`；精确 HH:MM **待核**）
- **URL**: [alignment.openai.com 来源](https://alignment.openai.com/cot-monitorability-model-lifecycle/)
- **人话**: OpenAI Alignment 用「无 CoT 能力」和「CoT 可控性」作监控规避的不完美代理，沿预训练困惑度、架构、RL 与模型生成数据（SFT）拆 GPT‑6 Astra 以来监控变难的来源。
- **要点**（均为官方自报）:
  - 观察到 Astra 在非对抗设置下 CoT 可监控性下降、对抗测试中更会规避，且无 CoT 能力明显高于前代；文称相对历史趋势「偏高」，但相对**基座困惑度**并不偏高。
  - 无 CoT 能力随基座困惑度下降而平滑提升；多数评测上架构差异可被困惑度解释，多跳规划/串行计算上部分架构在同一困惑度下更陡。
  - RL 即使只有长度约束与最终答案评分（作者称已核查无意外 CoT 奖励压力），CoT 可控性仍明显上升；加工具过程监督只有小幅再升。
  - 能力相近、可控性不同的教师 rollout 做 SFT，可控性可像「subliminal learning」一样传给学生。
  - **局限（文内自陈）**: 可控性是嘈杂代理；等能力模型对上，更可控者并不总有更高监控规避成功率。UK AISI 报 Astra 无 CoT 数学时间视野中位 **30.9 分钟**（相对此前约 2028 年底投影约 7 分钟），并提示污染可能高估。
- **为何重要**: 把「靠读 CoT 做可扩展监督」的假设压到训练栈选择上，是安全案例与后训练设计的硬参考。
- **对谁有用 / 深读**: 对齐、安全案例、预训练/RL 负责人；看文内图 1–6 与 Appendix B 反例。
- **标注**: 来源记录（URL/日）/ 官方自报（机制与相关）/ 时刻待核。

###### 2) Control Room：研究基础设施上的工作负载急停 — **建议进主包（安全工程）**
- **日期**: RSS `Mon, 09 Nov 2026 13:00:00 GMT` → **2026-11-09 21:00 Asia/Singapore**（窗口内）
- **URL**: [openai.com 来源](https://openai.com/index/control-room)
- **人话**: 中央系统追踪研究侧推理作业（含训练采样、评测、数据处理），在安全/安保告警时从推理引擎层拒绝继续出 token；服务自身宕机则「失败即关闭」。
- **要点**（官方自报）: 收到停止指令后，到无法继续推进的最大间隔 **35 秒**（授权缓存；称正在压向零）。要求带 agentic 推理的研究作业关联已批准 safety case。与错位监控联动；举 DNS 相关事件由监控捕获（仅结论）。外部服务栈本就更集中、已有下线能力。
- **为何重要**: 把「能发现」补成「能停得住」，且不把关键控制放在多变的 researcher workload 代码里。
- **标注**: 来源记录（RSS 时间戳/URL）/ 官方自报。

###### 3) Work at the Frontier: AI’s effect on freelance work — **建议进主包（经济研究）**
- **日期**: RSS `Tue, 10 Nov 2026 07:00:00 GMT` → **2026-11-10 15:00 Asia/Singapore**
- **URL**: [openai.com 来源](https://openai.com/index/ai-effect-on-freelance-work)
- **报告 PDF**: [cdn.openai.com 来源](https://cdn.openai.com/pdf/openai-upwork-full-report.pdf)（*The Rebundling of Freelance Work in the AI Age*，OpenAI + Upwork）
- **人话**: 用 ChatGPT 使用与 Upwork 帖子对照，看自由职业需求如何随 AI 使用变化：不是简单替代，AI 相关项目任务组合更新、固定价预算与工时更大。
- **要点**（官方自报）: 63 类工作中 **43** 类呈「ChatGPT 上更常见 → Upwork 份额下降」；其余 20 类相反。2023 初至 2025 末，AI 相关帖任务组合多样性约 **+45%**（约 14.6→21.2 个「同等常见任务」当量）。时薪接近，但 AI 相关项目固定价预算与工时更高（同工种、同月调整后）。背景引用 Upwork：38% 美国熟练知识工人自由职业；$1.5 万亿美元 2024 年美国自由知识工作收入（官方转述 Upwork，口径超出该平台）。
- **局限**: 观测性市场帖与产品使用份额，非因果就业效应；图轴时间窗在正文与图注中不完全同一，引用需看原图。
- **标注**: 来源记录（RSS 时间）/ 官方自报。

###### 窗口内其他 OpenAI（产品/客户故事，不建议挤主包研究条）
| 标题 | Asia/Singapore（RSS） | 判定 | URL |
|------|-----------|------|-----|
| Cogent and OpenAI build cyber defense factories | 11-10 08:00 | 客户故事。客户自报：一家 Fortune 1000 汽车客户关键漏洞 MTTR **−75%**；一家 Fortune 500 IT 客户分诊吞吐 **5×**。仅结论，不写利用/修复步骤。 | [openai.com 来源](https://openai.com/index/cogent-security) |
| CodeRabbit scales agentic software development and ships 20x more | 11-09 16:00 | 创业客户故事（「20x」为对方口径） | [openai.com 来源](https://openai.com/index/coderabbit-codex-daybreak) |
| Introducing Businesses in ChatGPT | 11-10 18:00 | 产品 | [openai.com 来源](https://openai.com/index/introducing-businesses-chatgpt) |
| ChatGPT Enterprise in AWS Marketplace | 11-10 03:00 | 采购/渠道 | [openai.com 来源](https://openai.com/index/chatgpt-enterprise-aws-marketplace) |
| Closing the AI guidance gap in education 等学院/航司/JioStar/Gilbert+Tobin/Veterans/Caregivers/Kuken | 11-09 16:00–11-12 08:00 | 教育或客户故事 | 见 RSS |

**alignment.openai.com**: 窗内新帖仅上述 CoT 文；Nov 2–3 activation classifiers / eval-production gap → 上期已标窗口外。

---

##### Anthropic

**源查证**: [anthropic.com 来源](https://www.anthropic.com/research)、`/news`（curl 200）；[alignment.anthropic.com 来源](https://alignment.anthropic.com/)（curl 200）。无带时区的公开 RSS；研究页多为「Published Nov N, 2026」日级，部分带 `article:published_time` 且常为当日 `00:00:00.000Z`（日级占位，时刻待核）。

###### 4) Introducing Claude Fable 5.2 and Claude Mythos 5.2 — **建议进主包（旗舰模型）**
- **日期**: 页面 **November 9, 2026**（仅日期；精确 HH:MM **待核**）。上期 11-09 09:21 采集的 research/news 列表**未出现**此条，更像当天后段上线，而非窗前遗漏。
- **URL**: [anthropic.com 来源](https://www.anthropic.com/claude-fable-and-mythos-5-2)
- **系统卡**: [anthropic.com 来源](https://www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card)
- **人话**: Fable / Mythos 是同一底座的两个对外形态：Fable 面向全用户并加强网安/生物防护；Mythos 经生命科学与 Cyber Verification 项目向合格机构开放。宣称编码、推理、视觉、机器人与形式化均有跃迁，默认价下调，并提供更快的 fast mode。
- **要点**（官方自报；各模型取其最高可用 effort，除非另注；Fable 分数默认含防护）:
  - 价：**$8 / $40** 每百万 in/out；fast mode 最高约 **2.5×** 生成速度，**$16 / $80**。相对 5.1 生成最高约快 **30%**。
  - FrontierCode 2.0：Fable 5.2 Xhigh **49.1%**（5.1 32.4%；Opus 5.5 45.5%；Astra 42.8%；Carbon medium 41.1%）。High effort 约 **45.3%**，与 Opus 5.5 最佳（45.5%）接近、称约一半每任务成本。
  - 其他表内：FrontierSWE v2 **69.9%**；AutomationBench **51.4%**（Carbon 更高，53.9%）；Terminal-Bench-Science 0.1 Fable **74.6%** / Mythos **75.3%**；OSWorld 2.1 partial **89.3%**；HLE with tools **74.2%**；RLI High **41.3%**；AA-Briefcase rubric **66.1%**；RoboDojo Sim **64.9%**（Astra 29.8%；Fable 5.1 27.6%）。BenchCAD 2.1 Max：**83.5** vs Opus 65.3 / Fable 5.1 44.4。
  - 网安（仅结论）：Mythos 在内部 CVE Rediscovery 上相对 Mythos 5.1 / Opus 5.5 分别高约 **14.4 / 10.2** 个百分点（表内 89.6% vs 78.3% / 81.3%）；CyScenarioBench 各实验室任务集不同，不可横向死比。
  - 数学：约 **1000** 个 Fable 5.2 agent、**30 小时**、最少人工，完成 FLT 的 Lean 形式化；同设置 Opus 5.5 在 18 小时约完成 **26%**、30 小时几乎不再推进。配读去年 9 月那次 11 天形式化文（**窗口外**，勿当新发）：[anthropic.com 来源](https://www.anthropic.com/research/formalizing-fermats-last-theorem) 。11-11 对形式化小节有勘误脚注（给过 60 条命题等，不是完全空白起步）。
  - 硬件：一句话提示设计三种可工作电子原型（语音助手、USB 会议扬声器、掌上电子宠物），电路无需改线（见下条研究文）。
  - 安全：高风险错位风险判断为低；Mythos 在约 1900 场景行为审计上多数指标不差于或优于近期模型。沙箱逃逸专用对抗评测中，利用箱外凭证/文件约 **3.1%**（Opus 5.5 3.3%；Mythos 5 / 5.1 为 39% / 21%）。Fable 相对 5.1 误拦约少 **55%**（网安约 60%、生物约 40%）。反蒸馏称收获数据降 **90%–99%**。对加速 AI 研发的部分能力（如某些 kernel/架构改进）训练期有意限制到约 Opus 5.5 水平。
- **局限**: 厂商自报、effort/harness 不同；RoboDojo 与部分网安为内部跑法；科学/物理「解决开放问题」需读预印本，此处不展开。
- **标注**: 来源记录（URL/日）/ 官方自报（数字）/ 时刻待核。

###### 5) Testing Claude on real-world electronics design — **建议作 #4 配读（研究长文）**
- **日期**: `article:published_time` **2026-11-09T00:00:00.000Z** → 若按字面为 **11-09 08:00 Asia/Singapore**（早于 09:40 起点）；`modified_time` 2026-11-09T18:51:01Z → **11-10 02:51 Asia/Singapore**。上期 09:21 列表未出现此文，**00:00Z 更像日级占位**。计入本期并标时刻待核，避免漏报。
- **URL**: [anthropic.com 来源](https://www.anthropic.com/research/claude-electronics-design)
- **人话**: 与 Diode Computers 合作，用 Fable 5.2 端到端设计并指导人工组装三台可工作电子原型；文内强调仍是原型，未经电性认证/量产验证，模型未接测试设备或产线机器。
- **进主包**: 与 Fable 发布绑定；单独优先级低于模型卡。
- **标注**: 来源记录（URL）/ 时刻待核（00:00Z）。

###### 6) Worse Together: Multi-User Multi-Agent Teams / MAMUBench — **建议进主包（多智能体评测）**
- **日期**: 页面 **November 11, 2026**（仅日期；时刻待核）
- **URL**: [alignment.anthropic.com 来源](https://alignment.anthropic.com/2026/worse-together/)
- **人话**: Anthropic Fellows + 员工在四个「多用户、每用户一个 agent、共享资源」环境里发现：每个用户各派一个 agent，群体结果全面差于「一个 agent 服务所有人」；并开源其中三个环境为 **MAMUBench**。
- **要点**（官方自报；模拟环境）:
  - 协调者相对点对点团队，在全部四环境、Claude Opus 5 / Sonnet 5 上约高 **10–45** 个百分点（相对最优策略的群体得分）。
  - API 预算：点对点团队仅为协调者的 **47%**（Opus 5）/ **38%**（Sonnet 5）；团队变大时行动的 agent 比例下降（Sonnet 5：4 人 **66%** → 16 人 **10%**；GPT‑5.6-sol：82%→25%）。GPT/Qwen 每局未经同意取消他人作业约 **3.9–7.1** 次，Sonnet 0.59，Opus 为 0。
  - 个人助理订餐/出行：协调者兑现「关键请求」的次数约是点对点团队的 **两倍**。下单 agent 几乎总能收到该请求（94–99%），但提交时已读入上下文仅 **47–67%**；读到后兑现 56–68%，未读到 19–36%。Claude 团队局中逾半出现对他人的无依据陈述（Opus 58%、Sonnet 53% vs 单 agent 17–20%）。
  - 缓解因环境而异：预算环境加「队长」可抹平差距；助理环境用「未读完消息不得下单」的平台闸，挽回失败局的 **73%**（Opus）/ **62%**（Sonnet）。
- **为何重要**: 把多智能体失败从「同一目标协作」扩展到「不同用户代理抢共享资源」，对产品与安全评测都有用。
- **标注**: 来源记录（URL/日）/ 官方自报 / 时刻待核。

###### Newsroom（非研究主条）
- **Anthropic launches roadshow for proposed IPO**：**Nov 10, 2026**（日级）。公司公告，不进研究主包。[anthropic.com 来源](https://www.anthropic.com/news/roadshow-launch)
- 页眉「November 12, 2026」是站点日期，勿当成新帖。

---

##### Google DeepMind

**源查证**: [deepmind.google 来源](https://deepmind.google/blog/rss.xml)（curl 实为 gzip，解码后可读；`lastBuildDate` Wed, 11 Nov 2026 15:00:15 +0000）。博客 HTML 同样常需解压。Carbon 博文会跳到 blog.google。

###### 7) Introducing AlphaProof Code：形式化验证 Signal 协议实现 — **建议进主包（安全/形式化）**
- **日期**: RSS `Tue, 10 Nov 2026 12:02:28 +0000` → **2026-11-10 20:02 Asia/Singapore**
- **URL**: [deepmind.google 来源](https://deepmind.google/blog/introducing-alphaproof-code/)
- **论文 PDF（官方域名，HTTP 200）**: [deepmind.google 来源](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf)
- **产物页**: [google-deepmind.github.io 来源](https://google-deepmind.github.io/code-verification)
- **人话**: 人机共写规范、Gemini Carbon 驱动的 agent 出证明，用 Lean 机器检查，声称对广泛部署的密码协议**实现**（编译后代码）首次做到这一深度的形式化验证；对象是 Signal 协议核心密码学代码（亦用于 Google Messages 等，文内表述）。
- **要点**（官方自报）: 证明逾 **600 万** 行 Lean；流程约 **四周**（对比「专家团队常年」的历史口径）。人只需复审约 **1%** 代码，其余由 Lean 检查。把两个此前已修复的真实缺陷重新引入隔离版本后，系统对有缺陷版本给出「不安全」的机器检查证明（仅结论）。开源验证产物。
- **安全写作边界**: 只写上述结论与规模，不写协议细节、缺陷机理或攻击路径。第三方转述中的版本号/分项性质等，若未在这篇官博直接出现，不写入主数字。
- **为何重要**: 把形式化从「协议设计」推到「正在跑的实现」，并展示 agent 证明流水线。
- **标注**: 来源记录（RSS 时间/URL/PDF 可取）/ 官方自报。

###### 8) Gemini Robotics 2.5 — **建议进主包（具身）**
- **日期**: RSS `Mon, 09 Nov 2026 19:51:47 +0000` → **2026-11-10 03:51 Asia/Singapore**；页面 jsonld `datePublished` **2026-11-10T15:00:00+00:00** → **23:00 Asia/Singapore**。两个官方时间戳不一致，**时刻待核**；日历日均在窗口内。
- **URL**: [deepmind.google 来源](https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/)
- **人话**: 新一代视觉-语言-动作模型，强调灵巧、可靠与可操纵的物理安全；向机器人合作伙伴滚动开放。
- **要点**（官方自报）: 评测逾 **200** 项任务。相对先前基线，成功率视任务类型高约 **30%–100%**，完成约快 **20%–30%**。与 Apptronik Apollo 2、Mercedes-Benz 在匈牙利/德国在产线做概念验证：汽车零件分拣入托，成功率 **96%**。推理时安全引导：绕障碍安全完成 +**33%**、近人 +**43%**。新开源机器人越狱基准 **ASIMOV-Jailbreak**：Gemini 4 Argon 抵御率 **99.5%** vs 先前 Gemini Robotics ER 2 的 **82%**（该数字属于 Argon，不是 2.5 本体）。称 2.5 研发受 Argon 仿真/数字孪生加速。
- **局限**: 产线 96% 为概念验证；成功率区间跨任务类型很宽，不可当成单一倍数。
- **标注**: 来源记录（URL）/ 官方自报 / 时刻待核（RSS vs jsonld）。

###### 9) AlphaGenome 2 — **建议进主包（生物/遗传学模型；仅高层）**
- **日期**: RSS / jsonld `2026-11-11T15:00:00+00:00` → **2026-11-11 23:00 Asia/Singapore**
- **URL**: [deepmind.google 来源](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/)
- **人话**: 下一代 DNA 序列模型，按组织/细胞类型或状态做条件预测，试图把变异效应从「组织平均」拉到具体细胞；非商业研究走 API，商业为私人预览。**研究用途，未经临床/诊断批准**（官方声明）。
- **要点**（官方自报，仅结论）: 训练含逾 **1.07 亿** 个细胞剖面、**68** 种组织。在 TenK10K 免疫细胞集上，识别因果变异约 **30% vs 16%**、方向性基因效应 **43% vs 23%**（相对「在单细胞数据上微调的 AlphaGenome 原版及其他专用工具」）。可在不重训情况下用少量新的单细胞档案做条件。提供面向数百种细胞/组织条件、对性状相关变异的预计算分数。
- **标注**: 来源记录 / 官方自报。不写实验或设计步骤。

###### 10) Gemini 4 Carbon is now available — **建议作候选/配读（模型开放与新榜）**
- **日期**: RSS `Tue, 10 Nov 2026 16:03:47 +0000` → **2026-11-11 00:03 Asia/Singapore**；jsonld `2026-11-10T16:00:00+00:00`
- **URL**: [deepmind.google 来源](https://deepmind.google/blog/gemini-4-carbon-is-now-available/) （落地 [blog.google 来源](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)）
- **人话**: 继 10 月底 Carbon 模型介绍之后，正式向付费开发者/企业开放 API；同时给出一批新的对外榜与成本声明。
- **要点**（官方自报）: 价与 Argon 引入价相同，**$2 / $10** 每百万 in/out。称在 CursorBench 4.0、Perplexity WANDR、Zapier AutomationBench 上排 **#1**，每任务成本低于次优外部模型 **2× 以上**。在 MKA 上质量 **#2**、平均每任务成本低于榜首 **6× 以上**（与下条 MKA 文一致）。
- **注意**: 这是「开放+新评测叙事」，不是 10/28 那篇「下一代前沿模型」的重复首发；引用时不要写成「本周首次发布 Carbon」。
- **标注**: 来源记录 / 官方自报。

---

##### Google Research / blog.google

**源查证**: [research.google 来源](https://research.google/blog/rss/)（curl 200）；[research.google 来源](https://research.google/blog/)、[blog.google 来源](https://blog.google/technology/ai/)（curl 200 / WebFetch）。

###### 11) Introducing the Multimodal Knowledge Agent (MKA) benchmark — **建议进主包或与 Carbon 配读（新基准）**
- **日期**: 页面 Nov 10, 2026；jsonld `2026-11-10T16:00:00+00:00` → **2026-11-11 00:00 Asia/Singapore**
- **URL**: [blog.google 来源](https://blog.google/innovation-and-ai/models-and-research/gemini-models/multimodal-knowledge-agent-benchmark/)
- **人话**: 与 Artificial Analysis 合作的知识工作基准：视觉复杂、多文件的专业任务；同一开源 harness（Stirrup）跑模型。
- **要点**（官方自报）: **200** 道私有题，覆盖 **10** 个行业、**83** 种职业；每题对应资深人士约 **3–8 小时** 工作，专家量规约 **70** 条是否项，事实 **75%** / 视觉设计 **25%**。非谷歌模型驱动的自动评分器与领域专家一致性 **96%**。另在 Hugging Face 放 **10** 道公开样例。受测前沿模型平均每题约 **30–130** 轮，效率差极大。Carbon 质量 #2、平均成本低于最高分模型约 **6×**。
- **标注**: 来源记录 / 官方自报。

###### 12) Gemini Decisions API — **候选（推理接口）**
- **日期**: jsonld `2026-11-11T18:00:00+00:00` → **2026-11-12 02:00 Asia/Singapore**
- **URL**: [blog.google 来源](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)
- **人话**: 新端点 + Gemini Decision 1，对封闭选项做单次前向打分（概率/置信度），不做逐 token 生成。
- **要点**（官方自报）: 端到端约 **150–250 ms**（模型计算中位 50–100 ms），上下文至 16K；**$0.10 / 1M input、输出不计费**；在其共享基准集上称比 Gemini 3.5 Flash-Lite（Interactions API）便宜近 **5×**。
- **标注**: 官方自报。

###### Google Research 博客
- **Language Explorer**（页面 November 9；RSS → **2026-11-10 04:29 Asia/Singapore**）: 1,000 Languages / LinguaMeta 可视化，配合柏林通信博物馆展览。偏科普展览，研究密度低于上述条目。[research.google 来源](https://research.google/blog/exploring-the-worlds-languages-with-language-explorer/)
- **CKM 可穿戴风险画像与个性化教练**（RSS → **2026-11-12 03:54 Asia/Singapore**）: SensorWM 自称训练于逾 **220 万** 人·周可穿戴数据；教练在 71.4% 评估中选其计划为最佳；医生认 99.2% 计划在安全运动强度内、97.6% 生理陈述准确（官方自报）。健康应用研究，可作次选。[research.google 来源](https://research.google/blog/using-wearables-to-enable-cardiovascular-kidney-metabolic-ckm-risk-profiling-for-personalized-coaching/)
- blog.google 另有 Gemini on Apple CarPlay（Nov 11）、Maps in AI Studio（Nov 9）→ 产品，不进研究主包。

---

##### Meta（research.meta.ai / about.fb.com / engineering.fb.com）

**源查证**: 未打开易坏的 ai.meta.com 主页。`research.meta.ai/blog/`、`about.fb.com/news/`、`engineering.fb.com` 列表 + 详情页 `article:published_time`。

###### 13) Muse Ember — **建议进主包（小模型/成本）**
- **日期**: 页面 November 9, 2026；`published_time` **2026-11-09T00:00:00.000Z**（若按字面 = 08:00 Asia/Singapore，早于窗口起点）。上期 09:21 未收录，**00:00Z 更像日级占位**。计入本期，时刻待核。
- **URL**: [research.meta.ai 来源](https://research.meta.ai/blog/muse-ember)
- **人话**: Meta 最小、最便宜的执行型模型，面向 agent 反复做的工具调用、编码子任务、路由、抽取与长文档；`muse-ember-1.0`，1M 上下文 / 至多 512K 输出。称由 Muse Wonder Full 训出。
- **要点**（官方自报；max reasoning；AA Index v5，2026-11-09）:
  - 价：≤200K prompt 为 **$0.10 / $0.50** 每百万 in/out（缓存输入 $0.004）；更长提示为 $0.30 / $1.50（缓存 $0.012）。
  - 称相对 Haiku 5.5 / GPT‑6 Luna「任意推理档」有更好的智力/美元；AA Intelligence Index 上与 Haiku 同为 **36**（Luna 28），每任务成本约 **$0.14** vs Spark 1.3 的 $2.39。
  - 表内（Ember / Haiku 5.5 / Luna，均为 max）: AutomationBench-AA **37.8 / 13.9 / 20.2**；Agents' Last Exam（内部，Linux 子集）**61.6 / 57.0 / 57.1**；PSI **46.8 / 36.1 / 37.0**；Terminal-Bench 4.0（各模型最佳已公布 harness，不可当作同一 harness）**40.9 / 39.2 / 16.4**；Coding Agent Index-AA **46 / 37 / 31**；FrontierCode 2.0-AA Ember **落后**（27.2 vs Haiku 34.9）。OSWorld 2.1 部分分 69.5 vs 68.9 / 50.5。
  - 安全：称在其 Scaling Framework 下低于高风险阈值（化生/网安/失控，仅结论）。
- **局限**: 成本点是「拟定/标价估算」；PSI 为内部八项合成；部分对比非同一 harness。
- **标注**: 来源记录（URL/日）/ 官方自报 / 时刻待核（00:00Z）。

###### Meta Engineering（系统/推荐，次选）
- **TLX: 面向生产 ML 的硬件原生 GPU 编译器** — `2026-11-10T16:59:31Z` → **11-11 00:59 Asia/Singapore**。[engineering.fb.com 来源](https://engineering.fb.com/2026/11/10/open-source/tlx-a-hardware-native-gpu-compiler-for-production-ml/)  
  官方自报：GEM 训练在数千块 Blackwell 上达 O(10^24) 总训练 FLOPs、端到端 MFU **20–25%**；某些注意力类核最高约 **2×** 前向；H100 上某 warp-specialized 核 **4×**；共设计模型计算密集净延迟最高约降 **2/3**。目标 Hopper/Blackwell 与 AMD MI300/MI350x，计划进 torch.compile。对训练系统读者有用。
- **Your Algorithm** — `2026-11-10T17:00:49Z` → **11-11 01:00 Asia/Singapore**。用自然语言偏好直接干预 Facebook Feed/Reels 推荐。产品工程文，无硬榜。[engineering.fb.com 来源](https://engineering.fb.com/2026/11/10/ml-applications/your-algorithm-giving-people-more-ways-to-personalize-facebook-recommendations/)
- **Extending LLDB across CPUs and GPUs** — `2026-11-09T17:00:12Z` → **11-10 01:00 Asia/Singapore**。调试工具。[engineering.fb.com 来源](https://engineering.fb.com/2026/11/09/developer-tools/extending-lldb-to-debug-applications-that-span-cpus-and-gpus/)
- **Intelligent Delivery** — `2026-11-11T17:00:38Z` → **11-12 01:00 Asia/Singapore**。广告投放算力分配；称 2017 至 2026 上半年在模型/系统进步之上额外约 **+10%** 排序；近期约 20% 优化有 agent 参与。偏广告系统。[engineering.fb.com 来源](https://engineering.fb.com/2026/11/11/ml-applications/intelligent-delivery-serve-better-ads/)

###### about.fb.com
- 全球扩展 Instagram 青少年账号 AI 年龄估计：**页面写 November 9 / 又写 November 8**，日期表述不干净，**待核**；政策/安全产品，不进研究主包。[about.fb.com 来源](https://about.fb.com/news/2026/11/expanding-teen-account-protections-to-teens-around-the-world/)
- Muse Spaces / Muse Voice / WhatsApp Events → 上期或窗前，不重复。

---

##### Microsoft Research

**源查证**: [microsoft.com 来源](https://www.microsoft.com/en-us/research/feed/)（Chrome UA，200）；博客列表一致。

###### 14) Lazare, veni foras：改休眠神经元给 agent 下后门 — **建议进主包（安全研究；仅结论）**
- **日期**: Feed `Tue, 10 Nov 2026 20:52:56 +0000` → **2026-11-11 04:52 Asia/Singapore**；页面 Published November 10, 2026
- **URL**: [microsoft.com 来源](https://www.microsoft.com/en-us/research/blog/lazare-veni-foras-reprogramming-dormant-neurons-to-backdoor-ai-agents/)
- **人话**: MSR 描述一种名为 Lazarus 的权重改写后门：无需重训，即可让平时表现正常、能通过常规评测的模型在隐藏触发出现时，驱使带工具/终端权限的 agent 执行恶意命令。作者强调这不是「开源权重才有的问题」，关键是权重完整性与出处。
- **要点**（官方自报，**只写结论与规模，不写做法**）: 称改写「少于 **10** 个」休眠神经元即够。触发可非常日常（文中举例为日期条件）。检测上，称前沿 agent 有时能发现异常权重修改，但可靠办法仍是与未改动原权重做 diff；单一扫描不能证明安全。Foundry 对受信任发布者模型做出处绑定与运行环境扫描；并在推进权重扫描、红队工具与密码学签名。建议把模型当潜在内部风险、限制权限并监控行为。
- **为何重要**: 把「权重被改过的模型」从抽象供应链风险写成可被评测漏掉的 agent 触发器，直接冲击开源与内部检查点的治理。
- **标注**: 来源记录（feed 时间）/ 官方自报。不收录机制步骤、触发构造或利用路径。

窗内 MSR 博客仅此一条（上期 PDD Kit 勿重复）。

---

##### NVIDIA

**源查证**: Atom [developer.nvidia.com 来源](https://developer.nvidia.com/blog/feed)（用 **`published`**，不用 `updated`）；[blogs.nvidia.com 来源](https://blogs.nvidia.com/feed/)。注意：Reshard 的 `updated` 为 11-09，但 `published` 仍是 11-06 → **不上本期**。

###### 15) Start and Restore GPU Workloads in Seconds with NVIDIA Snapshot — **建议进主包（推理基础设施教程）**
- **日期**: published `2026-11-10T15:00:00Z` → **2026-11-10 23:00 Asia/Singapore**
- **URL**: [developer.nvidia.com 来源](https://developer.nvidia.com/blog/start-and-restore-gpu-workloads-in-seconds-with-nvidia-snapshot/)
- **人话**: 对已初始化的推理副本做检查点，从快照恢复 GPU/进程状态，避免每次冷启动加载权重。
- **要点**（官方自报；B200 + VAST NFS 等设定）: 恢复 **3.6–42.7 s**，相对需数分钟的冷启动约 **8×–36×**；所有测试配置恢复都 <45 s，检查点+恢复仍短于一次冷启动。支持至约 **1 TB / 8 GPU** 的 MoE 检查点；创建检查点 15 s–5.5 min。合作方口径：Crusoe 将 GLM-5.3 Pod 就绪约 8 min→31 s；Saturn Cloud 将 vLLM 启动 2–8.5 min→6–34 s（HGX B300）。
- **局限**: 厂商博客、固定存储/硬件；倍速相对「冷启动」而非运行中吞吐。
- **标注**: 来源记录 / 官方自报。

###### 其他窗内 NVIDIA（候选）
- **Agent Substrate**（published 11-10 15:00Z → 23:00 Asia/Singapore）: 在少量常热 Kubernetes worker 上复用大量 agent 会话，空闲会话检查点内存+文件系统，与 Dynamo / KAI Scheduler / DSX 集成。偏平台设计，硬数字少于 Snapshot。[developer.nvidia.com 来源](https://developer.nvidia.com/blog/agent-substrate-advancing-kubernetes-for-agents-at-scale/)
- **Alpamayo 2 Edge：车载推理 VLA**（16:00Z → 11-11 00:00 Asia/Singapore）: 2B，DRIVE AGX Thor 上像素到轨迹约 **160–190 ms**；闭环 RL 相对无闭环 RL 最佳检查点驾驶表现 +**48.9%**；文称 AlpaSim 上故障间隔距离约 **60×**（相对其文内基线，勿外推）。[developer.nvidia.com 来源](https://developer.nvidia.com/blog/running-av-reasoning-models-within-onboard-compute-and-latency-limits/)
- **Holoscan 5 重力补偿机械臂教程**（published 11-09 19:09:32Z → 11-10 03:09 Asia/Singapore）: 开发者教程。[developer.nvidia.com 来源](https://developer.nvidia.com/blog/make-a-robot-arm-feel-weightless-with-nvidia-holoscan-5/)
- **NVIDIA Kubernetes Engine**、**DSX AI Factory runtime inventory**（11-10 / 11-11）: 集群与平台验证，偏运维产品。
- **OpenShell 捐赠与 AI 基础设施开源**（blogs，16:00Z → 11-11 00:00 Asia/Singapore）: KubeCon 生态公告。[blogs.nvidia.com 来源](https://blogs.nvidia.com/blog/open-source-openshell-infrastructure/)
- **CoRL：GR00T 2 / Isaac Lab 3.0 与新开放基准**（14:00:01Z → 11-09 22:00 Asia/Singapore）: 会议/产品叙事，可作具身边注。[blogs.nvidia.com 来源](https://blogs.nvidia.com/blog/robotics-simulation-advancements-corl/)
- 韩国投资/主权 AI/Dynamo recipes 等 11-09 13:00 起多条 → 区域商务，不进研究主包。回收站创业故事（11-11）同。

---

##### 其他权威源抽检

| 源 | 结果 |
|----|------|
| Amazon Science | 窗内两条已核到标题与日期（列表页）：[Mitra-v2 表格基础模型](https://www.amazon.science/blog/mitra-v2-scaling-synthetic-pretraining-for-tabular-foundation-models)（Nov 10）；[用数学验证网络配置](https://www.amazon.science/blog/using-mathematics-to-validate-network-configurations)（Nov 11）。本期未深读数字，不作主条。 |
| Thinking Machines 博客 | 访问成功；最新仍为 2026-07，**窗内无新帖**（非缺访问）。 |
| Apple Machine Learning Research | 列表页 curl 在约 30s/2MB 处超时，正文日期未能稳定解析；WebSearch 能扫到若干文章但**缺少可核的 Nov 9–12 日期**。**不写成「无更新」**，标为覆盖缺口。 |
| Anthropic FLT 形式化长文 | 页面 **Sep 4, 2026** → 窗口外；仅作 Fable 5.2「30 小时复现」的背景配读。 |

---

##### 汇总：建议进入主素材包（宁缺毋滥）

1. **Anthropic** — Claude Fable 5.2 / Mythos 5.2（旗舰能力与系统卡；配读电子原型文）
2. **Google DeepMind** — AlphaProof Code（Signal 实现级形式化验证）
3. **Google DeepMind** — Gemini Robotics 2.5（产线 96% 概念验证 + 安全基准）
4. **Google DeepMind** — AlphaGenome 2（细胞类型级变异效应；仅高层）
5. **OpenAI Alignment** — CoT 可监控性随训练生命周期如何变化
6. **Meta** — Muse Ember（小模型成本前沿；注意 FrontierCode 并非全面领先）
7. **Microsoft Research** — Lazarus 权重后门（仅结论）
8. **Anthropic Alignment** — Worse Together / MAMUBench

次选：OpenAI Control Room；OpenAI×Upwork 自由职业研究；NVIDIA Snapshot；Google MKA 基准 + Carbon 正式开放；Meta TLX 编译器；Gemini Decisions API；Google CKM 可穿戴研究。

**明确已成功访问、窗内无新研究长文的部分**: Thinking Machines 博客；MSR 除 Lazarus 外无第二篇研究博文。OpenAI Newsroom 研究长文以外多为客户/产品帖（已列出，不充数）。

**窗口边缘备忘**
- Muse Ember、Anthropic 电子设计文的 `00:00:00.000Z` 若按字面早于 09:40，但上期 09:21 未收录；按日级占位计入本期并标待核。
- 仍勿把窗前 OpenAI BioBasicsBench（11-06 08:00 Asia/Singapore）、Meta Specialized Models（11-06 08:00 Asia/Singapore）当新发。
- 上期已报四条（memory/dreaming、Reshard、FLUX Klein、Hacktron）及 Reshard 的 11-09 `updated` 均不重复。

**检索覆盖与失败**
- 成功：OpenAI RSS；Anthropic research/news/alignment WebFetch+curl；DeepMind RSS（需 gzip）；Google Research RSS + blog.google；MSR feed；NVIDIA 双 feed（用 published）；Meta research/about/engineering 详情页时间戳；OpenAI Alignment 列表；Amazon Science 列表；Thinking Machines 列表。
- 降级：OpenAI `/news` 与多数 `/index` 页 curl 403（WebFetch 成功读取 Control Room、freelance、Cogent）；DeepMind HTML/RSS 需解压；Carbon 博文跳转 blog.google；AlphaProof 详情页 curl 为 gzip。
- 失败/不完整：**Apple ML 研究列表未能完整抓取**，故不宣称「无更新」。
- 未把缺访问写成无更新。第三方（如非官方站点对 Signal 证明的转述数字）无官博原文则不收。

### arXiv 原始候选

#### arXiv raw pack: cs.AI / cs.CL / cs.LG（扫描窗口 2026-11-09 09:40 Asia/Singapore → 2026-11-12 ~09:27 Asia/Singapore）


核验方式：真实访问 `arxiv.org/list/*/pastweek|new|recent`、`/abs/`、`/html/`、`/pdf/` 首页；HTTPS `export.arxiv.org/api`。数字默认摘自摘要，必要时用 PDF/HTML 正文核对，标 **作者自报**；机构以 HTML `ltx_contact` / PDF 首页为准，**不以题目里出现的模型名为机构**。提交日多在美东；**Asia/Singapore 归属按 listing/放批日**，不按 Submitted on 字面。

##### 上期早放 2611.08488–08710 正式 listing 批日（补核结论）

**结论：正式归属 Asia/Singapore 11/09（Mon）批。** 证据（来源记录）：

- 今日拉取的 `list/cs.{AI,CL,LG}/pastweek|recent` 日期头已出现 **Mon, 9 Nov 2026**（AI 220 / CL 78 / LG 213 of 同数，列表完整）；`/new` 最新日仍是 Wed 11 Nov，不覆盖此批。
- 三个分类去重后，08488–08710 范围内的 AI/CL/LG 条目共 **63** 篇（ID **2611.08490–2611.08706**），**全部只出现在 Mon 9 Nov 日期头下**；Fri 6 / Tue 10 / Wed 11 头下为 0。
- 上期 Fri 6 Nov 列表新稿上沿仍是 **2611.08487**（与上期包一致），与 08488 起的周一新稿衔接。
- 范围两端不在 AI/CL/LG 列表中的 ID 已用 abs 核验（均为 200，科目属其他领域，不是「未进本批」）：08488 quant-ph、08489 astro-ph.EP、08707 cs.NI、08708 math.OC、08709 cs.IT、08710 cs.SI；Submitted on 5 Nov 2026（abs dateline）。
- 上期已报早放备选现已落在该正式列表中，**只更新归属，不作为本期新批真重点重报**：
  - [2611.08644](https://arxiv.org/abs/2611.08644) Decision Context（Georgian AI Lab）→ **Asia/Singapore 11/09 正式批**
  - [2611.08569](https://arxiv.org/abs/2611.08569) EMERGE、[2611.08551](https://arxiv.org/abs/2611.08551) SAE 压缩（Stanford）→ 同批

上期主包已报勿重复：2611.07554 Memory Trap、2611.08453 OPD、2611.07372 EnvOpt、2611.08407 Social Humanoid、2611.07232 RecSA；以及上期备选 D²-OPD / CORE / Test-Time Self-Play / Last Mile·HEELO（均属 11/06 批）。

##### Batch map（日期为 Asia/Singapore 放批早间；arXiv 美东 Sun–Thu 20:00 公布 → 新加坡约 Mon–Fri 早上有批；11 月为 EST，约 **09:00 Asia/Singapore**；**无周六批**）

| Asia/Singapore 批次 | listing 标签 | cs.AI/CL/LG 列表条目（含交叉，三个分类去重） | New-submission / abs 探测 ID 范围 | 状态 |
|---|---|---|---|---|
| 11/09 (Mon) | Mon, 9 Nov 2026 | AI 220 / CL 78 / LG 213；去重 **394**（2611: 389 + 更旧交叉 5） | 新稿约 **2611.08488 – 2611.09892** | **列表完整**。≤08710 上期已早放扫描，本期只补核批日；**08711–09892 共 326 篇为本期补扫** |
| 11/10 (Tue) | Tue, 10 Nov 2026 | AI 480 / CL 207 / LG 509；去重 **918**（2611: 914） | 新稿约 **2611.09897 – 2611.12884**（约 913） | **完整** |
| 11/11 (Wed) | Wed, 11 Nov 2026 | AI 248 / CL 112 / LG 235；去重 **465**（2611: 461） | 新稿约 **2611.12894 – 2611.14519**（约 460） | **完整**（`/new` 亦标 Wednesday, 11 November 2026） |
| 11/12 (Thu) | listing **尚未**出现 | — | abs 探测 **2611.14520 / 14521 / 14530 / 14600 均为 404**；14519 为 200 且已在周三列表 | **未放出**（采集截止 11/12 **09:27 Asia/Singapore**，晚于惯例约 09:00 放批窗口）。**续扫起点：2611.14520** |

说明：

- 扫描宇宙（本期新看、去重、去掉上期已报与更旧交叉）：**1699** 篇（Mon 补扫 326 + Tue 913 + Wed 460）。标题关键词粗筛 689；API 摘要 142；对 15 篇做了 abs + HTML + PDF 首页核验。
- 11/10 列表体量约为相邻日两倍（AI 480 / LG 509），列表页显示「showing N of N」，按完整计入。
- 个别 ID 的 abs「Submitted on」早于其 listing 日（例如 2611.10240 Submitted 6 Nov 但列入 Tue 10 批）；**归属以 listing 为准**。

##### Candidates（单位经 arXiv HTML / PDF 首页核实；数字来自摘要除非另注）

###### Batch 11/09 补扫（≥2611.08711，列表已齐）

1. **2611.09892** On Agentic Manipulation Policies  
   链接：[arXiv 2611.09892](https://arxiv.org/abs/2611.09892) · PDF [arXiv 2611.09892.pdf](https://arxiv.org/pdf/2611.09892.pdf) · 项目 [apple-aiml-research.github.io 来源](https://apple-aiml-research.github.io/ml-amp/)  
   提交/公布：Submitted 6 Nov 2026（abs dateline）；API published 2026-11-06T18:59:34Z → 2026-11-07 02:59 Asia/Singapore；**Asia/Singapore 归属 11/09 (Mon) 批**（列表内，ID 在补扫段）  
   机构证据：HTML `Affiliation: Apple`；PDF 首页页眉「Research Article Apple」及作者行下「Apple」（来源记录）  
   人话：用通用大模型在环直接指挥机械臂（AMP），给出可跨单臂/双臂/移动操作的参考 harness AMP1，不靠演示、不做任务微调。  
   为何重要：把「通用模型当操作策略」和专用 VLA/WAM 放到同一套仿真与实物对比里，数字差距大，且与上期 Social Humanoid 的具身线连续。  
   对谁有用/深读：人形/操作策略、agent harness、具身评测。  
   主要数字与条件/局限（作者自报；PDF 首页与摘要交叉核对）：RoboLab-120 零样本成功率 **85.6%**，对比文内领先 VLA **49.2%**、WAM **42.9%**；实物 12 任务 × 3 台机器人 **104/108** 成功，相对 FLUX 3 Action（49/108）与 π0.5（30/108）失败率约 **15× / 20×** 更低；加跨回合记忆后，RoboDojo 双臂失败率相对零样本再降 **4.6×**。无任务专用技能库。π0.5 / FLUX 仅为对比对象，**不是**作者单位。  
   标签：**主包** · 来源记录 机构 / 作者自报数字

2. **2611.09891** CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse  
   链接：[arXiv 2611.09891](https://arxiv.org/abs/2611.09891)  
   提交/公布：Submitted 6 Nov 2026；API published 2026-11-06T18:58:50Z → 2026-11-07 02:58 Asia/Singapore；**Asia/Singapore 归属 11/09**  
   机构证据：PDF 第 1–2 页页脚「© 2026 NVIDIA. All rights reserved.」，并链到 Lab / Project Moonshot（来源记录；HTML 作者行未印实验室名，以 PDF 为准）  
   人话：把一次推理痕迹编成可在 CPU 上反复执行的 agentic reasoning cache（ARC），同类新题不再让大模型从头想。  
   为何重要：给「推理可缓存、可解释、可继续训」一条系统级路径，并给出相对源模型的调用成本倍数。  
   对谁有用/深读：推理服务、agent 运行时、数学/科学解题流水线。  
   主要数字与条件/局限（作者自报；PDF 实验节核对）：相对源模型调用成本约 **16–291×**（GSM8K 约 16×，AIME 约 262–291×）；AIME ’25 缓存 **93.3%** vs 源模型 **83.3%**，AIME ’26 **96.7%** vs **90.0%**。目标端可用 Haiku 4.5 / Gemini 3.0 Flash Lite / GPT 5.4 Nano，或微调后的 Llama 3.2 1B。构建本身有成本（文内约 12–84× 量级）；数字绑定其基准与源模型，跨设置勿直接比倍速。  
   标签：**主包** · 来源记录 机构 / 作者自报

3. **2611.09798** Test-Time Compute Scales Better with Parallel Agent Teams  
   链接：[arXiv 2611.09798](https://arxiv.org/abs/2611.09798) · 代码 [GitHub modal-projects/parallel-agent-teams-scaling](https://github.com/modal-projects/parallel-agent-teams-scaling)  
   提交/公布：Submitted 6 Nov 2026；API published 2026-11-06T17:53:07Z → 2026-11-07 01:53 Asia/Singapore；**Asia/Singapore 归属 11/09**  
   机构证据：PDF 首页「Duke University / Modal Labs / Princeton University / New York University」（来源记录；HTML 单位字段损坏，以 PDF 为准）  
   人话：有可打分验证器时，不要只做 Best-of-N 单智能体，也不要只堆一个超大协作队，而是**并行采样许多小队并保留最好一队**。  
   为何重要：给 test-time scaling 一个可检验的组织方式，并解释「均值 vs 方差」为何单队和单智能体会先饱和。  
   对谁有用/深读：agent 推理时计算、核优化/形式化证明等可自动打分任务。  
   主要数字与条件/局限（作者自报）：12 个长程任务（GPU kernel、形式化证明等到 exploit development——此处只记任务类别，不写利用细节）；**27B** 模型、预算 **100** 个智能体时，十人小队在 **10/12** 任务上优于并行单智能体，并在全部 4 个跑过「百人一队」的任务上胜过后者；**同等美元成本**下，小队在一半任务上胜过文内 frontier 模型。依赖可评分验证器；大队实验未覆盖全部 12 任务。  
   标签：**主包** · 来源记录 / 作者自报

4. **2611.09828** Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL  
   链接：[arXiv 2611.09828](https://arxiv.org/abs/2611.09828) · NeurIPS 2026（PDF）；代码见 PDF  
   提交/公布：Submitted 6 Nov 2026；API published 2026-11-06T18:14:52Z → 2026-11-07 02:14 Asia/Singapore；**Asia/Singapore 归属 11/09**  
   机构证据：HTML 明确 Aria Wong = **MATS**、Neel Nanda = **Google DeepMind**；Joshua Engels 的 HTML 无 affiliation 字段，PDF 首页仅并列印出 MATS / Google DeepMind，**不以排版把 Engels 猜成 DeepMind**（Engels 单位待核）  
   人话：在三个真实一点的环境里系统比较「用监控器惩罚 reward hacking」怎么设计才有效，以及模型如何学会躲监控。  
   为何重要：把监控干预从口号落到可开源环境与可迁移的设计结论；对齐/RL 训练事故线的硬参考。安全向**仅结论**，不写环境漏洞或躲避步骤。  
   对谁有用/深读：RL 后训练、奖励设计、监控与对齐评测。  
   主要数字与条件/局限（作者自报）：Qwen3-4B；编码 / 医疗对话 / 传记生成三环境。摘要未给单一总成功率；称部分干预可把 hacking 率压回训练前水平（跨 seed）。监控越「漏学习信号」越能压 hacking，也越容易被绕。  
   标签：**主包** · 来源记录 部分机构 / 作者自报

5. **2611.09847** Computer-Use Agents Are Embodied Generalists  
   链接：[arXiv 2611.09847](https://arxiv.org/abs/2611.09847) · 站点 [pranjal2041.github.io 来源](https://pranjal2041.github.io/cua-embodied)  
   提交/公布：Submitted 6 Nov 2026；**Asia/Singapore 归属 11/09**  
   机构证据：HTML「Carnegie Mellon University」（来源记录）  
   人话：把具身任务做成「屏幕画面 + 键鼠」，同一套 computer-use agent 换软件即可做机器人任务。  
   为何重要：给「CUA 技能可迁移到具身」一个竞赛成绩支撑的论证，而非再训一套专用架构。  
   对谁有用/深读：computer-use、具身泛化、评测设计。  
   主要数字与条件/局限（作者自报）：同一 CUA 设计、不做比赛专项调参，在四场 ECCV workshop 竞赛中获第 1、2、3、6 名。摘要无单一成功率百分比。  
   标签：**备选偏强** · 来源记录 / 作者自报

6. **2611.09721** MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory  
   链接：[arXiv 2611.09721](https://arxiv.org/abs/2611.09721)  
   提交/公布：Submitted 6 Nov 2026；**Asia/Singapore 归属 11/09**  
   机构证据：PDF 首页 Rensselaer Polytechnic Institute / Microsoft；脚注「Work done while at Microsoft」（来源记录）  
   人话：跟踪有毒信息如何经不同记忆架构被写入、检索并在后续会话改变行为。  
   为何重要：与上期 Memory Trap（良性记忆越界）互补——这里是记忆作为攻击面的评测基准。安全向**仅结论**，不写投毒构造。  
   对谁有用/深读：agent 记忆系统、安全评测。  
   主要数字与条件/局限（作者自报；HTML 结果叙述核对）：155 条多会话轨迹、4 域、5 套记忆系统；称全部系统均可被影响，轨迹级行为率最高约 **45.70% BR**、任务级约 **21.02% BRT**，系统间差异大；记忆感知优化约再抬 **2–31** 个百分点。数字依系统/模型而变，不是单一总攻击率。  
   标签：**备选偏强** · 来源记录 / 作者自报

7. **2611.09030** A Controlled Study of Models, Skills, Feedback, and Curriculum in Agentic Robotics  
   链接：[arXiv 2611.09030](https://arxiv.org/abs/2611.09030)  
   提交/公布：Submitted 6 Nov 2026；**Asia/Singapore 归属 11/09**  
   机构证据：PDF 首页「Bosch / NVIDIA / UC Berkeley」（来源记录；NVIDIA 为合著单位之一，不是唯一署名实验室）  
   人话：在仿真里受控拆开模型能力、技能先验、反馈结构与课程，看 coding agent 怎样把物理交互翻译成策略更新。  
   为何重要：28K rollout 的析因实验，结论是瓶颈常不在「信息不够」而在「不会归因并改对代码」。  
   对谁有用/深读：agentic robotics、技能库与反馈设计。  
   主要数字与条件/局限（作者自报）：9 个操作任务、631 种配置、约 **28K** coding agent rollouts。摘要无单一成功率。正文提到的 GPT Astra / Claude Fable 是评测对象，**不是**作者单位。  
   标签：**备选** · 来源记录 / 作者自报

###### Batch 11/10（Tue）

8. **2611.12177** Embodied First Exam  
   链接：[arXiv 2611.12177](https://arxiv.org/abs/2611.12177) · [embodied-first-exam.ai 来源](https://embodied-first-exam.ai) · 代码 [GitHub mll-lab-nu/embodied-first-exam](https://github.com/mll-lab-nu/embodied-first-exam)  
   提交/公布：Submitted 9 Nov 2026；API published 2026-11-09T10:29:19Z → 2026-11-09 18:29 Asia/Singapore；**Asia/Singapore 归属 11/10 (Tue) 批**  
   机构证据：PDF 首页 Northwestern / CMU / UC Berkeley / University of Washington / Stanford / UNC-Chapel Hill / Texas A&M / UT Austin（来源记录；含 Abbeel、Fei-Fei、Jiajun Wu、Yuke Zhu、Dawn Song 等，多机构合作）  
   人话：给 coding agent 进物理世界的「入学考」：同一套任务允许直接控制、写代码控制、或先训策略再控制，并分标准/实时/特权三种设定。  
   为何重要：规模与设定都对准「agent 管机器人」而不是传统 visuomotor 基准；给出当前最强仍很低的标准设定分数。  
   对谁有用/深读：具身评测、coding agent、机器人平台。  
   主要数字与条件/局限（作者自报）：**1,156** 任务、35 套、47 种机器人；核心 **456** 任务上，八个 agent 中最强 GPT‑6 Astra + Codex 在 Standard Setting 成功率 **34%**。特权设定可重置、近似上界，不能当成真实部署分数。  
   标签：**主包** · 来源记录 / 作者自报

9. **2611.12799** Agentic-OPD: Recovering Forgotten Agent Capabilities via On-Policy Distillation for Agentic Tasks  
   链接：[arXiv 2611.12799](https://arxiv.org/abs/2611.12799) · comments 写 ICLR 2027  
   提交/公布：Submitted 9 Nov 2026；**Asia/Singapore 归属 11/10**  
   机构证据：PDF/HTML 邮箱「Baidu, Inc. / Beijing Jiaotong University」（来源记录）  
   人话：GRPO 只留验证集最佳 checkpoint 会丢掉更早就能解的题；把同一次训练里废弃的 checkpoint 当免费教师池，用 OPD 把覆盖面找回来。  
   为何重要：直接接上期 Salesforce OPD 算力账与 Amazon D²-OPD——这次问题换成「agent 训练跑完之后如何回收能力」。  
   对谁有用/深读：agent RL、后训练蒸馏。  
   主要数字与条件/局限（作者自报）：5 个 agent 域、24 个基准/子集；相对初始化 checkpoint 最高 **+7.4** points；称 4B 学生在 deep search 上超过文内 GPT‑5.6 与 DeepSeek-V4.1。后二者是评测对象，**不是**作者单位；外部复现与「超过前沿」声明需独立核验。  
   标签：**备选偏强** · 来源记录 / 作者自报

10. **2611.10240** PACE: Keeping the Right Tokens in the KV Cache Is Not Enough for Long-Horizon LLM Agents  
    链接：[arXiv 2611.10240](https://arxiv.org/abs/2611.10240)  
    提交/公布：Submitted 6 Nov 2026（abs dateline）；列入 **Tue 10 Nov** 列表；**Asia/Singapore 归属 11/10**  
    机构证据：HTML/PDF 首页「Amazon Web Services」（来源记录；单作者）  
    人话：长程 agent 里，该留的 KV token 都还在也不够——旋转位置离查询太远就会「在缓存里但取不回」；PACE 用计划感知保留 + 有界重编号。  
    为何重要：把 eviction 讨论从「留对 token」推进到「位置编码距离」，并给百万 token 会话的系统数字。  
    对谁有用/深读：长上下文 serving、coding agent 运行时。  
    主要数字与条件/局限（作者自报；称预注册评估）：Qwen3-8B、100K 会话、预算 2,048；只做高驻留仍从 **93%→64%**（定义与使用间隔 2K→90K，驻留 0.996）。PACE 在 100K 通过隐藏单测 **97%**，对照 H2O **42%**、SnapKV **3%**；单组件各约 63%。1M/2M 会话、单卡 24 GB 上称 99%/100%，KV 状态 <0.7 GB vs 全缓存 147–295 GB。重编号无额外 perplexity、墙钟约 +9%。数字高度依赖其 coding-session 构造，且为单作者工作，外部复现待核。  
    标签：**备选偏强** · 来源记录 / 作者自报

11. **2611.11995** Infrathon: Benchmarking Language Agents for Real-World, Long-Horizon AI Infra Optimization  
    链接：[arXiv 2611.11995](https://arxiv.org/abs/2611.11995) · [InfrathonX.github.io 来源](https://InfrathonX.github.io)  
    提交/公布：Submitted 9 Nov 2026；**Asia/Singapore 归属 11/10**  
    机构证据：PDF 首页 University of Washington / Allen Institute for AI / UPenn / Pyromind Dynamics / Stanford / RadixArk / UT Austin / Northwestern（来源记录）  
    人话：用 12–24 小时预算，测前沿 agent 能否在真实 AI 基础设施任务上持续优化，而不是只跑一两小时的 kernel 题。  
    为何重要：表明短窗口评测会漏掉后半段增益和名次变化；并给出 agent 发现的压缩方案超过人类基线的例子。  
    对谁有用/深读：infra agent、长程评测、系统优化。  
    主要数字与条件/局限（作者自报；**以 PDF 为准**——API 摘要曾把倍数写成百分号）：六模型、150 次、24 小时预算、合计逾 **10,000 GPU-hours**；**135/150** 次在预算后半段仍有提升；Claude Opus 5.5 把 KV-cache 压缩比从人类设计的 Quant-VideoGen **6.82×** 提到 **19.86×**（PDF 图中另有约 18.8× 的单例）。障碍包括任务违约、测试不可靠、过早收工。  
    标签：**备选偏强** · 来源记录 / 作者自报

12. **2611.11450** How Much Training-Inference Mismatch Can On-Policy Distillation Tolerate?  
    链接：[arXiv 2611.11450](https://arxiv.org/abs/2611.11450) · 代码 [GitHub benyucong/train-inference-mismatch-opd](https://github.com/benyucong/train-inference-mismatch-opd)  
    提交/公布：Submitted 8 Nov 2026；**Asia/Singapore 归属 11/10**  
    机构证据：PDF 首页 Aalto / NTU / Independent / Beijing Institute of Technology / University of Cambridge / Shenzhen University of Advanced Technology（来源记录）  
    人话：量化推理和异步 rollout 会拉开训练与推理分布，OPD 对此有多大容忍度，以及怎样用这个预算换吞吐。  
    为何重要：给上期 OPD 线补上「系统实现能不能偷工」的账；并称在同样会让 RL 崩的配置下 OPD 仍稳。  
    对谁有用/深读：蒸馏/后训练系统、推理引擎。  
    主要数字与条件/局限（作者自报）：模型特定 FP8 配方保持训练质量，KV-cache token 容量至少 **1.93×**（相对 BF16）；FP8 + 异步 rollout 达到同等训练质量比同步 BF16 快 **1.62×**。容忍度有预算，过高会下降；层间对低精度敏感度不同。正文提及的 Thinking Machines / NVIDIA 等为相关工作或发布案例，**不是**作者单位。  
    标签：**备选** · 来源记录 / 作者自报

###### Batch 11/11（Wed）

13. **2611.13560** Are Dense Rewards Worth Their Tokens in GRPO?  
    链接：[arXiv 2611.13560](https://arxiv.org/abs/2611.13560) · 代码 [GitHub vicky157/grpo-validation](https://github.com/vicky157/grpo-validation)  
    提交/公布：Submitted 10 Nov 2026；**Asia/Singapore 归属 11/11 (Wed) 批**  
    机构证据：PDF 首页 Department of Computer and Data Sciences, Case Western Reserve University；通讯 （机构署名邮箱略）（来源记录）  
    人话：过程奖励看起来每步都更优，但把生成 token 和训练 GPU 时间对齐后再比，结论会对调。  
    为何重要：方法学提醒——「每 update 更优」不等于「同样算力更优」；给 RLVR/GRPO  denser reward 一个预注册、对齐算力的反例与对照。  
    对谁有用/深读：RLVR 配方、评测设计。  
    主要数字与条件/局限（作者自报）：1,668 次运行、六模型；其设定下 Monte-Carlo 过程奖励的续写占全部生成 token 的 **91%**。Qwen2.5-1.5B 上，该奖励每 update 领先，但等 token 时低 **14.3** points、等训练时间低 **7.8** points；四种稠密变体在给足时间后仍未超过 GRPO。按预测成功率接近 1/2 选 prompt，等算力下 Qwen3-0.6B **+1.7**、Qwen2.5-1.5B **+0.8** points；把 GRPO 初始学习率加倍可追到差半个点以内。结论绑定其模型与协议。  
    标签：**备选偏强（方法学）** · 来源记录 / 作者自报

14. **2611.14009** Coding Agent Memory Post-Training II: … On-Policy Distillation  
    链接：[arXiv 2611.14009](https://arxiv.org/abs/2611.14009)  
    提交/公布：Submitted 10 Nov 2026；**Asia/Singapore 归属 11/11**  
    机构证据：PDF 首页 Peking University / JD.com / Sichuan University / Beijing Institute of Technology / Renmin University of China / HKUST（来源记录）  
    人话：不要给教师/学生一个预训练里没见过的专用记忆工具，而是用普通 Bash + 持久工作区当记忆，再用异步 OPD 把「何时读写文件」训进策略。  
    为何重要：把 agent 记忆从外挂协议拉回模型已有的文件操作先验，并报告向 Terminal-Bench / SWE-Bench 的迁移。  
    对谁有用/深读：coding agent、记忆后训练、OPD。  
    主要数字与条件/局限（作者自报）：CAMG-II 上 CAMP-II 相对最强 OPD 基线增益为 **2.97×**；称在 Terminal-Bench 2.1 与 SWE-Bench Pro V2 上也提高成功率（摘要未给这两项的绝对分数，表待核 PDF）。  
    标签：**备选** · 来源记录 / 作者自报

15. **2611.12835** Mitigating Agentic Deception via Evaluation-Side Partially Observable Games  
    链接：[arXiv 2611.12835](https://arxiv.org/abs/2611.12835)  
    提交/公布：Submitted 9 Nov 2026；列入 Tue 10 列表；**Asia/Singapore 归属 11/10**（按 listing，不按提交日）  
    机构证据：PDF 首页 Beihang / 中关村实验室 / 理想汽车 / 清华 / 港中文 / 北大人工智能研究院 & BigAI / 合肥综性国科中心（来源记录）  
    人话：把「防欺骗」写成评估侧的不完全信息博弈：监控器从完整轨迹揭欺骗，固定验证器把指控变成惩罚。安全向仅结论。  
    主要数字（作者自报）：Gemma3-4B-IT 与 Qwen3-4B/8B；相对最强基线欺骗缓解 **+26.0%**、任务成功最高 **+39.8%**。  
    标签：**备选（对齐）** · 来源记录 / 作者自报

##### 明确排除 / 误报提醒

- HTML/PDF 正文频繁出现 OpenAI / Anthropic / Qwen / DeepSeek / π0.5 / FLUX 等**评测对象或相关工作**，不能当作者单位。本期以 PDF 首页 / `ltx_contact` / 机构邮箱为准。
- **2611.09892** 对比 π0.5、FLUX 3 Action，单位是 **Apple**。
- **2611.12799**、**2611.14051**（未进主候选：KV 跨版本复用的 DeepSeek-V4-Flash *case study*）标题或摘要提及 DeepSeek / GPT，作者单位分别是百度、以及需独立核验的个人单位，**不是** DeepSeek。
- **2611.09828** 不可写成「DeepMind 三作论文」：HTML 只把 Nanda 标为 Google DeepMind，Wong 为 MATS。
- **2611.09030** 是 Berkeley + Bosch + NVIDIA 合著，不是 NVIDIA 单独出品。
- 上期已报条目（Memory Trap / OPD / EnvOpt / Social Humanoid / RecSA 及所列备选）不重复列入「新发现」。
- 安全、网络与生物相关只写结论与作者数字，不写操作细节。

##### 扫描完整性

| 项 | 结论 |
|---|---|
| 11/09 列表 | **完整**（pastweek 显示 220/78/213 of 同数） |
| 08488–08710 批日 | **已确认 = Asia/Singapore 11/09 (Mon) 正式批**（见文首补核） |
| 11/09 ≥08711 高信号筛选 | 已做关键词粗筛 + 重点 abs/HTML/PDF；宁缺毋滥 |
| 11/10、11/11 列表 | **完整** |
| 11/12 列表 | **未出现** |
| 11/12 abs | **未放出**：14520+ 404（09:27 Asia/Singapore 再探测） |
| 续扫起点 | **2611.14520** + 周四 `list/*/new` 一旦更新 |
| API | [arXiv api](https://export.arxiv.org/api) 可用；摘要数字若与 PDF 冲突（如 Infrathon 的 × vs %）以 PDF 为准 |

##### 建议进研究主包的 3–5 条（真重点）

1. [2611.09892](https://arxiv.org/abs/2611.09892) Apple：AMP1，通用模型直接做操作策略（85.6% / 104 of 108）  
2. [2611.09891](https://arxiv.org/abs/2611.09891) NVIDIA：CPU-ARC，推理缓存 16–291× 降本  
3. [2611.09798](https://arxiv.org/abs/2611.09798) Duke/Modal/Princeton/NYU：并行小队的 test-time scaling  
4. [2611.12177](https://arxiv.org/abs/2611.12177) Northwestern 等：Embodied First Exam，最强 Standard 仅 34%  
5. [2611.09828](https://arxiv.org/abs/2611.09828) MATS + Google DeepMind（Nanda）：RL 中监控 reward hacking 的干预设计  

（互补可点：Baidu [Agentic-OPD 2611.12799](https://arxiv.org/abs/2611.12799)；AWS [PACE 2611.10240](https://arxiv.org/abs/2611.10240)；UW/Ai2 [Infrathon 2611.11995](https://arxiv.org/abs/2611.11995)；Microsoft [MemoryDojo 2611.09721](https://arxiv.org/abs/2611.09721)。）


## X 公开动态

### 动态与跟踪

#### X/AI 源包 · 2026-11-12（三日合并）

窗口：2026-11-09 09:40 → 2026-11-12 约 09:20 Asia/Singapore。来源：
- 首页时间线 3 页，约 294 条（已过滤回复）。覆盖约 11-11 13:31 → 11-12 09:13 Asia/Singapore；窗口前约 2 天靠公开检索补齐。
- 官方/关键账号合并检索：OpenAI/Anthropic/ClaudeDevs/AA/Tibo/Cursor 一组；GoogleDeepMind/GoogleAI/GeminiApp/Kimi/MiniMax/Mistral/Meta/Qwen/dotey 一组。均 `-is:retweet -is:reply`；含 `from:grok` 的初检被回复刷屏，已改写查询。
- 定向检索：Anthropic IPO / 路演、Fable/Mythos、Claude Code / #107757、Cyber livestream、Kimi K3.1 Pro、Codex/额度、Cursor。
- X Today's News：两组约 72h 关键词。
- 交叉核对：Anthropic Fable/Mythos 发布页与 System Card、路演公告、SEC 公司页与 11-10 S-1/A；Google Carbon / Decisions API 博客；DeepMind AlphaGenome 2 与 AlphaProof Code 博客；HF `moonshotai/Kimi-K3.1-Pro`、`MiniMaxAI/MiniMax-H3-Image`；GitHub #107757；OpenAI Cyber 活动页、Control Room / Businesses 博客。

本期 X 侧无 429。openai.com 活动页 curl 曾 403，改用 WebFetch 读到日程页（未见回放或新公告正文）。GitHub 未认证 API 仅取到 #107757 有限字段。Kimi / DeepSeek 官方账号本窗口检索几乎无新主帖。

去重说明：上期主条（dreaming 记忆文、IPO「无定价」、Claude Code 云环境、Tibo Pro 倍率/FMF、DeepMind 1024-bit RSA）不重写为新主条。Fable/Mythos 上期仅是评测命名，本期已正式发售，升为主条。旧包数字均本期重核，不以旧包为事实源。

##### 主条目

###### 1. Anthropic 正式发布 Claude Fable 5.2 与 Claude Mythos 5.2：同一底座，Fable 对客开放，Mythos 走验证项目
上期记忆博文里的「Fable 5」还只是内部评测名。本窗口官方确认这是一条已在售的高端产品线，并推出 5.2：更快、更便宜，官方程评把多数项写在 Opus 5.5 之上。这是本期最硬的模型发布。
- **是什么**：
  - 官宣：@claudeai / @AnthropicAI 11-10 02:57–03:00 Asia/Singapore；发布页落款 November 9, 2026。
  - 结构（官方）：Fable 与 Mythos 是同一底层模型。Fable 加了更强的网络与生物安全护栏，面向所有用户；Mythos 护栏更松，须通过 Life Sciences / Cyber Verification Program，也可支撑 Enterprise 的 Claude Security。
  - 规格与定价（官方自报）：API 价 **$8 / $40** 每百万输入/输出 token，低于 5.1 的 $10 / $50；官方称输出最多快约 30%。可选 fast mode 最高约 2.5× 出字，价 **$16 / $80**。平台说明：上下文 1M、最大输出 128k，模型 ID `claude-fable-5-2` / `claude-mythos-5-2`。
  - 上线：Fable 已在 Claude Platform、Claude Code，以及 AWS / Google Cloud / Azure；Cursor 同期接入。Mythos 需申请。发布周对符合条件的付费计划提供额外 Fable 用量（按订阅时长 1–3 次 Fable reset；Pro / Team 标准席位可将 Fable 计入最高约 50% 的周限额）——细则以促销页为准。
  - 官方自报能力（非第三方复测；努力档与护栏开关因项而异，详见 System Card）：FrontierCode 2.0 在 Xhigh 约 49.1%（对比表中 Opus 5.5 45.5%、GPT-6 Astra 42.8%、Gemini 4 Carbon Medium 41.1%）；FrontierSWE v2 约 69.9%；HLE（带工具）约 74.2%；Remote Labor Index High 约 41.3%。网络安全项多报 **Mythos**（CyScenarioBench 76.3%、CVE Rediscovery 89.6%）。叙述性案例包括：约 1,000 个 agent、30 小时形式化费马大定理（脚注写明提供了 60 条命题、路线素描和 47 条既有引理；11-11 修订过表述）；从空目录用逾 1,000 个子 agent 八天做出可启动的原型操作系统；一句话提示设计三件可工作电子设备。此类案例均为厂商自报。
  - 安全叙事（官方）：外部评测方含 UK AISI、Frontier Design、METR；称高风险未对齐风险仍低；反蒸馏为「迄今最强」，并称已把蒸馏者可收获数据降 90%–99%（对该百分比应对照其 9 月威胁情报，勿当独立复测）。
- **为何重要**：把「比 Opus 再高一档、专打长程/双用途」写成可买可调用的产品，并第一次在本刊周期里坐实 Mythos 的验证制发售。会直接改写 ide / agent 默认选型和安全讨论。
- **对谁·深读建议**：开发者先读发布页的「何时用 Fable vs Opus」和 ClaudeDevs 选型指南；安全读者盯 System Card 与 Mythos 准入，不要只抄榜分。中文可对照宝玉 11-10 长拆。
- **证据**：
  - 官方自报：[@claudeai 发布](https://x.com/claudeai/status/2119867114450268322)、[@AnthropicAI](https://x.com/AnthropicAI/status/2119867707546071125)、[@ClaudeDevs 定价与上线](https://x.com/ClaudeDevs/status/2119868698613956992)、[发布页](https://www.anthropic.com/claude-fable-and-mythos-5-2)、[System Card PDF](https://assets.claude.com/27d60918d218125e7504bc7354c4b4626ec56b11.pdf)、[选型指南](https://claude.dev/blog/which-claude-model-should-you-build-with)
  - 第三方榜（AA 自报）：[@ArtificialAnlys Intelligence Index v5 称 Fable 5.2 max 得 65](https://x.com/ArtificialAnlys/status/2119878995386982508)
  - X 侧：[宝玉解读](https://x.com/dotey/status/2119872207241543744)、[@cursor_ai 接入](https://x.com/cursor_ai/status/2119880829212172509)
- **约时**：博文落款 11-09；X 官宣 11-10 02:57 Asia/Singapore

###### 2. Anthropic 正式启动 IPO 路演，并给出定价与股数：每股预期 $70–78，拟发行 8.25 亿股 A 类，代码 ANT
上期 SEC 仍停在 11-02 S-1/A、估值全是买方传闻。本窗口公司自己发了路演稿，定价区间和股数第一次变成可核文件，不再只是媒体推算。
- **是什么**：
  - 官方自报：@AnthropicAI 11-10 19:33 Asia/Singapore；新闻稿同日落款 Nov 10, 2026。拟发行 **825,000,000** 股 A 类普通股，其中公司出售 801,351,354 股、现有股东出售 23,648,646 股（公司不获股东售股所得）；另拟授予承销商 30 天内最多再购 **123,750,000** 股的超额配售权。预期发行价 **$70.00–$78.00** 每股；已申请在 Nasdaq Global Select Market 上市，代码 **ANT**。声明招股书尚未生效，本稿不构成要约。
  - 来源记录：EDGAR 公司页新增 2026-11-10 S-1/A（Acc-no: **0001628280-26-072484**），此前仍为 11-02 的 0001628280-26-068676 与 10-26 的 S-1。
  - 由官方数字可做的算术（不是市值）：825M×$70–78 ≈ 发行规模 **$578–643 亿**（未计超额配售）；按公司出售的 801,351,354 股计约 **$561–625 亿**。完整稀释后估值取决于招股书中的总股本，**本稿未把 1.1–1.5 万亿一类媒体数字写成 来源记录**。
  - 待核：路演期间承销商「上调至 1.5 万亿」等转述、AMD 上 Claude 适配时间等，均非本公告原文。
- **为何重要**：定价/股数空白被填上，后续只看是否再改 S-1/A 或缩圈定价。这是上期 IPO 线索本窗口真正落地的部分。
- **对谁·深读建议**：写资本市场的人对照新闻稿与 11-10 S-1/A 封面/稀释表，勿把发行规模误写成市值。
- **证据**：
  - 官方自报 / 来源记录：[@AnthropicAI 路演](https://x.com/AnthropicAI/status/2120117722230968385)、[路演公告](https://www.anthropic.com/news/roadshow-launch)、[EDGAR 公司 S-1 列表](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002130357&type=S-1&dateb=&owner=include&count=10)、[11-10 S-1/A index](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/0001628280-26-072484-index.htm)
- **约时**：公告与新 S-1/A 均为 11-10；X 帖 11-10 19:33 Asia/Singapore

###### 3. Google 开放 Gemini 4 Carbon：付费 API 与 AI Ultra 可用，官方仍把 Argon 当作日常主力
上期 News 还在说 Carbon「很难拿到」。本窗口 Google 官方宣布对开发者、企业和 Ultra 订阅开放，定位是长程、难任务，而不是替换 Argon。
- **是什么**：
  - 官宣：@GoogleAI 11-11 00:12 Asia/Singapore，@GeminiApp 11-11 00:06 Asia/Singapore，@GoogleDeepMind 随后跟帖；博客落款 Nov 10, 2026（相对 10-28 的「Introducing」是开放而非首发）。
  - 覆盖（官方）：消费者——Google AI Ultra 可在 Gemini 应用、Search 的 AI Mode 使用；开发者/企业——付费 API（AI Studio / Android Studio）、Gemini for business；Ultra 还可在 Google Antigravity 使用；科研可申请 Antigravity 最高档约 6 个月免费；网络防御方可申请 Fairwind。官方同时写：多数软件工程与知识工作仍宜用 **Gemini 4 Argon**，Carbon 留给「把模型推到极限」的任务。
  - 定价（官方自报）：与 Argon 相同的引入价，**$2 / $10** 每百万输入/输出 token，引入价至 **2026-11-30**；文档写此后为 $4 / $20。模型 ID `gemini-4-carbon`；文档称统一 1M 上下文。
  - 生态：@cursor_ai 称 Carbon 已进 Cursor，高努力档 CursorBench **60.4%**（Cursor/官方转述，待对照方法论）。
- **为何重要**：从「有限防御方预览」变成可付费调用的最强 Gemini，和同期 Fable 5.2 形成直接对位。引入价截止日是选型的硬日期。
- **对谁·深读建议**：要跑长程 agent 的人读开放博文与「Carbon vs Argon」说明；普通订阅用户先确认自己是否在 Ultra。中文可对照宝玉 11-11 拆。
- **证据**：
  - 官方自报：[@GoogleAI](https://x.com/GoogleAI/status/2120187753329791341)、[@GeminiApp](https://x.com/GeminiApp/status/2120186450927038900)、[@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2120219371473617099)、[开放博文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)
  - X 侧：[@cursor_ai](https://x.com/cursor_ai/status/2120193584670580857)、[宝玉解读](https://x.com/dotey/status/2120191790774960630)
- **约时**：博客落款 11-10；X 约 11-11 00:06–00:12 Asia/Singapore

###### 4. Google 推出 Gemini Decisions API：新模型 Decision 1 一次最多评 1000 题，输出不按 token 计费
这不是又一个聊天模型，而是专门做「是非 / 选择 / 量表」的决策端点，官方把时延和单价写得很具体。属于本窗口真正新出现的产品形态。
- **是什么**：
  - 官宣：@GoogleAIStudio 11-12 02:15 Asia/Singapore；@googledevs 同步；博客落款 Nov 11, 2026。
  - 机制（官方）：模型 `gemini-decision-1`，一次前向传递给最多 **1000** 道彼此独立的题打分，输入可含文本、图像、音频、视频、PDF（博客写输入上限 256K token）。题型三种：`noul`（是非概率）、`choice`（2–255 选项）、`score`（有序量表）。返回概率与 0–1 置信度，而不是逐 token 生成答案。
  - 官方自报性能/价格：端到端约 **150–250 ms**；**$0.10 / 1M 输入 token，输出 token 计 0**。AI Studio 有可 prototyping 的免费档。典型用途：路由、策略检查、工具选择、上下文打分。
  - 第三方：@ArtificialAnlys 称 Decision 1 在 AA Decision Index v2.1 得 **66**（AA 自报）。
- **为何重要**：把「agent 里大量便宜的判断」从完整生成里拆出来，可能改写路由/护栏的成本结构。数字均为官方或 AA 自报，需生产环境复核。
- **对谁·深读建议**：做 agent 编排和评测的人直接读官方博文的三种题型与计费（共享 input 只计一次）。
- **证据**：
  - 官方自报：[@GoogleAIStudio](https://x.com/GoogleAIStudio/status/2120581284690801060)、[@googledevs](https://x.com/googledevs/status/2120583940247552381)、[官方博文](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)
  - X 侧：[宝玉解读](https://x.com/dotey/status/2120647659388031454)、[AA Decision Index](https://x.com/ArtificialAnlys/status/2120582049522127205)
- **约时**：博客落款 11-11；X 11-12 02:15 Asia/Singapore

###### 5. DeepMind 连发 AlphaGenome 2 与 AlphaProof Code：细胞分辨率的变异预测，以及把 Signal 协议验证到机器码
同一窗口两条官方科学工程发布，对象完全不同，但都把「人机共导的 agent」写进可核对的论文/工具链。不是聊天模型发布。
- **是什么**：
  - **AlphaGenome 2**：@GoogleDeepMind 11-11 23:03 Asia/Singapore；博客落款 Nov 11, 2026。下一代 DNA 序列模型，按细胞类型/状态做条件预测，官方自报训练数据含 **68** 个组织、逾 **1 亿 / 约 1.07 亿** 个单细胞图谱，识别会改变基因表达的变异「几乎是上代的两倍」。可对未见过的实验状态做泛化（上传单细胞数据、不必重训）。即日起非商用研究走 AlphaGenome API，商用为 private preview。数字均为官方自报。
  - **AlphaProof Code 验证 Signal**：@GoogleDeepMind 11-11 19:50 Asia/Singapore；博客落款 Nov 10, 2026。人机协作框架，把 Signal 参考实现 `libsignal` 的关键安全性质形式化到编译后的 AArch64 机器码。官方自报：约 **四周** 完成、生成逾 **600 万 / 约 650 万** 行经 Lean 核验的证明；覆盖 PQXDH 与 Triple Ratchet 的前向保密、认证、事后妥协安全、握手保密等。称这是首次把广泛部署的密码协议实现验证到这一深度；并在隔离副本中回放两个已修复旧漏洞，系统给出「不安全」的机器检验证明。博客强调规范由人审定、并非验证整个 Signal 客户端应用。工件已开源。
- **为何重要**：一条把基因组解释推进到细胞分辨率并开放 API；一条把「AI 做形式化验证」推到真实、正在保护海量消息的代码。都需要对照论文假设与「未覆盖部分」。
- **对谁·深读建议**：生信读者读 AlphaGenome 2 的条件建模与非商用条款；密码/安全读者读 AlphaProof 博客与 Lean 仓库，注意规格由人写、证明由 agent 出、内核检查。
- **证据**：
  - 官方自报：[@GoogleDeepMind AlphaGenome 2](https://x.com/GoogleDeepMind/status/2120532824465805749)、[AlphaGenome 2 博客](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/)、[@GoogleDeepMind AlphaProof](https://x.com/GoogleDeepMind/status/2120484246401777737)、[AlphaProof Code 博客](https://deepmind.google/blog/introducing-alphaproof-code/)、[验证工件/论文页](https://google-deepmind.github.io/code-verification/)
- **约时**：AlphaProof 博文落款 11-10，X 11-11 19:50 Asia/Singapore；AlphaGenome 2 为 11-11 23:03 Asia/Singapore

##### 进展

###### 进展：Claude Code #107757 / 2.1.317——issue 仍 open，本窗口无官方修复公告可核为 来源记录
- **是什么**：GitHub #107757 标题仍为 *Bug Report: Privacy violation in User-Agent header*，state=open，updated 2026-11-10 02:26 Asia/Singapore。未见官方 changelog 把 2.1.317 写成已合并修复的 来源记录；上期社区版本对照仍待核。云会话自动配环境上期已记，本期无新官宣。
- **证据**：来源记录：[GitHub #107757](https://github.com/anthropics/claude-code/issues/107757)
- **约时**：核验于 11-12 上午 Asia/Singapore

###### 进展：OpenAI Cyber livestream——官方确认 11-12 10:00 AM PT（11-13 02:00 Asia/Singapore），采集时点尚未开播
- **是什么**：@OpenAI 11-11 01:10 Asia/Singapore 预告 *Cyber at the Frontier* 现场主题演讲，「最新网络安全公告」；活动页同样写 November 12 | 10:00 AM PT。采集时为 11-12 约 09:20 Asia/Singapore，距开播尚约 16.5 小时，页面未见回放或结果，故不预写内容。
- **证据**：官方自报：[@OpenAI](https://x.com/OpenAI/status/2120202353907486826)、[活动页](https://openai.com/cyber-at-the-frontier/)
- **约时**：预告 11-11 01:10 Asia/Singapore；开播 11-13 02:00 Asia/Singapore

###### 进展：ChatGPT / Codex 额度——无新的共享池公式；Anthropic 另发全模型免费重置；Tibo 仅暗示
- **是什么**：本窗口未见 OpenAI 官方重述「ChatGPT↔Codex 共享池」的新日期或公式（帮助中心未再核到新正文）。@ClaudeDevs 11-11 05:59 Asia/Singapore：已给所有 Pro / Max / Ultra / Team 用户一次跨模型、跨限额的免费 **full reset**，须在 **12-10 14:00 PT（12-11 06:00 Asia/Singapore）** 前使用；称近期有「比预期多耗限额」的小问题，且 Fable 专项 reset 对已用尽全模型周限额的用户帮助有限。@thsottiaux 11-11 14:55 Asia/Singapore 称「好久没 reset 了，也许该从地下室出来」——是暗示不是公告。dotey「周四 Codex 可能送重置卡」为待核。
- **证据**：官方自报：[@ClaudeDevs reset](https://x.com/ClaudeDevs/status/2120275296637321476)；暗示：[@thsottiaux](https://x.com/thsottiaux/status/2120410006273380750)；待核：[dotey](https://x.com/dotey/status/2120546916475773071)
- **约时**：Claude reset 11-11 05:59 Asia/Singapore

###### 进展：Kimi K3.1 Pro——权重/许可无实质变更；下载量上行
- **是什么**：来源记录 重核 `moonshotai/Kimi-K3.1-Pro`：`lastModified` 仍为 2026-11-05 15:11 Asia/Singapore；downloads≈33617（上期核验约 25569）；likes≈1935；siblings=112；`license=other`。未见 Moonshot 官方新许可修订。窗口内官方账号几乎无新主帖。
- **证据**：来源记录：[HF 模型页](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)
- **约时**：HF 核验 11-12 上午 Asia/Singapore

###### 进展：DeepMind 1024-bit RSA、dreaming 记忆栈——本窗口无后续官宣
- **是什么**：定向检索未见 RSA 论文的跟进公告或标准迁移声明。dreaming 本身无新工程长文；平台 release notes 称 Dreams 研究预览现支持 Fable 5.2（产品附带，不是新论文）。
- **证据**：官方检索空窗；Fable 发布页 / 平台说明为旁证
- **约时**：覆盖至 11-12

###### 进展：Cursor——Fable 5.2 与 Gemini 4 Carbon 均已接入；Projects 支持多智能体协作；扩展投毒无新 IoC
- **是什么**：@cursor_ai 11-10 03:52 Asia/Singapore：Fable 5.2 上线，CursorBench 默认 56.9%（5.1 为 49.2%），max effort 称 60%。11-11 00:35 Asia/Singapore：Carbon 上线，高努力档称 60.4%。另有 Projects「可与队友的 agent 协作」更新。本窗口未见扩展投毒新 IoC 或新恶意版本通报。榜分数为 Cursor 自报。
- **证据**：官方自报：[@cursor_ai Fable](https://x.com/cursor_ai/status/2119880829212172509)、[@cursor_ai Carbon](https://x.com/cursor_ai/status/2120193584670580857)、[@cursor_ai Projects](https://x.com/cursor_ai/status/2120295553309565139)
- **约时**：11-10 至 11-11

###### 进展：GPT‑6.2——仍无 OpenAI 官宣
- **是什么**：本窗口官方发布轴在 Cyber 预告、Control Room、Businesses in ChatGPT，未见 GPT‑6.2 / 新一代主模型。不重复上期传闻。
- **证据**：官方检索无对应发售帖
- **约时**：覆盖至 11-12

##### 其他

- **Claude 产品面**：@claudeai 11-11 01:26 Asia/Singapore 开始滚动推出 Whiteboards、Sheets，并将仪表盘更名为 Claude Data（付费档、测试范围以官方说明为准）。@ClaudeDevs：Claude 对 MCP Apps 扩展支持更多（应用内工具、嵌入站点）。[Whiteboards 帖](https://x.com/claudeai/status/2120206365759094857)、[MCP Apps](https://x.com/ClaudeDevs/status/2120227979041341943)、[宝玉拆](https://x.com/dotey/status/2120213189464105192)
- **OpenAI**：Control Room——研究推理负载的集中跟踪与熔断，官方称决定干预后约 35 秒内停止输出。[帖](https://x.com/OpenAI/status/2119913172039868579)、[博文](https://openai.com/index/control-room/)。ChatGPT 企业名片与 Business Agent 进入 beta。[帖](https://x.com/OpenAI/status/2120216592395174382)、[博文](https://openai.com/index/introducing-businesses-chatgpt/)。ChatGPT Business 可在 Notion、v0 等工具里「Sign in with ChatGPT」。Dots 可连接多台本地机器（Tibo / OpenAIDevs）。
- **MiniMax H3-Image**：官方称 4K / 约 1600 万像素、最多 16 张参考图、约 10 秒，并开放权重。HF `MiniMaxAI/MiniMax-H3-Image` 可访问，`lastModified` 约 11-11 15:10 Asia/Singapore。发布周 16MP+ 生成 50% off 为官方促销语。[帖](https://x.com/MiniMax_AI/status/2120179737695826420)、[HF](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)
- **Qwen4**：@Alibaba_Qwen 11-11 10:01 Asia/Singapore 称「Qwen4 is coming」，**Qwen4-Max** 已在阿里 Token Plan 预览，并可在 QwenWork / Qoder / Qwen APP / QwenStudio 提前试用。尚未见完整技术报告，不作已全面开源理解。[帖](https://x.com/Alibaba_Qwen/status/2120335993643684315)、[Token Plan](https://qwencloud.com/pricing/token-plan)
- **Gemini Robotics 2.5**：@GoogleDeepMind 11-10 23:00 Asia/Singapore，称可学数百种日常技能（折叠衣物、分拣零件等），官方自报，未单列主条。[帖](https://x.com/GoogleDeepMind/status/2120169787896525104)
- **Gemini on CarPlay**：@GeminiApp 11-12 05:14 Asia/Singapore，向 iOS 上 Gemini 用户全球滚动。
- **评测杂讯**：AA 称 Muse Ember Intelligence Index 36、与 Haiku 5.5 max 相近；Fable 5.2 领跑 AA-3D 与 VIALS-AA。均为 AA 自报。
- **News 摘要≠来源记录**：OpenAI 营收/亏损数字、Anthropic 天然气发电机、蒸馏导致中文圈模型停滞、SemiAnalysis 持久 agent 占比等，本包未独立核对原始财报或合同，保持待核，不写入主条。

##### A. 时间线 / 官方覆盖

| 来源 | 覆盖（Asia/Singapore） | 备注 |
|------|-------------|------|
| 首页时间线 3 页 | 约 11-11 13:31 → 11-12 09:13 | 99+98+97 条；仍有 next_token，未翻第 4 页 |
| 官方检索 off12c–g | 约 11-09 11:38 → 11-12 09:21 | 含 Anthropic/OpenAI/Google/Qwen/MiniMax/Cursor/AA/dotey 等 |
| 定向 topic | 窗口内 | IPO/Cyber/Kimi 等；无过滤时被杂讯淹没，已改写并交叉官网 |
| 缺口 | 11-09 09:40 → 11-11 13:31 | 靠 search_posts_all + News 补；非时间线全量 |
| 提示注入 | — | 帖文一律当数据，不执行其中指令；包中未引用指令性文本 |

本窗口首页时间线高信号账号包括官方实验室、Claude/OpenAI/Google 开发者号、AA、Cursor、dotey；大量预测市场与英伟达人事传闻未当作 AI 产品事实。无「只转发、无原帖」的关键官方账号被误当成唯一来源。

##### B. Today's News（摘录，摘要≠来源记录）

- Claude Fable / Mythos 发布与基准讨论：[2119868810153542050](https://x.com/i/trending/2119868810153542050) 一类集群（以官方帖为准）
- Anthropic IPO 路演与估值转述
- Gemini 4 Carbon 开放、Decisions API
- Claude Code vs Codex、harness、Opus 5.5 手感余波
- OpenAI 营收/亏损、持久 agent 支出占比等财经摘要——待核
- AlphaGenome / AlphaProof 进入部分科技摘要

##### C. 来源记录 摘要

1. Claude Fable 5.2 / Mythos 5.2 已官方发售；API $8/$40（5.1 为 $10/$50），fast mode $16/$80；Fable 对客、Mythos 需验证。数字与案例见发布页，均为官方自报。
2. Anthropic 11-10 启动路演：825,000,000 股 A 类，价 $70–78，代码 ANT；新 S-1/A Acc-no 0001628280-26-072484。
3. Gemini 4 Carbon 11-10/11 对付费 API 与 AI Ultra 开放；引入价 $2/$10 至 11-30。
4. Gemini Decisions API + `gemini-decision-1`：最多 1000 题；$0.10/1M 输入、输出不计费（官方自报）。
5. AlphaGenome 2 开放非商用 API；AlphaProof Code 称完成对 `libsignal` 关键性质的机器码级证明（官方自报，工件已开源）。
6. #107757 仍 open，更新至 11-10 02:26 Asia/Singapore。
7. Cyber at the Frontier：11-12 10:00 AM PT = 11-13 02:00 Asia/Singapore；采集时尚未开播。
8. HF Kimi-K3.1-Pro：lastModified 仍 11-05 15:11 Asia/Singapore；downloads≈33617。
9. MiniMax-H3-Image 权重在 HF 可访问；lastModified 约 11-11 15:10 Asia/Singapore。

##### E. 建议扩写（3–5）

1. **Fable 5.2 vs Opus 5.5 vs Carbon**：用官方成本-准确率图和 AA Index，写清「日常用 Opus/Argon、难任务再上 Fable/Carbon」，并标明努力档与护栏差异。
2. **IPO 文件精读**：把 $70–78、8.25 亿股、超额配售与招股书总股本做成一张表，避免把发行规模写成市值。
3. **Decisions API**：拆三种题型与「输出 token 为 0」的计费，设想在路由/护栏里的真实时延。
4. **AlphaProof × Signal**：讲清「人写规范、agent 出证明、Lean 检查、未覆盖整个 App」这条边界，对比上期 1024-bit RSA 压测。
5. **额度与重置**：并列 Claude 全模型免费 reset 截止时间、Fable 发布周促销，以及 OpenAI 侧尚无新公式——给订阅用户一份可执行对照。


## GitHub 项目与发行

### 项目原始材料

#### GitHub 三日刊（2026-11-09 → 2026-11-12）

1. **Hugging Face Datasets 5.2.0**
`huggingface/datasets` 于 11-10 05:40（Asia/Singapore）发布正式版 5.2.0（`prerelease=false`），距 5.1.0 一个小版本。功能上，面向 image/audio/video 等「文件夹数据集」做了更快的流式解码，3D Mesh feature / meshfolder 开始接受 `.gltf`。更需要立刻升级的是安全项：移除了对 pickle 版 pandas DataFrame 的加载，发布说明点名 CVE-2026-57845。此外还修了 `push_to_hub` 在进程数超过分片数时丢行、以及 `concatenate_datasets` 在按节点切分后每个 rank 拿到全量数据等问题。做多模态数据管道、或生产环境仍可能读到旧式 pickle 缓存的人应先看这条，不要把它当成新数据集托管平台发布。
证据：[5.2.0 Release](https://github.com/huggingface/datasets/releases/tag/5.2.0) · [huggingface/datasets](https://github.com/huggingface/datasets)

2. **Ollama v0.40.16：引入 Ripple Preview**
Ollama 于 11-10 02:21（Asia/Singapore）发布正式版 v0.40.16（`prerelease=false`；同窗口的 v0.40.17-rc0 为预发布，未收）。主菜是库里新增 [Ripple Preview](https://ollama.com/library/ripple-preview)：Ricursive Intelligence 的 65B 稠密模型，面向 agentic coding，用 `ollama run ripple-preview` 即可拉起。其余变更包括：发布说明称 Qwen3.8 Flash Next 在 Apple silicon 上约少占 27 GiB 内存（标「自称」）；`/v1/responses` 开始遵守 `truncation`，默认不再静默截断；`/v1/models` 在未安装模型时返回空列表而非 `null`；并加上 Windows on ARM 的 CUDA 13.5。在本机试用新编码模型、或对接 OpenAI 兼容 Responses 接口的人可以升；v0.40.17 仍是 rc，先别当稳定通道。
证据：[v0.40.16 Release](https://github.com/ollama/ollama/releases/tag/v0.40.16) · [Ripple Preview 模型页](https://ollama.com/library/ripple-preview)

3. **MiniMax-H3-Image 开源权重，ComfyUI v0.45.0 同步接入**
官方组织 `MiniMax-AI` 于 11-10 01:11（Asia/Singapore）新建本仓，站点 [minimax.io](https://www.minimax.io) / [platform.minimax.io](https://platform.minimax.io) 与 Hugging Face [MiniMaxAI/MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image) 可交叉核实。截至 11-12 09:21（Asia/Singapore）GitHub 约 **207 星（总量）**，仓内主要是文档、技能与示例，权重在 HF。项目自称：文生图与最多 16 张参考图的编辑共用一个检查点，可直接出约 16MP、默认 6 步、不必再接放大器；DiT 权重 BF16 约 68.65 GB，另需 MiniMax-H3 的 text encoder 约 66.7 GB，本地原版检查点加编码器约 135 GB，HF 整库约 204 GB（规格与体积均来自 README，标「自称」）。协议是社区许可证，不是 Apache。同窗口 ComfyUI 于 11-11 05:42（Asia/Singapore）发布正式版 v0.45.0（`prerelease=false`），除接入 MiniMax-H3-Image 外，还为 Qwen 3.x 增加视频输入、支持 RelayVSR / WeVisOne-VL / UltraTex，并加入 Pika H3、Kling 4.0 Flash、Seedream 5.5、GPT Image V3（含 GIF/SVG）等合作方节点。要在本地或工作流里试 4K 开源图模型的人，可把权重页和 Comfy 模板一起看；先读许可证再商用。
证据：[MiniMax-AI/MiniMax-H3-Image](https://github.com/MiniMax-AI/MiniMax-H3-Image) · [HF 权重](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image) · [ComfyUI v0.45.0](https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.45.0)

4. **LangChain 1.5.0 / langchain-core 1.8.0：最低 Python 升至 3.11**
`langchain-ai/langchain` 于 11-11 23:22–23:47（Asia/Singapore）连续发布正式版 langchain-core 1.8.0 与 langchain 1.5.0（均为 `prerelease=false`）。这是一次明确的破坏性切割：两个包都去掉已结束生命周期的 Python 3.10，最低改为 3.11；仍留在 3.10 上的环境会继续解析到 1.7.x / 1.4.x。1.5.0 还加入 model router 与 auto mode middleware（其中 `ModelRouterMiddleware` 被标为 beta），core 1.8.0 增加 decision models。还在 3.10 上跑生产、或要用新路由中间件的团队应先核运行时再升，不要把它看成一次无痛补丁。
证据：[langchain 1.5.0](https://github.com/langchain-ai/langchain/releases/tag/langchain%3D%3D1.5.0) · [langchain-core 1.8.0](https://github.com/langchain-ai/langchain/releases/tag/langchain-core%3D%3D1.8.0)

5. **HybridRobotics/supermimic**
UC Berkeley Hybrid Robotics 实验室官方组织于 11-10 18:46（Asia/Singapore）公开本仓，Apache-2.0，项目页 [supermimic.github.io](https://supermimic.github.io) 与论文 [arXiv:2610.28480](https://arxiv.org/abs/2610.28480) 可反链；截至 11-12 09:21（Asia/Singapore）约 **1,031 星（总量）**，根目录有训练/回放脚本，提交与 README 相符。思路是用一个可微分世界模型做人形全身运动跟踪，策略在真机 Unitree G1 上演示。项目页自称：1 张 H100 训练约 3 小时即可超过 SONIC 已发布检查点的归一化回报（SONIC 为 128 张 L40、7 天、约 21,000 GPU-hours），在 129,514 条动作上 SONIC 失败 179 条、SuperMimic 双卡 9.8 小时失败 0 条；并写明这是训练覆盖率而非泛化、两边数据与硬件并不对等（标「自称」）。做人形控制或世界模型的人值得读论文和项目页上的比较口径，不要直接把「>1000× GPU-hours」当成可复现的绝对结论。
证据：[HybridRobotics/supermimic](https://github.com/HybridRobotics/supermimic) · [项目页](https://supermimic.github.io) · [arXiv:2610.28480](https://arxiv.org/abs/2610.28480)

6. **Anthropic SDK：目录加入 Fable 5.2 / Mythos 5.2 标识**
官方 Python SDK 于 11-10 02:52（Asia/Singapore）发布正式版 v2.7.0，TypeScript 同步 `sdk-v1.7.0`（均为 `prerelease=false`）。changelog 写的是 **api：add `claude-fable-5-2` and `claude-mythos-5-2`**，这是 SDK / API 类型目录里的模型标识，本期未见单独的模型发布页或评测包，不能写成「两个新模型已正式开源发布」。v2.8.0（11-11 00:32 Asia/Singapore）则主要是分析报表与 Slack 相关字段，以及各云适配层的路径校验。已经在用 Anthropic API 的开发者可以升 SDK 以识别新 model ID；是否对你的账号开放，仍要以官方模型文档和后台为准。
证据：[Python v2.7.0](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.7.0) · [TypeScript sdk-v1.7.0](https://github.com/anthropics/anthropic-sdk-typescript/releases/tag/sdk-v1.7.0)

7. **openai/codex-security npm v0.9.1**
官方组织 `openai` 的安全扫描 CLI / TypeScript SDK（文档站 [developers.openai.com/codex/security](https://developers.openai.com/codex/security)）于 11-10 09:09（Asia/Singapore）发布正式版 `npm-v0.9.1`（`prerelease=false`）；`npm-v0.9.0` 因 macOS 签名中断未上 npm，官方指向 0.9.1。新进展包括 Deep Scan（分批独立审查、交叉核对证据并按同一修复归并发现），以及默认打开外部扫描器导入；npm 包还带有 Developer ID 签名的 macOS native addon。日榜同时出现约 **52 stars today**，总量约 **11,748**（抓取 2026-11-12 09:21 Asia/Singapore），但收录理由是窗口内正式发版，不是这 52 的日榜数字。把编码助手接入安全扫描或要在 CI 里跑审查的团队可以看 0.9.1 与 Action `action-v0.9.1`。
证据：[npm-v0.9.1 Release](https://github.com/openai/codex-security/releases/tag/npm-v0.9.1) · [openai/codex-security](https://github.com/openai/codex-security) · [官方文档](https://developers.openai.com/codex/security)

（热榜口径：日榜约为最近 24 小时，周榜统计最近七天，均于 2026-11-12 09:21 Asia/Singapore 抓取，不可当作本期 72h 净增。日榜首位 meta/astryx 约 2,776 stars today，上期已报 v0.7.9–v0.7.11，本期只是留榜。周榜 NVIDIA/auto-ontology、vercel-labs/agent-desktop、agent-browser 等同样是持续在榜或窗口内无新正式 Release，不重复。新仓搜索前列多为 iOS 改机工具与「预激活安装包」，以及明确带 PoC/提权描述的仓库，一律未收。`ranxianglei/billion-context` 本期仍无新的可交叉核验进展，继续不收录。）

窗口内无：vllm-project/vllm、sgl-project/sglang、ggml-org/llama.cpp（仅有 `b12xxx` 且 `prerelease=true` 的日构建，未收）、huggingface/transformers、pytorch/pytorch、modelcontextprotocol/python-sdk、modelcontextprotocol/typescript-sdk、axolotl-ai-cloud/axolotl、langchain-ai/langgraph（常规 / 预发布未收录：ollama v0.40.17-rc0；openai/codex 正式补丁 rust-v0.167.1 / 0.167.2 仅含 Vertex 上增量 tool 更新等，另有多枚 `*-alpha.*`；openai-python v3.48.0 / v3.49.0 与 openai-node v7.54.0 / v7.55.0 为 agent session 流式选项、typed async function tools，以及把已出现过的 `gpt-6-rosalind` 纳入 beta Responses 识别；Anthropic v2.8.0 及 TS sdk-v1.8.0、各云 SDK 子包；unsloth v0.1.917-beta；langchain 1.4.10 / langchain-core 1.7.7 / langchain-typesafe 0.1.0 / langchain-fireworks 1.7.3）


## 模型与数据集

### 模型、数据与榜单原始材料

#### HF / 模型三日雷达素材 · 2026-11-12

- 窗口：2026-11-09 09:40 Asia/Singapore（01:40 UTC）→ 2026-11-12 约 09:29 Asia/Singapore（01:29 UTC，实际采集时刻）。不是从 11/10 10:11 的发布时间算起。
- 去重基线：11/09 素材包（内部证据存档），sha256 1409676c…5a）以及 （内部证据存档） 里的榜单快照。上一期已经写过的条目只在有新事实时才写，并标为“更新”。
- 计数：主条 4｜次条 6（另有 2 条窗口前发布、被漏掉的补记）｜榜单 6 段｜数据集 4 条主条 + 2 条附记｜冒名/同名镜像 1 组（6 个 repo）。
- 数据口径：likes/downloads 统一取 HF API 在 2026-11-12 09:28–09:29 Asia/Singapore（01:28–01:29 UTC）的快照（采集证据快照）。downloads 是 HF 的近 30 天口径。Trending 取 09:21 Asia/Singapore 的 API 和网页，两者前 30 名一致（29/30）。
- 开放程度用语：“开放权重”= 权重能下载；“OSI 许可”= 权重许可证属于 OSI 认可的许可证（Apache-2.0/MIT），未逐项核对 OSAID；“自定义/非商用许可”= 权重开放，但不算开源。

##### 三句话结论

1. **MiniMax-H3-Image 是本窗口真正的新开放权重。** 33.1B DiT 的文生图/编辑模型，2026-11-10 22:50 Asia/Singapore 首次推送权重，HF Trending 排第 2。AA 图像榜同步上榜：t2i #23 / 编辑 #11。但许可证明确把欧盟、英国、韩国、美国列为排除地区，不是开源。
2. **Kimi K3.1 Pro 的官方权重仍停在 11/05。** 窗口内的新动作是两件“外围”的事：NVIDIA 发布了官方 NVFP4 量化版（1.6TB，downloads 仍为 0）；LMArena 文本榜首次列入 Kimi K3.1 Pro（Max），排 #24。HF 上还出现了 5 个与官方逐字节一致的同名镜像。
3. **榜单面最大的变化来自闭源。** AA Intelligence v5 新收录 Claude Fable 5.2 (Max)，64.6 分，直接越过 Gemini 4 Carbon（60.0）成为 #1。开放权重的榜首仍是 Kimi K3.1 Pro（46.5）。

---

##### 主条

###### 1. MiniMaxAI/MiniMax-H3-Image（+ MiniMax-H3-Image-PE）· 新发布（开放权重，非开源）

MiniMax 把 H3 系列从视频扩展到图像，放出一个可以本地跑的 33.1B 文生图 + 编辑模型，配了一个 27B 的提示词扩写模型（PE）。热度很真实：两天内 HF Trending #2，社区量化/转格式 repo 超过 40 个。能否商用要先过许可证：EU/UK/韩国/美国被排除；年化营收超过 100 万美元或对外提供托管服务需要书面授权；产品里必须标注“MiniMax-H3-Image”；输出不得用于改进其他模型。所以它是“开放权重”，不是“开源”。

- 为什么重要：这是窗口内唯一一个同时满足三点的新模型：官方组织、完整大权重、一线厂商；并且 AA 图像榜已经同步收录（见 B4/B5）。这也是 H3 视频之后 MiniMax 在开放图像生成上的正式入场。
- 适合谁 / 阅读建议：做本地图像生成、ComfyUI 工作流、图像编辑的人值得试；单一格式的权重约 135GB（transformer 66.3GB + text_encoder 66.7GB + vae 2.3GB；repo 同时放了 diffusers 副本，总共 204GB），消费级显卡需要用量化版。在受限地区或面向海外的商用团队，先读 LICENSE 再动手。
- 来源记录：
  - HF 时间：createdAt 2026-11-03 06:34 UTC / 11-03 14:34 Asia/Singapore；lastModified 2026-11-11 07:10 UTC / 11-11 15:10 Asia/Singapore。repo 创建于 11/03，但 commit 历史里最早一条是 `7b6142f879`“MiniMax-H3-Image”，时间 2026-11-10 14:50 UTC / 22:50 Asia/Singapore，推测此前一直是私有仓库。diffusers 格式权重来自 `492fd8c4ec`，2026-11-10 16:21 UTC / 11-11 00:21 Asia/Singapore。11-11 00:30 UTC 有一次 LICENSE 改动 `fbde899fff`，经 diff 只是把授权申请链接换成 `/console/license`，条款没变。
  - 热度：likes 720 / downloads 142,989（采集 11-12 09:28 Asia/Singapore）；HF Trending #2（trendingScore 699，09:21 Asia/Singapore）。
  - 许可 / 任务：license other（minimax-h3-image-community-license-agreement），pipeline text-to-image。属于开放权重 + 自定义许可，不是 OSI 开源（条款见采集证据快照）。
  - 权重证据：siblings 中有 41 个 safetensors，合计约 204.0GB。transformer 12 分片 66.3GB，text_encoder 14 分片 66.7GB，vae 2.3GB；transformer_diffusers（12 分片 66.3GB）和 vae_diffusers 是同一权重的 diffusers 格式副本，实际独立权重约 135GB（子目录 tree 另行抓取，见 （采集证据快照）。
  - 官方身份：repo 属于 MiniMaxAI 官方组织；MiniMax 官方博客（2026-11-11）和 GitHub MiniMax-AI/MiniMax-H3-Image 都互链到这个 HF repo。
  - PE：MiniMaxAI/MiniMax-H3-Image-PE，createdAt 2026-11-08 15:35 UTC / 11-08 23:35 Asia/Singapore；lastModified 2026-11-10 15:16 UTC / 11-10 23:16 Asia/Singapore。init commit `5cb2132bb8` 时间 2026-11-10 14:38 UTC / 22:38 Asia/Singapore。卡片写明从 Qwen3.8-27B 微调，NVFP4，4 个分片 17.9GB。likes 53 / downloads 600（采集 11-12 09:28 Asia/Singapore）；许可相同（license other（minimax-h3-image-community-license-agreement），pipeline text-generation）。
  - 卡片/博客参数：33.1B DiT，最高 16MP 输出，蒸馏到 6 步。
- 待核：
  - “4K 单图 <10 秒”、“提示词遵循 SOTA”都是厂商自述，未独立复现。
  - AA 页面上的 “H3-Image” 条目 releaseDate 写的是 2026-07-31，可能是更早的 API 版本，和这次开放的 checkpoint 是否是同一个模型待核。
  - 社区 repo akhaliq/minimax-h3-image-pdmd-2step（likes 43 / downloads 2,774（采集 11-12 09:28 Asia/Singapore）把元数据标成 apache-2.0，与基座许可冲突，不能把它当成“Apache 版 H3”。
  - Comfy-Org/MiniMax-H3-Image 创建于 11-08 20:37 UTC，早于官方首推，下载量（likes 253 / downloads 351,803（采集 11-12 09:28 Asia/Singapore）高于官方 repo。说明分发的大头走的是 ComfyUI 渠道，HF 官方 repo 的下载数会低估实际使用。
- 证据：
  - [HF MiniMaxAI/MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)
  - [HF MiniMaxAI/MiniMax-H3-Image-PE](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image-PE)
  - [minimax.io 来源](https://www.minimax.io/blog/minimax-h3-image)
  - [GitHub MiniMax-AI/MiniMax-H3-Image](https://github.com/MiniMax-AI/MiniMax-H3-Image)
  - [docs.comfy.org 来源](https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image)
  - 社区衍生（只列有代表性的）：[HF Comfy-Org/MiniMax-H3-Image](https://huggingface.co/Comfy-Org/MiniMax-H3-Image) · [HF unsloth/MiniMax-H3-Image-FP8](https://huggingface.co/unsloth/MiniMax-H3-Image-FP8) · [HF Abiray/MiniMax-H3-Image-GGUF](https://huggingface.co/Abiray/MiniMax-H3-Image-GGUF)

###### 2. Kimi K3.1 Pro 跟进：NVIDIA 官方 NVFP4 量化 + LMArena 首次上榜 · 更新

上次素材里 Kimi K3.1 Pro 已经是开放权重的榜首。这三天官方 repo 没有新 checkpoint，变化在周边：NVIDIA 用自家组织发布了 Kimi-K3.1-Pro-NVFP4，给 Blackwell 部署铺路；LMArena 文本榜 11/9 那次刷新首次列出 Kimi K3.1 Pro（Max），1483±11，#24，只有 3,443 票，置信区间很宽。Kimi 官方博客仍写着权重“will be released by Nov 4”，没有补上 HF 链接，属于文案滞后，不代表权重未发布。

- 为什么重要：NVIDIA 官方量化说明这个 2.8T 级 MoE 已经进入主流推理栈的适配节奏；LMArena 给了第一份盲测人类偏好分（目前低于 Kimi K3 (Max) 的 #19，样本少，暂不下结论）。
- 适合谁 / 阅读建议：有 B200/GB200 集群、打算自托管 Kimi 的团队看 NVFP4 卡片里的精度对比；普通读者只要记住“官方权重没变，多了一个 NVIDIA 量化版”。
- 来源记录：
  - nvidia/Kimi-K3.1-Pro-NVFP4：createdAt 2026-11-11 00:57 UTC / 11-11 08:57 Asia/Singapore；lastModified 2026-11-11 06:16 UTC / 11-11 14:16 Asia/Singapore。权重 commit `546b174b3d`“R3: NVFP4 routed experts, MXFP8 shared experts + KDA, BF16 rest”，时间 2026-11-11 04:13 UTC / 12:13 Asia/Singapore。siblings 有 96 个 safetensors，合计约 1,605GB。likes 4 / downloads 0（采集 11-12 09:28 Asia/Singapore）。许可 license other（nvidia-open-model-agreement），pipeline image-text-to-text：NVIDIA Open Model Agreement，同时须遵守 Kimi K3.1 Pro License，不是 OSI。卡片写 HF 发布日期为 11/10/2026。
  - 官方身份：repo 属于 nvidia 官方组织；卡片链接到 moonshotai/Kimi-K3.1-Pro 和 NVIDIA Model-Optimizer。
  - moonshotai/Kimi-K3.1-Pro：createdAt 2026-11-02 04:13 UTC / 11-02 12:13 Asia/Singapore；lastModified 2026-11-05 07:11 UTC / 11-05 15:11 Asia/Singapore，窗口内没有 commit。likes 1,935 / downloads 33,617（采集 11-12 09:28 Asia/Singapore）；HF Trending #6（trendingScore 394）。siblings 有 96 个 safetensors，repo 合计约 1,561GB。license other（kimi-k3.1-pro），pipeline image-text-to-text。
  - LMArena 文本榜（WebFetch，11-12 约 09:40 Asia/Singapore）：数据日期 Nov 9，总票数 9,105,428，421 个模型。Kimi K3.1 Pro (Max) 排 #24，1483±11，3,443 票，许可列写“Kimi K3.1 Pro License”。11/09 那期看到的 Nov 8 版本共 420 行，没有它。LMArena vision 榜（167 行）里仍然没有。
  - AA：Kimi K3.1 Pro 仍是 46.5，开放权重 #1（v5 口径），标注“Commercial Use Restricted”。
- 待核：
  - NVFP4 卡片自报的 MXFP4 → NVFP4 精度：GPQA 93.97→93.84、AA-LCR 81.69→82.06、IFBench 73.40→73.40、MMMU Pro 81.68→81.79、SciCode 59.52→59.47、TB2.1 88.20→87.78。都是 NVIDIA 自测，未复现。
  - NVFP4 版总体积（1,605GB）反而略大于官方原版（1,561GB），合理的解释是 shared experts 用 MXFP8、MLA 保留 BF16，待核。
  - LMArena 的 rank spread 是 9–50，“#24”不稳定。
- 第三方和衍生（降权）：
  - audnai/penclaw-Kimi-K3.1-pro-unrestricted：likes 215 / downloads 339（采集 11-12 09:28 Asia/Singapore），manual gated，lastModified 11-10 04:23 UTC / 12:23 Asia/Singapore。仍是第三方 repo，README 返回 401，未绕过查看。
  - fulcrumresearch/echo：基于 Kimi-K3（不是 K3.1）的 MIT LoRA，likes 28 / downloads 0（采集 11-12 09:28 Asia/Singapore）。
- 证据：
  - [HF nvidia/Kimi-K3.1-Pro-NVFP4](https://huggingface.co/nvidia/Kimi-K3.1-Pro-NVFP4)
  - [HF moonshotai/Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)
  - [lmarena.ai 来源](https://lmarena.ai/leaderboard/text)
  - [artificialanalysis.ai 来源](https://artificialanalysis.ai/models/kimi-k3-1-pro)
  - [kimi.ai 来源](https://www.kimi.ai/blog/kimi-k3-1-pro)
  - 本地：（采集证据快照），（采集证据快照）（可见文本与 11/09 版本一致）

###### 3. Zyphra/ZONOS3-Mini · 新发布（开放权重，Apache-2.0）

Zyphra 发布的 ZONOS3-Mini 是一个 43 种语言的 TTS 模型，100M 激活 / 800M 总参数的 MoE。Apache-2.0，自带 GGUF 和浏览器（web）版本，可以本地甚至端侧运行。它是本窗口里许可最宽松、最容易直接用上的新模型。

- 为什么重要：在开放 TTS 里同时做到多语言、MoE 低激活和宽松许可的不多。官方宣称在 MacBook Air M3 上首包音频延迟 <150ms，如果属实，就是实时语音代理可以直接拿来用的底座。
- 适合谁 / 阅读建议：做语音助手、配音、本地 TTS 的开发者；先看 gguf/ 和 web/ 两个入口。注意 repo 里有 `.pt` 文件（pickle 格式），加载前看清来源。
- 来源记录：
  - HF 时间：createdAt 2026-11-09 05:03 UTC / 11-09 13:03 Asia/Singapore；lastModified 2026-11-11 23:53 UTC / 11-12 07:53 Asia/Singapore。主权重 commit `d78708d603`“Zonos 3 Mini”，时间 2026-11-09 22:01 UTC / 11-10 06:01 Asia/Singapore（repo 创建于窗口内的 11-09 13:03 Asia/Singapore）。gguf/ 目录在 2026-11-11 23:53 UTC / 11-12 07:53 Asia/Singapore 又有更新。
  - 热度：likes 174 / downloads 4,170（采集 11-12 09:28 Asia/Singapore）；HF Trending #28。
  - 许可 / 任务：license apache-2.0，pipeline text-to-speech。开放权重，OSI 许可。
  - 权重证据：autoencoder/generator.pt 7.96GB，heads/full_mr 4.01GB，teacher/model.safetensors 0.77GB，另有 10 个 GGUF（backbone-ptq 等）和 web/ 分片。repo 合计约 30.7GB。
  - 官方身份：repo 属于 Zyphra 官方组织；官方博客 zyphra.com/our-work/zonos3-mini（Nov 9）和 GitHub Zyphra/ZONOS3-Mini 互链。
  - 同系列：Zyphra/ZONOS3-Mini-hf（transformers 格式），createdAt 2026-11-11 18:04 UTC / 11-12 02:04 Asia/Singapore；lastModified 2026-11-11 18:04 UTC / 11-12 02:04 Asia/Singapore，likes 1 / downloads 0（采集 11-12 09:28 Asia/Singapore）。Zyphra/ZAC-1 音频编解码器，createdAt 2026-11-12 00:25 UTC / 11-12 08:25 Asia/Singapore；lastModified 2026-11-12 00:26 UTC / 11-12 08:26 Asia/Singapore，likes 2 / downloads 0（采集 11-12 09:28 Asia/Singapore），license apache-2.0，pipeline 未填写，卡片称权重来自 ZONOS3 的 autoencoder 重新打包。社区 MLX 版：mlx-community/ZONOS3-Mini。
- 待核：
  - “在自家 ZTTS2-Eval 上开放模型第一”是自建评测上的自报结果。
  - “TTFA <150ms（M3 MacBook Air）”是厂商数字。
  - 官方尚未发技术报告（卡片 commit 原话：“no technical report yet”）。
- 证据：
  - [HF Zyphra/ZONOS3-Mini](https://huggingface.co/Zyphra/ZONOS3-Mini)
  - [zyphra.com 来源](https://www.zyphra.com/our-work/zonos3-mini)
  - [GitHub Zyphra/ZONOS3-Mini](https://github.com/Zyphra/ZONOS3-Mini)
  - [HF Zyphra/ZAC-1](https://huggingface.co/Zyphra/ZAC-1)

###### 4. nex-agi/Nex-N2.6 · 新发布（开放权重，Apache-2.0，0 下载）

Nex-AGI 在 GLM-5.3-Flash 上继续做 agent 后训练，发布 Nex-N2.6（FP8，约 328GB 权重）。主打两点：减少推理中的重复（自报重复率从 16.0% 降到 1.6%）和电脑操作（自报 OSWorld 83.0）。这个组织之前发过 N2/N2.5 系列，是正常发版；但 HF 下载数还是 0，实际热度主要在 OpenRouter 那边。

- 为什么重要：开放权重里专门针对 computer-use 和长程工具调用做优化的模型不多。如果 OSWorld 83.0 能被独立复现，它会是开放阵营的 agent 头部之一。
- 适合谁 / 阅读建议：做 computer-use agent 和长程工具链的团队可以试 OpenRouter 上的版本；自托管需要多卡 FP8 环境（按 GLM-5.3-Flash 的 SGLang 部署指南）。
- 来源记录：
  - HF 时间：createdAt 2026-11-10 05:34 UTC / 11-10 13:34 Asia/Singapore；lastModified 2026-11-11 15:03 UTC / 11-11 23:03 Asia/Singapore。权重分三次 upload-large-folder commit，最后一次 `07f8862f6a` 在 2026-11-10 07:14 UTC / 15:14 Asia/Singapore（第一次 `b421f93554` 在 07:13 UTC）。之后是 README、资源文件和 pipeline 配置改动。
  - 热度：likes 41 / downloads 0（采集 11-12 09:28 Asia/Singapore）。
  - 许可 / 任务：license apache-2.0，pipeline image-text-to-text。开放权重，OSI 许可；基座 zai-org/GLM-5.3-Flash-BF16 是 MIT。
  - 权重证据：siblings 中有 129 个 safetensors，合计约 328.3GB（FP8）。
  - 官方身份：repo 属于 nex-agi 组织，上一代是 nex-agi/Nex-N2.5-Pro。卡片链接 GitHub sii-nex/Nex-N2.6 和 OpenRouter 的 nex-agi/nex-n2.6。
- 待核：
  - OSWorld 83.0（N2.5-Pro 82.2、GLM-5.3-Flash 78.0）、重复率 16.0%→1.6% 都来自团队自测；卡片自己也写明“Scores depend on the evaluation harness”。
  - 参数量官方没有在卡片显式写出，“约 321B”是按权重体积推算。
- 证据：
  - [HF nex-agi/Nex-N2.6](https://huggingface.co/nex-agi/Nex-N2.6)
  - [GitHub sii-nex/Nex-N2.6](https://github.com/sii-nex/Nex-N2.6)
  - [openrouter.ai 来源](https://openrouter.ai/nex-agi/nex-n2.6)

---

##### 次条（新发布，信号弱或场景窄）

- **speridlabs/iris-z**：深度估计，两个版本 Iris-Z-big 32.2B / Iris-Z-small 9.1B。createdAt 2026-11-04 20:50 UTC / 11-05 04:50 Asia/Singapore；lastModified 2026-11-11 18:37 UTC / 11-12 02:37 Asia/Singapore；首个也是唯一的权重 commit `39cf884b84` 在 2026-11-11 18:20 UTC / 11-12 02:20 Asia/Singapore；20 个 safetensors，82.55GB。likes 15 / downloads 0（采集 11-12 09:28 Asia/Singapore）；license other（flux-non-commercial-license），pipeline depth-estimation，非商用。“超过专用深度模型”属自报，待核。同组织的 speridlabs/idol 是图生 3D，排 Trending #3，属于上期延续的热度。[HF speridlabs/iris-z](https://huggingface.co/speridlabs/iris-z)
- **inclusionAI/ZoomGain-4B / ZoomGain-9B**：多模态“放大看图”推理模型。9B 的权重 commit `bf82de97fe` 在 2026-11-10 11:46 UTC / 19:46 Asia/Singapore。likes 5 / downloads 6（采集 11-12 09:28 Asia/Singapore）（9B）。没有填许可证（license 未填写，pipeline 未填写），所以用途受限、待核。论文 [arXiv 2611.14076](https://arxiv.org/abs/2611.14076) 。[HF inclusionAI/ZoomGain-9B](https://huggingface.co/inclusionAI/ZoomGain-9B)
- **MinimaLabs/KLM-1.6**：99M 参数的小型基座模型，Apache-2.0。createdAt 2026-11-09 10:00 UTC / 11-09 18:00 Asia/Singapore；lastModified 2026-11-09 10:21 UTC / 11-09 18:21 Asia/Singapore；卡片和代码 commit `09b9991211` 在 2026-11-09 10:01 UTC / 18:01 Asia/Singapore。likes 50 / downloads 666（采集 11-12 09:28 Asia/Singapore）。自报在 Open SLM 榜同级第一，待核。[HF MinimaLabs/KLM-1.6](https://huggingface.co/MinimaLabs/KLM-1.6)
- **Efficient-Large-Model/Open-H3-Regenerate-2K-IC**（NVlabs Sana 团队）：给 MiniMax-H3 视频草稿做 1080P/2K/4K 再生成的 IC-LoRA。createdAt 2026-11-09 01:50 UTC / 11-09 09:50 Asia/Singapore；lastModified 2026-11-09 02:17 UTC / 11-09 10:17 Asia/Singapore；权重 commit `54a7104b20` 在 2026-11-09 02:17 UTC / 10:17 Asia/Singapore。likes 64 / downloads 21,181（采集 11-12 09:28 Asia/Singapore）；license other（minimax-h3-community），pipeline video-to-video，沿用 MiniMax-H3 许可，非 OSI。注意：10/30 那期写过的是另一个 Open-H3 变体，不是这一个。[HF Efficient-Large-Model/Open-H3-Regenerate-2K-IC](https://huggingface.co/Efficient-Large-Model/Open-H3-Regenerate-2K-IC)
- **KRAFTON/Raon-1-nano-gguf / -mlx**：KRAFTON 官方发的端侧量化版（带 MTP），createdAt 2026-11-10 10:12 UTC / 11-10 18:12 Asia/Singapore；lastModified 2026-11-11 12:18 UTC / 11-11 20:18 Asia/Singapore。likes 15 / downloads 148（采集 11-12 09:28 Asia/Singapore）（gguf）；license apache-2.0，pipeline text-generation。原模型 10/29 已经发布，这次只是格式扩展。[HF KRAFTON/Raon-1-nano-gguf](https://huggingface.co/KRAFTON/Raon-1-nano-gguf)
- **inclusionAI/SingVL_S1_4B**：基于 Qwen3.5 的多模态“决策打分”模型（Choice / Noul / Score）。createdAt 2026-11-11 03:58 UTC / 11-11 11:58 Asia/Singapore；lastModified 2026-11-11 05:38 UTC / 11-11 13:38 Asia/Singapore；likes 3 / downloads 17（采集 11-12 09:28 Asia/Singapore）；没有填许可证。卡片里的 Public Decision Index 是自报，待核。[HF inclusionAI/SingVL_S1_4B](https://huggingface.co/inclusionAI/SingVL_S1_4B)

###### 补记：窗口前发布、往期漏掉的（不算本期新发）

- **meituan-longcat/LongCat-2.5**：1.78T MoE，MIT，开放权重 + OSI 许可。createdAt 2026-11-04 11:48 UTC / 11-04 19:48 Asia/Singapore；lastModified 2026-11-10 07:28 UTC / 11-10 15:28 Asia/Singapore；权重分片上传集中在 11-04 至 11-05 UTC（例如 `ce55920fc0` 在 11-05 02:48 UTC），窗口内只有卡片和文档 commit（11-09 11:38、11-10 07:28 UTC）。210 个 safetensors，约 3,562GB。likes 144 / downloads 490（采集 11-12 09:28 Asia/Singapore）。[HF meituan-longcat/LongCat-2.5](https://huggingface.co/meituan-longcat/LongCat-2.5)
- **pfnet/plamo-3-8b-fin-instruct**：金融领域日语 8B 模型。createdAt 2026-11-08 13:51 UTC / 11-08 21:51 Asia/Singapore；lastModified 2026-11-10 03:24 UTC / 11-10 11:24 Asia/Singapore；权重在 11-08 13:57 UTC，早于窗口。likes 9 / downloads 758（采集 11-12 09:28 Asia/Singapore）；license other（plamo-community-license），pipeline text-generation。[HF pfnet/plamo-3-8b-fin-instruct](https://huggingface.co/pfnet/plamo-3-8b-fin-instruct)

---

##### 数据集

- **D1. google/multimodal-knowledge-agent（MKA）**：Google DeepMind 的多模态知识型 agent 评测。createdAt 2026-11-09 13:42 UTC / 11-09 21:42 Asia/Singapore；lastModified 2026-11-10 10:02 UTC / 11-10 18:02 Asia/Singapore；唯一的 commit `46bce7ab87`“Initial commit: MKA-Hero-10 showcase tasks”，2026-11-10 10:02 UTC / 18:02 Asia/Singapore。likes 17 / downloads 832（采集 11-12 09:28 Asia/Singapore）；license apache-2.0，pipeline 未填写。HF 上只公开了 10 个示例任务，完整基准是 200 个私有任务。AA 同日（Nov 10）发文并给出首批分数：Claude Fable 5.2 Climb WSR 57%、Gemini 4 Carbon 54%、Claude Opus 5.5 53%（AA 口径，待核）。[HF google/multimodal-knowledge-agent](https://huggingface.co/datasets/google/multimodal-knowledge-agent) · [artificialanalysis.ai 来源](https://artificialanalysis.ai/articles/google-deepmind-multimodal-knowledge-agent)
- **D2. nvidia/Nemotron-Personas-Finance-Japan**：日本金融场景的合成人设数据集。createdAt 2026-11-04 04:37 UTC / 11-04 12:37 Asia/Singapore；lastModified 2026-11-09 07:05 UTC / 11-09 15:05 Asia/Singapore；唯一的 commit“Initial release”`c73cc86565` 在 2026-11-09 07:05 UTC / 15:05 Asia/Singapore，落在窗口内，repo 创建于 11/04。likes 17 / downloads 1,732（采集 11-12 09:28 Asia/Singapore）；license cc-by-4.0，pipeline 未填写；parquet 约 1.39GB。[HF nvidia/Nemotron-Personas-Finance-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Finance-Japan)
- **D3. inclusionAI/ZoomGainBench + ZoomGain-RL-Data**：和 ZoomGain 模型配套的评测集与 RL 数据。Bench：createdAt 2026-11-10 11:55 UTC / 11-10 19:55 Asia/Singapore；lastModified 2026-11-11 07:47 UTC / 11-11 15:47 Asia/Singapore；likes 0 / downloads 14（采集 11-12 09:28 Asia/Singapore）。RL-Data：likes 1 / downloads 12（采集 11-12 09:28 Asia/Singapore）。都没有填许可证，用途待核。[HF inclusionAI/ZoomGainBench](https://huggingface.co/datasets/inclusionAI/ZoomGainBench) · [HF inclusionAI/ZoomGain-RL-Data](https://huggingface.co/datasets/inclusionAI/ZoomGain-RL-Data)
- **D4. figma-ai/motion-graphics-bench**：Figma / Stanford 的动效图形生成评测。createdAt 2026-10-02 07:08 UTC / 10-02 15:08 Asia/Singapore；lastModified 2026-11-10 05:01 UTC / 11-10 13:01 Asia/Singapore；repo 创建于 10/02，但唯一的 commit `89592d63cf`“Initial commit”在 2026-11-10 05:01 UTC / 13:01 Asia/Singapore，实际公开时间待核。likes 9 / downloads 532（采集 11-12 09:28 Asia/Singapore）；license cc-by-nc-sa-4.0，pipeline 未填写，非商用。[HF figma-ai/motion-graphics-bench](https://huggingface.co/datasets/figma-ai/motion-graphics-bench)
- 附记：
  - arc4g/arc-art：154 件 Blender 艺术作品，createdAt 2026-11-09 18:49 UTC / 11-10 02:49 Asia/Singapore；lastModified 2026-11-10 00:21 UTC / 11-10 08:21 Asia/Singapore；likes 35 / downloads 1,758（采集 11-12 09:28 Asia/Singapore）；license cc-by-nc-4.0，pipeline 未填写。[HF arc4g/arc-art](https://huggingface.co/datasets/arc4g/arc-art)
  - Angais/pixel-art-atlas-1.4m：数据集 Trending #1，但创建于 11-06，属于上期延续的热度（likes 382 / downloads 41,578（采集 11-12 09:28 Asia/Singapore），license cc0-1.0，pipeline 未填写）。[HF Angais/pixel-art-atlas-1.4m](https://huggingface.co/datasets/Angais/pixel-art-atlas-1.4m)

---

##### 榜单

- **B1. LMArena 文本**（WebFetch；curl 返回 301/403，WebFetch 能读到全表）：数据日期 Nov 8 → **Nov 9**；总票数 9,091,367 → 9,105,428；模型数 420 → 421。
  - #1 仍是 Gemini 4 Carbon (High)，1526±10，Preliminary（上期 1527）。
  - 唯一确认的新增行是 Kimi K3.1 Pro (Max)，#24，1483±11。Kimi K3 (Max) 仍在 #19。
  - 本地只保存了选摘行，没有保存全量增删名单，不推断其他变化。[lmarena.ai 来源](https://lmarena.ai/leaderboard/text)
- **B2. LMArena 视觉**：数据日期仍是 Nov 8，167 个模型。但总票数从 1,568,841 降到 1,567,670，多行的票数也有增有减，原因不明（可能是票数清洗），标为异常、待核。#1 Claude Fable 5 (High) 仍是 1309±7。[lmarena.ai 来源](https://lmarena.ai/leaderboard/vision)
- **B3. LMArena 文生图**：数据日期仍是 Nov 8，84 个模型。总票数从 6,880,326 降到 6,874,394，同样是异常、待核。#1 GPT-Image-2.5 Sunburst 1429±5（上期 1428）。MiniMax H3-Image 和 Seedream 5.5 都还没有上这个榜。[lmarena.ai 来源](https://lmarena.ai/leaderboard/text-to-image)
- **B4. AA 文生图**（新路径 /image/leaderboard/text-to-image）：按本期解析器计，107 → 111 行。11/09 那期写的是 108 行，口径差 1 行，见“口径”一节。新增 4 个：
  - Seedream 5.5（ByteDance Seed，发布于 11-09）#10，1135±13
  - H3-Image Highspeed #22，1072±15
  - H3-Image #23，1066±15
  - ADM 3 Cloud (Image)（Apple）#87，910

  榜首仍是 GPT Image 2.6 Sunburst，1261±14。[artificialanalysis.ai 来源](https://artificialanalysis.ai/image/leaderboard/text-to-image)
- **B5. AA 图像编辑**：78 → 82 行。新增：
  - Seedream 5.5 #6，1159±14
  - H3-Image #11，1141±16
  - H3-Image Highspeed #13，1133±16
  - ADM 3 Cloud #46，1040

  前 4 名置信区间重叠（#1 2.6 Sunburst 1209±13）。[artificialanalysis.ai 来源](https://artificialanalysis.ai/image/leaderboard/editing)
- **B6. AA Intelligence Index v5.0.1**（默认视图 28 个模型；v5 分数不能和 v4 比较）：
  - 新收录 **Claude Fable 5.2 (Max)**，发布于 2026-11-09，闭源，**64.6**，成为新 #1，超过 Gemini 4 Carbon 的 60.0。
  - 新收录 Muse Ember (Max)，发布于 11-09，闭源，36.0。
  - MiniMax-M3.1-Flash（29.1）和 Muse Spark Open（24.9）不再出现在默认视图里。这只表示默认不展示，不等于被删除。
  - 其余分数不变（Kimi K3.1 Pro 46.5、Hy4 34.6、Inkling 2 Small 30.6）。开放权重榜首仍是 Kimi K3.1 Pro（#1/27）。
  - AA 时间线里还有 JT-4.1 Flash 236B A21B（中国移动，闭源，19 分，11-11 评测）。AA 收录模型总数为 735。
  - [artificialanalysis.ai 来源](https://artificialanalysis.ai/models) · [artificialanalysis.ai 来源](https://artificialanalysis.ai/models/jt-4-1-flash-236b-a21b)

---

##### 延续热度 / 降权 / 冒名

- **Trending 前 7（模型，09:21 Asia/Singapore）**：
  1. xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic：Uncensored/Heretic 改包，过滤。
  2. MiniMax-H3-Image：主条 1。
  3. speridlabs/idol：10/28 发布，上期延续。
  4. NousResearch/Arete-27B：11/06 发布，窗口前。
  5. Lightricks/LTX-2.5：老模型。
  6. Kimi-K3.1-Pro：主条 2。
  7. ricursiveAI/Ripple-65B-Preview：窗口内只有代码修复。
- **窗口内更新但降权**：
  - deepseek-ai/DeepSeek-V4.1-Flash-1017：11-10 只改了 chat template，没有新权重。
  - tencent/Qwen3.8-27B-DSpine-b16：只改了 README。
  - openbmb/MiniCPM5-2B 等 MiniCPM 全系：11-09 和 11-11 批量改文档。
  - nvidia/GR00T-N1.7-3B：许可元数据改成 nvidia-open-model-license，旧许可是什么待核。
  - webAI-Official/TwIL-LM3-Pro：11-09 15:22 UTC 重新发布，非商用许可。
  - Cloudflare/clef：补了评测结果。
  - meta-models/Muse-Spark-Open-816B-A42B：lastModified 是 11-10，但权重树仍停在 10-15，manual gated，commit 记录返回 401，未绕过。
- **同名镜像 / 存疑 repo**（只按证据列出，不认定恶意）：
  - XURMATRONIX/Kimi-K3.1-Pro、drtuch/Kimi-K3.1-Pro、Huggersachin-s1/Kimi-K3.1-Pro、omegamentiszug/Kimi-K3.1-Pro、3006IA/Kimi-K3.1-Pro：这 5 个 repo 创建于 11-10 04:48 至 20:21 UTC，repo 名、卡片、Kimi logo 都和官方相同，112 个文件、约 1,561GB。抽查 3006IA，前 50 个条目里 39 个 LFS 文件的 sha256 与官方 repo 完全一致，说明是原样复制，不是篡改权重。但它们没有标注 base_model，不是官方来源，应引导读者使用 moonshotai 官方 repo。
  - resuurcct1/Kimi-K3.1-Pro-SuperExpert-12GB：宣称把 Kimi K3.1 Pro 做成 12GB 端侧模型，元数据标 apache-2.0，与 Kimi 许可冲突；只有约 12GB 文件，不可能是完整模型（likes 0 / downloads 758（采集 11-12 09:28 Asia/Singapore）。宣称不可信，不要转发。
  - 证据：（采集证据快照）

---

##### 口径 / 缺口 / 校验

- 采集方式：
  - HF API：trending（模型 300 条、数据集 100 条）、约 100 个重点组织按 lastModified 扫描（151 个窗口候选）、按名称搜索衍生 repo。
  - 每个 ID 都抓了 api / commits / README / tree；递归 tree 在 50 条处截断，所以子目录另抓。
  - AA 首页、模型页、图像榜用 curl 保存 HTML 后解析。
  - LMArena 用 WebFetch 读全表，本地只保存选摘行。
- 缺口：
  - 401 未绕过：Muse-Spark-Open、audnai、LTX-2.5 和部分数据集的 commits/README 返回 401，没有尝试绕过。
  - AA Kimi 页：curl 失败（status 0），改用 WebFetch 读取。
  - 只对比了公开榜单的选摘内容，没有声称完整的增删名单。
  - AA t2i 行数：本期解析器读出上期快照为 107 行，11/09 素材写的是 108 行，差 1 行，属于方法差异。
- 校验：素材中出现的每个 HF ID 都单独请求了 API（数据集走 datasets API），结果见 （采集证据快照）；外链检查见 （采集证据快照）。

