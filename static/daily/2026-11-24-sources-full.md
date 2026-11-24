# 2026-11-24 AI行业动态：全量原始素材

本期信息窗口从 2026 年 11 月 21 日 09:09 起，至 11 月 24 日各来源的实际采集截止（约 08:50–09:13），时区为 Asia/Singapore。本文保留四路采集到的全量原始摘要与来源链接，不是深读成稿，也不意味着所有候选均已独立复现。正文另见[本期深读](https://guige.ai/guige-ai-site/daily/2026-11-24/)。

- 研究与官博：官博约截止 11 月 24 日 09:12；包括研究汇总、官方原文摘录和论文候选三份材料。arXiv 在 Asia/Singapore 的 11 月 21 日、22 日为周末，按常规无批；11 月 23 日（周一）批的新稿与交叉列表完整；11 月 24 日（周二）批在采集截止时已开始出号但列表尚未放全，未纳入本期，不代表该批没有更新。扫描自 2611.26630 起，止于 2611.27986，下期从 2611.27987 续扫。
- X 公开动态：约截止 08:50；首页时间线实际覆盖约 11 月 23 日 09:49 至 11 月 24 日 08:43，此前约 48 小时以官方账号检索、公开检索与官方页面补齐，不代表全量时间线。
- GitHub 项目与发行：榜单与仓库快照约为 08:48；日榜、周榜不等于本期净增。
- 模型与数据集：HF 统计快照约为 08:57，热榜读取约 08:48，下载量为 HF 近 30 天口径；LMArena 完整表取自其官方公开的榜单数据集。保留模型卡、权重提交、许可、榜单与同名仓库记录。

原始材料之间可能保留不同取舍，以下说明用于避免误读：黎曼猜想一事，只能确认 Lean FRO 与 Mathlib Initiative 的联合声明称约 1,700 万行 Lean 证明可编译通过（并列出所证为 Mathlib 标准陈述、多个独立检查器接受等标准）；人类可读性、后续质疑与合作分工均待核，不等于数学界已公认。英伟达董事会恢复黄仁勋总裁、CEO 与董事职务有 8-K 与新闻稿；NVDA 11 月 23 日收 $165.05，较 11 月 20 日收盘 $125.53 上涨 31.48%；SEC 会计调查（路透社独家、匿名消息源）、总统亲自介入、市值换算等说法均待核。本篇不做投资判断。GPT‑6 Cyber 与“948 个内核提权漏洞”研究文落款 11 月 4 日 / 5 日，本窗口只是官方账号再次推送，不是新发布。Pachocki《Perplexity and Intelligence》中的行业共同上限是作者提议，不是已生效的规则；文中困惑度数字均为 OpenAI 内部数据集上的官方自报。许可：Xing4.1-Preview 与 Kolibri-1.1 为 Apache-2.0，Ling-3.2-air 与 LingSante-3.1-flash 为 MIT；Ling-3.2-air 上下文长度 AA 写 1M、config 写 262,144，待核；所有模型卡跑分均为自报。Unsloth 的解码与训练提速倍数为其自称；Transformers v5.24.0 把 past_key_values / cache_params 改名为 cache，属破坏性变更。冒名仓库与假仓（包括“预激活安装包”“修改器”类 HTML 仓、LingSante 等官方仓库的整仓复制件）只作安全提醒，原材料中的相关记录照录，不构成推荐，也不等于收录；星数可信度待核的新仓本期未收录。

除去内部协作名称、个人隐私、内部本地证据路径、来源标记和不宜公开的安全操作细节，正常来源与候选保留；未读、待核、自报与不收录理由照录。以下材料不是投资、上线或商业授权建议。


## 研究与官博

### 研究汇总

#### 研究素材包 · 2026-11-24（窗口 2026-11-21 09:09 → 11-24 ~09:12 Asia/Singapore）

> 官博 3 条 + arXiv 5 条（共 8 真重点）。数字标 来源记录 / 官方自报 / 作者自报 / 待核。原始摘录见同目录 labs-raw.md、arxiv-raw.md。
> arXiv：Asia/Singapore **11/21、11/22 无批**（周末常规日程，来源记录）；**11/23（周一）批**新稿+交叉列表完整（CS catchup 与 pastweek / `/new` 均为 showing N of N）。**11/24（周二）批已开始出号但列表未齐**：约 09:10–09:12 Asia/Singapore（arXiv localtime **Mon, 23 Nov 2026 20:10 EST**，已过 20:00 公告点）abs 探测 **2611.27987+** 为 200，但 CS catchup 仍是 Total 0 / No updates，`/new` 仍显示 Monday, 23 November 2026，export API 对已 200 的新号返回 0 条，且 28190、28201 等号仍有 404 空洞。**不要**写成该批无更新，也**不要**把未齐的新号算进本期完整宇宙。本期完整扫描宇宙仍止于周一全站上沿 **2611.27986**。扫描自 **2611.26630** 起。续扫 **2611.27987+** 与周二正式 listing（须等 showing N of N）。感恩节（2026-11-26）尚未到，留给下期日程核验。
> 网络安全、生物与对齐条目只写结论与官方/作者数字，不写利用/合成/实验步骤。不自写主线编号。数字均保留设定与基线，**勿**无条件跨模型、跨硬件、跨基准比较。

##### 官博

###### 1. OpenAI：Perplexity and Intelligence
OpenAI 首席科学家 Jakub Pachocki 在官网研究/安全栏目公开内部预训练 perplexity（文中等价于 cross-entropy / log-perplexity）轨迹，并主张把它做成跨实验室可对照的进度尺，用来讨论能力涌现和开发节奏。是本窗最重要的官方进度与安全治理论述，也是读「压缩进度 vs 下游榜」时的硬参考；数字全部绑在 OpenAI 自用的持出集上，**不能**直接拿去跟别家比。
- News RSS `Sun, 22 Nov 2026 00:00:00 GMT` → **2026-11-22 08:00 Asia/Singapore**（来源记录）。页面分类 Research / Safety，作者署 Chief Scientist。
- **URL**: [openai.com 来源](https://openai.com/index/perplexity-and-intelligence/)（经 308 后 HTTP 200）
- 口径（均为官方自报的内部测量与作者论述，除非另注）：主要持出集自 GPT‑3.5 起取自内部代码库的固定快照（文内脚注）。GPT‑3.5 的 log-perplexity 约 **0.99**（流利对话、原 ChatGPT 基础）；GPT‑4 约 **0.91**（能较有效使用思维链）。写到已到 **0.8** 以下，并称在网络安全与数学等领域看到「变革性」能力（只记这条结论，不写能力细节）。称换到约 **0.76** 的模型后，开放数学问题开始连续出突破性结果。作者预期进入约 **0.68–0.7** 窗口还会有新的变革性能力，同时现有为主的对齐审计方式会进一步变差、评测与训练察觉会上升。文中建议实验室共同设定以 perplexity 等可跟踪指标为基础的开发上限，在监控与理解能力达到明确里程碑（文中举例：思维链监控的后继方案）之前不要越过。作者也列出该指标的局限：跨实验室数据不同、不直接对应下游任务、解释不了思维链等预训练之外的进展、以及未知的数据熵下界。
- 关于自动化：作者认为 2027 年就「有可能」出现类似的预训练算法洞察雪崩，但这是展望不是预测承诺。文中提到 2026 年损失曲线变陡，主要归因于长期研究与算力投入，自动化只占较小部分；最近的模型已有来自 AI 的有意义设计贡献。文中把「完全递归自我改进且无人监督」写成应当避免的状态，以保持人类控制。
- **局限**: 个人署名的立场文，虽发在官网；数字是内部代码库 perplexity，作者自己写明跨实验室不好比。勿把 0.76 / 0.68–0.7 写成已公开的某款产品型号分数，文中没有把这些阈值点名到对外产品名。
- **标注**: 来源记录 / 官方自报。

###### 2. Google DeepMind：用智能体团队与形式化验证加快量子算法
DeepMind 与 Google Quantum AI 合作，用 Gemini 4 智能体团队改进已知量子算法，并用 Lean 形式化证明结果；同步开源 Lean 库、问题说明和已验证解。是本窗最大的官方科学发现长文。配套论文 arXiv **2611.09822**（题为 *Discovering formally verified quantum programs with AI*）API 首发 `2026-11-06T18:08:06Z`，**不属于**本期 2611.26630 起的扫描宇宙；本期收入的是 11/24 的官方博客与开源发布。
- 页面 `datePublished` `2026-11-23T17:00:00+00:00` → **2026-11-24 01:00 Asia/Singapore**（来源记录）。DeepMind RSS `Mon, 23 Nov 2026 16:59:40 +0000` → **00:59 Asia/Singapore**。文首日期 November 23, 2026。署名 Sergey Shirobokov、Ben Jaderberg、Ryan Babbush；致谢列出完整作者名单，并写明是 DeepMind 与 Google Quantum AI 合作。
- **URL**: [deepmind.google 来源](https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/)（HTTP 200）
- **论文**: [arXiv 2611.09822](https://arxiv.org/abs/2611.09822)（HTTP 200，本窗见到 v3）
- **代码**: [GitHub google-deepmind/formal-quantum-computation](https://github.com/google-deepmind/formal-quantum-computation)（HTTP 200）
- 要点（官方自报）：独立智能体团队分别找算法改进，经 Lean 验证后写入共享笔记本，每四小时开一次「虚拟会议」交换想法。惯性约束聚变中一项性质的计算：综合计算成本（量子比特与操作的组合指标）降为原来的 **1/11.8**，纠错后内存从 **5,650** 降到 **4,338** 个量子比特。一种常见光敏分子的量子模拟便宜 **8×**。药物代谢关键酶 Cytochrome P450：改进 **2.5×**，内存从 **481** 降到 **333** 个量子比特。某个具体实现的 Grover 算法 **2.57×** 加速；arcsin 例程 **290×** 加速。文中同时写明：真要跑这些科学模拟，所需资源仍可能高于第一代纠错量子计算机很可能具备的水平，但改进幅度可观。
- **局限**: 数字来自官方博客对论文结果的转述，未在本包逐表深读 09822 PDF。不能把单项加速外推成通用量子优势，也不能写成已经能在现有量子硬件上跑这些电路。
- **标注**: 来源记录 / 官方自报。

###### 3. Anthropic：Working with AI
Anthropic 经济团队对 58 家企业客户做了 66 场访谈，描述公司如何采用 Claude、卡在哪里、以及怎样围绕模型重组岗位。是本窗唯一一篇新的官方劳动/采用研究，适合和「AI 是否在裁员」这类外部叙事对读；结论全部是访谈自报，不是就业普查。
- 页面 `publishedOn` **2026-11-23**（日级）。CMS `_createdAt` `2026-11-23T18:46:09.484Z` → **2026-11-24 02:46 Asia/Singapore**，`_updatedAt` `2026-11-23T22:13:27.525Z` → **06:13 Asia/Singapore**（来源记录）。对外首次可见的精确时刻 **待核**，按日计已落入本窗。
- **URL**: [anthropic.com 来源](https://www.anthropic.com/research/working-with-ai)（HTTP 200）
- **官方 PDF**: [assets.claude.com 来源](https://assets.claude.com/0cb09418f04d09baf72922e53a3f17383ef838c9.pdf)（HTTP 200）
- 作者：Nathan Wilmers、Maxim Massenkoff、Peter McCrory（Economics / Labor market）。
- 要点（官方自报）：受访对象认为，多数 AI 用途是靠提高产出、而不是靠砍成本来创造价值，既加速原有工作，也带来新的产品与服务改进；编码智能体越来越多被用到非技术岗位。访谈里很少看到由 AI 自动化驱动的**国内**裁员；虽然有公司因 AI 扩招，但**多数**公司因 AI 而少招人，不少还减少了对承包商的使用，尤其是离岸承包商——文中把后者写成国际商务服务行业可能的早期预警。瓶颈包括专家抵制、以及编码变快之后代码审查、销售和战略决策跟不上。单纯自上而下自动化容易带来岗位不安全感、监控担忧和专家抵制；只发工具等自下而上采用，则会遇到采用不均和单任务用法。访谈里价值最高的用法，涉及对岗位与工作流的实质性重组：拓宽个人职责、把人调到模型做不了的瓶颈任务、为非开发者提供编码基础设施、并扩大内部业务数据的获取。
- **局限**: 样本是 Anthropic 的企业客户，不是随机雇主调查；「很少裁员 / 多数少招」不能外推到整个经济。主包数字取自摘要与正文开头，未逐节核对附录表。
- **标注**: 来源记录 / 官方自报。

##### arXiv

###### 4. 2611.26809 Search From the Start: Search-Native Pretraining for Language Models
链接：[arXiv 2611.26809](https://arxiv.org/abs/2611.26809)  
提交/公布：API published `2026-11-19T20:58:34Z` → 2026-11-20 04:58 Asia/Singapore；**Asia/Singapore 归属 11/23**（Mon 新稿，主类 cs.CL；兼 cs.AI、cs.LG）  
机构证据：PDF 首页机构行作「EPFL」「University of Toronto」，通讯 `（机构署名邮箱略）`、`（机构署名邮箱略）`（来源记录）。五位作者未在页眉逐人上标，**不要**把 Colin Raffel / Martin Jaggi 拆到未写明的第三家单位。作者：Kaustubh Ponkshe、Gyung Hyun Je（共同一作）、Stefan Taga、Colin Raffel、Martin Jaggi。  
人话：预训练不再只预测静态文本，而是在普通语料里插入检索查询和本地索引返回的网页，让模型在预训练阶段就学会发起搜索并引用证据（QueryLM）。  
为何重要：本窗最清楚的预训练范式论文之一；作者称 1.4B 的 QueryLM 在所测知识型任务上持续达到或超过 FLOP 对齐的 3.3B 常规预训练基线，而且这一优势在双方都做监督微调之后仍然在。  
对谁有用/深读：检索增强预训练、工具使用的前置、知识型 QA、后训练能不能补上预训练没教过的搜索能力。  
主要数字与条件/局限（作者自报）：语料为 Wikipedia 与 DCLM-Edu，模型规模 360M 到 3.3B。作者称在全部知识密集型任务上，1.4B QueryLM 持续击败或打平 FLOP 对齐的 3.3B 基线；并称所测后训练程序没有完全补回预训练阶段形成的能力。文中写明释放训练产物（checkpoint 与数据），但 PDF 首页「Training artifacts are available at .」未给出可核验 URL，**产物链接待核**，本包不编造地址。不能把 1.4B 对 3.3B 写成无条件「小模型全面超过大模型」，对照是 FLOP 对齐、带搜索的设定，且任务范围由作者定义。  
标签：**真重点** · 来源记录 / 作者自报

###### 5. 2611.26863 LLMs Memorize Their Own Hallucinations During Post-Training
链接：[arXiv 2611.26863](https://arxiv.org/abs/2611.26863)  
提交/公布：API published `2026-11-19T22:28:14Z` → 2026-11-20 06:28 Asia/Singapore；**Asia/Singapore 归属 11/23**（Mon 新稿，主类 cs.CL；兼 cs.LG）  
机构证据：PDF 首页两位作者均署 Cornell University，通讯 `（机构署名邮箱略）`、`（机构署名邮箱略）`（来源记录）。应写成 **康奈尔大学**。作者：Anirudh Atmakuru、Tanya Goyal。  
人话：如果把为数学和代码设计的结果奖励、假设与回退等推理训练配方，直接用到知识问答上，模型可能会把推理链里自己编出的错误事实记住。  
为何重要：给「推理配方外溢到知识任务」提供了一条可测量的失败路径，适合和本期 OpenAI 把 perplexity 当进度尺、以及上期后训练/幻觉讨论配读。  
对谁有用/深读：知识任务上的 RL 后训练、幻觉来源、拒答/弃答、推理痕迹与最终答案不一致时的训练信号。  
主要数字与条件/局限（作者自报，只写结论）：六个开源模型、两个模型族、两种架构。训练中被强化的自编幻觉，事后召回平均上升 **4.83%**；未给训练信号的自编幻觉只升 **0.17%**。模型甚至会记住推理里已经收回的错误事实。记错在最难的训练题上最强；一旦某条幻觉得到奖励，之后对该内容弃答的可能性平均再降 **7.23%**。数字绑在作者的开源模型与协议上，不能直接外推到未测的前沿闭源模型。不写提取或构造步骤。  
标签：**真重点** · 来源记录 / 作者自报

###### 6. 2611.27116 CoEvoBench: Can LLMs Drive Recursive Co-Evolution of Agentic Systems?
链接：[arXiv 2611.27116](https://arxiv.org/abs/2611.27116) · 代码 [GitHub AlibabaResearch/CoEvoBench](https://github.com/AlibabaResearch/CoEvoBench)（HTTP 200）  
提交/公布：API published `2026-11-20T04:40:59Z` → 2026-11-20 12:40 Asia/Singapore；**Asia/Singapore 归属 11/23**（Mon 新稿，主类 cs.AI）  
机构证据：PDF 首页「1 Zhejiang University 2 Alibaba Group 3 Shanghai Jiao Tong University」，通讯 `（机构署名邮箱略）`、`（机构署名邮箱略）`（来源记录）。应写成 **浙江大学 + 阿里巴巴 + 上海交通大学**，不要写成单一的阿里论文。作者：Chuan Xiao、Baojie Wang（共同一作）、Haizhao Fan、Hongzhe Du、Xander Xu。  
人话：把大模型当成「研究员」，在 24 小时预算里共同改目标智能体的模型权重和 harness（工具与环境之间的中介代码），看能不能一轮轮把系统改进续下去。  
为何重要：把递归式系统改进（作者明确写成一种可测的 RSI）从口号收成受控基准；作者的结论是：现在的模型能做出很强的第一轮改进，但还不能把改进后系统的反馈稳定变成下一轮增益。适合和本期 OpenAI 关于自动化参与预训练的讨论对读。  
对谁有用/深读：智能体 harness 与模型的联合优化、研究型智能体评测、长程编码 vs 交互任务上的自我改进。  
主要数字与条件/局限（作者自报）：五个智能体领域，统一的基座模型和初始 harness，24 小时训练/修改预算，提交模型–harness 对，在单独测试任务上打分。五个前沿「研究员」模型中，最强的缩小了与指令微调参考系统之间「五分之四以上」的差距；协同进化在交互任务上更成功，在长程编码上很少成功。摘要未点名这五个模型，**勿补**。不能把「缩小五分之四差距」读成已经实现稳定的递归自我改进，作者的判断正好相反。  
标签：**真重点** · 来源记录 / 作者自报

###### 7. 2611.26637 SDG: State-Dependent Gating at Chunk Boundaries for Linear Attention
链接：[arXiv 2611.26637](https://arxiv.org/abs/2611.26637)  
提交/公布：API published `2026-10-16T17:49:16Z`（提交较早）；**Asia/Singapore 归属 11/23**（Mon **交叉**列表，主类 stat.ML；兼 cs.CL、cs.LG）。全站号 2611.26637 落在 CS 新稿段（26643–27978）之前，但是本三科交叉宇宙的一部分（来源记录）。  
机构证据：PDF 首页「1 Peking University, 2 Meituan Inc.」；Renjia Deng 标 1,2，并写明「Work done during the internship at Meituan Inc.」；通讯 Kun Yuan，邮箱 `（机构署名邮箱略）`（来源记录）。应写成 **北京大学 + 美团**（邓为美团实习）。作者：Renjia Deng、Yuxi Liu、Yutong He、Xue Wang、Kun Yuan。  
人话：现有门控线性注意力的遗忘系数往往不直接读本层记忆；SDG 改成根据一个 chunk 内记忆的变化，在 chunk 边界做逐元素、依赖状态的门控，同时保留 chunk 内并行。  
为何重要：给 Gated DeltaNet、Kimi Delta Attention、Gated DeltaNet-2、Mamba-3 这类当代线性/混合结构补了一种仍兼容分块核的状态反馈遗忘；是本周一交叉列表里最值得读的架构文。  
对谁有用/深读：线性注意力与混合架构、长上下文检索、分块并行核。  
主要数字与条件/局限（作者自报）：在 1.3B 的线性注意力和混合模型、**100B** token 训练上，作者称语言建模、常识推理、合成与真实检索、长上下文理解都有提升。摘要**没有**给出可转写的绝对分或百分点，本包不补表内数字。作者自报代码 [GitHub lovekdl/SDG](https://github.com/lovekdl/SDG)，本窗访问为 **HTTP 404**，**不把该链当作已核验可点链接**。  
标签：**真重点** · 来源记录 / 作者自报

###### 8. 2611.27910 Decision Columns as an Index: Interpretable Embeddings for Explainable Entity Matching and Search
链接：[arXiv 2611.27910](https://arxiv.org/abs/2611.27910)  
提交/公布：API published `2026-11-20T17:48:55Z` → 2026-11-21 01:48 Asia/Singapore；**Asia/Singapore 归属 11/23**（Mon 新稿，主类 cs.IR；兼 cs.AI、cs.DB）  
机构证据：PDF 首页三位作者均署 Microsoft，通讯均为 `@microsoft.com`（`（机构署名邮箱略）`、`（机构署名邮箱略）`、`（机构署名邮箱略）`）（来源记录）。页眉写的是 **Microsoft**，**未**出现 Microsoft Research 字样，本包按印刷单位写，不改写成 MSR。作者：Aadharsh Kannan、Robert Bruckner、Phil Bernstein。  
人话：把一组自然语言问题的校准回答（是 / 否 / 未陈述）当成可解释的向量坐标，用来做实体匹配和检索，并能精确解释为什么两条记录被判为同一实体。  
为何重要：本窗少有的大厂系统/数据集成论文，针对智能体要改业务记录时「必须说得清依据」的需求；作者把它定位成稠密检索旁边的可读通道，而不是替代品。  
对谁有用/深读：实体匹配、企业检索、可解释嵌入、用失败案例加问题而不重编码整个语料。  
主要数字与条件/局限（作者自报）：评测在 WDC Products 与 STaRK-Amazon。作为 retrieve-then-verify 匹配器的候选生成，问题空间与稠密检索在统计上相当，同时能为接受的匹配提供精确解释。根据检索失败设计的新问题，可在不重编码已有回答的情况下把 MRR 提高到原来的 **三倍**。搜索任务上，推断「合适结果应具备的属性」优于只编码字面请求；问题空间与稠密分数结合能改善检索，但**没有**达到作者预先设定的置信阈值。一个小网络可把已有稠密嵌入映射成完整可解释向量，作者称用几千行已标注数据回填语料，成本大约是原来的 **1/200**。不要把「三倍 MRR」或「1/200 成本」写成通用 SOTA。  
标签：**真重点** · 来源记录 / 作者自报

##### 备选（不挤主包）

- Google Research 博客 [Supercharging transformer residual connections](https://research.google/blog/supercharging-transformer-residual-connections/)（RSS **11-24 01:21 Asia/Singapore**）：介绍 ICML 2025 论文 DeepCrossAttention（arXiv [2502.06785](https://arxiv.org/abs/2502.06785)，HTTP 200）。官方自报可达同等质量且最多约 **3×** 更快、参数可少 **30–40%**。是旧文新博，不当本期新结果。
- OpenAI + Cisco [Shirudo](https://openai.com/index/introducing-shirudo/)（RSS **11-24 05:20 Asia/Singapore**）：开源 Linux 运行时防护，仓库 [GitHub shirudo-dev/shirudo](https://github.com/shirudo-dev/shirudo)（HTTP 200）。只记「受控测试中 Codex 生成的盾在不重启的情况下挡住了对运行中 Elasticsearch 的利用尝试」这一官方结论，不写利用或防护构造细节。产品/安全工程，不进研究主包。
- **2611.26835** IBM Research，NeurIPS 2026：用非扩展门控连分数替换前馈层，代码 [GitHub IBM/CoFrNets](https://github.com/IBM/CoFrNets)（HTTP 200）。摘要仅称在 GPT‑2 / Llama‑3 / Mamba‑2 / nano Llama-MoE 上相当或明显好于前作、吞吐更高，**无**可转写的绝对分。
- **2611.27734** AutoOntologyBench：杜伦大学 + 上海财经大学 + 北京协和医学院/协和医院 + 阿里达摩院。19,947 项任务；作者称在检索之上叠加智能体自建本体可多 **6.1** 分，但仍落后专家参考 **13.0** 分。文中提及的 NVIDIA / Palantir / AWS 是相关产业实践，**不是**作者单位。
- **2611.27759** DPMA：Ikerlan、巴斯克大学、剑桥、SOFAIR、Flower Labs 等合作的 MoE 压缩。作者称在 75% 专家削减下，对每个被测模型都优于最强基线，最多高 **6.7** 个百分点。

##### Apple 补录备忘（不是本期新发）

对照上期记录，本期 `/research` 全列表仍为 **1194** 条。按 `published` 日期，**2026-11-21 及以后为 0 条**；11-20 仍是已在上期报告的 Depth Pro 2。上期已报的 Split-and-Scale（11-16）及更早条目不再重复。

##### 覆盖缺口

- 官博：OpenAI News RSS、Anthropic 研究页、DeepMind / blog.google / Google Research RSS、Apple `/research` 全列表、MSR 博客与 feed、Meta 研究博客与 about.fb、Amazon Science RSS、Thinking Machines 博客与新闻页、NVIDIA 工程双 feed 与研究门户、OpenAI / Anthropic Alignment，本窗均已成功访问（非缺访问）。
- DeepMind 量子一文的数字取自官方博客，未逐表深读 2611.09822 PDF。Anthropic *Working with AI* 主包取自摘要与正文开头，未逐节核对附录。OpenAI perplexity 文没有把内部阈值点名到对外产品型号。
- blog.google 主 RSS 仍然偏短，已用 models / developer-tools 分类 RSS 与 DeepMind、Google Research RSS 补扫；消费类短帖仍可能被挤出，但不影响本窗三条研究长文。
- Apple RSS 只有 10 条，完整性以 `/research` 全列表 1194 条为准。
- arXiv：Asia/Singapore **11/21–11/22** 无批；**11/23** 新稿+交叉已完整；替换稿未当新条目精读。**11/24** 批已开始出号但列表未齐，本期完整宇宙不含这些新号；续扫 **2611.27987+**。
- 未把缺访问写成无更新。窗内无新研究长文的机构：Apple、Microsoft Research 官方博客（本窗有一篇署名 Microsoft 的 arXiv，已进主包，页眉未写 MSR）、Meta AI 研究博客（about.fb 有一篇开放权重医疗应用综述，不是新模型或新方法）、OpenAI Alignment、Amazon Science、Thinking Machines、NVIDIA 研究频道（工程博客有 cuDSS 1.0 与 DuckDB Sirius，不进研究主包）。
- 第三方转述数字无官博原文则不收。

### 官方原文摘录

#### Labs Raw Excerpts — 2026-11-24

- **窗口**: 2026-11-21 09:09 Asia/Singapore → **2026-11-24 约 09:12 Asia/Singapore**（Asia/Singapore, UTC+8；采集截止以本机 `date` 复核为准）
- **采集时间**: 2026-11-24 约 08:47–09:12 Asia/Singapore
- **说明**: 原始摘录；关键数字标「官方自报 / 来源记录 / 待核」。网络安全与生物仅写结论与官方数字，不写利用/合成/实验步骤、攻击轨迹或提示构造。已在上期主包或窗口外的条目不作为本期重点重复。
- **去重参照**: （内部证据存档）、`research.md`。上期已报勿重复：Gemini 4 Neon 发布文与模型卡、Thinking Machines Inkling 2 Mini、OpenAI jagged-frontier RSI 报告、MedChemBench、对抗蒸馏防护、Apple Depth Pro 2。上期备选与更早主包不当新条目重报。上期数字不在此复述。
- **边界排除**: blog.google [Get your year-end tasks done with new Connected Apps](https://blog.google/products-and-platforms/products/search/connected-apps-holiday-errands/) RSS **2026-11-21 02:00 Asia/Singapore**、[Watch Duty](https://blog.google/company-news/outreach-and-initiatives/google-org/watch-duty-gemini-tool/)（**01:00 Asia/Singapore**）、以及 Google Research [How Google Duplex evolved...](https://research.google/blog/how-google-duplex-evolved-to-also-call-businesses-for-you-in-gemini/)（**07:30 Asia/Singapore**）均早于 09:09 起点，**不纳入本窗**（已在上期窗口）。Amazon Science「Mathematical proof, powered by AI...」RSS `Wed, 18 Nov 2026 18:55:35 GMT` → **2026-11-19 02:55 Asia/Singapore**，早于本窗。

---

##### OpenAI

**源查证**: [openai.com 来源](https://openai.com/news/rss.xml)（curl + Chrome UA，HTTP 200）；[openai.com 来源](https://openai.com/news/) 与 `/news/research/` 本窗 HTTP 200。辅以 [alignment.openai.com 来源](https://alignment.openai.com/) 与 [alignment.openai.com 来源](https://alignment.openai.com/rss.xml)（均 200；列表可见的最近研究帖仍在窗口之前，窗内无新帖）。

###### 1) Perplexity and Intelligence — **建议进主包（内部 perplexity 轨迹 + 开发节奏主张）**
- **日期**: News RSS `Sun, 22 Nov 2026 00:00:00 GMT` → **2026-11-22 08:00 Asia/Singapore**（来源记录）
- **URL**: [openai.com 来源](https://openai.com/index/perplexity-and-intelligence/)（308 后 200）
- **人话**: 首席科学家公开 OpenAI 内部预训练 log-perplexity，主张用它做跨实验室可对照的进度尺，并讨论在监控能力跟上之前设置开发上限。
- **要点**（官方自报，除非另注）:
  - 持出集自 GPT‑3.5 起主要取自内部代码库固定快照。
  - GPT‑3.5 约 **0.99**；GPT‑4 约 **0.91**；已到 **0.8** 以下，并称在网络安全与数学等领域出现变革性能力（只记结论）。
  - 约 **0.76** 的模型开始在开放数学问题上连续给出突破性结果。
  - 作者预期约 **0.68–0.7** 窗口还会有新的变革性能力，同时现有为主的对齐审计会变差、评测与训练察觉会上升。
  - 建议共同设定以 perplexity 等指标为基础的开发上限，在出现思维链监控后继方案之类明确里程碑之前不要越过。
  - 作者列出局限：跨实验室数据不同、不直接对应下游任务、解释不了思维链等预训练之外的进展、未知数据熵下界。
  - 2026 年损失曲线变陡：主要归因于长期研究与算力，自动化只占较小部分；最近模型已有来自 AI 的有意义设计贡献。2027 年「有可能」出现预训练算法洞察雪崩，是展望不是承诺。完全无人监督的递归自我改进被写成应当避免。
- **局限**: 个人署名立场文；内部代码库指标不能直接跨实验室比较；文中未把阈值点名到对外产品型号。
- **标注**: 来源记录 / 官方自报。

###### 2) OpenAI and Cisco introduce Shirudo — **不挤研究主包（开源运行时防护，仅高层）**
- **日期**: News RSS `Mon, 23 Nov 2026 21:20:00 GMT` → **2026-11-24 05:20 Asia/Singapore**（来源记录）
- **URL**: [openai.com 来源](https://openai.com/index/introducing-shirudo/)（308 后 200）
- **仓库 / 文档**: [GitHub shirudo-dev/shirudo](https://github.com/shirudo-dev/shirudo) 、[docs.shirudo.dev 来源](https://docs.shirudo.dev/index.html)（均 HTTP 200）
- **人话**: 开源 Linux 运行时，用来在补丁还没铺开时给正在跑的系统加临时「盾」。
- **要点**（官方自报，仅高层）: 受控测试中，Codex 生成的盾在不重启的情况下挡住了对运行中 Elasticsearch 服务的利用尝试。设计围绕 eBPF 的实时防护、面向智能体的可编程控制（部署仍由安全团队批准）、签名与内核校验、以及 TPM 支持的加载记录。许可证：运行时 BSD 2-Clause，BPF 程序 BSD 与 GPL 双许可。不写利用路径、盾的构造或执法细节。
- **标注**: 来源记录 / 官方自报。

**其他窗内（不挤研究主包）**:
- [Connected intelligence for in-house legal](https://openai.com/business/learn/connected-intelligence-for-in-house-legal)（RSS **11-23 16:00 Asia/Singapore**）：商务/法律场景。
- [Richpanel helps companies automate 50% of support in 30 days](https://openai.com/business/customer-stories/richpanel-ai-customer-support)（**11-23 16:00 Asia/Singapore**）：客户案例，百分比为客户或商务口径，不录入研究主包。

**Alignment 博客**: 窗内无新帖（非缺访问）。RSS 可见条目的日期均早于 11-21 09:09。

---

##### Anthropic

**源查证**: [anthropic.com 来源](https://www.anthropic.com/research)、`/news`、`/engineering`（均 200）；[alignment.anthropic.com 来源](https://alignment.anthropic.com/)（200）。RSS 备用地址 `/feed`、`/rss.xml` 为 404，完整性以列表页与文章页 `publishedOn` / CMS 字段为准。

###### 3) Working with AI — **建议进主包（企业采用与劳动访谈）**
- **日期**: 文章页 `publishedOn` **2026-11-23**（日级）。`_createdAt` `2026-11-23T18:46:09.484Z` → **2026-11-24 02:46 Asia/Singapore**；`_updatedAt` `2026-11-23T22:13:27.525Z` → **06:13 Asia/Singapore**（来源记录）。首次对外可见的精确时刻 **待核**。
- **URL**: [anthropic.com 来源](https://www.anthropic.com/research/working-with-ai)
- **官方 PDF**: [assets.claude.com 来源](https://assets.claude.com/0cb09418f04d09baf72922e53a3f17383ef838c9.pdf)（200）
- **人话**: 对 58 家企业客户做 66 场访谈，看 AI 价值从哪来、招人怎么变、以及高价值用法怎样重组岗位。
- **要点**（官方自报）: 多数用途据称靠提高产出而非砍成本；编码智能体进入非技术岗位。访谈中很少看到由 AI 自动化驱动的国内裁员；多数公司因 AI 少招人，不少减少承包商、尤其是离岸承包商。自上而下自动化与自下而上发工具都有瓶颈；价值最高的用法涉及实质性重组。作者：Nathan Wilmers、Maxim Massenkoff、Peter McCrory。
- **局限**: 客户样本，不是就业普查；主包未逐节核附录。
- **标注**: 来源记录 / 官方自报。

**News**: 列表页 200。可见的 “Latest news” / “November 24, 2026” 是页面头，**不是**新稿（与上期把采集日页头误当成发稿的坑相同）。上期已报的 IPO 定价与收盘公告不重报。本窗未发现新的研究向 News 长文。

**Engineering / Alignment**: 窗内**无新研究长文**（非缺访问）。

---

##### Google DeepMind / blog.google

**源查证**: DeepMind RSS [deepmind.google 来源](https://deepmind.google/blog/rss.xml)（200）；blog.google 主 RSS 与 models / developer-tools 分类 RSS（均 200）。DeepMind 博客页 200。本窗量子一文的 deepmind.google/blog URL 为 **200**（未再 302 到 blog.google，来源记录）。

###### 4) Finding faster quantum algorithms with agents and formal verification — **建议进主包（智能体 + Lean 验证的量子算法改进）**
- **日期**: `datePublished` `2026-11-23T17:00:00+00:00` → **2026-11-24 01:00 Asia/Singapore**（来源记录）。RSS `Mon, 23 Nov 2026 16:59:40 +0000` → **00:59 Asia/Singapore**。文首 November 23, 2026。
- **URL**: [deepmind.google 来源](https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/)
- **论文**: [arXiv 2611.09822](https://arxiv.org/abs/2611.09822)（题 *Discovering formally verified quantum programs with AI*；API 首发 `2026-11-06T18:08:06Z`，本窗见到 v3，HTTP 200）。该 ID **早于**本期扫描起点 2611.26630，只作为本条官方发布的配套论文。
- **代码**: [GitHub google-deepmind/formal-quantum-computation](https://github.com/google-deepmind/formal-quantum-computation)（200）
- **人话**: Gemini 4 智能体团队改进已知量子算法，Lean 证明正确性，并开源形式化库。
- **要点**（官方自报）: 独立团队找改进，Lean 验证后写入共享笔记本，每四小时交流一次。惯性约束聚变相关电路：综合成本降为 **1/11.8**，纠错后内存 **5,650 → 4,338** 量子比特。一种光敏分子模拟便宜 **8×**。Cytochrome P450：**2.5×**，内存 **481 → 333** 量子比特。某具体 Grover 实现 **2.57×**；arcsin **290×**。文中写明科学模拟所需资源仍可能高于第一代纠错机很可能具备的水平。合作方：Google DeepMind 与 Google Quantum AI。
- **局限**: 数字取自博客，未逐表深读论文 PDF。
- **标注**: 来源记录 / 官方自报。

**其他窗内（不挤研究主包）**:
- [Introducing file slicing controls in the Gemini API](https://blog.google/innovation-and-ai/technology/developers-tools/file-slicing-controls/)（RSS **11-24 00:12 Asia/Singapore**）：API 工程。
- [See what 6 builders are making with Gemini 4 Hydrogen](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-hydrogen-builders/)（**11-24 02:00 Asia/Singapore**）：Hydrogen 已在上期窗口发布后的开发者案例，不是新模型发布。
- Search 个性化、Google Photos 节日更新、Gemini Canvas 技巧等消费帖不录。

---

##### Google Research

**源查证**: [research.google 来源](https://research.google/blog/rss.xml)（200）。

###### 5) Supercharging transformer residual connections — **不挤研究主包（ICML 2025 旧文新博）**
- **日期**: 文首 **November 23, 2026**；RSS `Mon, 23 Nov 2026 17:21:12 +0000` → **2026-11-24 01:21 Asia/Singapore**（来源记录）。页面 JSON-LD 未取到 `datePublished`。
- **URL**: [research.google 来源](https://research.google/blog/supercharging-transformer-residual-connections/)（200）
- **论文**: [arXiv 2502.06785](https://arxiv.org/abs/2502.06785)（HTTP 200；博客写明系 ICML 2025 论文 *DeepCrossAttention: Supercharging Transformer Residual Connections*）
- **人话**: 用可学习权重和深度交叉注意力动态组合前层输出，替代等权相加的残差连接。
- **要点**（官方自报）: 称可达同等质量且最多约 **3×** 更快，参数增加可忽略；后文又称参数可减少最多 **30–40%**。两条都是博客原文，本包不做强制对表。作者：Kyriakos Axiotis、Thomas Fu。
- **标注**: 来源记录 / 官方自报。旧文新博，不当本期新结果。

---

##### Meta AI

**源查证**: [ai.meta.com 来源](https://ai.meta.com/blog/) 或研究列表页（200）；[engineering.fb.com 来源](https://engineering.fb.com/) feed（200）；[about.fb.com 来源](https://about.fb.com/news/feed/)（200）。

**研究博客**: 最新仍是 **Introducing Our Smallest, Most Efficient Model: Muse Ember**（November 9, 2026）与 November 6 的 Muse 专项模型文，均早于本窗。窗内**无新研究长文**（非缺访问）。

**about.fb**：[Researchers Are Using Meta’s Open-Weight AI Models to Transform Medicine](https://about.fb.com/news/2026/11/researchers-using-meta-open-weight-ai-models-medical-breakthroughs/)（RSS **11-24 02:00 Asia/Singapore**）。应用综述，不是新模型或新方法发布；生物方向只记「开放权重模型被用于医学研究」这一层，不转写实验或临床细节。不进研究主包。

**Engineering feed**: 可见最新条目为 11-18 的 Ads Ranking 智能体与模板化 ML 生态，RSS 时刻早于本窗。窗内无新帖。

---

##### Apple Machine Learning Research

**源查证**: [machinelearning.apple.com 来源](https://machinelearning.apple.com/research) 全列表 `__NEXT_DATA__`（200，**1194** 条 `published` 字段，与上期条数相同）；RSS 仅 10 条，完整性以全列表为准。

按 `published` 日期，**2026-11-21 及以后为 0 条**。11-20 仍是 Depth Pro 2（RSS `Fri, 20 Nov 2026 00:00:00 GMT` → **11-20 08:00 Asia/Singapore**），已在上期报告。窗内无新发（非缺访问）。

---

##### Microsoft Research

**源查证**: MSR 博客列表与 feed（200）。

Feed 可见最新研究向条目：TokenEconomizer（`Mon, 16 Nov 2026 17:01:35 +0000`），以及 “Can AI help build a healthier future?”（`Tue, 17 Nov 2026 16:52:17 +0000` → **11-18 00:52 Asia/Singapore**），均早于本窗。窗内**官方博客无新研究长文**（非缺访问）。

本窗 arXiv **2611.27910** 页眉署 **Microsoft**（通讯均为 @microsoft.com），已建议进主包；PDF **未**写 Microsoft Research 字样，不能把博客无更新和「微软没有论文」混为一谈。

---

##### Amazon Science

**源查证**: Amazon Science index / RSS（200）。

最新条目「Mathematical proof, powered by AI. And no hallucinations!」RSS `Wed, 18 Nov 2026 18:55:35 GMT` → **2026-11-19 02:55 Asia/Singapore**，早于本窗。其后可见 “Using mathematics to validate network configurations”（11-11）、Mitra-v2（11-05）。窗内无新帖（非缺访问）。

---

##### NVIDIA

**源查证**: [blogs.nvidia.com 来源](https://blogs.nvidia.com/) 与 [developer.nvidia.com 来源](https://developer.nvidia.com/blog) 双 feed（200）；研究门户页面已访问。

**工程博客（不进研究主包）**:
- [Accelerating Direct Sparse Solvers ... NVIDIA cuDSS 1.0](https://developer.nvidia.com/blog/accelerating-direct-sparse-solvers-for-computational-engineering-with-nvidia-cudss-1-0/)（**11-24 03:59 Asia/Singapore**）
- [Get Started with GPU-Accelerated DuckDB Analytics Using the Sirius Core Extension](https://developer.nvidia.com/blog/get-started-with-gpu-accelerated-duckdb-analytics-using-the-sirius-core-extension/)（**11-24 01:09 Asia/Singapore**）
- [Merry Making: Play, Build and Create With NVIDIA Technologies This Holiday Season](https://blogs.nvidia.com/blog/nvidia-technologies-holidays-2026/)（**11-24 01:00 Asia/Singapore**）：节日综述。

**研究频道**: 未取到窗内新的研究长文（非把工程博客算成研究发布）。

---

##### Thinking Machines Lab

**源查证**: 博客 Connectionism 与 News 页（200）。可见卡片：博客最新仍是 End-to-End 4-Bit Training（**Nov 13, 2026**）；News 最新仍是 Introducing Inkling 2 Mini（**Nov 20, 2026**），已在上期主包。页面 HTML 中出现的 11-23 字符串来自资源或页眉，**不是**新帖。窗内无新发（非缺访问）。

---

##### 其他实验室速记

未把第三方媒体转述当官方更新。本窗无新的 Anthropic Engineering / Alignment 长文，无新的 OpenAI Alignment 帖。

---

##### 覆盖小结

- 已成功访问的源见上，未把缺访问写成无更新。
- 建议进主包：OpenAI Perplexity and Intelligence；DeepMind 量子算法+Lean；Anthropic Working with AI。
- 旧文新博或产品/工程：Google Research DCA（ICML 2025）；Shirudo；Gemini API file slicing；Hydrogen 开发者案例；NVIDIA cuDSS / DuckDB Sirius。
- 窗内无新研究长文：Apple、MSR 官方博客、Meta 研究博客、OpenAI Alignment、Amazon Science、Thinking Machines、NVIDIA 研究频道。

### arXiv 原始候选

#### arXiv raw pack: cs.AI / cs.CL / cs.LG（扫描窗口 2026-11-21 09:09 Asia/Singapore → 2026-11-24 ~09:12 Asia/Singapore）


核验方式：真实访问 `arxiv.org/list/cs.{AI,CL,LG}/{new,pastweek}`、`arxiv.org/catchup/cs/YYYY-MM-DD`、`/abs/`、`/pdf/` 首页，以及 [Availability of submissions](https://info.arxiv.org/help/availability.html) 假期表与 [localtime](https://arxiv.org/localtime)；HTTPS `export.arxiv.org/api`。数字默认摘自摘要，必要时用 PDF 首页核对，标 **作者自报**；机构只以 HTML `Affiliation` / PDF 首页（含脚注、通讯邮箱）为准，**不以题目或摘要里出现的模型名、硬件名、或 GitHub 组织名为机构**。提交日多在美东或更早；**Asia/Singapore 归属按 listing/放批日**，不按 Submitted on 字面。本窗 HTML 机构栏仍常残缺，已改用 **PDF 首页**（来源记录）。

上期主包已报勿重复：2611.26358 Beam、2611.25673 CompAct-Bench、2611.25123 GrepMem、2611.22971 SEAM、2611.21832 Auditors；上期扫描宇宙止于 2611.26629。本期扫描宇宙全部 ≥2611.26630，与上期已报 ID 无交集。DeepMind 博客配套论文 **2611.09822** 首发于 11-06，只在官博条引用，不计入本期 arXiv 精选。

##### 假期与日程（本窗无额外推迟；下期需看感恩节）

官方假期表 2026 年 11 月条目仅有 **Wednesday 2026-11-11**（Veterans Day，已在更早期处理）与 **Thursday 2026-11-26**（Thanksgiving，尚未到）。本窗 11/21–11/24 **无额外假期、无官方延期公告**（来源记录，availability.html 2026 Holidays）。常规日程：美东 **Sun–Thu 20:00** 放批（11 月为 EST）→ 新加坡约 **Mon–Fri 09:00** 可见；**无周六、周日批**。因此：

- 周五、周六无公告 → catchup **Sat, 21 Nov 2026** 与 **Sun, 22 Nov 2026** 均为 0 条（来源记录）
- 周日 11/22 20:00 ET 公告 → listing 日期 **Mon, 23 Nov 2026**（Asia/Singapore 11/23 早批）
- 周一 11/23 20:00 ET 公告 → listing 日期 **Tue, 24 Nov 2026**（Asia/Singapore 11/24 09:00 前后）。该批在 08:48、08:53 时尚为 catchup 0；**09:10–09:12 Asia/Singapore 复核时 abs 新号已开始出现，但 CS 列表仍未切换**（见下表）。**不要**写成「周二无更新」，也**不要**把未齐新号算进本期完整宇宙。

采集早期 arXiv localtime 为 **Mon, 23 Nov 2026 19:48 EST**（公告前约 12 分钟）。截止复核时 localtime 为 **Mon, 23 Nov 2026 20:10 EST**（已过公告点）。再下一批最早为周二 20:00 EST（Asia/Singapore 周三 09:00）。感恩节日程留给下期核验。

##### Batch map（日期为 Asia/Singapore 放批早间 / listing 标签日）

| Asia/Singapore 批次 | listing 标签 | cs 全集 catchup（新稿 / 交叉 / 替换） | 全站新号范围 | 状态 |
|---|---|---|---|---|
| 11/21 (Sat) | catchup “Sat, 21 Nov 2026，Total of 0 entries / No updates” | — | — | **无新批**（常规周末日程） |
| 11/22 (Sun) | catchup “Sun, 22 Nov 2026，Total of 0 entries / No updates” | — | — | **无新批**（常规周末日程） |
| 11/23 (Mon) | Mon, 23 Nov 2026；CS catchup Total **1136** | 新稿 **648/648**，交叉 **64/64**，替换 **424/424** | **2611.26630 – 2611.27986**（CS 新稿首条 **26643**、末条 **27978**；26630–26642 与 27979–27986 共 21 个号均 200，主类见下，绝大多数不在本三科） | **列表完整**（showing N of N）。`/new` 在周二早间仍显示 Monday, 23 November 2026 |
| 11/24 (Tue) | 截止时 catchup 仍为 “Total of 0 entries / No updates”；`/new` 横幅仍为 Monday, 23 November 2026 | 列表未齐 | abs 在 09:10–09:12 Asia/Singapore 已出现 **2611.27987+**（抽样 27987/27988 主类 q-fin.TR，28215 主类 quant-ph）；探测可见到至少 28215=200，但 28190、28201 等仍 404，export API 对已 200 的新号返回 0 条 | **出号中、列表未齐**。不以移动中的探测上沿作为完整批次终点 |

说明：

- 周一全站并不是从 26643 起号。abs/API 探测确认 **2611.26630–2611.26642** 与 **2611.27979–2611.27986** 均已放出。主类如下（来源记录，export API `primary_category`）：
  - 26630 math.AP；26631 math.AP；26632 math.AP；26633 math.CA；26634 math.AP；26635 math.AP；26636 math.AP；**26637 stat.ML**（兼 cs.CL、cs.LG，已入本三科交叉宇宙）；26638 math.AP；26639 math.AP；26640 math.CO；26641 math.RA；26642 math.AP。
  - 27979 astro-ph.GA；27980 cond-mat.mes-hall；27981 cond-mat.mes-hall；27982 cond-mat.str-el；**27983 stat.ML**（兼 cs.AI、cs.IT、cs.LG，已入交叉宇宙）；27984 math.AP；27985 hep-ph；27986 hep-ph。
- pastweek（showing N of N）：AI **1383/1383**（分段 214、252、230、259、428；后四段与上期周五至周二吻合，首段为新的周一），CL **597/597**（91、96、72、102、236），LG **1274/1274**（171、213、218、211、461）。周末无 listing，故 pastweek 仍是五个公告日。
- 扫描宇宙（本期新看的周一新稿+交叉，已去掉替换稿，且 ID ≥2611.26630、科目含 cs.AI/CL/LG）：**364** 篇（新稿 **340** + 交叉 **24**）。24 篇交叉里，号段落在 CS 新稿 26643–27978 之外的只有 **2611.26637** 与 **2611.27983**。标题/摘要关键词粗筛后，对 **29** 篇做了 API 摘要核验，并对 **8** 篇最终候选人做了 PDF 首页机构核验。
- 替换稿未计入「新发现」宇宙，也未当新条目精读。
- 机构：以 **PDF 首页**为准（来源记录）。2611.27734 正文提到的 NVIDIA Auto Ontology、Palantir、AWS 是相关产业实践，**不是**作者单位。2611.27116 的 GitHub 组织 AlibabaResearch 只作旁证，机构仍以 PDF 首页「Zhejiang University / Alibaba Group / Shanghai Jiao Tong University」为准。2611.27910 页眉写 Microsoft，未写 Microsoft Research。
- 本期**完整**扫描所依据的全站上沿仍是周一的 **2611.27986**。09:10 之后 27987+ 已开始出现但列表未齐、API 未入索引、号段有空洞，这些新号**不计入**本期 364 篇宇宙。续扫 **2611.27987+** 与周二正式 listing。

##### Candidates（单位经 PDF 首页核实；数字来自摘要除非另注）

###### 真重点

1. **2611.26809** Search From the Start: Search-Native Pretraining for Language Models  
   链接：[arXiv 2611.26809](https://arxiv.org/abs/2611.26809)  
   提交/公布：API published 2026-11-19T20:58:34Z → 2026-11-20 04:58 Asia/Singapore；**Asia/Singapore 归属 11/23**（Mon 新稿，主类 cs.CL；兼 cs.AI、cs.LG）  
   机构证据：PDF 首页机构行「EPFL」「University of Toronto」，通讯 `（机构署名邮箱略）`、`（机构署名邮箱略）`（来源记录）。五人未逐人上标，不要把 Raffel / Jaggi 拆到未写明的第三家单位。  
   人话：在普通语料里插入检索查询和本地索引返回，让模型在预训练阶段就学会发起搜索并引用证据（QueryLM）。  
   为何重要：本窗最清楚的预训练范式论文；作者称 1.4B QueryLM 在所测知识型任务上持续达到或超过 FLOP 对齐的 3.3B 基线，且该优势在双方都做 SFT 之后仍在。  
   对谁有用/深读：检索增强预训练、工具使用前置、知识型 QA。  
   主要数字与条件/局限（作者自报）：Wikipedia 与 DCLM-Edu，360M 到 3.3B。1.4B QueryLM 据称在全部知识密集型任务上持续击败或打平 FLOP 对齐的 3.3B 基线；所测后训练没有完全补回预训练形成的能力。作者称释放 checkpoint 与数据，但 PDF 首页 “Training artifacts are available at .” 未给出可核验 URL，**产物链接待核**。对照是 FLOP 对齐、带搜索的设定。  
   标签：**真重点** · 来源记录 / 作者自报

2. **2611.26863** LLMs Memorize Their Own Hallucinations During Post-Training  
   链接：[arXiv 2611.26863](https://arxiv.org/abs/2611.26863)  
   提交/公布：API published 2026-11-19T22:28:14Z → 2026-11-20 06:28 Asia/Singapore；**Asia/Singapore 归属 11/23**（Mon 新稿，主类 cs.CL；兼 cs.LG）  
   机构证据：PDF 首页两位均署 Cornell University，通讯 `（机构署名邮箱略）`、`（机构署名邮箱略）`（来源记录）。**康奈尔大学**。  
   人话：把为推理任务设计的结果奖励和回退配方直接用到知识问答上，模型可能记住推理链里自己编出的错误事实。  
   为何重要：给推理配方外溢到知识任务提供可测量路径。  
   对谁有用/深读：知识任务 RL、幻觉来源、弃答。  
   主要数字与条件/局限（作者自报，仅结论）：六个开源模型、两族、两种架构。被强化的自编幻觉事后召回平均升 **4.83%**，未给信号的只升 **0.17%**；模型也会记住已被收回的错误事实。最难训练题上记忆更强；幻觉受奖后弃答可能性平均再降 **7.23%**。不能直接外推到未测闭源模型。不写提取或构造步骤。  
   标签：**真重点** · 来源记录 / 作者自报

3. **2611.27116** CoEvoBench: Can LLMs Drive Recursive Co-Evolution of Agentic Systems?  
   链接：[arXiv 2611.27116](https://arxiv.org/abs/2611.27116) · 代码 [GitHub AlibabaResearch/CoEvoBench](https://github.com/AlibabaResearch/CoEvoBench)（HTTP 200）  
   提交/公布：API published 2026-11-20T04:40:59Z → 2026-11-20 12:40 Asia/Singapore；**Asia/Singapore 归属 11/23**（Mon 新稿，主类 cs.AI）  
   机构证据：PDF 首页「1 Zhejiang University 2 Alibaba Group 3 Shanghai Jiao Tong University」，通讯 `（机构署名邮箱略）`、`（机构署名邮箱略）`（来源记录）。写成 **浙江大学 + 阿里巴巴 + 上海交通大学**，不要写成单一阿里论文。  
   人话：让大模型当研究员，在 24 小时预算里共同改目标智能体的模型与 harness，看改进能不能递归续上。  
   为何重要：把可测的系统级递归改进收成基准；作者结论是能做很强的第一轮，但不能稳定把反馈变成下一轮。  
   对谁有用/深读：harness 与模型联合优化、研究型智能体、RSI 评测。  
   主要数字与条件/局限（作者自报）：五个智能体领域，统一基座与初始 harness，24 小时预算。五个前沿「研究员」里最强的缩小了与指令微调参考系统之间「五分之四以上」的差距；交互任务较成功，长程编码很少成功。摘要未点名五个模型，勿补。不能读成已经实现稳定 RSI。  
   标签：**真重点** · 来源记录 / 作者自报

4. **2611.26637** SDG: State-Dependent Gating at Chunk Boundaries for Linear Attention  
   链接：[arXiv 2611.26637](https://arxiv.org/abs/2611.26637)  
   提交/公布：API published 2026-10-16T17:49:16Z；**Asia/Singapore 归属 11/23**（Mon **交叉**，主类 stat.ML；兼 cs.CL、cs.LG）  
   机构证据：PDF 首页「1 Peking University, 2 Meituan Inc.」；Renjia Deng 标 1,2，并写实习在美团；通讯 Kun Yuan，`（机构署名邮箱略）`（来源记录）。**北京大学 + 美团**（邓为美团实习）。  
   人话：在 chunk 边界用依赖本层记忆变化的逐元素门控，给线性注意力补状态反馈，同时保留 chunk 内并行。  
   为何重要：为 Gated DeltaNet、Kimi Delta Attention、Gated DeltaNet-2、Mamba-3 提供仍兼容分块核的遗忘机制。  
   对谁有用/深读：线性注意力、混合架构、长上下文检索、分块核。  
   主要数字与条件/局限（作者自报）：1.3B 线性注意力和混合模型，**100B** token。作者称语言建模、常识、检索和长上下文均有提升，摘要无绝对分，本包不补表。作者自报代码 [GitHub lovekdl/SDG](https://github.com/lovekdl/SDG)，本窗 **HTTP 404**，不把该链当已核验链接。  
   标签：**真重点** · 来源记录 / 作者自报

5. **2611.27910** Decision Columns as an Index: Interpretable Embeddings for Explainable Entity Matching and Search  
   链接：[arXiv 2611.27910](https://arxiv.org/abs/2611.27910)  
   提交/公布：API published 2026-11-20T17:48:55Z → 2026-11-21 01:48 Asia/Singapore；**Asia/Singapore 归属 11/23**（Mon 新稿，主类 cs.IR；兼 cs.AI、cs.DB）  
   机构证据：PDF 首页三人均署 Microsoft，通讯 `@microsoft.com`（来源记录）。页眉是 **Microsoft**，未出现 Microsoft Research 字样。  
   人话：用一组自然语言问题的校准回答做成可解释向量，做实体匹配和检索，并能精确解释匹配依据。  
   为何重要：大厂系统/数据集成论文，强调智能体改业务记录时必须说得清依据；定位是稠密检索旁边的可读通道。  
   对谁有用/深读：实体匹配、企业检索、可解释嵌入。  
   主要数字与条件/局限（作者自报）：WDC Products 与 STaRK-Amazon。retrieve-then-verify 的候选生成上，问题空间与稠密检索统计上相当。按失败案例加问题，可在不重编码已有回答的情况下把 MRR 提到原来的 **三倍**。推断合适结果属性优于只编码字面请求；与稠密分数结合能改善检索，但未达预先设定的置信阈值。小网络回填成本约 **1/200**。不要写成通用 SOTA。  
   标签：**真重点** · 来源记录 / 作者自报

###### 强候选（不挤主包）

6. **2611.26835** Non-Expanding Gated Continued Fraction Architecture for Feedforward Layers in Language Models  
   链接：[arXiv 2611.26835](https://arxiv.org/abs/2611.26835) · 代码 [GitHub IBM/CoFrNets](https://github.com/IBM/CoFrNets)（HTTP 200）  
   提交/公布：API published 2026-11-19T21:37:17Z；**Asia/Singapore 归属 11/23**（Mon 新稿，主类 cs.CL；兼 cs.AI）。NeurIPS 2026。  
   机构证据：PDF 首页五人均署 IBM Research，通讯 `@us.ibm.com` / `（机构署名邮箱略）`（来源记录）。  
   人话：用非扩展门控连分数组件替换前馈层，并用对数-指数重写除法以稳定训练。  
   主要数字与条件/局限（作者自报）：在 GPT‑2、Llama‑3、Mamba‑2、(nano) Llama-MoE 上称相当或明显好于前作、吞吐更高，且不再需要前作的增量训练。摘要无绝对分。  
   标签：**强候选** · 来源记录 / 作者自报

7. **2611.27734** AutoOntologyBench: A Task-Grounded Benchmark for Agentic Knowledge Engineering  
   链接：[arXiv 2611.27734](https://arxiv.org/abs/2611.27734) · 代码 [GitHub VinyehShaw/AutoOntologyBench](https://github.com/VinyehShaw/AutoOntologyBench)（HTTP 200）  
   提交/公布：API published 2026-11-20T15:29:27Z → 2026-11-20 23:29 Asia/Singapore；**Asia/Singapore 归属 11/23**（Mon 新稿，主类 cs.CL）。  
   机构证据：PDF 首页「1 Durham University 2 Shanghai University of Finance and Economics 3 Peking Union Medical College Hospital, Peking Union Medical College 4 Alibaba DAMO Academy, Alibaba Group」（来源记录）。NVIDIA / Palantir / AWS 只在相关工作中出现，**不是**作者单位。  
   主要数字与条件/局限（作者自报）：19,947 项已审核任务，18 个真实知识源，7 个领域，九个前沿模型智能体。在检索之上叠加智能体自建本体，任务成功率加 **6.1** 分，仍落后专家参考 **13.0** 分。  
   标签：**强候选** · 来源记录 / 作者自报

8. **2611.27759** DPMA: Learning to Compress Mixture-of-Experts Models  
   链接：[arXiv 2611.27759](https://arxiv.org/abs/2611.27759)  
   提交/公布：API published 2026-11-20T15:46:35Z → 2026-11-20 23:46 Asia/Singapore；**Asia/Singapore 归属 11/23**（Mon 新稿，主类 cs.LG）  
   机构证据：PDF 首页 Ikerlan Technology Research Center、University of the Basque Country UPV/EHU、University of Cambridge、SOFAIR、HiTZ / Ixa、Flower Labs（来源记录）。多机构合作，不要写成单一剑桥或 Ikerlan 论文。  
   主要数字与条件/局限（作者自报）：四个 MoE、八个选择题基准、五个压缩比；作者称在每个模型上按基准与压缩比平均准确率都最高。75% 专家削减下，对每个被测模型都优于最强基线，最多高 **6.7** 个百分点。权重保持冻结，用校准数据学习剪枝/合并/吸收系数。  
   标签：**强候选** · 来源记录 / 作者自报

###### 看过但未进短名单的说明（宁缺毋滥）

- **2611.27895** TEA-Bench-BR：Kaggle Gemma 4 Developer Agent Paper Track，单作者临床分支规格基准，体量与机构权重不够。
- **2611.27102** Opsis、**2611.27095** Epistemic Guard、**2611.27426** Cleave、**2611.27477** / **2611.27891** 投机解码、**2611.27348** 短视野过程监督、**2611.26853** LoCo-WAM、**2611.27243** Gemma-4 反向传播病例、**2611.27983** 无方差最优线性回归等：或过于专门、或摘要缺少可核验硬数字、或属安全攻击向（Cleave 只在粗筛中看过，不写利用步骤，也不进主包）。
- 未把模型名或硬件名推断成机构。

##### 下期续扫

- 本期完整宇宙的全站上沿：**2611.27986**（周一已齐）。
- 下期从 **2611.27987** 起扫（周二批的第一个已出现 abs 号），并**先等** `catchup/cs/2026-11-24` 与 `/new` 显示 Tuesday listing 且 showing N of N；本窗截止时列表未切换、号段仍有 404 空洞，不能把 09:12 左右探测到的临时上沿当成批次终点。
- 下期还须核验 **2026-11-26 Thanksgiving** 是否造成公告延期。


## X 公开动态

### 动态与跟踪

#### X/AI 源包 · 2026-11-24（三日合并）

窗口：2026-11-21 09:09 → 2026-11-24 约 08:50 Asia/Singapore。来源：
- 首页时间线 4 页，约 394 条（98+100+99+97，已过滤回复）。实际覆盖约 11-23 09:49 → 11-24 08:43 Asia/Singapore；窗口前约 48 小时靠公开检索与 Today's News 补齐。
- 官方/关键账号合并检索：OpenAI/OpenAIDevs/thsottiaux/AnthropicAI/claudeai/ClaudeDevs/ArtificialAnlys/cursor_ai/GoogleDeepMind/GoogleAI/GeminiApp/Alibaba_Qwen/dotey/thinkymachines/leanprover/merettm 一组（3 页后 result_count=0）。均 `-is:retweet -is:reply`，未传 `end_time`。另用 `get_posts_by_ids` 补 @nvidianewsroom、@sama、@gdb 等关键原帖。
- 定向检索与交叉核对：Lean FRO / Mathlib 联合声明与 MIT 核验页；OpenAI《Perplexity and Intelligence》、Shirudo 博文；Claude Ship / Plugins / ZDR+EFS 官方页；NVIDIA 新闻室与 8-K（CIK 0001045810，最早事件日 11-22）；Yahoo Finance 对 NVDA、ANT 的历史行情；Reuters 关于 SEC 会计调查的独家报道（仅作待核线索）。
- 可复用但均本期重核：（内部证据存档）、11-23 早报分片、11-24 早报分片。只读作线索，未改动这些文件。
- X Today's News：约 72h 一组（摘要≠来源记录）。

本期 X 侧无 429。官方主检索末页 result_count=0，窗口内该组已收束。openai.com、claude.com、leanprover-community、nvidianews 与 SEC 8-K 本次 WebFetch 成功。未用浏览器绕过任何封锁。旧包与早报数字均本期重核，不以旧稿为事实源。

去重说明：上期主条（Anthropic 定价与首两日交易、Gemini 4 Neon 发布、Genie 4 / Tool Retrieval、GPT-Live-1.1 与 Performance Factory、OpenAI 芯片 PPA / 研究加速 / 对抗蒸馏 / MedChemBench）不重写为新主条。对抗蒸馏官宣与 Inkling 2 Mini 官方/AA 首发均在 11-21 09:09 之前，只把窗口内的后续讨论写入进展。GPT‑6 Cyber 与「948 个提权漏洞」研究博文落款 11-4 / 11-5，早于本窗口，不作为新发布主条。本期主条从黎曼猜想的机器核验、Pachocki 预训练透明度、黄仁勋复职，以及 11-24 凌晨的 Claude / Shirudo 产品写入手。

##### 主条目

###### 1. Lean FRO 与 Mathlib 联合声明：核验 Alpöge 与 Claude 合作的黎曼猜想 Lean 证明
上期只记下 AA 对「宣称证明」的待核转述，当时独立核验尚未完成。本窗口有 Lean FRO 与 Mathlib Initiative 的联合声明，可以把「机器核验已通过、且证明的是 Mathlib 中的标准命题」写成有官方出处的事实；人能否读懂、以及随后出现的质疑，仍要分开写。
- **是什么**：
  - 发布与规模（联合声明）：2026-11-20，Anthropic 数学家 Levent Alpöge 发布一份黎曼猜想的 Lean 证明库，声明称约 **1,700 万行**。这是窗口之前的发布，本窗口的新事实是核验结果。
  - 联合声明（官方）：@leanprover 11-21 23:12 Asia/Singapore 宣布 Lean FRO 与 Mathlib Initiative 发表联合声明，对证明的正确性「有充分信心」。社区博文列出四条标准并称全部满足：Mathlib 中的 `RiemannHypothesis` 陈述经专家审定；库可正确编译，多人复现同一份原始证明导出；用 `comparator` 与 `con-leche --compare` 对照，确认所证即 Mathlib 陈述；导出证明已由 Lean 官方 kernel 以及 `con-leche`、`con-ron` 等多个独立检查器接受。`con-leche` / `con-ron` 还带有相对于集合论的形式化论证，用于回应「Lean 逻辑本身是否可被利用」的担心。声明结尾期待数学界继续解释证明中的新想法。
  - 补充核验页（MIT，Andrew Sutherland）：[math.mit.edu 来源](https://math.mit.edu/~drew/grh/) 页脚可见更新至 11-24 07:45 Asia/Singapore（页上原始时刻 11-23 23:45，已换算）。页上写明还检查了四条 Dirichlet L 函数的广义黎曼猜想陈述；源码可编译、五个标题定理只依赖三个标准公理；部分独立 kernel 已接受完整导出。页上也标明仍有检查在进行，故本包只引用已写明通过的项，不把「全部检查已结束」写成事实。
  - 争议与限度（待核 / 进行中）：机器核验通过，不等于数学共同体已完成人类可读的理解，也不等于不再出现质疑。窗口内有数学家称该证明无效（尽管已通过 Lean 检查）、以及独立研究者致信声称与既有研究重叠等说法，目前均为单方或二手来源，**待核**，不能用来否定联合声明本身。Today's News 另有「Claude 证明 Valiant 猜想（VP≠VNP）」类标题，仅见预测市场/传闻，**待核**，不升主条。
- **为何重要**：这是本窗口最硬的「AI + 形式化数学」事件。联合声明把问题从「有没有人宣称证明了」推进到「机器检查是否接受、所证是否为标准陈述」。真正的后续工作，是人类能否抽出可交流的新思想，以及质疑能否被独立复核。
- **对谁·深读建议**：先读联合声明和四条标准，再看 MIT 核验页的检查清单；引用时写明「Lean 核验通过」，不要写成「数学界已一致承认」或「AI 独自证明」。对质疑帖只标待核，并回到原声明。
- **证据**：
  - 来源记录 / 官方：[@leanprover 联合声明](https://x.com/leanprover/status/2124159121645801562)、[社区博文](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)、[MIT 核验页](https://math.mit.edu/~drew/grh/)
  - 窗口内讲解（非核验本身）：[@dotey](https://x.com/dotey/status/2124282462343967111)
- **约时**：证明库发布 11-20（窗口前）；X 联合声明 11-21 23:12 Asia/Singapore；MIT 页换算后可见更新至 11-24 07:45 Asia/Singapore

###### 2. OpenAI 首席科学家 Pachocki 发表《Perplexity and Intelligence》，公开预训练困惑度曲线并提议共同上限
这不是新模型发布，而是实验室少见地把内部预训练指标公开出来，并提议用困惑度等度量给行业设「先理解、再越线」的闸门。@sama 称这是 OpenAI 近来最重要的发布。
- **是什么**：
  - 官宣：@merettm（Jakub Pachocki）11-23 01:03 Asia/Singapore 发帖并链到官方博文（落款 11-22）。他主张把 perplexity（或等价的交叉熵损失）作为比较模型开发者、并据以制定共同安全标准的度量；同时公布 OpenAI 内部困惑度测量，「尽管会让竞争者更清楚我们的位置」。
  - 官方自报数字（内部主评估集，自 GPT‑3.5 起追踪的代码相关持出集）：GPT‑3.5 的 log-perplexity 约 **0.99**；GPT‑4 约 **0.91**；当前已到 **0.8 以下**，官方称在此出现网络安全与数学方面的「变革性」能力。另称在 log-perplexity 约 **0.76** 的模型上，开始对数学开放问题产出「突破性」结果。他推断，进入约 **0.68–0.7** 窗口还可能出现今天并未在测的新能力。
  - 政策建议（官方）：希望开发者共同设立基于困惑度及其他测量的上限，在「理解与监测模型行为」达到某一具体里程碑（例如 CoT monitor 的后继）之前不越过该上限。他也列出该度量的难点：跨实验室数据集难以直接比较；与下游任务不是一一对应；思维链等预训练之外的进展不降低 perplexity；以及数据固有熵未知，无法把损失降到 0。
  - 实验室表态：@sama 11-23 01:12 Asia/Singapore 称「This is the most important thing OpenAI has published in awhile」，并希望业界就共同上限达成一致。@gdb 11-23 03:15 Asia/Singapore 称这些透明度可以成为行业共享安全门槛的基础。
- **为何重要**：前沿实验室主动公开预训练曲线，并把「能力闸门」从口头原则写成可追踪的度量建议。数字全部是 OpenAI 内部评估，不能直接拿去和其他实验室对表；但它提供了讨论「该在哪一条线上停下来等安全工具」的共同语言。
- **对谁·深读建议**：安全与治理读者应连同博文对度量缺陷的四条自我限定一起引用；不要把 0.76 / 0.68–0.7 写成已被外部复现的普遍定律，也不要把「2027 年可能出现预训练算法雪崩」写成预测事实——那是作者的外推。
- **证据**：
  - 官方自报：[@merettm](https://x.com/merettm/status/2124549218995949967)、[官方博文](https://openai.com/index/perplexity-and-intelligence/)、[@sama](https://x.com/sama/status/2124551594691932405)、[@gdb](https://x.com/gdb/status/2124582684840399311)
- **约时**：博文落款 11-22；X 主帖 11-23 01:03 Asia/Singapore

###### 3. 英伟达董事会全票恢复黄仁勋总裁、CEO 与董事职务；NVDA 11-23 收涨 31.48%
领导层风波在上期和早报里多为传闻与评论。本窗口有公司新闻稿和 8-K，可以把「已经复职」写成事实；SEC 会计调查、总统亲自介入、开盘十分钟市值暴涨等说法，仍须与官方表述分开，标待核。
- **是什么**：
  - 公司与监管文件：NVIDIA 新闻室 11-23 宣布，董事会**一致表决**，立即恢复 Jensen Huang（Jen-Hsun Huang）的总裁、首席执行官和董事职务。8-K 写明最早事件日为 **11-22**，新闻稿作为 Exhibit 99.1 于 11-23 发布。Colette Kress 不再任临时 CEO，继续担任执行副总裁兼 CFO；Harvey C. Jones 留任董事长。@nvidianewsroom 11-23 21:58 Asia/Singapore 发帖并链到新闻稿。
  - 官方对决策过程的表述：董事会在与黄仁勋一系列讨论后，「对其坦诚与领导能力感到满意」；「在作出决定的过程中，董事会听取了美国政府高层的意见，并基于该意见相信复职不构成国家安全风险」。新闻稿**没有**点名具体官员，也没有写「总统致电董事会」。此类细节仅见媒体与预测市场转述，**待核**。
  - 仍在进行的调查与治理安排（官方）：就先前「黄仁勋曾是外国情报活动目标」的报道，董事会已成立全部由独立董事组成的委员会并聘请独立律师，调查将进行至结束；黄仁勋表示支持并配合。董事会另新设国家安全与出口管制委员会；公司开始招聘首席合规官，向提名与公司治理委员会汇报；并称将继续配合「正在进行的政府调查与问询」。8-K 与新闻稿均未把调查定性为「SEC 会计调查」。
  - 行情（Yahoo Finance 历史表）：11-23（美东，开盘约 11-23 22:30 Asia/Singapore）NVDA 开 $167.04、高 $171.50、低 $156.93、收 **$165.05**，成交量 776,225,888，较 11-20 收盘 $125.53 上涨 **$39.52（+31.48%）**。采集时已是 11-24 上午，美股当日常规交易尚未开始；Yahoo 显示 11-23 盘后约 19:47 ET（≈ 11-24 08:47 Asia/Singapore）为 $166.13，只是盘后快照。11-20 收盘 $125.53 相对 11-19 收盘 $145.98 约 -14.0%，与窗口前段的股价重挫一致；因果（是否由某一则报道单独引起）不能写成 来源记录。
  - 待核项：Reuters 11-20 独家称 SEC 执法部门正在审视 Nvidia 的会计问题（匿名消息源，公司未在本则 8-K 中确认具体范围）。「开盘 10 分钟美股市值涨超 3 万亿美元」「特朗普亲自介入董事会电话」等为单一或二手来源，**待核**。
- **为何重要**：AI 算力龙头的掌门人在短期缺位后被董事会正式恢复，且公司主动写明听取了美国政府高层意见。复职本身已有 8-K；调查并未结束，不能写成「事件已经了结」。周一股价大幅反弹，但应与发行/市值叙事一样只用行情表，不用媒体对总市值变动的换算。
- **对谁·深读建议**：写复职只引用新闻稿和 8-K；写「政府意见」用公司原句，不要升格为已核的总统点名干预。SEC 会计调查保持 Reuters 独家 + 待核。行情用 Yahoo 的 O-H-L-C。
- **证据**：
  - 来源记录 / 官方：[@nvidianewsroom](https://x.com/nvidianewsroom/status/2124865060397019480)、[新闻稿](https://nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director)、[8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000090/nvda-20261122.htm)
  - 行情：[Yahoo Finance NVDA 历史](https://finance.yahoo.com/quote/NVDA/history/)
  - 待核线索：[Reuters 独家报道](https://www.reuters.com/3fec1b0a85a0/world/us-secs-nvidia-probe-is-examining-potential-accounting-issues-sources-say-2026-11-20/)、[The Verge 转述](https://www.theverge.com/tech/1039305/nvda-down-sec-investigation-accounting)
- **约时**：董事会决议日 11-22（8-K）；新闻稿与 X 帖 11-23 21:58 Asia/Singapore；NVDA 常规收盘约 11-24 05:00 Asia/Singapore

###### 4. Anthropic 推出 Claude Ship（beta），并把 Connectors 与 Skills 收成 Plugins；ZDR+EFS 进入公测
上期写过 Claude Code 的实验功能与代码审查博文（后者落款更早）。本窗口是产品层的一次集中发布：让 Claude 审 PR、修问题、按政策批准，同时把插件做成统一入口。
- **是什么**：
  - Claude Ship（官方，博文落款 11-23）：@ClaudeDevs 11-24 04:13 Asia/Singapore 宣布公开 beta。系统由已正式提供的 Code Review，以及两个 beta 组件构成——**PR Steward**（处理失败的 CI、合并冲突和审查意见，不负责批准或合并）和 **Claude Approvals**（按仓库里的政策文件决定能否批准，官方建议先观察模式）。目标是「写得有多快，就能运得多快」。面向 **Claude Team / Enterprise**、GitHub 仓库。开发者可在 Claude Code 里用 `/ship`。符合条件的 Enterprise 组织可在 2027-01-15 前领取至少 **$10,000**、领取后 30 天内可用的 Claude Ship 积分（条款适用）。按 token 计费；**不向**采用 Zero Data Retention、HIPAA 配置或客户托管密钥的组织提供。官方回顾称，Claude Code 团队 6–9 月合并 PR 超过翻倍，回滚比例下降逾 40%（官方自报，与上期已引用的审查博文口径一致）。
  - Plugins（官方）：@claudeai 11-24 04:56 Asia/Singapore 称 Connectors 与 Skills 合并为 plugins，已在 **Free / Pro / Max / Ultra** 上线，Team / Enterprise「即将推出」；并称可浏览 **10,000+** 插件（官方自报）。入口：[claude.ai 来源](https://claude.ai/plugins)
  - ZDR + Enterprise Frontier Safeguards（官方）：@claudeai 11-24 02:15 Asia/Singapore 宣布向符合条件的企业公测。官方称可在保持零数据保留的同时，跨多次请求查找滥用；与逾 100 家客户共同开发。加密副本进入客户自己的云存储，自动检查标记严重风险供团队审阅。注意：Ship 明确不面向 ZDR 组织，与本项不要混写成同一套默认能力。
  - 相邻产品：@ClaudeDevs 11-24 05:30 Asia/Singapore 称桌面版 Claude Code 侧栏改为标签布局（文件、更改、终端等），先在 Mac 推出，Windows / Linux 随后。
- **为何重要**：编程助手的瓶颈已经从「会不会写」转到「PR 堆起来谁来审、谁来合」。Ship 把审查、修补和有政策约束的批准连成一条流水线，但仍是 beta，且把最终控制权留给仓库政策和分支保护。Plugins 则把生态入口收拢，数字是官方自报。
- **对谁·深读建议**：Team / Enterprise 管理员先读可用性、计费、ZDR/HIPAA 排除项和观察模式建议；个人开发者看 `/ship` 是否已滚到自己的客户端。不要把 $10,000 积分写成无条件赠款，也不要把 10,000+ 插件写成已审核的官方精选目录。
- **证据**：
  - 官方自报：[@ClaudeDevs Ship](https://x.com/ClaudeDevs/status/2124959436640858475)、[Ship 博文](https://claude.com/resources/articles/introducing-claude-ship)、[@claudeai Plugins](https://x.com/claudeai/status/2124970294523945328)、[@claudeai ZDR+EFS](https://x.com/claudeai/status/2124929944530587712)、[ZDR+EFS 说明](https://claude.com/resources/articles/zero-data-retention-with-enterprise-frontier-safeguards)、[@ClaudeDevs 桌面标签](https://x.com/ClaudeDevs/status/2124978802006851961)
- **约时**：ZDR+EFS 11-24 02:15 Asia/Singapore；Ship 11-24 04:13 Asia/Singapore；Plugins 11-24 04:56 Asia/Singapore

###### 5. OpenAI 与 Cisco 开源 Shirudo：用 eBPF 在不停机的情况下为运行中的 Linux 系统加临时盾
这是本窗口 OpenAI 侧真正的新联合发布，不要与 11-4/11-5 已公布的 GPT‑6 Cyber / 948 个内核提权研究混成同一条「刚发表的论文」。
- **是什么**：
  - 官宣：@OpenAI 11-24 05:37 Asia/Singapore 宣布与 Cisco 共同推出开源 Linux 运行时 **Shirudo**（日文「盾」）。博文落款 11-23。设计目标是在正式补丁还需要数天或数周测试时，先用临时「盾」挡住漏洞利用路径，同时尽量放行合法请求，且不必重启服务。
  - 机制（官方）：基于 eBPF，在操作系统内特定点运行小程序。官方概括四项能力：实时防护（先观察再强制执行）；「机器速度」的防御（agent 可调查漏洞、编写并验证盾，部署仍由安全团队控制）；受信任部署（盾在加载前加密签名，并经 Linux eBPF 验证器检查）；硬件支持的验证（用 TPM 记录盾的加载或移除）。官方举出在受控测试中，由 Codex 生成的盾在无需重启的情况下挡住针对运行中 Elasticsearch 的 Java4Shell 利用。Cisco 侧同步发文。项目开源，邀请开发者与安全研究者共同建设。
  - 相邻、但属旧文新推（不作为本条新事实）：@OpenAI 11-24 07:25 Asia/Singapore 再次介绍 GPT‑6 Cyber 在一次运行中帮助验证 948 个可获本地 root 的 Linux 内核漏洞并生成供审核的补丁。对应研究文 [A thousand fewer paths to root](https://openai.com/index/a-thousand-fewer-paths-to-root/) 落款 **11-4**，产品介绍 [GPT‑6 Cyber](https://openai.com/index/introducing-gpt-6-cyber/) 落款 **11-5**，均早于本窗口。其中官方自报还包括动态复现 1,724 个漏洞、该次运行 API 成本约 $1,213,430 等，引用时须标明旧文与官方自报，见进展。
- **为何重要**：把 agent 写代码的能力用到「边打补丁、边保系统在线」。官方把部署权留在安全团队，并强调签名与验证，避免被理解成 agent 可任意改内核。它是防守方窗口，不是新的进攻模型发布。
- **对谁·深读建议**：安全与基础设施读者读 OpenAI 与 Cisco 两篇博文，以及 eBPF 验证器和 TPM 的具体约束；不要把受控测试里的 Java4Shell 示例写成已在生产环境大规模部署的效果数据。
- **证据**：
  - 官方自报：[@OpenAI Shirudo](https://x.com/OpenAI/status/2124980590717911527)、[OpenAI 博文](https://openai.com/index/introducing-shirudo)、[Cisco 新闻稿](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m11/cisco-and-openai-launch-shirudo-a-new-project-to-safeguard-agentic-ai.html)
- **约时**：博文落款 11-23；X 官宣 11-24 05:37 Asia/Singapore

##### 进展

###### 进展：Anthropic ANT 后续走势——11-23 收 $87.64，仍高于发行价 $83
- **是什么**：上期已核首日收 $97.17、次日（11-20）收 $88.91。11-21、11-22 为周末，无常规交易。Yahoo Finance：11-23 开 $93.69、高 $94.24、低 $84.65、收 **$87.64**，成交量 253,330,731，较 11-20 收盘约 -1.43%，相对发行价 $83 仍约 +5.6%。采集时 11-24 常规交易尚未开始；Yahoo 盘后约 19:47 ET（≈ 11-24 08:47 Asia/Singapore）为 $87.36，只是快照。媒体市值与杠杆 ETF 等报道待核，不与 $81.34B 发行规模混用。FinancialContent 对开、低、成交量的尾数与 Yahoo 略有出入，包中以 Yahoo 为准。
- **证据**：[Yahoo Finance ANT 历史](https://finance.yahoo.com/quote/ANT/history/)
- **约时**：11-23 常规收盘约 11-24 05:00 Asia/Singapore

###### 进展：OpenAI 对抗蒸馏——原官宣在窗口之前；本窗口多为转述
- **是什么**：上期主条已写 11-21 03:33 Asia/Singapore 的官方博文及 54.0%→0.2% 的内部评估。该时间早于本窗口起点。窗口内可见中文解读与「轻松蒸馏时代结束」等评论，没有新的官方评估表或改口。数字仍以上期已核博文为准，不重复当作新发布。
- **约时**：原官宣 11-21 03:33 Asia/Singapore（窗口前）

###### 进展：循环层小模型——Inkling 首发在窗口前，窗口内有社区实测与后续同类方案
- **是什么**：@thinkymachines 对 Inkling 2 Mini 的官方发布与 AA 首测均在 11-21 04:10–04:35 Asia/Singapore，早于本窗口，上期已在「其他」记下 AA 口径（26B / 5.4B 激活、Apache 2.0、Index 20）。本窗口出现社区 KernelBench 等实测（单一来源，待核），以及 SenseNova-Loop-9B、智谱 GLM-5.4 等「复用中间层、增加有效深度」的官方或准官方介绍（官方自报，须回对原帖/产品页）。这是方向性进展，不是 Inkling 的二次首发。
- **约时**：覆盖至 11-24 上午 Asia/Singapore

###### 进展：GPT‑6 Cyber / 948 个内核 LPE——旧文在本窗口被官号再次推送
- **是什么**：@OpenAI 11-24 07:25 Asia/Singapore 介绍一次运行中验证 948 个可获本地 root 的 Linux 内核漏洞并生成补丁。研究文与产品文分别落款 11-4、11-5，不是本期新论文。引用时标明日期与官方自报（另有动态复现 1,724、API 成本约 $121.3 万等）。GPT‑6 Cyber 当时写明先向部分 Daybreak Red 客户提供。
- **证据**：[@OpenAI](https://x.com/OpenAI/status/2125007927098699827)、[研究文（11-4）](https://openai.com/index/a-thousand-fewer-paths-to-root/)、[产品文（11-5）](https://openai.com/index/introducing-gpt-6-cyber/)
- **约时**：X 再推 11-24 07:25 Asia/Singapore

###### 进展：Gemini 4 Neon / Antigravity——无新的官方改价；有配额与演示
- **是什么**：Neon 发布已在上期主条。本窗口可见 Antigravity 扩容缓存并重置配额、以及再开放 Carbon 等使用体验转述（部分为用户截图，须回对官方设置页）。@GoogleDeepMind 11-24 04:12 Asia/Singapore 发布 Neon 在 Antigravity 中重建图灵 1936 年书房的演示。Today's News 仍在把 11-18 的 Neon 当作新发布，属滞后，不写入来源记录。
- **证据**：[@GoogleDeepMind 演示](https://x.com/GoogleDeepMind/status/2124959312606818597)
- **约时**：11-24 04:12 Asia/Singapore

###### 进展：ChatGPT / Codex 客户端与商业促销
- **是什么**：@thsottiaux 11-22 10:03 Asia/Singapore 询问桌面应用更新后的体验，并称团队已在准备下一个大更新；11-24 06:48 Asia/Singapore 称答案质量将有「显著跳升」（产品负责人口径，无独立评测）。11-24 01:45 Asia/Singapore 称 11-30 前新建的 ChatGPT Business 工作区，各席位在 12-31 前包含用量翻倍；已有 Business 用户「随后也有礼物」。11-24 01:48 Asia/Singapore 称公司内部 dots 正成为主要工作方式。
- **证据**：[@thsottiaux 桌面](https://x.com/thsottiaux/status/2124322968499282388)、[@thsottiaux 质量](https://x.com/thsottiaux/status/2124998553856844186)、[@thsottiaux Business](https://x.com/thsottiaux/status/2124922313019953319)
- **约时**：11-22 10:03 Asia/Singapore 至 11-24 06:48 Asia/Singapore

##### 其他

- **Google DeepMind 量子电路**（官方自报，11-24 01:00 Asia/Singapore）：称用多组 Gemini 4 agent 构建新量子电路，未来模拟成本最多可降 **10 倍**。Today's News 出现「290 倍」等标题，与官方原帖不一致，不以 News 为准。[@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2124911073266413634)
- **OpenWorks**（官方，11-24 01:44 Asia/Singapore）：OpenAI 新项目，资助本地 AI 从业者免费帮助小企业搭建工具；@OpenAIDevs 呼吁申请。[@OpenAI](https://x.com/OpenAI/status/2124922133545714160)
- **AA 语音**：Phonic 1.1（High）在 AA Speech to Speech Index 以 89.1 升至第一（AA 自报，11-24 01:30 Asia/Singapore）。[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2124918494110298127)
- **待核、不升主条**：OpenRouter 输出被他人打开的隐私事件；「内部模型证明 Valiant / VP≠VNP」；Dario「80% 初级岗位」等媒体标题；AMD 登记再售约 $152B 股票等 News 数字；Anthropic IPO 后「现金堆到 $237B」等估值/现金口径；银行抛售数据中心贷款的金额细节。一律需回对原公司或监管文件。
- **窗口内被讨论、但首发早于本窗口或非官方首发**：Inkling 2 Mini 首发、对抗蒸馏原文、GPT‑6 Cyber / 948 研究文，见进展。Qwen3.5 27B「自改权重」论文（准确率 57.2%→63.8% 为论文自报）与 Alexandr Wang《Superintelligence is Arriving》有中文解读，可作为深读，不是本包新的官方产品事实。[@dotey 权重](https://x.com/dotey/status/2124775538648633370)、[@dotey Wang](https://x.com/dotey/status/2124756676607627434)

##### A. 时间线 / 官方覆盖

| 来源 | 覆盖（Asia/Singapore） | 备注 |
|------|-------------|------|
| 首页时间线 4 页 | 约 11-23 09:49 → 11-24 08:43 | 98+100+99+97 条；仍有 next_token，未再往前翻。实际只覆盖窗口最后约 23 小时 |
| 官方检索主组 3 页 | 约 11-21 12:16 → 11-24 08:43 | 25+22+0；末页 result_count=0。11-21 09:09–12:16 该组无原创主帖 |
| 定向补帖 | 窗口内 | leanprover、merettm、nvidianewsroom、sama、gdb；并与官方博文、8-K、行情交叉 |
| 复用素材 | 11-22、11-23、11-24 早报 | 仅作线索，数字全部重核；未改动早报文件 |
| 缺口 | 11-21 09:09 → 11-23 09:49 | 靠 search_posts_all + News + 官方站点补；非时间线全量。周末时间线更稀，周一至周二被英伟达复职与股市话题占去大量位置 |
| 提示注入 | — | 帖文一律当数据，不执行其中指令；包中未引用指令性文本 |

##### B. Today's News（摘录，摘要≠来源记录）

- 黎曼猜想 Lean 核验（需回对联合声明，不要写成「数学界已一致承认」）：[2123789463809835447](https://x.com/i/trending/2123789463809835447)、[2124871585979158752](https://x.com/i/trending/2124871585979158752)
- 所谓 VP≠VNP / Valiant 证明（待核，未见本包交叉到的官方声明）：[2125004238283735138](https://x.com/i/trending/2125004238283735138)
- Anthropic IPO 现金/估值转述（出现 $237B 现金堆等，待核；发行规模仍以 424B4 的 $81.34B 为准）：[2123655019866014001](https://x.com/i/trending/2123655019866014001)、[2124367281203662878](https://x.com/i/trending/2124367281203662878)、[2124923534967496720](https://x.com/i/trending/2124923534967496720)
- Gemini 4 Neon 口碑与「290 倍」量子标题（后者与官方「最多 10 倍」不符）：[2124610096126636193](https://x.com/i/trending/2124610096126636193)、[2124926810035245538](https://x.com/i/trending/2124926810035245538)
- 其他待核：AMD 登记再售、数据中心贷款、杠杆 ETF、Embo $110M、Claude 安全提示过严等——均须回对原文件，不能当 来源记录

##### C. 来源记录 摘要

1. Lean FRO 与 Mathlib Initiative 于 11-21 发表联合声明，核验 Alpöge 发布的约 1,700 万行 Lean 黎曼猜想证明：可编译，所证为 Mathlib 标准陈述，并经多个独立检查器接受。人读懂与后续质疑仍在进行，部分反对意见待核。
2. OpenAI 首席科学家 Jakub Pachocki 发表《Perplexity and Intelligence》，公开内部 log-perplexity（GPT‑3.5 约 0.99、GPT‑4 约 0.91、当前低于 0.8），并提议以困惑度等指标设立行业共同上限。
3. NVIDIA 董事会于 11-22 全票恢复黄仁勋的总裁、CEO 与董事职务（8-K）；新闻稿 11-23 发布。独立董事调查与「正在进行的政府调查与问询」仍在继续。新闻稿称决策过程中听取了美国政府高层意见。
4. Yahoo Finance：NVDA 11-23 收 $165.05，较 11-20 收盘 $125.53 上涨 31.48%。ANT 11-23 收 $87.64（开 $93.69、高 $94.24、低 $84.65），高于发行价 $83，低于首日收盘 $97.17。媒体市值待核；发行规模仍不是市值。
5. Claude Ship（beta）面向 Team / Enterprise 的 GitHub 仓库，含 Code Review、PR Steward 与 Claude Approvals；Plugins 已在 Free/Pro/Max/Ultra 上线（官方称 10,000+）；ZDR+EFS 对符合条件的企业进入公测。Ship 不面向 ZDR / HIPAA / 客户托管密钥组织。
6. OpenAI 与 Cisco 开源 Shirudo，用可签名的 eBPF「盾」在不停机的情况下为运行中的 Linux 系统提供临时防护。博文落款 11-23，X 官宣 11-24 05:37 Asia/Singapore。
7. GPT‑6 Cyber 与「948 个本地提权漏洞」研究文落款 11-4 / 11-5，本窗口只是官号再次介绍，不作为新发布。
8. Reuters 关于 SEC 调查 Nvidia 会计问题的报道为独家、匿名消息源，公司本则 8-K 未确认该具体范围，标待核。

##### E. 建议扩写（3–5）

1. **机器核验 vs 人类理解**：用联合声明的四条标准和 MIT 检查清单，写清「Lean 通过了什么、还没证明什么」；把质疑帖单列为待核，避免写成已经翻案。
2. **Pachocki 的闸门怎么用**：把 0.99 / 0.91 / <0.8 / 0.76 / 0.68–0.7 做成一张带「官方自报、内部数据集」标签的表，并解释为什么思维链进步不会反映在 perplexity 上。
3. **黄仁勋复职对照表**：8-K 与新闻稿写了什么、没写什么（政府高层 vs 总统点名、正在进行的调查 vs SEC 会计调查），再配 NVDA 11-20 与 11-23 的 O-H-L-C。
4. **Claude Ship 的控制权**：PR Steward 不合并、Approvals 先观察、ZDR 组织被排除、以及和 Plugins / ZDR+EFS 的关系，写给要不要打开仓库级自动化的工程负责人。
5. **Shirudo 与旧的 948 研究不要混**：一篇写 eBPF 临时盾和签名/TPM；另一篇如需引用 948 / $121.3 万成本，必须标明 11-4/11-5 旧文与官方自报。


## GitHub 项目与发行

### 项目原始材料

#### GitHub 三日刊（2026-11-21 → 2026-11-24）

1. **Transformers v5.24.0**
`huggingface/transformers` 于 11-21 20:28（Asia/Singapore）发布正式版 v5.24.0（`prerelease=false`）。这一版把 Thinking Machines Lab 的 Inkling 2 Mini 写进官方库：24 层解码器、第 6–17 层循环三遍，并与 Inkling 2 Small 共用图像编码器；同时接入瑞士 Apertus 1.5（图 / 音离散标记进文本骨干，不支持反生成媒体）、Meta FAIR 覆盖 1,600 多种语言的 Omnilingual ASR，以及 NVIDIA Dory、混元 HY4-VL、WavTokenizer、Sarvam-105B / 30B 架构和 LG EXAONE（加载时走 Llama 实现，不再需要 `trust_remote_code`）。Translated 的 Lara Mini（7.2B 总参数、每 token 约 0.6B 激活）也进了库，但权重是 CC BY-NC-SA 4.0 且仓库需申请。破坏性变更是：原来的 `past_key_values` / `cache_params` 统一改名为 `cache`（旧名仍可用但会告警），生成式多模态模型改为共用输出类。本地跑 Inkling 2 Mini、要接新开源多模态 / ASR，或升级后发现 cache 参数对不上的人应该看这版说明。
证据：[v5.24.0 Release](https://github.com/huggingface/transformers/releases/tag/v5.24.0) · [Inkling 2 Mini 说明](https://huggingface.co/blog/inkling2mini)

2. **Unsloth Desktop v0.1.923-beta：Inkling 推理加速与 Fast 图像 / 视频**
`unslothai/unsloth` 于 11-23 23:40（Asia/Singapore）发布 v0.1.923-beta。标签仍带 `-beta`，但 API 字段为 `prerelease=false`。上期刚接入的 Inkling 2 Mini，这期自称在 8–12GB 显卡上解码最高约 1.9 倍、专家全进显存时提示处理最高约 1.9 倍，并改进 RTX Spark；同时新开 NVIDIA Qwen-Image-Flash（自称默认设置下约比 Qwen-Image 快 14 倍）和 FastWan 三步视频（自称比基座最高约 3 倍），以及双卡扩散 LoRA 训练（自称两张 GPU 上样品吞吐约 2 倍）。桌面端还能把翻译结果直接叠到音频、字幕和图片上。训练侧自称 AsyncGRPO 可少花 29–40% 时间。数字均为「自称」。已经在桌面端跑 Inkling，或要试 4 步图像 / 3 步视频的人可以跟上。
证据：[v0.1.923-beta Release](https://github.com/unslothai/unsloth/releases/tag/v0.1.923-beta) · [Inkling 11-23 更新说明](https://unsloth.ai/docs/models/inkling-2-mini#id-23rd-november-update)

3. **OpenAI Codex 0.172.0**
`openai/codex` 于 11-24 08:03（Asia/Singapore）发布正式版 0.172.0（`prerelease=false`；同窗口多枚 `*-alpha.*` 未收）。终端里可以在搜索结果和记录中点开线程链接，用 `Tab` 补全斜杠命令参数（例如 `/mcp lo` 补成 `/mcp login`），并用 `Shift+Up` / `Shift+Down` 在任务组之间跳转；带缓存工具列表的可选 stdio MCP 服务器改为第一次真正调用时再启动。配置里可为单个已连接的应用工具指定审批人，app-server 客户端在设置或登录时可选 Amazon Bedrock Runtime。`codex exec resume` 会恢复已保存的沙箱权限和工作目录，远程会话在客户端与服务器操作系统不同时也会保住工作区路径。附带的文档技能补充了 GPT-6.2 Astra / Sol 的迁移说明，这是文档而非新的权重发布。日常用 Codex 终端、或要把会话接到 Bedrock Runtime 的人应该升。
证据：[0.172.0 Release](https://github.com/openai/codex/releases/tag/rust-v0.172.0)

（热榜口径：日榜约为最近 24 小时，周榜统计最近七天，均于 2026-11-24 08:48 Asia/Singapore 抓取，不可当作本期 72h 净增。HKUDS/CLI-Anything 日榜约 790 星，仍是旧仓留榜，最近正式版还是 6 月的 v0.4.0，本期不单列。日榜前列 obra/superpowers、firecrawl/firecrawl、zhouxiaoka/autoclip 等，以及周榜 plannotator、stitch-skills、open-code-review、astryx、ag-ui、sure、last30days-skill 等，均为旧仓留榜或非本期新进展。新仓搜索首位 `EL4CTEO/fast-anything` 窗口内新建，搜索接口显示总量约 3,123 星、201 个 fork，有 MIT 许可和 npm 包页面，但是个人账户、关注者仅 4，星数可信度待核，本期不单列。同批还有 `sybil-solutions/skill-distill`（仓库体积很小，身份与效果待核，不收录）。新仓后段大量 HTML 仓星数集中在约 338–357，描述像预激活安装包、修改器或「完整工具集即用」，包括 CapCut / Studio One、Cellebrite 取证套件和游戏修改器等，视为可疑克隆或盗版引流，不收录。`ranxianglei/billion-context` 仍无新的可交叉核验进展，继续不收录。）

窗口内无：vllm-project/vllm、sgl-project/sglang、ggml-org/llama.cpp（仅 `b12xxx` 预发布日构建）、ollama/ollama（v0.40.17 现为 `prerelease=false`，但 `published_at` 仍是窗口前的 2026-11-10 22:25 UTC / 11-11 06:25 Asia/Singapore，按发布时间不计入本期）、pytorch/pytorch、huggingface/datasets、modelcontextprotocol/python-sdk、modelcontextprotocol/typescript-sdk、Comfy-Org/ComfyUI、axolotl-ai-cloud/axolotl、langchain-ai/langgraph（常规 / 预发布未收录：openai/codex 多枚 `*-alpha.*`；openai/openai-python v3.58.0 与 openai-node v7.63.0，主要为 agent session 支出限额；anthropics/anthropic-sdk-python v2.13.0 与 TypeScript sdk-v1.13.0，Admin API External Storage 测试以及把 Opus 4.5 标为将于 2027-01-22 停用；langchain-text-splitters 1.2.0、langchain-classic 1.1.0，以及 huggingface / ollama / chroma / qdrant / fireworks 等对接包的小版本）


## 模型与数据集

### 模型、数据与榜单原始材料

#### HF / 模型三日雷达素材 · 2026-11-24

- 窗口：2026-11-21 09:09 Asia/Singapore（01:09 UTC，上期采集截止）→ 2026-11-24 约 08:57 Asia/Singapore（00:57 UTC，实际采集时刻）。
- 去重基线：11/21 素材包（内部证据存档），sha256 bdc724cf…c63a）和 （内部证据存档） 的榜单快照、镜像核查。上期写过的条目只在有新事实时再写，标“更新”。
- 计数：主条 4（全部为本窗新公开）｜跟进 6（Inkling 2 Mini、Hy4、Kimi K3.1 Pro、SenseNova、热度变化、salgr 假仓库）｜次条 7｜补记 1｜榜单 6 段｜数据集 4 条主条 + 4 条附记｜同名镜像/冒名 5 组。
- 数据口径：likes/downloads 统一取 HF API 在 2026-11-24 08:57 Asia/Singapore（00:57 UTC）的快照（采集证据快照）。downloads 是 HF 的近 30 天口径，新 repo 常显示 0。Trending 取 08:48 Asia/Singapore 的 API（模型 300 条、数据集 100 条），trending HTML 页一并保存。
- 开放程度用语：“开放权重”= 权重能下载；“OSI 许可”= 权重许可证属于 OSI 认可的许可证（Apache-2.0/MIT），未逐项核对 OSAID；“自定义/非商用许可”= 权重开放，但不算开源。
- 本窗整体偏安静：没有 Hy4 级别的旗舰发布，新增的是几个中等规模的国产/欧洲开放权重模型；热度榜被 Inkling 2 Mini 及其衍生版占据。窗口内新建 repo：模型 13,789 个、数据集 6,109 个（createdAt 分页统计）。

##### 三句话结论

1. **中国电信（星辰 AGI / 原 TeleChat 团队）放出 Xing4.1-Preview：285B 总参 / 约 17B 激活的 MoE，Apache-2.0，卡片称全程在 8,192 张国产加速卡 + MindSpore 上预训练。** 这是本窗规模最大的新开放权重，但它自己卡片里的对比表显示，在大多数 agent 基准上它落后 Hy4 flash 和 GLM-5.3-Flash，卖点是“全国产算力栈”而不是分数。
2. **蚂蚁 inclusionAI 一口气补了三款 MIT 许可的模型：124B / 5.5B 激活的多模态 Ling-3.2-air（AA 给 23.4 分，高于 Inkling 2 Mini 和 Qwen3.8 27B 的 20.1），以及医疗专用的 LingSante-3.1-flash（560B / 25B 激活）和 LingSante-3.1-air-VL。** Aleph Alpha 也发了 Kolibri 1.1（75B / 3.44B 激活，Apache-2.0，主打德英双语），官方称每任务 GPU 时间比 1.0 少 3.4 倍。
3. **榜单侧最大的进展是拿到了 LMArena 完整表：LMArena 官方在 HF 上公开了 lmarena-ai/leaderboard-dataset，带全部模型的分数、置信区间和票数。** 据此确认：Kimi K3.1 Pro 在文本榜排第 27（开放权重第 2，次于 Kimi K3），新上榜的 Inkling 2 Mini 只排第 210；文本榜刷新到 Nov 22，文生图榜刷新到 Nov 21，视觉榜未刷新。AA 的 Intelligence Index 默认表和两张图片榜都没有变化。

---

##### 主条

###### 1. XingChen-AGI/Xing4.1-Preview · 新开放权重（Apache-2.0，OSI 许可）

中国电信人工智能科技公司（星辰 AGI，Xing 系列前身是 TeleChat）发布的 Xing4.1-Preview 是一个 285B 总参、约 17B 激活的稀疏 MoE：45 层（前 3 层稠密 FFN、后 42 层 MoE），256 个路由专家取 8 个加 1 个共享专家，注意力沿用 DeepSeek-V3.2 一系的 MLA + DSA（DeepSeek 稀疏注意力），配置的最大上下文 1M，定位“agent 编程和长程 agent 工作流”。卡片最强调的是训练栈：预训练全程跑在 8,192 张国产 AI 加速卡上，用 MindSpore 和自研训练系统（HSDP 代替全局 FSDP、按 owner 分片计算 Muon 等），称端到端吞吐提升约 15–30%。要清醒看待的是，卡片自己的对比表里它在多数基准上不如同级的 Hy4 flash 和 GLM-5.3-Flash。

- 为什么重要：
  - 这是“国产芯片 + 国产框架”训练出的最大一档公开权重之一，而且用 Apache-2.0，商用没有额外门槛；同时 FlagRelease 已给出 5 个国产芯片平台（昇腾、天数智芯、沐曦、真武，以及 NVIDIA）的 W8A8 部署版。
  - 技术报告 arXiv 2611.22115（《TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks》）把 HSDP、Muon 分片、选择性重计算等系统细节公开了，对在国产集群上训大模型的团队有参考价值。
- 适合谁 / 阅读建议：
  - 关心国产算力训练栈的读者，读技术报告的系统章节比看分数更有收获。
  - 想部署的团队：BF16 权重约 560GB（261 个分片），需要多机；国产芯片用户直接看 FlagRelease 的 W8A8 版和卡片里的 FlagOS 部署指南。
  - 只想要“最强开放模型”的读者可以跳过：按它自己公布的数字，同尺寸里 GLM-5.3-Flash、Hy4 flash 更强。
- 来源记录：
  - HF 时间：createdAt 2026-11-22 07:47 UTC / 11-22 15:47 Asia/Singapore（窗口内）；261 个权重分片各自一个上传 commit，从 07:49 UTC 到 13:08 UTC（11-22 15:49–21:08 Asia/Singapore）；lastModified 2026-11-23 15:31 UTC / 11-23 23:31 Asia/Singapore（只改 README）。2026-11-23 08:45 UTC 的 commit `4d81e8dd06` 加入 FlagOS 多芯片部署指南。
  - 热度（采集 11-24 08:57 Asia/Singapore）：likes 204 / downloads 672，Trending #254（trendingScore 17）。窗口内新建模型里 likes 排第 1。
  - 许可 / 任务：license apache-2.0，pipeline text-generation，library transformers（custom code：`modeling_deepseek.py`）。开放权重，OSI 许可。
  - 权重证据：261 个 safetensors 共 559.81GB（卡片写约 521.4GiB，BF16，部分辅助张量 FP32）；HF 解析参数 279,902,121,728（卡片写 285B，差额来源未说明）。
  - 官方身份：XingChen-AGI 组织（未认证，391 关注者，11 个模型），组织简介写明是中国电信人工智能科技公司的开源组织；技术报告署名“Xingchen AGI Lab”，v1 提交于 2026-11-17；卡片同时链到 ModelScope 和天翼 AI 平台。
  - 国产芯片部署版：FlagRelease 组织下 Xing4.1-Preview-W8A8-{ascend,iluvatar,metax,zhenwu,nvidia}-FlagOS 五个 repo，nvidia 版权重 2026-11-22 10:54 UTC / 18:54 Asia/Singapore 上传，参数与原版相同；其余四个 11-23 01:58–01:59 UTC 建库。都是 apache-2.0，likes 和 downloads 都是 0（采集 11-24 08:57 Asia/Singapore）。
- 待核：
  - 卡片对比表全部是自测或引用各家报告：Terminal-Bench 4.0 20.6（跳过了 GPU sandbox 任务）、AutomationBench v1.0.6 45.3、Apex-Agents v1.1 50.7、HLE w/ tools 45.7（只测纯文本题）、Claw-Eval pass^3 49.7。同表 Hy4 flash 分别为 19.2 / 52.2 / 63.1 / 55.2，GLM-5.3-Flash 为 35.4 / 48.4 / 51.5 / 52.2。
  - “8,192 张国产加速卡”“吞吐提升 15–30%”是卡片和报告自述；卡片没写具体芯片型号。
  - 卡片里的 GitHub 链接 github.com/XingChen-AGI/Xing4.1-Preview 目前返回 404。AA、LMArena 都未收录。
- 证据：
  - [HF XingChen-AGI/Xing4.1-Preview](https://huggingface.co/XingChen-AGI/Xing4.1-Preview)
  - [arXiv 2611.22115](https://arxiv.org/abs/2611.22115)
  - [modelscope.cn 来源](https://modelscope.cn/models/XingChen-AGI/Xing4.1-Preview)
  - [HF FlagRelease/Xing4.1-Preview-W8A8-ascend-FlagOS](https://huggingface.co/FlagRelease/Xing4.1-Preview-W8A8-ascend-FlagOS)

###### 2. inclusionAI/Ling-3.2-air · 新开放权重（MIT，OSI 许可）

蚂蚁百灵团队的 Ling-3.2-air 是一个原生多模态的“混合线性” MoE：总参 124B、激活 5.5B，35 层 KDA 线性注意力加 7 层 Gated MLA（5:1），512 个路由专家取 8 个，架构与 9 月的 Ling-3.0-flash-VL 相同。它的卖点是用很小的激活量做工作流自动化和专业文档推理。第三方 AA 已在发布当天收录，给出 Intelligence Index v5 23.4 分，比激活量相近的 Inkling 2 Mini（20.1）和 Qwen3.8 27B（20.1）都高。

- 为什么重要：
  - 5.5B 激活拿到 AA 23.4，明显高于激活量相近的 Inkling 2 Mini（约 5.4B 有效激活，20.1）；MIT 许可，比多数国产大模型的自定义许可更宽。
  - 发布当天 Trending #23，SGLang 首发支持并带 MTP 投机解码。
- 适合谁 / 阅读建议：
  - 做文档处理、表格分析、法律/金融类 agent 的团队：卡片推荐 4 张 141GB 级 GPU（H20-3e / H200）跑 256K 上下文，80GB 卡需要 8 卡。
  - 和上期的 Inkling 2 Mini、SenseNova-Loop-9B 放在一起看“小激活模型”这一路线。
- 来源记录：
  - HF 时间：createdAt 2026-11-23 03:55 UTC / 11-23 11:55 Asia/Singapore（窗口内）；权重 commit `cfa6e1fe4e`“Upload folder using huggingface_hub”，2026-11-23 07:25 UTC / 11-23 15:25 Asia/Singapore，13 个 safetensors；13:57 UTC 的 `d9c5700286` 把 config.json 的 max_position_embeddings 从 262080 改成 262144（影响加载配置，已下载的人应同步）；14:49 UTC 补传 `modeling_bailing_moe_v3_vl.py`；lastModified 15:25 UTC / 23:25 Asia/Singapore（README）。
  - 热度（采集 11-24 08:57 Asia/Singapore）：likes 100 / downloads 0，Trending #23（trendingScore 89）。
  - 许可 / 任务：license mit，HF 上 pipeline 字段为空（卡片示例是图文输入）。开放权重，OSI 许可。AA 记为 open weights、permissive、MIT。
  - 权重证据：13 个 safetensors 共 129.28GB；HF 解析参数 127,920,654,544（卡片写 124B 总参）。
  - 官方身份：inclusionAI 组织（未认证，3,759 关注者，253 个模型），即 Ling / Ming / LingSante 系列的发布方；ModelScope 同名 repo。
  - AA：模型页 artificialanalysis.ai/models/ling-3-2-air，releaseDate 2026-11-23，intelligenceIndex 23.39，参数 124B / 5.5B 激活，上下文 1,048,576。不在 AA 默认表里。
- 待核：
  - 卡片自报（与前代比较）：AutomationBench-AA 15.7% → 61%、GDP.pdf 全通过率 8.4% → 16%、AA-Briefcase v1.1 Elo 987 → 1340、Terminal-Bench 4.0 0% → 27%、Harvey LAB-AA v1.1 准则通过率 87.7%（材料幻觉检查后全通过率只有 0.8%）。除 AA Index 外都未见第三方复现。
  - 上下文长度口径不一：AA 写 1M，config 的 max_position_embeddings 是 262,144，卡片推荐配方是 256K。
  - 卡片两张主图指向 intranetproxy.alipay.com，匿名访问返回 302 跳转，外部读者可能看不到图。
- 证据：
  - [HF inclusionAI/Ling-3.2-air](https://huggingface.co/inclusionAI/Ling-3.2-air)
  - [artificialanalysis.ai 来源](https://artificialanalysis.ai/models/ling-3-2-air)
  - [HF inclusionAI/Ling-3.2-air](https://huggingface.co/inclusionAI/Ling-3.2-air/commit/d9c5700286)

###### 3. inclusionAI/LingSante-3.1-flash（+ MXFP4）与 LingSante-3.1-air-VL · 新开放权重（MIT，OSI 许可；医疗专用）

同样来自蚂蚁的医疗大模型系列。LingSante-3.1-flash 基于 Ling-3.1-flash（MIT）继续训练，560B 总参 / 25B 激活、1M 上下文，主打复杂医学推理、循证检索和长程医疗任务，后训练用多教师 on-policy 蒸馏把各项能力合到一个模型里；LingSante-3.1-air-VL 是基于 Ling-3.0-flash-VL 的轻量多模态版（HF 解析约 125B 参数）。卡片明确写“仅供研究和评测，不是医疗器械，不能作为诊断、处方或治疗的独立依据”。上期收录的 LingSante-MedGuard 数据集和 LingSante-Pulse 是同一系列。

- 为什么重要：开放权重的医疗专用大模型不多，500B 级、MIT 许可的更少；flash 版 Trending #22，air-VL #41。
- 适合谁 / 阅读建议：医疗 AI 研究者、做医学检索/问答评测的团队。flash 版卡片的部署示例是 8 × H200（TP8 + EP8）；MXFP4 版体积约减半（313GB）。普通读者只需记住：这是研究用模型，不能直接用于临床。
- 来源记录：
  - LingSante-3.1-flash：createdAt 2026-11-19 04:30 UTC / 11-19 12:30 Asia/Singapore，但上期 11-21 00:51 UTC 前的全量扫描里没有它，当时未公开；权重由两个 commit（`66ba4109c6`、`e020986adc`）在 2026-11-22 05:05 UTC / 11-22 13:05 Asia/Singapore 上传，54 个权重文件 573.78GB，HF 解析参数 572,120,680,768；之后 8 次提交只改 README 和基准图；lastModified 2026-11-23 09:55 UTC / 11-23 17:55 Asia/Singapore。likes 113 / downloads 397，Trending #22（trendingScore 92）。
  - LingSante-3.1-flash-MXFP4：createdAt 2026-11-22 03:19 UTC / 11-22 11:19 Asia/Singapore，153 个权重文件 313.18GB，likes 18 / downloads 325。
  - LingSante-3.1-air-VL：createdAt 2026-11-19 04:31 UTC；权重在 2026-11-20 13:41 UTC / 11-20 21:41 Asia/Singapore 上传（250GB，参数 124,848,460,496），同样不在上期扫描里，公开时刻在本窗内但无法精确到小时；pipeline image-text-to-text；likes 83 / downloads 206，Trending #41（trendingScore 64）（采集 11-24 08:57 Asia/Singapore）。
  - 许可：三个 repo 都是 mit；基座 Ling-3.1-flash、Ling-3.0-flash-VL 也都是 MIT，许可链无冲突。开放权重，OSI 许可。
  - 官方身份：inclusionAI 组织（同上）。
- 待核：
  - 卡片称在 InclusionMed 医疗基准上总分 45.064、在 23 个模型配置里排第 5 并处于性能-成本帕累托前沿；InclusionMed 也是蚂蚁自己的基准。其余医学基准图都是自测。
  - air-VL 的确切公开时间。
- 证据：
  - [HF inclusionAI/LingSante-3.1-flash](https://huggingface.co/inclusionAI/LingSante-3.1-flash)
  - [HF inclusionAI/LingSante-3.1-flash-MXFP4](https://huggingface.co/inclusionAI/LingSante-3.1-flash-MXFP4)
  - [HF inclusionAI/LingSante-3.1-air-VL](https://huggingface.co/inclusionAI/LingSante-3.1-air-VL)

###### 4. Aleph-Alpha/Kolibri-1.1（+ GGUF）· 新开放权重（Apache-2.0，OSI 许可）

德国 Aleph Alpha 在 Kolibri 1.0 发布七周后推出 1.1：仍是 75B 总参 / 3.44B 激活的德英双语 MoE（2 层稠密 + 48 层 MoE，384 专家取 6 个加 1 个共享专家），这次加了“4 层滑窗 : 1 层稀疏注意力”的结构，原生 262,144 上下文、最长可到 1,048,576。它是从 Kolibri 1 的中期训练检查点继续训的（再加 805B 中期训练和 201B 长上下文 token），不是新基座。官方博客称每任务 GPU 时间比 1.0 少 3.4 倍、综合分更高，并在 3–4B 激活这一档“德英双语都最强”。

- 为什么重要：欧洲少有的、持续迭代的主权开放权重模型，Apache-2.0；官方首发就带量化版和 vLLM、transformers 支持。Aleph Alpha 还是欧盟 GPAI 行为准则签署方，卡片的训练数据、算力（5.52×10²² FLOPs）披露比多数模型详细。
- 适合谁 / 阅读建议：需要德语能力或在欧盟合规框架下自部署的团队；最低 2 × H100 或 1 × B200（显存约 77.6GB）。卡片的“Design goals”和 compute 两节值得读。
- 来源记录：
  - HF 时间：createdAt 2026-11-20 09:01 UTC / 11-20 17:01 Asia/Singapore（上期扫描里没有它，当时未公开）；唯一 commit `e9515166e2`“Release 2026-11-23”，2026-11-23 14:59 UTC / 11-23 22:59 Asia/Singapore，权重同时上传，也是 lastModified。卡片“Release Date”写 23rd of November 2026，官方博客日期 23/11/2026。
  - 热度（采集 11-24 08:57 Asia/Singapore）：likes 46 / downloads 4，Trending #62（trendingScore 45）。官方 Kolibri-1.1-GGUF likes 9 / downloads 7。
  - 许可 / 任务：license apache-2.0，pipeline text-generation，library vllm。开放权重，OSI 许可。
  - 权重证据：31 个权重文件 77.54GB；HF 解析参数 75,112,665,344（卡片写总参 75,128,393,984、激活 3,439,874,304）。
  - 官方身份：Aleph-Alpha 组织（HF 认证，1,090 关注者）；官方博客 aleph-alpha.com/en/blog/kolibri-1-1/ 链回 HF。旧版 Kolibri-1 在 2026-11-23 15:38 UTC 加了指向 1.1 的“新版本”提示（commit `59859a1333`）。
- 待核：“GPU 时间少 3.4 倍”“超过 GPT-OSS 120B、Mistral Small 4 和 Nemotron 3 Super”都基于 Aleph Alpha 自己定义的综合分；AA 尚无 Kolibri 1.1 条目（推测 slug 返回 404），LMArena 也未收录。
- 证据：
  - [HF Aleph-Alpha/Kolibri-1.1](https://huggingface.co/Aleph-Alpha/Kolibri-1.1)
  - [aleph-alpha.com 来源](https://aleph-alpha.com/en/blog/kolibri-1-1/)
  - [HF Aleph-Alpha/Kolibri-1.1-GGUF](https://huggingface.co/Aleph-Alpha/Kolibri-1.1-GGUF)

---

##### 跟进（上期条目的新事实）

###### F1. Inkling 2 Mini：登上 HF Trending #1，但在 LMArena 文本榜首秀只排第 210 · 更新

- 判断：热度和竞技场口碑出现明显反差。HF 上它三天里 likes 从 598 涨到 5,492，Trending #4 → #1（trendingScore 1,121），unsloth 的 GGUF 版排 #2、downloads 已到 1,292,888。但 LMArena 文本榜 Nov 22 版第一次收录它，风格控制分 1366.9（95% 区间 1352.4–1381.5，1,793 票），427 个模型里排第 210，低于 Qwen3.8-27B（#112，1435.0）和自家的 Inkling 2 Small（#156，1412.2）。票数还少，区间较宽，但差距远大于区间。AA 仍是 20.1。
- HF 变化：窗口内只有两次 README 修改。`b85c3cfa61`（2026-11-21 22:23 UTC / 11-22 06:23 Asia/Singapore）调整了支持框架列表；`7a67ae2314`（2026-11-23 08:08 UTC / 11-23 16:08 Asia/Singapore）更新评测表，参数一栏从“5/26”改为“5.4/26.4”，并改了 PMPP-Hard、ScreenSpot Pro、CritPt v2 等几格数字。TML-d24-varloop-research 同时更新了评测表。权重没变。
- 衍生：按名称搜到窗口内新建的 Inkling-2-Mini 相关 repo 335 个（GGUF/MLX/NVFP4 为主，另有大量 Uncensored/abliterated 改包，过滤）。完全同名的复制件见冒名段；Red Hat 的 RedHatAI/Inkling-2-Mini 是 11-23 18:41 UTC 的“Duplicate from”原样复制，权重相同。
- 热度（采集 11-24 08:57 Asia/Singapore）：Inkling-2-Mini likes 5,492 / downloads 41,888；ggml-org GGUF downloads 497,658；Inkling 2 Small likes 1,446 / downloads 55,885（上期 649 / 40,574）。
- 证据：[HF thinkingmachines/Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini) · [HF unsloth/Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF) · [HF 数据集 lmarena-ai/leaderboard-dataset](https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset) · 本地 （采集证据快照）、（采集证据快照）

###### F2. 腾讯 Hy4：公开时间基本可推定在 11-20 上午；Hy4 flash 改了一个 Engram 配置；AA 仍没有 Hy4 flash · 更新

- 公开时间（上期待核）：三条证据指向同一时段。GitHub Tencent-Hunyuan/Hy4 在 2026-11-20 02:35 和 02:46 UTC 有推送；HF 上 tencent 的“Hy4”收藏集，按其 ID 内嵌的时间戳创建于 2026-11-20 02:51 UTC；HF repo 被压缩后的唯一 commit 在 03:05 UTC。推定 Hy4 在 2026-11-20 约 03:00 UTC（11:00 Asia/Singapore 前后）公开。这仍是推断，腾讯没有给出官方时间。
- 配置修改：2026-11-23 06:53 UTC / 11-23 14:53 Asia/Singapore，Hy4-flash（commit `eccd3123ee`）和 Hy4-flash-FP8（`8a1b19890d`）同时把 config.json 的 `engram_fp8_embedding` 从 true 改成 false，commit 标题只有“update”，没有说明。它影响 Engram 嵌入的加载方式，已下载的人应同步 config.json。权重未变。
- AA：Tencent Hy4 仍是 34.6、开放权重第 2；Hy4 flash 仍没有 AA 条目（推测 slug tencent-hy4-flash、hy4-flash 都返回 404，已抓页面里也没有这个名字）。LMArena 文本榜完整表里也没有 Hy4，腾讯排名最高的是 Hy3（#77，1455.5）。
- 新衍生：Red Hat 认证组织发布 RedHatAI/Hy4-NVFP4（createdAt 2026-11-21 02:34 UTC，权重 02:41 UTC 上传，沿用 tencent-hy-license，likes 1 / downloads 191）。
- 热度（采集 11-24 08:57 Asia/Singapore）：Hy4 likes 286 / downloads 1,815（上期 127 / 89），Trending #21 → #40；Hy4-flash likes 649 / downloads 7,696（上期 545 / 3,949），#8 → #7；AngelSlim 官方 GGUF downloads 130,690（上期 75,614）。
- 证据：[HF tencent/Hy4-flash](https://huggingface.co/tencent/Hy4-flash/commit/eccd3123ee) · [HF collections/tencent](https://huggingface.co/collections/tencent/hy4-6affb5b22bd7b19ce2487b4d) · [GitHub Tencent-Hunyuan/Hy4](https://github.com/Tencent-Hunyuan/Hy4) · [HF RedHatAI/Hy4-NVFP4](https://huggingface.co/RedHatAI/Hy4-NVFP4) · 本地 （采集证据快照）、（采集证据快照）

###### F3. Kimi K3.1 Pro：LMArena 名次终于查到，文本榜第 27、开放权重第 2 · 更新

- 上期因 LMArena 改版看不到开放模型名次，本期从官方数据集拿到全表：Kimi K3.1 Pro (Max) 1483.1（95% 区间 1475.2–1490.9，7,378 票），Nov 22 版排第 27（Nov 20 版第 29）；开放权重里排第 2，第 1 是旧版 Kimi K3 (Max)（#22，1487.9，45,111 票）。AA 46.5 不变，仍是 AA 开放权重第一。
- HF：moonshotai/Kimi-K3.1-Pro 窗口内没有 commit；likes 2,441 / downloads 73,560（采集 11-24 08:57 Asia/Singapore）（上期 2,420 / 64,576）；Trending #40 → #56。license other（kimi-k3.1-pro），开放权重，自定义许可。
- 同名全量复制件又多 5 个，见冒名段。
- 证据：[HF moonshotai/Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) · [artificialanalysis.ai 来源](https://artificialanalysis.ai/models/kimi-k3-1-pro) · 本地 （采集证据快照）

###### F4. 商汤 SenseNova：Loop-9B 补上 DFlash2 草稿模型；另发机器人 agent 模型 RoboRSI-27B · 更新

- sensenova/SenseNova-Loop-9B-DFlash2：createdAt 2026-11-20 08:03 UTC；检查点 commit `4b73a99c08` 在 2026-11-23 06:29 UTC / 11-23 14:29 Asia/Singapore，1 个权重文件 1.93GB、参数 967,264,768，用于 Loop-9B 的投机解码，部署走 LightLLM；apache-2.0；likes 5 / downloads 2（采集 11-24 08:57 Asia/Singapore）。
- sensenova/SenseNova-RoboRSI-27B：机器人操作用的视觉语言 agent 模型，可以调用 VLA 策略、审查轨迹或直接写代码算夹爪目标位姿（Code as Policy），通过“模型 + Harness 一起迭代”的递归自我改进训练。createdAt 2026-11-17 11:51 UTC，唯一 commit `48be9e0ae2`“Release”在 2026-11-23 06:23 UTC / 11-23 14:23 Asia/Singapore；12 个权重文件 54.71GB、参数 27,356,728,560；基座 SenseNova-RoboRSI-27B-Preview；apache-2.0；likes 18 / downloads 4，Trending #232。卡片称 RoboDojo 平均 34.7（Preview 10.0），自测待核。
- 主模型 SenseNova-Loop-9B 窗口内无 commit；likes 643 / downloads 2,036（上期 445 / 1,631），Trending 仍 #9。“256K 上下文约 15GiB 显存”仍无第三方复测。
- 证据：[HF sensenova/SenseNova-Loop-9B-DFlash2](https://huggingface.co/sensenova/SenseNova-Loop-9B-DFlash2) · [HF sensenova/SenseNova-RoboRSI-27B](https://huggingface.co/sensenova/SenseNova-RoboRSI-27B) · [GitHub OpenSenseNova/SenseNova-RoboRSI](https://github.com/OpenSenseNova/SenseNova-RoboRSI)

###### F5. 热度变化：Haru-4B 的 likes 三天少了约 4,500；DepthPro2 涨到 1,141 · 更新

- higurashi-ai/Haru-4B：仍只有 11-13 那一个 commit，但 likes 从上期的 5,437 降到 939（downloads 9,087），Trending #1 → #6。likes 大幅回落的原因不明，可能是 HF 清理了异常点赞，待核。Agnes-AI/Agnes-2.5-Pro-Theta 也从 59 降到 55。
- apple/DepthPro2（上期次条）likes 125 → 1,141，Trending #16 → #12；主 repo 仍不含权重，downloads 0。apple/FastFrames-L likes 569、downloads 仍为 0，Trending #12 → #10，计数原因仍待核。
- harness-hub/Qwen3.8-27B-pi-adapted：只改 README，likes 1,036，Trending #2 → #5。RadixArk/DaisyRose-27B likes 346 / downloads 2,130，#27 → #17，无新 commit。microsoft/Aion-1.0-Instruct-2.3B likes 277 / downloads 4,747，无新 commit。
- internlm/Sage-S2.1-Flash 2026-11-23 03:15 UTC 只在 README 加了技术报告引用（arXiv 2611.21072），license 元数据仍为空，likes 316。Agnes 2.5 Pro Theta 窗口内无 commit，基座和许可问题仍无新证据。
- （以上 likes/downloads 均采集于 11-24 08:57 Asia/Singapore）
- 证据：[HF higurashi-ai/Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B) · [HF apple/DepthPro2](https://huggingface.co/apple/DepthPro2) · [HF apple/FastFrames-L](https://huggingface.co/apple/FastFrames-L)

###### F6. salgr 的假“闭源模型”仓库已全部下线 · 更新

- 上期提醒的 salgr/Gemini-4-Neon 以及抽查的 Gemini-4-Carbon、Claude-Opus-5.5、GPT-6.3-Astra、Claude-Fable-6.9、GPT-6-Cyber，匿名访问现在都返回 401（已删除或转为私有）。该账号当前公开的只有 11-22 至 11-23 新建的 9 个 SalgrAI_* 小模型，元数据写明基于 google/gemma-3-270m-it、Qwen2.5-Coder-0.5B-Instruct 等，不再冒用大厂模型名。上期的风险提示可以降级。
- 证据：本地 （采集证据快照）、（采集证据快照）（salgr/Gemini-4-Neon 401）

---

##### 次条（新发布，信号弱或场景窄）

- **MemTensor/MemT-1.0-Pro**：“记忆原生”模型，把持续更新的记忆状态做进模型计算里，而不是靠检索或超长 KV cache；基座是 NVIDIA Nemotron-3-Ultra-550B-A55B，卡片写 554B 总参 / 59B 激活、4.23B 可训练记忆参数，称在 128K 历史长度下存储约为完整 KV cache 的 1/66。createdAt 2026-11-20 13:14 UTC / 11-20 21:14 Asia/Singapore，权重 19 个 commit 在 16:32–18:03 UTC 上传（226 个文件 1,129.51GB，HF 解析参数 564,752,562,944），上期扫描里不在，判断为本窗公开。license other（openmdw-1.1），与基座相同。likes 65 / downloads 31，Trending #47（采集 11-24 08:57 Asia/Singapore）。技术报告 arXiv 2610.26825（v1 10-19），指标待核。MemTensor 组织未认证。[HF MemTensor/MemT-1.0-Pro](https://huggingface.co/MemTensor/MemT-1.0-Pro) · [arXiv 2610.26825](https://arxiv.org/abs/2610.26825) · [GitHub MemTensor/MemT-1.0](https://github.com/MemTensor/MemT-1.0)
- **Lakonik/pi-H3**：Hansheng Chen、Gordon Wetzstein、Leonidas Guibas 等人（卡片署名）的 MiniMax-H3 蒸馏适配器，卡片标题“2–4 步生成视频、不需要 VAE 解码器”。repo 11-12 建库，唯一的发布 commit `9114cb21f8`“Release pi-H3 1.0 adapters”在 2026-11-21 12:06 UTC / 11-21 20:06 Asia/Singapore；6 个权重文件 13.0GB；沿用 minimax-h3-community-license-agreement（非 OSI）。likes 220 / downloads 32,375，Trending #37（采集 11-24 08:57 Asia/Singapore）。个人账号发布，效果待核。[HF Lakonik/pi-H3](https://huggingface.co/Lakonik/pi-H3)
- **腾讯 WeMM-Ecom 系列（0.8B / 2B / 4B / 9B / 35B-A3B，各带 FP8 / GGUF / GPTQ）**：微信电商场景的多模态内容理解模型，基于 Qwen3.5（35B-A3B 版基座 Qwen/Qwen3.5-35B-A3B）。repo 11-18 建库，BF16 权重在窗口内上传（35B-A3B `8f4f44f36d` 2026-11-23 09:59 UTC / 11-23 17:59 Asia/Singapore，70.21GB；9B 09:54 UTC，18.82GB）。apache-2.0，OSI 许可。热度很低：35B-A3B likes 8 / downloads 0（采集 11-24 08:57 Asia/Singapore）。卡片里的 GitHub 链接 Tencent/WeMM-Ecom 目前 404。[HF tencent/WeMM-Ecom-35B-A3B](https://huggingface.co/tencent/WeMM-Ecom-35B-A3B)
- **腾讯 WePocketModel 1.0（2B / 4B，含 GGUF）**：微信 AI 的端侧视觉语言模型，一个模型同时做生成、图文向量（4B 版 2,048 维）和结构化决策三件事。4B 版唯一 commit `d57517468f`“Release WePocketModel 1.0”在 2026-11-23 11:23 UTC / 11-23 19:23 Asia/Singapore，6 个权重文件 9.13GB、参数 4,539,265,536；apache-2.0。likes 9 / downloads 35（4B），2 / 25（2B）（采集 11-24 08:57 Asia/Singapore）。[HF tencent/WePocketModel1.0-4B](https://huggingface.co/tencent/WePocketModel1.0-4B) · [GitHub Tencent/WePocketModel](https://github.com/Tencent/WePocketModel)
- **Salesforce/BLIP-Live（+ BLIP-Live-Gemma）**：Salesforce 研究院的“主动式流媒体视频 agent”微调，研究在视频流里该何时开口（论文 arXiv 2611.21553，提交于 2026-11-16）。基于 Qwen3.5-35B-A3B 的 LoRA（rank 64）合并全量权重，21 个文件 71.9GB；完整模型 commit 在 2026-11-20 14:40 UTC，但上期扫描里没有这个 repo，判断为本窗公开；11-23 20:46 UTC 补上论文链接。license cc-by-nc-4.0（非商用，非 OSI）。likes 0 / downloads 2（采集 11-24 08:57 Asia/Singapore）。Salesforce 组织 HF 认证。[HF Salesforce/BLIP-Live](https://huggingface.co/Salesforce/BLIP-Live) · [arXiv 2611.21553](https://arxiv.org/abs/2611.21553)
- **CaryPalmer/Kintsugi-27B**：个人开发者把 Qwen3.8-27B 压到 2.47 bit/权重，配自研推理引擎，称 12GB 显卡就能跑满 262,144 上下文、agent 任务上与 BF16 持平、245K 处“大海捞针”24/24。createdAt 2026-11-20 19:53 UTC（上期采集时已公开，当时漏收）；2 个权重文件 11.64GB；apache-2.0；likes 68 / downloads 7,312，Trending #44（采集 11-24 08:57 Asia/Singapore）。属社区量化，全部数字是作者自测，待核。[HF CaryPalmer/Kintsugi-27B](https://huggingface.co/CaryPalmer/Kintsugi-27B) · [GitHub professorpalmer/Kintsugi-27B](https://github.com/professorpalmer/Kintsugi-27B)
- **其他信号弱的新发布**：allenai/RoboTracker（机器人视频点跟踪，基于 aharley/alltracker，apache-2.0，0.07GB，11-23 补齐 RoboTrack-Bench 分数，likes 1 / downloads 0）；OpenMOSS-Team/VideoGym-LTX-2.3（基于 LTX-2.3，权重 2026-11-23 09:45 UTC 上传，ltx-video-2-open-source-license，likes 4 / downloads 0）。只记一笔。[HF allenai/RoboTracker](https://huggingface.co/allenai/RoboTracker) · [HF OpenMOSS-Team/VideoGym-LTX-2.3](https://huggingface.co/OpenMOSS-Team/VideoGym-LTX-2.3)

###### 补记：窗口前发布、往期漏掉的（不算本期新发）

- **OVHaiLLM/Olala-v1.0-mini-7A1B**：Mamba 混合架构的 7B 总参 / 1B 激活 MoE，支持工具调用和推理，卡片写在欧洲的 JUPITER（1,024 张 GH200）、Jean Zay、MeluXina 超算上训练，并披露约 1.16 GWh 能耗。10-30 建库，v1.0 commit 在 2026-11-19 10:13 UTC，早于本窗；窗口内只改卡片。HF 解析参数 6,773,124,144；apache-2.0；likes 302 / downloads 63,289，Trending #46（采集 11-24 08:57 Asia/Singapore）。OVHaiLLM 组织未认证（326 关注者），与 OVHcloud 的关系卡片未写明，待核。[HF OVHaiLLM/Olala-v1.0-mini-7A1B](https://huggingface.co/OVHaiLLM/Olala-v1.0-mini-7A1B)

---

##### 数据集

###### D1. X-LANCE/SynthDCB · 新数据集（cc-by-4.0）

- 判断：一个评测 agent“设备控制”能力的基准，覆盖家居、汽车、手机三个场景，配套“World Distillation”流水线把设备说明自动变成可执行的模拟环境和确定性任务，适合做 agent 训练的奖励设计。
- 来源记录：卡片写 22 个模型、2,560 道测试题、32 种子任务、8 种指令风格、20 多项诊断指标。createdAt 2026-11-18 07:44 UTC，但不在上期全量扫描里，判断为本窗公开；lastModified 2026-11-23 06:36 UTC / 11-23 14:36 Asia/Singapore。likes 26 / downloads 1,575（采集 11-24 08:57 Asia/Singapore），数据集 Trending #46。
- 待核：卡片里与 Codex 的 token 消耗对比（少 46.2–92.5%）是自测。
- [HF 数据集 X-LANCE/SynthDCB](https://huggingface.co/datasets/X-LANCE/SynthDCB)

###### D2. rimelabs/PhonBench · 新数据集（cc-by-sa-4.0）

- 判断：TTS 公司 Rime 发布的发音评测集，1,500 个词、6 种语言（英、德、法、西、意、葡），含音频、单词和 IPA 标注，用来测语音合成“读不读得准”。
- 来源记录：createdAt 2026-11-23 18:04 UTC / 11-24 02:04 Asia/Singapore，分 5 次上传、1,503 个文件；likes 4 / downloads 0（采集 11-24 08:57 Asia/Singapore），Trending #56。
- [HF 数据集 rimelabs/PhonBench](https://huggingface.co/datasets/rimelabs/PhonBench)

###### D3. THUSI-Lab/GameDojo · 新数据集（许可字段为空）

- 判断：清华等机构的游戏 agent 基准环境包，覆盖 20 个游戏环境里的 120 场 Boss 战（2D、3D 各 60 场，各分三档难度）。注意卡片说的 600 小时游戏轨迹数据还在待发布清单里，目前放出的是环境、训练接口和评测框架。
- 来源记录：createdAt 2026-11-21 11:52 UTC / 11-21 19:52 Asia/Singapore；likes 2 / downloads 51（采集 11-24 08:57 Asia/Singapore）。HF license 字段为空，使用前需核实许可。
- [HF 数据集 THUSI-Lab/GameDojo](https://huggingface.co/datasets/THUSI-Lab/GameDojo) · [gamedojo-benchmark.github.io 来源](https://gamedojo-benchmark.github.io/)

###### D4. cfahlgren1/tesla-fsd-drive-5min · 新数据集（cc-by-4.0）

- 判断：一段 5 分钟、6 路摄像头的特斯拉 Model Y（HW4）FSD（Supervised）连续驾驶记录，带逐帧车辆遥测，规模很小，适合做自动驾驶数据格式和可视化的样例。
- 来源记录：createdAt 2026-11-23 03:42 UTC / 11-23 11:42 Asia/Singapore；卡片写已去除位置和时间元数据、遮挡本车车牌，帧率 36fps。likes 23 / downloads 319（采集 11-24 08:57 Asia/Singapore），Trending #40。个人账号发布，拍摄素材的权利归属待核。
- [HF 数据集 cfahlgren1/tesla-fsd-drive-5min](https://huggingface.co/datasets/cfahlgren1/tesla-fsd-drive-5min)

###### 数据集附注

- **lmarena-ai/leaderboard-dataset**（cc-by-4.0）：LMArena 官方的榜单数据集，每次刷新都把各赛道（text、vision、text_to_image、image_edit、webdev、agent 等）的完整表写进 parquet，含分数、置信区间、票数和许可证字段，最近一次 commit 2026-11-23 04:09 UTC / 11-23 12:09 Asia/Singapore。本期榜单段的全表数据都来自这里，下期起可以替代 WebFetch 抓页面。[HF 数据集 lmarena-ai/leaderboard-dataset](https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset)
- **模型输出蒸馏数据**：Jackrong/DeepSeek-V4.1-Flash-Nemotron-Competitive-Coding-Distill（Trending #22，likes 44）和 Jackrong/Qwen3.8-2.4T-A95B-Distill；zake7749/Qwen4-Max-Agentic-Trajectories（1,722 条轨迹，license 写 other: qwen-4-max，而 Qwen4 Max 是闭源模型）。这类数据的许可取决于原模型的使用条款，商用前需核实。[HF 数据集 Jackrong/DeepSeek-V4.1-Flash-Nemotron-Competitive-Coding-Distill](https://huggingface.co/datasets/Jackrong/DeepSeek-V4.1-Flash-Nemotron-Competitive-Coding-Distill)
- **补记 xlangai/RoboWild**（apache-2.0）：RoboWild 机器人 agent 基准的 OpenUSD 场景、物体和机器人模型资产，共 38 个仿真环境，供 Isaac Lab 加载。createdAt 2026-11-20 15:20 UTC，上期采集时已公开但漏收；likes 37 / downloads 4,879，Trending #39（采集 11-24 08:57 Asia/Singapore）。[HF 数据集 xlangai/RoboWild](https://huggingface.co/datasets/xlangai/RoboWild) · [robowild.xlang.ai 来源](https://robowild.xlang.ai)
- **延续热度**：Vyber07/cyber-security（#1）、Angais/pixel-art-atlas-1.4m（#2）、nvidia/USDCraft-10K（#3）、Digitaluz/uzbek-language-corpus（#5，likes 142）、HubLabs/HubEgo-100K（#8，gated: auto）都是往期条目，本期没有展开。FINAL-Bench/weil-positivity-gauge（数学证明类，作者自述结论）降权不收。

---

##### 榜单

###### B1. LMArena 文本榜：更新到 Nov 22；唯一新面孔是 Inkling 2 Mini（#210）；本期首次拿到完整表

- Nov 20 → Nov 22；总票数 9,213,799 → 9,241,799；模型 426 → 427。前三不变：Gemini 4 Carbon (High) 1527、Gemini 4 Argon (High) 1520、Gemini 4 Neon (High) 1512。前 20 只有小幅换位：Claude Opus 4.6 (High) 与 Claude Fable 5.2 (Max) 互换第 7、8，Gemini 3.8 Flash (High) 与 Muse Spark 1.3 (Max) 互换第 11、12，Gemini 4 Hydrogen (High) 从第 18 升到第 17。
- 完整表来源：网页对 WebFetch 仍只渲染前 15 名，本期改用 LMArena 官方 HF 数据集 lmarena-ai/leaderboard-dataset 的 text_style_control 子集（与网页默认分数一致，前 15 名误差 <1 分），快照在 （采集证据快照）。
- 开放权重名次（Nov 22，按风格控制分）：Kimi K3 (Max) #22 1487.9 > Kimi K3.1 Pro (Max) #27 1483.1（Nov 20 版 #29）> MiMo-V2.6-Pro #31 1481.3 > GLM-5.3 (Max) #33 1481.1（#30 → #33）> GLM-5.3-Flash #37 > GLM-5.2 (Max) #40 > DeepSeek-V4.1-Flash-20260910 (Max) #43。Inkling 2 Small #156，Inkling 2 Mini #210，Qwen3.8-27B #112。427 个模型里有 231 个的许可证字段不是 Proprietary。
- [lmarena.ai 来源](https://lmarena.ai/leaderboard/text) （curl 403，WebFetch 可读；快照 （采集证据快照）

###### B2. LMArena 视觉榜：没有刷新；上期没认出的另一个新增模型是 GPT-6.1 Terra (Max)

- 网页仍是 Nov 20 版（1,606,278 票，168 个模型），与上期相同。用数据集补齐上期缺口：Nov 20 版相对 Nov 8 版新增 Claude Fable 5.2 (Max)（#2，1305.3）和 GPT-6.1 Terra (Max)（#44，1263.0），同时移除了 GLM-5V-Turbo，所以模型数只净增 1。
- 开放权重最高：GLM-5.3-Flash #36（1273.8）、Kimi K2.6 #40、Gemma 4 31B #41。
- [lmarena.ai 来源](https://lmarena.ai/leaderboard/vision)

###### B3. LMArena 文生图榜：更新到 Nov 21；新增 Recraft V4.1 Flash V2；Gemini Nano Banana 2.1 掉了 22 分

- Nov 16 → Nov 21；票数 6,988,405 → 7,045,110；模型 86 → 87。新增 Recraft V4.1 Flash V2（闭源，#62，1098.0）。前 7 名不变，第 1 仍是 GPT-Image-2.5 Sunburst 1429；Gemini Nano Banana 2.1 从 1327.6 降到 1305.0，与 Grok Imagine Image 2.0 互换第 8、9。MAI-Image-2.7 仍 #4。
- 开放权重最高仍是 Qwen-Image-2.1（#22，1226.9，许可 qwen-research），MiniMax H3-Image #24（1198.4）。
- [lmarena.ai 来源](https://lmarena.ai/leaderboard/text-to-image)

###### B4. AA 文生图榜：无增减

- 116 行，与上期相比没有新增或移除。第 1 仍是 GPT Image 2.6 Sunburst (max) 1263±14（上期 1262）；MAI-Image-2.7 1215；H3-Image 排第 27，1066。
- [artificialanalysis.ai 来源](https://artificialanalysis.ai/image/leaderboard/text-to-image)

###### B5. AA 图像编辑榜：无增减

- 86 行，没有新增或移除，前列分数完全未变。第 1 仍是 MAI-Image-2.7 1215；H3-Image 第 14，1136。
- [artificialanalysis.ai 来源](https://artificialanalysis.ai/image/leaderboard/editing)

###### B6. AA Intelligence Index v5：默认表无变化；新收 Ling-3.2-air 23.4

- 首页默认 28 个模型的成员和分数与上期完全相同：前三 Claude Fable 5.2 64.6、GPT-6.2 Astra 62.1、Gemini 4 Neon 61.4；开放权重排序 Kimi K3.1 Pro 46.5 > Tencent Hy4 34.6 > DeepSeek V4.1 Flash 1017 32.6 > GLM-5.3 31.7 > Inkling 2 Small 30.6。
- 新收录 Ling-3.2-air（23.4，2026-11-23，开放权重、MIT），不在默认视图。Hy4 flash、Kolibri 1.1、Xing4.1-Preview 都还没有 AA 条目。
- [artificialanalysis.ai 来源](https://artificialanalysis.ai/models) · [artificialanalysis.ai 来源](https://artificialanalysis.ai/models/ling-3-2-air)

---

##### 延续热度 / 降权 / 冒名

###### HF Trending 模型前 10 点评（trending API 08:48 Asia/Singapore；likes 来自 08:57 Asia/Singapore 快照）

  1. thinkingmachines/Inkling-2-Mini：见 F1。
  2. unsloth/Inkling-2-Mini-GGUF：社区量化分发，downloads 1,292,888。
  3. inworld/voice-isolator：上期补记，没有新 commit，downloads 仍为 0。
  4. AtomicChat/Inkling-2-Mini-Uncensored-GGUF：Uncensored 改包，likes 650，降权。
  5. harness-hub/Qwen3.8-27B-pi-adapted：见 F5。
  6. higurashi-ai/Haru-4B：见 F5，likes 大幅回落。
  7. tencent/Hy4-flash：见 F2。
  8. SulphurAI/Sulphur-3：基于 MiniMax-H3 的“无审查”视频模型（往期记作 FusionCow/Sulphur-3，旧地址现 307 跳转到新组织），11-21 只整理了目录结构，降权。
  9. sensenova/SenseNova-Loop-9B：见 F4。
  10. apple/FastFrames-L：见 F5。

###### 降权（只改 README / 文档，或属于改包）

- 只改说明、模板或文档、不动权重：Inkling 2 Mini 评测表、TML-d24-varloop-research 评测表、Sage S2.1 Flash（加引用）、AngelSlim/Hy4-flash-GGUF（README 图片）、Comfy-Org/MiniMax-H3-Image（工作流链接）、unsloth/Inkling-2-Mini-GGUF（README）、Olala（卡片）、Kolibri-1（新版本指针）、Xing4.1-Preview 和 LingSante 的多次 README 修改。
- Uncensored / heretic / abliterated 改包：AtomicChat/Inkling-2-Mini-Uncensored-GGUF（Trending #4）、nokeepai/Inkling-2-Mini-Unbound-GGUF、OpenUncensored/Inkling-2-Mini-Uncensored、DavidAU/Inkling-2-Mini-26B-Heretic-Uncensored-Turbo-Brilliance-50X-V2-AGI、orcarouter/Hy4-flash-abliterated-GGUF、Blackfrost-AI/Inkling-2-Mini-Derisked、SulphurAI/Sulphur-3、TenStrip/10Eros-Max、chatrlabs/Qwen-Image-2.1-Uncensored-Omni-Quantized，过滤。
- Sentinel7/h3（Trending #18，likes 1,499、downloads 0，批量上传的 NSFW LoRA 文件夹）降权。
- 小众社区改造：strata-engine 的 Inkling-2-Mini-Strata / Hy4-Flash-Strata（自定义 .strata 压缩格式）、eltokh7/inkling-2-mini-decision、autotrust/inkling-2-mini-concise，信号弱，只记名。

###### 冒名 / 同名复制（本地 （采集证据快照），按 LFS sha256 与官方 tree 比对）

- **组 1：LingSante-3.1-flash 原样复制**：blearyhope/LingSante-3.1-flash（56/58 个 LFS 文件与官方相同，不同的 2 个是官方之后更新的 benchmark 图）、Harish117/LingSante-3.1-flash（58/58）、Brobhavesh/LingSante-3.1-flash（58/58）。都在 11-23 创建，downloads 0–13，没有写 base_model。MIT 允许再分发，不判定为恶意，但容易被误认为官方 repo。
- **组 2：Kolibri-1.1**：nokkela-ai/Kolibri-1.1（32/32 相同，11-23 16:49 UTC 建库，写明了 base_model Aleph-Alpha/Kolibri-1.1），属透明的再上传。nokkela-ai 上期也复制过 Inkling-2-Mini。
- **组 3：Inkling-2-Mini 完全同名 17 个**：14 个与官方 4/4 个 LFS 文件逐一相同（RedHatAI、YuCollection、sharonSD、synaptex-community、txchmechanicus、blearyhope、rorz99、robfon19、AlpooXYZyt56、FamilyOrang、Theoversight、omegabaer、red4ct3d、Marti99），downloads 0–26。其中 RedHatAI 是 HF 认证的 Red Hat 组织，首个 commit 写“Duplicate from thinkingmachines/Inkling-2-Mini”，不算冒名。litert-community（LiteRT int8 转换）和 drawthingsai（Draw Things 应用的 .ckpt）是格式转换，文件不同；rao-studios 只有 2/4 相同，写了 base_model。
- **组 4：Kimi-K3.1-Pro 又多 5 个**：Kiruba072、SAIFIINDUSTRIES、omegabaer、AdelKazzaz、rlmyfs，98/98 个 LFS 文件与官方相同，downloads 0–29。加上往期记录，累计 23 个。
- **组 5：blearyhope、FamilyOrang、omegabaer 等账号批量复制**：blearyhope 本窗复制了 LingSante-3.1-flash 和 Inkling-2-Mini（上期复制过 Hy4），FamilyOrang 复制了 Inkling-2-Mini（上期复制过 Hy4 / Hy4-flash / Kimi），omegabaer 同时复制了 Inkling-2-Mini 和 Kimi-K3.1-Pro。这些账号都没有写来源，但文件与官方一致，目前没有看到篡改权重的证据。salgr 的假仓库已下线，见 F6。

---

##### 口径、缺口与校验

- 统计口径：likes/downloads 统一取 2026-11-24 08:57 Asia/Singapore（00:57 UTC）快照（采集证据快照）；Trending 名次取 08:48 Asia/Singapore 的 trending API；时间同时给 UTC 和 Asia/Singapore；“权重 commit”指改动了 safetensors/gguf 等 LFS 权重文件的 commit。LMArena 名次按风格控制分排序，数据集的 publish_date 有时比网页标题早一天（视觉 2026-11-19 对应网页 Nov 20，文生图 2026-11-20 对应 Nov 21）。
- 未能拿到 / 未绕过：
  - 多个 repo 建库早于窗口但当时是私有的（LingSante-3.1-flash / air-VL、Kolibri-1.1、MemT-1.0-Pro、BLIP-Live、WePocketModel），只能用两次全量扫描框定“本窗内公开”，精确时刻待核。
  - Hy4 的公开时间只是推断（见 F2）。
  - Xing4.1-Preview 和 WeMM-Ecom 卡片里的 GitHub 链接 404；Ling-3.2-air 卡片图片在支付宝内网域名（302）。
  - AA 没有 Hy4 flash、Kolibri 1.1、Xing4.1-Preview 的条目。
  - HubLabs/HubEgo-100K 和 RodrigoFlorencio/brazilian-portuguese-medicine-corpus 是 gated，commits 接口匿名 401。
- 待核总表：所有模型卡和技术报告里的基准分数；Ling-3.2-air 上下文长度口径；Haru-4B likes 回落原因；FastFrames downloads 一直为 0 的原因；Kintsugi-27B “与 BF16 持平”；MemT “存储省 66 倍”；Olala 与 OVHcloud 的关系。
- 校验：全部 HF id 的 API 200 检查见 （内部证据存档）；外链检查见 （采集证据快照）（LMArena 对 curl 返回 403，WebFetch 可读，单独注明）；证据目录 （内部证据存档）（lb/、ext/、suspect/、commits/、cards/、api/）。

