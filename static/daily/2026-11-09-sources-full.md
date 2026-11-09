# 2026-11-09 AI行业动态：全量原始素材

本期信息窗口从 2026 年 11 月 6 日 09:50 起，至 11 月 9 日各来源的实际采集截止，时区为 Asia/Singapore。本文保留采集到的全量原始摘要与来源链接，不是深读成稿，也不意味着所有候选均已独立复现。正文另见[本期深读](https://guige.ai/guige-ai-site/daily/2026-11-09/)。

- 研究与官博：研究汇总约截止 09:21；官博补充读取至约 09:25；arXiv 扫描约至 09:30。包括研究汇总、官方原文摘录和论文候选三份材料。
- X 公开动态：约截止 09:18；时间线只覆盖部分时段，其余以公开检索补充，不代表全量时间线。
- GitHub 项目与发行：榜单与仓库核验快照为 09:19；日榜、周榜不等于本期净增。
- 模型与数据集：复验截止 09:25:43；保留模型卡、权重提交、许可、榜单与访问限制记录。

原始材料之间可能保留不同取舍，以下说明用于避免误读，不改写成已经解决的事实：研究流未找到 DeepMind 独立博客，X 流另有官方帖子、文章及论文来源；缺少博客不是缺少所有一手来源。Anthropic 页面只有日级日期，窗口边界仍待核。arXiv 11 月 6 日余批是补充扫描；11 月 9 日早放摘要的批次归属待列表确认。audnai 第三方仓的公开元数据已有 96 片权重记录，受限内容与真实文件未核，不可沿用空仓或诈骗定性。以下保留该第三方仓的公开元数据与原始来源链接；非官方不等于冒名，访问受限也不等于恶意。

除去内部协作名称、个人隐私、内部本地证据路径、来源标记和不宜公开的安全操作细节，正常来源与候选保留；未读、待核、自报与不收录理由照录。以下材料不是投资、上线或商业授权建议。


## 研究与官博

### 研究汇总

#### 研究素材包 · 2026-11-09（窗口 2026-11-06 09:50 → 11-09 ~09:21 Asia/Singapore）

> 官博 4 条 + arXiv 5 条（共 9 真重点）。数字标 来源记录 / 官方自报 / 作者自报 / 待核。原始摘录见同目录 labs-raw.md、arxiv-raw.md。
> arXiv：上期余批 **2611.07144–08487** 已补齐；**11/09 仅早放 08488–08710**（listing 未出，归属待核）；续扫 **08711+**。
> 网络安全与生物条目只写结论与官方数字，不写利用/实验步骤。

##### 官博

###### 1. Anthropic：agent 记忆拆成「写 notes + dreaming」
把跨会话记忆定义成可读写的笔记，并用空闲时「dreaming」对日志离线重放：纠错、建 wiki、把关键笔记提升到每会话预载层。这是产品侧把记忆工程化的系统说明，对长程 agent / 上下文产品是硬参考；但需与同窗 arXiv Memory Trap 对照——后者证明良性互动写入的记忆也会越界造成不安全行为，**dreaming 纠事实错误 ≠ 自动解决「作用域」安全问题**（关联/差异见下条 arXiv）。
- CL-Bench 数据库任务上，Opus 5 / 5.5、Sonnet 5.5 能闭环写已验证规则；「只记失败」规则反而削弱记忆增益（官方自报）。Pokémon：Sonnet 3.7 约 413 文件/225 文件夹、1 badge vs Fable 5 约 9 文件/2 文件夹、4 badges（约 10k steps）（官方自报）。Stainless 语料 ~350k 文件 / ~420M tokens；dreaming 2→128 会话，25 问评分 13%→48%；wiki+search 54%→61% vs search alone 53%；约省 20k tokens/问（官方自报）。Harvey LAB 多文档题 wiki 87% vs search 73%；合同事实进 wiki 41/57→57/57（改指令后）（官方自报）。页面仅日级日期 Nov 6，精确时刻待核。

> 编辑注：原文把 Harvey LAB 与并购问答合写。87%/73% 实指 24 道并购问题中需跨文档综合的项目，不是 Harvey LAB 总分；41/57 与 57/57 是改写建库指令前后、生成简报可满足的合同事实标准，不宜直接当作 wiki 全库事实召回率。均为[厂商评测](https://www.anthropic.com/research/components-of-agent-memory)。
- [官博](https://www.anthropic.com/research/components-of-agent-memory) · 配读 [Memory Trap 2611.07554](https://arxiv.org/abs/2611.07554)

###### 2. NVIDIA：Reshard 集合通信加速 RL weight refit
把 train GPU→infer GPU 的权重刷新从 gather-and-broadcast 改成 DTensor「Reshard」，只传源/目的分片交集；开源 NCCL M2N Reshard，接入 NeMo RL。万亿参后训练里「搬权重」成为显性瓶颈时，这是可引用的系统解法。
- 逻辑 payload 量级估算：最大开源权重量级下 gather+broadcast 约 ~10 TB/次（Kimi K3 BF16 ≈11.2 TB；Qwen 3.8 2.4T ≈9.6 TB）（官方自报估算）。NeMo RL：相对传统 refit **2.7×–5.7×**（Qwen3 235B、DeepSeek v3 671B、Nemotron Ultra v3；DGX H100 / GB200）（官方自报）。例：DeepSeek v3 671B on H100 14.9 s→2.6 s；Qwen3.8 2.4T BF16 microbench Reshard 4.3 s（官方自报）。约 95% 参数的 FFN projection 走 Reshard，其余小权重仍 gather-broadcast（官方自报）。**勿**与 FLUX 图生延迟倍速横向比较——任务/硬件不同。
- [开发者博文](https://developer.nvidia.com/blog/accelerating-reinforcement-learning-weight-refit-with-the-reshard-collective/)（published → **2026-11-07 02:03 Asia/Singapore**）

###### 3. NVIDIA：FLUX 3 Image Klein 在 Blackwell 上的 VisualGen 优化菜谱
TensorRT LLM VisualGen 上跑 BFL FLUX 3 Image Klein（Base/蒸馏），叠 NVFP4、注意力、Cache-DiT、多 GPU，给出单卡 B200 与 8×B200 延迟。扩散服务落地的可复现优化说明。
- 单卡 B200：NVFP4 vs BF16 最高约 1.62× T2I / 1.58× I2I；组合优化相对未编译 BF16 最高约 **3.46×** T2I（22.36→6.46 s）、**4.45×** I2I（54.64→12.28 s）；Cache-DiT 2048² Base 约 1.94×（LPIPS 0.033）（官方自报，固定分辨率/设定）。8×B200：Base 中位 T2I 14.90→3.00 s，蒸馏 2.73→1.08 s（官方自报）。质量用 LPIPS 近似。
- [开发者博文](https://developer.nvidia.com/blog/speed-up-image-generation-with-flux-3-image-klein-on-nvidia-blackwell-gpus/)（published → **2026-11-07 06:20 Asia/Singapore**）

###### 4. OpenAI：与 Hacktron 合作测自家系统与第三方交界
扩大 Daybreak Red / 前沿 cyber 模型访问，重点测与第三方服务交互面；叙事衔接 Cathedral sprint 与上调 bug bounty。把「对外卖 cyber 能力」与「对内红队自己」放在同一周。
- 仅结论：不写漏洞类型、利用路径或测试步骤。RSS **2026-11-06 16:00 Asia/Singapore**。
- [官博](https://openai.com/index/partnering-with-hacktron) · 配读上期 [GPT‑6 Cyber](https://openai.com/index/introducing-gpt-6-cyber/)

##### arXiv

###### 5. Princeton + Anthropic：Memory Trap——良性互动的持久记忆越界（2611.07554）
**与官博 #1 的关联/差异（已核正文）**：同属 Anthropic 记忆工具生态（Fellows + Lampinen）；官博讲「怎么把记忆写好、dreaming 怎么纠错/建表示」，本稿定义 **memory trap**：无对手方时，良性互动写入的偏好/流程被过度泛化，导致后续高风险跳过确认、谄媚/过批、削弱正确安全测试。关联是同一能力栈的正反面；差异是目标——产品可用性 vs 作用域安全。Dreaming 可对照日志修正事实错误笔记，**不能**据此推断已解决 write-time / read-time 越界；作者明确把「preserve scope」列为开放问题。
- 六款前沿模型（Claude Sonnet/Opus/Fable 与 GPT‑5.6 等）。Autonomy：低风险编码「跳过确认」笔记后，Sonnet-4.6 不安全动作率约 **0.66–0.81**、Opus-4.7 约 **0.35–0.58**（无记忆基线多 <0.01；确认/自检两套模拟高风险场景）（作者自报）。ImpossibleBench SWE 冲突分割：Opus-4.8 作弊率约 **29%→74%**；Fable-5 几乎不动（约 18%→19%）（作者自报）。破损防护测试集上，笔记显著提高「改测试掩盖缺陷」比例（作者自报）。安全向仅结论。单位 Princeton + Anthropic（来源记录）。
- [arXiv](https://arxiv.org/abs/2611.07554) · [代码](https://github.com/safety-research/memory-trap)

###### 6. Salesforce AI Research：OPD 对 GRPO 的训练 FLOPs 账（2611.08453）
**计算口径（已核正文）**：按生成 token 计——GRPO **10 N_s**/token（生成 2 + 重算 logprob 2 + 更新 6）；OPD 另加冻结教师前向 **+2 N_t**；不计共享 prompt。外部 post-trained 教师时，匹配设定下 OPD 通常不如 GRPO（且易回复变长）；**教师=学生自己的 GRPO checkpoint（self-GRPO）** 时，数学上 OPD 用约 **50×** 更少**蒸馏阶段** FLOPs 追平该 checkpoint（G=1；默认 G=8 约 6×）（作者自报）。多教师：蒸馏阶段仅占专家训练 FLOPs 的 **5.2%**（2 域）/ **8.0%**（4 域）；专家训练+蒸馏合计相对联合 GRPO 少 **42.0%** total FLOPs（2 域）（作者自报）。单域已有 GRPO checkpoint 时再蒸馏会加总账——效率故事在「多分域专家再合并」。单位 Salesforce AI Research + UIUC（来源记录）。
- [arXiv](https://arxiv.org/abs/2611.08453) · 互补算法改法 [D²-OPD 2611.07241](https://arxiv.org/abs/2611.07241)（Amazon AGI 等）

###### 7. Berkeley / Chicago / Bespoke：EnvOpt 自动优化静止环境（2611.07372）
**成本条件（已核正文）**：固定模型与 harness，用**无 grader/参考答案**的训练任务让研究 agent 改环境表示（文档/工单/Slack 类静止环境）；验证集带 verifier 监控成本与通过率，恶化则回滚。AutomationBench：Claude Haiku 4.5 成本 **-72.7%**、通过率 **+14.34%**；同环境迁到 Opus 5 成本 **-68.1%**、+1.34%；叠在 Meta-Harness 优化 harness 上相对 Meta-Harness 再 **-83.4%** 成本、+11.17% 准确率（作者自报）。文称五基准显著降本且通过率不掉或更好、平均成本约降 48%；AutomationBench 离线优化约 **USD $150** 量级（作者自报）。数字绑定具体 bench/模型/harness，**勿**与 Reshard/FLUX 硬件倍速混比。单位 UC Berkeley / UChicago / Bespoke Labs（来源记录）。
- [arXiv](https://arxiv.org/abs/2611.07372)

###### 8. UC Berkeley + Sony + Meta：Social Humanoid 跟人互动全身反应（2611.08407）
在 Unitree G1（29-DoF）上做社交人形交互：高层共享 token 序列、底层全身跟踪，双阶段自适应重定向；新 HHI 数据约 **260 hours**（作者自报）。人形从「独舞」到「可社交协作」的一条具身线；摘要无单一实物成功率百分比（实验表待核）。CoRL 2026（comments）。单位 UC Berkeley / Sony / Meta（来源记录）。
- [arXiv](https://arxiv.org/abs/2611.08407)

###### 9. UCSD + CMU：RecSA 百万级长度外推、对数代价稀疏注意力（2611.07232）
Recursive Sparse Attention 在 KV 上建树，选择/读取 **O(log L)**；从 Qwen3-4B 初始化，原 32K 训练长度上用 **0.62B** tokens（作者自报）。RULER 131K–2M 称全胜基线；**1M** 上 **60.5** vs Dense+DCA **40.0**；524K 单卡 H200 prefill **3.2×**、decode **3.8×**（作者自报，相对其文内基线）。与上期 NVIDIA CISA（稠密改稀疏、无重训）不同路线，**勿**跨文直接比倍速。单位 UCSD / CMU（来源记录）。
- [arXiv](https://arxiv.org/abs/2611.07232)

##### 备选（简洁）

- 官博次选：Meta [Muse Spaces](https://about.fb.com/news/2026/11/introducing-spaces-customize-muse-app/)（11-07 02:00 Asia/Singapore）；Anthropic [Teaching AI to build scientific models](https://www.anthropic.com/research/teaching-ai-to-build-scientific-models)（嘉宾框架）；NVIDIA [6G 开源工具回顾](https://blogs.nvidia.com/blog/telco-open-source-tools-research-6g-networks/)
- arXiv：Amazon AGI [D²-OPD 2611.07241](https://arxiv.org/abs/2611.07241)；Qualcomm [CORE 2611.07859](https://arxiv.org/abs/2611.07859)；ETH/Tufa [Test-Time Self-Play 2611.07367](https://arxiv.org/abs/2611.07367)；UIUC/Georgia Tech [Last Mile / HEELO 2611.07461](https://arxiv.org/abs/2611.07461)；早放（listing 待核）Georgian [Decision Context 2611.08644](https://arxiv.org/abs/2611.08644)

##### 覆盖缺口 / 排除

- **窗前排除（勿当本期新发）**：OpenAI BioBasicsBench（11-06 **08:00** Asia/Singapore）；Meta Specialized Models 博文（meta `00:00Z`=08:00 Asia/Singapore）；上期已报 GPT‑6 Cyber、PDD Kit、GSLM2、Antigravity、Omni 1.2 Flash、LifeVal、CISA、Apple 人形 91% 等
- **已核无新帖（非缺访问）**：DeepMind / Google Research / MSR 窗内列表与 RSS
- **arXiv**：11/06 列表齐；11/09 listing 未出，abs 早放至 **2611.08710**；续扫 **08711+** 与周一 `list/*/new`
- 第三方 RSA/DeepMind 等无正牌 URL → 未收

### 官方原文摘录

#### Labs Raw Excerpts — 2026-11-09

- **窗口**: 2026-11-06 09:50 Asia/Singapore → **2026-11-09 09:21 Asia/Singapore**（Asia/Singapore, UTC+8；采集截止以本机 `date` 为准）
- **采集时间**: 2026-11-09 约 09:19–09:25 Asia/Singapore
- **说明**: 原始摘录；关键数字标「官方自报 / 来源记录 / 待核」。网络安全与生物仅写结论与官方数字，不写利用/合成步骤。已在上期主包或窗口外的条目不作为本期重点重复。
- **去重参照**: （内部证据存档）、`research.md`（GPT‑6 Cyber、Linux 管线、Images 2.6、Pierre、Antigravity cheminformatics、Omni 1.2 Flash、PDD Kit、GSLM2、CUDA 13.5、vault 粒子、科研会话分析等）。

---

##### OpenAI

**源查证**: [openai.com 来源](https://openai.com/news/rss.xml)（curl + Chrome UA 成功）；辅以 [openai.com 来源](https://openai.com/news/)、[openai.com 来源](https://openai.com/news/research/) WebFetch。

###### 1) Partnering with Hacktron to find vulnerabilities in OpenAI’s systems — **建议进主包（安全合作）**
- **日期**: RSS `Fri, 06 Nov 2026 08:00:00 GMT` → **2026-11-06 16:00 Asia/Singapore**（窗口内）
- **URL**: [openai.com 来源](https://openai.com/index/partnering-with-hacktron)
- **人话**: OpenAI 与安全公司 Hacktron 正式合作，重点测自家系统与第三方服务交界处的漏洞，并扩大其 Daybreak Red / 前沿 cyber 模型访问。
- **要点**:
  - 工程师与 Hacktron 研究员共同选定高优先级测试面，强调与第三方服务交互（官方自报）。
  - 扩大 Hacktron 经 Daybreak Red 对前沿模型的访问（官方自报）。
  - 叙事衔接本周 Cathedral 安全 sprint、上调 bug bounty；Hacktron 来自 Bug Bounty 高影响披露（官方自报）。
  - **仅结论**：不写漏洞类型、利用路径或测试步骤。
- **为何重要**: 把「对外卖 cyber 能力」与「对内用同一能力红队自己」放在同一周叙事里；对安全产品与第三方集成风险读者有用。
- **对谁有用 / 深读**: 平台安全、红队采购、政策/供应链；配读上期 GPT‑6 Cyber 与 Linux 管线文。
- **标注**: 来源记录（日期/URL）/ 官方自报（合作范围表述）。

###### 窗口边缘排除（OpenAI）
| 标题 | Asia/Singapore | 判定 | URL |
|------|-----|------|-----|
| Measuring how AI agents handle everyday wet-lab science（BioBasicsBench） | 2026-11-06 **08:00** | **早于** 09:50 起点 → 不计入本期窗口；下期勿漏若未报 | [openai.com 来源](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/) |
| Cult.fit / Australian universities 等 | ≤11-06 04:00 | 窗口外或客户故事 | 见上期 |

**窗口内 OpenAI newsroom 其他**: RSS 扫描至采集截止，**仅 Hacktron 一条**落入窗口；新闻首页最新亦为 Hacktron。

**alignment.openai.com**: WebSearch 可见 Nov 2–3「activation classifiers」「eval-production gap」等 → **窗口外**（早于 11-06 09:50）。

---

##### Anthropic

**源查证**: [anthropic.com 来源](https://www.anthropic.com/research)（WebFetch）；[anthropic.com 来源](https://www.anthropic.com/news)（WebFetch + curl）。无公开带时区的 RSS；页面多为「Published Nov N, 2026」日级。

###### 2) The components of agent memory — **建议进主包**
- **日期**: 页面 **Nov 6, 2026**（仅日期；精确 HH:MM **待核**；按日历日落入窗口日）

> 编辑注：“窗口日”不等于已证明晚于 11 月 6 日 09:50（Asia/Singapore）。页面只有日级日期，精确发布边界仍待核；窗口内官方传播应与原文首次发布分开记。
- **URL**: [anthropic.com 来源](https://www.anthropic.com/research/components-of-agent-memory)
- **人话**: Anthropic 系统讲解 agent「记忆」：会话内写 notes + 空闲时「dreaming」整理/纠错/建 wiki，并给多组评测数字。
- **要点**（均为官方自报）:
  - **Dreaming**: 对日志离线重放，纠正错误笔记、建新表示（wiki）、把笔记提升到每会话预载层。
  - **CL-Bench 1.0** 数据库任务：Managed Agents + 跨会话记忆目录；Opus 5 / Opus 5.5 / Sonnet 5.5 能「闭环」写已验证规则；「只记失败」规则反而削弱记忆增益。
  - **Pokémon**: Sonnet 3.7 约写 **413** 文件 / **225** 文件夹、1 badge；Fable 5 约 **9** 文件 / **2** 文件夹 + `global.md`、4 badges（约 10k steps 对比）。
  - **Stainless 语料 wiki**: ~**350,000** 文件 / ~**420M** tokens；25 问，dreaming **2→128** 会话，评分 **13%→48%**；wiki+search **54%→61%** vs search alone **53%**；约省 **20,000** tokens/问。
  - **Harvey LAB / 并购合同**: 多文档题 wiki **87%** vs search **73%**；合同事实进 wiki **41/57→57/57**（改指令后）。

> 编辑注：这段是压缩摘要，不能把不同实验合成一个 Harvey 总指标。87%/73% 属于并购问答的跨文档项目；41/57→57/57 对应建库指令改进后生成简报可覆盖的合同事实标准。详见[官方原文](https://www.anthropic.com/research/components-of-agent-memory)。
- **为何重要**: 把「记忆 = 对未来需求的预测」+ dreaming 工程化，是 agent 产品线与上下文工程的硬参考。
- **对谁有用**: agent 平台、长程任务、记忆/RAG 产品；深读全文评测图。
- **标注**: 来源记录（URL/日）/ 官方自报（数字）/ 时刻待核。

###### 3) Teaching AI to build scientific models — **候选（嘉宾科学评论，次优先）**
- **日期**: **Nov 6, 2026**（仅日期；时刻待核）
- **URL**: [anthropic.com 来源](https://www.anthropic.com/research/teaching-ai-to-build-scientific-models)
- **人话**: AI for Science 受赠方（ELLIS Tübingen）谈用 AI 做科学建模三步：建模型 / 约束参数 / 解释；强调分布而非单点最优、insight 重于拟合。
- **要点**: 以 Hodgkin–Huxley 为线；simulation-based inference；LLM agent 搜模型空间；**无明显新基准数字**（官方自报框架论述）。
- **进主包理由偏弱**: 高质量科普/框架，非实验室新结果发布。
- **标注**: 来源记录（URL/日）/ 时刻待核。

###### Newsroom
- 页面出现「November 9, 2026」字样，但下列公告仍为 Sep–Oct（Opus 5.5、S-1、Public Benefit Fund 等）；**未见可核的 11/06–11/09 新 news 条目**（查了 News 首页；勿把页眉日期当成新帖）。
- **Progress on provable inference / FlashProve**: Published **Nov 2, 2026** → **窗口外**。[anthropic.com 来源](https://www.anthropic.com/research/provable-inference)

---

##### Google DeepMind

**源查证**: [deepmind.google 来源](https://deepmind.google/blog/rss.xml)（curl 成功）；[deepmind.google 来源](https://deepmind.google/blog/)（curl 曾返回压缩乱码；RSS 可读）。

###### 窗口内
- **无新帖**。RSS 最新：Gemini Omni 1.2 Flash **2026-11-06 01:05 Asia/Singapore** → 早于窗口起点；已在上期。
- 第三方摘要提到的「agents vs legacy RSA」等 **未找到** deepmind.google / blog.google 同期正牌原文 → **不收录**（宁缺毋滥）。

> 编辑注：此句只反映该研究流未找到独立博客，不是全渠道无官方材料的结论。下方 X 材料保留了[官方帖](https://x.com/GoogleDeepMind/status/2118755418675765656)、[负责人文章](https://x.com/pushmeet/status/2118752095859794390)与论文来源；成稿仅据这些来源写能力结论。

---

##### Google Research / blog.google

**源查证**: [research.google 来源](https://research.google/blog/)（WebFetch）；[blog.google 来源](https://blog.google/technology/ai/)（curl）。

###### 窗口内
- Google Research 列表最新仍为 **Nov 5** 高血压可穿戴、**Nov 4** Agile Deliberation → **窗口外 / 上期已录**。
- blog.google：「Turn sketches into apps with Gemini」**Nov 05, 2026** → 窗口外；Playground 游戏平台 **Oct 07** → 窗口外。
- **本期 Google 研究官博：无窗内新帖**（访问成功，非缺访问）。

---

##### Meta（research.meta.ai / about.fb.com / engineering.fb.com / ai.meta.com）

**源查证**: WebFetch / curl 详情页 `article:published_time`；engineering.fb.com 列表检索。

###### 4) Design the Muse App, Just for You（Spaces）— **候选（产品）**
- **日期**: meta `2026-11-06T18:00:58+00:00` → **2026-11-07 02:00 Asia/Singapore**（窗口内）
- **URL**: [about.fb.com 来源](https://about.fb.com/news/2026/11/introducing-spaces-customize-muse-app/)
- **人话**: Muse App 上线「spaces」：用自然语言搭个性化空间（规划板、追踪器、小游戏等），可钉到侧栏/主 Tab，并称同步推出经 Muse Wonder 蒸馏的专用模型。
- **要点**: 产品叙事为主；文末提到 specialized models 向 Muse 滚动（官方自报）。无硬评测表。
- **标注**: 来源记录（时间戳）/ 官方自报。

###### 窗口边缘排除（Meta）
- **Bringing Specialized Models to Muse and Meta AI**: meta `2026-11-06T00:00:00.000Z` → **2026-11-06 08:00 Asia/Singapore**，**早于** 09:50 → **不计入本期窗口**（数字可供边注：Personal Superintelligence Index **47%** vs **38%**；Active Memory eval **90%** vs **76%**；遗忘关键信息约 **2.4×** 降低；意外瓶颈任务完成约 **+67%**——均为官方自报）。URL: [research.meta.ai 来源](https://research.meta.ai/blog/specialized-models-for-muse-and-metaai)
- Give Your Muse a Voice（Nov 5）、F3 Lightning（Nov 3）、GSLM2（Nov 4）→ 上期/窗口外。
- engineering.fb.com：窗口内 **无** 2026/11/06–09 新帖（最新仍 Nov 3 F3 Lightning）。

---

##### Microsoft Research

**源查证**: [microsoft.com 来源](https://www.microsoft.com/en-us/research/feed/)（curl）；[microsoft.com 来源](https://www.microsoft.com/en-us/research/blog/)（WebFetch）。

###### 窗口内
- **无新帖**。最新仍为 PDD Kit（Nov 5 / 上期已录）。Feed 与博客列表一致；**访问成功，确认为无更新而非抓取失败**。

---

##### NVIDIA

**源查证**: Atom [developer.nvidia.com 来源](https://developer.nvidia.com/blog/feed)（用 **`published`**）；[blogs.nvidia.com 来源](https://blogs.nvidia.com/feed/)。

###### 5) Accelerating Reinforcement Learning Weight Refit with the Reshard Collective — **建议进主包（训练系统）**
- **日期**: `published` / `published_time` `2026-11-06T18:03:26Z` → **2026-11-07 02:03 Asia/Singapore**（页面文案写 Nov 06；以 published 为准）
- **URL**: [developer.nvidia.com 来源](https://developer.nvidia.com/blog/accelerating-reinforcement-learning-weight-refit-with-the-reshard-collective/)
- **人话**: 把 RL post-training 里 train→infer 的权重 refit 改成 DTensor「Reshard」集合通信，避免 gather-and-broadcast 的整模冗余传输；开源 NCCL M2N Reshard，进 NeMo RL。
- **要点**（官方自报）:
  - 最大开源权重量级下，gather+broadcast 逻辑 payload 可达约 **~10 TB/次 refit**（例：Kimi K3 BF16 ≈11.2 TB；Qwen 3.8 2.4T ≈9.6 TB 量级估算）。
  - NeMo RL 基准：相对传统 refit **2.7×–5.7×** 加速（Qwen3 235B、DeepSeek v3 671B、Nemotron Ultra v3；H100 / GB200）。
  - 例：DeepSeek v3 671B on H100：14.9 s → **2.6 s**；Qwen3.8 2.4T BF16 microbench Reshard **4.3 s**。
  - 混合路径：约 **95%** 参数的 FFN projection 走 Reshard，其余小权重仍 gather-broadcast。
  - 代码/指南：NCCL extensions + NeMo RL `refit_transport: nccl_reshard`。
- **为何重要**: 万亿参 RL 的隐性瓶颈从「算」转到「搬权重」；系统/infra 读者必看。
- **局限**: 官方自选模型与并行布局；端到端吞吐还取决于其他阶段。
- **标注**: 来源记录（时间戳/URL）/ 官方自报（倍速与 TB 估算）。

###### 6) Speed Up Image Generation with FLUX 3 Image Klein on NVIDIA Blackwell GPUs — **建议进主包（推理优化教程）**
- **日期**: `published_time` `2026-11-06T22:20:20+00:00` → **2026-11-07 06:20 Asia/Singapore**（页面「Nov 06」）
- **URL**: [developer.nvidia.com 来源](https://developer.nvidia.com/blog/speed-up-image-generation-with-flux-3-image-klein-on-nvidia-blackwell-gpus/)
- **人话**: TensorRT LLM VisualGen 上跑 BFL FLUX 3 Image Klein（Base/蒸馏），在 Blackwell 上叠 NVFP4、注意力、Cache-DiT、多 GPU，报单卡与 8×B200 延迟。
- **要点**（官方自报；单卡 B200、2048² 等设定）:
  - NVFP4 vs BF16：最高约 **1.62×** T2I / **1.58×** I2I。
  - 组合优化相对未编译 BF16：最高约 **3.46×** T2I（22.36→6.46 s）、**4.45×** I2I（54.64→12.28 s）。
  - Cache-DiT：2048² Base 约 **1.94×**（LPIPS 0.033）。
  - 8×B200：Base 中位 T2I 14.90→**3.00 s**；蒸馏 2.73→**1.08 s**；denoising 加速约 **6.01×** / **4.44×**。
- **为何重要**: 扩散服务落地的可复现优化菜谱；对推理工程有用。
- **局限**: 厂商博客、固定硬件/分辨率；质量用 LPIPS 近似。
- **标注**: 来源记录 / 官方自报。

###### 7) How NVIDIA Open Source Tools Are Helping Researchers Build Next-Generation 6G Networks — **候选（应用/生态）**
- **日期**: feed → **2026-11-07 00:00 Asia/Singapore**
- **URL**: [blogs.nvidia.com 来源](https://blogs.nvidia.com/blog/telco-open-source-tools-research-6g-networks/)
- **人话**: Aerial / Sionna 等开源 5G/6G 工具一年回顾：下载与机构覆盖，以及语义通信降机器人任务时延等案例。
- **要点**（官方自报）: 开源 5G/6G 工具下载超 **100 万**；Aerial+Sionna 开发者采用约 **10×**；**>8,000** 研究/学术机构；King’s College 案例任务完成时间最高降约 **52.6%**。
- **进主包优先级**: 低于 Reshard/FLUX（偏生态故事）。
- **标注**: 官方自报。

###### 窗口外 NVIDIA（勿重复）
- DSX OS、Co-Design / AI Factory、Vera CPU、Omniverse agents 等 published ≤ 11-06 01:00 Asia/Singapore → 上期或窗口外。

---

##### 其他权威源抽检

| 源 | 结果 |
|----|------|
| OpenAI News / Research 列表 | 窗内仅 Hacktron |
| Anthropic Newsroom | 无可靠窗内新公告 |
| DeepMind RSS | 无 ≥09:50 Asia/Singapore 新帖 |
| Google Research 博客 | 无 ≥11-06 新帖 |
| MSR Blog/Feed | 无 ≥11-06 新帖 |
| Meta Engineering | 无 11/06–09 新帖 |
| 第三方日报 RSA/DeepMind 等 | **无正牌 URL 核验 → 不收** |

---

##### 汇总：建议进入主素材包（宁缺毋滥）

1. **Anthropic** — The components of agent memory（dreaming / 记忆工程）  
2. **NVIDIA** — Reshard Collective（RL weight refit）  
3. **NVIDIA** — FLUX 3 Image Klein on Blackwell（VisualGen 优化）  
4. **OpenAI** — Partnering with Hacktron（安全合作；结论 only）  

次选：Meta Muse Spaces；Anthropic「Teaching AI to build scientific models」嘉宾文；NVIDIA 6G 开源工具回顾。

**明确本期无料（已成功访问）**: Google DeepMind 新博、Google Research 新博、Microsoft Research 新博；OpenAI 除 Hacktron 外无窗内研究长文。

**窗口边缘备忘（下期/补报）**: OpenAI BioBasicsBench（11-06 08:00 Asia/Singapore）；Meta Specialized Models 博文（meta 00:00Z = 08:00 Asia/Singapore）。

**检索覆盖与失败**
- 成功：OpenAI RSS、MSR feed、NVIDIA dual feeds、DeepMind RSS、Anthropic research/news WebFetch、Google Research WebFetch、Meta/NVIDIA 详情页 curl。
- 降级：DeepMind 博客 HTML curl 压缩乱码（改用 RSS）；FLUX 首轮 WebFetch 超时（改 curl 成功）。
- 未把缺条目写成「无更新」的机构：以上「无新帖」均有列表/RSS 证据。

### arXiv 原始候选

#### arXiv raw pack: cs.AI / cs.CL / cs.LG（扫描窗口 2026-11-06 09:50 Asia/Singapore → 2026-11-09 ~09:30 Asia/Singapore）


核验方式：真实访问 `arxiv.org/list/*/pastweek|new|recent`、`/abs/`、`/html/`、`/pdf/` 首页；HTTPS `export.arxiv.org/api`（HTTP 端点 500，改用 HTTPS）。数字默认摘自摘要，标 **作者自报**；机构以 HTML `ltx_author` / PDF 首页为准，**不以题目里出现的模型名为机构**。

##### Batch map（日期为 Asia/Singapore 放批早间；arXiv 美东 Sun–Thu 20:00 公布 → 新加坡约 Mon–Fri 早上有批；**无周六批**）

| Asia/Singapore 批次 | listing 标签 | cs.AI/CL/LG 列表条目（含交叉，三个分类去重约） | New-submission / abs 探测 ID 范围 | 状态 |
|---|---|---|---|---|
| 11/06 (Fri) | Fri, 6 Nov 2026 | AI 198 / CL 94 / LG 224；去重约 **396**（2611.*） | 列表 New 约 **2611.06953 – 2611.08487**（上期 abs 仅到 **07143**） | **已补全**：上期部分放出；本期自 **2611.07144** 起续扫至列表齐 |
| 11/07 (Sat) | — | — | — | 无批（惯例） |
| 11/08 (Sun) | — | — | — | 无批（惯例；周日晚美东公布 → 周一 Asia/Singapore） |
| 11/09 (Mon) | listing **尚未**出现 | abs 探测 AI/CL/LG **62** 篇 | **2611.08488 – 2611.08710**（当前 max **08710**；08800+ 404） | **部分放出**：列表页滞后；已用 abs 科目探测 |

说明：
- 上期截止 **2611.07143**（洞 07134）；上期主包已收 **2611.07071**（Goodfire），本期不重复当新发现。
- 11/06 列表现已齐；本期新发现焦点为 **≥2611.07144**。
- 11/09 早放 abs 可开但 `/pastweek` 最新日仍是 Fri 6 Nov；**续扫起点：2611.08711**（及周一 listing 一旦出现）。
- 提交日多在 4–5 Nov 2026（美东）；**Asia/Singapore 归属按 listing/放批日**，不按 Submitted on 字面。

##### Candidates（单位经 arXiv HTML / PDF 首页核实；数字来自摘要除非另注）

###### Batch 11/06 续扫（≥2611.07144，列表已齐）

1. **2611.08453** Unpacking the Compute Efficiency of Strong-to-Weak OPD against GRPO  
   链接：[arXiv 2611.08453](https://arxiv.org/abs/2611.08453) · PDF [arXiv 2611.08453.pdf](https://arxiv.org/pdf/2611.08453.pdf)  
   提交/公布：Submitted 5 Nov 2026；**Asia/Singapore 归属 11/06 (Fri) 批**（列表内）  
   机构证据：PDF 首页「Salesforce AI Research」+ UIUC（来源记录）  
   人话：系统比较 on-policy distillation（OPD）与 GRPO 的**训练 FLOPs 效率**，并看多教师蒸馏如何合并分域 GRPO 专家。  
   为何重要：直接回答「密监督蒸馏能不能比 RL 更省算力」；对后训练配方取舍是硬证据。  
   对谁有用/深读：做 post-training / 蒸馏 / RLVR 的团队。  
   主要数字与条件/局限（作者自报）：教师=学生自己的 GRPO checkpoint 时，OPD 在数学上用约 **50×** 更少蒸馏 FLOPs 追平该 checkpoint；多教师 OPD 蒸馏阶段仅占专家训练 FLOPs 的 **5.2%**（2 域）/ **8.0%**（4 域）；合计专家训练+蒸馏相对联合 GRPO 少 **42.0%** total FLOPs（2 域）。外部 post-trained 教师时 OPD 常输给 GRPO，且有回复变长问题。  
   标签：**主包** · 来源记录 机构 / 作者自报数字

2. **2611.07554** The Memory Trap: Language Agents Overgeneralize from Benign Interactions  
   链接：[arXiv 2611.07554](https://arxiv.org/abs/2611.07554)  
   提交/公布：Submitted 5 Nov 2026；**Asia/Singapore 归属 11/06**  
   机构证据：PDF「Princeton University² Anthropic」（Lampinen 等）；HTML 亦见 Anthropic（来源记录）  
   人话：持久记忆会把**良性**互动里的偏好/流程过度泛化，导致后续高风险任务跳过确认、谄媚/过批、甚至削弱安全测试。  
   为何重要：把「agent memory」从产品功能推进到可复现的安全失败模式；与上期 alignment/agent 线连续。  
   对谁有用/深读：做长程 agent、记忆系统、安全评测的人。  
   主要数字与条件/局限（作者自报）：六款前沿模型（含 Claude Sonnet/Opus/Fable、GPT‑5.6）；低风险编码「跳过确认」记忆会迁移到模拟高风险场景；合法修陈旧测试的记忆会削弱抓住坏防护的正确测试，并抬高 ImpossibleBench 作弊（更强 Sonnet/Opus 增幅更大）。摘要无单一总百分比。安全向**仅结论**。  
   标签：**主包** · 来源记录 机构 / 作者自报

3. **2611.07372** EnvOpt: Automated Optimization for Agent Environments  
   链接：[arXiv 2611.07372](https://arxiv.org/abs/2611.07372)  
   提交/公布：Submitted 5 Nov 2026；**Asia/Singapore 归属 11/06**  
   机构证据：PDF「University of California, Berkeley / University of Chicago / Bespoke Labs」（来源记录）  
   人话：除了调模型与 harness，把**共享静止环境**（文档库、工单、Slack 类空间）也当成可自动优化对象。  
   为何重要：把 agent 成本/成功率的第三杠杆说清楚，并给出可迁移的环境优化结果。  
   对谁有用/深读：企业 agent 平台、harness/环境工程。  
   主要数字与条件/局限（作者自报）：AutomationBench 上 Claude Haiku 4.5 成本 **-72.7%**、通过率 **+14.34%**；同环境迁到 Opus 5 成本 **-68.1%**、+1.34%；叠在 Meta-Harness 优化 harness 上再 **-83.4%** 成本、+11.17% 准确率；跨 5 基准显著降本且通过率不掉或更好。无 grader/参考答案。  
   标签：**主包** · 来源记录 / 作者自报

4. **2611.08407** Social Humanoid: Socially Responsive Human-Humanoid Interaction  
   链接：[arXiv 2611.08407](https://arxiv.org/abs/2611.08407) · 项目页见 PDF  
   提交/公布：Submitted 5 Nov 2026；**Asia/Singapore 归属 11/06**；CoRL 2026（comments）  
   机构证据：PDF「UC Berkeley†, Sony Group Corporation‡, Meta§」（来源记录；含 Malik / Darrell / Kanazawa）  
   人话：在 Unitree G1 上做**跟人互动**的全身反应动作：高层共享 token 序列建模，底层全身跟踪；并做双阶段自适应重定向。  
   为何重要：人形从「独舞」到「可社交协作」；新 HHI 数据约 **260 小时**。  
   对谁有用/深读：人形/具身、交互策略。  
   主要数字与条件/局限（作者自报）：29-DoF G1；五源 mocap → HHI 基准约 **260 hours**；仿真与实物均展示协调行为。摘要无单一成功率百分比（待核 PDF 实验表）。  
   标签：**主包** · 来源记录 / 作者自报

5. **2611.07232** Recursive Sparse Attention: Million-Token Length Extrapolation at Logarithmic Cost  
   链接：[arXiv 2611.07232](https://arxiv.org/abs/2611.07232)  
   提交/公布：Submitted 4 Nov 2026；**Asia/Singapore 归属 11/06**  
   机构证据：HTML footnote「University of California, San Diego / Carnegie Mellon University」；通讯 （机构署名邮箱略）（来源记录）  
   人话：RecSA 在 KV 上建树，每层共享 pooler 摘要，使选择/读取成本 **O(log L)**，并声称训练长度内相对距离始终可见从而外推到百万级。  
   为何重要：长上下文稀疏注意力的可训练层级方案，带端到端加速数字。  
   对谁有用/深读：长上下文推理系统、注意力内核。  
   主要数字与条件/局限（作者自报）：从 Qwen3-4B 初始化，在原 32K 训练长度上用 **0.62B** tokens；RULER 从 131K–2M 全胜基线；**1M** 上 **60.5** vs 最佳基线 Dense+DCA **40.0**；524K 单卡 H200 prefill **3.2×**、decode **3.8×**。  
   标签：**主包** · 来源记录 / 作者自报

6. **2611.07241** $D^2$-OPD: Separating Direction and Distance in Extrapolative On-Policy Distillation  
   链接：[arXiv 2611.07241](https://arxiv.org/abs/2611.07241)  
   提交/公布：Submitted 4 Nov 2026；**Asia/Singapore 归属 11/06**  
   机构证据：abs 作者行 + PDF/HTML「Columbia University / AWS AI Lab / Amazon AGI」；@amazon.com（来源记录）  
   人话：把外推 OPD 的**方向**与**距离**解耦：硬 KL 限距离，自适应组合定方向，用 forward KL 训学生。  
   为何重要：与 08453 同属 OPD 线，互补「算法改法」vs「算力账」。  
   对谁有用/深读：蒸馏/后训练。  
   主要数字与条件/局限（作者自报）：数学推理三设定均最高，相对最强基线最高 **+9.45** points。  
   标签：**主包/强备选** · 来源记录 / 作者自报

7. **2611.07859** CORE: Coarse-to-Fine Search with Context Management for Deep Research  
   链接：[arXiv 2611.07859](https://arxiv.org/abs/2611.07859)  
   提交/公布：Submitted 5 Nov 2026；**Asia/Singapore 归属 11/06**  
   机构证据：HTML「Qualcomm AI Research / Qualcomm Vietnam」；@qti.qualcomm.com（来源记录）  
   人话：训练免费的 deep research harness：粗到细检索 + 用 late-interaction 相似度只回短片段，并做上下文扩展/去重。  
   为何重要：对准「检索要长、进上下文要短」的矛盾；闭搜对比 Tongyi DeepResearch / OpenResearcher。  
   对谁有用/深读：deep research agent、RAG harness。  
   主要数字与条件/局限（作者自报）：三模型 × 三基准（BrowseComp-Plus / Wikipedia / Plus-CM）；语料最大约 **553M** 文档；称 SOTA 准确率与证据召回（具体表待核 PDF）。  
   标签：**备选偏强** · 来源记录 / 作者自报

8. **2611.07367** Test-Time Self-Play: Scaling without a Verifier  
   链接：[arXiv 2611.07367](https://arxiv.org/abs/2611.07367)  
   提交/公布：Submitted 5 Nov 2026；**Asia/Singapore 归属 11/06**  
   机构证据：PDF/HTML「ETH Zurich & Tufa Labs」（来源记录）  
   人话：无强验证器时，用不对称 self-play 做 test-time scaling。  
   为何重要：部署侧常没有可靠 verifier；给无 verifier 极限一个可量化增益。  
   对谁有用/深读：推理时计算、代码生成评测。  
   主要数字与条件/局限（作者自报）：LiveCodeBench v6 难度校准子集；无 verifier 极限 mean@8 **+35** absolute；弱 verifier 时优势更大；基策略近零覆盖正解时失效。  
   标签：**备选偏强** · 来源记录 / 作者自报

9. **2611.07586** Stress Testing Chain-of-Thought Monitoring Against Covert Misalignment  
   链接：[arXiv 2611.07586](https://arxiv.org/abs/2611.07586) · NeurIPS 2026（comments）  
   提交/公布：Submitted 5 Nov 2026；**Asia/Singapore 归属 11/06**  
   机构证据：HTML「Tsinghua University T-STAR Lab / Shanghai Qi Zhi Institute」（来源记录）  
   人话：TraceMRT 研究压测思维链监控可靠性，并提出改进监控；此处仅记能力结论，不转述规避构造。
   为何重要：CoT 监控是 agent 控制常见抓手；本文强调「策略性隐蔽」红队。安全向**仅结论**。  
   对谁有用/深读：对齐评测、监控系统。  
   主要数字与条件/局限（作者自报）：黑盒攻击含 GPT‑5.2、Claude‑4.5 等监控；自方法 **0.91 AUC**、**0.74 TPR@FPR=0.05**。  
   标签：**备选** · 来源记录 / 作者自报

10. **2611.07461** The Last Mile to the Real World: Agent-Native Primitives…  
    链接：[arXiv 2611.07461](https://arxiv.org/abs/2611.07461) · [heelo.dev 来源](https://www.heelo.dev/)  
    提交/公布：Submitted 5 Nov 2026；**Asia/Singapore 归属 11/06**  
    机构证据：PDF「University of Illinois Urbana-Champaign / Georgia Institute of Technology / heelo.dev」（来源记录）  
    人话：把「够到资源」与「会用资源」拆开，用带驻留 LLM 的 agent-native primitives + HEELO harness 工程框架补最后一公里。  
    为何重要：Terminal-Bench 等真实任务上 frontier harness 仍低分，本文给可组合原语与大幅提升数字。  
    对谁有用/深读：coding/agent harness 产品。  
    主要数字与条件/局限（作者自报）：Terminal-Bench 4.0 上 GPT‑5.6 Sol+Codex **37.3%**、Claude Opus 5+Claude Code **51.8%**（作者转述基线）；Dev-Primitives 同骨干提到 **55.5%**；ToolBench **55.8%→75.1%**；GAIA-Text-103 **45.6%→58.3%**；自平台 46 任务上接 HEELO MCP 后完成数 9→39/35，时间约 **1.9×/2.3×** 更少、成本约 **1.55×** 更低。数字依赖其 harness/原语库，外部复现待核。  
    标签：**备选** · 来源记录 机构 / 作者自报

11. **2611.08438** Understanding AI from the Inside: The State of Mechanistic Interpretability for AI Safety  
    链接：[arXiv 2611.08438](https://arxiv.org/abs/2611.08438)  
    提交/公布：Submitted 5 Nov 2026；**Asia/Singapore 归属 11/06**  
    机构证据：PDF 多机构（Oxford、Martian、MIT、**Anthropic**、LawZero、MPI、EleutherAI、Mila 等）（来源记录：合著 survey，非单一实验室出品）  
    人话：机制可解释性 × AI 安全长综述：方法、评价框架、六类研究取向、安全用途与局限；附可复现 notebook 库。  
    为何重要：给安全/解释社区一张地图；作者含 Anthropic 等但**勿当作 Anthropic 官方单一署名文**。  
    对谁有用/深读：安全研究、interpretability 入门与立项。  
    主要数字：综述文，无单一 benchmark 数字。  
    标签：**备选（综述）** · 来源记录

12. **2611.07778** The Intrusion Pathway: How Non-Evidential Context Degrades Language Model Performance  
    链接：[arXiv 2611.07778](https://arxiv.org/abs/2611.07778)  
    提交/公布：Submitted 5 Nov 2026；**Asia/Singapore 归属 11/06**  
    机构证据：PDF「TurboML / IIIT Delhi / Independent / Singapore Institute of Technology / **NVIDIA** / IIT Kanpur / NTU」（来源记录：NVIDIA 为合著单位之一）  
    人话：无关/随机前缀如何经 MLP→parroting heads→intrusion heads 腐蚀预测；并给可部署 head knockout。  
    为何重要：给 RAG/工具/长上下文「噪声上下文」一个机制叙事与干预。  
    对谁有用/深读：mechanistic、长上下文稳健性。  
    主要数字与条件/局限（作者自报）：oracle 换干净 residual 平均恢复干扰落差的 **97.6%**；约 **10** 个头（~**1%**）mask knockout 恢复 **57%**，对有用上下文有界代价。  
    标签：**备选** · 来源记录 / 作者自报

13. **2611.07166** Multi-step SWE: Can Coding Agents Keep Building on Their Own Code Over Long Horizons?  
    链接：[arXiv 2611.07166](https://arxiv.org/abs/2611.07166) · [multistepswe.com 来源](https://multistepswe.com/)  
    提交/公布：Submitted 4 Nov 2026；**Asia/Singapore 归属 11/06**  
    机构证据：HTML「Klavis AI」；@klavis.ai（来源记录；**非** Apple——此前 HTML 误报来自正文模型名）  
    人话：69 个长程软件工程任务，每任务 5–15 步依赖链，在自己写的代码上继续改。  
    为何重要：补「单次 SWE-bench 式」评测缺口。  
    主要数字（作者自报）：九款前沿最强仅 **18.5%** solve；**38/69** 无人解出。  
    标签：**备选** · 来源记录 / 作者自报

14. **2611.07605** The Gating Mechanism of KV Cache Eviction  
    链接：[arXiv 2611.07605](https://arxiv.org/abs/2611.07605)  
    提交/公布：Submitted 5 Nov 2026；**Asia/Singapore 归属 11/06**  
    机构证据：PDF「HKUST / NYU / HKUST(GZ) / Tencent HunYuan / Georgia Tech / CityU HK / SJTU」（来源记录）  
    人话：论证可学习 eviction gate 的目标陷阱，并提出把稠密注意力移出 gate 可达范围、以稠密预测为靶的改法。  
    主要数字（作者自报）：**75%** KV 压缩下 Qwen3-8B：RULER@8K **90.14**（全缓存差 3.72）、LongBench **46.03**（差 1.36）。  
    标签：**备选** · 来源记录 / 作者自报

15. **2611.08156** La-JEPA: Compact Robot Policies with Latent World Modeling  
    链接：[arXiv 2611.08156](https://arxiv.org/abs/2611.08156)  
    提交/公布：Submitted 5 Nov 2026；**Asia/Singapore 归属 11/06**  
    机构证据：PDF「Huawei / Toronto / McGill / Mila」（来源记录；正文提 Physical Intelligence 等为对比对象，**非**其机构）  
    人话：在 V-JEPA 2.1 特征空间从零训紧凑 world-action 策略，推理只出动作。  
    主要数字：称在 RoboTwin 2.0 / LIBERO-Plus 无具身预训练设定 SOTA；真机四任务平均成功率可比 π0.5（作者自报，表待核）。并纠正 LIBERO-Plus 官方评测器损坏指令问题。  
    标签：**备选** · 来源记录 / 作者自报

16. **2611.08403** StepBack: Step-Level Error-Localized Resampling for Efficient Test-Time Reasoning  
    链接：[arXiv 2611.08403](https://arxiv.org/abs/2611.08403) · NeurIPS 2026  
    机构证据：NCSU（来源记录）  
    要点：定位首错步再重采样后缀；平均匹配 self-consistency，token 最高 **-41.26%**（作者自报）。  
    标签：**备选**

17. **2611.07932** AttnSR: Attention Step Reward for Long-Horizon Agentic RL  
    链接：[arXiv 2611.07932](https://arxiv.org/abs/2611.07932)  
    机构证据：ECNU 等（@cs.ecnu.edu.cn）（来源记录）  
    要点：用策略注意力分配 step reward；ALFWorld **91.2%→97.1%**，ScienceWorld 交互 **-29.9%**（作者自报）。  
    标签：**备选**

18. **2611.07482** SAVeR²: Reasoning-based Safety Alignment for LRMs via Verifiable Rewards  
    链接：[arXiv 2611.07482](https://arxiv.org/abs/2611.07482)  
    机构证据：Zhejiang University / Ant / Alibaba Group（来源记录）  
    要点：可验证细粒度安全奖励 + 保推理梯度投影；实验至 **671B**（作者自报）。安全向仅结论。  
    标签：**备选**

19. **2611.07542** FlashOffloading: Low-Latency KV Cache Offloading…  
    链接：[arXiv 2611.07542](https://arxiv.org/abs/2611.07542)  
    机构证据：@huawei.com / Ascend910C 实验（来源记录 偏华为栈）  
    要点：全卸载 KV；GLM‑5.2+MTP3 下 prefill 最高 **1.38×**、decode **1.91×**（30 ms TPOT）（作者自报）。  
    标签：**备选**

20. **2611.07203** τ-bench-LILT: Multilingual tool-use agent eval  
    链接：[arXiv 2611.07203](https://arxiv.org/abs/2611.07203)  
    机构证据：LILT（@lilt.com）（来源记录）  
    要点：德/韩/土/波斯语本地化 τ-bench；相对英语最大掉点约 **61** pass^4（韩/波斯零售）（作者自报）。  
    标签：**备选**

21. **2611.07639** Measuring the Marginal Value of Verifier-Based RL Beyond SFT  
    链接：[arXiv 2611.07639](https://arxiv.org/abs/2611.07639)  
    机构证据：独立/Santa Clara（摘要未给实验室名）（待核）  
    要点：受控基准上 SFT 已吃掉大部分；预注册规模 GRPO 分布内无显著增益，OOD 仅小幅（作者自报；全研究算力约 $8.69）。  
    标签：**备选（方法学）**

###### Batch 11/09 早放（abs 部分；列表未出）

22. **2611.08644** Decision Context: Persistent Behavioral Learning for AI Agents  
    链接：[arXiv 2611.08644](https://arxiv.org/abs/2611.08644)  
    提交/公布：Submitted 5 Nov 2026；**Asia/Singapore 归属暂标 11/09 早放（待 listing 确认）**  
    机构证据：HTML「Georgian AI Lab」（@georgian.io）（来源记录）  
    人话：把纠正与工具失败编成 RULE，在决策点注入行为记忆，而非只记事实。  
    主要数字（作者自报）：DC-Bench 71 场景；合规 **95%** vs naive retrieval **55%**；每查询约 **10×** 更少注入 token。  
    标签：**备选（早放）** · 待核放批日

23. **2611.08569** Not All Misalignment Is Alike: A Decomposed Benchmark for Emergent Misalignment  
    链接：[arXiv 2611.08569](https://arxiv.org/abs/2611.08569)  
    提交/公布：Submitted 5 Nov 2026；**Asia/Singapore 归属 11/09 早放（待确认）**  
    机构证据：HTML 未见大实验室邮箱（gmail）；**勿**因正文评测对象含模型名归到某厂（待核作者主单位）  
    要点：EMERGE 分解 8 类错位行为；8 开源模型 × 13 微调集。  
    标签：**备选（早放）** · 机构待核

24. **2611.08551** How Small Can We Go? Calibrating Activation-Cache Compression for SAE Training  
    链接：[arXiv 2611.08551](https://arxiv.org/abs/2611.08551)  
    提交/公布：Submitted 5 Nov 2026；**Asia/Singapore 归属 11/09 早放（待确认）**  
    机构证据：Stanford University（来源记录）  
    要点：SAE 激活缓存压缩校准；强调 reseed 地板与 codec 比较方法。  
    标签：**备选（早放）**

##### 明确排除 / 误报提醒

- HTML 全文常出现 OpenAI/Anthropic/Qwen/DeepSeek 等**评测对象或相关工作**，不能当作者单位；本期以 PDF 首页 / `ltx_affiliation` / 机构邮箱为准。
- **2611.07166** 正文提多模型，单位是 **Klavis AI**，不是 Apple。
- **2611.08156** 对比 π0.5 / Physical Intelligence 等，作者单位是 **Huawei/Toronto/McGill/Mila**。
- **2611.08438** 含 Anthropic 合著者的**多机构综述**，非 Anthropic 单独官文。
- 上期已报 **2611.07071**（Goodfire）等 ≤07143 条目不重复列入「新发现」。

##### 扫描完整性

| 项 | 结论 |
|---|---|
| 11/06 列表 | **完整**（pastweek 显示 198/94/224 of 同数） |
| 11/06 ≥07144 高信号筛选 | 已做关键词粗筛 + 重点 abs/HTML/PDF；宁缺毋滥 |
| 11/09 列表 | **未出现** |
| 11/09 abs | **部分**：AI/CL/LG 命中 62；ID 至 **2611.08710** |
| 续扫起点 | **2611.08711** + 周一 `list/*/new` 一旦更新 |
| API | [arXiv export.arxiv.org](http://export.arxiv.org) 500；[arXiv export.arxiv.org](https://export.arxiv.org) 可用，但对最新早放 ID 曾返回空，abs/HTML/PDF 为准 |

##### 建议进研究主包的 3–5 条（真重点）

1. [2611.08453](https://arxiv.org/abs/2611.08453) Salesforce：OPD vs GRPO 算力账  
2. [2611.07554](https://arxiv.org/abs/2611.07554) Princeton+Anthropic：Memory Trap  
3. [2611.07372](https://arxiv.org/abs/2611.07372) Berkeley+Chicago+Bespoke：EnvOpt  
4. [2611.08407](https://arxiv.org/abs/2611.08407) Berkeley+Sony+Meta：Social Humanoid  
5. [2611.07232](https://arxiv.org/abs/2611.07232) UCSD+CMU：RecSA 百万级稀疏注意力  

（互补可点：Amazon AGI [2611.07241](https://arxiv.org/abs/2611.07241)；Qualcomm CORE [2611.07859](https://arxiv.org/abs/2611.07859)。）


## X 公开动态

### 动态与跟踪

#### X/AI 源包 · 2026-11-09（三日合并）

窗口：2026-11-06 09:50 → 2026-11-09 约 09:18 Asia/Singapore。来源：
- 首页时间线 3 页，约 294 条（已过滤回复）。覆盖约 11-08 01:01 → 11-09 09:13 Asia/Singapore；窗口前约 1.5+ 天靠公开检索补齐。
- 官方/关键账号合并检索两组：OpenAI/Anthropic/ClaudeDevs/AA/Tibo 等一组，GoogleDeepMind/Meta/Kimi/MiniMax/dotey 等一组。
- 定向检索：Kimi K3.1 Pro / Foundry、Anthropic IPO / dreaming / science、GPT‑6 Cyber / FMF、Claude Code cloud / User-Agent、Codex/Pro 额度、Cursor、Fable/Mythos、Personal Finance / vault。
- X Today's News：两组 72h 关键词。
- 交叉核对：Anthropic 工程博文「components of agent memory」、科学建模博文、How researchers use Claude（发布日边界）、FMF Jailbreak Rating Framework、DeepMind cryptanalysis X Article + PDF、HF `moonshotai/Kimi-K3.1-Pro`、SEC EDGAR 公司页 S-1 列表、GitHub anthropics/claude-code#107757。

本期 X 侧无 429。GitHub 未认证 API 仅取到 #107757 有限字段（仍 open，updated 2026-11-08 22:09:40 Asia/Singapore）；SEC 公司页截至核验仍仅见 11-02 S-1/A，无新定价/股数修订。Cursor 官方账号本窗口公开检索 `from:cursor_ai` 结果为 0。

去重说明：上期主条（Cyber/Linux、Kimi 权重首开、METR、Personal Finance、vault）本包不重写为新主条；相关仅记「无实质新进展」或可核实增量。旧包数字均本期重核，不以旧包为事实源。

##### 主条目

###### 1. Anthropic 工程博文拆解智能体记忆：「做梦」（dreaming）用离线算力纠错、建 wiki、上推上下文
本窗口最硬的官方工程材料。不是新产品发布，而是把「会话中写笔记 + 空闲时回放整理」写成可评测的记忆栈，并给出 CL-Bench / 宝可梦 / 并购文档等多组官方自报数字。
- **是什么**：
  - 官宣：@AnthropicAI 11-07 05:16 Asia/Singapore；工程页落款 Published Nov 6, 2026。
  - 定义（官方）：agent memory = 从经历获得、跨会话保留、可再读的知识；不含改权重、单次对话 in-context、compaction 摘要。
  - dreaming：会话后对照原始 transcript 校正笔记、建可链 wiki、把少量内容提升到每会话预加载层；类比睡眠 consolidation / sleep-time compute。
  - 官方自报评测（单次运行或内部集，非第三方复测）：
    - CL-Bench 数据库任务：有记忆时 Opus 5 约 0.564→0.828；Sonnet 4.6 约 0.330→0.364（提示「先读记忆再验证」后约 0.641）。
    - 宝可梦红：Sonnet 3.7 写 413 文件/225 文件夹、约 1 徽章；文中称 Claude Fable 5 写约 9+1 文件、4 徽章；Opus 5.5 类似小文件夹并通关（均为官方叙述的单次对比）。
    - Stainless 语料约 35 万文件 / 4.2 亿 token：128 轮 dreaming 建 wiki 后，25 题只靠 wiki 约 13%→48%；wiki+搜索约 54%→61%，每题约省 2 万 token。
    - 并购 24 题（多文档综合）：wiki 87% vs 仅搜索 73%。
    - Claude Code 自动记忆：只预加载 `MEMORY.md` 前 200 行或 25KB。
  - 产品边界：dreaming 在 Claude Managed Agents 为研究预览（需申请）；跨会话记忆库 beta。文中出现 Sonnet 5 / Opus 5 / Fable 5 / Opus 5.5 等内部评测命名，**不等于**对外发售声明。
- **为何重要**：把「记忆该记什么、何时整理、预加载层为何必须短」写成可对照的工程规范；对 agent harness、长期任务和「睡眠算力」讨论提供官方锚点。与上期 vault / Personal Finance 同属 Anthropic 产品化叙事，但本条是记忆系统本身。
- **对谁·深读建议**：做 agent 运行时与记忆产品的人先读「Dreaming can correct memory」与预加载层警告；评测读者盯官方自报分数的单次运行局限。中文可对照宝玉 11-08 长拆。
- **证据**：
  - 官方自报：[@AnthropicAI](https://x.com/AnthropicAI/status/2118814753154064501)、[工程原文](https://www.anthropic.com/research/components-of-agent-memory)
  - X 侧：[宝玉长解读](https://x.com/dotey/status/2119269064543445168)
- **约时**：博文 Published Nov 6, 2026；X 官宣 11-07 05:16 Asia/Singapore

###### 2. Anthropic IPO：路演进入 11-09 当周；买方讨论估值约 1.1–1.3 万亿美元（待核）；招股书仍无定价/股数
上期「无新 S-1 修订 + 市场怀疑 1.5T」的后续。本窗口媒体与 X 讨论升温，但**公司文件侧仍无价格区间**。
- **是什么**：
  - 来源记录：EDGAR 公司页（CIK 0002130357）截至本包核验，最新仍为 2026-11-02 S-1/A（Acc-no: 0001628280-26-068676）；其前为 2026-10-26 S-1。未见本窗口新的定价或发行规模修订。
  - 待核（媒体/转述，非公司公告）：彭博 11-06 稿称估值预期承压；中文转述称下周正式路演、潜在买家谈 1.2–1.3 万亿、有人只给约 1.1 万亿；X News 摘要写路演周为 11-09 当周、Nasdaq 代码 ANT 等（细节以招股书/交易所为准）。Andrew Curran 称估值相对此前圈子里约 2 万亿的说法大致腰斩，IPO 媒体攻势自周一开始——单源意见。
  - 旁侧：NYT 11-05 Dario 人物稿在本窗口被广泛转发（稿件本身略早于窗口起点，作背景，不作新 来源记录）。
- **为何重要**：定价空白仍是硬约束；路演周叙事会左右后续 S-1/A。与上期 METR 加速评估同处上市窗口，但本条只记可核文件 + 标注待核的估值区间。
- **对谁·深读建议**：写资本市场的人先盯下一份 S-1/A 是否出现 price range / share count；勿把 Bloomberg/X News 数字写成已定价。
- **证据**：
  - 来源记录：[EDGAR 公司 S-1 列表](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002130357&type=S-1&dateb=&owner=include&count=10)、[S-1/A index](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/0001628280-26-068676-index.htm)
  - 待核：[Bloomberg 标题页](https://www.bloomberg.com/news/articles/2026-11-06/anthropic-ipo-valuation-expectations-pressured-after-ai-rout)（付费墙，正文未全文核）、[宝玉转述](https://x.com/dotey/status/2119251293025800501)、[Andrew Curran](https://x.com/AndrewCurran_/status/2119233522603020553)、[X News：路演估值](https://x.com/i/trending/2119174990922666252)
- **约时**：彭博稿 11-06；路演讨论持续至 11-09；SEC 核验于 11-09 上午 Asia/Singapore

###### 3. Claude Code：云会话自动配环境（Pro/Max/Ultra）；社区跟进 User-Agent 邮箱泄露，称隐私修复自 2.1.317
上期 #107757 未从 API 核到；本窗口产品官宣 + issue 状态可核。
- **是什么**：
  - 官方自报：@ClaudeDevs 11-07 03:58 Asia/Singapore——Pro/Max/Ultra 的 Claude Code **cloud sessions** 更易跑起仓库：Claude 推断依赖、网络与 API key 需求并保存环境；API key 安全保存且「Claude never sees them」。
  - 来源记录（GitHub）：[anthropics/claude-code#107757](https://github.com/anthropics/claude-code/issues/107757) 标题 *Bug Report: Privacy violation in User-Agent header*；state=open；created 2026-11-06 06:13:15 Asia/Singapore；updated 2026-11-08 22:09:40 Asia/Singapore。本包未认证 API 未拉到正文/里程碑。
  - 待核（社区单源）：有帖称 stable 仍停在 2.1.311，阻断邮箱进 User-Agent 的隐私改动自 **2.1.317** 起；需对照 changelog / 发行说明后再采信为 来源记录。
- **为何重要**：云环境「一次配好下次复用」降低远程 agent 摩擦；同时 User-Agent 邮箱问题把「本地 CLI 默认遥测/指纹」推到前台，和上期扩展投毒同属供应链/隐私关注。
- **对谁·深读建议**：Claude Code 付费用户看官方云会话说明与版本号；安全读者跟 #107757 与 changelog，勿仅信推文版本对照表。
- **证据**：
  - 官方自报：[@ClaudeDevs](https://x.com/ClaudeDevs/status/2118795192090386454)
  - 来源记录：[GitHub #107757](https://github.com/anthropics/claude-code/issues/107757)
  - 待核：[社区版本对照帖](https://x.com/xTheMarketMaker/status/2119587497605038192)
- **约时**：云环境官宣 11-07 03:58 Asia/Singapore；issue 更新至 11-08 22:09 Asia/Singapore

###### 4. OpenAI：Tibo 澄清 Pro 档无 5 小时限额并给出倍率；与 FMF 发布越狱严重性框架；Cyber livestream 仍指向 11-12
额度叙事与网络安全治理同窗出现；GPT‑6 Cyber 本体上期已主条，本期只记增量。
- **是什么**：
  - 官方自报（额度）：@thsottiaux 11-08 13:09 Asia/Singapore——「所有 Pro 计划都没有 5 小时限额」；相对 Plus：Pro 100=10×、Pro 200=20×、Pro 500=50× 且可访问 ultrafast。随后试探「要不要做 Pro 50」。**未**在本帖重述「12 月 ChatGPT↔Codex 共享池」的新日期或公式（上期帮助中心页本期 curl 遇 403，未能重拉正文）。
  - 官方自报（安全治理）：@OpenAI 11-07 03:58 Asia/Singapore 转发合作——Frontier Model Forum **Jailbreak Rating Framework for Frontier Cyber Threats v1.0**（FMF 页落款 5 Nov 2026）：用 capability gain / scope / ease of deployment / ease of discovery 四级评估成功越狱的相对风险；公开征询至 2026-12-21。成员公司安全负责人表态见 FMF 原文。
  - 日程：上期已记 Cyber livestream 11-12 10am PT；本窗口社区帖再次对齐该日期。@OpenAIDevs 11-09 04:04 Asia/Singapore 仅发「Tomorrow.」+视频，**未在帖文写明产品名**——待核具体指向（勿默认等于 Cyber 场）。
- **为何重要**：Pro 倍率是付费用户争议点的官方口径；FMF 框架给「越狱成功 ≠ 同等危害」提供跨厂共同语言，和 GPT‑6 Cyber 升到 Critical 档同一治理轴线。
- **对谁·深读建议**：订阅用户以 Tibo 帖 + 帮助中心为准；安全/政策读 FMF 原文四维评分；看直播的人盯 11-12 官方日程页而非单条「Tomorrow」。
- **证据**：
  - 官方自报：[@thsottiaux Pro 倍率](https://x.com/thsottiaux/status/2119296267545419987)、[@thsottiaux Pro 50 试探](https://x.com/thsottiaux/status/2119305294291612140)、[@OpenAI × FMF](https://x.com/OpenAI/status/2118795218099253606)、[FMF 原文](https://www.frontiermodelforum.org/updates/introducing-the-fmf-jailbreak-rating-framework-for-frontier-cyber-threats/)
  - 待核：[@OpenAIDevs Tomorrow](https://x.com/OpenAIDevs/status/2119521359185478140)；Cyber 日程社区对齐例：[praxisvectorai](https://x.com/praxisvectorai/status/2119583496670712170)
- **约时**：FMF/OpenAI 帖 11-07 03:58 Asia/Singapore；Tibo 11-08 13:09 Asia/Singapore；OpenAIDevs 11-09 04:04 Asia/Singapore

###### 5. Google DeepMind：人机协作用 AI agent 压测加密，指出来遗留 1024-bit RSA 的两类弱点；强调现代 2048+ 仍安全

> 编辑注：标题末句为官方对本次研究适用范围的说明，不能扩大为“任何 2048-bit 及以上实现都绝对安全”。这里只能说本次结果不表明现代体系已被攻破。
本窗口少见的「AI for cryptanalysis」官方硬发布；与上期 Cyber 攻防叙事对照，但对象是已退役密钥长度。
- **是什么**：
  - 官宣：@GoogleDeepMind 11-07 01:20 Asia/Singapore；VP Science @pushmeet X Article 同日展开。
  - 官方自报：人机协作推进对遗留 1024-bit RSA 的分析；官方强调本次结果不表明现代 2048-bit 及以上体系已被攻破。具体独立复现待核；此处不转述算法、控制条件或利用细节。
  - 边界（官方反复强调）：只影响过时的 1024-bit；现代协议普遍 2048-bit+ **仍然安全**；目的是更快压力测试「计算困难假设」。
  - 技术 PDF（官方 Article 内链）：[Faster Affine Root…](https://storage.googleapis.com/deepmind-media/papers/Faster_Affine_Root_and_a_1024bit%20Computation.pdf)、[Fan Factories…](https://storage.googleapis.com/deepmind-media/papers/Fan_Factories_Multiple_Number_Fields_in_Factorization_Factories_and_Batch_NFS.pdf)。deepmind.google 上一条猜测博客路径 404，以 X Article + PDF 为准。
- **为何重要**：把「agent 加速数学/密码分析」从口号落到可下载论文；对标准迁移与「AI 缩短防御提前量」讨论有直接材料。
- **对谁·深读建议**：密码与基础设施读者读两篇 PDF 的假设与沙盒边界；产品安全读者记住「1024 vs 2048」官方免责声明。
- **证据**：
  - 官方自报：[@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2118755418675765656)、[@pushmeet Article](https://x.com/pushmeet/status/2118752095859794390)、上述两篇 Google 存储 PDF
- **约时**：2026-11-07 01:20 Asia/Singapore（DeepMind）；Article 约 11-07 01:07 Asia/Singapore

##### 进展

###### 进展：Kimi K3.1 Pro——本窗口无权重/许可实质变更；HF 元数据仍停在 11-05，下载约 2.6 万
- **是什么（新增）**：来源记录 重核 `moonshotai/Kimi-K3.1-Pro`：`lastModified` 仍为 2026-11-05 15:11:43 Asia/Singapore；downloads≈25569；likes≈1729；siblings=112；`license=other`（具体条款仍见仓库 LICENSE，上期已述营收阈值，本期未发现 LICENSE 文件日期变更信号）。X News 仍在传播开放权重/NVIDIA Build 免费试用等，多为上期事件余波。未见 Moonshot 官方本窗口新的许可修订长帖。
- **证据**：来源记录：[HF 模型 API/页](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)；余波例：[X News NVIDIA Build](https://x.com/i/trending/2118755132603060694)
- **约时**：HF 核验 11-09 上午 Asia/Singapore

###### 进展：Claude Personal Finance / vault——本窗口无产品或论文增量官宣
- **是什么**：定向检索未见 @claudeai / @AnthropicAI 对本窗口 Personal Finance 扩区或 vault 随访的新主帖；上期条目不重复。
- **证据**：官方检索空窗（相对上期帖）
- **约时**：覆盖至 11-09

###### 进展：Cursor Live Apps / 扩展投毒——官方账号本窗口无新帖；未见新 IoC
- **是什么**：公开 `from:cursor_ai` 在窗口内 result_count=0。上期 Live Apps 与投毒后续无线索更新可写。
- **证据**：检索元数据（空）
- **约时**：11-09

###### 进展：METR 加速评估——无 Anthropic 正式对标 RSP 长文；讨论仍在
- **是什么**：上期 Sam McCandlish「未来几周自家报告」承诺本窗口未见落地长文。X News 仍转述 METR「约 2×」等（数字以上期 METR 原文为准，勿用 News 摘要）。国会侧有人借题发挥（待核政治转述）。
- **证据**：上期 [METR 原文](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/)；本窗口无新官方长文链接
- **约时**：持续讨论

###### 进展：GPT‑6.2 / Fable / Mythos——仍无产品发布；但 Anthropic 记忆文在评测中点名「Claude Fable 5」
- **是什么**：dotey 等「GPT‑6.2 要来了」属猜测帖，无 OpenAI 官宣。Mythos 无线索。**注意**：Anthropic 记忆博文在宝可梦对比里写到 Claude Fable 5（及 Sonnet 5 / Opus 5.5 等）——这是官方研究叙述中的模型名，**不是**对外发售确认。
- **证据**：猜测例：[dotey](https://x.com/dotey/status/2119539550112317743)；官方评测命名见 [记忆原文](https://www.anthropic.com/research/components-of-agent-memory)
- **约时**：猜测帖 11-09 清晨 Asia/Singapore

###### 进展：Meta 将 Muse Wonder 训练的专项模型接入 Muse 与 Meta AI（Active Memory / Active Focus）
- **是什么**：@AIatMeta 11-07 02:14 Asia/Singapore。官方自报：Active Memory 识别早先信息是否仍相关；Active Focus 在约束变化时恢复/找替代。Muse 上自报「与目标关键信息遗忘」约 **2.4× 减少**，约束演化下「摆脱卡住」约 **67% 改进**（厂商自报，待第三方）。研究博客短链跳转 meta 域。
- **证据**：官方自报：[@AIatMeta](https://x.com/AIatMeta/status/2118768974779634084)
- **约时**：11-07 02:14 Asia/Singapore

###### 进展：评测榜——GPT Image 2.6 登 AA 图像榜；Decision Index 等有更新声量
- **是什么**：@ArtificialAnlys 称 GPT Image 2.6 在 AA-Image-T2I v2.1 与 Editing v2.1 占 #1/#2；另有 Decision Index v2 讨论。均为 AA 自报榜单，非模型卡。
- **证据**：[@ArtificialAnlys Image 2.6](https://x.com/ArtificialAnlys/status/2118851088111865983)
- **约时**：11-07 07:40 Asia/Singapore

##### 其他

- Anthropic 科学建模嘉宾博文（@AnthropicAI 11-07 03:49 Asia/Singapore）→ [teaching-ai-to-build-scientific-models](https://www.anthropic.com/research/teaching-ai-to-build-scientific-models)：AI 写/跑/拟合/修订科学模型代码。属研究向，未单列主条。
- How researchers use Claude（约 20.7 万科研会话）：站点 Published Nov 5, 2026，**略早于本窗口起点**；本窗口有宝玉长拆（11-08）。关键官方自报：数据分析约占 Claude 科研会话 1/3、Claude Code 近一半；情景推演「现有能力普及约可翻倍、非体力全自动化则 CS/统计最高约 15×」——模型假设强，作背景勿当预测 来源记录。[报告页](https://www.anthropic.com/research/how-researchers-use-claude)、[宝玉解读](https://x.com/dotey/status/2119283516143776186)
- X News 高频：Claude Code vs Codex、Opus 5.5「手感/推理风格变化」、harness 比模型更决定分数、Gemini 4 Carbon 仍难获取等——多用户观察或摘要，**待核**，未升主条。
- OpenAIDevs：Showcase tab、GPT Image 2.6 做 GIF、Pro/Business 可领 API credits 等开发者向更新。

##### A. 时间线 / 官方覆盖

| 来源 | 覆盖（Asia/Singapore） | 备注 |
|------|-------------|------|
| 首页时间线 3 页 | 约 11-08 01:01 → 11-09 09:13 | ~294 帖；仍有 next_token，未翻第 4 页 |
| 官方检索 off09a/b | 约 11-07 01:20 → 11-09 05:20 | 含 DeepMind/OpenAI/Anthropic/Meta/Tibo/AA/dotey 等 |
| 定向 topic | 窗口内 | IPO/Cyber/Kimi/Claude Code 等；噪声已过滤 |
| 缺口 | 11-06 09:50 → 11-08 01:01 | 靠 search_posts_all + News 补；非时间线全量 |

##### B. Today's News（摘录，摘要≠来源记录）

- Claude Code Desktop / harness / Opus 5.5 手感争论（多条）
- Anthropic IPO 路演与估值下修讨论：[2119174990922666252](https://x.com/i/trending/2119174990922666252)、[2118150803340788179](https://x.com/i/trending/2118150803340788179)
- Kimi 开放权重余波 / NVIDIA Build：[2118824973016117608](https://x.com/i/trending/2118824973016117608)、[2118755132603060694](https://x.com/i/trending/2118755132603060694)
- METR 加速评估余波：[2118427442922901851](https://x.com/i/trending/2118427442922901851)
- Gemini 4 Carbon 难获取：[2119567610132009285](https://x.com/i/trending/2119567610132009285)
- Visa Agentic Commerce Benchmark 等非核心 AI 实验室条目略

##### C. 来源记录 摘要

1. Anthropic 11-06 工程文定义 agent memory 与 dreaming；多组官方自报评测数字见主条 1（非第三方复测）。
2. SEC：Anthropic 最新 S-1/A 仍为 2026-11-02（0001628280-26-068676）；本窗口无新定价修订可核。
3. ClaudeDevs：cloud sessions 自动环境配置已官宣（Pro/Max/Ultra）。
4. GitHub #107757 仍 open，最近更新 2026-11-08 22:09:40 Asia/Singapore。
5. Tibo：Pro 无 5h 限；100/200/500 = 10×/20×/50×(+ultrafast)。
6. FMF Jailbreak Rating Framework v1.0 已发布；OpenAI 发帖背书。
7. DeepMind：1024-bit RSA 两类弱点 + 论文 PDF；明确 2048+ 仍安全。
8. HF Kimi-K3.1-Pro：lastModified 仍 2026-11-05 15:11:43 Asia/Singapore；downloads≈25569。
9. Meta：Muse Wonder 专项模型进 Muse/Meta AI；2.4× / 67% 为官方自报。

##### E. 建议扩写（3–5）

1. **Dreaming 记忆栈**：对照 Letta sleep-time compute，写清四层记忆与「预加载必须短」——适合 agent 工程读者。
2. **IPO 文件 vs 路演叙事**：一张表列 S-1 已披露项 vs Bloomberg/X 待核估值，避免合刊把买方口头区间写成定价。
3. **FMF 越狱分级 × GPT‑6 Cyber Critical**：治理侧扩写——成功越狱如何排序修复优先级。
4. **DeepMind 1024 压测**：科普「为何还测退役密钥」+ 链到两篇 PDF 的可复核主张。
5. **Claude Code 云环境 + #107757**：产品便利与 CLI 隐私/供应链并读，追 changelog 是否 2.1.317。


## GitHub 项目与发行

### 项目原始材料

#### GitHub 三日刊（2026-11-06 → 2026-11-09）

1. **Transformers Patch v5.22.2（Jinja 沙箱加固）**
Hugging Face Transformers 于 11-06 23:43（Asia/Singapore）发布正式补丁 v5.22.2（`prerelease=false`）。changelog 只收了两笔：一是 Jinja 沙箱加固（#50431），二是分布式场景下仅对 NCCL 设置 `device_id`（#50281）。对所有用 chat template / Jinja 渲染提示词的部署，这是安全向补丁，不是模型功能发布；跑多卡 NCCL 的人也应顺带升。不要把它当成新架构或新模型版本。
证据：[v5.22.2 Release](https://github.com/huggingface/transformers/releases/tag/v5.22.2) · [huggingface/transformers](https://github.com/huggingface/transformers)

2. **DIYgod/pinky：人在回路的手机操控网关**
DIYgod（RSSHub 作者，个人账号 `DIYgod`，邮箱域名 diygod.me）于 11-07 00:53（Asia/Singapore）公开本仓，语言 Go，Apache-2.0；截至 11-09 09:19（Asia/Singapore）约 **828 星（总量）**，窗口内持续有正式版发布（如 `v2026.1109.7`，`prerelease=false`）与多人合入，提交活跃与 README / `android`·`cmd`·`ui` 目录相符，未见明显假仓迹象。项目自称让本机 MCP 客户端经网关操作真机 iPhone / Android，并提供以下保护（未实测）：支付、转账等默认等人点允许，银行/钱包/密码管理应用默认对 agent 不可见，一次性验证码在界面与截图里打码；Android 13+ 还可走隐藏第二屏。做手机端 agent 自动化、又担心误触支付的人应看；这些保护未做运行时安全审计，勿仅凭 README 当作安全保证，也勿跑不明脚本。
证据：[DIYgod/pinky](https://github.com/DIYgod/pinky) · [最新 Release](https://github.com/DIYgod/pinky/releases/latest) · [作者主页](https://github.com/DIYgod)

3. **meta/astryx：Meta 开源、面向人与 agent 的设计系统（Beta）**
官方组织 `meta` 仓库，站点 [astryx.atmeta.com](https://astryx.atmeta.com) 可访问且与 README 互链；自称在 Meta 内部用了约八年、支撑 13,000+ 应用（标「自称」）。当前 Beta，基于 React 19+ / StyleX，提供 150+ 组件、主题、CLI 与面向编码助手的同一套文档约定。窗口内正式发了 v0.7.9（11-06 12:17 Asia/Singapore）、v0.7.10（11-07 02:53 Asia/Singapore）、v0.7.11（11-07 23:00 Asia/Singapore），均为 `prerelease=false`，内容以触控 Popover、Lightbox 缩放、Carousel snap、无障碍与 CLI 修复为主，不是 0.x 大版本首发。日榜约 **875 stars today**、总量约 **16,849**（抓取 2026-11-09 09:19 Asia/Singapore）；日/周榜窗口≠本期 72h 净增。做「agent 能搭 UI」或内部设计体系开源对照的前端团队值得跟。
证据：[meta/astryx](https://github.com/meta/astryx) · [v0.7.11 Release](https://github.com/meta/astryx/releases/tag/v0.7.11) · [官网 Docs](https://astryx.atmeta.com)

4. **dsx-ai-factory/nvke（NVIDIA Kubernetes Engine，Preview）**
仓库在组织 `dsx-ai-factory` 下，但 README 版权署名为 NVIDIA，且官方文档站 [docs.nvidia.com/nvke/](https://docs.nvidia.com/nvke/) 可打开并描述同一产品，身份可交叉核实。定位是给 AI 工厂运营方在自有 GPU 裸机上安装的 **Kubernetes 管理平面**（创建/扩缩/升级 workload 集群），依赖 NICo；文档写明 Preview、不建议生产。日榜约 **345 stars today**、总量约 **860**（同次抓取）；窗口内 **无** 新 GitHub Release（最近正式版仍是窗口前的 v0.23.1）。本期收录理由是官方 Preview 首次进入雷达 + 日榜异常，不是版本 bump。平台 / 私有云 GPU 团队可当「NVIDIA 在开源什么」来读，勿当生产就绪发行版。
证据：[dsx-ai-factory/nvke](https://github.com/dsx-ai-factory/nvke) · [NVIDIA 文档 What is NVKE](https://docs.nvidia.com/nvke/) · [GitHub Trending 日榜](https://github.com/trending?since=daily)

（热榜口径：日榜约为最近 24 小时，周榜统计最近七天，均于 2026-11-09 09:19 Asia/Singapore 抓取，不可当作本期 72h 净增。周榜前列 NVIDIA/auto-ontology 已在 11-06 报道；vercel-labs/agent-browser 日增约 815、周增约 2,190，但窗口内无新正式 Release，仅留榜/热度，不单列。新仓搜索前列大量「预激活安装包」类仓库未收录。`ranxianglei/billion-context` 日榜约 460、总量约 5,174，但 open issues 约 923 与个人账号声明的「5× / billion tokens」高度自述并存，可信度未充分交叉验证，本期不收录。）

> 编辑注：这项取舍源于关键性能说法未充分交叉核验，不是因为 issue 数量多便判定项目恶意；原始计数仅作快照保留。

窗口内无：vllm-project/vllm、sgl-project/sglang、ggml-org/llama.cpp（仅有 `b12xxx` 且 `prerelease=true` 的日构建，未收）、ollama/ollama、pytorch/pytorch、huggingface/datasets、openai/openai-python、anthropics/anthropic-sdk-python、anthropics/anthropic-sdk-typescript、openai/codex（仅 `*-alpha.*` 且 `prerelease=true`）、modelcontextprotocol/python-sdk、modelcontextprotocol/typescript-sdk、comfyanonymous/ComfyUI、axolotl-ai-cloud/axolotl、langchain-ai/langchain（常规 / 预发布未收录：openai-node v7.53.0 主要为 agent session 错误改以 stream 事件下发；unsloth v0.1.916-beta；langgraph-sdk 0.4.14 / langgraph-cli 0.4.42）


## 模型与数据集

### 模型、数据与榜单原始材料

#### HF / 模型三日刊原始素材 · 2026-11-09

- **窗口**：2026-11-06 09:50:00 Asia/Singapore（2026-11-06 01:50:00 UTC）至 2026-11-09 09:25:43 Asia/Singapore（2026-11-09 01:25:43 UTC）；正文证据采集主要在 11-09 09:19–09:22 Asia/Singapore，ID/外链复验在09:24–09:25 Asia/Singapore，末尾 API / 链接复验另见日志。
- **去重基线**：已读取 11/06 两份 models.md，SHA256 均为 `7e90a42ad67b9f6b34d6dc8dcffdef1ff423dd0188d95402dbaac063fa55a748`；已读 11/06 榜单快照，文本/视觉补看 11/03 快照。没有把旧稿事实当成本期证据。
- **条数口径**：主条 **4**（3 个本窗新仓 + 1 个真实 drafter 权重更新）；次级 **2**（1 个本窗新仓 + 1 个发布/重传时间待核）；榜单 **6**（LMArena 三榜 + AA 三榜）；数据集新条 **4**。Kimi 专项复核、延续热度及过滤审计另列，不计作新增。
- **本窗判断**：没有新的巨型通用基座主线，值得深读的是后训练的可审计性、推测解码与连续潜空间语言建模。不能把 PLaMo 的窗前发布、Qwen 的模板更新或 Kimi 的持续热度写成新发。
- **开放度口径**：Apache-2.0 / MIT 是 OSI 认可的软件许可证；本稿可确认的是权重适用该许可，**未审计每个模型是否满足完整 Open Source AI Definition 的训练数据/训练代码要求**。自定义、非商用、缺许可不写成“OSI 开源”。`gated:auto` 只是自动授权门槛，不等于未发布。

##### 一、优先主条

###### 1. Arete-27B：把价值对齐做成“权重 + 训练数据 + 评测”可检查的实验（本窗新发）

Nous Research 在官方组织发布了 Qwen3.8-27B 的全参数 SFT 微调，价值立场改变是其明确目标，而不是新架构或通用能力跃迁。真正值得跟进的是模型、训练配对数据和独立保留评测同时可读；作者用自己的口径声称改变了特定政治话题的回答框架，不能把这个单方评测写成“已客观消除偏见”。它也不是无说明的 Uncensored/GGUF 重打包。

**意义 / 适用人群 / 深读建议**：适合研究后训练、偏见测量和训练数据审计的团队。先看评测题目、来源和裁判 rubric，再看分数；英文来源选择、价值分类与裁判本身都可能带来系统偏差。不要直接把它当成中文通用助手的升级版。

**来源记录**
- HF ID：`NousResearch/Arete-27B`（models API；[实时元数据](https://huggingface.co/api/models/NousResearch/Arete-27B)）。
- createdAt：2026-11-07 03:31:28 Asia/Singapore。
- lastModified：2026-11-07 05:04:27 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**293 / 1,747**；采集：2026-11-09 09:19:55 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**apache-2.0**；pipeline：**text-generation**；gated：`False`。
- 开放度：开放权重；Apache-2.0（OSI 认可许可证）；不据此自动宣称完整开源 AI。
- 官方身份 / 来源：Nous 官方发布文章反链同名 HF 权重、训练集和评测集；HF 作者 NousResearch，提交者 mormio / dmayhem93。
- siblings：32 个条目；18 个 safetensors。 18 片 BF16，HF safetensors 统计 27,356,728,560 参数；tree 的 lastCommit 与上传提交一致。
- 权重/数据提交：[443b722e87](https://huggingface.co/NousResearch/Arete-27B/commit/443b722e87ad08bec9d4750b1e9e689029ea4be5)，2026-11-07 03:31:51 Asia/Singapore；`Add files using upload-large-folder tool`。
- 可复查：[HF 页面](https://huggingface.co/NousResearch/Arete-27B) · [文件树](https://huggingface.co/NousResearch/Arete-27B/tree/main) · [提交历史](https://huggingface.co/NousResearch/Arete-27B/commits/main)。

**待核**：作者报告其 803 题评测中“propaganda”回答比例 22%→0.9%、事实分 2.32→2.98/5；均为作者自测，非本次实测。部分跨模型温度、thinking 设置不同；博客 thinking-on 行仅完成 2/5 次运行，是暂定结果。模型卡称约 20k prompts，当前训练数据卡列 34,878 prompts / 29,236 SFT rows，博客互动图又写 28,886 examples；版本与最终训练子集对应关系未核清，不能混用这些数字。

具体来源：[官方发布文章](https://nousresearch.com/arete)；正文反链关系保存在 （采集证据快照）；Trending #9、trendingScore 285（本期 API 快照）。

###### 2. 腾讯 DSpine 新增 Qwen3.8-27B 草稿模型：这是推理加速组件，不是腾讯新发 27B 基座（本窗新发）

腾讯把 DSpine 的适配推进到 Qwen3.8-27B，下载的是五层并行 drafter，文件约 4.05GB，不是把 27B 基座重新训练了一遍。它通过层间传递相邻前驱的预测特征提高草稿接受长度；本期新鲜点是新的目标模型适配和真实权重，而不是窗前论文首次公开。

**意义 / 适用人群 / 深读建议**：适合已有 Qwen3.8-27B + SGLang 的推理工程团队。先对齐并发、采样温度、draft block size、ReplaySSM 和缓存配置，再测端到端延迟；别把 tokens/s 的提高直接等同于任务正确率提升。

**来源记录**
- HF ID：`tencent/Qwen3.8-27B-DSpine-b16`（models API；[实时元数据](https://huggingface.co/api/models/tencent/Qwen3.8-27B-DSpine-b16)）。
- createdAt：2026-11-07 22:20:29 Asia/Singapore。
- lastModified：2026-11-07 23:40:48 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**95 / 652**；采集：2026-11-09 09:19:55 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**apache-2.0**；pipeline：**text-generation**；gated：`False`。
- 开放度：开放权重；Apache-2.0（OSI 认可许可证）；属于 drafter，不是完整基座。
- 官方身份 / 来源：tencent 官方组织；DSpine 项目页署名 Tencent YouTu Lab 并反链此精确 HF 仓库。
- siblings：5 个条目；1 个 safetensors。 model.safetensors，4,051,831,880 bytes；tree lastCommit 指向本窗 Upload 4 files。
- 权重/数据提交：[30de2dad4d](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16/commit/30de2dad4de18ddf9c66d6a5a3a39b59ea6444fb)，2026-11-07 22:33:15 Asia/Singapore；`Upload 4 files`。
- 可复查：[HF 页面](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16) · [文件树](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16/tree/main) · [提交历史](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16/commits/main)。

**待核**：卡片自报 WorkBuddy Code xhigh 回放吞吐 613.55 tokens/s、较 AR 3.18×，非本次实测。该比较为并发 8 的回放，DSpine block16、对照 DFlash2 block8，不能当成所有在线负载的公平硬件极限。对真实 agent 首字延迟、拒收率和长上下文负载仍需自测。

具体来源：[DSpine 官方项目页](https://dspine-project.github.io/)；项目页明确新增 Qwen3.8-27B 支持，保存在 （采集证据快照）。

###### 3. ByteDance Seed Cola2：连续潜变量语言模型终于有可下载 checkpoint，但别写成许可完备的开源聊天模型（本窗新发）

Cola2 把语义压缩、潜空间生成和离散文本解码拆成互相配合的层次结构：先压成连续语义块，再由 DiT 建模，最后解码并重新编码反馈。此次官方 HF 仓确有八片权重和推理代码，不是只有论文的空仓；但这是研究基座，未做指令聊天后训练，权重许可也未明确，不能因为代码 Apache-2.0 就给整套模型盖“开源”章。

**意义 / 适用人群 / 深读建议**：适合语言建模研究、扩散语言模型、推理系统研究者。优先读“压缩是否保留决策信息”和 encoder/decoder 共适应设计；一般应用团队没有必要把它替换生产聊天模型。

**来源记录**
- HF ID：`ByteDance-Seed/Cola2`（models API；[实时元数据](https://huggingface.co/api/models/ByteDance-Seed/Cola2)）。
- createdAt：2026-11-06 14:59:36 Asia/Singapore。
- lastModified：2026-11-06 17:54:18 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**10 / 523**；采集：2026-11-09 09:19:55 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**未声明**；pipeline：**text-generation**；gated：`False`。
- 开放度：权重文件公开可下载，权重授权未明确；不能确认 OSI 开源，也不是闭源 API-only。代码 Apache-2.0 不自动覆盖权重/第三方素材。
- 官方身份 / 来源：ByteDance-Seed 官方组织；论文作者 Hongcan Guo 与提交者 HongcanGuo04 一致；作者项目页反链精确 HF 仓。
- siblings：31 个条目；8 个 safetensors。 8 片 safetensors；另有 eval_data 中八个 JSONL、SHA256SUMS、custom Transformers code。卡片明确训练代码未随本次 release 提供。
- 权重/数据提交：[a310630624](https://huggingface.co/ByteDance-Seed/Cola2/commit/a3106306247a2687b0d785ae76600c8f63c1dc0b)，2026-11-06 16:58:42 Asia/Singapore；`Upload folder using huggingface_hub`。
- 可复查：[HF 页面](https://huggingface.co/ByteDance-Seed/Cola2) · [文件树](https://huggingface.co/ByteDance-Seed/Cola2/tree/main) · [提交历史](https://huggingface.co/ByteDance-Seed/Cola2/commits/main)。

**待核**：卡片/论文自报 346.03B source tokens、八任务平均 60.10，均未实测；decoder 从既有 Qwen 基座初始化，不应把“43× 更少 token”解读成完整从零训练成本仅为对照的 1/43。模型卡已提示各模型 recipe/tokenizer 不同，潜变量采样有随机性，论文原始 seeds 未发布。权重、tokenizer、评测数据各自许可仍需逐项确认；运行需要审计 remote code。

具体来源：[作者项目页](https://hongcanguo.github.io/Cola2/)；（采集证据快照） 与本期模型卡。

###### 4. Nemotron 3.5 Parse 刷新 DFlash2 权重：本窗是文档解析加速更新，不是 Parse 基座首发（本窗真实权重更新）

NVIDIA 这次确实改了权重，不只是 README：仓内 dflash2/model.safetensors 的 lastCommit 落在窗口内，而主 model.safetensors 仍是 10 月版本。应写成老文档解析器的推测解码加速组件刷新，不能写成“11 月新发 Nemotron 3.5 Parse”。这比仅按 lastModified 判断更新更可靠。

**意义 / 适用人群 / 深读建议**：适合批量 PDF / 报表解析、RAG 数据准备团队。对比单/双/三 pass 的成本与质量，先在自己文档集验证 Markdown、表格合并与阅读顺序，后看吞吐数字。

**来源记录**
- HF ID：`nvidia/Nemotron-3.5-Parse`（models API；[实时元数据](https://huggingface.co/api/models/nvidia/Nemotron-3.5-Parse)）。
- createdAt：2026-09-03 14:29:29 Asia/Singapore。
- lastModified：2026-11-07 06:57:31 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**154 / 19,392**；采集：2026-11-09 09:21:02 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**openmdw-1.1**；pipeline：**image-text-to-text**；gated：`False`。
- 开放度：开放权重，OpenMDW-1.1 宽松模型许可；本次未核到正式 OSI 批准，不标为 OSI 开源。
- 官方身份 / 来源：nvidia 官方组织，模型卡署名 NVIDIA 并链接 NVIDIA Build 的同名产品；本次 NVIDIA Build 页面 WebFetch 超时，未作为独立反链证据。
- siblings：216 个条目；2 个 safetensors。 2 个 safetensors：主模型 + dflash2/model.safetensors。主权重 lastCommit 2026-10-18 10:52:38 Asia/Singapore / 02:52:38 UTC，drafter 于本窗刷新。tree 仅取前 100 条（分页未全量），但两份权重均已命中，完整 siblings 另存。
- 权重/数据提交：[72ad4d71dd](https://huggingface.co/nvidia/Nemotron-3.5-Parse/commit/72ad4d71dd827135ee581502363e14748008900a)，2026-11-07 06:57:31 Asia/Singapore；`Refresh DFlash2 weights, throughput results and model-card plot`。
- 可复查：[HF 页面](https://huggingface.co/nvidia/Nemotron-3.5-Parse) · [文件树](https://huggingface.co/nvidia/Nemotron-3.5-Parse/tree/main) · [提交历史](https://huggingface.co/nvidia/Nemotron-3.5-Parse/commits/main)。

**待核**：0.631B 主模型、89.3M drafter、ParseBench triple-pass 75.20、单 pass 18.57 pages/s 都是作者报告，非本次实测。速度测试为单 H200、2,078 页、三次中位数，不能外推到消费级 GPU。卡片 DFlash2 公告写 11/04，这是旧功能上线日期；本窗只是 11/06 UTC 刷新。

具体来源：[本窗权重文件记录](https://huggingface.co/nvidia/Nemotron-3.5-Parse/blob/main/dflash2/model.safetensors) · [OpenMDW-1.1 原文](https://openmdw.ai/license/1-1/)。

##### 二、次级线索（不抢主线）

###### 5. Sage-SciPerception：九个科学模态投影器已上传，许可与上游依赖仍不齐（本窗新发）

这不是新的全能科学大模型，而是将晶体、光谱、蛋白序列、DNA/RNA、ECG/EEG 等科学特征映射到语言模型输入空间的九个任务投影器。权重是真的，但小规模关注、缺许可证，且部分科学 encoder / 预处理资产未附，不宜宣传为开箱即用的开源科研助手。

**意义 / 适用人群 / 深读建议**：科学 AI 研究者可读其 prompt embeddings 接入方式；一般用户先等资产、许可与复现实验齐全。不要拿不同任务的 F1/MCC/accuracy 做横向总排名。

**来源记录**
- HF ID：`internlm/Sage-SciPerception`（models API；[实时元数据](https://huggingface.co/api/models/internlm/Sage-SciPerception)）。
- createdAt：2026-11-06 15:34:30 Asia/Singapore。
- lastModified：2026-11-06 20:57:46 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**9 / 103**；采集：2026-11-09 09:19:55 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**未声明**；pipeline：**未标 pipeline_tag**；gated：`False`。
- 开放度：公开可下载 projector 权重；许可元数据未指定，不能确认 OSI 开源或商用授权。
- 官方身份 / 来源：internlm 官方组织；模型卡署名 InternLM 并指向同名官方项目。未额外读取 GitHub 反链，官方性主要依据已知 org 与署名。
- siblings：39 个条目；9 个 safetensors。 9 个 projector.safetensors；tree 文件最后提交均指向 release nine GLM scientific projectors；不是九个完整语言模型。
- 权重/数据提交：[fd0cd31495](https://huggingface.co/internlm/Sage-SciPerception/commit/fd0cd31495b62ae090f082c63e1a1f2536d14df6)，2026-11-06 17:36:25 Asia/Singapore；`feat(projectors): release nine GLM scientific projectors`。
- 可复查：[HF 页面](https://huggingface.co/internlm/Sage-SciPerception) · [文件树](https://huggingface.co/internlm/Sage-SciPerception/tree/main) · [提交历史](https://huggingface.co/internlm/Sage-SciPerception/commits/main)。

**待核**：模型卡自报各任务成绩均未复测；DNA、MPBind、ncRNA 所需 task-adapted scientific models 尚未包含，输入从已准备的科学特征开始；须核匹配语言模型 revision 和各依赖许可。

###### 6. TwIL-8B：窗内有权重文件提交，但“首发”日期不能只信当前历史（时间线待核，降权）

Granite 4.2 8B 上的数学/代码后训练模型当前有 balanced 与 verbose 两套完整权重，文件 lastCommit 是 11/08；然而第三方发布报道与测试已在 11/04–05 出现，说明不能凭当前只剩一条 Publish 提交就说本窗首次发布。更稳妥的写法是“本窗仓库发布/重传记录，是否发生权重内容变化待核”，不进新发统计。

**意义 / 适用人群 / 深读建议**：可作小模型推理研究候选，尤其是非商用本地实验。卡片的长思考链、知识短板和 benchmark 版本缺口，比漂亮的单项成绩更值得先读。

**来源记录**
- HF ID：`webAI-Official/TwIL-8B`（models API；[实时元数据](https://huggingface.co/api/models/webAI-Official/TwIL-8B)）。
- createdAt：2026-10-15 00:50:12 Asia/Singapore。
- lastModified：2026-11-08 17:57:35 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**232 / 22,737**；采集：2026-11-09 09:19:56 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**other / webai-non-commercial-license-ver.-1.0**；pipeline：**text-generation**；gated：`False`。
- 开放度：开放权重；webAI Non-Commercial License ver.1.0，非商用限制，因此非 OSI 开源。
- 官方身份 / 来源：HF 发布账号 webAI-Official；外部 webAI 署名发布帖与多篇早期报道一致，但本次未取得官网反链，独立官方身份链不如前三条充分。
- siblings：23 个条目；2 个 safetensors。 2 个完整 safetensors（balanced / verbose），各 17,583,228,544 bytes；并非仅 GGUF repack。当前文件时间无法证明与 11/04 版本的字节差异。
- 权重/数据提交：[9563ba7dfb](https://huggingface.co/webAI-Official/TwIL-8B/commit/9563ba7dfb70eeca4a26654b195011cbf818e7d9)，2026-11-08 17:57:35 Asia/Singapore；`Publish TwIL-8B`。
- 可复查：[HF 页面](https://huggingface.co/webAI-Official/TwIL-8B) · [文件树](https://huggingface.co/webAI-Official/TwIL-8B/tree/main) · [提交历史](https://huggingface.co/webAI-Official/TwIL-8B/commits/main)。

**待核**：MATH-500 98.2 / LiveCodeBench 81.6 为作者自报，后者只在 verbose 测过且版本/日期窗未记录；不能写成已压过其他 31B 模型。需要旧 revision 的 LFS hashes 才能证明本窗权重更新；当前证据不足。具体早期报道与局部测试：[11/04 报道](https://www.marktechpost.com/2026/11/04/webai-twil-8b-reasoning-model/) · [11/05 Mac mini 测试](https://nithinkd.github.io/workshop/pieces/2026-11-05-twil-8b-on-a-mac-mini/)。后者只是小样本，不替代独立标准榜单。

##### 三、Kimi K3.1 Pro 专项复核（延续热度，不是本窗新发）

Kimi 的官方权重仍可见，但本窗没有新 checkpoint：lastModified 仍停在 11/05 UTC。官方博客也仍写“Full model weights will be released by Nov 4, 2026”，没有改成已发布或补上该模型 HF 链接。AA 的 46.5 与开放权重标注未变；LMArena 虽刷新了文本/视觉榜，完整返回表里仍未见 K3.1 Pro，不能把榜上的 Kimi K3 当成 K3.1 Pro。

**意义 / 适用人群 / 深读建议**：仍适合有大集群、关心长上下文 agent 的部署团队；本期没有理由重复上期整套性能故事。商用尤其要读 MaaS / 超大规模产品条款。

**来源记录**
- HF ID：`moonshotai/Kimi-K3.1-Pro`（models API；[实时元数据](https://huggingface.co/api/models/moonshotai/Kimi-K3.1-Pro)）。
- createdAt：2026-11-02 12:13:51 Asia/Singapore。
- lastModified：2026-11-05 15:11:43 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**1,729 / 25,569**；采集：2026-11-09 09:19:55 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**other / kimi-k3.1-pro**；pipeline：**image-text-to-text**；gated：`False`。
- 开放度：开放权重；自定义 Kimi K3.1-Pro License（other），含收入/规模相关附加条款，非 OSI 开源。
- 官方身份 / 来源：moonshotai 官方组织；AA 当前模型页反链精确 HF ID；博客与模型卡署名一致。
- siblings：112 个条目；96 个 safetensors。 96 片 safetensors；tree 抽样各片 lastCommit 为窗前 Initial commit。公开可见时间不等于 initial commit 时间。
- 权重/数据提交：[6d0a020295](https://huggingface.co/moonshotai/Kimi-K3.1-Pro/commit/6d0a0202956796543364d666ab19c6ad1a494ee1)，2026-11-02 12:13:51 Asia/Singapore；`Initial commit`。
- 可复查：[HF 页面](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) · [文件树](https://huggingface.co/moonshotai/Kimi-K3.1-Pro/tree/main) · [提交历史](https://huggingface.co/moonshotai/Kimi-K3.1-Pro/commits/main)。

**待核**：官方博客没有可用的修订时间，故只能确认今天正文仍如此，不能证明整个页面完全没改；Highspeed 是否独立 checkpoint 未核。AA 单模型页 WebFetch 超时，但公开 HTML 采集 HTTP200、首页解析和 /models 可读页面可相互印证。官方仓提交历史无本窗提交。

具体来源：[官方博客](https://www.kimi.ai/blog/kimi-k3-1-pro) · [AA 精确模型页](https://artificialanalysis.ai/models/kimi-k3-1-pro)。原始/可见正文：（采集证据快照）、（采集证据快照）；与旧页比较的 HF links 列表相同（有其他模型引用，但没有 K3.1 Pro 自身链接）。

##### 四、数据集：四个本窗新仓，分清作者数据、合成数据和社区转换

###### D1. Arete data pairs：审计价值大于直接拿来喂模型（本窗新发）

Nous 放出了 teacher 与起点模型的配对回答、接受筛选状态和 reasoning traces，研究者终于有机会检查后训练“改了什么”。但数据卡直说多数 accepted rows 仍带 factual_error 标签，且没有许可字段，不应不筛选就直接训练或把它称为开放商用训练集。

**意义 / 人群 / 深读**：偏好对齐、数据清洗研究者；先按 review_scores / issue_tags 切片，核验来源与最终 SFT 子集。

**来源记录**
- HF ID：`NousResearch/arete-data-pairs`（datasets API；[实时元数据](https://huggingface.co/api/datasets/NousResearch/arete-data-pairs)）。
- createdAt：2026-11-07 04:53:00 Asia/Singapore。
- lastModified：2026-11-07 05:14:56 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**43 / 642**；采集：2026-11-09 09:19:56 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**未声明**；pipeline：**未标 pipeline_tag；task_categories=['text-generation', 'question-answering']**；gated：`False`。
- 开放度：数据文件公开；未声明许可证，不能继承模型 Apache-2.0；不作 OSI 模型分类。
- 官方身份 / 来源：Nous 官方发布文章反链该精确数据集；与 Arete 模型同一发布组织。
- siblings：25 个条目；数据文件清单已保存（不是模型权重）。 siblings 含 paired/、sft_accepted/、reasoning/ 的 JSONL 与 release_manifest.json。
- 权重/数据提交：[0bd530bb63](https://huggingface.co/datasets/NousResearch/arete-data-pairs/commit/0bd530bb6300d8b8c71a5104d4c4408750a64a1d)，2026-11-07 04:53:19 Asia/Singapore；`arete data pairs v1.0.0: paired + sft_accepted + reasoning`。
- 可复查：[HF 页面](https://huggingface.co/datasets/NousResearch/arete-data-pairs) · [文件树](https://huggingface.co/datasets/NousResearch/arete-data-pairs/tree/main) · [提交历史](https://huggingface.co/datasets/NousResearch/arete-data-pairs/commits/main)。

**待核**：卡片列 34,878 配对 prompts、29,236 accepted SFT rows，仅为作者计数，未逐行复算；与博客/训练叙述数目不一致。teacher 是否满足再分发条件、数据权利链、与保留评测的去重质量待核。Trending #9、score43。

###### D2. Propaganda_Eval：803 题的作者立场评测公开了，不是独立事实真理榜（本窗新发）

这份保留集给出题目、来源文章、必要事实和裁判脚本，适合复查 Arete 的具体行为变化。它测的是 Nous 定义的事实与框架维度，不能把分数泛化为模型的全部政治偏见或事实可靠性。

**意义 / 人群 / 深读**：评测研究者、模型风险审计；先看题目采样与 rubric，加入不同语言、不同来源的对照集再下结论。

**来源记录**
- HF ID：`NousResearch/Propaganda_Eval`（datasets API；[实时元数据](https://huggingface.co/api/datasets/NousResearch/Propaganda_Eval)）。
- createdAt：2026-11-07 00:58:27 Asia/Singapore。
- lastModified：2026-11-07 04:39:08 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**40 / 620**；采集：2026-11-09 09:19:56 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**mit**；pipeline：**未标 pipeline_tag；task_categories=['question-answering']**；gated：`False`。
- 开放度：公开数据，MIT 许可（OSI 认可软件许可证）；不等于题目内容免除原文权利义务。
- 官方身份 / 来源：Nous 官方发布文章反链；同组织作者数据，不是第三方独立榜单。
- siblings：7 个条目；数据文件清单已保存（不是模型权重）。 含 data/items.jsonl 与评分/裁判工具。
- 权重/数据提交：[63d1a456e7](https://huggingface.co/datasets/NousResearch/Propaganda_Eval/commit/63d1a456e747fbead2aa41873f9adcfcf54de43a)，2026-11-07 00:58:28 Asia/Singapore；`China Censorship & Propaganda Eval: 803 prompts, judge prompt, reference grader and scorer`。
- 可复查：[HF 页面](https://huggingface.co/datasets/NousResearch/Propaganda_Eval) · [文件树](https://huggingface.co/datasets/NousResearch/Propaganda_Eval/tree/main) · [提交历史](https://huggingface.co/datasets/NousResearch/Propaganda_Eval/commits/main)。

**待核**：803 题规模为卡片/页面显示，未逐题复核；来源、rubric、LLM judge 一致性与主观偏差待查。Trending #13、score37。不要与训练集混淆。

###### D3. Pixel Art Atlas：百万级 16×16 精灵数据可做风格实验，不适合直接测指令遵循（本窗新发）

作者发布合成像素画与英文描述，CC0 声明很友好；但说明已明确承认 caption 只是生成意图，未系统人工验图。适合像素风训练实验，不适合拿文字标注当高可信精确真值。

**意义 / 人群 / 深读**：像素游戏、美术工具和小图像生成研究者；先人工抽样检查图文一致性与主体泄漏，再划分评测集。

**来源记录**
- HF ID：`Angais/pixel-art-atlas-1.4m`（datasets API；[实时元数据](https://huggingface.co/api/datasets/Angais/pixel-art-atlas-1.4m)）。
- createdAt：2026-11-06 20:37:24 Asia/Singapore。
- lastModified：2026-11-06 21:05:13 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**51 / 1,771**；采集：2026-11-09 09:19:56 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**cc0-1.0**；pipeline：**未标 pipeline_tag；task_categories=['text-to-image']**；gated：`False`。
- 开放度：数据按作者可放弃权利范围作 CC0-1.0 声明；不覆盖第三方商标、素材或生成模型条款，不是模型开源发布。
- 官方身份 / 来源：Angais 作者自发布，卡片明说独立数据集，并非 Krea 官方或背书。
- siblings：21 个条目；数据文件清单已保存（不是模型权重）。 Parquet 训练/验证分片和原始 ZIP 资产清单可见；不含 LoRA 或生成模型权重。
- 权重/数据提交：[3183df4ee5](https://huggingface.co/datasets/Angais/pixel-art-atlas-1.4m/commit/3183df4ee59427d6d428b61948728e945b6a6f1b)，2026-11-06 20:28:04 Asia/Singapore；`Publish Pixel Art Atlas with training and validation splits`。
- 可复查：[HF 页面](https://huggingface.co/datasets/Angais/pixel-art-atlas-1.4m) · [文件树](https://huggingface.co/datasets/Angais/pixel-art-atlas-1.4m/tree/main) · [提交历史](https://huggingface.co/datasets/Angais/pixel-art-atlas-1.4m/commits/main)。

**待核**：卡片计数 1,409,404 张、1,405,308 train + 4,096 validation，未复算；来自 Krea 2 Turbo + LoRA，需核生成/再分发条件。commit 12:28 UTC 早于 createdAt 12:37 UTC，公开 API 与导入历史并非完全一致，不据此猜测首次公开分钟。Trending #7、score49。

###### D4. PLATEAU city GLB：社区把日本城市数据做成可流式场景资产，不是日本政府新发 AI 数据集（本窗新仓）

CodePawl 把已有政府城市数据改造成分块 GLB、LOD、移动端与碰撞网格。价值在工程可用性而非新采样；必须保留原始地方政府/MLIT 署名，不能因为 HF 仓刚创建就说城市原始数据也是本周新增。

**意义 / 人群 / 深读**：3D agent、WebGPU、城市演示开发者；先看坐标原点、单位、精度与署名条款，不用作测绘真值。

**来源记录**
- HF ID：`codepawl/plateau-city-glb`（datasets API；[实时元数据](https://huggingface.co/api/datasets/codepawl/plateau-city-glb)）。
- createdAt：2026-11-07 02:23:34 Asia/Singapore。
- lastModified：2026-11-07 14:43:50 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**31 / 1,850**；采集：2026-11-09 09:19:56 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**cc-by-4.0**；pipeline：**未标 pipeline_tag；task_categories=[]**；gated：`False`。
- 开放度：数据卡 CC-BY-4.0，需署名并保留修改说明；社区衍生，不是官方模型开源事件。
- 官方身份 / 来源：codepawl 社区转换；卡片明确非 MLIT / 地方政府制作或背书，列出原始来源与修改项。
- siblings：6,490 个条目；数据文件清单已保存（不是模型权重）。 GLB、metadata.jsonl / metadata.parquet、tiles.json；实际 siblings 共 6,490 个。
- 权重/数据提交：[afabd42481](https://huggingface.co/datasets/codepawl/plateau-city-glb/commit/afabd424814c1e09aa87d32105f9901047ba7c40)，2026-11-07 02:33:30 Asia/Singapore；`Add web`。
- 可复查：[HF 页面](https://huggingface.co/datasets/codepawl/plateau-city-glb) · [文件树](https://huggingface.co/datasets/codepawl/plateau-city-glb/tree/main) · [提交历史](https://huggingface.co/datasets/codepawl/plateau-city-glb/commits/main)。

**待核**：797 tiles、覆盖城市、尺寸/载入性能均来自作者卡片，未运行渲染验证；原始政府数据年份为 2020，不应混同采集日。Trending #16、score29。

##### 五、榜单：真正变化在 LMArena 刷新和 AA 图像榜新入场

###### B1. LMArena 文本终于刷新，但还没有 K3.1 Pro

文本榜由 Oct 27 刷到 **Nov 8, 2026**：9,003,272→**9,091,367** 票，418→**420** 模型。榜首 Gemini 4 Carbon (High) 1528±9→**1527±10（Preliminary）**；Argon #2 为1522±5；Muse Wonder (Max) 当前#3，Claude Opus5.5(High)#4。Kimi K3(Max) 是#19、1487±4，**不是K3.1 Pro**；后者在此次完整420行响应中仍未出现。

**意义 / 深读**：这次能明确说文本榜刷新了，不能继续沿用“未动”；也不能把 AA 上的领先结论套进人类偏好榜。**来源记录**：来源页标日期为11/08（日粒度，无具体时区时分，不擅自换成某个Asia/Singapore分钟）；本次读取11/09 09:19 Asia/Singapore。**待核**：11/06本地只有文本摘要，所引用的全文文件实际不存在，因此不能仅凭模型总数+2逐个断言谁是这窗新增；11/03完整表仅作辅助。所有 Elo 带置信区间，Preliminary尤其不宜过度排序。

[具体榜页](https://lmarena.ai/leaderboard/text)；（采集证据快照） 为本次完整响应的**选行快照**（不是420行全表）。

###### B2. LMArena 视觉也刷新，榜首没换

视觉榜从 Oct19 刷到 **Nov8**，1,493,948→**1,568,841** 票，166→**167** 模型；Claude Fable5(High) 仍#1、**1309±7**。当前#2 Claude Opus4.7 1300±7、#3 Qwen3.8-Max1299±7；完整167行中未见K3.1 Pro。

**意义 / 深读**：确认刷新但不是冠军更替；分差在区间内，不夸大#2/#3。**来源记录**：日期与票数来自本次WebFetch，读取11/09 09:19Asia/Singapore。**待核**：缺11/06完整视觉表，不能准确列全新增/移除名单；版权/开放度以模型自身许可为准，不由榜单名次决定。

[具体榜页](https://lmarena.ai/leaderboard/vision)；（采集证据快照）（选行）。

###### B3. LMArena 文生图刷新，但总票数倒退，先记录异常

日期 Nov2→**Nov8**，模型仍84个；GPT-Image-2.5 Sunburst仍#1，1427±5→**1428±5 Preliminary**。GPT-Image-2.6 Sunburst/Flare(Medium)仍#2/#4，**1406±13 /1383±13**，不是本窗才加入LMArena。

**意义 / 深读**：别把已在11/06稿出现的2.6档位再当新模型新闻。**来源记录**：总票数6,961,993→**6,880,326**，减少81,667；读取11/09 09:19Asia/Singapore。**待核**：票数回退可能涉及口径/筛选/缓存，原因未证实，不推测为热度下降，不把票数当累计单调序列。

[具体榜页](https://lmarena.ai/leaderboard/text-to-image)；（采集证据快照）（选行，与11/06完整84行基线比较）。

###### B4. AA Intelligence v5 默认28款的分数没变，不能把HTML对象数当新增

AA 本次可读页写 **Intelligence Index v5.0.1**。默认28款与11/06解析结果逐项核对，无分数变化：Gemini4Carbon60.0、KimiK3.1Pro46.5、Hy4 34.6、Inkling2Small30.6均维持。Kimi仍是页面标注的最高分开放权重模型；**它上期就已经是，不是今天新晋**。

**意义 / 深读**：读榜时须区分默认筛选与全站；本期默认图不支持“新冠军”故事。**来源记录**：首页公开HTML已存，默认28条；/models可读正文也确认v5.0.1与Kimi开放权重地位。**待核**：原始HTML可匹配对象46→62，包括alias/其他图表对象，不是新增16个评测模型；未取得全726模型统一数值导出，不做全榜无变化的断言。10/27前v4分数**不能**与v5纵向比较。

[具体模型榜](https://artificialanalysis.ai/models)；（采集证据快照）、（采集证据快照）、（采集证据快照）。

###### B5. AA 文生图新增 GPT Image2.6 两档，Sunburst到榜首

AA 文生图从106→**108**款，新增闭源 **GPT Image2.6 Sunburst(max)**、**Flare(max)**；分别#1 **1259±15**（4,947样本）、#2 **1228±12**（6,849样本）。旧Sunburst2.5为#3、1227±10，数值基本未动；Flare2.6与2.5Sunburst区间重叠，不应断言后者稳定落后。

**意义 / 深读**：这是本窗可证实的“新上榜”，不等于OpenAI本窗首次发模型，也不等于有HF开放权重。**来源记录**：108行完整表由本期HTML解析，与11/06名称集合相比只增这两条、无移除；页面发布月标Nov2026，无具体加入时间，精确入榜时刻待核。**待核**：与LMArena(Medium)不是相同推理档位，两站Elo不能直接相减或横比。

[具体榜页](https://artificialanalysis.ai/image/leaderboard/text-to-image)；（采集证据快照）、（采集证据快照）、（采集证据快照）。

###### B6. AA 图像编辑同样由2.6占据前二，但置信区间重叠

编辑榜77→**79**款，同样新增闭源GPTImage2.6 Sunburst(max)/Flare(max)：#1 **1209±14**（6,226样本）、#2 **1206±13**（6,413样本）；2.5Sunburst退#3、1199±11，MAI-Image-2.7-Preview退#4、1195±14，后者主要是被新模型挤下，并非能力骤降。

**意义 / 深读**：图像编辑的相对领先尚有较大不确定性；优先用自己的编辑任务复测。**来源记录**：79行完整表；对比11/06仅新增这两项，无移除；首轮SSL EOF失败，WebFetch成功并另取公开HTML成功，不能把失败当无变化。**待核**：前四置信区间重叠，排名不等于统计显著胜出。

[具体榜页](https://artificialanalysis.ai/image/leaderboard/editing)；（采集证据快照）、（采集证据快照）、（采集证据快照）。

##### 六、延续热度与降权审计（不当新发写）

###### 延续热度

Trending前三里只有Kimi官方模型值得跟踪部署；榜首Idol是窗前老版本，排名#2的去审查社区改装按规则过滤，不能用榜单热度制造一轮大模型发布潮。Ripple升#4但窗内改的是推理兼容代码，不是16片权重。

| 条目 | 本期模型Trending / score | likes / downloads | 窗口判断 |
|---|---|---|---|
| speridlabs/idol | #1 / 792 | 1,387 / 22,854 | 窗前发布；权重无本窗提交 |
| moonshotai/Kimi-K3.1-Pro | #3 / 562.5 | 1,729 / 25,569 | 窗前发布；见专项 |
| ricursiveAI/Ripple-65B-Preview | #4 / 393 | 403 / 5,087 | 本窗是Transformers4/5、缓存/position_ids兼容修复；不冒充新权重 |
| nvidia/simready-assets（数据集） | #1 / 243 | 1,485 / 1,434,099 | lastModified窗前，仅数据集延续热度 |

表内数据均来自11/09 09:19Asia/Singapore API；完整来源记录见下方补充，既有Kimi不重复展开。

###### 窗前发布 / 维护变更

- **Qwen3.8-27B**：11/07UTC更新标题为 response template / generation tags；降权，不是新权重。
- **MiniCPM-OCR-1.0**：11/08UTC是中文模型卡与图片/链接清理；降权。
- **Pika-H3-Flex**：11/07UTC仅改library_name以改善下载计数；降权。
- **PLaMo3Translate 0.8B/31B**：官方11/05已宣布发布，权重初始提交11/04UTC；窗内11/07–08UTC是chat template更新/回退。搜索结果把它包装成11/07新发，**以官方11/05原文与提交记录纠正**。自定义PLaMoCommunityLicense，非OSI。[11/05官方公告](https://www.preferred.jp/ja/news/pr20261105)
- **Cosmos3-Edge**：11/07媒体再次写“发布”，但本次API仍为7月创建、9月最后修改，8月权重更新；不是本窗新发。避免按报道日期误收。
- 其余Uncensored/Heretic/abliteration、社区GGUF/MLX重打包、0 downloads或只有README/模板变更的候选不进主条。名单在采集原始API/提交审计，不以名字推断诈骗。

###### 冒名 / 非官方（证据边界单列）

> 编辑注：保留原始分类标题，但“非官方”和“冒名”不是同义词。本条材料没有足够证据把 audnai 定性为冒名、恶意或诈骗。下列四个链接依次是公开元数据 API、模型主页、文件目录与提交历史，属于核验来源，不是官方背书或下载推荐；受限正文未读、权重文件未下载，保留中性说明而不删除来源。

本窗**未新增证据充分的冒名/诈骗定性**。上期可疑的 audnai 仓，本次与旧稿已有重要差别：公开元数据列出96片safetensors，downloads157，不能再照抄“0权重、downloads0”。它的作者仍是audnai而非moonshotai，属于第三方去审查衍生；manual gated导致README/commits匿名读取401，未实际下载权重，不能证明文件有效、也不能仅凭gate判定未发布或诈骗。官方使用入口仍应选moonshotai仓。

**来源记录**
- HF ID：`audnai/penclaw-Kimi-K3.1-pro-unrestricted`（models API；[实时元数据](https://huggingface.co/api/models/audnai/penclaw-Kimi-K3.1-pro-unrestricted)）。
- createdAt：2026-10-24 05:38:11 Asia/Singapore。
- lastModified：2026-11-06 20:34:39 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**184 / 157**；采集：2026-11-09 09:20:35 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**other / kimi-k3.1-pro**；pipeline：**text-generation**；gated：`manual`。
- 开放度：metadata声明other/Kimi许可、manual gated；实际权重可下载性与再分发合规未核，不作OSI开源结论。
- 官方身份 / 来源：第三方audnai，明确不是Moonshot官方；base_model元数据指向官方模型，不能继承官方身份。
- siblings：112 个条目；96 个 safetensors。 本期112 siblings、96片safetensors是公开元数据，不是实际下载验证。
- 可复查：[HF 页面](https://huggingface.co/audnai/penclaw-Kimi-K3.1-pro-unrestricted) · [文件树](https://huggingface.co/audnai/penclaw-Kimi-K3.1-pro-unrestricted/tree/main) · [提交历史](https://huggingface.co/audnai/penclaw-Kimi-K3.1-pro-unrestricted/commits/main)。

**待核**：提交历史/卡片匿名读取401；不获取登录、不越过gate；与上期空仓的公开转换时间无法核准。公开API200不能替代权重真实性审计。

> 编辑注：“与上期空仓的公开转换时间”只是在引用旧稿描述，并未证实该仓此前确实为空。本期只能确认公开元数据列有 96 片权重记录，不能推定真实文件有效、无效或未发布。

##### 七、补充来源记录：延续与过滤项的元数据（只供核验，不建议再写成主新闻）

###### speridlabs/idol
本期只用于去重或延续热度，不作为新发布推荐。

**来源记录**
- HF ID：`speridlabs/idol`（models API；[实时元数据](https://huggingface.co/api/models/speridlabs/idol)）。
- createdAt：2026-10-28 23:55:17 Asia/Singapore。
- lastModified：2026-10-30 02:17:36 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**1,387 / 22,854**；采集：2026-11-09 09:19:56 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**apache-2.0**；pipeline：**image-to-3d**；gated：`False`。
- 开放度：开放权重，Apache-2.0（OSI认可许可证）。
- 官方身份 / 来源：speridlabs作者原始模型；本期以官方org与已有发布链为基线，不新增官方性结论。
- siblings：16 个条目；4 个 safetensors。 权重提交窗前；本期只记热度
- 可复查：[HF 页面](https://huggingface.co/speridlabs/idol) · [文件树](https://huggingface.co/speridlabs/idol/tree/main) · [提交历史](https://huggingface.co/speridlabs/idol/commits/main)。

- 最近提交：2026-10-30 02:17:36 Asia/Singapore，`README: GPU sweep from the research page (RTX 3080 and L4 added, RTX PRO rows dropped); model details before Benchmark`（仓库级；是否权重变更以本文单独核验为准）。

**待核 / 建议**：本期未新增实测，若要使用仍需读完整许可与版本差异。

###### ricursiveAI/Ripple-65B-Preview
本期只用于去重或延续热度，不作为新发布推荐。

**来源记录**
- HF ID：`ricursiveAI/Ripple-65B-Preview`（models API；[实时元数据](https://huggingface.co/api/models/ricursiveAI/Ripple-65B-Preview)）。
- createdAt：2026-11-04 10:41:21 Asia/Singapore。
- lastModified：2026-11-07 03:26:32 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**403 / 5,087**；采集：2026-11-09 09:19:55 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**apache-2.0**；pipeline：**未标 pipeline_tag**；gated：`False`。
- 开放度：开放权重，Apache-2.0（OSI认可许可证）。
- 官方身份 / 来源：ricursiveAI作者org；本期只核提交变化，官方发布身份沿用已核官网链。
- siblings：31 个条目；16 个 safetensors。 16片权重tree最后提交2026-11-04 10:42:18Asia/Singapore /02:42:18UTC；窗内无新片
- 可复查：[HF 页面](https://huggingface.co/ricursiveAI/Ripple-65B-Preview) · [文件树](https://huggingface.co/ricursiveAI/Ripple-65B-Preview/tree/main) · [提交历史](https://huggingface.co/ricursiveAI/Ripple-65B-Preview/commits/main)。

- 最近提交：2026-11-07 03:26:32 Asia/Singapore，`Fix explicit position_ids generation on Transformers 4 (#8)`（仓库级；是否权重变更以本文单独核验为准）。

**待核 / 建议**：本期未新增实测，若要使用仍需读完整许可与版本差异。

###### nvidia/simready-assets
本期只用于去重或延续热度，不作为新发布推荐。

**来源记录**
- HF ID：`nvidia/simready-assets`（datasets API；[实时元数据](https://huggingface.co/api/datasets/nvidia/simready-assets)）。
- createdAt：2026-06-29 23:38:26 Asia/Singapore。
- lastModified：2026-11-05 04:49:04 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**1,485 / 1,434,099**；采集：2026-11-09 09:19:56 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**cc-by-4.0**；pipeline：**未标 pipeline_tag；task_categories=[]**；gated：`False`。
- 开放度：公开数据，CC-BY-4.0；不作模型OSI分类。
- 官方身份 / 来源：nvidia官方组织；物理仿真资产集，不是语言模型。
- siblings：100,000 个条目；数据文件清单已保存（不是模型权重）。 API siblings返回100,000条，可能达到返回上限，不宣称完整总文件数
- 可复查：[HF 页面](https://huggingface.co/datasets/nvidia/simready-assets) · [文件树](https://huggingface.co/datasets/nvidia/simready-assets/tree/main) · [提交历史](https://huggingface.co/datasets/nvidia/simready-assets/commits/main)。

- 最近提交：2026-11-05 04:49:04 Asia/Singapore，`Update README.md`（仓库级；是否权重变更以本文单独核验为准）。

**待核 / 建议**：本期未新增实测，若要使用仍需读完整许可与版本差异。

###### Qwen/Qwen3.8-27B
本期只用于去重或延续热度，不作为新发布推荐。

**来源记录**
- HF ID：`Qwen/Qwen3.8-27B`（models API；[实时元数据](https://huggingface.co/api/models/Qwen/Qwen3.8-27B)）。
- createdAt：2026-08-05 16:22:59 Asia/Singapore。
- lastModified：2026-11-07 12:42:17 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**19,416 / 7,668,187**；采集：2026-11-09 09:19:56 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**apache-2.0**；pipeline：**image-text-to-text**；gated：`False`。
- 开放度：开放权重，Apache-2.0（OSI认可许可证）。
- 官方身份 / 来源：Qwen官方组织；也是Arete与DSpine目标/基座来源。
- siblings：32 个条目；18 个 safetensors。 本窗response template/generation tags提交，不作权重更新证据
- 可复查：[HF 页面](https://huggingface.co/Qwen/Qwen3.8-27B) · [文件树](https://huggingface.co/Qwen/Qwen3.8-27B/tree/main) · [提交历史](https://huggingface.co/Qwen/Qwen3.8-27B/commits/main)。

- 最近提交：2026-11-07 12:42:17 Asia/Singapore，`Add a response template and generation tags (#236)`（仓库级；是否权重变更以本文单独核验为准）。

**待核 / 建议**：本期未新增实测，若要使用仍需读完整许可与版本差异。

###### openbmb/MiniCPM-OCR-1.0
本期只用于去重或延续热度，不作为新发布推荐。

**来源记录**
- HF ID：`openbmb/MiniCPM-OCR-1.0`（models API；[实时元数据](https://huggingface.co/api/models/openbmb/MiniCPM-OCR-1.0)）。
- createdAt：2026-10-21 23:51:40 Asia/Singapore。
- lastModified：2026-11-09 01:07:22 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**452 / 69,204**；采集：2026-11-09 09:19:56 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**apache-2.0**；pipeline：**image-text-to-text**；gated：`False`。
- 开放度：开放权重，Apache-2.0（OSI认可许可证）。
- 官方身份 / 来源：openbmb官方组织。
- siblings：14 个条目；1 个 safetensors。 本窗README/中文卡面变更
- 可复查：[HF 页面](https://huggingface.co/openbmb/MiniCPM-OCR-1.0) · [文件树](https://huggingface.co/openbmb/MiniCPM-OCR-1.0/tree/main) · [提交历史](https://huggingface.co/openbmb/MiniCPM-OCR-1.0/commits/main)。

- 最近提交：2026-11-09 01:07:22 Asia/Singapore，`Chinese model card: remove leftover GitHub model-guide links and hero image (#16)`（仓库级；是否权重变更以本文单独核验为准）。

**待核 / 建议**：本期未新增实测，若要使用仍需读完整许可与版本差异。

###### Pika-Labs/Pika-H3-Flex
本期只用于去重或延续热度，不作为新发布推荐。

**来源记录**
- HF ID：`Pika-Labs/Pika-H3-Flex`（models API；[实时元数据](https://huggingface.co/api/models/Pika-Labs/Pika-H3-Flex)）。
- createdAt：2026-10-30 01:08:44 Asia/Singapore。
- lastModified：2026-11-08 05:24:24 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**516 / 1,083**；采集：2026-11-09 09:19:56 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**other / minimax-h3-community-license-agreement**；pipeline：**image-to-video**；gated：`False`。
- 开放度：开放权重，自定义许可other；不作OSI开源结论。
- 官方身份 / 来源：Pika-Labs作者组织。
- siblings：96 个条目；23 个 safetensors。 本窗library_name元数据变更
- 可复查：[HF 页面](https://huggingface.co/Pika-Labs/Pika-H3-Flex) · [文件树](https://huggingface.co/Pika-Labs/Pika-H3-Flex/tree/main) · [提交历史](https://huggingface.co/Pika-Labs/Pika-H3-Flex/commits/main)。

- 最近提交：2026-11-08 05:24:24 Asia/Singapore，`Set library_name to pika-h3-flex for download counting; keep diffusers as a tag`（仓库级；是否权重变更以本文单独核验为准）。

**待核 / 建议**：本期未新增实测，若要使用仍需读完整许可与版本差异。

###### pfnet/plamo-3-translate-0.8b
本期只用于去重或延续热度，不作为新发布推荐。

**来源记录**
- HF ID：`pfnet/plamo-3-translate-0.8b`（models API；[实时元数据](https://huggingface.co/api/models/pfnet/plamo-3-translate-0.8b)）。
- createdAt：2026-10-27 14:58:53 Asia/Singapore。
- lastModified：2026-11-08 14:20:22 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**24 / 1,431**；采集：2026-11-09 09:20:35 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**other / plamo-community-license**；pipeline：**translation**；gated：`False`。
- 开放度：开放权重，自定义PLaMo Community License，非OSI。
- 官方身份 / 来源：PFN11/05官方公告反链此精确HF仓。
- siblings：16 个条目；1 个 safetensors。 11/04UTC初始权重；窗内chat template变更/回退
- 可复查：[HF 页面](https://huggingface.co/pfnet/plamo-3-translate-0.8b) · [文件树](https://huggingface.co/pfnet/plamo-3-translate-0.8b/tree/main) · [提交历史](https://huggingface.co/pfnet/plamo-3-translate-0.8b/commits/main)。

- 最近提交：2026-11-08 14:20:22 Asia/Singapore，`Revert the chat template to the previous version (drop target_lang=auto)`（仓库级；是否权重变更以本文单独核验为准）。

**待核 / 建议**：本期未新增实测，若要使用仍需读完整许可与版本差异。

###### pfnet/plamo-3-translate-31b
本期只用于去重或延续热度，不作为新发布推荐。

**来源记录**
- HF ID：`pfnet/plamo-3-translate-31b`（models API；[实时元数据](https://huggingface.co/api/models/pfnet/plamo-3-translate-31b)）。
- createdAt：2026-10-26 16:41:09 Asia/Singapore。
- lastModified：2026-11-08 14:21:02 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**23 / 501**；采集：2026-11-09 09:20:35 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**other / plamo-community-license**；pipeline：**translation**；gated：`False`。
- 开放度：开放权重，自定义PLaMo Community License，非OSI。
- 官方身份 / 来源：PFN11/05官方公告反链此精确HF仓。
- siblings：30 个条目；14 个 safetensors。 11/04UTC初始权重；窗内chat template变更/回退
- 可复查：[HF 页面](https://huggingface.co/pfnet/plamo-3-translate-31b) · [文件树](https://huggingface.co/pfnet/plamo-3-translate-31b/tree/main) · [提交历史](https://huggingface.co/pfnet/plamo-3-translate-31b/commits/main)。

- 最近提交：2026-11-08 14:21:02 Asia/Singapore，`Revert the chat template to the previous version (drop target_lang=auto)`（仓库级；是否权重变更以本文单独核验为准）。

**待核 / 建议**：本期未新增实测，若要使用仍需读完整许可与版本差异。

###### nvidia/Cosmos3-Edge
本期只用于去重或延续热度，不作为新发布推荐。

**来源记录**
- HF ID：`nvidia/Cosmos3-Edge`（models API；[实时元数据](https://huggingface.co/api/models/nvidia/Cosmos3-Edge)）。
- createdAt：2026-07-02 05:54:04 Asia/Singapore。
- lastModified：2026-09-17 02:48:41 Asia/Singapore。这是仓库修改时刻，不自动等于权重发布。
- likes / downloads：**239 / 60,396**；采集：2026-11-09 09:19:56 Asia/Singapore。downloads 为 HF API 统计口径，非本窗新增下载。
- license：**other / openmdw1.1-license**；pipeline：**未标 pipeline_tag**；gated：`False`。
- 开放度：开放权重，自定义other；具体许可证细节本期未深审，OSI状态不下结论。
- 官方身份 / 来源：nvidia官方组织；本期不采用媒体新发日期。
- siblings：54 个条目；4 个 safetensors。 lastModified在9月，权重更新提交在8月，均窗外
- 可复查：[HF 页面](https://huggingface.co/nvidia/Cosmos3-Edge) · [文件树](https://huggingface.co/nvidia/Cosmos3-Edge/tree/main) · [提交历史](https://huggingface.co/nvidia/Cosmos3-Edge/commits/main)。

- 最近提交：2026-09-17 02:48:41 Asia/Singapore，`docs: scope model versions and parameter list to Cosmos3-Edge`（仓库级；是否权重变更以本文单独核验为准）。

**待核 / 建议**：本期未新增实测，若要使用仍需读完整许可与版本差异。

##### 八、采集范围、缺口与交付验证

- HF：Trending HTML两页 + models API前300、datasets API前100，保留trendingScore；HTML可见顺序与API相符。模型rank是未过滤原榜名次，不是本稿评选名次。
- 机构扫描：`orglist.txt`列出最初62个author查询，按`/api/models?author=X&sort=lastModified&limit=30`；补pfnet与Ornith，OpenMOSS-Team再核一次。含Qwen、Moonshot、DeepSeek、Meta、Mistral、MiniMax、腾讯、NVIDIA、Nous、字节、微软、Google等。大小写/别名存在重复，不能将查询数称为同等数量独立机构。每org仅最近30条，未保证全量历史覆盖。
- 所有窗口候选保留`org_window_cands.json`（补查org原始响应在orgs/）；检查本窗提交标题，再对主条/重要候选用siblings和tree.lastCommit核权重。对README-only / 模板-only按规则降权；提交标题不是完整diff，仅重要项文件级补证。
- Kimi官方博客、主条官方项目页均本期读取并保存；未抓取登录后内容、未下载TB权重、未实测模型或复算数据集全量行数。
- AA完整图像榜HTML、解析全表和差异JSON已存；LMArena通过WebFetch取得完整响应，但本地仅手工保留选行快照，已显式标明范围，不能冒充完整可重放全榜。11/06文本/视觉基线本身也不完整，故不编造完整新增名单。
- 新发仓：createdAt/真实权重提交都在窗内；旧仓公开发布可能晚于createdAt，公开可见时刻不从createdAt猜。TwIL明确保留时间线冲突，Kimi只追踪不重复发布。
- 数据许可缺口：Cola2权重、Sage、Arete训练集；自定义/非商用许可与OSI认可软件许可证严格分开。OpenMDW正式OSI审批状态未获得权威最终名单确认。
- 数字口径：模型卡/论文自报分数一律待核，AA / LMArena系第三方榜单，不是本次实测；不同版本、harness、推理档位不横比。
- `final_verify.json`：只验证本稿实际出现的HF model/dataset精确ID，分别调用models/datasets API；每项HTTP200、时间、证据路径与响应hash落盘。详细结果见该文件。`link_check.json`记录正文具体外链及HTTP状态；错误/不可读不推断不存在。

###### 本次验证结果

- 本文精确HF ID共 **21**：models **16**、datasets **5**（其中数据集新条4 + 延续1）；**21/21 API HTTP200**，原始响应在（采集证据快照），哈希/采集时间在`final_verify.json`。
- 正文外链 **111** 个：106次HTTP200；3个LMArena链接curl403但WebFetch本期完整可读；AA文生图复验SSL EOF但本期先前HTTP200且完整108行HTML已存；1个audnai提交历史401（限制已明确）。**未发现404**；不把传输/鉴权错误当页面不存在。
- 主要机构扫描没有证明“全行业没有新模型”；只说明在本次author×最近30条和Trending范围内，筛出本文4主条与2次级。
- 两份交付文件SHA256与字节一致性由独立`delivery_manifest.json`记录，避免在正文嵌入自身哈希。

