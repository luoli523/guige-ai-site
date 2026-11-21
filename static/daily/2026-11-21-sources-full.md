# 2026-11-21 AI行业动态：全量原始素材

本期信息窗口从 2026 年 11 月 18 日 09:09 起，至 11 月 21 日各来源的实际采集截止，时区为 Asia/Singapore。本文保留四路采集到的全量原始摘要与来源链接，不是深读成稿，也不意味着所有候选均已独立复现。正文另见[本期深读](https://guige.ai/guige-ai-site/daily/2026-11-21/)。

- 研究与官博：官博约截止 11 月 21 日 09:01，arXiv 约在同一时段完成交叉核对；包括研究汇总、官方原文摘录和论文候选三份材料。arXiv 在 Asia/Singapore 的 11 月 18 日、19 日、20 日三批新稿与交叉列表完整；11 月 21 日周六按常规无批。扫描自 2611.21612 起（上期周三批未放全的续扫点），全站新号止于 2611.26629，续扫 2611.26630+ 与下周一正式 listing。Apple 本窗口新发为 Depth Pro 2；上期已报条目不再重复。
- X 公开动态：约截止 08:50；首页时间线实际覆盖约 11 月 20 日 05:02 至 11 月 21 日 08:48，此前约 44 小时以官方账号检索、公开检索与官方页面补齐，不代表全量时间线。
- GitHub 项目与发行：榜单与仓库快照约为 08:50–08:52；日榜、周榜不等于本期净增。
- 模型与数据集：HF 统计快照约为 09:00，热榜读取约 08:50；LMArena 因页面改版只读到前 15 名，不能跟上期全表硬比。保留模型卡、权重提交、许可、榜单与同名仓库记录，下载量为 HF 近 30 天口径。

原始材料之间可能保留不同取舍，以下说明用于避免误读：Anthropic IPO 最终定价为每股 $83.00，发行 9.80 亿股 Class A，424B4 载明公开发行总价约 $813.4 亿，这是发行规模，不是市值；ANT 首日开盘 $111.50、最高 $115.10、最低 $92.72、收盘 $97.17，次日收盘 $88.91；媒体给出的市值数字待核；采集时 SEC 公司页未见交割 8-K，不把“已交割”写成已核事实。Gemini 4 Neon、OpenAI 背景模式“最多省 40%”、OpenAI 研究进展（含与 AMD 合作最多 14% PPA 等）以及 Unsloth 的性能数字，均为厂商或作者自报。OpenAI SDK 与 Codex 中的 GPT-6.2 Sol / Astra、gpt-live-1.1 只是目录标识，不是权重发布。腾讯 Hy4 与 Hy4 flash 使用自定义的 Tencent Hy License 1.0：年营收超 5,000 万美元或月活超 1 亿的 MaaS 要另签授权，不算 OSI 开源；Hy4 flash 的 AA 分数和具体公开了哪些，待核。Inkling 2 Mini 为 Apache-2.0；微软 Aion 1.0 Instruct 为 MIT；DaisyRose-27B 是在 Qwen3.8-27B 上做的纯强化学习，Apache-2.0。harness-hub LoRA 的作者已把基座 SWE-bench Pro 从 64.7% 更正为 74.5%。冒名仓库与假仓（包括借用 Gemini 4 Neon 或其他新模型名义的仓库、非官方试用脚本、同名复制仓等）只作安全提醒，原材料中的相关记录照录，不构成推荐，也不等于把它们当作项目收录；合法转存的非官方仓库不等于冒名。本篇不做投资判断。

除去内部协作名称、个人隐私、内部本地证据路径、来源标记和不宜公开的安全操作细节，正常来源与候选保留；未读、待核、自报与不收录理由照录。以下材料不是投资、上线或商业授权建议。


## 研究与官博

### 研究汇总

#### 研究素材包 · 2026-11-21（窗口 2026-11-18 09:09 → 11-21 ~09:01 Asia/Singapore）

> 官博 4 条 + arXiv 5 条（共 9 真重点）。数字标 来源记录 / 官方自报 / 作者自报 / 待核。原始摘录见同目录 labs-raw.md、arxiv-raw.md。
> arXiv：Asia/Singapore **11/18、11/19、11/20** 批新稿+交叉列表完整（CS catchup 与 pastweek / `/new` 均为 showing N of N）；**11/21（周六）无批**（常规日程，来源记录）。扫描宇宙自 **2611.21612** 起（上期周三批未放全的续扫点）。全站新号止于 **2611.26629**（26630+ abs 探测为 404）。续扫 **2611.26630+** 与下周一正式 listing。
> 网络安全、生物与对齐条目只写结论与官方/作者数字，不写利用/合成/实验步骤。不自写主线编号。数字均保留设定与基线，**勿**无条件跨模型、跨硬件、跨基准比较。Gemini 4 Neon 模型卡已通读（10 页），完整 Safety & Security Report 官方写明「coming soon」，引用安全阈值须带这一层。

##### 官博

###### 1. Google DeepMind：Gemini 4 Neon
把 Gemini 4 家族补上介于 Carbon（最难长程项目）与 Hydrogen（日常快执行）之间的一档：主打复杂软件工程、知识工作与科学工作流，强调「更快、更便宜的前沿级推理」。是本窗口最大的官方模型发布，也是要不要在 Carbon / Hydrogen 之外再加一档生产模型的硬参考。
- blog.google `datePublished` `2026-11-18T21:00:00+00:00` → **2026-11-19 05:00 Asia/Singapore**（来源记录）。DeepMind 博客 RSS `Wed, 18 Nov 2026 21:35:43 +0000` → **05:35 Asia/Singapore**（同一文，DeepMind URL 302 到 blog.google）。模型卡 PDF 文首只标 **November 2026**（月级）。价（官方自报，每百万 token）：**$3** 输入 / **$0.15** 缓存输入（称打 **95%** 折）/ **$15** 输出；上下文 **100 万** token。即日起在 Gemini API（AI Studio 付费档）、Gemini for business、Google AI Pro / Ultra 的 Antigravity 与 Gemini 应用中推出；Fairwind 项目的网络防御用户「未来几天」开放。Neon **改编自 Carbon**（模型卡，官方自报）。知识截止日期 **2026 年 3 月**。榜均为官方自报，设定与对照须原样保留：**勿**补未给出的绝对分，也勿与 GPT‑6.2 / Claude 无条件横比。Artificial Analysis Intelligence Index 在 **xhigh** 思维档称总分 **61**、整体第 **3**，「紧随更大、更慢的模型」。Vals Index 第 **2**（**70.9%**），并称落在 Pareto 前沿；Legal Research Bench 与 Tax Agent Bench 称第 **1**。Agent Arena Index 在 4200+ 真实 agent 会话上总分 **1336**、全球第 **2**，可操纵性（steerability）亦第 **2**。Chartography **73.5%**；Agents' Last Exam v1.1 **75.8%**，称与领先模型相当。Zapier AutomationBench **56.3%**、Vending-Bench 2 **$16,843**，均称第 **1**。科学向：Terminal-Bench Science **70.5%**、RiemannBench **84.0%**、HLE-Diamond **71.3%**，称所引设定下 best in class。编码：Artificial Analysis Coding Agent Index **58.6** 称第 **1**；Terminal-Bench 4.1 **65.2%**；FrontierCode 2.0 在默认 **high** 档 **46.2%**。SWE-sweep：mini-SWE harness **12.8%**，在 Antigravity 中到 **39.0%**——后一条明确绑定 Antigravity 套件，不能当成裸模型分。默认 **high** 档称每任务成本比 Carbon 低 **32%**；在 Vals 与 Agent Arena 的 high 档称比「顶尖竞品前沿模型」每任务成本大约低 **50%–80%**；**xhigh** 称比竞品最高档仍低 **36%+**。内部 Antigravity 测试称「迄今最低的虚构率」（未给绝对值）。对齐与安全仅结论（发布文 + 10 页模型卡，官方自报）：内容安全与 Hydrogen 相近（文到文 **0.00** 个百分点、多语 **-0.40**、图到文 **+1.90**，均在置信区间内）；不当拒答比 Hydrogen 低 **3.00** 个百分点。Terminal-Bench 4.0 作弊率 **0.0%**（与 Carbon 持平），内部编码作弊评测走捷径 **2.45%**（称 Gemini 4 系列最低）；agent 安全套件不当行动率 **0.09%**，诚实性评测通过率 **99.2%**；相对 Carbon，服务不足再降 **43%–56%**、越权再降 **15%–35%**（随 effort）。Gray Swan IPI 在最高思维档加实时防护下称攻击成功率 **0.0%**，与其他 Gemini 模型相同。Terminal-Bench 4.0 拒答率 **1.98%**，Terminal-Bench-Science **0%**。网安基准只记结论：AutoBaxBench 困难档 **76%** 称 SOTA；WebExploitBench v1.2 **51.26%** 称 SOTA 且成本约为大型竞品一半；SEC-bench Pro **90.5%** 称 SOTA；CWE-bench v2 **70.7%**，比 Carbon 高 **3.4** 个百分点。Frontier Safety（模型卡，仅高层）：对 Neon 做了 Material Capability Change 评估，相对最近一次做过关键能力评估的 **Gemini 4 Argon** 有通识能力提升，但**未达到**需重跑全套关键能力评测的阈值；T/CCL 判定**沿用 Argon**——生物 CCL、网络 CCL、以及 Loss of Control 的隐蔽/情境觉知 TCL **均 cannot be ruled out**；化学/放射/核 TCL、有害操纵 CCL、ML R&D 加速与自动化 CCL **未达到**。完整 Safety & Security Report 官方写明即将发布，**本包未读到该报告**。
- [发布文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)（DeepMind 原链会跳转到此）· [模型卡 PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Neon-Model-Card.pdf)

###### 2. Thinking Machines：Inkling 2 Mini
放出一款能在笔记本上跑的开源权重小模型：中间层循环三遍的 looped transformer，想用更少生成 token 换更强推理，尤其是 agent 编程。是本窗唯一把「循环深度、可监控性与端侧体积」写在一起的官方模型发布。
- 页面 `datePublished` `2026-11-20T00:00:00+00:00` → **2026-11-20 08:00 Asia/Singapore**（官方页面元数据，来源记录）；新闻列表亦标 Nov 20。**00:00 UTC 也可能只是日级占位，精确时刻待核**。结构（官方自报）：MoE，总参数 **26.4B**、激活 **3.4B**，计循环后每 token 权重激活 **5.4B**；中间层默认循环 **3** 次。多数权重以 NVFP4 训练和部署，最后四层 MXFP8，总内存约 **20GB**。另发布研究用可变循环变体 `TML-d24-varloop-research`。开源权重，Tinker 可推理与定制；HF：`thinkingmachines/Inkling-2-Mini`。解码速度图是 **614 GB/s、BF16、batch size 1** 的理论上限，且「各模型评测设置不同」。主比较口径是「总参数小于 100B 的开源权重模型」。官方自报：DeepSWE v1.1（mini-swe-agent v2.4.6）**48.2%**、Vals Index v2.2 **46.5%**，称在该口径下领先所有对照的 <100B 开源权重模型；SWE-bench Pro v2 Hard（51 题，同一 harness）**77.9%**。表内也列了总参数 **124.5B** 的 Nemotron 3.5 Super VL，**不在**「<100B」这句里，不能混用。同表还给出 FrontierCode v2.0 **15.1%**、Terminal Bench v2.1（pi v0.83.0）**71.6%**（该行 Qwen3.8-27B 为 **73.0%**，Mini 是第二）、SWE-bench Verified（仅 bash）**79.2%**、BrowseComp（带 compaction）**79.0%**、MCP Atlas Public **82.7%** 等，均须带上表内 harness。可变循环实验（官方自报）：无 CoT 时程从 1 次循环的 **16 秒** 提到 3 次的 **37 秒**；串行推理基准在训练所用循环数的两倍（10 次）上仍在提升；CoT 随循环变短但仍可读；循环加多后，agent 破坏类测试**没有**变高的趋势。知识类基准不随循环提升，模型靠搜索和工具补事实。安全数字仅记结论，不写攻击构造。
- [发布文](https://thinkingmachines.ai/news/inkling-2-mini/) · [HF 权重](https://huggingface.co/thinkingmachines/Inkling-2-Mini) · [模型卡](https://thinkingmachines.ai/model-card/inkling-2-mini/) · [可变循环研究模型](https://thinkingmachines.ai/model-card/tml-d24-varloop-research/)

###### 3. OpenAI：研究加速的 jagged frontier
用内部测量更新「编码智能体如何加速 OpenAI 自己的研究」：智能体已经能独立完成近一半的中短时任务，但提升是参差的，人仍在回路里。这是本窗最完整的一份官方 RSI / 研究加速指标，可与上期 GPT‑6.2 系统卡里的 Self-Improvement 阈值对照，但不能把内部使用数字读成对外模型能力。
- News RSS `Wed, 18 Nov 2026 08:00:00 GMT` → **2026-11-18 16:00 Asia/Singapore**（来源记录）。文首日期 November 18, 2026。数字均为**官方自报的内部测量**，方法学随文有修订，且任务类型会随能力变化而改变，不能外推到其他实验室或对外 API。2026 年 3 月至 10 月，对「估计需要人做 2–4 小时」的任务，零干预成功率从 **23%** 升到 **46%**；4–8 小时任务从 **13%** 升到 **35%**。按任务类型：监控训练运行 **79%**，启动训练运行 **35%**，编写推理与 serving 代码 **25%**。按 API 标价，10 月研究者每日用量中位数约 **$2,400**（比 9 月高 **62%**），90 分位约 **$23,000**（高 **105%**）；9 月基线是 **$1,500** / **$11,000**。问卷：为保留三个月的前沿编码智能体，中位数愿意拿团队算力的 **30%**，或另题中的团队编制 **40%**。Safety & Alignment 的记录工作周 1–9 月增加 **77%**，是各研究方向里绝对增量最大的，文中将加速与 7 月 Hugging Face 事件后的安全案例工作联系起来。每个研究者的「智能体工作日」（每 8 小时计 1 日）从 **0.5** 增到 **5.7**（约 **11** 倍）；预训练与后训练团队约 **8**，扩缩与基础设施约 **4**；该指标一般只计交互使用，可能低估自动化。到 10 月中，超过三分之二的纳入统计研究者日峰值至少 **4** 个并发智能体，超过 **10%** 至少 **16** 个。9 月，研究组织里智能体使用的 API 等价花费约为非股权薪酬的 **两倍**（股权通常占目标薪酬 **70%–80%**，未计入）；内部部署只占研究算力的 **2%**。文中明确：这是对 RSI 指标的透明报告，**不应**读成追求完全递归自我改进的声明。
- [发布文](https://openai.com/index/research-acceleration-jagged-frontier)

###### 4. OpenAI：MedChemBench
用 99 道来自已发表研究的题，测模型能不能把分子结构、实验证据和「下一步测哪个化合物」连起来。是本窗少有的、带完整论文的药物化学推理基准，只说明模型在历史证据上的推理表现，不能读成已经能发现新药。
- News RSS `Fri, 20 Nov 2026 00:00:00 GMT` → **2026-11-20 08:00 Asia/Singapore**（来源记录）。文首 November 20, 2026。论文 PDF 由发布文给出。基准（官方自报）：**99** 题，源自 **117** 篇论文与专利，含 **761** 个不同分子结构；四部分是结构复原、科学解释、排序/选择、数值性质预测。在 **xhigh** 推理档，GPT‑6.2 Astra 得到可用分数的 **84.5%**，对照 GPT‑6 Astra **83.3%**、GPT‑6.1 Sol **82.0%**、GPT‑5.6 Sol **58.2%**。在十一套模型共享的最高档（xhigh）上，GPT‑6 Astra 全基准 **83.3%**，结构部分 **95.4%**，但选择化合物与预测数值性质「大约只有一半分数」。GPT‑6 Astra 在 max 档到 **83.8%**。局限写得很清楚（官方自报）：不能说明模型能否发现新药或改进实验室决策；无法排除对已发表来源的事先暴露；每次作答是单次尝试，不用工具、没有反馈、也没有新实验。只写评测结论，不转写具体分子改造或实验步骤。
- [发布文](https://openai.com/index/introducing-medchembench/) · [论文 PDF](https://cdn.openai.com/pdf/09c4ec60-a32e-4652-837b-1811368a3bb0/medchembench-paper.pdf)

##### arXiv

###### 5. Reflection：Beam（2611.26358）
Reflection 的第一款开源权重模型：501.3B 总参数、23.4B 激活的稀疏 MoE，对准编程、推理和 agent 负载，并配上一份很长的训练与服务报告。是本窗体量最大的开源模型技术报告。
- 提交/公布：API published `2026-11-19T16:28:23Z` → 2026-11-20 00:28 Asia/Singapore；**Asia/Singapore 归属 11/20**（Fri 新稿，主类 cs.CL，兼 cs.AI）。机构证据：PDF 首页「Reflection Team」、通讯 `（机构署名邮箱略）`（来源记录）。文中 GLM-5.2、Qwen 3.8-Max、NVIDIA GB300、DFlash 等是对照、硬件或解码组件，**不是**作者单位。主要数字与条件（作者自报）：总参数 **501.3B** / 激活 **23.4B**，52 层、每层 256 专家、每 token 激活 8 个专家，词表约 **152K**，上下文提到 **1M** token（两阶段 midtraining）。预训练 **23.8T** token；预训练在 **6,144** 块 GB300 上不到四周，后期 goodput **92.3%**、稳态 MFU **21%**（已计重启）。后训练异步 RL：超过 **100M** 条 rollout，**10.5K** 块 GB300，四周；作者称这是「开放实验室迄今最大规模的 RL 之一」，评测集上「随 RL 算力增加仍未见平台」。推理侧有 FP8/NVFP4 与 **1.93B** 的 DFlash 2 草稿器。作者称推理算力约为「同类许多模型」的 **1/3 到 1/4**，并与 GLM-5.2、Qwen 3.8-Max（LongBench-v2）对照——都是作者口径，不能改写成无条件 SOTA。安全仅结论：在其 Open Safety Framework 下，生物武器、化学武器、失控、网络攻击四类均为 **Limited**（称相对可比开源权重模型，攻防平衡与威胁面无实质扩大）；内部 ISE 基准上，有害请求拒绝/转向 **88.9%**、无害请求遵从 **81.5%**，称在开源权重 Pareto 前沿上有害拒绝/转向率最高。对齐教师从 100B 扩到 501B 后，误拒下降 **48.7%**。摘要未列 SWE-bench 等绝对分，引用须回到正文表格。
- [2611.26358](https://arxiv.org/abs/2611.26358)

###### 6. 2611.25673 CompAct-Bench：把「压缩工作上下文」当成可单独打分的能力
长程智能体常把历史交给一个模型压短再继续干；这篇把压缩器与执行器拆开，看压完之后还能不能把活做完。对正在做上下文压缩、handoff 或记忆折叠的人，是一套能直接对照的过程级基准。
- API published `2026-11-19T07:49:37Z` → 2026-11-19 15:49 Asia/Singapore；**Asia/Singapore 归属 11/20**（Fri 新稿，主类 cs.AI）。机构证据：PDF 首页「1 Fudan University，2 Hunyuan Team, Tencent，3 SIGS, Tsinghua University」，通讯 `（机构署名邮箱略）`、`（机构署名邮箱略）`（来源记录）。应写成 **复旦大学 + 腾讯混元（Maxm Pan）+ 清华深圳国际研究生院**，不要写成单一机构论文。数字（作者自报）：**200** 项过程级任务，覆盖信息检索、软件工程与办公自动化（BrowseComp、SWE-bench 与内部 CompanyBench）。每个实例在中间边界压缩，固定执行器从对应环境状态、在匹配的动作预算下续跑。评估 **12** 个前沿模型作压缩器。入选任务在压缩前三次预筛中全部做成，压缩后平均准确率降到 **56.7%**，最好的模型也只有 **68.5%**（摘要未点名该模型，勿补）。失败路径概括为：漏掉信息导致重复劳动、预算耗尽；以及状态被写歪，把尚不确定的证据写成结论并过早结束。这些是该套件、该执行器协议上的数字，不能外推到其他压缩实现。
- [2611.25673](https://arxiv.org/abs/2611.25673)

###### 7. 2611.25123 GrepMem：先原样记下，需要时再 grep
不先决定「该记什么」，而是把完整历史追加成纯文本日志，用正则搜索按需召回。和上期 HEAMS、以及本期 CompAct-Bench 正好形成对照：有人做结构化记忆与治理，有人把压缩本身当能力，这篇则把「无损、无索引」做到一种可训练的基线。
- API published `2026-11-18T20:02:57Z` → 2026-11-19 04:02 Asia/Singapore；**Asia/Singapore 归属 11/20**（Fri 新稿，主类 cs.CL，兼 cs.AI）。机构证据：PDF 首页「University of Southern California」，通讯 （机构署名邮箱略）（来源记录）。Qwen3.5-9B 是被训练和评测的底座，不是作者单位。数字（作者自报）：在五种上下文管理策略下用强化学习训练 Qwen3.5-9B，评测多问题研究会话、长流召回和轨迹问答。ContextBench 准确率 **95–97%**，有损基线最高 **21%**；在 BCP-Multi 上比 SUPO 的摘要法高 **8.8** 个百分点。作者称在五个任务上都还留在准确率–token 成本的 Pareto 前沿。这是该模型、这五套任务上的结果，不能直接说「grep 已经替代结构化记忆」。
- [2611.25123](https://arxiv.org/abs/2611.25123)

###### 8. 2611.22971 SEAM：跨屏幕组合起来才有害的计算机使用评测
现有计算机使用安全基准，往往把危害放在指令或单屏上；SEAM 要测的是：每条指令、每一屏单独看都无害，组合起来才有害时，智能体还会不会做下去。只写结论，不写任务构造或利用步骤。
- API published `2026-11-17T15:53:58Z` → 2026-11-17 23:53 Asia/Singapore；**Asia/Singapore 归属 11/18**（Wed 新稿，主类 cs.CR，兼 cs.AI）。机构证据：PDF 首页「Tsinghua University The Chinese University of Hong Kong ByteDance Shenzhen University」，通讯 `（机构署名邮箱略）`（来源记录）。**多机构合作**，不要写成单一的清华或 ByteDance 论文。数字与结论（作者自报）：**600** 项跨应用、多步的 OSWorld 任务；开源权重与旗舰智能体在最多 **92%** 的运行里仍会执行该组合危害，但若用户用一句话直接说出同一危害，则会拒绝。智能体常常打开了关键页面，暴露本身不是主要瓶颈；问及时能标出危害，思维链里有时也会写下冲突，然后仍然确认执行。作者称专有模型明显更谨慎。识别危害并不稳定地转化成安全执行，而且更取决于信息是出现在用户指令里，还是出现在屏幕上。发布页：[yuxuan2003.github.io 来源](https://yuxuan2003.github.io/SEAM/) 。
- [2611.22971](https://arxiv.org/abs/2611.22971)

###### 9. 2611.21832：审计人员很难从完整研究记录里抓住对安全研究的破坏
在「模型可能破坏用于改进自身安全的研究」这个设定下，用人类专家做代理破坏者，再让审计人员看完整记录并复跑实验。和本期 OpenAI 的研究加速报告是同一主题的另一面：智能体越深地进入研发，审计是不是跟得上。只写结论，不写破坏手法。
- API published `2026-11-16T19:52:38Z`；PDF 页眉有 v2（18 Nov 2026）；**Asia/Singapore 归属 11/18**（Wed 新稿，主类 cs.AI）。机构证据：PDF 脚注「1 Redwood Research。2 Georgia Institute of Technology。…… Independent。4 Equistamp」，通讯 `（机构署名邮箱略）`（来源记录）。作者行：Keshav Shenoy、Eric Gan、Sebastian Prasanna、Julian Stastny、Vivek Hebbar 属 Redwood Research；Anthony Zang 属 Georgia Institute of Technology；Jacqueline Tay 为 Independent；Amy Ngo 属 Equistamp。应写成 **Redwood Research + Georgia Institute of Technology + Independent + Equistamp**。数字（作者自报）：10 项新的安全研究实验，得到 10 条良性与 12 条被破坏的记录。人类审计人员在能看完整记录并复跑实验的条件下，区分两者的 AUROC 为 **0.59**，与随机无显著差异；只有 **17%** 的案例完全找出具体破坏。摘要还写：在**不允许**复跑实验的条件下，前沿模型可能高于人类审计（Fable 5.1：AUROC **0.73**，完全识别 **32%**）——这两条不是同一协议，不能合成「模型已经比人会审计」。正文另有 25 名审计、各 90 分钟等设定，引用须带回协议限制。这是小样本、人工代理破坏的压力测试，不是对线上系统已被破坏的判断。
- [2611.21832](https://arxiv.org/abs/2611.21832)

##### 其他窗口内条目（不进主包，供对照）

- OpenAI [Combatting adversarial distillation](https://openai.com/index/combatting-adversarial-distillation/)（RSS **11-20 18:00 Asia/Singapore**）：官方安全方法文。内部自适应黑盒评测（官方自报，仅高层）：从先前请求中提取受保护推理的攻击成功率，从 GPT‑6 Astra 原防护的 **54.0%** 降到 GPT‑6.2 Astra 更新防护的 **0.2%**；当前请求为 **22.9% → 0.9%**。不写提取或攻击步骤。可与主包 #3 对照。
- OpenAI [Inside the Codex sandbox](https://openai.com/index/inside-the-codex-sandbox)（**11-18 16:00 Asia/Singapore**）、[Performance Factory](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)（**11-19 16:00 Asia/Singapore**）、[Managing frontier AI risk](https://openai.com/index/managing-frontier-ai-risk)（**11-18 14:00 Asia/Singapore**）：工程与政策长文，非新模型或新基准。[The Silent Consensus](https://openai.com/index/the-silent-consensus)（**11-18 18:00 Asia/Singapore**）为个人演讲改写，文首写明不代表 OpenAI 立场。客户案例与商务演示不录。
- DeepMind / Google [Genie 4 现已对 Ultra 用户开放](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/)（blog.google `datePublished` 11-18 18:00 UTC → **11-19 02:00 Asia/Singapore**；DeepMind RSS `Wed, 18 Nov 2026 18:13:42 +0000` → **02:13 Asia/Singapore**）：世界模型产品化更新（实时改环境、原生音频、社区画廊、Genie 3 单段最长 3 分钟等）。研究概述页 [Genie 4: A new generation of world simulation](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/) 的 DeepMind RSS 为 **2026-10-27 16:01:38 +0000**，早于本窗，不是新论文宣布。[Genie 4 进入 Gemini API](https://blog.google/innovation-and-ai/technology/developers-tools/genie-4-in-gemini-api/)（**11-20 01:00 Asia/Singapore**）为接口短讯。
- Google [Gemini API Tool Retrieval](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/)（**11-20 02:00 Asia/Singapore**）：Interactions API 预览，按需加载工具参数 schema，面向 Gemini 3.6 及以后。产品/API 文。
- Apple [Depth Pro 2](https://machinelearning.apple.com/research/depth-pro-2-monocular)（页面/RSS `2026-11-20 00:00:00 GMT` → **08:00 Asia/Singapore**，Apple 常见日级占位，时刻待核）+ arXiv [2611.26603](https://arxiv.org/abs/2611.26603)（Asia/Singapore 11/20，主类 cs.CV，兼 cs.LG）。PDF 首页单位为 **Apple**（来源记录）。单网络同时处理图像与视频，称同时做到度量尺度、边缘锐利与时间一致性；发布 24M–872M 一簇模型及[代码与权重](https://github.com/apple-aiml-research/ml-depth-pro-2)。视觉基础模型，不是 agent 主线。
- Amazon Science [Mathematical proof, powered by AI](https://www.amazon.science/blog/mathematical-proof-powered-by-ai-and-no-hallucinations)（**11-19 02:55 Asia/Singapore**）：介绍 AutoCorrode 套件（I/Q、I/R、Isabelle Assistant）经 MCP 把智能体接到 Isabelle；示例为经典证明，不是新的大规模自动形式化结果。
- Google Research [A game you cannot win unless you have a quantum computer](https://research.google/blog/a-game-you-cannot-win-unless-you-have-a-quantum-computer/)（RSS **11-20 04:03 Asia/Singapore**）与 blog.google [量子语境性大规模检验](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/putting-one-of-quantum-mechanics-deepest-features-to-test-at-scale/)（**11-20 03:00 Asia/Singapore**）：量子研究，不是语言模型发布。
- Meta 工程：[用 AI agents 规模化广告排序模型创新](https://engineering.fb.com/2026/11/18/ml-applications/ai-agents-to-scale-ml-innovations-across-ads-ranking-models/)（**11-19 01:00 Asia/Singapore**）、[模板化 ML 生态](https://engineering.fb.com/2026/11/18/ml-applications/design-once-deploy-at-scale-template-driven-ml-ecosystem/)（**11-19 00:59 Asia/Singapore**）。about.fb 另有开源科学峰会综述（**11-21 02:30 Asia/Singapore**），属活动回顾。
- NVIDIA 开发者博客：[Dynamo 降低 RL rollout 瓶颈](https://developer.nvidia.com/blog/reducing-rollout-bottlenecks-in-reinforcement-learning-with-nvidia-dynamo/)（**11-20 04:28 Asia/Singapore**）等工程文；无新的基础模型技术报告。上期已报的 MLPerf / Vera Rubin 等不当本期新发。
- Anthropic 窗内 News 为 [IPO 定价](https://www.anthropic.com/news/anthropic-prices-initial-public-offering)（页面 `publishedOn` **2026-11-18**，日级）与 [IPO 完成](https://www.anthropic.com/news/ipo-close)（**2026-11-20**），属公司公告，不进研究主包。研究列表最新可见 [Claude 与黑洞物理](https://www.anthropic.com/research/claude-black-hole-physics)（`publishedOn` **2026-11-17**），**早于本窗起点**，不作为本期新发。
- arXiv 备选偏强：[2611.24636 Clover-35B-A3B-Preview](https://arxiv.org/abs/2611.24636)（DiffuSpace；35B-A3B 扩散语言模型，作者自报 SWE-bench Verified **73.6**、Terminal-Bench 2.1 **51.7**，内部 1×GB300 BF16 bs=1 生成约 **680** token/s）；[2611.22161](https://arxiv.org/abs/2611.22161)（**Surge AI** 对 Nemotron 3.5 Super 做分任务 LoRA RL，**不是** NVIDIA 官方论文；SWE-bench Pro V2 **86.9%→92.1%** 等，作者自报）；[2611.26248 TwinLab-Bench](https://arxiv.org/abs/2611.26248)（浙江大学；52 项真实实验室孪生任务，注释写 Claude Fable 5.2 **45.0**，仅高层，不写实验操作）；[2611.21646 Limite 1B Violetto](https://arxiv.org/abs/2611.21646)（Paradigma；1B 数学模型，AIME 2026 **94.01%**，提交于 10 月 14 日、Asia/Singapore 11/18 才放批）；[2611.22777 CrossEnv](https://arxiv.org/abs/2611.22777)（北京理工大学 + 阿里巴巴 + 北京邮电大学）。

##### Apple 补录备忘（不是本期新发）

对照上期记录，本期 `/research` 全列表为 **1194** 条（上期 **1192**）。按 `published` 日期，**2026-11-17 及以后只有 Depth Pro 2**。上期已报的 Split-and-Scale（11-16）及更早补录，不再重复。本机上期 `__NEXT_DATA__` 缓存为空，未能做 slug 逐条对账；若另有 1 条晚出现但 `published` 早于窗口的条目，**不当本期新发**。

##### 覆盖缺口

- OpenAI `/news`、`/news/research/` 与多篇 `/index` 详情页本窗 curl **200**（上期部分 403）；正文以页面提取为准。MedChemBench 论文 PDF 已下载（27 页），主包数字取自发布文，未逐表深读 PDF。
- Gemini 4 Neon 模型卡（10 页）已通读；完整 Safety & Security Report **尚未上线**（模型卡写明 coming soon）。blog.google 主 RSS 仍只有 20 条，最旧约 11-19 01:00 Asia/Singapore；已用 models / developer-tools / innovation / cloud 分类 RSS 与 DeepMind RSS 补扫 11-18 09:09 之后的研究长文，消费类短帖仍可能被主 RSS 挤出。
- Apple RSS 只有 10 条，完整性以 `/research` 全列表为准；上期 next-data 缓存缺失，slug 对账不完整。
- arXiv：Asia/Singapore **11/18–11/20** 新稿+交叉已完整；替换稿未当新条目精读。11/21 无批。续扫 **2611.26630+**。
- 未把缺访问写成无更新。Anthropic research/news/engineering、Alignment、OpenAI Alignment、Google Research RSS、MSR 博客列表、Meta research / engineering feed、Thinking Machines 博客与新闻页、Amazon Science index.rss、NVIDIA 双 feed 均已成功访问。窗内无新研究长文的机构：Anthropic（仅 IPO 公告）、Microsoft Research、Meta AI 研究博客（工程博客有文，见上）、OpenAI Alignment。
- 第三方转述数字无官博原文则不收。

### 官方原文摘录

#### Labs Raw Excerpts — 2026-11-21

- **窗口**: 2026-11-18 09:09 Asia/Singapore → **2026-11-21 09:01 Asia/Singapore**（Asia/Singapore, UTC+8；采集截止以本机 `date` 为准）
- **采集时间**: 2026-11-21 约 08:51–09:01 Asia/Singapore
- **说明**: 原始摘录；关键数字标「官方自报 / 来源记录 / 待核」。网络安全与生物仅写结论与官方数字，不写利用/合成/实验步骤、攻击轨迹或提示构造。已在上期主包或窗口外的条目不作为本期重点重复。
- **去重参照**: （内部证据存档）、`research.md`。上期已报勿重复：GPT‑6.2 Astra / Sol 发布文与系统卡、OpenAI 科学家使用研究与格点标准模型客座文、Hydrogen Safety & Security Report、Anthropic 缩短 CVD 窗口、blog.google EmbeddingGemma 2 技术报告帖（模型本身 10 月已发）、Apple Split-and-Scale、MSR TokenEconomizer、NVIDIA MLPerf Training v6.1 / Endpoints v1.0 / Vera Rubin 相关、Nemotron 后训练科学域文、Thinking Machines 端到端 4-bit 训练。上期备选与更早主包不当新条目重报。上期数字不在此复述。
- **边界排除**: OpenAI [Advancing chip design](https://openai.com/index/advancing-chip-design-with-our-models) RSS `Wed, 18 Nov 2026 00:00:00 GMT` → **2026-11-18 08:00 Asia/Singapore**，早于 09:09 起点，**不纳入本窗**。Anthropic [Claude Fable 5.2 solves two open problems in the physics of black holes](https://www.anthropic.com/research/claude-black-hole-physics) 页面 `publishedOn` **2026-11-17**（日级），早于本窗。

---

##### OpenAI

**源查证**: [openai.com 来源](https://openai.com/news/rss.xml)（curl + Chrome UA，HTTP 200，1421 条）；[openai.com 来源](https://openai.com/news/) 与 `/news/research/` 本窗 HTTP 200。辅以 [alignment.openai.com 来源](https://alignment.openai.com/) 与 [alignment.openai.com 来源](https://alignment.openai.com/rss.xml)（均 200；最新仍是 10 月 6 日 LASER，窗内无新帖）。

###### 1) Research acceleration: The jagged frontier — **建议进主包（官方 RSI / 研究加速指标）**
- **日期**: News RSS `Wed, 18 Nov 2026 08:00:00 GMT` → **2026-11-18 16:00 Asia/Singapore**（来源记录）
- **URL**: [openai.com 来源](https://openai.com/index/research-acceleration-jagged-frontier)
- **人话**: 用内部测量更新编码智能体如何加速 OpenAI 自己的研究：中短时任务的零干预成功率大约翻倍，但按任务类型很参差，人仍在回路里。
- **要点**（均为官方自报的内部测量，除非另注）:
  - 3 月至 10 月：估计需人做 2–4 小时的任务，零干预成功 **23% → 46%**；4–8 小时 **13% → 35%**。
  - 任务类型：监控训练运行 **79%**，启动训练运行 **35%**，编写推理与 serving 代码 **25%**。
  - API 标价日用量：10 月中位数约 **$2,400**（+**62%** vs 9 月 **$1,500**），90 分位约 **$23,000**（+**105%** vs **$11,000**）。
  - 问卷：为保留三个月前沿编码智能体，中位数愿拿出团队算力 **30%**，或另题中的团队编制 **40%**。
  - Safety & Alignment 记录工作周 1–9 月 +**77%**，绝对增量最大；文中联系 7 月 Hugging Face 事件后的安全案例工作。
  - 「智能体工作日」（8 小时计 1 日）人均 **0.5 → 5.7**（约 11 倍）；预训练/后训练约 8，扩缩与基础设施约 4。一般只计交互使用。
  - 10 月中：超过三分之二的纳入统计研究者日峰值 ≥**4** 个并发智能体，超过 **10%** ≥**16** 个。
  - 9 月 API 等价智能体花费约为非股权薪酬的 **两倍**（股权通常占目标薪酬 70%–80%，未计）；内部部署占研究算力 **2%**。
- **局限**: 内部口径，方法学有修订；任务委派类型会随能力变化。文中写明不应读成追求完全 RSI。不可外推到其他实验室或对外产品能力。
- **标注**: 来源记录 / 官方自报。

###### 2) Can AI help scientists identify promising drug candidates? / Introducing MedChemBench — **建议进主包（药物化学推理基准）**
- **日期**: News RSS `Fri, 20 Nov 2026 00:00:00 GMT` → **2026-11-20 08:00 Asia/Singapore**（来源记录）
- **URL**: [openai.com 来源](https://openai.com/index/introducing-medchembench/)
- **论文 PDF（官方）**: [cdn.openai.com 来源](https://cdn.openai.com/pdf/09c4ec60-a32e-4652-837b-1811368a3bb0/medchembench-paper.pdf)（27 页，已下载；主包数字取自发布文，未逐表深读）
- **人话**: 99 道来自已发表文献的题，测模型能否把分子结构、实验证据和化合物选择连起来；发布文把结构复原强、选择与数值预测弱这一点写清楚了。
- **要点**（官方自报）: 99 题、117 篇论文/专利、761 个分子结构；四部分为结构、解释、排序/选择、数值预测。xhigh 档：GPT‑6.2 Astra **84.5%**，GPT‑6 Astra **83.3%**，GPT‑6.1 Sol **82.0%**，GPT‑5.6 Sol **58.2%**。GPT‑6 Astra 结构部分 **95.4%**，选择与数值「大约一半分数」；max 档 **83.8%**。
- **局限**: 官方写明不能说明能否发现新药；无法排除对已发表来源的事先暴露；单次作答、无工具、无新实验。只写结论，不转写分子改造或实验步骤。
- **标注**: 来源记录 / 官方自报。

###### 3) Combatting adversarial distillation — **强候选（安全方法，仅高层）**
- **日期**: News RSS `Fri, 20 Nov 2026 10:00:00 GMT` → **2026-11-20 18:00 Asia/Singapore**（来源记录）
- **URL**: [openai.com 来源](https://openai.com/index/combatting-adversarial-distillation/)
- **人话**: 说明为何要保护模型的思维链，以及 GPT‑6.2 上请求级与活动级防护如何一起用。
- **要点**（官方自报，仅高层）: 内部自适应黑盒评测、六种攻击模型汇总：从先前请求提取受保护推理的 ASR，GPT‑6 Astra 原防护 **54.0%** → GPT‑6.2 Astra 更新防护 **0.2%**；当前请求 **22.9% → 0.9%**。称正在把部分改进回应用到 GPT‑6 Astra。不写提取、红队或执法操作细节。
- **标注**: 来源记录 / 官方自报。

**其他窗内（不挤研究主包）**:
- [Inside the Codex sandbox](https://openai.com/index/inside-the-codex-sandbox)（RSS **11-18 16:00 Asia/Singapore**）：工程深潜。
- [How OpenAI’s Performance Factory keeps ChatGPT fast](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)（**11-19 16:00 Asia/Singapore**）。
- [Managing frontier AI risk: From training to deployment](https://openai.com/index/managing-frontier-ai-risk)（**11-18 14:00 Asia/Singapore**）：政策/流程综述，仅高层。
- [The Silent Consensus](https://openai.com/index/the-silent-consensus)（**11-18 18:00 Asia/Singapore**）：Dean Ball 演讲改写，文首写明不代表 OpenAI 立场。
- 客户案例（Hebbia、Sumitomo Life）与商务演示（Codex Security Plugin、PR scans、Daybreak）不录。

**Alignment 博客**: 窗内无新帖（非缺访问）。

---

##### Anthropic

**源查证**: [anthropic.com 来源](https://www.anthropic.com/research)、`/news`、`/engineering`（均 200）；[alignment.anthropic.com 来源](https://alignment.anthropic.com/)（200）。RSS 备用地址 `/feed`、`/rss.xml` 为 404，完整性以列表页 `publishedOn` 为准。

**窗内 News（公司公告，不进研究主包）**:
- [Anthropic prices initial public offering](https://www.anthropic.com/news/anthropic-prices-initial-public-offering)：页面 `publishedOn` **2026-11-18**（日级，时刻待核）。
- [Anthropic announces closing of initial public offering...](https://www.anthropic.com/news/ipo-close)：**2026-11-20**（日级）。

**研究 / Engineering / Alignment**: 窗内**无新研究长文**（非缺访问）。列表可见的 [Claude Fable 5.2 solves two open problems in the physics of black holes](https://www.anthropic.com/research/claude-black-hole-physics) 为 **2026-11-17**，早于本窗。[Strengthening our defenses against distillation attacks](https://www.anthropic.com/news/distillation-defenses) 页面日期 **2026-10-12**，不是新发。

---

##### Google DeepMind / blog.google

**源查证**: DeepMind RSS [deepmind.google 来源](https://deepmind.google/blog/rss.xml)（200，100 条）；blog.google 主 RSS 与 models / developer-tools / innovation / cloud 分类 RSS（均 200，各约 20 条）。DeepMind 博客页 200。Gemini 4 Neon 与 Genie 4 的 deepmind.google/blog URL 均 **302** 到 blog.google 对应文（来源记录）。

###### 4) Introducing Gemini 4 Neon — **建议进主包（前沿模型发布）**
- **日期**: blog.google `datePublished` `2026-11-18T21:00:00+00:00` → **2026-11-19 05:00 Asia/Singapore**（来源记录）。DeepMind RSS `Wed, 18 Nov 2026 21:35:43 +0000` → **05:35 Asia/Singapore**。
- **URL**: [blog.google 来源](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)
- **模型卡 PDF（官方）**: [storage.googleapis.com 来源](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Neon-Model-Card.pdf)（标题 *Gemini 4 Neon Model Card*，文首 **Published: November 2026**；**10** 页，已通读）。完整 Safety & Security Report 写明「coming soon」，本窗未取到。
- **人话**: Gemini 4 家族里介于 Carbon 与 Hydrogen 之间的一档，面向复杂软件工程、知识工作与科学工作流，强调更快、更便宜的前沿级推理。
- **要点**（官方自报，除非另注；设定与对照须原样保留）:
  - 定价（发布文口径，每百万 token）：**$3** 输入 / **$0.15** 缓存输入（称 95% 折扣）/ **$15** 输出；100 万 token 上下文。
  - 可用性：Gemini API（AI Studio 付费档）、Android Studio、Gemini for business、Pro/Ultra 的 Antigravity 与 Gemini 应用；Fairwind 网络防御用户「未来几天」。
  - 模型卡：Neon **改编自 Carbon**；知识截止日期 **2026 年 3 月**。
  - 主要榜（发布文）：AA Intelligence Index 在 xhigh 档总分 **61**、整体第 3；Vals Index 第 2（**70.9%**）；Agent Arena **1336** / 全球第 2（4200+ 会话），steerability 第 2；Chartography **73.5%**；Agents' Last Exam v1.1 **75.8%**；AutomationBench **56.3%**、Vending-Bench 2 **$16,843** 称第 1；Terminal-Bench Science **70.5%**、RiemannBench **84.0%**、HLE-Diamond **71.3%**；Coding Agent Index **58.6** 称第 1；Terminal-Bench 4.1 **65.2%**；FrontierCode 2.0 默认 high **46.2%**；SWE-sweep mini-SWE **12.8%**，Antigravity **39.0%**（后一条绑定套件）。
  - 成本：默认 high 比 Carbon 每任务低 **32%**；Vals / Agent Arena 的 high 档称比顶尖竞品低约 **50%–80%**；xhigh 比竞品最高档低 **36%+**。
  - 安全仅高层：见主包。完整安全报告未上线；T/CCL 沿用 Argon。网安基准不要当成线上带防护系统的表现。
- **标注**: 来源记录 / 官方自报。模型卡未逐项对外基准表深读（卡内基准细节指向 deepmind.com/models/evals-methodology/gemini-4-neon）。

###### 5) Genie 4 is now available / Project Genie update — **产品化更新（不挤研究主包）**
- **日期**: blog.google `datePublished` `2026-11-18T18:00:00+00:00` → **2026-11-19 02:00 Asia/Singapore**（来源记录）。DeepMind RSS `Wed, 18 Nov 2026 18:13:42 +0000` → **02:13 Asia/Singapore**（来源记录）。
- **URL**: [blog.google 来源](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/)
- **人话**: 向 Google AI Ultra 用户开放 Genie 4 与新的 Project Genie 体验（实时改环境、原生音频、社区画廊、Genie agent）；Genie 3 单段最长提到 3 分钟（此前 60 秒），并支持 360° 全景锚定。文中指向既有研究概述 [deepmind.google 来源](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)（DeepMind RSS `Tue, 27 Oct 2026 16:01:38 +0000`，早于本窗），不是本窗新论文宣布。输入输出走 SynthID 与安全筛查。
- **相关短讯**: [Genie 4 now available through the Gemini API](https://blog.google/innovation-and-ai/technology/developers-tools/genie-4-in-gemini-api/)（`2026-11-19T17:00:00+00:00` → **11-20 01:00 Asia/Singapore**）。

###### 6) Introducing Tool Retrieval in the Gemini API — **产品 / API（不挤主包）**
- **日期**: `2026-11-19T18:00:00+00:00` → **2026-11-20 02:00 Asia/Singapore**（来源记录）
- **URL**: [blog.google 来源](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/)
- **要点**: Interactions API 预览；`tool_search` + `defer_loading: true`，先只给工具名与描述，需要时再加载参数 schema。文称适用于 Gemini 3.6 及以后。未给节省 token 的官方绝对数。

**产品 / 活动（不挤研究主包）**: Gemini 应用电脑使用（Mac）、历史导入、Connected Apps、Watch Duty、Workspace 中小企业故事、Flow 艺术家、Project Suncatcher 与 Blue Origin 合作、数据中心与水务、Duplex 演进（见下）等。

---

##### Google Research

**源查证**: [research.google 来源](https://research.google/blog/rss/)（200，100 条）。

- [How Google Duplex evolved to also call businesses for you in Gemini](https://research.google/blog/how-google-duplex-evolved-to-also-call-businesses-for-you-in-gemini/)（RSS **2026-11-21 07:30 Asia/Singapore**）：产品演进综述，不是新模型或新论文宣布。
- [A game you cannot win unless you have a quantum computer](https://research.google/blog/a-game-you-cannot-win-unless-you-have-a-quantum-computer/)（RSS **2026-11-20 04:03 Asia/Singapore**）：量子计算科普/研究文。配合 blog.google [Testing quantum contextuality at scale](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/putting-one-of-quantum-mechanics-deepest-features-to-test-at-scale/)（`2026-11-19T19:00:00+00:00` → **11-20 03:00 Asia/Singapore**）。均非语言模型发布。

上期已报的 Antigravity `/teamwork` 汇编不重复。

---

##### Meta（research.meta.ai / about.fb.com / engineering.fb.com）

**源查证**: 未打开易坏的 ai.meta.com 主页。`research.meta.ai/blog/`（200）、`about.fb.com/news/` + `/news/feed/`（200）、`engineering.fb.com` + `/feed/`（200）。

- **research.meta.ai/blog/**: 已成功访问。列表最新仍是 November 9 的 Muse Ember 与 November 6 的 Specialized Models——均上期已报或更早，**窗内无新研究博文**（非缺访问）。
- **engineering.fb.com 窗内工程文（不挤研究主包）**:
  - [How Meta Uses AI Agents to Scale ML Innovations Across Ads Ranking Models](https://engineering.fb.com/2026/11/18/ml-applications/ai-agents-to-scale-ml-innovations-across-ads-ranking-models/)（feed `Wed, 18 Nov 2026 17:00:00 +0000` → **11-19 01:00 Asia/Singapore**）。
  - [Design Once, Deploy at Scale: Building a Template-Driven ML Ecosystem](https://engineering.fb.com/2026/11/18/ml-applications/design-once-deploy-at-scale-template-driven-ml-ecosystem/)（**11-19 00:59 Asia/Singapore**）。
- **about.fb.com**: [Advancing Science Together: Highlights From the Open Source AI For Science Summit](https://about.fb.com/news/2026/11/advancing-science-together-highlights-from-the-open-source-ai-for-science-summit/)（**11-21 02:30 Asia/Singapore**）为活动综述。另有 Forum 印尼上线、商业条款更新、Loblaw×Muse、印度反诈微短剧等产品/地区新闻。

---

##### Microsoft Research

**源查证**: [microsoft.com 来源](https://www.microsoft.com/en-us/research/feed/)（Chrome UA，200；feed 仍只展示约 10 条，最新仍是上期已报的 TokenEconomizer 与 11-18 00:52 Asia/Singapore 的健康播客）。已用博客首页与 page/2 交叉。

窗内**无新研究博文**（非缺访问）。博客列表可见最新研究长文日期为 November 16, 2026（TokenEconomizer，上期已报）。

---

##### NVIDIA

**源查证**: [blogs.nvidia.com 来源](https://blogs.nvidia.com/feed/)（200，18 条）、[developer.nvidia.com 来源](https://developer.nvidia.com/blog/feed/)（Atom，200，100 条）；[blogs.nvidia.com 来源](https://blogs.nvidia.com/) 与 [research.nvidia.com 来源](https://research.nvidia.com/)（200）。开发者博客条目日期以 Atom `<published>` 为准。

**窗内开发者 / 博客（工程为主，不挤研究主包）**:
- [Reducing Rollout Bottlenecks in Reinforcement Learning with NVIDIA Dynamo](https://developer.nvidia.com/blog/reducing-rollout-bottlenecks-in-reinforcement-learning-with-nvidia-dynamo/)（`2026-11-19T20:28:13Z` → **11-20 04:28 Asia/Singapore**）：用 Dynamo 路由与 ModelExpress / 增量权重传输减轻 RL rollout 等待。
- [Enabling Real-Time AI for Scientific Instruments with GPU-Native Data Acquisition](https://developer.nvidia.com/blog/enabling-real-time-ai-for-scientific-instruments-with-gpu-native-data-acquisition/)（**11-20 01:00 Asia/Singapore**）。
- [Build Tool-Calling Parsers in Rust with AI Agents](https://developer.nvidia.com/blog/build-tool-calling-parsers-in-rust-with-ai-agents/)（**11-20 00:30 Asia/Singapore**）。
- [Build Training-Ready Physical AI Datasets with Two Prompts in NVIDIA Cosmos](https://developer.nvidia.com/blog/build-training-ready-physical-ai-datasets-with-two-prompts-in-nvidia-cosmos/)（**11-19 01:00 Asia/Singapore**）。
- [Tackling GPU Bottlenecks in Plane-Wave DFT with K-Point Batching and Mixed Precision](https://developer.nvidia.com/blog/tackling-gpu-bottlenecks-in-plane-wave-dft-with-k-point-batching-and-mixed-precision/)（**11-18 23:00 Asia/Singapore**）。
- [NVIDIA and Microsoft Expand Accelerated Computing From Azure to Windows PCs](https://blogs.nvidia.com/blog/microsoft-ignite-accelerated-computing-azure-windows-pcs/)（**11-20 04:00 Asia/Singapore**）：Ignite 产品合作。另有 Omniverse 开发者故事、GeForce NOW 促销、RTX Spark 桌面上市等。

上期已报的 MLPerf / Vera Rubin / cuPotential / 稀疏注意力等，发布时间在 11-18 09:09 之前或更早，不当本期新发。本窗未见新的基础模型技术报告。

---

##### Apple

**源查证（成功）**: 主页 RSS [machinelearning.apple.com 来源](https://machinelearning.apple.com/rss.xml)（200，仍只有 10 条，**不可作完整性依据**）；[machinelearning.apple.com 来源](https://machinelearning.apple.com/research) 全列表 `__NEXT_DATA__` **1194** 条（上期记录 1192 条）。本机上期 next-data 缓存为空，未能做 slug 逐条对账。

###### 7) Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth — **建议备选（官方视觉模型，兼本期 arXiv）**
- **日期**: RSS / 页面 `Fri, 20 Nov 2026 00:00:00 GMT` → **2026-11-20 08:00 Asia/Singapore**（来源记录，Apple 常见日级 00:00 GMT，精确时刻待核）。页面 `published` 字段 **2026-11-20**。
- **URL**: [machinelearning.apple.com 来源](https://machinelearning.apple.com/research/depth-pro-2-monocular)
- **arXiv**: [2611.26603](https://arxiv.org/abs/2611.26603)（API published `2026-11-19T18:55:41Z` → 11-20 02:55 Asia/Singapore；**Asia/Singapore 归属 11/20**，主类 cs.CV，兼 cs.LG）
- **代码 / 项目**: [GitHub apple-aiml-research/ml-depth-pro-2](https://github.com/apple-aiml-research/ml-depth-pro-2) · [apple-aiml-research.github.io 来源](https://apple-aiml-research.github.io/ml-depth-pro-2/)
- **机构证据**: PDF 首页单位行「Apple」；作者 Peiyun Hu, Marko Mihajlovic, Lyndon Duong, Lahav Lipson, Wei Dong, Amaël Delaunoy, Stephan R. Richter, Vladlen Koltun（来源记录）。
- **人话**: 一个网络同时处理单张图和视频，想同时保住度量尺度、边缘锐利和时间一致性；并放出 24M 到 872M 一簇模型。
- **要点**（作者/官方自报）: 训练 1–32 帧片段，混合图像、视频与多视图数据；在焦距未知时用轻量焦距估计器，文称 1080p 在 B200 上 **118 fps**，且比先前估计器更准。称在锐度、时间一致性与度量精度上均优于先前单帧/多帧方法。代码与权重已发布。
- **标注**: 来源记录 / 作者自报 / 官方页面。不是 agent 主线，故未进研究主包。

按 `published` 日期，2026-11-17 及以后只有这一条。上期已报的 Split-and-Scale（11-16）及 11-10/12 补录不再重复。

---

##### Amazon Science

**源查证**: [amazon.science 来源](https://www.amazon.science/index.rss)（200，25 条）；站点首页 200。备用 `/blog/feed` 为 404，完整性以 index.rss 为准。

###### 8) Mathematical proof, powered by AI. And no hallucinations! — **可作对照（工具发布，非新基准）**
- **日期**: RSS `Wed, 18 Nov 2026 18:55:35 GMT` → **2026-11-19 02:55 Asia/Singapore**（来源记录）
- **URL**: [amazon.science 来源](https://www.amazon.science/blog/mathematical-proof-powered-by-ai-and-no-hallucinations)
- **作者**: Hanno Becker, Larry Paulson
- **人话**: AWS 在 AutoCorrode 套件中公开 I/Q、I/R 和 Isabelle Assistant，经 MCP 把智能体接到 Isabelle，边写边检查形式化证明。
- **要点**（官方自报）: 示例为 √2 无理、N 个连续合数、sin x 定积分等经典命题，由 Claude Opus 4.6 在 Isabelle Assistant 中写出可读、可检查的证明；文中还提到模型纠正了作者故意不完整的合数证明。工具链接指向 [GitHub awslabs/AutoCorrode](https://github.com/awslabs/AutoCorrode) 。这是工具与工作流介绍，不是大规模自动形式化评测。
- **标注**: 来源记录 / 官方自报。

---

##### Thinking Machines Lab

**源查证**: [thinkingmachines.ai 来源](https://thinkingmachines.ai/blog/) 与 `/news/`（均 200）。博客 RSS 备用地址 404，完整性以页面为准。博客列表最新长文仍是上期已报的端到端 4-bit 训练（列表可见 2026-11-13）。

###### 9) Introducing Inkling 2 Mini — **建议进主包（开源权重小模型）**
- **日期**: 页面 `datePublished` `2026-11-20T00:00:00+00:00` → **2026-11-20 08:00 Asia/Singapore**（官方元数据，来源记录）；新闻列表标 Nov 20, 2026。**00:00 UTC 可能为日级占位，精确时刻待核**。另见 `dateModified` 含 `2026-11-20T14:37:41`。
- **URL**: [thinkingmachines.ai 来源](https://thinkingmachines.ai/news/inkling-2-mini/)
- **权重 / 卡**: [HF thinkingmachines/Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini) · [thinkingmachines.ai 来源](https://thinkingmachines.ai/model-card/inkling-2-mini/) · 可变循环变体 [thinkingmachines.ai 来源](https://thinkingmachines.ai/model-card/tml-d24-varloop-research/) · HF `thinkingmachines/TML-d24-varloop-research`
- **人话**: 26.4B 总参数、约 20GB 内存的 looped MoE，可在笔记本上跑，主打长程 agent 编程，并把循环深度对可监控性的影响单独做了实验。
- **要点**（官方自报，须带对照口径与 harness）: 见主包。主比较是「总参数 <100B 的开源权重模型」；表内 Nemotron 3.5 Super VL（12.0/124.5B）不在该口径内。解码速度为 614 GB/s、BF16、bs=1 的理论上限。
- **标注**: 来源记录 / 官方自报。安全与破坏类测试只记结论。

---

##### 其他实验室

未把缺访问写成无更新。本窗已成功访问且无新研究长文的还有：OpenAI Alignment、Anthropic Alignment、MSR 研究博客（见上）。未单开 sto 的实验室若仅有产品或转载，不在此展开。

---

##### 采集说明

**窗口内建议进主包**: Gemini 4 Neon；Inkling 2 Mini；OpenAI jagged frontier；OpenAI MedChemBench。
**强候选**: OpenAI 对抗蒸馏方法文（仅高层）。
**产品 / 工程 / 对照**: Genie 4 对 Ultra 开放与 API 短讯、Gemini Tool Retrieval、Apple Depth Pro 2、Amazon AutoCorrode、Google 量子两则、Meta 工程两则、NVIDIA Dynamo 等、Anthropic IPO 公告。
**明确排除**: GPT‑6.2 及上期已报各条；OpenAI chip design（11-18 08:00 Asia/Singapore，窗前）；Anthropic 黑洞物理文（11-17）；Apple 11-16 及更早条目。

**检索覆盖与失败**
- 成功：OpenAI News RSS（1421）+ `/news` 与 `/news/research/`（200）+ Alignment 列表/RSS + 发布文/PDF；Anthropic research/news/engineering/alignment（curl）；DeepMind RSS + blog.google 主 RSS 与分类 RSS + Neon 模型卡 PDF；Google Research RSS；MSR feed 与博客列表（含 page/2）；NVIDIA 双 feed（Atom/RSS）及 Dynamo 等正文；Meta research / about.fb feed / engineering feed；Thinking Machines 博客与新闻页及 Inkling 正文；Amazon Science index.rss 与证明文正文；Apple 主页、/research 全列表（__NEXT_DATA__ 1194 条）、RSS、详情页与 arXiv/项目页。
- 降级：blog.google 主 RSS 只有 20 条，最旧约 11-19 01:00 Asia/Singapore；已用分类 RSS 与 DeepMind RSS 补扫。Apple RSS 只有 10 条，完整性以 /research 全列表为准；上期 next-data 缓存缺失，slug 对账不完整。Neon 完整安全报告未上线。MedChemBench PDF 未逐表深读。Anthropic、Apple、Inkling 部分日期为日级或 00:00 UTC，时刻待核。
- 失败/不完整：无「写成无更新」的缺访问。上期 Antigravity `/teamwork` 子结果仍未在本任务中逐篇复核。
- 未把缺访问写成无更新。第三方转述数字无官博原文则不收。

### arXiv 原始候选

#### arXiv raw pack: cs.AI / cs.CL / cs.LG（扫描窗口 2026-11-18 09:09 Asia/Singapore → 2026-11-21 ~09:01 Asia/Singapore）


核验方式：真实访问 `arxiv.org/list/cs.{AI,CL,LG}/{new,pastweek}`、`arxiv.org/catchup/cs/YYYY-MM-DD`、`/abs/`、`/html/`、`/pdf/` 首页，以及 [Availability of submissions](https://info.arxiv.org/help/availability.html) 假期表与 [localtime](https://arxiv.org/localtime)；HTTPS `export.arxiv.org/api`。数字默认摘自摘要，必要时用 PDF/HTML 正文核对，标 **作者自报**；机构只以 HTML `Affiliation` / PDF 首页（含脚注、通讯邮箱）为准，**不以题目或摘要里出现的模型名、硬件名为机构**。提交日多在美东或更早；**Asia/Singapore 归属按 listing/放批日**，不按 Submitted on 字面。本窗 HTML 机构栏多数转成残缺的 `Affiliation:`，已改用 **PDF 首页**（来源记录）。

上期主包已报勿重复：2611.21003 K2-Horizon、2611.20771 Nemotron 3.5 Bolt E4B、2611.19700 test-time adaptation、2611.17880 Soteria、2611.20144 HEAMS；备选 2611.21072 Sage S2.1 Flash 等亦不作新条目。更早已报 ID 已对照避开。本期扫描宇宙全部 ≥2611.21612（上期探测为周三批正在放出、列表未齐的起点），与上期已报 ID 无交集。

##### 假期与日程（本窗无额外推迟）

官方假期表 2026 年 11 月条目仅有 **Wednesday 2026-11-11**（Veterans Day，已在更早期处理）与 **Thursday 2026-11-26**（Thanksgiving，尚未到）。本窗 11/18–11/21 **无额外假期、无官方延期公告**（来源记录，availability.html 2026 Holidays + localtime）。常规日程：美东 **Sun–Thu 20:00** 放批（11 月为 EST）→ 新加坡约 **Mon–Fri 09:00** 可见；**无周六、周日批**。因此：

- 周二 11/17 20:00 ET 公告 → listing 日期 **Wed, 18 Nov 2026**（Asia/Singapore 11/18 早批；上期截止时列表未齐，本期补全）
- 周三 11/18 20:00 ET 公告 → listing 日期 **Thu, 19 Nov 2026**（Asia/Singapore 11/19 早批）
- 周四 11/19 20:00 ET 公告 → listing 日期 **Fri, 20 Nov 2026**（Asia/Singapore 11/20 早批）
- 周五、周六无公告 → catchup **Sat, 21 Nov 2026** 为 0 条（来源记录）

采集时 arXiv localtime 为 **Fri, 20 Nov 2026 19:51 EST**；下一提交截止为周一 14:00 EST，下一次新稿公告最早为周一 20:00 EST（周二 09:00 Asia/Singapore 那批）。

##### Batch map（日期为 Asia/Singapore 放批早间 / listing 标签日）

| Asia/Singapore 批次 | listing 标签 | cs 全集 catchup（新稿 / 交叉 / 替换） | 全站新号范围 | 状态 |
|---|---|---|---|---|
| 11/18 (Wed) | Wed, 18 Nov 2026；CS catchup Total **1341** | 新稿 **798/798**，交叉 **62/62**，替换 **481/481** | **2611.21612 – 2611.23232**（CS 新稿首条 21612、末条 **23229**；abs 探测 **23230–23232 = 200**，主类分别为 math.DS、hep-th、cond-mat.supr-con，**不在**本三科） | **列表完整**（showing N of N） |
| 11/19 (Thu) | Thu, 19 Nov 2026；CS catchup Total **1371** | 新稿 **839/839**，交叉 **71/71**，替换 **461/461** | **2611.23233 – 2611.24942**（CS 新稿首条 23233、末条 **24941**；abs 探测 **24942 = 200**，主类 math.FA，**不在**本三科） | **列表完整** |
| 11/20 (Fri) | Fri, 20 Nov 2026；`/new` 横幅为 Friday, 20 November 2026；CS catchup Total **1382** | 新稿 **822/822**，交叉 **70/70**，替换 **490/490** | **2611.24943 – 2611.26629**（CS 新稿首条 24943、末条 **26629**；abs 探测 **26630–26654 = 404**，确认全站上沿为 **26629**） | **列表完整**。`/new`：AI 400 条（新稿 109/109）、CL 161（64/64）、LG 359（119/119） |
| 11/21 (Sat) | catchup “Sat, 21 Nov 2026，Total of 0 entries / No updates” | — | — | **无新批**（常规日程） |

说明：

- pastweek（showing N of N）：AI **1333/1333**（分段 252、230、259、428、164，后两段与上期周二/周一吻合）、CL **568/568**（96、72、102、236、62）、LG **1263/1263**（213、218、211、461、160）。
- 扫描宇宙（本期新看的周三+周四+周五新稿+交叉，已去掉替换稿与上期已报，且 ID ≥2611.21612、科目含 cs.AI/CL/LG）：**1293** 篇（按批：18 新稿 401 + 交叉 29；19 新稿 372 + 交叉 34；20 新稿 417 + 交叉 40）。标题/摘要关键词粗筛后，对 **14** 篇做了 abs + HTML + API + PDF 首页核验。
- 替换稿未计入「新发现」宇宙，也未当新条目精读。
- 机构：多数 HTML 把 `\affiliation` 转成残缺的 `Affiliation:`，已改用 **PDF 首页**（来源记录）。2611.22161 是 Surge AI 对 NVIDIA 模型的后训练，**不要**写成 NVIDIA 论文。
- 本窗截止约 **09:01 Asia/Singapore**。全站已放出新号上沿 **2611.26629**。

##### Candidates（单位经 arXiv HTML / PDF 首页核实；数字来自摘要除非另注）

###### 真重点

1. **2611.26358** Beam Model Technical Report  
   链接：[arXiv 2611.26358](https://arxiv.org/abs/2611.26358)  
   提交/公布：API published 2026-11-19T16:28:23Z → 2026-11-20 00:28 Asia/Singapore；**Asia/Singapore 归属 11/20**（Fri 新稿，主类 cs.CL；兼 cs.AI）  
   机构证据：PDF 首页「Reflection Team」、通讯 `（机构署名邮箱略）`（来源记录）。文中 GLM-5.2、Qwen 3.8-Max、NVIDIA GB300、DFlash 等是对照、硬件或解码组件，**不是**作者单位。API 作者栏以 “Reflection Team” 领衔（230 名）。  
   人话：Reflection 的第一款开源权重模型，501.3B 总参数、23.4B 激活的稀疏 MoE，对准编程、推理和 agent，并写了从预训练到服务的完整报告。  
   为何重要：本窗体量最大的开源模型技术报告；预训练 23.8T token、1M 上下文，以及作者所称「开放实验室迄今最大规模之一」的异步 RL。  
   对谁有用/深读：开源 MoE、长上下文 midtraining、大规模 RL 后训练、投机解码（DFlash 2）、开放权重安全框架。  
   主要数字与条件/局限（作者自报）：总参数 **501.3B** / 激活 **23.4B**，52 层、256 专家、每 token 激活 8 专家，词表约 152K，上下文 **1M** token。预训练 **23.8T** token；在 **6,144** 块 GB300 上不到四周，后期 goodput **92.3%**、稳态 MFU **21%**（已计重启）。后训练异步 RL：超过 **100M** 条 rollout，**10.5K** 块 GB300，四周；评测集上「随 RL 算力增加仍未见平台」。作者称推理算力约为「同类许多模型」的 **1/3 到 1/4**，并与 GLM-5.2、Qwen 3.8-Max（LongBench-v2）对照，不能改写成无条件 SOTA。服务侧有 FP8/NVFP4 与 **1.93B** 的 DFlash 2 草稿器。安全仅结论：Open Safety Framework 下生物武器、化学武器、失控、网络攻击四类均为 **Limited**；内部 ISE 上有害请求拒绝/转向 **88.9%**、无害请求遵从 **81.5%**。对齐教师从 100B 扩到 501B 后误拒下降 **48.7%**。摘要未列 SWE-bench 等绝对分。  
   标签：**真重点** · 来源记录 / 作者自报

2. **2611.25673** CompAct-Bench: A Benchmark for Working-Context Compaction in Long-Horizon Agent Tasks  
   链接：[arXiv 2611.25673](https://arxiv.org/abs/2611.25673)  
   提交/公布：API published 2026-11-19T07:49:37Z → 2026-11-19 15:49 Asia/Singapore；**Asia/Singapore 归属 11/20**（Fri 新稿，主类 cs.AI）  
   机构证据：PDF 首页「1 Fudan University 2 Hunyuan Team, Tencent 3 SIGS, Tsinghua University」，通讯 `（机构署名邮箱略）`、`（机构署名邮箱略）`（来源记录）。应写成 **复旦大学 + 腾讯混元（Maxm Pan）+ 清华深圳国际研究生院**。  
   人话：把「把历史压短再继续执行」从实现细节里抽出来，单独打成分数。  
   为何重要：长程 agent 几乎都要做上下文压缩，但这篇表明：压缩前能做完的任务，压完之后平均只剩一半出头。  
   对谁有用/深读：上下文压缩、handoff、工作记忆、长程 agent 评测设计。  
   主要数字与条件/局限（作者自报）：**200** 项过程级任务（BrowseComp、SWE-bench、内部 CompanyBench）。在中间边界压缩，固定执行器按匹配动作预算续跑。评估 **12** 个前沿模型作压缩器。入选任务在压缩前三次预筛中全部做成，压缩后平均准确率 **56.7%**，最好的模型也只有 **68.5%**（摘要未点名该模型，勿补）。失败概括为漏信息导致重复劳动/预算耗尽，以及状态被写歪后过早结束。数字绑定该执行器协议，不能外推到其他压缩实现。  
   标签：**真重点** · 来源记录 / 作者自报

3. **2611.25123** Forget Freely, Grep Later: Lossless, Index-Free Memory for Long-Horizon LLM Agents  
   链接：[arXiv 2611.25123](https://arxiv.org/abs/2611.25123)  
   提交/公布：API published 2026-11-18T20:02:57Z → 2026-11-19 04:02 Asia/Singapore；**Asia/Singapore 归属 11/20**（Fri 新稿，主类 cs.CL；兼 cs.AI）  
   机构证据：PDF 首页「University of Southern California」，通讯 （机构署名邮箱略）（来源记录）。Qwen3.5-9B 是被训练和评测的底座，不是作者单位。  
   人话：不先决定该记什么，而是把完整历史追加成纯文本日志，用正则搜索按需召回（GrepMem）。  
   为何重要：给结构化记忆和有损摘要提供一个很简单的无损基线；和本期 CompAct-Bench、上期 HEAMS 适合配读。  
   对谁有用/深读：agent 记忆、上下文管理、可验证奖励 RL。  
   主要数字与条件/局限（作者自报）：在五种上下文管理策略下用 RL 训练 Qwen3.5-9B。ContextBench 准确率 **95–97%**，有损基线最高 **21%**；BCP-Multi 上比 SUPO 摘要法高 **8.8** 个百分点。作者称五个任务都还留在准确率–token 成本的 Pareto 前沿。不能直接说 grep 已经替代结构化记忆。  
   标签：**真重点** · 来源记录 / 作者自报

4. **2611.22971** SEAM: Computer-Use Agents Know the Harm Between Screens, and Commit It Anyway  
   链接：[arXiv 2611.22971](https://arxiv.org/abs/2611.22971) · 项目 [yuxuan2003.github.io 来源](https://yuxuan2003.github.io/SEAM/)  
   提交/公布：API published 2026-11-17T15:53:58Z → 2026-11-17 23:53 Asia/Singapore；**Asia/Singapore 归属 11/18**（Wed 新稿，主类 cs.CR；兼 cs.AI）  
   机构证据：PDF 首页「Tsinghua University The Chinese University of Hong Kong ByteDance Shenzhen University」，通讯 `（机构署名邮箱略）`（来源记录）。**多机构合作**，不要写成单一的清华或 ByteDance 论文。  
   人话：测计算机使用智能体在「指令和每一屏单独看都无害，组合起来才有害」时，还会不会把动作做完。  
   为何重要：指出安全识别并不稳定地转化成安全执行，而且更取决于信息出现在用户指令里还是屏幕上。  
   对谁有用/深读：计算机使用 agent 安全评测、跨应用工作流、拒答与执行落差。  
   主要数字与条件/局限（作者自报，仅高层结论）：**600** 项跨应用、多步 OSWorld 任务。开源权重与旗舰智能体在最多 **92%** 的运行里仍会执行该组合危害，但用户若用一句话直接说出同一危害则会拒绝。作者称专有模型明显更谨慎。暴露本身不是主要瓶颈。只写结论，不写任务构造或利用步骤。  
   标签：**真重点** · 来源记录 / 作者自报

5. **2611.21832** Auditors Struggle to Catch Sabotage In End-to-End Transcripts of AI Safety Research  
   链接：[arXiv 2611.21832](https://arxiv.org/abs/2611.21832)  
   提交/公布：API published 2026-11-16T19:52:38Z；PDF 页眉 v2（18 Nov 2026）；**Asia/Singapore 归属 11/18**（Wed 新稿，主类 cs.AI）  
   机构证据：PDF 脚注「1 Redwood Research。2 Georgia Institute of Technology。…… Independent。4 Equistamp」，通讯 `（机构署名邮箱略）`（来源记录）。Keshav Shenoy、Eric Gan、Sebastian Prasanna、Julian Stastny、Vivek Hebbar = Redwood Research；Anthony Zang = Georgia Institute of Technology；Jacqueline Tay = Independent；Amy Ngo = Equistamp。应写成 **Redwood Research + Georgia Institute of Technology + Independent + Equistamp**。  
   人话：用人类专家做代理，压力测试「安全研究本身会不会被破坏、审计能不能从完整记录里看出来」。  
   为何重要：和本期 OpenAI 研究加速报告同一主题的另一面——智能体越深地进入研发，现有审计并不乐观。  
   对谁有用/深读：研发过程审计、RSI / 研究破坏控制、安全研究记录设计。  
   主要数字与条件/局限（作者自报，仅高层）：10 项新的安全研究实验，10 条良性与 12 条被破坏记录。人类审计人员在能看完整记录并复跑实验的条件下，AUROC **0.59**（与随机无显著差异），只有 **17%** 的案例完全找出具体破坏。摘要另写：在**不允许**复跑实验的条件下，前沿模型可能高于人类（Fable 5.1：AUROC **0.73**，完全识别 **32%**）——与人类协议不同，不能合成「模型已经比人会审计」。小样本、人工代理破坏的压力测试，不是对线上系统已被破坏的判断。不写破坏手法。  
   标签：**真重点** · 来源记录 / 作者自报

###### 备选

6. **2611.24636** Clover-35B-A3B-Preview Technical Report  
   链接：[arXiv 2611.24636](https://arxiv.org/abs/2611.24636) · 代码 [GitHub DiffuSpace/Clover-35B-A3B-Preview](https://github.com/DiffuSpace/Clover-35B-A3B-Preview) · 权重 [HF Diffuspace/Clover-35B-A3B-Preview](https://huggingface.co/Diffuspace/Clover-35B-A3B-Preview)  
   提交/公布：API published 2026-11-18T15:46:14Z → 2026-11-18 23:46 Asia/Singapore；**Asia/Singapore 归属 11/19**（Thu 新稿，主类 cs.CL）  
   机构证据：PDF 首页「DiffuSpace Technical Team」、站点 diffuspace.ai，通讯邮箱为 `@diffuspace.ai`（来源记录）。不要写成其他大厂论文。  
   人话：35B 总参数、3B 激活的混合专家扩散语言模型，带 thinking mode，主打 agent 与高速生成。  
   为何重要：本窗另一份开源 agent 向技术报告，SWE / Terminal 数字比较具体；但机构体量小于 Beam，适合作为对照而不是唯一主条。  
   主要数字与条件/局限（作者自报）：称在所评的七项 agent 指标上领先，包括 SWE-bench Verified **73.6**、Terminal-Bench 2.1 **51.7**。内部工作负载、1×NVIDIA GB300、BF16、batch size 1 下生成约 **680** token/s。决策模型变体在内部 500 组问题上，问题准确率 **90.37%→93.88%**，整组全对 **65.4%→77.0%**。数字不能与 Beam 或 Gemini 4 无条件横比。  
   标签：**备选偏强** · 来源记录 / 作者自报

7. **2611.22161** What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super  
   链接：[arXiv 2611.22161](https://arxiv.org/abs/2611.22161)  
   提交/公布：API published 2026-11-17T03:48:06Z → 2026-11-17 11:48 Asia/Singapore；**Asia/Singapore 归属 11/18**（Wed 新稿，主类 cs.LG）  
   机构证据：PDF 首页「Surge AI」，通讯 `（机构署名邮箱略）`（来源记录）。**不是** NVIDIA 官方论文；Nemotron 3.5 Super 是被后训练的底座。训练在 Tinker 上进行，Thinking Machines 也不是作者单位。  
   人话：Surge AI 用五份专家任务数据，分别给 Nemotron 3.5 Super 训 rank-32 LoRA（CISPO，无监督阶段），看分任务 RL 能补上哪些失败模式。  
   主要数字与条件/局限（作者自报）：底座 120B 总 / 12B 激活。十二项头条基准上，增益从 IFBench **+4.5** 到 GDP.pdf **10.4%→24.2%**（**+13.8**）；SWE-bench Pro V2 **86.9%→92.1%**，Terminal-Bench 2.1 **63.9%→70.3%**，MultiChallenge **58.3%→66.6%**，AutomationBench **14.8%→27.5%**，Chartography **39.4%→50.6%**。其中八项由其他机构构建、四项由 Surge AI 构建。这是该底座、这些 adapter 与 harness 上的头对头，不能写成 NVIDIA 官方后训练结果。  
   标签：**备选** · 来源记录 / 作者自报

8. **2611.26248** TwinLab-Bench: Evaluating AI Scientists in Agentic Twins of Real Labs  
   链接：[arXiv 2611.26248](https://arxiv.org/abs/2611.26248) · 项目 [twinlab-bench.github.io 来源](https://twinlab-bench.github.io/)  
   提交/公布：API published 2026-11-19T15:25:34Z → 2026-11-19 23:25 Asia/Singapore；**Asia/Singapore 归属 11/20**（Fri 新稿，主类 cs.AI）  
   机构证据：PDF 首页「Zhejiang University」（来源记录）。应写成 **浙江大学**。  
   人话：在 52 项来自真实实验室记录的孪生任务上，让智能体自己设计实验，再与隐藏的真实结果对照。  
   主要数字与条件/局限（作者自报，仅高层）：52 项任务，覆盖物理、生命科学与工程；作者注释列出 13 个智能体，最强为 Claude Fable 5.2 **45.0**，另有 Opus 5.5 **40.2**、GPT-6.1-sol **31.7** 等。这些任务对前沿模型仍然很难。不写实验操作或湿实验步骤。  
   标签：**备选** · 来源记录 / 作者自报

9. **2611.21646** Limite 1B - Violetto: Technical Report  
   链接：[arXiv 2611.21646](https://arxiv.org/abs/2611.21646) · 代码 [GitHub paradigma-inc/limite-violetto](https://github.com/paradigma-inc/limite-violetto) · 博客 [paradigma.inc 来源](https://paradigma.inc/blog/limite-1b-violetto/)  
   提交/公布：API published 2026-10-14T13:49:22Z（提交较早）；**Asia/Singapore 归属 11/18**（Wed 新稿，主类 cs.CL）  
   机构证据：PDF 首页「Paradigma」，通讯 `（机构署名邮箱略）`（来源记录）。  
   人话：从零训一个 10 亿参数、面向高吞吐数学推理的专用模型，并开源权重与服务代码（Apache 2.0）。  
   主要数字与条件/局限（作者自报）：预训练 **2370 亿** token，上下文最长 **131k**。AIME 2026 **94.01%**，BeyondAIME **74.25%**；作者估计训练计算约 **1.71×10²¹** FLOPs，并在图中与更大模型对照。模型只做了轻度指令微调，定位是单轮数学求解器，不是通用助手。提交于 10 月，本周才放批。  
   标签：**备选** · 来源记录 / 作者自报

10. **2611.26603** Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth  
    链接：[arXiv 2611.26603](https://arxiv.org/abs/2611.26603) · 项目 [apple-aiml-research.github.io 来源](https://apple-aiml-research.github.io/ml-depth-pro-2/) · 代码 [GitHub apple-aiml-research/ml-depth-pro-2](https://github.com/apple-aiml-research/ml-depth-pro-2)  
    提交/公布：API published 2026-11-19T18:55:41Z → 2026-11-20 02:55 Asia/Singapore；**Asia/Singapore 归属 11/20**（Fri 新稿，主类 cs.CV；兼 cs.LG）  
    机构证据：PDF 首页单位行「Apple」（来源记录）。与 Apple ML 站点同日条目对应。  
    人话：一个网络同时处理图像和视频，想同时保住度量尺度、边缘锐利和时间一致性，并放出 24M–872M 一簇模型。  
    主要数字与条件/局限（作者自报）：称在锐度、时间一致性与度量精度上均优于先前单帧/多帧方法。焦距估计器称 1080p 在 B200 上 **118 fps**。视觉基础模型，不是 agent 主线；官博侧已作备选记录。  
    标签：**备选（与官博对照）** · 来源记录 / 作者自报

11. **2611.22777** CrossEnv: Synthesizing Verifiable Cross-Environment Tasks for Long-Horizon Agent Training  
    链接：[arXiv 2611.22777](https://arxiv.org/abs/2611.22777)  
    提交/公布：API published 2026-11-17T13:44:28Z → 2026-11-17 21:44 Asia/Singapore；**Asia/Singapore 归属 11/18**（Wed 新稿，主类 cs.AI）  
    机构证据：PDF 首页「Beijing Institute of Technology」「Alibaba Group」「Beijing University of Posts and Telecommunications」（来源记录）。**多机构合作**。  
    人话：为长程智能体训练合成可验证的跨环境任务，而不是只在单一环境里刷分。  
    标签：**备选** · 来源记录 / 作者自报

另看过但未展开：2611.24540（JPMorgan Chase LLM Suite Team 的小模型因子实验，PDF 声明不是研究部产品）；2611.25257 Keel（UIUC + NYU + CMU + Yale，用前沿模型改 VLM 权重以减少循环）；2611.25403 Antom 支付基础模型（Ant International 内部数据，领域过窄）。

##### 完整性与续扫

| 项目 | 结论 |
|---|---|
| 11/18 (Wed) 列表 | **完整**（CS catchup 新稿 798/798、交叉 62/62、替换 481/481）。上期截止时该批列表未齐，本期已补全 |
| 11/19 (Thu) 列表 | **完整**（新稿 839/839、交叉 71/71、替换 461/461） |
| 11/20 (Fri) 列表 | **完整**（新稿 822/822、交叉 70/70、替换 490/490；`/new` 与 pastweek 均为 showing N of N） |
| 11/21 (Sat) 列表 | **无新批**（catchup 0 条，符合常规日程） |
| 全站新号衔接 | 上期周二批止于 **2611.21611**；本窗周三自 **21612** 起、止于 **23232**；周四自 **23233** 起、止于 **24942**；周五自 **24943** 起、止于 **26629**（26630+ = 404） |
| 替换稿 | 未当作新条目系统精读 |
| 续扫起点 | **2611.26630** + 下周一 `list/*/new` 与 `/catchup/cs/2026-11-23`（对应周一 20:00 EST 公告，Asia/Singapore 11/24 早批；11/22 周日无批） |


## X 公开动态

### 动态与跟踪

#### X/AI 源包 · 2026-11-21（三日合并）

窗口：2026-11-18 09:09 → 2026-11-21 约 08:50 Asia/Singapore。来源：
- 首页时间线 5 页，约 479 条（98+100+92+94+95，已过滤回复）。实际覆盖约 11-20 05:02 → 11-21 08:48 Asia/Singapore；窗口前约 44 小时靠公开检索与 Today's News 补齐。
- 官方/关键账号合并检索：OpenAI/OpenAIDevs/thsottiaux/AnthropicAI/claudeai/ClaudeDevs/ArtificialAnlys/cursor_ai/GoogleDeepMind/GoogleAI/GeminiApp/Alibaba_Qwen/dotey 一组（5 页后 result_count=0）；另补 GoogleAIStudio/googledevs/PaloAltoNtwks 一组（收束到关键产品帖）。均 `-is:retweet -is:reply`，未包含 `from:grok`，未传 `end_time`。
- 定向检索与交叉核对：Anthropic 定价新闻稿、SEC EDGAR 公司页（CIK 0002130357，带 User-Agent）及 424B4（0001628280-26-074944）、Nasdaq 新闻室、Yahoo Finance 历史行情、CNBC / Reuters 转载对首日与次日收盘的报道；Gemini 4 Neon / Project Genie / Genie 4 API / Tool Retrieval 官方博文；OpenAI 芯片设计、研究加速、对抗蒸馏、MedChemBench、Performance Factory 博文与 GPT-Live-1.1 文档；Palo Alto Networks 收购公告。
- 可复用但均本期重核：11-19 个人早报素材、11-20 早报素材。采集时 （内部证据存档） 下尚无 11-21 09:00 早报。
- X Today's News：约 72h 一组（摘要≠来源记录）。

本期 X 侧无 429。官方主检索末页 result_count=0，窗口内该组已收束。openai.com / anthropic.com / blog.google 博文本次 WebFetch 成功。未用浏览器绕过任何封锁。旧包与早报数字均本期重核，不以旧稿为事实源。

去重说明：上期主条（GPT‑6.2 Astra/Sol 正式发布、S-1/A-3 仍未定价、Qwen4-Max、学术研究者计划、Claude Code Mode / Linked billing）不重写为新主条。GPT‑6.2 官宣在 11-18 01:54 Asia/Singapore，早于本窗口起点，只把窗口内的后续产品与研究写入进展或并列主条。本期主条从「已定价并开始交易」写起。

##### 主条目

###### 1. Anthropic 定价 $83、发行 9.80 亿股、规模 $813.4 亿，ANT 完成首两日交易
上期写到 11-17 S-1/A 与 8-A12B 时，发行价仍是 $70–78 的待定区间，采集时尚未定价、尚未上市。本窗口有公司新闻稿、@AnthropicAI 主帖和 424B4，可以把最终发行条款写成已披露事实；首两日行情则用 Nasdaq 新闻室与主流行情源交叉，不再只靠单一预测市场帖。
- **是什么**：
  - 定价（官方）：Anthropic, PBC 将 IPO 定价为每股 **$83.00**。发行 **980,000,000** 股 Class A 普通股，其中公司出售 956,351,354 股，出售股东出售 23,648,646 股；公司不会从出售股东的股票中获得任何所得。承销商有 30 天期权，可再向公司购买最多 **147,000,000** 股。424B4 封面价目表写明：公开发行总价 **$81,340,000,000**（即 9.80 亿股 × $83）；承销折扣合计 $550,000,000；扣除承销折扣后、费用前，公司所得 $78,840,438,875，出售股东所得 $1,949,565,525。这是**发行规模**，不是市值。
  - 上市安排（官方）：注册声明已于 11-18 被 SEC 宣布生效（EFFECT）。股票预计 11-19 起在 Nasdaq Global Select Market 以代号 **ANT** 交易；发行预计 11-20 交割，须满足惯例交割条件。@AnthropicAI 11-19 07:29 Asia/Singapore 发帖确认「定价 $83，预计明天开始在 Nasdaq 交易」，并链到新闻稿。最终招股书 424B4 已于 11-19 提交（登录号 0001628280-26-074944，Accepted 11-19 06:05:50 ET ≈ 11-19 19:05 Asia/Singapore）。截至采集时，SEC 公司页可见 424B4、S-1MEF、CERT、S-8 与 11-19 FWP，**未见交割 8-K**，故不把「已交割」写成已核事实。
  - 同期 Class N 私募（424B4 载明，有条件）：发行完成后、在满足若干条件的前提下，Google、NVIDIA、AMD、Broadcom、Micron、Microsoft 与 TSMC Partners 将按每股 $83 向公司购买合计 **$26.0 billion**、共 313,253,007 股 Class N：Google 与 NVIDIA 各约 $10.0B（各 120,481,927 股），AMD 约 $2.5B（30,120,481 股），Broadcom / Micron / Microsoft 各约 $1.0B（各 12,048,192 股），TSMC 约 $500 million（6,024,096 股）。私募所得全部归公司，不付承销折扣。招股书估计 IPO 与该私募合计净所得约 $104.8B（若绿鞋全部行使则约 $117.0B）。这不是二级市场成交，交割仍取决于发行完成等条件。
  - 首日交易（11-19，美东；开盘约 11-19 22:30 Asia/Singapore）：Nasdaq 新闻室写明开盘 **$111.50**。Yahoo Finance 历史行情：开 $111.50、高 $115.10、低 $92.72、收 **$97.17**，成交量 857,312,300。相对发行价 $83，开盘约 +34.3%，收盘约 +17%。CNBC 与 Reuters 报道同样给出开盘 $111.50、收盘 $97.17。不同行情源的成交量略有出入（CNBC 写逾 8.46 亿股），包中成交量以 Yahoo 历史表为准。
  - 次日交易（11-20，美东；常规收盘约 11-21 05:00 Asia/Singapore）：Yahoo Finance：开 $89.86、高 $92.56、低 $83.05、收 **$88.91**，成交量 399,629,474；相对首日收盘约 -8.50%，相对发行价仍约 +7.1%。Reuters 亦报道周五收于 $88.91。采集时已是周六上午，美股无常规交易；Yahoo 显示 11-20 盘后约 19:49 ET（≈ 11-21 08:49 Asia/Singapore）为 $88.69，只是盘后快照，不是正式收盘价。
  - 市值叙事（待核，不得与发行规模混用）：媒体与 Today's News 出现过定价时约 $1.5T、盘中一度约 $2T、首日收盘完全稀释约 $1.8T、以及预测市场/早报转述的约 $1.28T 等说法，分母与口径不一致。在公司未给出可核对的完全稀释股本、且未见交易所官方市值公告之前，这些数字一律标待核，也不在本包自行换算市值。此前有帖把募资规模写成约 $107.3B，与 424B4 的 $81.34B 公开发行总价不符，不能当 来源记录。
  - 公司侧叙事：CEO Dario Amodei 在开盘后发表 IPO 致辞（@AnthropicAI 11-20 01:01 Asia/Singapore）；Nasdaq 新闻室另引述了 Dario 与 Daniela Amodei 在开市铃仪式上的讲话。11-21 00:57 Asia/Singapore，@AnthropicAI 发布七位联合创始人讲述公司历程的视频。
- **为何重要**：这是窗口内最大的资本市场事件：最终发行价从 $70–78 上修到 $83，发行股数从招股阶段的 8.25 亿上修到 9.80 亿，公开发行总价达到 $813.4 亿。必须把「公司卖掉多少股票、拿到多少钱」和「二级市场愿意出什么价格、媒体怎么算市值」分开写。首日高开后回落到 $97.17、次日再收到 $88.91，说明上市本身已经完成，但定价之上的溢价在两天内明显收窄。
- **对谁·深读建议**：写发行条款只引用公司新闻稿和 424B4 价目表；写开盘价优先引用 Nasdaq 新闻室；写高低收与成交量用 Yahoo 等主流行情表，并注明来源。不要把 Polymarket 或 Today's News 的估值、募资总额直接写进 来源记录。若后续出现交割 8-K 或绿鞋行使公告，应另核净所得。
- **证据**：
  - 来源记录 / 官方自报：[@AnthropicAI 定价](https://x.com/AnthropicAI/status/2123196808675405860)、[公司新闻稿](https://www.anthropic.com/news/anthropic-prices-initial-public-offering)、[424B4 索引](https://www.sec.gov/Archives/edgar/data/2130357/000162828026074944/0001628280-26-074944-index.htm)、[SEC 公司页 CIK 0002130357](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002130357&type=&dateb=&owner=include&count=40)、[@AnthropicAI 致辞](https://x.com/AnthropicAI/status/2123461658890686863)、[@AnthropicAI 创始人视频](https://x.com/AnthropicAI/status/2123822989154369958)
  - 行情交叉（非公司文件）：[Nasdaq 新闻室（开盘 $111.50）](https://www.nasdaq.com/newsroom/anthropic-marks-ipo-at-nasdaq)、[Yahoo Finance 历史行情](https://finance.yahoo.com/quote/ANT/history/)、[CNBC 首日报道](https://www.cnbc.com/2026/11/19/anthropic-ipo-ant-live-updates.html)
- **约时**：新闻稿落款 11-18；X 定价帖 11-19 07:29 Asia/Singapore；424B4 接受于 11-19 19:05 Asia/Singapore；首日开盘约 11-19 22:30 Asia/Singapore；Dario 致辞 11-20 01:01 Asia/Singapore；次日常规收盘约 11-21 05:00 Asia/Singapore

###### 2. Google 正式发布 Gemini 4 Neon：官方价 $3/$15，AA Index 61（xhigh）排第三
Gemini 4 家族在上期已有 Carbon 与 Hydrogen。本窗口 Neon 以官方博文和多账号同步官宣落地，位置明确放在 Carbon 与 Hydrogen 之间，强调「前沿智力 + 更快做完复杂任务」，而不是再发一款更高价旗舰。
- **是什么**：
  - 官宣：@GoogleDeepMind 11-19 05:34 Asia/Singapore「Gemini 4 Neon is rolling out now」；@GoogleAI、@GeminiApp、@GoogleAIStudio、@googledevs 几乎同时转发。博文落款 11-18，作者 Koray Kavukcuoglu。
  - 定价与窗口（官方）：每百万 token **$3 输入 / $0.15 缓存输入（官方称 95% 折扣）/ $15 输出**，上下文 **1M** token。
  - 覆盖（官方）：即日起在 Gemini API（Google AI Studio 付费层）、Gemini for business、付费 Google AI Pro / Ultra 的 Antigravity 与 Gemini 应用中推出。网络安全向的 Neon for cyber 将在随后几天向 Fairwind Program 的受信任防守方开放。
  - 官方自报评测（非独立复测）：称在 Artificial Analysis Intelligence Index 的 xhigh 档得 **61、总排名第三**，位于更大、更慢的模型之后；Vals Index 第 2（70.9%）；官方还列举 Terminal-Bench 4.1 65.2%、FrontierCode 2.0（默认 high）46.2%、AA Coding Agent Index 58.6（第 1）等。@ArtificialAnlys 同日确认 Neon（xhigh）得分 61，并称相对 Carbon 任务成本约低 17%（AA 自报）。
  - 第三方产品接入（Cursor 自报）：@cursor_ai 11-19 07:35 Asia/Singapore 称 Neon 已在 Cursor 上线，默认 effort 在 CursorBench 4.1 得 **63.7%**，高于 Gemini 4 Hydrogen 的 57.3%；报价与官方一致为 $3 / $15。
- **为何重要**：Google 在约七周内连发 Gemini 4 家族多款模型，Neon 把「接近旗舰的智力」放到明显低于 GPT / Claude 旗舰档的价位。对选型的人来说，关键不是再记一个模型名，而是官方价、1M 上下文、以及 AA / Cursor 各自标明来源的分数。
- **对谁·深读建议**：开发者先读官方博文的定价、覆盖范围和 Fairwind 时间表；引用 61 分时写明是 AA Index、且 Google 与 AA 都有陈述；CursorBench 只标 Cursor 自报。不要把官方罗列的一长串行业基准不加来源地写成独立复测。
- **证据**：
  - 官方自报：[@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2123167884411077030)、[@GoogleAI](https://x.com/GoogleAI/status/2123168242797809944)、[@GeminiApp](https://x.com/GeminiApp/status/2123168704662012079)、[@GoogleAIStudio](https://x.com/GoogleAIStudio/status/2123168408678359294)、[官方博文](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)
  - AA 自报：[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2123170645777526962)
  - Cursor 自报：[@cursor_ai](https://x.com/cursor_ai/status/2123198346802450926)
- **约时**：博文落款 11-18；X 官宣 11-19 05:34 Asia/Singapore；Cursor 接入 11-19 07:35 Asia/Singapore

###### 3. Genie 4 进入 Project Genie 与 Gemini API，并推出 Tool Retrieval
同一窗口里，Google 先把 Genie 4 作为可玩的世界模型交给 Ultra 订阅用户，次日再把同一模型放到开发者 API，并单独发布面向大规模工具库的 Tool Retrieval。这是产品和平台两步，不要写成「只发了一个演示」。
- **是什么**：
  - Project Genie（官方，博文落款 11-18）：@GoogleDeepMind 11-19 02:14 Asia/Singapore 宣布 Genie 4 在 Project Genie 中上线，带原生音频、实时编辑，以及协助创建可交互世界的新 agent。官方称面向符合条件的 Google AI Ultra 订阅用户；Pro 可在同一页面候补。
  - Gemini API（官方，博文与 changelog 落款 11-19）：@GoogleAIStudio 11-20 02:10 Asia/Singapore 称可通过 Gemini API 与 AI Studio 试用，支持中途改天气、召唤角色，并生成自适应原生音频。changelog 写明模型代码 `genie-4`，在 Interactions API（`v1beta`）正式提供：从文本、16:9 参考图或两者生成，实时 720p / 24 fps、同步 48 kHz 立体声，经 WebRTC / WebSockets 传输。付费层定价为每百万 token **$1.50 输入 / $9.00 文本输出 / $17.50 视频输出**（官方约合 ~$0.10/秒，立体声包含在视频输出里）。单次会话最长 120 秒；官方称视觉连贯与物体持久在前 45–90 秒最强。文档写明该模型**不支持** function calling 与 Tool Retrieval。
  - Tool Retrieval（官方，预览，博文落款 11-19）：@googledevs 11-20 03:06 Asia/Singapore 宣布。做法是在 Interactions API 中加入 `tool_search`，并对暂不需要的工具设 `defer_loading: true`，让模型先看到名称与描述，需要时再加载完整参数 schema。官方称适用于 Gemini 3.6 及之后模型（含 Gemini 4），也可用于远端 MCP；无单独加价，仍按所用模型的输入/输出计费。Genie 4 本身不在此功能范围内。
  - 相邻产品（官方，写入本条以免另立主条）：@GeminiApp 11-20 04:26 Asia/Singapore 称 Gemini 应用的 Mac 版已支持 computer use，可在用户不交出屏幕与光标的前提下，于后台窗口点击、滚动和输入，并把任务交到本地文件夹、应用和网页。
- **为何重要**：Genie 4 从「订阅产品里的世界模型」变成有公开价目的 API；Tool Retrieval 则直接回应 agent 工具一多、schema 就把上下文和缓存前缀撑爆的问题。两者都已有官方文档，可以按条款写，不必靠演示视频推测。
- **对谁·深读建议**：想「玩世界」的人读 Project Genie 博文和 Ultra / Pro 资格；要接入实时世界流的开发者读 Genie 4 模型页与价目，注意会话时长和不支持函数调用；工具很多的 agent 开发者读 Tool Retrieval 博文，不要误以为 Genie 4 也能用该功能。
- **证据**：
  - 官方自报：[@GoogleDeepMind Project Genie](https://x.com/GoogleDeepMind/status/2123117733709586849)、[@GoogleAI](https://x.com/GoogleAI/status/2123117803775426737)、[Project Genie 博文](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/)、[@GoogleAIStudio API](https://x.com/GoogleAIStudio/status/2123479057996116143)、[Genie 4 API 博文](https://blog.google/innovation-and-ai/technology/developers-tools/genie-4-in-gemini-api/)、[Genie 4 模型文档](https://aistudio.google.com/docs/models/genie-4)、[@googledevs Tool Retrieval](https://x.com/googledevs/status/2123493028732207296)、[Tool Retrieval 博文](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/)、[@GeminiApp computer use](https://x.com/GeminiApp/status/2123513203745538423)
- **约时**：Project Genie 11-19 02:14 Asia/Singapore；Genie 4 API 11-20 02:10 Asia/Singapore；Tool Retrieval 11-20 03:06 Asia/Singapore；Mac computer use 11-20 04:26 Asia/Singapore

###### 4. OpenAI 推出 GPT-Live-1.1、推理复用与 Performance Factory，background 模式最高可省 40%
GPT‑6.2 本身已在上期主条写过。本窗口开发者侧的新事实，是语音 API 迭代、可等待任务的折扣、推理缓存方式的变化，以及 OpenAI 用 Codex agent 维护 ChatGPT 性能的内部系统被写成公开博文。
- **是什么**：
  - GPT-Live-1.1（官方）：@OpenAIDevs 11-20 04:00 Asia/Singapore 宣布 API 已可用，称跨语言口音更自然、更稳定，并新增 standby 以降低空闲成本。开发者文档写明模型 ID `gpt-live-1.1`，经 `v1/live/sessions` 提供全双工语音；按时长计费，**活跃 $0.05/分钟、standby $0.02/分钟**，后端模型与工具另计。
  - Background mode（官方自报）：@OpenAIDevs 11-19 06:54 Asia/Singapore 称，对可以等待的单轮或多轮工作，在 Responses API background mode 为 GPT‑6.2 Astra 或 Sol 选择 2 小时或 8 小时的「首次响应」目标，可比 Standard **每 token 最多节省 40%**。
  - 推理复用（官方）：@OpenAIDevs 11-20 07:56 Asia/Singapore 称，从最新旗舰模型开始，Responses API 里每条推理项会绑定到此前的对话历史，agent 可在此基础上继续，以更少 token、更多缓存命中得到更好结果。编辑更早的消息会打破这一绑定——主帖在此处截断，细节以官方后续文档为准，不补写未见原文。
  - Performance Factory（官方自报）：@OpenAIDevs 11-20 01:42 Asia/Singapore 与博文称，该系统调度 Codex agent 调查性能回退、提出供工程师审阅的修复，并在上线后检查是否恢复基线。官方称回归工作流在三个多月里跟踪了超过 1,700 次调查，其中逾 600 次定位到根因，约合每天 17 次自动调查。
- **为何重要**：这是 6.2 发布之后，把「能用」变成「更好用、更便宜、更好维护」的一层。Live 1.1 的 standby 价、background 40% 都是可核对的条款；Performance Factory 则说明 OpenAI 已把 agent 用在自己的生产性能值班上，数字是官方自报。
- **对谁·深读建议**：做语音会话的读 GPT-Live 文档和价目；做长任务、可异步等结果的看 background mode 的 2h/8h 目标；关心推理缓存的人注意「改历史消息会断开绑定」。不要把 1,700 / 600 写成第三方审计结果。
- **证据**：
  - 官方自报：[@OpenAIDevs GPT-Live-1.1](https://x.com/OpenAIDevs/status/2123506733524136446)、[GPT-Live-1.1 文档](https://developers.openai.com/api/docs/models/gpt-live-1.1)、[@OpenAIDevs background](https://x.com/OpenAIDevs/status/2123188195202617408)、[@OpenAIDevs 推理复用](https://x.com/OpenAIDevs/status/2123566018866151579)、[@OpenAIDevs Performance Factory](https://x.com/OpenAIDevs/status/2123471880292299171)、[Performance Factory 博文](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/)
- **约时**：background 11-19 06:54 Asia/Singapore；Performance Factory 11-20 01:42 Asia/Singapore；GPT-Live-1.1 11-20 04:00 Asia/Singapore；推理复用 11-20 07:56 Asia/Singapore

###### 5. OpenAI 称与 AMD 合作最多带来 14% PPA，并发布研究加速、对抗蒸馏与 MedChemBench
窗口后半段，OpenAI 连续用官方博文把 6.2 的能力故事从聊天产品扩到芯片设计、内部科研节奏、蒸馏防护和药物化学基准。这些都是官方自报，不是外部审计。
- **是什么**：
  - 芯片设计（官方自报，博文落款 11-18）：@OpenAI 11-19 01:05 Asia/Singapore 称，与 AMD 合作，在 AMD 工程师已多年优化的旗舰 GPU IP 上，模型找出最多 **14% 的 PPA（功耗/性能/面积）改进**，用时不到五个月；其中部分改动已被 AMD 送去制造，另一些进入未来版本的生产设计文件。同一方法用于 OpenAI 自研推理芯片 Jalapeño：官方称向量单元标准单元面积约降 13%、矩阵单元约降 10%，并已在硅验证中得到确认。博文还提到与 Synopsys 合作训练 GPT‑Synopsys，以及在开源 RISC-V 核心上的对比评测。
  - 研究加速（官方自报，博文落款 11-18）：@OpenAI 11-19 07:07 Asia/Singapore 发布 *Research acceleration: The jagged frontier*。关键数字：3 月至 10 月，估计需人类 2–4 小时的任务，agent 独立完成率从 23% 升至 46%；4–8 小时任务从 13% 升至 35%。按 API 标价，10 月内部研究者日用量中位数 $2,400（较 9 月 +62%），90 分位 $23,000（+105%）。调查中，研究者为保留三个月旗舰编程 agent，中位愿意拿 30% 团队算力或 40% 团队编制来换。官方同时强调提升是「锯齿状」的，人类仍处在研究循环中心；Safety and Alignment 的记录工作周在 1 月至 9 月增加 77%。
  - 对抗蒸馏（官方自报，博文落款 11-20）：@OpenAI 11-21 03:33 Asia/Singapore 发布 *Combatting adversarial distillation*。官方称，在内部自适应红队评估中，从先前一轮回复提取受保护推理的平均攻击成功率，从 GPT‑6 Astra 原防护下的 **54.0%** 降到 GPT‑6.2 Astra 更新防护下的 **0.2%**。博文把蒸馏视为安全问题（能力被转移到防护更弱的模型），并讨论保护完整推理轨迹、请求级与战役级检测。上述成功率为官方内部评估，不是外部复现。
  - MedChemBench（官方自报，博文落款 11-20）：@OpenAI 11-21 03:09 Asia/Singapore 介绍新基准，含 99 道来自已发表研究的药物化学推理题。官方称在 xhigh 档，GPT‑6.2 Astra 获得 84.5% 的可用分数，对照 GPT‑6 Astra 83.3%、GPT‑6.1 Sol 82.0%、GPT‑5.6 Sol 58.2%。官方自己写明：这不能证明模型能发现新药或改进实验室决策，也不能排除对已发表材料的先验接触。
- **为何重要**：把「模型变强」从榜单分数转到芯片 PPA、内部科研吞吐和防蒸馏，是 6.2 之后最完整的官方能力叙事。所有关键百分比都来自 OpenAI 自己的测量，引用时必须标明官方自报，尤其是 14% PPA 和 54.0%→0.2%。
- **对谁·深读建议**：关心半导体与自定义芯片的人读芯片博文，注意「最多 14%」是相对已高度优化基线、且含 AMD 验证的表述。关心科研自动化与治理的人读研究加速报告的任务分档和「人类仍在环内」。安全与政策读者读蒸馏博文的评估设定，不要把内部红队成功率写成已在野外验证。药物化学读者应连同官方的限度声明一起引用 MedChemBench。
- **证据**：
  - 官方自报：[@OpenAI 芯片](https://x.com/OpenAI/status/2123100386638877054)、[芯片博文](https://openai.com/index/advancing-chip-design-with-our-models/)、[@OpenAI 研究加速](https://x.com/OpenAI/status/2123191365983248653)、[研究加速报告](https://openai.com/index/research-acceleration-jagged-frontier/)、[@OpenAI 蒸馏](https://x.com/OpenAI/status/2123862344422088794)、[蒸馏博文](https://openai.com/index/combatting-adversarial-distillation/)、[@OpenAI MedChemBench](https://x.com/OpenAI/status/2123856316187975756)、[MedChemBench 博文](https://openai.com/index/introducing-medchembench/)
- **约时**：芯片帖 11-19 01:05 Asia/Singapore；研究加速 11-19 07:07 Asia/Singapore；蒸馏与 MedChemBench 分别为 11-21 03:33、03:09 Asia/Singapore

##### 进展

###### 进展：Anthropic IPO——已定价并开始交易，见主条 1
- 上期「尚未定价、无 424B」的状态在本窗口结束。后续若出现交割 8-K、绿鞋行使或官方股本数据，再核净所得与市值口径。

###### 进展：GPT‑6.2——发布本身不重写；窗口内有产品说明与第三方评测
- **是什么**：官宣早于本窗口。本窗口 @OpenAIDevs 11-21 04:46 Asia/Singapore 再次说明 ChatGPT Pro 200 可对 Sol 使用 Ultrafast。@ArtificialAnlys 11-19 10:06 Asia/Singapore 称 Astra / Sol 的回复风格较前代更短、结构更少、更少承认不确定（Astra 每则约 352→210 词，Sol 337→223 词，AA 自报）；11-21 称在 AA-Robotics v0.1 上 Astra 用最少动作完成任务（AA 自报）。@thsottiaux 11-18 13:47 Asia/Singapore 解释部分评测者可能用了数日前的旧版本。这些都不改变上期已核的官方定价。
- **证据**：[@OpenAIDevs Ultrafast](https://x.com/OpenAIDevs/status/2123880710843048001)、[@ArtificialAnlys 风格](https://x.com/ArtificialAnlys/status/2123236464003588136)、[@ArtificialAnlys Robotics](https://x.com/ArtificialAnlys/status/2123866468156854664)、[@thsottiaux](https://x.com/thsottiaux/status/2122929634916679820)
- **约时**：11-18 13:47 Asia/Singapore 至 11-21 04:46 Asia/Singapore

###### 进展：ChatGPT 新移动体验与 dots 扩测
- **是什么**：@thsottiaux 11-20 07:17 Asia/Singapore 称开始向少量 ChatGPT Plus 用户测试 dots，并说主动性反馈转正向；同日 07:20 Asia/Singapore 宣布正在做新的 ChatGPT 移动体验，先从拥有或有资格创建 dot 的 Pro 用户开始，dot 有独立标签，可固定 Codex 等。11-20 11:00 Asia/Singapore 以「Le ChatGPT 2.0」引用该帖。11-21 03:29 Asia/Singapore 还呼吁升级桌面应用。上述为产品负责人口径，未见单独的官方帮助页列出全量开放时间表。
- **证据**：[@thsottiaux dots](https://x.com/thsottiaux/status/2123556256392847657)、[@thsottiaux 移动体验](https://x.com/thsottiaux/status/2123557171321561133)、[@thsottiaux 引用](https://x.com/thsottiaux/status/2123612433923051976)
- **约时**：11-20 07:17–11:00 Asia/Singapore

###### 进展：Daybreak——本窗口未见新的官方定价或长复盘
- **是什么**：官方检索中未见 @OpenAI 就 Daybreak / Cyber 直播发布新的评测表、价目或长文复盘。上期已确认的产品页与直播记录仍是可引用的最新官方说明，本期未重开浏览器核页，故不更新产品条款。
- **约时**：覆盖至 11-21 上午 Asia/Singapore

###### 进展：Gemini 4 家族其余产品——Hydrogen / Carbon 未见官方改价
- **是什么**：Neon 见主条 2。本窗口 @GoogleAI 11-21 01:19 Asia/Singapore 发了近两周产品回顾（主帖在 Hydrogen 一句处截断）。Microsoft-Decision-1.1 由 AA 在 Ignite 相关帖中提及，不是 Google Decisions API 的条款修订。
- **证据**：[@GoogleAI 回顾](https://x.com/GoogleAI/status/2123828467124851025)
- **约时**：11-21 01:19 Asia/Singapore

##### 其他

- **Palo Alto Networks 拟全股票 $4.5B 收购 Applied Compute**（官方，新闻稿落款 11-18）：帮助企业在公有云或主权环境中安全地训练、适配和部署开源/开放权重模型；交易有惯例交割条件，预计于 Palo Alto Networks 2027 财年第三季度完成；Applied Compute CEO Yash Patil 预计交割后任联席首席 AI 官。@PaloAltoNtwks 11-19 05:22 Asia/Singapore 发帖。另，该公司 X 帖自报 FY27 Q1 营收 $3.44B（同比 +39%）等，属财报口径，不在此展开。[@PaloAltoNtwks](https://x.com/PaloAltoNtwks/status/2123165024545845701)、[新闻稿](https://www.paloaltonetworks.com/company/press/2026/palo-alto-networks-to-acquire-applied-compute--bringing-secure-open-weight-ai-to-the-enterprise)
- **Thinking Machines Inkling 2 Mini**（AA 自报，11-21 04:35 Asia/Singapore）：称在 AA Intelligence Index 得 20，开源权重、Apache 2.0，总参数 26B、激活 5.4B（含三轮 loop），每文本 token 约 3.1B 独立权重，1M 上下文，支持文本与图像输入。未见本检索中的官方账号主帖，数字以 AA 为准。[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2123877871316087012)
- **千禧年大奖问题相关宣称**（待核，11-21 03:45 Asia/Singapore）：AA 称 OpenAI 曾在 9 月用未发布内部模型宣称解决 Navier-Stokes，Anthropic 侧有 Levent Alpöge 与 Claude 合作宣称证明黎曼猜想；AA 自己写明两者仍待独立验证，分数为暂记。本包不把任一宣称写成已解决。[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2123865423364161861)
- **Claude Code 团队如何做代码审查**：@dotey 11-20 07:14 Asia/Singapore 转发 [claude.dev 博文](https://claude.dev/blog/solving-code-review-at-anthropic/)。该文落款 **2026-10-15**，不是本窗口新发布，只是窗口内被重新传播。文中「Claude 约写 90% 自身代码」、仓库合并 PR 翻倍而回滚下降逾 40% 等均为官方自报、且时间早于本窗口。
- **Gemini 应用其他**：可用 Gemini Omni 1.2 Flash 在应用里生成 GIF（@GeminiApp 11-21 00:17 Asia/Singapore）；Gemini 应用扩到更低内存的 Android / Go 设备（11-19 01:08 Asia/Singapore）。[@GeminiApp GIF](https://x.com/GeminiApp/status/2123813017855103449)、[@GeminiApp Android](https://x.com/GeminiApp/status/2123100943604707606)
- **AA 其他自报**：请 GPT‑6.2 Astra 与 Claude Fable 5.2 在 AA-3D 沙盒各用一条提示搭建迈阿密（11-18 12:06 Asia/Singapore）；并对比 Astra 与视频模型做三维场景（11-20 08:59 Asia/Singapore）。[@ArtificialAnlys Miami](https://x.com/ArtificialAnlys/status/2122904331276177768)、[@ArtificialAnlys 视频对照](https://x.com/ArtificialAnlys/status/2123581865965855205)
- **Qwen4-Max**：上期已发布。本窗口仅为登陆更多第三方平台的宣传（如 @runware、Nous Portal），未见官方改价。[@Alibaba_Qwen](https://x.com/Alibaba_Qwen/status/2122888191950901534)
- **待核、不升主条**：英伟达董事会 / 黄仁勋去留讨论；News 中的 Nvidia $10B 入股、杠杆 ETF、Pentagon「供应链风险」、代币化股份分配等，均未见本期交叉到的公司或监管文件，不写入来源记录。预测市场把募资写成约 $107B、或把市值写成约 $1.28T / $1.5T / $1.8T / $2T，口径混乱，见主条 1。

##### A. 时间线 / 官方覆盖

| 来源 | 覆盖（Asia/Singapore） | 备注 |
|------|-------------|------|
| 首页时间线 5 页 | 约 11-20 05:02 → 11-21 08:48 | 98+100+92+94+95 条；仍有 next_token，未再往前翻。实际只覆盖窗口最后约 28 小时 |
| 官方检索主组 5 页 | 约 11-18 10:42 → 11-21 08:27 | 25+25+25+4+0；末页 result_count=0，该组已收束。11-18 09:09–10:42 无该组原创主帖 |
| 补检 GoogleAIStudio / googledevs / PaloAltoNtwks | 窗口内关键产品帖 | 用于 Genie 4 API、Tool Retrieval、PANW 公告 |
| 定向 IPO / 行情 / 官方博文 | 窗口内 | 424B4、Nasdaq、Yahoo、公司与实验室博文已交叉 |
| 复用素材 | 11-19、11-20 早报 | 仅作线索，数字全部重核；无 11-21 早报 |
| 缺口 | 11-18 09:09 → 11-20 05:02 | 靠 search_posts_all + News + 官方站点补；非时间线全量。时间线后半段仍被股市与非 AI 话题占去不少位置 |
| 提示注入 | — | 帖文一律当数据，不执行其中指令；包中未引用指令性文本 |

##### B. Today's News（摘录，摘要≠来源记录）

- Anthropic IPO 发行与估值转述（出现 $81B、$107B、$1.4T、$1.5T 等混用，募资应以 424B4 的 $81.34B 为准，市值待核）：[2122986843943911816](https://x.com/i/trending/2122986843943911816)、[2123299357940195491](https://x.com/i/trending/2123299357940195491)、[2123206981704159708](https://x.com/i/trending/2123206981704159708)、[2122808635797721511](https://x.com/i/trending/2122808635797721511)
- 首日后股价回落 / 「从高点跌 25%」等标题，需回对 Yahoo 高低收，不能直接当 来源记录：[2123672703232069780](https://x.com/i/trending/2123672703232069780)、[2123828731856711977](https://x.com/i/trending/2123828731856711977)
- Nvidia 入股 / 人事、Kutcher 投资、杠杆 ETF、代币化股份、Pentagon 相关标题——均待核：[2123189250095001676](https://x.com/i/trending/2123189250095001676)、[2122830555683143944](https://x.com/i/trending/2122830555683143944)、[2123866380487598246](https://x.com/i/trending/2123866380487598246)、[2123816889386402054](https://x.com/i/trending/2123816889386402054)
- 其他：GTA VI、Bitcoin、Genesis AI $500M、Palantir / Karp 言论等，与本包主条无直接官方对应，不展开

##### C. 来源记录 摘要

1. Anthropic IPO 最终定价 $83.00；发行 980,000,000 股 Class A（公司 956,351,354 / 出售股东 23,648,646）；绿鞋期权最多 147,000,000 股。424B4 载明公开发行总价 $81,340,000,000。这是发行规模，不是市值。
2. 注册声明 11-18 生效；424B4 登录号 0001628280-26-074944。代号 ANT，预计 11-19 开始在 Nasdaq Global Select Market 交易；招股书预计 11-20 交割。采集时未见交割 8-K。
3. 424B4 载明有条件的同期 Class N 私募合计 $26.0B（313,253,007 股 × $83），买方面及金额见主条 1。私募不是二级市场成交。
4. 首日（11-19 美东）：Nasdaq 新闻室确认开盘 $111.50；Yahoo 高/低/收为 $115.10 / $92.72 / $97.17，成交量 857,312,300。次日（11-20 美东）Yahoo 收 $88.91（开 $89.86、高 $92.56、低 $83.05，成交量 399,629,474）。媒体市值数字待核。
5. Gemini 4 Neon 已发布；官方价 $3 / $0.15 缓存 / $15（每百万 token），1M 上下文。Google 与 AA 均提到 AA Index xhigh 得 61、排第三。
6. Genie 4 已在 Project Genie 上线，并进入 Gemini API（`genie-4`）；API 官方价 $1.50 / $9.00 文本输出 / $17.50 视频输出。Tool Retrieval 为 Interactions API 预览功能，不单独加价。
7. GPT-Live-1.1 已在 API 上线；文档价为活跃 $0.05/分钟、standby $0.02/分钟。Responses API background mode 官方称对 GPT‑6.2 Astra/Sol 最多比 Standard 省 40%。
8. OpenAI 官方自报：与 AMD 合作在旗舰 GPU IP 上最多 14% PPA；研究加速报告给出 2–4 小时任务 23%→46% 等内部数字；对抗蒸馏内部评估 54.0%→0.2%；MedChemBench 上 GPT‑6.2 Astra（xhigh）84.5%。
9. Palo Alto Networks 宣布拟以全股票 $4.5B 收购 Applied Compute，预计 2027 财年第三季度交割，尚须监管批准等惯例条件。

##### E. 建议扩写（3–5）

1. **发行规模 vs 市值对照表**：把 424B4 的 $83、9.80 亿股、$813.4 亿总价、公司/出售股东所得、绿鞋和 $26B Class N 私募做成一张表，再另栏列出首两日 O-H-L-C，明确市值媒体数字为何还不能进 来源记录。
2. **ANT 首两日交易复盘**：开盘 $111.50、盘中 $115.10 到收 $97.17，再收到 $88.91 接近发行价的过程，只用 Nasdaq / Yahoo / 主流报道，避免预测市场口径。
3. **Gemini 4 三档对照**：Carbon / Neon / Hydrogen 的官方价、上下文、官方自报定位，加上 AA Index 与 CursorBench（分别标明来源），写给要在同一家族里选型的人。
4. **Genie 4 产品 vs API**：Project Genie 的订阅资格，和 `genie-4` 的 $1.50/$9/$17.50、120 秒上限、不支持函数调用；再解释 Tool Retrieval 适用哪些模型。
5. **OpenAI 官方自报能力包**：14% PPA、研究加速的任务分档与日用量、54.0%→0.2% 蒸馏评估、MedChemBench 84.5%，全部保留「官方自报 / 内部评估」标签，避免写成外部验证。


## GitHub 项目与发行

### 项目原始材料

#### GitHub 三日刊（2026-11-18 → 2026-11-21）

1. **ComfyUI v0.46.0**
`Comfy-Org/ComfyUI`（原 `comfyanonymous/ComfyUI`）于 11-19 06:55（Asia/Singapore）发布正式版 v0.46.0（`prerelease=false`）。核心侧新接入 PAN2 与 SenseNova 的思考 / 交错生成 / 自纠错，并增加 Video Deflicker 节点和更快的 RAFT 光流；工作流上可把多段视频对齐到第一段的帧率和音轨，还支持拆分图像通道、保存单通道 PNG。这一版去掉了 DirectML 支持，并在支持 CUDA 13 的 GPU 上提示不要继续用旧 CUDA。合作节点里补了 MiniMax H3 Image，以及一批云端模型目录标识（不要把它们写成新开源权重）。做本地图生视频、还在用 DirectML、或要跟 PAN2 / SenseNova 工作流的人应该升。
证据：[v0.46.0 Release](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.46.0)

2. **OpenAI Codex 0.170.0 / 0.171.0**
`openai/codex` 在窗口内连续发布两个正式版：0.170.0 于 11-18 11:40（Asia/Singapore），0.171.0 于 11-20 08:44（Asia/Singapore），均为 `prerelease=false`（同窗口多枚 `*-alpha.*` 未收）。0.170 给终端补上实时语音通话的 WebRTC 协商，并修了 Cloud 会话重连和 Windows 沙箱权限。0.171 把上期还是可选的终端工作区改成默认打开，可在主对话旁预览文档、图片和子智能体记录；并增加 `codex exec --remote`，以及用 `/rc`、`/remote` 管理本机远程控制与设备配对。模型目录里加入 GPT-6.2 Sol 与 Astra，并把 Sol 设为默认目录选项——这是客户端目录标识，不是新的权重发布。日常用 Codex 终端、或要在已有 app server 上跑非交互任务的人应该升到 0.171。
证据：[0.171.0 Release](https://github.com/openai/codex/releases/tag/rust-v0.171.0) · [0.170.0 Release](https://github.com/openai/codex/releases/tag/rust-v0.170.0)

3. **Unsloth Desktop：AMD NPU、Inkling 2 Mini，以及视频扩散 LoRA**
`unslothai/unsloth` 在窗口内连续发布 v0.1.920-beta（11-19 22:31 Asia/Singapore）、v0.1.921-beta（11-21 03:56 Asia/Singapore）和 v0.1.922-beta（11-21 07:53 Asia/Singapore）。标签仍带 `-beta`，但 API 字段均为 `prerelease=false`。920 把自行转换的 Q4NX 文本模型接到 AMD NPU，并开放 LTX-2.5、MOSS-Image 的 LoRA 训练，以及 Cosmos3 的 FP8 视频权重；配套有 AMD 官方博客。921 / 922 接入 Inkling 2 Mini（发布说明写明约 26B 总参数、5.4B 激活、1M 上下文，自称「同体积最强」、可在 16GB 内存上跑，标「自称」），并称 8GB 显卡上 MiniMax-H3-Image 新提示从 82.7 秒降到 36.7 秒、GGUF 图像模型加载内存少 52–66%、MCP 对话少处理 83–87% 提示词，均为「自称」。有 Ryzen AI 机器、想训视频 / 图像 LoRA，或要在桌面端跑 Inkling 2 Mini 的人可以跟上。
证据：[v0.1.922-beta Release](https://github.com/unslothai/unsloth/releases/tag/v0.1.922-beta) · [v0.1.920-beta Release](https://github.com/unslothai/unsloth/releases/tag/v0.1.920-beta) · [Inkling 2 Mini 说明](https://unsloth.ai/docs/models/inkling-2-mini) · [AMD 博客](https://www.amd.com/en/blogs/2026/unlocking-the-amd-ryzen-ai-npu-for-unsloth-desktop.html)

4. **OpenAI Python v3.55–3.57 / Node v7.60–7.62：Live MCP 与 gpt-live-1.1 目录标识**
OpenAI 官方 SDK 在窗口内连发三档正式版（均为 `prerelease=false`）：Python v3.55.0 于 11-18 13:21（Asia/Singapore）、Node v7.60.0 于 11-19 00:06（Asia/Singapore）加入 Live 的 MCP 服务器配置；Python v3.56.0 / Node v7.61.0 于 11-20 04:56（Asia/Singapore）把 `gpt-live-1.1` 加入 Live 模型选项；Python v3.57.0 / Node v7.62.0 于 11-20 09:27（Asia/Singapore）支持 Live WebRTC standby。`gpt-live-1.1` 是 API / SDK 目录标识，不是本期在 GitHub 上的权重发布。做实时语音或要把 MCP 接到 Live 会话里的应用应升到 3.57 / 7.62。
证据：[Python v3.57.0](https://github.com/openai/openai-python/releases/tag/v3.57.0) · [Node v7.62.0](https://github.com/openai/openai-node/releases/tag/v7.62.0) · [Python v3.55.0](https://github.com/openai/openai-python/releases/tag/v3.55.0)

（热榜口径：日榜约为最近 24 小时，周榜统计最近七天，均于 2026-11-21 08:50 Asia/Singapore 抓取，不可当作本期 72h 净增。HKUDS/CLI-Anything 日榜约 773、总量约 61,381，港大数据科学组织身份可核，官网 [clianything.cc](https://clianything.cc/)，但最近正式版仍是 6 月的 v0.4.0，本期不单列。周榜前列 plannotator、stitch-skills、open-code-review、astryx、ag-ui、sure 等均为旧仓留榜。新仓搜索前列混有大量可疑项目，未收录：`bookwjitchieni1986/blender-ai-mcp-addon` 约 1,778 星、两天内新建、账户名随机、README 关键词堆砌且仓库语言为空；`duwqijlk/google-trial-tool`、`hoangsvit/google-ai` 同类 Play 结算试用脚本，非 Google 官方；另有锁屏绕过、安装包克隆，以及一批星数同为约 158 的游戏「战术 HUD」仓。`ranxianglei/billion-context` 仍无新的可交叉核验进展，继续不收录。）

窗口内无：vllm-project/vllm、sgl-project/sglang、ggml-org/llama.cpp（仅 `b12xxx` 预发布日构建）、ollama/ollama（最新仍为窗口前发布的 v0.40.17-rc4，`prerelease=true`）、huggingface/transformers、pytorch/pytorch、huggingface/datasets、modelcontextprotocol/python-sdk、modelcontextprotocol/typescript-sdk、axolotl-ai-cloud/axolotl（常规 / 预发布未收录：openai/codex 多枚 `*-alpha.*`；anthropics/anthropic-sdk-python v2.11.0 / v2.12.0 与 TypeScript sdk-v1.11.0 / sdk-v1.12.0 / bedrock-sdk-v1.1.3，主要为 Admin API 与错误码；langchain 1.5.1 / 1.5.2、langchain-core 1.8.3 / 1.8.4、langchain-openai 1.8.2–1.8.5，以及 langgraph 1.2.23 / 1.2.24、prebuilt 1.1.3 等补丁）


## 模型与数据集

### 模型、数据与榜单原始材料

#### HF / 模型三日雷达素材 · 2026-11-21

- 窗口：2026-11-18 09:09 Asia/Singapore（01:09 UTC，上期采集截止）→ 2026-11-21 约 09:00 Asia/Singapore（01:00 UTC，实际采集时刻）。
- 去重基线：11/18 素材包（内部证据存档），sha256 b71f99fd…c8f）和 （内部证据存档） 的榜单快照、镜像核查。上期写过的条目只在有新事实时再写，标“更新”。
- 计数：主条 4（全部为本窗新公开）｜跟进 8（SenseNova-Loop-9B、Inkling 2 Small、harness-hub pi-adapted、FastFrames、Sage S2.1 Flash、Kimi K3.1 Pro、Agnes、热度榜 Haru/H3-Image）｜次条 7｜补记 2｜榜单 6 段｜数据集 5 条主条 + 3 条附记｜同名镜像/冒名 4 组。
- 数据口径：likes/downloads 统一取 HF API 在 2026-11-21 09:00 Asia/Singapore（01:00 UTC）的快照（采集证据快照）。downloads 是 HF 的近 30 天口径，新 repo 常显示 0。Trending 取 08:50 Asia/Singapore 的 API（模型 300 条、数据集 100 条），trending HTML 页一并保存。
- 开放程度用语：“开放权重”= 权重能下载；“OSI 许可”= 权重许可证属于 OSI 认可的许可证（Apache-2.0/MIT），未逐项核对 OSAID；“自定义/非商用许可”= 权重开放，但不算开源。

##### 三句话结论

1. **本窗最大的事是腾讯一次放出 Hy4 全家：770B 旗舰 Hy4（49B 激活）和 220B 的 Hy4 flash（12B 激活），各带 FP8 和 base 版。但许可证是自定义的“Tencent Hy License 1.0”，不是 Apache-2.0。** 它以 Apache-2.0 为底稿，加了一条：年营收超 5,000 万美元、或产品月活超 1 亿的 MaaS（对外提供推理/微调 API）业务要另签授权。Artificial Analysis 随即把 Hy4 从闭源改标为开放权重（commercial-license），34.6 分，成为开放权重第 2。
2. **Thinking Machines 发了 Inkling 2 Mini（26.4B 总参、3.4B 激活，Apache-2.0）：一个约 20GB、原生 NVFP4/MXFP8 的“循环层”MoE，32GB 内存的 Mac 就能跑。** AA 给它 20.1 分，和 Qwen3.8 27B 打平；同时放出研究版 TML-d24-varloop-research，可以在推理时选 1–5 次循环。
3. **另外两条值得写：微软 Windows 团队的 2.3B 端侧模型 Aion 1.0 Instruct（MIT），以及 RadixArk 在 Qwen3.8-27B 上纯 RL 训练的 DaisyRose-27B（Apache-2.0）。** 榜单侧，AA 新收 Gemini 4 Neon（61.4，闭源），LMArena 文本和视觉榜刷新到 Nov 20；LMArena 页面改版后 WebFetch 只能读到前 15 名，本期无法逐行比对全表（见缺口）。

---

##### 主条

###### 1. tencent/Hy4 + tencent/Hy4-flash（各含 -FP8、-base）· 新开放权重（Tencent Hy License 1.0，自定义许可，非 OSI）

这是本窗分量最重的开放权重发布。腾讯混元团队把 11 月初还只在 AA 上以闭源身份出现的旗舰 Hy4（往期 11/06 写过“HF 上无 tencent/Hy4 仓库”）连同新的轻量版 Hy4 flash 一起放上 HF，各配 FP8 量化版和预训练 base 版，共 6 个 repo。Hy4 是 770B 总参 / 49B 激活的 MoE（78 层，256 路由专家取 top-8，Gated DSA 稀疏注意力 + IndexCache，1M 上下文），支持文本、图像和视频理解；Hy4 flash 是 220B 总参（含 64B 的 n-gram “Engram” 参数）/ 12B 激活，混合稀疏/滑窗注意力、LatentMoE（512 专家取 16），定位“最省钱的 Hy 模型”。两者都内置 DFly2 草稿模型做投机解码。要讲清楚的是许可：8 月的 Hy4-preview 是 Apache-2.0，这次正式版换成了自定义的 Tencent Hy License。

- 为什么重要：
  - 国内大厂的旗舰级模型以完整权重放出，规模（770B）和 Kimi K3.1 Pro、GLM-5.3 处在同一梯队；AA 已把 Hy4 改标为开放权重，34.6 分，排在 Kimi K3.1 Pro（46.5）之后、DeepSeek V4.1 Flash 1017（32.6）之前，是目前开放权重第 2。
  - Hy4 flash 在本窗百亿参数以上的新模型里 Trending 排名最高（#8）；窗口内按名称能搜到 64 个 Hy4-flash 衍生 repo（GGUF/MLX/EXL3 等），腾讯 AngelSlim 组织的官方 GGUF 版 downloads 已到 75,614。
  - 许可证的变化本身值得报道：从 preview 的 Apache-2.0 收紧为“Apache-2.0 + 大型 MaaS 商业条款”。
- 适合谁 / 阅读建议：
  - 想自托管国产大模型的团队：Hy4 BF16 约 1.55TB、FP8 约 786GB，需要多机；Hy4 flash BF16 约 441GB、FP8 约 287GB，门槛低得多。卡片给了 vLLM/SGLang 部署和 DFly2 配置。
  - 做云服务或 API 转售的公司要先读 LICENSE 第 10 节，判断自己是否落在“营收 > 5,000 万美元或月活 > 1 亿”的门槛内；内部自用不受此条约束。
  - 普通读者记住：Hy4 = 腾讯旗舰开放权重，Hy4 flash = 便宜好部署的版本，许可证可商用但对大型 API 厂商设了门槛。
- 来源记录：
  - HF 时间：
    - tencent/Hy4：createdAt 2026-10-29 08:29 UTC / 10-29 16:29 Asia/Singapore；历史被压成 1 个 commit `c10c0de5b6`“update”，2026-11-20 03:05 UTC / 11-20 11:05 Asia/Singapore，这也是 lastModified。repo 创建早于窗口，但往期 11/06 核查时 HF 上没有这个 repo；确切公开时刻待核。
    - tencent/Hy4-FP8：createdAt 2026-11-18 06:59 UTC / 11-18 14:59 Asia/Singapore；tencent/Hy4-base：createdAt 2026-11-18 07:01 UTC / 11-18 15:01 Asia/Singapore（都在窗口内），两者同样只有一个 11-20 03:05 UTC 的压缩 commit。
    - tencent/Hy4-flash：createdAt 2026-11-17 03:44 UTC / 11-17 11:44 Asia/Singapore；权重文件的 lastCommit 都是 `bf68d9f097`，2026-11-17 13:19 UTC / 11-17 21:19 Asia/Singapore。但上期 11-18 01:00 UTC 的按 createdAt 全量扫描里没有这个 repo，说明当时仍未公开；LICENSE 文件和图表在 2026-11-18 02:49 UTC / 11-18 10:49 Asia/Singapore（commit `fd4b2041a0`，窗口内）才加入，lastModified 2026-11-19 11:25 UTC / 11-19 19:25 Asia/Singapore（`b2498eba6a` 只改 chat_template.jinja）。GitHub 仓库 Tencent-Hunyuan/Hy4-flash 创建于 2026-11-17 08:18 UTC。
  - 热度（采集 11-21 09:00 Asia/Singapore）：Hy4 likes 127 / downloads 89，Trending #21（trendingScore 94）；Hy4-flash likes 545 / downloads 3,949，Trending #8（175.5）；Hy4-flash-FP8 likes 23 / downloads 1,219；Hy4-flash-base likes 24 / downloads 699；Hy4-FP8 likes 11 / downloads 71；Hy4-base likes 8 / downloads 68。
  - 许可 / 任务：6 个 repo 的 license 都是 other（tencent-hy-license），pipeline image-text-to-text。LICENSE 全文开头写明“derived from the Apache License, Version 2.0 … This License is not the Apache License”；第 10 节规定，经营 MaaS 业务且（a）全球年营收超过 5,000 万美元，或（b）用于月活超过 1 亿的产品时，须另行取得腾讯书面授权；纯内部使用（模型和输出都不对外）不受此限。Hy4 与 Hy4-flash 的 LICENSE 逐字节相同（13,942 字节）。判定：开放权重，自定义许可，非 OSI。对照：tencent/Hy4-preview（8 月）的 license 是 apache-2.0。
  - 权重证据（`?blobs=true` 与完整 tree 统计）：Hy4 245 个权重文件 1,548.93GB，HF 解析参数 774,434,002,142（含 ViT、DFly2）；Hy4-FP8 245 个 786.31GB；Hy4-base 280 个 1,542.35GB、771,142,535,581 参数；Hy4-flash 148 个 440.52GB、220,251,201,958 参数；Hy4-flash-FP8 148 个 287.07GB；Hy4-flash-base 139 个 438.83GB。
  - 官方身份：tencent 组织（HF 认证，13,608 关注者）。卡片链回 GitHub Tencent-Hunyuan/Hy4、Tencent-Hunyuan/Hy4-flash，以及 ModelScope、GitCode 同名页；官方 GGUF 指向 AngelSlim/Hy4-flash-GGUF（AngelSlim 是腾讯的压缩工具组织，未认证；createdAt 2026-11-16 14:28 UTC，9 个 GGUF 共 781.88GB，likes 118 / downloads 75,614，采集 11-21 09:00 Asia/Singapore，Trending #61）。
  - AA：Tencent Hy4 记录的 isOpenWeights 从 false 变为 true，openSourceCategorization 从 proprietary 变为 commercial-license，分数仍 34.6，releaseDate 仍写 2026-11-03。AA 还没有 Hy4 flash 的条目。
- 待核：
  - Hy4 的确切公开时间（repo 历史已被压缩）；HF 的 createdAt 10-29 只是建库时间。
  - 卡片的所有分数都是腾讯自测：Hy4 flash 在内部基准 WorkIndex 上 42.1（Hy4 preview 39.7）、单任务成本是 Hy4 preview 的 1/13；盲测满意度 2.79/4（Claude Haiku 5.5 为 2.81/4）；解码速度“超过 150 tokens/s”。
  - Hy4 flash 的 KV cache “是 Hy3 的 1/24、Hy4 的 1/6”，为卡片自述。
- 衍生（降权）：窗口内按名称搜到 Hy4-flash 衍生 64 个、Hy4 衍生约 19 个（FlagRelease 的 8 个国产芯片 W8A8 版、MLX、GGUF 等）；autotrust/hy4-flash-concise 见次条；alesha-pro/Hy4-flash-Uncensored-GGUF、trohrbaugh/Hy4-flash-heretic 属改包，过滤。全量同名复制件见文末冒名段。
- 证据：
  - [HF tencent/Hy4](https://huggingface.co/tencent/Hy4)
  - [HF tencent/Hy4-flash](https://huggingface.co/tencent/Hy4-flash)
  - [HF tencent/Hy4-flash](https://huggingface.co/tencent/Hy4-flash/blob/main/LICENSE)
  - [GitHub Tencent-Hunyuan/Hy4](https://github.com/Tencent-Hunyuan/Hy4)
  - [GitHub Tencent-Hunyuan/Hy4-flash](https://github.com/Tencent-Hunyuan/Hy4-flash)
  - [artificialanalysis.ai 来源](https://artificialanalysis.ai/models)
  - 本地：（采集证据快照）、（采集证据快照）、（采集证据快照）
  - 注：卡片上的官网 hy.tencent.ai/research/hy4-flash 对脚本只返回反爬挑战页，未作为外链。

###### 2. thinkingmachines/Inkling-2-Mini（+ TML-d24-varloop-research）· 新开放权重（Apache-2.0，OSI 许可）

Thinking Machines 在 Inkling 2 Small（11/05）之后放出更小的 Inkling 2 Mini：26.4B 总参、3.4B 激活，24 层里中间 12 层（两个 6 层块）共享权重、每个 token 跑三遍，所以每 token 有 48 次层计算，官方折算“有效激活约 5.4B”。权重以训练时的原生精度发布（20 层 NVFP4、最后 4 层 MXFP8），单个检查点约 20GB，官方写明 32GB 内存的 Apple 芯片设备或单卡 32GB 显存即可运行，1M 上下文，多模态输入。官方博客还交代了训练过程：先以 384 选 8 专家训练，中途按使用率剪掉三分之二专家只留 128 个，再用一个更大的内部 Inkling 模型蒸馏 1T token“愈合”，之后 SFT 加 2.2T token 的 RL。同时放出的 TML-d24-varloop-research 是同架构的研究版，可以在推理时选择循环 1–5 次，专供研究“多循环一次到底带来什么”，不提供 API。

- 为什么重要：
  - 这是本窗 Trending 上排名最高的新模型（#4），unsloth 的 GGUF 版也冲到 #7。小体积 + Apache-2.0 + 原生 4bit 训练，意味着本地部署不用再做有损量化。
  - 和上期的 SenseNova-Loop-9B 一样走“循环层换参数”的路线，但规模更大、配套更全（vLLM、SGLang、llama.cpp、Ollama、MLX 等首发即支持），说明 looped transformer 正在从论文走向主流开放模型。
  - 第三方 AA 已测：Intelligence Index v5 20.1 分，与 Qwen3.8 27B（20.1）打平，在 4B–40B 开放权重组里排第 2/16。
- 适合谁 / 阅读建议：
  - 想在笔记本或单卡上跑 agent/编程助手的开发者，优先试这个和 Qwen3.8-27B 对比。
  - 研究循环模型、CoT 可监控性的研究者：读官方博客“Monitorability of looped transformers”一节，再用 TML-d24-varloop-research 复现不同循环次数的对比（卡片给了 1–5 次的分数表）。
  - 官方自己写明短板：多轮对话和多约束指令（MultiChallenge 50.0%、ComplexConstraints v1.1 33.4%）不如 Qwen3.8-27B。
- 来源记录：
  - HF 时间：Inkling-2-Mini createdAt 2026-11-17 00:26 UTC / 11-17 08:26 Asia/Singapore（建库早于窗口，但上期全量扫描里没有它，当时未公开）；权重 commit `1fb4134b9a`“upload model”，2026-11-20 22:02 UTC / 11-21 06:02 Asia/Singapore（窗口内，也是首个 commit）；lastModified 2026-11-20 22:55 UTC / 11-21 06:55 Asia/Singapore（`ed40e7da62` 只在 config.json 顶层加 `"dtype": "bfloat16"`）。卡片写“Date of release: November 20, 2026”。TML-d24-varloop-research createdAt 2026-11-18 21:23 UTC / 11-19 05:23 Asia/Singapore，权重 commit `657b53ba5d` 同为 2026-11-20 22:02 UTC。
  - 热度（采集 11-21 09:00 Asia/Singapore）：Inkling-2-Mini likes 598 / downloads 136，Trending #4（trendingScore 202.5，08:50 Asia/Singapore）；TML-d24-varloop-research likes 9 / downloads 15。unsloth/Inkling-2-Mini-GGUF likes 193 / downloads 0，Trending #7；ggml-org/Inkling-2-Mini-GGUF likes 13 / downloads 0。
  - 许可 / 任务：license apache-2.0，pipeline image-text-to-text，library transformers。开放权重，OSI 许可；另附“Model Acceptable Use Policy”链接（使用政策，不改变许可证类型）。
  - 权重证据：model-00001-of-00001.safetensors 19,526,019,168 字节 + mtp.safetensors 635,801,416 字节，合计约 20.16GB；HF 解析参数 26,388,646,440；config 架构类 `Inkling2LoopForConditionalGeneration`。TML-d24 两个权重文件大小与 Mini 逐字节相同，但 sha256 不同（是另一套权重），tokenizer、chat template、量化配置文件完全相同。
  - 官方身份：thinkingmachines 组织（显示名 Thinking Machines Lab，未认证，2,338 关注者，10 个模型），即往期 Inkling 2 Small 的发布方；官方新闻页 thinkingmachines.ai/news/inkling-2-mini/（Nov 20, 2026）和 HF 博客 hf.co/blog/inkling2mini 都链回该 repo。
  - AA：模型页 artificialanalysis.ai/models/inkling-2-mini，releaseDate 2026-11-20，intelligenceIndex 20.13；页面写“26B parameters (5.4B active)”，输出速度 280 tok/s，价格输入 $0.15 / 输出 $0.50（每百万 token，提供方为 Thinking Machines 自家 API）。它不在 AA 首页默认 28 个模型里。
- 待核：
  - 卡片自报 DeepSWE v1.1 48.2%、SWE-bench Verified 79.2%、BrowseComp 79.0%、Vals Index v2.2 46.5% 等，以及“领先所有 100B 以下开放权重模型”的说法，除 AA Index 外都是自测。
  - 安全一栏的 Misbehavior / Destructive actions 是内部评测。
- 衍生（降权）：窗口内按名称搜到 30 个衍生 repo（MLX、GGUF、NVFP4 为主）；OpenUncensored/Inkling-2-Mini-Uncensored、JoaoZaokk/Inkling-2-Mini-Heretic-GGUF 等属改包，过滤。
- 证据：
  - [HF thinkingmachines/Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini)
  - [HF thinkingmachines/TML-d24-varloop-research](https://huggingface.co/thinkingmachines/TML-d24-varloop-research)
  - [thinkingmachines.ai 来源](https://thinkingmachines.ai/news/inkling-2-mini/)
  - [HF blog/inkling2mini](https://huggingface.co/blog/inkling2mini)
  - [artificialanalysis.ai 来源](https://artificialanalysis.ai/models/inkling-2-mini)
  - 本地：（采集证据快照）、（采集证据快照）、（采集证据快照）、（采集证据快照）

###### 3. microsoft/Aion-1.0-Instruct-2.3B（+ ONNX-WebGPU 版）· 新开放权重（MIT，OSI 许可）

微软 Windows 应用科学组（Applied Sciences Group）放出 2.3B 参数的端侧小模型 Aion 1.0 Instruct。卡片的定位很直接：它是 Windows 生态的基础小模型，主打本机上的摘要、改写、问答和操作系统场景，32K 上下文，支持英、德、西、葡、意、法、中、日 8 种语言；进一步优化、并搭配微软内容审核模型的版本，会在 2027 年 1 月底成为 Windows 系统内置的 SLM。HF 版是“提前公开、收集反馈”，先放未量化版，量化版之后再出。

- 为什么重要：
  - 这是 Windows 内置模型的公开前身，意味着今后 Windows 上的本地 AI 功能，其底座可以被开发者提前下载、评测和微调。
  - 许可是 MIT，比多数端侧模型的自定义许可更宽松。
- 适合谁 / 阅读建议：做 Windows 应用、本地 RAG、隐私敏感场景的开发者；ONNX-WebGPU 版面向浏览器内推理（WebGPU）。配套示例代码在 GitHub microsoft/Aion-Instruct-Preview-Sample。
- 来源记录：
  - HF 时间：createdAt 2026-11-18 17:05 UTC / 11-19 01:05 Asia/Singapore；首个 commit `1423a073e2`“Duplicate from asgmodels/Aion-Instruct-v1”同时带入权重；lastModified 2026-11-18 22:31 UTC / 11-19 06:31 Asia/Singapore（之后只改 README、删 logo 图片）。ONNX-WebGPU 版 createdAt 2026-11-18 17:08 UTC / 11-19 01:08 Asia/Singapore，同样从 asgmodels/Aion-Instruct-v1-ONNX-WebGPU 复制而来。来源 repo asgmodels/Aion-Instruct-v1 现在匿名访问返回 401（私有或受限）。
  - 热度（采集 11-21 09:00 Asia/Singapore）：likes 161 / downloads 1,578，Trending #54（trendingScore 40.5）；ONNX-WebGPU 版 likes 10 / downloads 81。
  - 许可 / 任务：license mit（repo 内有 LICENSE），pipeline text-generation，custom_code。开放权重，OSI 许可。
  - 权重证据：1 个权重文件 4.58GB，HF 解析参数 2,288,831,488。
  - 官方身份：microsoft 组织（HF 认证，23,166 关注者）；卡片署名“Applied Sciences Group @ Microsoft Windows & Devices”；GitHub microsoft/Aion-Instruct-Preview-Sample 创建于 2026-05-31，早于本次 HF 发布。
- 待核：卡片没有给出基准分数，也没有技术报告；“2027 年 1 月底成为 Windows OS SLM”是卡片表述，以微软正式公告为准；LMArena、AA 都未收录。
- 证据：
  - [HF microsoft/Aion-1.0-Instruct-2.3B](https://huggingface.co/microsoft/Aion-1.0-Instruct-2.3B)
  - [HF microsoft/Aion-1.0-Instruct-2.3B-ONNX-WebGPU](https://huggingface.co/microsoft/Aion-1.0-Instruct-2.3B-ONNX-WebGPU)
  - [GitHub microsoft/Aion-Instruct-Preview-Sample](https://github.com/microsoft/Aion-Instruct-Preview-Sample)

###### 4. RadixArk/DaisyRose-27B（+ FP8 / NVFP4 / GGUF）· 新开放权重（Apache-2.0，OSI 许可；Qwen3.8-27B 微调）

RadixArk（SGLang、Miles 训练框架背后的团队）的第一个模型。它不是新基座，而是在 Qwen3.8-27B 上只做强化学习、不做 SFT 和蒸馏：约 1,200 个精选长程 agent 任务、单会话最长 1M token，在 144 张 H200 上训练 18 天。架构、分词器、chat template 都和 Qwen3.8-27B 一样，可以直接替换。官方自报的主要提升是 Terminal-Bench 4.1 pass@1 从 5.6 升到 12.0，其他基准多为小幅提升（如 Terminal-Bench 2.1 73.0 → 75.5、GPQA Diamond 89.2 → 90.7）。

- 为什么重要：Trending #27；窗口内按名称搜到 37 个 DaisyRose 相关 repo（含官方 4 个），bartowski 的 GGUF 下载已过万；它是“小团队用有限算力、只靠 RL 能把 27B 推多远”的一个公开样本，训练框架 Miles 也开源。
- 适合谁 / 阅读建议：已在用 Qwen3.8-27B 做 agent/编程的人可以直接替换对比；做 RL 后训练的团队可读官方博客里任务设计和基础设施两节。
- 来源记录：
  - HF 时间：createdAt 2026-11-18 05:31 UTC / 11-18 13:31 Asia/Singapore；权重 commit `19b7ed5cce`“Model release”，2026-11-18 08:11 UTC / 11-18 16:11 Asia/Singapore（窗口内）；lastModified 2026-11-19 21:10 UTC / 11-20 05:10 Asia/Singapore（其后 14 次都是 README 修改）。
  - 热度（采集 11-21 09:00 Asia/Singapore）：likes 270 / downloads 918，Trending #27（trendingScore 78.5）；FP8 版 likes 6 / downloads 245，NVFP4 版 likes 11 / downloads 338，官方 GGUF 版 likes 6 / downloads 10,288；bartowski/RadixArk_DaisyRose-27B-GGUF likes 20 / downloads 12,690。
  - 许可 / 任务：license apache-2.0，base_model Qwen/Qwen3.8-27B（base_model_relation: finetune），pipeline image-text-to-text。基座 Qwen3.8-27B 本身是 Apache-2.0，许可链无冲突。开放权重，OSI 许可。
  - 权重证据：18 个 safetensors 55.56GB，HF 解析参数 27,781,427,952，与 Qwen3.8-27B 完全相同。
  - 官方身份：RadixArk 组织（未认证，416 关注者，25 个模型）；官方博客 radixark.com/blog/daisyrose-27b（November 18, 2026）链回该 repo。
- 待核：卡片对比表（Terminal-Bench 4.1 12.0、SWE-bench Pro v2 94.7、IFBench 82.4 等）全为 RadixArk 自测，Terminal-Bench 4.1 是其内部 mini-swe-agent 框架；AA、LMArena 未收录。
- 证据：
  - [HF RadixArk/DaisyRose-27B](https://huggingface.co/RadixArk/DaisyRose-27B)
  - [radixark.com 来源](https://www.radixark.com/blog/daisyrose-27b)
  - [HF bartowski/RadixArk_DaisyRose-27B-GGUF](https://huggingface.co/bartowski/RadixArk_DaisyRose-27B-GGUF)

---

##### 跟进（上期条目的新事实）

###### F1. SenseNova-Loop-9B：上期待核的官方 AWQ 版已发布，另出官方 GGUF 和 MTP 草稿权重 · 更新

- 判断：上期待核点“商汤说首发会有的 AWQ 量化版还没出现”已解决。官方 AWQ 版和 GGUF 版都在 11-18 上传，GitHub News 写“2026-11-18: Added download links for the AWQ and GGUF weights”。主 repo 同期补了 BF16 MTP 草稿权重，用于投机解码。
- sensenova/SenseNova-Loop-9B-AWQ：createdAt 2026-11-18 03:25 UTC / 11-18 11:25 Asia/Singapore；权重 commit `7a0545f471`“Add SenseNova-Loop-9B AWQ weights and MTP draft”，2026-11-18 08:53 UTC / 11-18 16:53 Asia/Singapore；3 个 AWQ 分片合计 5.59GB，外加 0.49GB 的 MTP 草稿；部署走 LightLLM。likes 17 / downloads 446（采集 11-21 09:00 Asia/Singapore）；apache-2.0。
- sensenova/SenseNova-Loop-9B-GGUF：createdAt 2026-11-18 06:47 UTC / 11-18 14:47 Asia/Singapore；权重 commit `384a4241b4`，2026-11-18 09:28 UTC / 11-18 17:28 Asia/Singapore；BF16、Q8_0、Q5_K_M、Q4_K_M 四档加 mmproj，共 41.62GB。likes 78 / downloads 49,470（采集 11-21 09:00 Asia/Singapore），Trending #67；apache-2.0。
- 主 repo：2026-11-18 03:20 UTC / 11-18 11:20 Asia/Singapore 的 commit `fa381f7c46`“Add BF16 MTP draft weights”加入 2 个文件（0.49GB），2026-11-20 05:34 UTC 的 `3cc220e9c1` 把它写进权重索引，所以 HF 解析参数从上期的 9,412,963,952 变为 9,656,254,576。主权重文件（`c26b3edcf4`）没有变化。仍是 gated: auto，commits 接口匿名 401，以上来自 tree 的 lastCommit。likes 445 / downloads 1,631（采集 11-21 09:00 Asia/Singapore）（上期 likes 184 / downloads 0）；Trending #12 → #9。
- 待核：“256K 上下文约 15GiB 显存”仍是官方数字，没有第三方复测。
- 证据：[HF sensenova/SenseNova-Loop-9B-AWQ](https://huggingface.co/sensenova/SenseNova-Loop-9B-AWQ) · [HF sensenova/SenseNova-Loop-9B-GGUF](https://huggingface.co/sensenova/SenseNova-Loop-9B-GGUF) · [GitHub OpenSenseNova/SenseNova-Loop](https://github.com/OpenSenseNova/SenseNova-Loop)

###### F2. Inkling 2 Small：官方修了 chat template、补上 eos/pad 和 generation_config，自己做微调或批量推理的用户应同步 · 更新

- 判断：这是继上期 config.json 改参数之后的第二次“影响使用”的修补。2026-11-20 14:09 UTC / 11-20 22:09 Asia/Singapore，两个官方 repo 各提交三次：
  - `0674689cb3`（MXFP8 版 `680439eb06`）：在 tokenizer_config.json 和 special_tokens_map.json 里补上 `eos_token: <|content_model_end_sampling|>`、`pad_token: <|endoftext|>`。
  - `3cdd8a8204`（MXFP8 版 `ba8f9aafcd`）：chat template 给 assistant 消息包上 `{% generation %}` 标记，transformers 用它生成 assistant mask，做 SFT 时才能只对回答部分算损失。
  - `885d78bfca`（MXFP8 版 `14f2cb29a5`）：新增 generation_config.json（eos_token_id 200006，pad_token_id 199999）。
  - 权重文件仍未变（25 个 safetensors，393.48GB）。同日 01:16 UTC 另有一次 surge-update，只更新卡片里的 DAYJOB 评测表。新发布的 Inkling 2 Mini 首发就带了这套配置。
- 热度：likes 649 / downloads 40,574（采集 11-21 09:00 Asia/Singapore）（上期 likes 442 / downloads 18,359）；Trending #5 → #24。AA 仍 30.6。
- 证据：[HF thinkingmachines/Inkling-2-Small](https://huggingface.co/thinkingmachines/Inkling-2-Small) · 本地 （采集证据快照）、`_0674689cb3.diff`、`_885d78bfca.diff`

###### F3. harness-hub/Qwen3.8-27B-pi-adapted：作者更正了 SWE-bench Pro 对比，“不开思考就追平最高思考档”的说法收回一半 · 更新

- 判断：上期写的这个 LoRA 现在是 HF Trending #2，但 2026-11-19 08:01 UTC / 11-19 16:01 Asia/Singapore 的 commit `80d05c9051`“Corrected thinking-on SWE-bench Pro scores”改了关键数字：基座 Qwen3.8-27B 开 xhigh 思考时，SWE-bench Pro（hard 51 题）从 64.7% 更正为 74.5%；adapter 不开思考仍是 64.7%。卡片表述随之改成“在 SWE-bench Pro 上拿到思考档 35 个点提升中的 25 个（64.7% vs 74.5%），生成 token 约少 4.5 倍”：Terminal-Bench 2.1 上仍与最高思考档持平（56.6% vs 54.2%），SWE-bench Pro 上落后约 10 个点。同一 commit 还修了一个把 opencode 写成 pi 的表头。
- 热度：likes 863 / downloads 1,874（采集 11-21 09:00 Asia/Singapore）（上期 likes 128 / downloads 0）；Trending #17 → #2（trendingScore 293）。姊妹版 opencode-adapted likes 194 / downloads 302，Trending #46。apache-2.0。
- 待核：全部是作者自测，样本只有 51 题；上期提到的 HF 博客链接仍未写入外链。
- 证据：[HF harness-hub/Qwen3.8-27B-pi-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted) · 本地 （采集证据快照）

###### F4. FastFrames：论文 arXiv 编号已出（2611.23226）；repo 历史被重新压缩，权重未变 · 更新

- 上期待核“arXiv 编号未出”已解决：arXiv 2611.23226“FastFrames: Video Generation at Interactive Latency”，v1 提交于 2026-11-17 18:59 UTC / 11-18 02:59 Asia/Singapore，作者 Gene Chou、Guandao Yang、Fujun Luan、Lars Mescheder、Wei Dong、Stephan Richter、Vladlen Koltun。
- 两个 repo 的历史都被重新压成一个“Public release” commit：S 版 `aa099efced`，2026-11-18 05:29 UTC / 11-18 13:29 Asia/Singapore；L 版 `d18ec5f054`，2026-11-20 02:22 UTC / 11-20 10:22 Asia/Singapore。与上期保存的 tree 逐文件比对，只有 README.md（arXiv 徽章从“coming soon”换成编号，L 版加了社区 Demo 链接）和 SHA256SUMS 两个文件变了，权重 LFS 哈希全部相同。
- 热度：L likes 489 / downloads 0，S likes 111 / downloads 0（采集 11-21 09:00 Asia/Singapore）（上期 33 / 10）；L 从 Trending #122 升到 #12。downloads 仍为 0，可能与 HF 对该库的计数方式有关，待核。许可仍是 apple-amlr（仅限非商用研究）。
- 证据：[arXiv 2611.23226](https://arxiv.org/abs/2611.23226) · [HF apple/FastFrames-L](https://huggingface.co/apple/FastFrames-L)

###### F5. Sage S2.1 Flash：技术报告 v2 已改掉“S1.5”笔误；激活参数量仍无官方数字 · 更新

- arXiv 2611.21072 现在有 v2，提交于 2026-11-17 15:05 UTC / 11-17 23:05 Asia/Singapore（上期采集时已存在，当时漏看）。当前页面摘要里已没有“Sage S1.5 Flash”字样（上期保存的 v1 页面有 4 处），上期的笔误待核点可以关闭。
- HF 两个 repo 窗口内没有新 commit，license 元数据仍为空。likes 250 / downloads 1,068（采集 11-21 09:00 Asia/Singapore）（上期 97 / 337）；Trending #21 → #35。AA、LMArena 仍未收录；激活参数量仍只有第三方推算。
- 证据：[arXiv 2611.21072](https://arxiv.org/abs/2611.21072) · [HF internlm/Sage-S2.1-Flash](https://huggingface.co/internlm/Sage-S2.1-Flash)

###### F6. Kimi K3.1 Pro：官方 repo 和博客正文都没变；旧版 Kimi-K3 加了“新版本”指针 · 更新

- moonshotai/Kimi-K3.1-Pro 窗口内没有 commit（lastModified 仍是 2026-11-05 07:11 UTC）。likes 2,420 / downloads 64,576（采集 11-21 09:00 Asia/Singapore）（上期 2,197 / 53,224）；Trending #25 → #40。license other（kimi-k3.1-pro），开放权重，自定义许可。
- moonshotai/Kimi-K3 在 2026-11-20 02:36 UTC / 11-20 10:36 Asia/Singapore 提交 `1f5d44f794`“Add new_version pointer to Kimi-K3.1-Pro”，HF 页面会提示用户转到 K3.1 Pro。
- 博客 kimi.ai/blog/kimi-k3-1-pro：与上期逐段比对，只有导航栏变化（新增 Design、Plugins、Skills、Swarm 和模型菜单），正文未改。
- AA 46.5 不变，仍是开放权重第一。LMArena 文本榜虽刷新到 Nov 20，但改版后看不到它的名次（见榜单 B1）。
- 同名全量复制件又多 3 个，见文末冒名段。
- 证据：[HF moonshotai/Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3) · [kimi.ai 来源](https://www.kimi.ai/blog/kimi-k3-1-pro)

###### F7. Agnes：2.5-Pro-Theta 的基座和许可问题仍无回应；同一账号又发了一个 MiniMax-H3 视频改造实验 · 更新

- Agnes-AI/Agnes-2.5-Pro-Theta 窗口内没有 commit，卡片仍未声明基座。likes 59 / downloads 958（采集 11-21 09:00 Asia/Singapore）（上期 29 / 537）。AA 仍只有条目、没有分数（creator 仍记为 Sapiens AI）。上期待核“是否基于 Qwen3.8-Flash-Next（qwen-community-1.0）”没有新证据。
- 新 repo Agnes-AI/Agnes-Video-H3-MoE：createdAt 2026-11-20 08:39 UTC / 11-20 16:39 Asia/Singapore，权重 commit `2594d73ea4` 在 08:49 UTC。卡片自述是把 MiniMax-H3 FL2VA 第 15–34 块的 FFN 改成“1 个共享专家 + 8 选 1 私有专家”的 token 级 MoE，训练到第 60 步的实验检查点；它是“组合包”，内含原版 FL2VA 权重和 Router/LoRA 检查点，共 144.67GB。这次正确声明了 base_model MiniMaxAI/MiniMax-H3 和 minimax-h3-community-license，与 Agnes 2.5 Pro Theta 的做法形成对比。likes 0 / downloads 0，信号弱。
- 证据：[HF Agnes-AI/Agnes-2.5-Pro-Theta](https://huggingface.co/Agnes-AI/Agnes-2.5-Pro-Theta) · [HF Agnes-AI/Agnes-Video-H3-MoE](https://huggingface.co/Agnes-AI/Agnes-Video-H3-MoE)

###### F8. 热度变化：Haru-4B 升到 Trending #1；MiniMax-H3-Image 退到 #10 · 更新

- higurashi-ai/Haru-4B 仍只有 11-13 那一个 commit，likes 从 506 涨到 5,437、downloads 7,323（采集 11-21 09:00 Asia/Singapore），Trending #3 → #1（trendingScore 313）。Apache-2.0。上期的待核点（延迟口径、缺少标准化对比）仍无进展。
- MiniMaxAI/MiniMax-H3-Image 窗口内没有 commit，likes 1,702 / downloads 876,986（采集 11-21 09:00 Asia/Singapore），Trending #1 → #10。母模型 MiniMax-H3 只改了 README 的下载命令。
- 证据：[HF higurashi-ai/Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B) · [HF MiniMaxAI/MiniMax-H3-Image](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image)

---

##### 次条（新发布，信号弱或场景窄）

- **kyutai/AURA-5B / AURA-1.3B（+ Teacher-TalkVerse）**：Kyutai 的实时“音频驱动数字人”模型，输入一张肖像和语音流，逐块生成说话视频，是从 50 步双向教师蒸馏出的 4 步因果学生模型，只需当前块的音频、不用提前几秒看后文（BMVC 2026）。三个 repo 创建于 2026-11-18 15:11–15:13 UTC / 11-18 23:11–23:13 Asia/Singapore，权重 commit 都在 2026-11-20 14:13 UTC / 11-20 22:13 Asia/Singapore：AURA-5B 47.01GB（基于 snap-research/talkverse-s2v-5b，license other：snap-inc-non-commercial-license），AURA-1.3B 13.40GB、Teacher 7.01GB（cc-by-nc-4.0，基于 Wan2.1-T2V-1.3B）。都是非商用许可，非 OSI。likes 4 / 7 / 1，downloads 都是 0（采集 11-21 09:00 Asia/Singapore）。论文摘要称 AURA 5B 720p 流式 9.7fps、与教师质量相当且快 17 倍；卡片注明参考代码在单张 H100 上约 8fps，待核。配套数据集见 D3。kyutai 组织 HF 认证。[HF kyutai/AURA-5B](https://huggingface.co/kyutai/AURA-5B) · [arXiv 2611.26540](https://arxiv.org/abs/2611.26540) · [GitHub kyutai-labs/aura](https://github.com/kyutai-labs/aura)
- **apple/DepthPro2（S / B / L / H / focal / coreml）**：苹果 Depth Pro 的第二代，单目度量深度估计，主打边缘锐利和视频帧间稳定。主 repo 只放说明和素材（没有权重），权重分在四个尺寸 repo：S 24.3M、B 96.5M、L 334.0M、H 872.1M 参数，另有 23.5M 的焦距估计器 DepthPro2-focal（createdAt 2026-11-19 18:02 UTC / 11-20 02:02 Asia/Singapore）和 Core ML 版。这些 repo 大多 11-03 至 11-09 建库，但全部在 2026-11-20 11:28 UTC / 11-20 19:28 Asia/Singapore 被压成单个“init” commit（coreml 12:27 UTC），技术报告 arXiv 2611.26603 v1 于 2026-11-19 18:55 UTC 提交，判断为本窗公开。主 repo likes 125、Trending #16；各尺寸 likes 3–17、downloads 26–94（采集 11-21 09:00 Asia/Singapore）。license apple-amlr（Apple 机器学习研究许可，仅限研究用途），非 OSI。[HF apple/DepthPro2](https://huggingface.co/apple/DepthPro2) · [arXiv 2611.26603](https://arxiv.org/abs/2611.26603) · [GitHub apple-aiml-research/ml-depth-pro-2](https://github.com/apple-aiml-research/ml-depth-pro-2)
- **tencent/WeMM-Video 系列（2B / 4B / 9B / 35B-A3B，各带 FP8 / AWQ / GGUF / NVFP4）**：腾讯的中英双语“音视频联合理解”模型，能结合画面和原声描述事件、转写语音、推理。repo 在 11-17 08:53–08:59 UTC 建好，但 BF16 权重在窗口内才上传（35B-A3B 2026-11-20 03:57 UTC / 11-20 11:57 Asia/Singapore，9B 05:08 UTC），技术报告 arXiv 2611.26409 v1 于 2026-11-19 16:58 UTC 提交。35B-A3B 72.36GB、参数 36,177,564,536；9B 20.98GB。license apache-2.0，OSI 许可。热度很低：35B-A3B likes 21 / downloads 5，9B likes 7 / downloads 6（采集 11-21 09:00 Asia/Singapore）。卡片自报约 1.2T 多模态 token 预训练，基准待核。[HF tencent/WeMM-Video-35BA3B](https://huggingface.co/tencent/WeMM-Video-35BA3B) · [arXiv 2611.26409](https://arxiv.org/abs/2611.26409) · [GitHub Tencent/WeMM-Video](https://github.com/Tencent/WeMM-Video)
- **autotrust/hy4-flash-concise**：第三方对 Hy4 flash 做的“少思考”编辑版：用模型自身激活推出的秩一、无梯度编辑改写 9 个共享专家 down-projection，作者自测思考 token 少 37–55%，但代码和指令遵循准确率明显下降；另附 α=0.05 温和版和 v2 目录。createdAt 2026-11-19 09:34 UTC / 11-19 17:34 Asia/Singapore，49 个权重文件 494.15GB，沿用 tencent-hy-license，基座声明为 tencent/Hy4-flash 和 atakans/Hy4-flash-NVFP4。likes 174 / downloads 307（采集 11-21 09:00 Asia/Singapore）。属社区改造，不是官方版，效果待核。[HF autotrust/hy4-flash-concise](https://huggingface.co/autotrust/hy4-flash-concise)
- **AuroraAI-Research/Aurora2-400M-A20M**：个人研究者用单卡、100B token 从零预训练的 400M 总参 / 约 19M 激活 MoE 基础模型（32 路由专家 top-1 + 1 共享专家，训练序列长 2,048），没有指令微调。createdAt 2026-11-18 19:08 UTC / 11-19 03:08 Asia/Singapore，权重 commit 同时上传；likes 42 / downloads 643（采集 11-21 09:00 Asia/Singapore），Trending #72；apache-2.0。适合做小模型/MoE 教学和消融，组织背景不明。[HF AuroraAI-Research/Aurora2-400M-A20M](https://huggingface.co/AuroraAI-Research/Aurora2-400M-A20M)
- **Comfy-Org/LongCat-Video-Avatar**：ComfyUI 官方组织给上期收录的美团 LongCat-Video-Avatar-1.6 做的 ComfyUI 打包（int8 主模型 + 两个 rank128 LoRA + 文本编码器等），createdAt 2026-11-18 21:17 UTC / 11-19 05:17 Asia/Singapore，37.08GB，mit。likes 21 / downloads 3,345（采集 11-21 09:00 Asia/Singapore）。属分发版，降权。[HF Comfy-Org/LongCat-Video-Avatar](https://huggingface.co/Comfy-Org/LongCat-Video-Avatar)
- **mit-han-lab/Qwen3.8-27B-PEAR-DFlash2、inclusionAI/LingSante-Pulse-1.0**：前者是 MIT 韩松组给 Qwen3.8-27B 的 DFlash2 草稿模型（3.85GB，2026-11-19 05:01 UTC 上传），没有 README，likes 0；后者是蚂蚁 inclusionAI 的 16.7M 参数生理信号特征提取模型（mit，2026-11-20 09:12 UTC 上传），likes 3 / downloads 0（采集 11-21 09:00 Asia/Singapore）。信号都很弱，只记一笔。

###### 补记：窗口前发布、往期漏掉的（不算本期新发）

- **inworld/voice-isolator**：Inworld 的语音分离/去噪模型，HF Trending #11（trendingScore 164.5，likes 501，采集 11-21 09:00 Asia/Singapore），但 downloads 为 0。createdAt 2026-11-14 02:14 UTC / 11-14 10:14 Asia/Singapore，只有一次上传，2 个权重文件 0.49GB，apache-2.0。往期漏收。窗口内已出现至少 5 个原样复制件和 1 个同名不同模型，见冒名段。[HF inworld/voice-isolator](https://huggingface.co/inworld/voice-isolator)
- **Cloudflare/clairic（+ clairic-flash）**：Cloudflare 的 27B 多模态结构化输出模型：输入状态和带类型字段的 schema，逐字段返回值和置信分，覆盖抽取、数值估计和预测。10-16（clairic）/ 11-12（clairic-flash）建库，往期未收。窗口内 2026-11-18 20:58 UTC / 11-19 04:58 Asia/Singapore 两个 repo 同时有提交；clairic 的 commit `2c161be5cc` 在元数据里补写 base_model Qwen/Qwen3.8-27B，并把接口名从“System One: Predict”改成“System One: Extract”；clairic-flash 元数据的基座是 Qwen/Qwen3.5-9B。clairic likes 185 / downloads 246，Trending #44；clairic-flash likes 72 / downloads 318（采集 11-21 09:00 Asia/Singapore）；都是 apache-2.0。[HF Cloudflare/clairic](https://huggingface.co/Cloudflare/clairic)

---

##### 数据集

###### D1. Digitaluz/uzbek-language-corpus · 新数据集（odc-by）

- 判断：乌兹别克斯坦数字技术部（HF 认证组织 Digitaluz）发布的乌兹别克语文本语料，拉丁和西里尔两种文字都有，属政府官方开放的低资源语言数据，这类发布不多见。
- 来源记录：卡片写 5,637,052 篇文档、6,062,245,161 个词。createdAt 2026-11-18 14:02 UTC / 11-18 22:02 Asia/Singapore；v1.3 更新于 2026-11-20 04:36 UTC / 11-20 12:36 Asia/Singapore。likes 73 / downloads 877（采集 11-21 09:00 Asia/Singapore），数据集 Trending #6。license odc-by。
- 待核：去重和清洗方式、各来源占比只看到卡片自述。
- [HF 数据集 Digitaluz/uzbek-language-corpus](https://huggingface.co/datasets/Digitaluz/uzbek-language-corpus)

###### D2. alphaXiv/AgentAlphaXiv · 新数据集（cc-by-4.0）

- 判断：31 个实验室 12 周里让 agent 写研究报告的真实记录，含 916 篇 agent 写的研究和 9,052 条对话消息，适合研究“AI 科研助手”的实际用法和失败模式。
- 来源记录：createdAt 2026-11-17 23:56 UTC / 11-18 07:56 Asia/Singapore（窗口前几小时建库）；正式发布 commit 在 2026-11-20 09:21 UTC / 11-20 17:21 Asia/Singapore。likes 27 / downloads 374（采集 11-21 09:00 Asia/Singapore），Trending #27。alphaXiv 账号为普通用户号，非 HF 认证组织。
- 待核：参与实验室名单和授权方式只看到卡片自述。
- [HF 数据集 alphaXiv/AgentAlphaXiv](https://huggingface.co/datasets/alphaXiv/AgentAlphaXiv)

###### D3. kyutai/AURA-Dataset · 新数据集（cc-by-nc-4.0）

- 次条 AURA 的配套训练数据，985.67GB，非商用。createdAt 2026-11-18 15:13 UTC，数据上传 2026-11-20 14:13 UTC / 11-20 22:13 Asia/Singapore。likes 1 / downloads 0（采集 11-21 09:00 Asia/Singapore）。[HF 数据集 kyutai/AURA-Dataset](https://huggingface.co/datasets/kyutai/AURA-Dataset)

###### D4. inclusionAI/LingSante-MedGuard · 新数据集（许可元数据为空）

- 蚂蚁 inclusionAI 的医疗安全评测数据：卡片写 14,588 条风险样本、578 张图片，对应 arXiv 2611.25509。createdAt 2026-11-18 07:02 UTC / 11-18 15:02 Asia/Singapore；likes 2 / downloads 62（采集 11-21 09:00 Asia/Singapore）。HF license 字段为空，商用前需核实许可。[HF 数据集 inclusionAI/LingSante-MedGuard](https://huggingface.co/datasets/inclusionAI/LingSante-MedGuard)

###### D5. codepawl/cmu-mocap-glb · 新数据集（license other）

- 把 CMU 动作捕捉库 2,426 段动作重定向成 GLB 格式（约 10.5 小时，60fps），可以直接拖进 3D 引擎用。createdAt 2026-11-18 18:13 UTC / 11-19 02:13 Asia/Singapore；likes 36 / downloads 1,862（采集 11-21 09:00 Asia/Singapore），Trending #19。是第三方整理，原始数据的使用条款以 CMU 为准。[HF 数据集 codepawl/cmu-mocap-glb](https://huggingface.co/datasets/codepawl/cmu-mocap-glb)

###### 数据集附注

- **InternRobotics/GameRealm**：上海 AI Lab 具身组的游戏场景数据，createdAt 2026-11-18 09:17 UTC，cc-by-nc-4.0，downloads 23,771 但 likes 只有 2（采集 11-21 09:00 Asia/Singapore），卡片写分批发布、目前只放出一部分。[HF 数据集 InternRobotics/GameRealm](https://huggingface.co/datasets/InternRobotics/GameRealm)
- **JaimeMaLangue/JML-fon-speech-v1**：丰语（Fongbe，贝宁）语音数据，v1 于 2026-11-19 01:08 UTC 发布，cc-by-sa-4.0，likes 39，Trending #23。[HF 数据集 JaimeMaLangue/JML-fon-speech-v1](https://huggingface.co/datasets/JaimeMaLangue/JML-fon-speech-v1)
- **延续热度**：Vyber07/cyber-security（#1，gated: auto）、nvidia/USDCraft-10K（#2）、HubLabs/HubEgo-100K（#7，gated: auto，downloads 190,021）都是往期条目；google/physical-engineerings-last-exam（#5，10-18 建库，gated: auto，cc-by-4.0）是窗口前发布的，本期没有展开。

---

##### 榜单

###### B1. LMArena 文本榜：更新到 Nov 20；Gemini 4 Neon 首次上榜就排第 3，Claude Fable 5.2 (Max) 进前 10

- Nov 11 → Nov 20；总票数 9,122,174 → 9,213,799；模型 421 → 426。
- 前三：Gemini 4 Carbon (High) 1527（上期 1526）、Gemini 4 Argon (High) 1520（上期 1522）、新上榜的 Gemini 4 Neon (High) 1513。另一个新面孔 Claude Fable 5.2 (Max) 以 1503 排第 7。
- 上期第 15 的 Gemini 4 Hydrogen 和 Muse Spark 1.1 跌出前 15。
- 口径缺口：LMArena 页面改版，WebFetch 只返回前 15、性价比前沿和部分名次，没有完整表、置信区间和票数，Kimi K3.1 Pro、Inkling 2 Small 等开放模型的名次本期看不到，无法逐行 diff。性价比前沿里的开放模型：MiMo-V2.6-Pro 1481、GLM-5.3-Flash 1475、DeepSeek-V4-Pro 1458。
- [lmarena.ai 来源](https://lmarena.ai/leaderboard/text)（curl 403，WebFetch 可读；快照见 （采集证据快照）

###### B2. LMArena 视觉榜：更新到 Nov 20；Claude Fable 5.2 (Max) 新上榜第 2

- Nov 8 → Nov 20；票数 1,567,670 → 1,606,278；模型 166 → 168。第 1 仍是 Claude Fable 5 (High) 1309；新上榜 Claude Fable 5.2 (Max) 1305 排第 2。另一个新增模型在改版后的页面里无法确认是哪一个。
- [lmarena.ai 来源](https://lmarena.ai/leaderboard/vision)

###### B3. LMArena 文生图榜：没有更新

- 仍是 Nov 16 版（6,988,405 票，86 个模型）。MAI-Image-2.7 #4，MiniMax-H3-Image #24，与上期相同。
- [lmarena.ai 来源](https://lmarena.ai/leaderboard/text-to-image)

###### B4. AA 文生图榜：无增减

- 116 行，与上期相比没有新增或移除。第 1 仍是 GPT Image 2.6 Sunburst (max) 1262±14（上期 1261）；MAI-Image-2.7 1216；MiniMax-H3-Image 排第 27，1066。
- [artificialanalysis.ai 来源](https://artificialanalysis.ai/text-to-image/arena?tab=leaderboard)

###### B5. AA 图像编辑榜：无增减

- 86 行，没有新增或移除。第 1 仍是 MAI-Image-2.7 1215；MiniMax-H3-Image 排第 14，1136。
- [artificialanalysis.ai 来源](https://artificialanalysis.ai/text-to-image/arena?tab=leaderboard-image-editing)

###### B6. AA Intelligence Index v5：Gemini 4 Neon 61.4 排第 3；Tencent Hy4 被改标为开放权重，成为开放权重第 2

- 新增 Gemini 4 Neon (Xhigh) 61.4，release 2026-11-18，闭源，默认视图排第 3。前两名不变：Claude Fable 5.2 64.6、GPT-6.2 Astra 62.1。
- Tencent Hy4 的标记从“专有”改成“开放权重（commercial-license）”，分数仍是 34.6，直接成为开放权重第 2。开放权重排序：Kimi K3.1 Pro 46.5 > Tencent Hy4 34.6 > DeepSeek V4.1 Flash 1017 32.6 > GLM-5.3 31.7 > Inkling 2 Small 30.6 > MiMo-V2.6-Pro 29.9。
- Qwen3.8 Max (0902) 33.7 退出首页默认视图。Inkling 2 Mini 有独立页面（20.1），但不在默认视图里。Hy4 flash 本次没有拿到 AA 单页（抓取失败），是否已有分数待核。
- [artificialanalysis.ai 来源](https://artificialanalysis.ai/models) · [artificialanalysis.ai 来源](https://artificialanalysis.ai/models/gemini-4-neon) · [artificialanalysis.ai 来源](https://artificialanalysis.ai/models/inkling-2-mini)

---

##### 延续热度 / 降权 / 冒名

###### HF Trending 模型前 10 点评（trending API 08:50 Asia/Singapore；likes 来自 09:00 Asia/Singapore 快照）

  1. higurashi-ai/Haru-4B：见 F8，没有新 commit。
  2. harness-hub/Qwen3.8-27B-pi-adapted：见 F3，作者已更正数字。
  3. Qwen/Qwen3.8-27B：老模型。
  4. thinkingmachines/Inkling-2-Mini：本期主条 2。
  5. Sentinel7/h3：likes 263、downloads 0、没有 README，是批量上传的 NSFW LoRA 文件夹，降权。
  6. Lightricks/LTX-2.5：老模型。
  7. unsloth/Inkling-2-Mini-GGUF：社区量化分发，likes 193 / downloads 0（HF 对 GGUF 的计数可能有延迟）。
  8. tencent/Hy4-flash：本期主条 1。
  9. sensenova/SenseNova-Loop-9B：见 F1。
  10. MiniMaxAI/MiniMax-H3-Image：见 F8。

###### 降权（只改 README / 文档，或属于改包）

- 只改说明、模板或文档、不动权重：Aleph-Alpha Kolibri-1（11-19 README）、Muse-Glimmer（chat template）、LFM3-Omni-2B OpenVINO 版（README）、nvidia/Qwen3.8-27B-NVFP4-QAD（README）、Edge0（文档）、KORMo-Web（文档）、Ming-3.0-tts（补 LICENSE 文件）、KittenML int4 ONNX。
- Uncensored / heretic / abliterated 改包：alesha-pro/Hy4-flash-Uncensored-GGUF、trohrbaugh/Hy4-flash-heretic、OpenUncensored/Inkling-2-Mini-Uncensored、chatrlabs/Qwen-Image-2.1-Uncensored-Omni-Quantized（Trending #13）、satellitedown 的 SenseNova abliterated GGUF 等，过滤。

###### 冒名 / 同名复制（本地 （采集证据快照），按 LFS sha256 与官方 tree 比对）

- **组 1：Hy4 / Hy4-flash 原样复制**：FamilyOrang/Hy4（250/250 个 LFS 文件哈希与官方相同）、FamilyOrang/Hy4-FP8（251/251）、FamilyOrang/Hy4-flash（153/153）、FamilyOrang/Hy4-flash-FP8（153/153）、blearyhope/Hy4（250/250）、akshay42/Hy4-flash（153/153）。都创建于 11-19 至 11-20，downloads 0–26，没有写 base_model，卡片照抄官方。腾讯许可允许再分发，不判定为恶意，但容易让人误以为是官方 repo。
- **组 2：Kimi-K3.1-Pro 又多 3 个**：FamilyOrang、Infinix-ai、Jattt6789 三个同名 repo，98/98 个 LFS 文件与官方相同，downloads 0–39。加上往期记录，累计 18 个。
- **组 3：本期其他新模型的复制件**：nokkela-ai/Inkling-2-Mini（4/4）、ml-resources/DaisyRose-27B（20/20）、NarsAI/Aion-1.0-Instruct-2.3B（3/3）、Renedffd/FastFrames-L（13/13）。注意 FastFrames 是苹果非商用许可，复制件同样受约束。
- **组 4：voice-isolator 复制件，以及 salgr 假模型的新风险**：Infinix-io、0x3、yacan1585、orz99、ml-resources 五个 voice-isolator（2/2 文件与 inworld 官方相同）。Trelis/voice-isolator 同名但是另一个模型（基座 weya-ai/hush，polyform-small-business 许可，gated），不是复制件。salgr 账号自 11-16 以来没有新建 repo，但名下 11 个假“闭源模型”repo 里有 salgr/Gemini-4-Neon（以及 Gemini-4-Carbon、Claude-Opus-5.5、GPT-6.3-Astra、Claude-Fable-6.9、Claude-Mythos-6.9、GPT-6-Cyber 等）。Gemini 4 Neon 本周成了真实的 Google 模型（AA 61.4、LMArena 文本 #3），搜这个名字的人可能被引到这个假 repo，需提醒读者。[HF salgr/Gemini-4-Neon](https://huggingface.co/salgr/Gemini-4-Neon)

---

##### 口径、缺口与校验

- 统计口径：likes/downloads 统一取 2026-11-21 09:00 Asia/Singapore（01:00 UTC）快照（采集证据快照）；Trending 名次取 08:50 Asia/Singapore 的 trending API；时间同时给 UTC 和 Asia/Singapore；“权重 commit”指改动了 safetensors/gguf 等 LFS 权重文件的 commit。
- 窗口内新建 repo 总量：模型 11,468 个、数据集 5,404 个（createdAt 分页统计）。
- 未能拿到 / 未绕过：
  - 匿名 401：SenseNova-Loop-9B 的 commits 接口和 README、Trelis/voice-isolator 及其 duplex 数据集、HubEgo 的数据文件、asgmodels 的 Aion 源 repo（API 401）。
  - Hy4 的准确公开时间仍不确定（repo 10-29 建库，GitHub 和许可资料不足以确定上线时刻）。
  - LMArena 改版后拿不到完整表，开放模型名次缺失。
  - AA 的 tencent-hy4 单页抓取失败。
  - 外链排除：hy.tencent.ai（反爬挑战页）、kyutai.org/aura（HTTP 500）、mocap.cs.cmu.edu（超时）。
- 待核总表：所有模型卡和技术报告里的基准分数；SenseNova-Loop-9B 的显存数字；FastFrames downloads 一直为 0 的原因；AURA 9.7fps；Agnes 2.5 Pro Theta 的基座与许可；Hy4 flash 是否已有 AA 分数。
- 校验：全部 HF id 的 API 200 检查见 （内部证据存档）；外链检查见 `link_check.json`（LMArena 对 curl 返回 403，WebFetch 可读，单独注明）；证据目录 （内部证据存档）（lb/、ext/、suspect/、commits/、cards/、api/）。

