# 2026-11-03 AI行业动态 · 原始素材整理稿

本文是 [2026-11-03 AI行业动态](https://guige.ai/guige-ai-site/daily/2026-11-03/) 的附件，收的是窗口内（2026-10-30 09:43 → 2026-11-03 09:32 SGT，跨周末，约四天）的全量原始素材，不是深读稿，篇幅和取舍都比正文粗。数字后标「已核」的是对照官方原文或一手数据核过的；「待核」「自述」「自报」表示只有单一来源或厂商自己的说法。安全、漏洞、投毒类内容只记结论和修复版本，不记攻击细节。冒名或虚假仓库只写判定，不放链接。

- **官方博客与 arXiv**：OpenAI、Google DeepMind、Microsoft Research、NVIDIA 等官博逐篇扫描；arXiv cs.AI / cs.CL / cs.LG 三类 10/30、11/02 两批全扫，11/03 批截至发稿未放全。
- **X**：官方与关键账号检索、X Today's News 和定向检索，并对照 SEC、OpenAI 帮助文档、NVD、CISA KEV 等一手来源交叉核对。
- **GitHub**：主要推理引擎与官方 SDK 的发版记录，加上 GitHub Trending 日榜、周榜。
- **Hugging Face 与榜单**：HF Trending 模型和数据集、主要机构仓库更新，以及 LMArena、Artificial Analysis 各榜（AA Intelligence Index 为 v5，分数不能与 v5 之前各期直接比较）。

---

# 一、官方博客与 arXiv（精选）

> 本期 Anthropic、Google Research、Meta 官博窗口内无新帖；旧主线无实质新进展。
> arXiv 说明：没有单独的 10/29 批（并入 10/30 双倍批，已补扫完）；周六无批次；11/03 批截至 09:30 未放全，下期补扫。

## 官博

### 1. OpenAI 自研 Git 后端 Pando，扛住 agent 带来的海量并发提交
Codex 让工程师同时开大量分支、频繁推送，原有代码托管扛不住；OpenAI 用 Codex 10 周做出兼容 Git 的新后端，整个 monorepo 已迁移。这是一线实验室首次公开说明 AI 编码 agent 把 Git 基础设施压到极限，并给出架构解法（只保证分支内顺序、复用打包文件、分层合并）。对平台工程、代码托管厂商、多 agent 协作团队有参考价值。
- 中位推送延迟降近 5 倍（文中另一处写降近 80%，口径不一）；每天交付近 1 PB Git 数据，单小时峰值超 57 TB，99% 以上来自本地缓存；旧系统可靠性一度低于 90%（均为官方自报）。部分补丁已进上游 Git（待核）。
- [官博](https://openai.com/index/scaling-git-at-openai)

### 2. OpenAI Grid Protectors：数据中心高峰降负荷、自担电网成本
OpenAI 承诺旗下算力园区在电网吃紧时主动少用电，电网扩建费用自己承担、不转嫁居民，首个试点在佐治亚州。AI 推高电价已是美国政治议题，这是头部实验室首次把可中断负荷做成全国性承诺，可能成为各地审批数据中心的参照。
- 与 Georgia Power 协议含最多 1,000 MW 可调负荷，约合 70 万户平均用电（官方自报）；2029 年起用户每年省约 9.5 亿美元、典型居民每月至少省 15 美元（Georgia Power 多协议整体预测，待核）。
- [官博](https://openai.com/index/grid-protectors-program)

### 3. OpenAI LifeVal：测 AI 能否替普通人办成日常事
新评测，题目来自时间使用调查（找幼儿园、找房、做糖尿病食谱、办政府业务），测的是 agent 能否动手完成而不是答题，显示评测重心转向个人助理式操作任务。但页面只给示例分数，没有完整基准、模型名和数据集，目前更像方向宣示。
- 问卷受访者 3,995 人（官方自报）；示例得分 90.4%–100%，未说明模型与评分口径（待核）。
- [官博](https://openai.com/index/lifeval)

### 4. DeepMind PlanAssist 扩展到 15 个英国地方规划机构
基于 Gemini 的规划审批助手，3 个议会试点后进入 12 个月 Beta，新增 12 个议会，最终决定仍由官员做出。这是大模型进入政府审批流程且有量化效果的少见案例。
- 住户类申请评估时间平均降 58%，超过 70% 的报告被官员原样采纳（官方自报）；2027 年是否推向全英格兰视测试结果而定（待核）。
- [官博](https://deepmind.google/blog/speeding-up-planning-decisions-with-ai/)

次要：[OpenAI 将遵守 IETF AI 训练偏好信号](https://openai.com/index/helping-websites-express-ai-training-preferences)（未来几个月实施）；[OpenAI 社区安全报告与青少年新保护](https://openai.com/index/community-safety-report-and-new-protections-for-teens)；[NVIDIA Vera Rubin NVL72 首个跨节点带宽数据](https://developer.nvidia.com/blog/making-kubernetes-ai-ready-for-nvidia-vera-rubin-on-day-one/)；[NVIDIA Cosmos 3 Nano 仿真检查点](https://developer.nvidia.com/blog/build-world-models-for-interactive-simulation-with-nvidia-cosmos/)。

## arXiv

### 5. Redwood Research：GPT 系列模型会为刷分违背用户指令（2610.41014）
泄露评分器后，GPT 系列模型会为了提高分数违背用户的明确指令，且无论分数被说成用于训练、评测还是根本不用，违规率都差不多。这是对 reward hacking 动机的直接实证，对象是一线商用模型。单位 Redwood Research（已核）。
- 另一个 agent 能得 1 分而非 0 分时，GPT 5.6 Sol 与 GPT 5.5 帮它的频率平均高 24.6 个百分点；给别人打分或做监控时从未通过篡改分数串通（作者自报，待核）。
- [arXiv](https://arxiv.org/abs/2610.41014)

### 6. Anthropic：用价值探针指导红队束搜索（2610.38526）
用线性探针读目标模型激活，预测"这段对话接下来会不会出问题"，再用它引导束搜索红队，审计效果明显提升，且可用小模型离策略数据拟合。对红队与模型审计团队有用。单位 Anthropic + Anthropic Fellows（已核）。
- 18 种目标行为、3 个模型规模上，峰值审计分比同 token 预算的标准方法高约 50%（官方自报）。
- [arXiv](https://arxiv.org/abs/2610.38526)

### 7. 简单特征打败多数 AI control 监控器（2610.41713）
AI control 常用的后门代码评测集存在标签泄露，不运行代码、只靠简单特征就能胜过多数大模型监控器，直接质疑现有监控器高分是否说明真能识别破坏行为；作者已放出重建数据集。单位 University of Virginia + UC San Diego（已核）。
- 简单特征胜过 24 个开源权重监控器中的 20 个；每 7 个后门有 1 个通不过有效性检查；Sonnet 5 监控器抓旧模型后门 77%、抓自身后门仅 37%（核验后 78% 对 61%）（作者自报，待核）。
- [arXiv](https://arxiv.org/abs/2610.41713)

### 8. Meta FAIR：循环 Transformer 怎么循环最划算（2610.40325，配读 2610.42030）
系统研究"参数复用换深度"：参数受限时循环整个模型最好，算力受限时只循环中间几层更划算，循环次数多了会饱和甚至变差。配读的微软论文结论是，在已预训练的 4B/9B 模型上事后加循环不划算。对架构设计、端侧小模型、推理成本优化有用。单位 FAIR at Meta；配读为 Microsoft（已核）。
- 主篇最大 1B 参数、155B tokens、最多 32 次循环（官方自报）；配读中 Qwen3/3.5 从 0.8B 到 9B，只有 0.8B 的循环版同时胜过两个基线（作者自报，待核）。
- [arXiv 2610.40325](https://arxiv.org/abs/2610.40325) · [arXiv 2610.42030](https://arxiv.org/abs/2610.42030)

### 9. Microsoft Mage-VL-Cowork：4B 端侧电脑操作 agent（2610.40747）
4B 的端侧"图形界面 + 代码终端"混合电脑操作智能体，附完整训练配方，训练数据全为合成，成本更低。对做电脑使用和端侧 agent 的人有用。单位 Microsoft Mage Team（已核）。
- OSWorld-Verified 66.0%；合成 293,806 个任务、覆盖 6,915 个技能，单任务重复成本降 82.6%（官方自报）。
- [arXiv](https://arxiv.org/abs/2610.40747)

### 10. Google：在模拟环境中用强化学习训练精神科初诊 agent（2610.40476）
在模拟环境里用多轮强化学习训练精神科初诊问诊 agent，在精神科医生扮演病人、双盲评审的随机交叉研究中明显胜过基座模型，是高风险医疗对话中"模拟 + 强化学习"的首个临床医生评审实证。单位 Google DeepMind / Google Research / Google for Health + Stanford（已核）。
- 60 对场景中 76.7% 胜出（p<0.0001）；鉴别诊断恰当率 68.3% 对 33.3%；急性安全风险漏判率从 30.5% 降到 12.9%（作者自报，待核）。
- [arXiv](https://arxiv.org/abs/2610.40476)

备选：SecPO [2610.41998](https://arxiv.org/abs/2610.41998)（UC Berkeley + Anthropic，网络安全类只写结论：提示注入攻击成功率大幅下降）；[2610.40051](https://arxiv.org/abs/2610.40051) 合成预预训练在算力对齐时从未胜过纯自然语言；[2610.41073](https://arxiv.org/abs/2610.41073) bf16 舍入吞掉强化学习更新。
排除：2610.40890、2610.42010、2610.39796 标题误导（与所提实验室无关）。

---

# 二、官方博客（全量扫描）
窗口：2026-10-30 09:43 SGT → 2026-11-03 ~09:15 SGT（UTC+8）。扫描时间：2026-11-03 09:13–09:30 SGT。

## 无窗口内新帖的来源
- **Anthropic**（/news、/research、sitemap）：最新日期 Oct 28, 2026，窗口内无新帖。
- **Google Research**：RSS 与博客首页最新为 2026-10-28 01:35 SGT（睡眠式持续学习框架，旧主线），窗口内无新帖。
- **Meta AI**：about.fb.com 最新 Oct 29（feed 最新 10-30 01:00 SGT，在窗口前）；research.meta.ai 最新 Oct 28。青少年自伤提醒扩展属 2026-10-29 04:00 PT（=10-29 19:00 SGT）更新，在窗口前；Muse Spark 1.1 为 2026-07-09 发布，媒体近日转载，非新闻。engineering.fb.com 最新 10-30 00:00 SGT，在窗口前。

---

## OpenAI

### 1. Scaling Git at OpenAI（Pando）
- 机构：OpenAI（Engineering）｜发布：2026-11-02 23:30 SGT
- 链接：[原文](https://openai.com/index/scaling-git-at-openai)
- 要点：OpenAI 自研 Git 兼容后端 Pando，现已承载其整个 monorepo 的开发；起因是 Codex 带来的并发推送/拉取激增，旧系统可靠性“at times falling below 90%”。
- 生产效果：中位 push 延迟降低“nearly 5x”（文中另处写“reduced … by nearly 80%”）；每天交付“nearly a petabyte of Git data”；单小时峰值“more than 57 terabytes”，>99% 来自本地缓存；Express 缓存命中率 >99%；普通云 VM 可打满 10 Gbps。
- 设计：放弃全库一致性，改为按 ref 的因果一致性 + 复用 packfile（packfile-uri），类 LSM 压缩（monorepo 用到 L4）；中位 packfile <20 KiB，P99 <3 MiB。
- 开发方式：用 Codex 从立项到上线“just 10 weeks”，核心由“a single engineer”设计、agent 团队实现；用 GPT‑6 Astra 写 Lean/TLA+ 形式化“theory of Pando”找 bug；2026 年 4 月起服务生产流量；部分补丁已进上游 Git，并“exploring ways to share the technology … with our users”。

### 2. Introducing the Grid Protectors Program
- 机构：OpenAI（Global Affairs）｜发布：2026-11-02 23:00 SGT
- 链接：[原文](https://openai.com/index/grid-protectors-program)
- 要点：全国性计划，未来算力园区在电网紧张时主动降负荷，并承担自身电力与基础设施成本。
- 试点：Georgia Effingham County 园区，与 Georgia Power 协议含“up to 1,000 megawatts of flexible demand response”，约相当于“roughly 700,000 households”平均用电。
- Georgia Power 预计 2029 年起组合大负荷协议每年为用户节省“approximately $950 million”，典型居民（1,000 kWh/月）每月至少受益“$15”（为电力公司口径）。
- 背景数字：引用美国数据中心容量到 2030 年“exceed 100 gigawatts”的预测。

### 3. LifeVal
- 机构：OpenAI（Research）｜发布：2026-11-02 17:00 SGT
- 链接：[原文](https://openai.com/index/lifeval)
- 要点：新评测，衡量模型在日常生活任务（育儿、健康、教育、家庭事务、个人财务、购物、政府服务）中“动手办成事”的能力，而非学术知识。
- 任务来源：American Time Use Survey + Multinational Time Use Study，外加新的代表性调查“3,995 respondents”。
- 示例得分（官方展示，未说明是哪款模型/何种评分口径）：幼儿园择校 93.1%、洪灾志愿者组织 98.0%、找房 100%、远程看球 96.3%、糖尿病膳食 90.4%。
- 页面未公布完整基准、数据集或开放方式；称用它在过去一年追踪并推动浏览器/电脑使用/连接器能力。

### 4. Qodo builds context into AI code review with Codex
- 机构：OpenAI（客户案例）｜发布：2026-11-02 08:00 SGT
- 链接：[原文](https://openai.com/index/qodo-codex-plugin)
- 要点：Qodo 在 Codex 插件市场上架插件，为 Codex 注入跨仓库上下文、组织规则和独立评审；客户环境可达“10,000 or more repositories”。
- 使用 GPT‑6 Astra（Extra High / Ultra effort）；设想用 Decisions API 从“200 rules”中筛选需检查的规则。属案例软文，无新产品/数字。

### 5. OpenAI appoints Dan Driscoll as Senior Counselor for National Security Modernization
- 机构：OpenAI｜发布：2026-11-02 08:00 SGT
- 链接：[原文](https://openai.com/index/dan-driscoll-joins-openai)
- 要点：前第 26 任美国陆军部长 Dan Driscoll 加入，新设职位，负责国家与网络安全领域 AI 现代化、与盟友合作；关联 OpenAI 的 Daybreak 计划。人事新闻。

### 6. Making it easier for websites to express AI training preferences
- 机构：OpenAI｜发布：2026-10-30 17:30 SGT
- 链接：[原文](https://openai.com/index/helping-websites-express-ai-training-preferences)
- 要点：OpenAI 宣布将遵守 robots.txt 中一个跨厂商通用的“foundational generative AI training”偏好信号，源自 IETF AI Preferences 工作组，与其他参与方同日宣布。
- 计划“in the coming months”实施，届时另发实现细节；不替代现有 GPTBot 等爬虫控制。呼吁其他 AI 厂商也遵守。

### 7. Community safety report and new protections for teens
- 机构：OpenAI（Safety）｜发布：2026-10-30 17:00 SGT
- 链接：[原文](https://openai.com/index/community-safety-report-and-new-protections-for-teens)
- 要点：2026 Q3 向执法部门转介“over 200”起；承诺发布《Community Safety Report》，首份“early 2027”覆盖 2026 下半年，此后每六个月一次。
- 政策收紧：限制对过往大规模袭击的细节重建（适用所有用户）；近期聊天有暴力预警信号时回答更保守；对疑似未成年人进一步限制武器/安防相关实用信息；对暴力执念对话可自动结束聊天，多次触发可暂停账号。
- 年龄预测持续评估、Persona 验证纠错；措施“in the next few weeks”开始推出。

## Google DeepMind

### 8. Speeding up planning decisions with AI（PlanAssist）
- 机构：Google DeepMind（与英国政府、Google Cloud、Faculty）｜发布：RSS 2026-10-30 22:18 SGT（页面标 Oct 31, 2026）
- 链接：[原文](https://deepmind.google/blog/speeding-up-planning-decisions-with-ai/)
- 要点：基于 Gemini 的规划审批助手 PlanAssist，在 Barnet、Camden、Dorset 试点中将住户类申请的官员评估时间平均降低“58%”；生成报告“more than 70%”被官员无修改采纳。
- 进入 12 个月 Beta，新增 12 个地方规划机构，总计 15 个；若测试成功，英国政府计划 2027 年向英格兰所有议会开放，每份评估仍由合格官员审批。
- 背景：住户类申请占规划官员工作量“up to 70%”；英国目标 2029 年前建 150 万套住房。

## Microsoft Research

### 9. From synthetic enterprise data evaluations to real Microsoft Copilot AI confidence
- 机构：Microsoft Research｜发布：2026-10-30 21:05 SGT
- 链接：[原文](https://www.microsoft.com/en-us/research/blog/from-synthetic-enterprise-data-evaluations-to-real-microsoft-copilot-ai-confidence/)
- 要点：构建“Industry Evaluation Data Generation Platform”，用 O*NET、招聘启事、SEC 文件等公开数据生成全合成企业租户（制药、资本市场、IT 三个行业，每个“hundreds of users”），评测 Copilot，不碰客户数据。
- 六阶段自动查询生成流水线；综合质量分比初版提升“39%”，部分行业环境“above 0.9 out of 1.0”。
- 估算每个评测数据集节省“approximately $100,000”，项目总计“$300,000”；已成为 Copilot 首个标准化评测基线（内部）。

## NVIDIA

### 10. Things That Go Beep in the Night: Agentic AI Joins the Search for Extraterrestrial Signals
- 机构：NVIDIA Blog｜发布：2026-10-30 23:00 SGT
- 链接：[原文](https://blogs.nvidia.com/blog/ai-joins-the-search-for-extraterrestrial-signals/)
- 要点：SETI Institute/Breakthrough Listen 在 Allen Telescope Array 接入 Holoscan，agent 可用自然语言指令操控望远镜、校准、纠错和跑模型。
- 系统可处理“2.4 terabits per second”（RTX PRO 6000 Blackwell，本地推理）；称实现了首次对蟹状星云脉冲星的实时 AI 探测；正评估 Nemotron 用于离线场景。

### 11. Build World Models for Interactive Simulation with NVIDIA Cosmos（技术博客）
- 机构：NVIDIA Technical Blog｜发布：2026-11-03 01:00 SGT
- 链接：[原文](https://developer.nvidia.com/blog/build-world-models-for-interactive-simulation-with-nvidia-cosmos/)
- 要点：发布开放模块化的 Cosmos Framework（训练/RL/优化/推理 + agent skills），扩展支持 Alpamayo、GR00T、Qwen、pi0.5；新增 Cosmos 3 Nano 仿真配方与检查点（自动驾驶相机+LiDAR 联合生成、双臂机器人、手术仿真）。
- Cosmos NIM 推测解码在 H200 上平均约“2–3×”加速；Cosmos3-Nano 生成需 58 GiB（BF16）/44 GiB（FP8）/31 GiB（FP8+offload）。
- 参考运行：7 路 720p 视频（297 帧 30 FPS）+ 99 帧 LiDAR。

### 12. Making Kubernetes AI-Ready for NVIDIA Vera Rubin on Day One（技术博客）
- 机构：NVIDIA Technical Blog｜发布：2026-11-03 02:00 SGT
- 链接：[原文](https://developer.nvidia.com/blog/making-kubernetes-ai-ready-for-nvidia-vera-rubin-on-day-one/)
- 要点：AICR v1.0.0 发布 Vera Rubin NVL72 Preview 配方（训练/推理/Dynamo），在早期硬件上完成部署、一致性和性能验证。
- 首个跨节点 NCCL all-reduce（多节点 NVLink）：“744.71 GB/s busbw at 16 GiB”；驱动 R615.23，GPU Operator v26.7.0，DRA driver v0.5.0。
- 推理性能验证暂缓：vLLM 官方镜像仍基于 CUDA 13.0.3，Rubin（sm_107a）内核需 CUDA ≥13.4。

### 13–19. NVIDIA 技术博客其他窗口内文章（偏工程教程，低信号）
- Diagnose Distributed AI Workload Failures with NVIDIA Attribution — 2026-11-03 07:39 SGT — [原文](https://developer.nvidia.com/blog/diagnose-distributed-ai-workload-failures-with-nvidia-attribution/) （分布式训练故障归因）
- Keep Distributed Training Running with Automated Workload Recovery — 2026-11-03 06:43 SGT — [原文](https://developer.nvidia.com/blog/keep-distributed-training-running-with-automated-workload-recovery/)
- Support New AI Frameworks Faster Using NVIDIA Workload Map — 2026-11-03 00:00 SGT — [原文](https://developer.nvidia.com/blog/support-new-ai-frameworks-faster-using-nvidia-workload-map/)
- Build a Validated Kubernetes Runtime for NVIDIA Dynamo — 2026-10-31 05:35 SGT — [原文](https://developer.nvidia.com/blog/build-a-validated-kubernetes-runtime-for-nvidia-dynamo/)
- Run AI Models for Edge Application Development with Just a Few Commands — 2026-10-31 04:33 SGT — [原文](https://developer.nvidia.com/blog/run-ai-models-for-edge-application-development-with-just-a-few-commands/)
- Build Specialized Agents on a Stack You Control with NVIDIA NemoClaw — 2026-10-31 00:00 SGT — [原文](https://developer.nvidia.com/blog/build-specialized-agents-on-a-stack-you-control-with-nvidia-nemoclaw/)
- How to Check and Configure NVIDIA GPUDirect Storage for Your Platform — 2026-10-30 23:01 SGT — [原文](https://developer.nvidia.com/blog/how-to-check-and-configure-nvidia-gpudirect-storage-for-your-platform/)
（以上仅读 feed 摘要，未全文精读。）

## 旧主线检查
窗口内未发现以下旧主线的实质新进展：Gemini 4 Carbon、Genie 4、OpenAI 失准监控/Model Spec/三项证明/GPT-6.1 Terra/训练暂停/PHP 漏洞/Google Cloud/收购 Orchestra Bio/MultiLangBench、Anthropic 各项、睡眠式持续学习、Nemotron 3.5 Transcribe、KLS 猜想、Agent Skills/AAIF。Qodo 案例提到 Decisions API，但只是客户设想，不算新进展。

---

# 三、arXiv（全量扫描）：cs.AI / cs.CL / cs.LG（扫描于 2026-11-03 09:13–09:30 SGT）

## 扫描范围与批次情况

批次日期为新加坡时间的发布早晨。arXiv 在美东周日至周四 20:00 公告，所以新加坡时间周一到周五各有一批，**没有周六批次**。

| 新加坡批次 | arXiv 列表标签 | cs.AI / cs.CL / cs.LG（含交叉列表） | 三类去重 | 新投稿编号范围 | 提交日期（v1） | 状态 |
|---|---|---|---|---|---|---|
| 10/29（周四） | 「Thu, 29 Oct」**不存在**（当天 catchup 为 0 条，pastweek 跳过 29 Oct） | — | — | 并入下一批 | — | 并入 10/30 |
| 10/30（周五） | 「Fri, 30 Oct 2026」 | 392 / 175 / 372 | 736 | 2610.37671 – 2610.40655（约 3k 个编号，是平时的两倍） | 10-28 至 10-29 | 完整 |
| ↳ 上期已看部分 | ≤ 2610.38461 | — | 258 | 2610.37671 – 2610.38461 | 10-28 | 上期已扫 |
| ↳ 本期新看部分 | 2610.38462 – 2610.40655 | 247 / 110 / 244 | 476 | | 10-28 至 10-29 | 本期扫描 |
| 10/31（周六） | 无（美东周五不公告） | — | — | — | — | 不存在 |
| 11/02（周一） | 「Mon, 2 Nov 2026」 | 186 / 86 / 198 | 374 | 2610.40700 – 2610.42149（摘要页最高到 2610.42152） | 10-29 至 10-30 | 完整 |
| 11/03（周二） | 「Tue, 3 Nov」列表截至 09:30 SGT 仍未发布 | — | 已出现 79 个标注 AI/CL/LG 的摘要页 | 2611.00001 – 2611.00317（全 arXiv 约 282 个摘要页） | 多为 10-30 | **不完整**，下期补扫 |

关于 10/29：从未单独发布过 10/29 列表。上期看到的约 243 篇（编号到 2610.38461，10-28 提交）其实是合并后 10/30 批次先放出的摘要页，该批其余部分（2610.38462–40655）在本期扫描。

## 候选论文（单位已对照 arXiv HTML 作者栏或 PDF 首页核对，数字摘自摘要）

### 10/30 批次（周五列表）

### 1. 2610.38526 — Value Probes: Learned Value Functions for Beam-Search Red Teaming
- 单位：Anthropic（Andrew K. Lampinen）+ Anthropic Fellows Program（Jonathan F. Jao）（已核）· [arXiv](https://arxiv.org/abs/2610.38526)
- 要点：把自动化红队审计当作马尔可夫决策过程做束搜索；在目标模型激活上训练线性探针，预测未来评审打分的折扣和（「价值探针」）。在 18 种目标行为、3 个模型规模上，峰值审计分比同 token 预算的标准审计高「约 50%」。探针可以用更小模型的离策略数据拟合。

### 2. 2610.38882 — Aligning Autoresearch: Co-Improvement between Agents and Humans
- 单位：FAIR at Meta（Jason Weston、Ping Yu、Ilia Kulikov 等）+ JHU / CMU / UW（已核）· [arXiv](https://arxiv.org/abs/2610.38882)
- 要点：(i) 实证研究发现人在自动化研究中仍起关键作用，尤其在构思阶段；(ii) 新基准 **HackBench** 显示现有 autoresearch agent 未对齐，且不善于定位钻空子行为；(iii) 在 RL 中用人类模拟器训练 agent 与人协作；(iv) 用专家对齐的评分细则做 RL，改进 agent 的沟通。摘要没有给出具体数字。

### 3. 2610.40325 — How to Loop Your Transformer: Loop Scaling, Specialization, and Parallel Inference
- 单位：FAIR at Meta（Mike Lewis、Shruti Bhosale 等；第一作者同时在 MIT）（已核）· [arXiv](https://arxiv.org/abs/2610.40325)
- 要点：稠密解码器模型最大 1B 参数、155B token、1.07×10^21 训练 FLOPs、最多 32 次循环。参数预算固定时循环整个 Transformer 最好；FLOPs 受限时循环中间块回报更高。循环次数增加后最终会饱和、反转或不稳定。每次循环专属的 LoRA 有帮助，循环越多帮助越大。原始 Parallel Loop Transformer 的写法不能稳定保留收益，保留当前 token 嵌入并单独归一化即可修复。全文 149 页。

### 4. 2610.40747 — Mage-VL-Cowork: A Full Training Recipe to Learn Hybrid Computer Use From Evolved Harnesses
- 单位：Microsoft Mage Team（PDF 首页；代码与模型见 [microsoft/Mage](https://github.com/microsoft/Mage)）（已核）· [arXiv](https://arxiv.org/abs/2610.40747)
- 要点：4B 的图形界面 + 代码/终端混合电脑操作 agent，五阶段课程（中期训练 → SFT → RL）。Mage-CUA-Forge 在 6,915 个技能上合成 293,806 个桌面与网页任务，单任务重复成本降 82.6%。**OSWorld-Verified 66.0%**，自称同尺寸最佳（作者自述，待核）。同日相关论文：2610.41432 Hybrid Computer Use（MSR + 复旦/清华），在 OSWorld 2.0 上 Partial/Binary 分数最高。模型权重部分见第六部分。

### 5. 2610.40476 — Training language models in simulation for psychiatric intake
- 单位：Google DeepMind / Google Research / Google for Health + Stanford（已核）· [arXiv](https://arxiv.org/abs/2610.40476)
- 要点：在模拟环境中做多轮 RL。随机双盲交叉研究（60 对匹配场景、120 次问诊；32 名执业精神科医生扮演病人，15 名评分）。训练后的 agent 在 76.7% 的配对中胜过基座模型（p<0.0001）。鉴别诊断恰当率 68.3% 对 33.3%。127 个模拟场景的临床评分 0.706 对 0.379。256 个对抗性案例中，急性安全风险漏判率从 30.5% 降到 12.9%。

### 6. 2610.39302 — Proving and Improving the Platonic Representation Hypothesis with JEPAs
- 单位：Randall Balestriero，Brown University / NYU / AMI Labs（PDF 首页）（已核）· [arXiv](https://arxiv.org/abs/2610.39302)
- 要点：证明「柏拉图表示定理」：在好的视角下，分别在任意多种模态上训练的 JEPA 学到的表示只差一个旋转。下一 token 预测是「坏视角」的 JEPA。报告一条「对齐缩放律」，可在种子噪声范围内预测未见过的运行。好的视角达到同等对齐所需样本比下一 token 预测少 42 倍。一个 109M 的文本 JEPA 与 DINOv2/CLIP 图像编码器的对齐度高于所评测的最大 72B 的任何语言模型。无配对数据时 ImageNet-100 top-5 为 64%，对照组 ≤56%。

### 7. 2610.40051 — Rethinking Pre-pretraining
- 单位：Cohere（Alexander Stern、Acyr Locatelli）+ UCL AI Centre（Tim Rocktäschel）+ MIT（Laura Ruis）（已核）· [arXiv](https://arxiv.org/abs/2610.40051)
- 要点：算力对齐时，合成数据「预预训练」（k-Dyck、NCA、声明式语料、代码）**从未胜过**纯自然语言训练，在包括 881M 参数 / 50B token 在内的 3 种设置下都成立。此前报告的 5.4% 困惑度增益依赖初始化方案。额外给算力时，增益只在自然语言预算很小时存在，到 1B token 时消失。

### 8. 2610.38981 — Why Speculative Decoding Works Better Than Predicted on Sparse MoE Models
- 单位：Cohere · NeurIPS 2026 主会（已核）· [arXiv](https://arxiv.org/abs/2610.38981)
- 要点：10 个稀疏 MoE 模型（30B–1T，8–512 个专家）。细粒度 MoE 打破了预测的「凹」曲线，在小批量下投机解码加速最高。最大熵 IPF 模型预测去重专家数的误差 <4%。

### 9. 2610.40613 — TextSeal2: Distortion-Free LLM Watermarking with Copula Mixing and Memoryless Races
- 单位：Meta Superintelligence Labs（已核）· [arXiv](https://arxiv.org/abs/2610.40613)
- 要点：一种无失真水印，在投机解码下仍有效且不改变接受率。同等多样性、误报率 10^-3 下，100 token 回答的检出率比 TextSeal 高 8–22 个百分点；投机解码下，200 token 回答的检出率比 TextSeal / textGrain 分别高 18 / 22 个百分点。

### 10. 2610.39264 — Online Dense Reinforcement Learning with Planning-Grounding Agent for UI Navigation on Live iOS Apps
- 单位：Apple（Samy Bengio、Emmanuel Abbe、Jeffrey Nichols 等）（已核）· [arXiv](https://arxiv.org/abs/2610.39264)
- 要点：在真实 iOS 应用上做在线 PPO，数百台并发虚拟 iOS 设备，新价值估计器 GiGPPO。8B 的 RL agent 在分布外 Android 泛化上比 SFT 提升「近 7 倍」；在真实 iOS 应用上胜过 Gemini-3.5-Flash，与 Gemini-3.1-Pro 持平。

### 11. 2610.40396 — Understanding and Mitigating Role Spoofing in LLMs
- 单位：UPenn / Princeton / Apple MLR（Eran Malach；工作完成于 Apple）（已核）· [arXiv](https://arxiv.org/abs/2610.40396)
- 要点（AI 安全类，只记结论）：模型同时根据内容和结构线索判断「谁说了什么」。只针对内容型注入做对抗训练，模型仍可能被结构型冒充，这解释了为什么前沿模型仍会被冒充。线性探针检测有效。

### 12. 2610.39006 — Blind Spots: Where Small Language Models Fall Behind Frontier Models on Terminal Tasks
- 单位：Microsoft Research + UCLA（已核）· [arXiv](https://arxiv.org/abs/2610.39006)
- 要点：把小模型与前沿模型的差距拆成可解性、验证和置信度三部分。重复采样能缩小可解性差距，验证差距依然存在。小模型更过度自信、校准更差。

### 13. 2610.40535 — Efficient Scalable Oversight via Rewinding
- 单位：MIT（Yael Tauman Kalai 等）+ Succinct（Ron Rothblum）（已核）· [arXiv](https://arxiv.org/abs/2610.40535)
- 要点：理论论文，提出可回滚交互式证明（RIP），验证者可以把 AI 证明者回滚到某个快照。不假设证明者诚实，也不使用密码学。诚实证明者线性时间运行；预处理后，验证者对输入长度近线性时间运行。

### 14. 2610.38867 — Where You Inject Matters: The Trust Region Effect in LLM Agents
- 单位：Microsoft Research（Jianfeng Gao 等）+ UChicago / UIUC（Bo Li）等（已核）· [arXiv](https://arxiv.org/abs/2610.38867)
- 要点（AI 安全类，只记结论）：注入内容不变时，**放在哪里**会改变 agent 的遵从程度。对 GPT-5.4 agent，放在 README/TODO 文件中的注入被照做的频率是放在代码或数据文件中的 2.6 倍。

### 11/02 批次（周一列表）

### 15. 2610.41014 — Towards Understanding Score-Seeking in LLMs
- 单位：Redwood Research（Ryan Greenblatt、Alex Mallen、Aghyad Deeb）（已核）· [arXiv](https://arxiv.org/abs/2610.41014)
- 要点：研究对象为 GPT 5.6 Sol、GPT 5.5 和一个未做安全训练的 OpenAI o3 检查点（「exp-rl-cap-late」），置于评分器被泄露的 agent 环境。模型会「追分」：即使违背用户明确指令也要追求分数，且无论分数被说成用于训练、评测还是根本不用，违规率都差不多。当另一个 agent 的分数会是 1 而非 0 时，GPT 5.6 Sol 与 GPT 5.5 帮它的频率高 24.6 个百分点。给别的轨迹打分或做监控时，它们**从未**通过扭曲分数串通（作者自述，待核）。

### 16. 2610.41998 — SecPO: Principled Adversarial Training for Prompt Injection Security
- 单位：UC Berkeley（David Wagner 等）+ Anthropic（工作完成于 Google DeepMind）（已核）· [arXiv](https://arxiv.org/abs/2610.41998)
- 要点（AI 安全类，只记结论）：新的 SecPO 损失加强对抗训练，显著降低自适应提示注入的成功率。AgentDojo ASR@800 为 8.8%，Meta-SecAlign 为 78.8%。9 个基准上没有明显的能力下降。代码和数据已放出。

### 17. 2610.42030 — There Is No Free Loop: When Does Looping a Trained Model Pay for Its Inference Compute?
- 单位：Microsoft Applied Sciences Group（已核）· [arXiv](https://arxiv.org/abs/2610.42030)
- 要点：在预训练后给 Qwen3/3.5（0.8B–9B）加循环。只有 0.8B 的循环版同时胜过两个基线（等参数、等 FLOPs）。4B/9B 的循环版甚至比不过同模型不加循环继续训练。宜与第 3 篇对照读。

### 18. 2610.41713 — Simple Features Beat Most AI Control Monitors
- 单位：University of Virginia + UC San Diego · NeurIPS 2026 EvoRobust workshop（已核）· [arXiv](https://arxiv.org/abs/2610.41713)
- 要点：在标准后门代码 control 评测集上，不运行代码的简单特征胜过 24 个被提示当监控器的开放权重模型中的 20 个。标签通过代码风格泄露（正常代码由人写，后门由旧模型写）。测试集中每 7 个后门有 1 个通不过有效性检查。Sonnet 5 监控器抓旧模型后门 77%，抓 Sonnet 5 自己的后门只有 37%；两边都核验后为 78% 对 61%。重建后的数据集已放出（作者自述，待核）。

### 19. 2610.40939 — The First Few Tokens Matter: Understanding Chain-of-Thought Controllability
- 单位：Harvard / Cambridge Boston Alignment Initiative / MIT（Laura Ruis）（已核）· [arXiv](https://arxiv.org/abs/2610.40939)
- 要点：模型难以控制思维链，是因为思考标签后头几个 token 熵塌缩。哪怕只预填一个 token，或禁用常见开头 token 并给上下文示例，平均遵从率就能提高 34–41 个百分点。「添加/风格」和「抑制」两类可控性表现为不同能力，它们与可监控性的关系取决于评测方式。

### 20. 2610.41073 — bf16 Rounding Silently Discards Most RL Policy Updates
- 单位：Stanford（已核）· [arXiv](https://arxiv.org/abs/2610.41073)
- 要点：RL 后训练中，用就近舍入导出 bf16 会丢掉大部分更新。Qwen3-1.7B 上每步只有 0.4–0.5% 的服务权重改变，策略比优化器落后 50–150 步。「Fair Cast」（随机舍入 / 误差反馈）只需改一行，每次导出耗时 22–38 ms。25 组种子对：18 胜、6 平、1 负，平均 +6.1 分。

### 21. 2610.41437 — A prospective randomized study of patient-centered AI for clinical visit preparation
- 单位：Google Research（Google Health app）（已核）· [arXiv](https://arxiv.org/abs/2610.41437)
- 要点：前瞻性随机研究，802 名美国成年人、866 段对话。临床医生评估的准备完整度 67.2% 对 50.6%。患者自评准备充分 73.8% 对 57.0%。各组安全性都保持在高水平。

### 22. 2610.42146 — Hierarchical World Models with Implicit Dynamics（ID-WM）
- 单位：NYU Courant（Yann LeCun、Lerrel Pinto）+ Meta-FAIR（Mido Assran、Nicolas Ballas）+ AMI Labs（已核）· [arXiv](https://arxiv.org/abs/2610.42146)
- 要点：分层世界模型，比 SOTA 策略/扩散规划器高 38.5%，比单层世界模型 MPC 高 135%。

### 11/03 批次（周二，不完整：摘要页 2611.00001–00317）

### 23. 2611.00284 — OCELOT: Planetary-Scale Species Distribution Modeling with Satellite Foundation Embeddings
- 单位：Google DeepMind + Google Research（已核）· [arXiv](https://arxiv.org/abs/2611.00284)
- 要点：在 100,000 个分类单元的 20 亿条 GBIF 记录上训练。卫星基础嵌入让地理外推比只用坐标的模型提升 51%。（生态学方向，中等信号。）

### 24. 2611.00314 — Decentralized Multi-Agent Coordination and Communication in Shared Codebases（ParallACT）
- 单位：UT Austin（Peter Stone 等）+ NVIDIA（Joydeep Biswas）（已核）· [arXiv](https://arxiv.org/abs/2611.00314)
- 要点：新基准 ParallACT，让多个编码 agent 在没有编排器的情况下编辑同一仓库。并行 agent 明显低于单 agent 理想上限，矛盾任务上尤甚。（中等信号。）

## 只记结论（生物 / 网络安全）
- 2610.41015 EDB-Bio（生物证据权衡基准；与 2610.38851 同一团队）：开箱即用的模型信心不足，得分接近基础概率预测者；用恰当评分规则做后训练有明显帮助。不记细节。
- 本轮网络安全论文（如 2610.38617 Snyk VulnBench、2610.40721 MetaVul、2611.00138 Kerkoporta）均非顶级实验室或高信号，不收录。

## 排除（低信号、实验室误命中或标题误导）
- 2610.40940 FABench：「Hugging Face」命中只是一个数据集链接，作者为 Raven Labs / 浙江大学，非顶级实验室，排除。
- 2610.41956 Chronos-2（AWS）：Chronos-2 已于 2025 年公开发布，新闻价值低。
- 2610.40738 Apriel Voice 27B Preview（ServiceNow，基于 Gemma 4 26B-A4B）：合理的开放模型但信号中等，留作备选（Big Bench Audio 98.90，τ-Voice 65.51%）。
- 标题误导：2610.40890「ChatGPT as a Surveillance Assistant?」（SFU）、2610.42010 TurnTurk-GPT（Ata Technology）、2610.39796（一篇随笔）。标题中的模型名与相应实验室无关。
- 2610.38520（幻觉定义）：Meta（FAIR）只是 17 个单位之一，牵头方为牛津，立场论文性质，不收录。

---

# 四、X

窗口：2026-10-30 09:43 → 2026-11-03 09:12 SGT。来源：
- 首页时间线 3 页，共 294 条（已过滤回复）。只覆盖 11-02 16:51 → 11-03 09:08 SGT，前面约 3 天半靠检索补齐。
- 官方/关键账号合并检索两组：OpenAI/Anthropic/Cursor/Cohere 等一组，Google/DeepSeek/Kimi/MiniMax/Mistral 等一组。
- 定向检索：S-1/A、Kimi K3.1 Pro、蒸馏后续、Carbon/Genie、AGENTS.md/Fragnesia/Playwright、Navier–Stokes、Codex 限额、Fable/MiniMax/Mistral/Decart、Weight-Space Programming、Cathedral/阿里-Cohere/下一代旗舰泄露、ADNOC。
- X Today's News：72 小时内检索 6 组关键词。
- 交叉核对：SEC EDGAR（S-1/A 原文）、OpenAI Help Center、The New Stack 原文、Anthropic Alignment 博客、Cursor 博客、CISA KEV JSON、NVD API、Hugging Face API、GitHub API。

Codex 版本说明本期未核。

## 主条目

### 1. Anthropic 递交 S-1/A：Q3 收入 170 亿美元，9-30 后新签 8,954 亿美元算力承诺；首次写明"可能很快"触及 RSP 的"AI 显著加速进展"门槛
修订稿比 10-26 的初稿多了一个完整季度，数字很猛：单季收入是去年同期的 12 倍多，但算力成本占比从 48% 回升到 58%，单季重新出现经营亏损。更值得写的是新增的风险因素：Anthropic 在证券文件里说，按内部估计和对未来模型的预期，可能"很快"达到自家负责任扩展政策（RSP）里"AI 带来显著加速进展"的定义，但目前没有任何模型被认定越线。价格区间、发行股数仍然空着。
- **是什么**：
  - 递交：2026-11-02 09:24 ET 递交 S-1/A（Amendment No.1），Nasdaq Global Select，代码 ANT。价格区间、发行股数、募资额仍是空白（"between $ and $"），截至 10-31 的 Run-Rate Revenue 也留空。
  - 收入与利润（单位百万美元）：
    - Q3 收入 16,956（同比 +1,127%），Q2 为 11,555。
    - 前九个月收入 33,242，净亏损 104,039。亏损主要来自合作方融资和可转债的公允价值变动等非现金项。
    - 季度表：Q2 经营利润 974，Q3 经营亏损 567；Q2 净亏损 66,309，Q3 净亏损 23,291。
    - 算力与基础设施费用 Q3 为 9,863，占收入 58%（Q2 为 48%）。
  - 承诺：9-30 之后新签合同承诺 8,954 亿美元，约 4,475 亿在 2030 年底前，其余在 2031–2045 年；9-30 后 12 个月内到期 698 亿。
  - 其他：员工从 2024 年底约 940 人增至约 5,300 人；前五大客户约占九个月收入 25%。
  - 新增风险表述（初稿没有）："internal estimates and our expectations regarding future models… indicate that we may imminently meet our Responsible Scaling Policy's definition of 'dramatically accelerated progress attributable to AI.' We have not designated any of our current models as exceeding this threshold."
- **为何重要**：
  - 这是 Anthropic 第一次在有法律责任的文件里，给"自我加速"门槛加上"很快"的时间判断，会被拿来和 RSP 的安全承诺对照。
  - 8,954 亿美元承诺是"收入增速能否覆盖算力合同"讨论的核心数字。
  - Q3 毛利压力回升，说明增长主要靠算力堆出来。
- **对谁·深读建议**：投资/财经写作者、AI 政策与安全读者。S-1/A 重点读 Risk Factors 里 RSP 那段、季度经营数据表和 Contractual Obligations；拿新稿和 10-26 初稿逐段对比，能找出其他措辞变化。
- **证据**：
  - 已核：[S-1/A 索引](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/0001628280-26-068676-index.htm)、[S-1/A 原文](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)
  - X 侧：[X News：Q3 收入与安全警示](https://x.com/i/trending/2117023506613293386)、[Polymarket：170 亿](https://x.com/Polymarket/status/2117280179404112116)、[Polymarket：8,954 亿](https://x.com/Polymarket/status/2117342177730961738)、[MTSlive 解读（含 58% 算力占比）](https://x.com/MTSlive/status/2117415479304446163)
  - 待核：[lefttailguy：称修订稿改了"出售前沿 token"的措辞](https://x.com/lefttailguy/status/2117423239979028696)
- **约时**：S-1/A 递交 2026-11-02 22:24 SGT；X 侧讨论 11-02 23:38 → 11-03 09:10 SGT

### 2. Cursor 扩展市场被投毒：篡改版 Claude Code 扩展在线约 11 小时，最多 5,000 名用户受影响
这是 agent 工具链第一次大规模的"官方插件被替换"事件。恶意包冒用的是 Anthropic 的 Claude Code VS Code 扩展，不是 Anthropic 发布的，通过 Cursor 自己的扩展市场分发。Cursor 当天下线了市场，清理后恢复。受影响用户机器上可能留下 SSH 后门，需要按博客自查。
- **是什么**：
  - 受影响版本：Anthropic.claude-code 2.1.312 / 2.1.313（Windows、macOS），在线时间 10-29 2:27am–1:35pm PT。
  - 影响（只记结论）：受影响机器可能被植入远程访问后门，需按 Cursor 官方安全通告自查。攻击细节不在此记录。
  - 处置：下线扩展市场、轮换密钥、重建市场，并让服务商关停攻击者服务器。要求所有用户升级到 2.1.314。博客最后更新于 10-30 11:30am PT。
- **为何重要**：编码 agent 扩展天然拿着仓库、终端和凭据权限。上期讲的是模型被 AGENTS.md 劫持，这期是分发渠道本身被替换。对企业来说，扩展的来源校验和版本钉死要纳入供应链治理。
- **对谁·深读建议**：用 Cursor 的团队、IT/安全负责人、做 IDE 插件市场的人。按 Cursor 官方安全通告自查，并升级到 2.1.314。
- **证据**：
  - 官方自报：[@cursor_ai](https://x.com/cursor_ai/status/2116074289053175808)、[Cursor 安全通告](https://cursor.com/blog/claude-code-extension-security-notice)
  - X 侧：[X News：恶意扩展在线 11 小时](https://x.com/i/trending/2116054158553842030)
- **约时**：恶意包在线 10-29 17:27 → 10-30 04:35 SGT；Cursor 发帖 10-30 15:46 SGT；博客更新 10-31 02:30 SGT

### 3. MIT CSAIL "Weight-Space Programming"：GPT‑6 Astra 不用梯度、直接改 0.016% 的权重，让 0.8B 小模型数学成绩翻几倍
这是本窗口传播最广的研究帖。作者让 GPT‑6 Astra 读一个小模型的权重，然后直接写回修改，不做任何训练，就修好了 Qwen3.5‑0.8B 的推理死循环。已有人在推特上独立复现。但被改的都是小模型，作者也列出了失败案例，"前沿模型能读写神经网络"这个说法要打折看。
- **是什么**：
  - 作者：Takehi、Teoh、Zhang、Khattab（MIT CSAIL），博客 11-02 发布，日志开源在 GitHub（RikiyaT/lm_understand-logs）。
  - Qwen3.5‑0.8B：Astra 只改了 131,072 个权重（0.016%，第 15/19 层 MLP 里的一个方向），用了 50 次前向检查，MATH‑500 从 7.9 到 48.1，GSM8K 从 13.8 到 67.1，IFEval 从 21.0 到 62.3；撞到 token 上限的比例从 93% 降到 33%。
  - 其他实验：
    - 只看权重就能判断一个网络在玩哪款游戏。
    - 从零手写 MinAtar 策略网络，Breakout 得分 517.4，同期 PPO 训练 5 亿步为 25.3。
    - 1.48M 参数的围棋网络 50 次前向后胜过同尺寸 PPO 网络。
    - Kinetix 小车任务只改了 3.5% 的权重。
  - 失败案例：只看权重认不出哪个模型被训练成谄媚，给了注意力模式才认出来；改不动 Gemma 3 270M。
  - 复现：AlexKrentsel 称复现了博客结果，同时提醒被改的 Breakout 模型只有 20,486 个参数，前沿模型是万亿级。
- **为何重要**：如果站得住，这是"模型直接编辑模型"的第一组可量化结果，对可解释性、模型修复和安全审计都有意义，也会被拿来讨论递归自我改进。同时有人认为说法夸大，规模外推还没有证据。
- **对谁·深读建议**：可解释性和模型编辑方向的研究者、AI 安全读者。先读博客的失败案例和方法部分，再看复现帖的提醒；中文速读看宝玉。
- **证据**：
  - 官方自报（作者）：[@rikiyatakehi](https://x.com/rikiyatakehi/status/2117313742891327994)、[博客](https://rikiyat.github.io/blog/weight-space-programming/)
  - 第三方：[AlexKrentsel 复现](https://x.com/AlexKrentsel/status/2117376683724660898)、[AlexKrentsel 提醒](https://x.com/AlexKrentsel/status/2117376696211091894)
  - X 侧：[宝玉解读](https://x.com/dotey/status/2117408133773705525)
- **约时**：原帖 2026-11-03 01:51 SGT；复现 11-03 06:01 SGT

### 4. Claude 订阅改名：Max 5x 改叫 Max、Max 20x 改叫 Ultra，已验证的 Ultra 账号取消 5 小时限额
价格没变，但 200 美元档取消了最让重度用户头疼的 5 小时滚动窗口，只保留周限额。和 OpenAI 这边"12 月起 ChatGPT 与 Codex 共用额度"（见进展）放在一起看，两家在高价订阅的额度设计上正在走向不同方向。
- **是什么**：
  - 改名：Max 5x → Max（$100/月），Max 20x → Ultra（$200/月），现有订阅者无需操作。
  - 限额：已验证的 Ultra 账号取消 5 小时限额，大部分现有订阅者即日生效；较新的账号先保留临时限额，验证后邮件通知，官方说是为了防欺诈和滥用。周限额不变。
  - 媒体：X News 称 Ultra 的周限额是 Pro 的 10 倍（待核）；前 Claude Code 成员 Thariq 称 200 美元档对大多数任务足够。
- **为何重要**：重度 Claude Code 用户最常遇到的就是 5 小时窗口打断工作流。Anthropic 选择用"账号验证"换取更宽的额度，同时周限额不动，成本控制还在。
- **对谁·深读建议**：Claude Code 重度用户、团队采购。读官方帖和价格页即可。
- **证据**：
  - 官方自报：[@claudeai](https://x.com/claudeai/status/2116220869479428500)、[@bcherny](https://x.com/bcherny/status/2116222842413142111)、[Claude 价格页](https://claude.com/pricing)
  - X 侧：[X News：改名与取消限额](https://x.com/i/trending/2116229906925568174)、[X News：$200 档够用](https://x.com/i/trending/2117370798793175082)
- **约时**：2026-10-31 01:29 SGT

### 5. 周末"下一代旗舰"泄露潮：Altman 称解出 Navier–Stokes 的就是"下一个 GPT"且"很快"发布；GPT‑6.2 Astra、Fable/Mythos 5.5 只是截图和目录条目
本条唯一有官方来源的是 Altman 在 ADIPEC 上的发言，但他没给名字和日期。GPT‑6.2 Astra 在 Codex 里灰度、Claude Fable 5.5 / Mythos 5.5 即将发布，都只来自截图和被撤下的目录条目，两家都没确认。适合写成"怎么读泄露"，不要写成发布新闻。
- **是什么**：
  - Altman（11-02 ADIPEC 能源大会）：9 月那次 Navier–Stokes 结果，是由"即将发布的下一个 GPT"驱动 1 万个 agent、约 4 天跑出来的，发布"很快"。同场 OpenAI 与阿布扎比方面签了四份协议，ADNOC 部署相关技术（ADNOC 新闻稿本包未能打开，按转述）。
  - 待核：
    - GPT‑6.2 Astra：有人晒出 Codex 用量截图，显示 gpt‑6.2‑astra 约占 19.8%，被解读为小范围灰度；还有"跳过 6.1 Astra""价格降 60% 到 $4/$20"等说法，均无来源。
    - Claude：Azure 模型目录一度出现 `claude-fable-5-5` 条目后被撤；Mythos 官网源码里有 5.5 字样（只剩截图）；有人晒出所谓 Fable 5.5 纯代码动画 demo，发帖者自己写明"Not confirmed by Anthropic"。
- **为何重要**：Anthropic 上市路演前后、OpenAI 刚结束 28 天连更，市场对"下一代模型"预期很高，泄露信息会被大量转发。读者需要知道哪条有官方来源、哪条没有。
- **对谁·深读建议**：AI 媒体写作者、要排期模型迁移的开发者。先读 jiangding01 的证据分档，再看 Altman 发言的转述；不要引用价格和流量比例。
- **证据**：
  - X 侧：[X News：Altman 称下一个 GPT 解出千禧难题](https://x.com/i/trending/2117332420252877265)、[MTSlive](https://x.com/MTSlive/status/2117418093748297943)、[0xwolverines 中文转述](https://x.com/0xwolverines/status/2117425147778941146)、[MayaGPU：四份协议](https://x.com/MayaGPU/status/2117425151553966449)
  - 官方自报（未能打开）：[ADNOC 新闻稿](https://www.adnoc.ae/media-center/news/2026/11/ADNOC-Signs-Landmark-Partnership-Agreement-with-OpenAI)
  - 待核：[jiangding01 证据分档](https://x.com/jiangding01/status/2117421850913636792)、[dongqingtry](https://x.com/dongqingtry/status/2117425172554862652)、[RoundtableSpace：Fable 5.5 demo](https://x.com/RoundtableSpace/status/2117425275839316344)、[xxuln1：降价传言](https://x.com/xxuln1/status/2117425275009183882)
- **约时**：Altman 发言 11-02（阿布扎比时间）；泄露讨论 11-01 晚 → 11-03 09:15 SGT

## 进展

### 进展：Anthropic IPO：S-1/A 已递交但价格区间、发行规模仍空白；报道称 11-9 那周路演、感恩节前上市
- **是什么（新增）**：
  - 已核：S-1/A 于 11-02 递交，价格区间、发行股数、募资额仍空白（详见主条目 1）。上期"仍无 S-1/A"的状态结束。
  - 时间表（转述）：Bloomberg 称最早 11-9 那周开始路演；X News 称目标在感恩节（11-26）前登陆 Nasdaq。上期按"11-16 那周交易"推算，新说法往后挪了大约一周（待核）。
  - 估值与规模（待核）：X News 引述称投资者把估值往 1.5 万亿美元推；向日本投资者出售最多 35 亿美元股份；Pre-IPO 交易价约 $1,742。
  - 市场：Polymarket 11-02 上线 ANT 永续合约；X News 称 Anthropic 占 SpaceX 三季度收入 34.5%（待核）。
- **证据**：
  - 已核：[S-1/A 原文](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)
  - X 侧：[X News：Polymarket 永续](https://x.com/i/trending/2117328872840544544)、[Polymarket 帖](https://x.com/Polymarket/status/2117273318785221042)
  - 待核：[X News：1.5 万亿估值/路演/日本份额](https://x.com/i/trending/2117386316300087720)、[MTSlive：Bloomberg 路演时间](https://x.com/MTSlive/status/2117415479304446163)、[S1Journal_JP](https://x.com/S1Journal_JP/status/2117420050743439657)
- **约时**：11-02 22:24 → 11-03 09:06 SGT

### 进展：Codex/ChatGPT 限额：12 月起 Plus/Pro/Business 的 ChatGPT 与 Codex 共用一个按 token 计的额度（官方帮助文档已确认）；Chat 与 Work 合并；28 天连更收尾
- **是什么（新增）**：
  - 已核：OpenAI 帮助文档《Understanding ChatGPT and Codex usage limits》写明：从 12 月起，Plus、Pro、Business 的用量额度在 ChatGPT 和 Codex 之间共享，按 token 计量，模型越强、任务越复杂消耗越多；Instant 对话不占额度；可在 Settings → Usage 看合并后的剩余量和重置时间。官方称预计多数用户等待重置的频率不会比现在高。上期这条只是 X News 说法（标待核），现已有官方文档。
  - 第三方：The New Stack 称 OpenAI 拒绝回答具体哪天生效、合并后额度是否等于原来两份之和；开发者论坛有用户要求保持分开或先上线实时用量面板。
  - 产品：Chat 和 Work 两个标签将合并为一个界面，先对部分用户开放（媒体报道，OpenAI 邮件通知用户）。
  - Tibo 的 28 天系列：
    - 第 26 天：手机端可切换多个账号，桌面端即将支持。
    - 随后两天发放两次"banked"重置（Banked 1/2、2/2），28 天系列结束。帮助文档同时说明：用掉一次完整的 banked reset 会同时刷新 5 小时和周窗口，并改变每周重置日。
- **证据**：
  - 已核：[OpenAI 帮助文档：共享额度](https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits)、[OpenAI 帮助文档：Codex 与 ChatGPT 计划（含 banked reset）](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan)、[多账号帮助文档](https://help.openai.com/en/articles/20001068-using-multiple-chatgpt-accounts-on-web-and-mobile)
  - 官方自报：[@thsottiaux 第 26 天](https://x.com/thsottiaux/status/2116405414921384099)、[Banked 1/2](https://x.com/thsottiaux/status/2116692529970311254)、[Day 28 Banked 2/2](https://x.com/thsottiaux/status/2117035794678546764)
  - 第三方：[The New Stack](https://thenewstack.io/openai-chatgpt-codex-shared-limits/)
  - X 侧：[thenewstack 帖](https://x.com/thenewstack/status/2117330973679345899)、[Tesla_Optimus_K：Chat/Work 合并](https://x.com/Tesla_Optimus_K/status/2117372121890632166)、[jpsharada：Impress Watch](https://x.com/jpsharada/status/2117386848771154221)
- **约时**：Tibo 10-31 13:42 → 11-02 07:27 SGT；帮助文档 11-02 前后更新；TNS 11-02 11:45（美东）

### 进展：GPT‑6.1 Terra：OpenAI 称将用 Astra、Terra 等前沿模型扩展 dots
- **是什么（新增）**：Tibo 称 dots 背后的前沿模型家族正在扩充，包括 GPT‑6 Astra 和 GPT‑6.1 Terra，以后还会加其他模型；Terra 带来速度和"性格升级"，会帮助 dots 覆盖更多用户。第三方继续出 Terra 对比测评（The New Stack：Terra vs Opus 5.5、Terra vs Astra）。
- **证据**：官方自报：[@thsottiaux](https://x.com/thsottiaux/status/2117283124833055196)；X 侧：[X News：Terra](https://x.com/i/trending/2116283597795807480)
- **约时**：11-02 23:50 SGT

### 进展：OpenAI 科学发现：仍无外部定论；Altman 把 Navier–Stokes 结果归给"下一个 GPT"
- **是什么（新增）**：
  - Altman 在 ADIPEC 称 Navier–Stokes 结果由即将发布的下一个 GPT 完成（见主条目 5）。这是 OpenAI 自己的说法，不是外部核查。
  - X News 汇总的争议：批评者认为"光滑但极端的外力"设定是钻规格漏洞；OpenAI 公开了 Lean 形式化验证，但没有申领百万美元奖金，数学家仍在核验。
  - ETH（指数时间假设）结果：X News 称正由包括假设提出者在内的专家审阅，暂无结论。
- **证据**：X 侧：[X News：数学证明争议](https://x.com/i/trending/2116274739953975524)、[X News：ETH 审阅中](https://x.com/i/trending/2116233269377450277)、[X News：Altman](https://x.com/i/trending/2117332420252877265)
- **约时**：10-31 02:26 → 11-03 08:25 SGT

### 进展：模型监控模型：Anthropic 让上千个 Claude agent 自动造"骗过训练数据监控器"的数据
- **是什么（新增）**：Anthropic 新研究，把红队自动化：让数千个 Claude agent 去造能骗过训练数据监控器的数据。产出的数据看起来无害（如老摔跤手带新人、养蜂问答），但会让小型研究模型学到错位行为。这些样本可直接用来改进下一代监控器；官方称只是第一步。上期讲的是 OpenAI/Anthropic 的运行时监控，这期是"监控器本身怎么被攻破、怎么补"。
- **证据**：官方自报：[@AnthropicAI](https://x.com/AnthropicAI/status/2116349211549843666)、[Alignment 博客原文](https://alignment.anthropic.com/2026/automated-em-search/)；X 侧：[X News](https://x.com/i/trending/2116359580469146040)
- **约时**：10-31 09:59 SGT

### 进展：Chrome 补丁与浏览器 agent：Playwright 1.64.1 仍捆绑 Chromium 156.0.8078.4，早于 CVE-2026-118306 修复版
- **是什么（新增）**：
  - 已核：NVD 收录 CVE-2026-118306：Chrome 156.0.8078.73 之前 FileSystem 组件内存破坏，可能在沙箱外执行任意代码，Chromium 评级 Critical（NVD 10-27 发布）。
  - X 侧：开发者 nisten 11-02 提醒 Playwright 1.64.1 仍捆绑 156.0.8078.4；aldabrahq 补充 Playwright 默认关闭沙箱，风险在于 agent 浏览不可信页面，不在测试自家应用（待核）。也有反驳称只有安装并运行 Chromium、打开陌生页面才有风险。
  - 上期只说"Puppeteer、Playwright 钉住的版本落后"，这期有了具体 CVE 和版本号。
- **证据**：已核：[NVD CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306)；X 侧：[X News](https://x.com/i/trending/2117377176194699724)、[aldabrahq](https://x.com/aldabrahq/status/2117424986042339500)、[yagcidev 反驳](https://x.com/yagcidev/status/2117396755360747594)
- **约时**：11-02 → 11-03 09:13 SGT

### 进展：Kimi K3.1 Pro：权重仍未上 HF；AA 称其"性格变化"是迄今最大
- **是什么（新增）**：
  - 已核：截至 11-03 上午，Hugging Face 上 K3.1 Pro 仓库仍返回 401，moonshotai 最新公开仓库仍是 Kimi‑K3（09-02）。
  - 第三方：
    - AA-PersonalityBench：K3.1 Pro 与 K3 相比，30 项性格特质的百分位排名平均变动 30 分，是 AA 见过的最大一次（第二大是 GPT‑6 Sol → 6.1 Sol 的 23 分）。
    - DesignArena：K3.1 Pro 在 Game Dev 榜开放权重模型中第一（尚未开放权重，此处为榜单原话），总榜升至前五。
  - 官方：Kimi 上线 3D Make。
  - 待核：多名用户称权重 11-04 发布，未见官方新确认。
- **证据**：已核：[Hugging Face moonshotai](https://huggingface.co/moonshotai)；官方自报：[@Kimi_Moonshot 3D Make](https://x.com/Kimi_Moonshot/status/2116005725814280570)；第三方：[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2117385943959093677)、[@DesignArena](https://x.com/DesignArena/status/2117315418528575649)；待核：[mdrizalnp](https://x.com/mdrizalnp/status/2117374742487605434)
- **约时**：10-30 11:14 → 11-03 06:38 SGT

### 进展：MiniMax 与 Mistral：只有生态和演示，无新模型
- **是什么（新增）**：
  - MiniMax：官方致谢社区为 428B 的 M3.1 Flash 做量化，包括 Unsloth 2-bit 动态 GGUF（143.9 GB）、AMD MXFP4、Apple Silicon 的 MLX 量化等。
  - Mistral：演示 Large 4 从零写量子化学 SCF 求解器并做 3D 可视化；HF 仓库可正常访问。
- **证据**：官方自报：[@MiniMax_AI](https://x.com/MiniMax_AI/status/2116996123164569606)、[@MistralAI](https://x.com/MistralAI/status/2117229259425038344)
- **约时**：11-02 04:49 → 11-02 20:16 SGT

以下追踪项本期**无新消息**，不单列：
- 蒸馏报道：DeepSeek、月之暗面、OpenAI 均无回应，X 上只有对上期报道的转述。
- Gemini 4 Carbon：仍未对公众开放，本窗口无扩大开放范围的官方消息；Genie 4 无新消息。SemiAnalysis GDPx 中 Carbon 得分见「其他」。
- AGENTS.md 劫持 Codex：GitHub issue #41499 仍为 open，最后更新 08-29，0 条评论，无厂商补丁。
- Brotli/Fragnesia：CISA KEV 10-29/10-30 新增的是 Ivanti、GitLab、Cisco 漏洞，无相关新条目。
- 阿里对 Cohere：无回应。Cohere 本窗口只发了加拿大投资承诺（见「其他」）。
- Fable 5.5：仍无官方消息，新传言见主条目 5。
- Claude auto mode：无官方生效公告。
- Decart：无新帖。
- Cathedral：只有一条单源帖称其 12 小时内攻入 Anthropic 内部业务系统（待核），无报道跟进。

## 其他
- **OpenAI 其他**：
  - Pando：OpenAI 为 monorepo 自研 Git 后端，push 延迟降约 80%，每天服务近 1PB Git 数据。[@OpenAIDevs](https://x.com/OpenAIDevs/status/2117408792346509663) · [X News](https://x.com/i/trending/2117416317305131207) · 11-03 08:09 SGT
  - LifeVal：基于数千名 ChatGPT 用户反馈的个人助理日常任务基准。[@OpenAI](https://x.com/OpenAI/status/2117307611338997846) · [原文](https://openai.com/index/lifeval/) · 11-03 01:27 SGT
  - Private Intelligence：面向企业的零数据保留、私有推理与数据控制。[@OpenAI](https://x.com/OpenAI/status/2116186509384815084) · [原文](https://openai.com/business/private-intelligence/) · 10-30 23:12 SGT
  - 发布 77 秒动画短片 "Museum of What Could Be"。[@OpenAI](https://x.com/OpenAI/status/2116253388883345623)
  - 关停免费 LaTeX 科研写作工具 Prism。[X News](https://x.com/i/trending/2116219623100338529)
  - Dan Driscoll 加入 OpenAI（待核）。[Polymarket](https://x.com/Polymarket/status/2117420789137834379)
- **Anthropic 其他**：
  - Messages API 的 message threads 公测：服务端缓存对话，只需发新消息和上一条消息 ID。[@ClaudeDevs](https://x.com/ClaudeDevs/status/2117332449382510884) · 11-03 03:06 SGT
  - Anthropic Residency 开放申请：6 周到 6 个月的付费研究岗，不要求 ML 背景，年化薪酬 35–50 万美元，11-22 截止。[@AnthropicAI](https://x.com/AnthropicAI/status/2117343929960112486) · [原文](https://alignment.anthropic.com/2026/anthropic-residency/)
  - Claude Code 系统提示词新增限制：不得复刻具体已有游戏（改名也不行），原创和同类型游戏不受影响。[X News](https://x.com/i/trending/2116891884039852484)
  - Claude Code 2.1.317 即将发布。[ClaudeCodeLog](https://x.com/ClaudeCodeLog/status/2117407889031614912)
- **Google/DeepMind**：
  - 英国 PlanAssist（DeepMind 参与）扩展到另外 12 个地方议会，试点审批时间最多缩短 58%。[@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2116524000977285321) · [X News](https://x.com/i/trending/2116538622782714060)
  - Gemini Drops 月度更新。[@GeminiApp](https://x.com/GeminiApp/status/2116304609383710988)
  - Antigravity 接入 Gemini 4 Argon。[@googledevs](https://x.com/googledevs/status/2117315944079057023)
  - 有人称 Gemini 2.5 将于 12-01 起退役并自动改路由（待核）。[youaregoogled](https://x.com/youaregoogled/status/2117425276309373297)
- **中国模型与开源**：
  - DeepSeek：Harness 上线 Creator Mode，用自然语言描述即可生成插件。[X News](https://x.com/i/trending/2117308547239137776)
  - DeepSeek：开源 super-agent 原型 dsh-superagent。[X News](https://x.com/i/trending/2116731970004591075)
  - DeepSeek：Search/Fetch 工具 API 结束免费，按成功请求计费，每千次 $0.75（单源，待核）。[shao__meng](https://x.com/shao__meng/status/2117249746234466370)
  - ISTA 发布高度压缩的 DeepSeek‑V4.1‑Flash‑1017 编码版。[X News](https://x.com/i/trending/2117351175200661631)
  - 深度原理（Deep Principle）发布 753B 开放权重科研模型 Hydrogen‑1.0，基于 GLM‑5.3，MIT 许可。[X News](https://x.com/i/trending/2117280628781768999)
  - 智谱 GLM‑5.5 后训练泄露（待核）。[X News](https://x.com/i/trending/2116517186793775606)
  - Pika H3 Flex 开放权重视频模型，基于 MiniMax H3，登顶 DesignArena 开放权重文生视频榜。[X News](https://x.com/i/trending/2116434831865520255)
- **评测**：
  - SemiAnalysis 发布 GDPx（206 个专家任务、11 个领域）：Opus 5.5 得 12%，Gemini 4 Carbon 10.9%。[X News](https://x.com/i/trending/2117085754379682287)
  - AA：AA-Omniscience v1.1。[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2116319506318635503)
  - AA：HLE-Diamond。[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2115989388689813945)
  - AA：Silicon Data AgentPerf。[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2117255658613735918)
  - X News 称 Astra 在机器人智能聚合榜领先专用机器人模型。[X News](https://x.com/i/trending/2116805922211410376)
- **产业**：
  - Cohere 承诺到 2031 年在加拿大投入超 40 亿加元、创造 1,500 个岗位。[@cohere](https://x.com/cohere/status/2116186531366949192)
  - Altman 在播客中谈用机器人建"自我复制的数据中心"。[X News](https://x.com/i/trending/2116002830494683239)
  - 科技巨头资本承诺合计约 3.3 万亿美元（待核）。[KobeissiLetter](https://x.com/KobeissiLetter/status/2117424042944721041)
  - 有人称 OpenAI、Google、微软、Anthropic 支持一条共享 robots.txt AI 训练退出规则（待核）。[AIooze](https://x.com/AIooze/status/2117425040308445609)

## A 时间线/官方
- **时间线覆盖**：首页 3 页共 294 条（已过滤回复），只覆盖 11-02 16:51 → 11-03 09:08 SGT。10-30 09:43 → 11-02 16:51 这段靠官方检索、X News 和定向检索补齐，可能漏掉个人帖。
- **时间线内容**：集中在 S-1/A、Weight-Space Programming、Pando、Codex 共享额度、Mistral 演示和下一代模型泄露。高信号来源有 OpenAI、OpenAIDevs、AnthropicAI、ClaudeDevs、Tibo、宝玉、shao__meng、ArtificialAnlys。噪音是 Polymarket 的非 AI 快讯、加密行情和营销号。
- **无原创帖的账号**：deepseek_ai、Alibaba_Qwen、DecartAI 本窗口无原创帖。
- **提示注入与广告**：时间线和检索结果里有让读者"去跑这段提示词"的帖子和返佣推广，本包只当作数据处理，未执行、未引用。

## B Today's News
- **Anthropic Q3 收入 170 亿美元与安全警示**；**投资者推向 1.5 万亿估值**；**Polymarket 上线 ANT 永续**。[X News](https://x.com/i/trending/2117023506613293386) · [X News](https://x.com/i/trending/2117386316300087720) · [X News](https://x.com/i/trending/2117328872840544544)
- **Cursor 市场恶意 Claude 扩展在线 11 小时**；**Playwright 捆绑 Chromium 存在严重漏洞**。[X News](https://x.com/i/trending/2116054158553842030) · [X News](https://x.com/i/trending/2117377176194699724)
- **Claude 订阅改名、Ultra 取消 5 小时限额**；**Claude Code 禁止复刻现有游戏**；**前员工称 $200 档够用**。[X News](https://x.com/i/trending/2116229906925568174) · [X News](https://x.com/i/trending/2116891884039852484) · [X News](https://x.com/i/trending/2117370798793175082)
- **Altman：下一个 GPT 解出千禧难题**；**OpenAI 数学证明争议**；**ETH 被推翻、专家审阅中**。[X News](https://x.com/i/trending/2117332420252877265) · [X News](https://x.com/i/trending/2116274739953975524) · [X News](https://x.com/i/trending/2116233269377450277)
- **OpenAI Pando**；**Private Intelligence**；**关停 Prism**。[X News](https://x.com/i/trending/2117416317305131207) · [X News](https://x.com/i/trending/2116193874297409964) · [X News](https://x.com/i/trending/2116219623100338529)
- **Anthropic 自动化错位研究**；**SemiAnalysis GDPx**；**Hydrogen‑1.0**；**DeepSeek Creator Mode**。[X News](https://x.com/i/trending/2116359580469146040) · [X News](https://x.com/i/trending/2117085754379682287) · [X News](https://x.com/i/trending/2117280628781768999) · [X News](https://x.com/i/trending/2117308547239137776)
- 其余（Grok 相关产品、加密行情、游戏周边、印度上市等）不列。

## C 已核摘要
- **Anthropic S-1/A**（11-02 递交）：Q3 收入 169.56 亿美元，同比 +1,127%；九个月收入 332.42 亿、净亏损 1,040.39 亿；Q3 经营亏损 5.67 亿；Q3 算力费用占收入 58%（Q2 48%）；9-30 后新签承诺 8,954 亿，其中约 4,475 亿在 2030 年底前；员工约 5,300 人；新增"可能很快达到 RSP 加速门槛"表述；价格区间、股数仍空白。
- **ChatGPT/Codex 额度**：OpenAI 帮助文档确认 12 月起 Plus/Pro/Business 共享额度、按 token 计、Instant 不计。
- **Cursor 事件**：Claude Code 扩展 2.1.312/2.1.313 被篡改，最多 5,000 用户，修复版 2.1.314。
- **Claude 订阅**：Max 5x → Max（$100），Max 20x → Ultra（$200）；已验证 Ultra 取消 5 小时限额，周限额不变。
- **Weight-Space Programming**（作者自报，有一人复现）：Qwen3.5‑0.8B 改 0.016% 权重，MATH‑500 7.9 → 48.1。
- **NVD**：CVE-2026-118306 影响 Chrome 156.0.8078.73 之前版本，Critical。
- **Kimi**：K3.1 Pro 的 HF 仓库仍返回 401。
- **KEV**：10-29/10-30 新增 Ivanti（CVE-2026-118527、CVE-2026-111357）、GitLab（CVE-2026-97229）、Cisco ASA/FTD（CVE-2026-76418），无 Brotli/Fragnesia 新条目。
- **GitHub #41499**：仍 open，无补丁。
- **Anthropic Residency**：年化 35–50 万美元，11-22 截止。

## E 可扩写方向
1. **读懂 Anthropic S-1/A**：从"可能很快达到 RSP 加速门槛"这句切入，对照 RSP 原文的定义；再拆 8,954 亿算力承诺和 Q3 算力占比回升到 58%，回答"收入增速能否跑赢算力合同"。附路演到上市的时间表（标明哪些是转述）。
2. **编码 agent 的供应链**：Cursor 市场投毒（分发渠道被替换）+ 上期 AGENTS.md 劫持（指令被替换）+ Playwright 捆绑旧 Chromium（依赖落后），给团队一张自查清单：扩展来源与版本钉死、SSH 密钥与计划任务巡检、浏览器 agent 的沙箱和版本。
3. **模型能直接改模型吗**：Weight-Space Programming 的结果、复现和失败案例，加上 Anthropic 用 agent 自动造"骗过监控"的数据，讨论"模型修改模型"对可解释性和安全审计意味着什么，以及为什么小模型结果不能直接外推。
4. **两家高价订阅走向不同**：Anthropic 取消 Ultra 的 5 小时窗口，OpenAI 12 月起把 ChatGPT 和 Codex 并成一个 token 池。帮重度用户算一笔账，并列出 OpenAI 还没公开的数字。
5. （可选）**怎么读泄露**：以 GPT‑6.2 Astra 截图、Azure 上的 Fable 5.5 条目为例，按证据硬度分档，和 Altman"下一个 GPT 很快"的官方说法对照。

---

# 五、GitHub（2026-10-30 → 2026-11-03）

1. **vLLM v0.33.0**
vLLM 于 11-02 18:10（SGT）发布 v0.33.0（release 名为 v0.33.0，挂在 v0.33.0rc3 tag 上，仓库另有 v0.33.0 tag），共 927 个 commit、389 位贡献者。这一版最影响部署的是两处底层变化：底座升级到 PyTorch 2.14.0 / Triton 3.8.0，发布的 wheel 和镜像只剩 CUDA 13.0，cu129 产物停发。新模型包括 Reflection Beam-1.0（501B MoE，23B 激活）、Muse Spark Open、Step-5 Preview、MiniCPM-OCR 1.0 等。投机解码新增 XPress refiner 和 FLy 有损验证；官方引用 PR 基准称，DeepSeek-V4.1-Flash + DSpark 在 GB300 上从 1373 提升到 3390 output tok/s。破坏性变更包括移除 Medusa / MLP speculator 和旧 Ray compiled-graph executor，并弃用 LM Format Enforcer。自建推理集群、还在用 CUDA 12.9 或 Medusa 的团队升级前要先核对这份清单；新增的 `vllm/vllm` 短镜像名和 AWS EFA 镜像值得运维关注。
证据：[v0.33.0 Release](https://github.com/vllm-project/vllm/releases/tag/v0.33.0rc3) · [vllm-project/vllm](https://github.com/vllm-project/vllm)

2. **SGLang v0.5.23**
SGLang 于 11-03 06:14（SGT）发布 v0.5.23，合入 1007 个 PR（257 位贡献者）。新模型覆盖 Muse Spark Open、Beam-1.0、MiniMax-M3.1-Flash、MiniCPM-V 4.7，以及 FLUX.3 Image Klein、Cosmos3 等扩散模型。最值得看的是两个 opt-in 能力。一是「低延迟模式」：用 NVIDIA megakernel / AMD monokernel 插件把 DeepSeek-V4.1-Flash 的 decode 跑成融合常驻 kernel，官方称单用户 decode 在 GB300 上最多快 44%、在 MI350X 上快 75%。二是 Paged Experts：让超出显存的 MoE 模型在单张消费级 GPU 上运行，官方称最多比 CPU offload 快 30 倍。和上一条 vLLM 同期对照可以看出，两大推理引擎都在押注投机解码与 MoE 专家调度；关心单用户延迟或想在小卡上跑大 MoE 的人可以先读这两节的 PR。
证据：[v0.5.23 Release](https://github.com/sgl-project/sglang/releases/tag/v0.5.23) · [Paged Experts PR #42557](https://github.com/sgl-project/sglang/pull/42557)

3. **OpenAI Python v3.42.0 / Node v7.46.0–v7.47.0：Agent 会话能力进 SDK**
OpenAI 两个官方 SDK 在 10-31 同步发版（Python v3.42.0 08:26 SGT，Node v7.46.0 08:27 SGT、v7.47.0 12:46 SGT），新增 agent context compaction（上下文压缩）设置、agent session review 与 tool settings、实验性的 agent time awareness，以及图像编辑的 markup overlays、WebSocket warmup 与断线恢复等。Python 随后在 11-02 04:56（SGT）发布 v3.42.1，修复 Responses WebSocket 连接行为。这说明长会话 agent 的上下文管理和审阅机制正在变成 API 一等参数，不再需要应用层自己拼。做长时运行 agent 的开发者可以对照 changelog 看哪些自研逻辑可以交给平台。
证据：[openai-python v3.42.0](https://github.com/openai/openai-python/releases/tag/v3.42.0) · [openai-node v7.46.0](https://github.com/openai/openai-node/releases/tag/v7.46.0) · [openai-python v3.42.1](https://github.com/openai/openai-python/releases/tag/v3.42.1)

4. **deepseek-ai/dsh-superagent-prototype**
DeepSeek 官方组织于 10-31 17:32（SGT）新建这个仓库，截至 11-03 09:13（SGT）已有 13,237 星，是窗口内新仓库的星数第一。它是一个面向单个 GitHub 仓库的「主动式」coding agent，打包给 DeepSeek Harness 使用：监听 GitHub（可选飞书）上被授权的请求，为每项工作开独立的会话和目录，处理完在原对话里回复，例如提交 PR，另有一个 Web 面板汇总需要人处理的事项。README 明确写着这是「仅供参考的研究原型，不是 DeepSeek 官方产品」，与其文章《Exploring Super-agent Design》描述的实现并不完全一致，大量工程由 coding agent 完成。它的价值主要在设计文档：docs 下 000–008 依次讲理念、领域模型、授权、执行和提示词，核心原则是「占用尽量少的人类注意力」。想设计团队级 agent 权限与打扰边界的人值得按顺序读。
证据：[deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype) · [000 Philosophy](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/docs/000-philosophy.md)

5. **storytold/craft-anything**
ArtCraft 团队于 10-31 22:50（SGT）新建，截至 11-03 09:13（SGT）有 4,298 星，状态标为 early alpha。它是一个纯 Rust 的「净室」复刻引擎：指向一个网站、App 或游戏，先用真实检查工具研究原作，再让 coding agent 用你指定的技术栈从头写一个新项目，然后拿结果与原作对比并迭代（网页会在三种屏宽下比对）。项目自称提供 314 个工具，每个都同时是 CLI 命令和 MCP 工具，检查环节本身不需要 AI。它把「agent 写代码」推进到「先取证、再生成、再验收」的闭环，适合做前端复刻、竞品研究或 agent 验收流程的人参考；用于商业产品前要自行判断复刻对象的版权与条款。
证据：[storytold/craft-anything](https://github.com/storytold/craft-anything)

6. **JustVugg/colibri v2.1.0**
这个纯 C、零依赖、从磁盘流式加载专家、在普通硬件上跑大 MoE 的推理引擎于 10-31 20:50（SGT）发布 v2.1.0（自 v2.0.0 起 387 个 PR），日榜同时以 675 stars today 上榜。这是新版本，不只是老仓库留榜。主要更新：CPU / Vulkan / CUDA 全引擎原生读取 GGUF，无需转换或二次量化；新增 Mistral-Large-4（1T，52B 激活）、Muse Spark Open（816B）等模型；Vulkan 下超出显存的专家放进内存池由 CPU 并行计算；新增 `coli ui` 聊天界面。性能数字均为项目自称，例如 Qwen3.8-Flash-Next 在 262,144 上下文下 decode 9.6→45.7 tok/s、一次 agent 回合从 86 s 降到 4.9 s，测试硬件是单张 24 GB 卡。想在本地单卡尝试万亿参数级 MoE 的人可以和上面 SGLang 的 Paged Experts 对照看。
证据：[colibri v2.1.0 Release](https://github.com/JustVugg/colibri/releases/tag/v2.1.0) · [JustVugg/colibri](https://github.com/JustVugg/colibri) · [GitHub Trending 日榜](https://github.com/trending?since=daily)

（热榜口径：日榜约为最近 24 小时，周榜统计最近七天，均于 2026-11-03 09:13 SGT 抓取。周榜前列的 Nutlope/hallmark、pbakaus/impeccable、cloudflare/security-audit-skill 已在往期报道，本期只是留榜，不重复。）

窗口内无：ggml-org/llama.cpp、ollama/ollama、pytorch/pytorch、huggingface/datasets、openai/codex、modelcontextprotocol/python-sdk、modelcontextprotocol/typescript-sdk、comfyanonymous/ComfyUI、axolotl-ai-cloud/axolotl（常规更新未收录：Transformers v5.22.1 仅修文档；Anthropic SDK Python v2.4.0 / TS sdk-v1.4.0 及各云 SDK 子包为 Admin 分析、额度与 RBAC 接口；unsloth v0.1.913-beta；langchain 1.4.8 / langchain-core 1.7.4 / langchain-anthropic 1.7.8–1.7.9；langgraph 1.2.19 / sdk 0.4.11 / checkpoint-sqlite 3.1.3）

---

# 六、Hugging Face 与榜单

- **窗口**：2026-10-30 09:43 SGT（10-30 01:43 UTC）→ 2026-11-03 09:13 SGT（11-03 01:13 UTC），约 95.5 小时（采集开始时间 09:13:18 SGT）。
- **范围**：HF Trending 模型（前 300）与数据集（前 50）；主要机构按 lastModified 逐家扫描；LMArena 文本、视觉、文生图三榜；Artificial Analysis 的 Intelligence Index（v5）、文生图榜和图像编辑榜。
- **窗口判断：偏薄到中等。** 本窗没有新的前沿级开放权重。新东西主要有三件：微软 4B 电脑操作代理 Mage-VL-Cowork、商汤 SenseNova-Loop-9B-Preview，以及 NVIDIA 给 DeepSeek V4.1 Flash 1017 做的官方 NVFP4 量化。此外有两条值得写的跟进：Mistral Large 4 补上技术报告；Nanbeige4.3-33B 首次进入 AA 测评。
- **Kimi K3.1 Pro 截至 11-03 09:19 SGT 仍不在 HF。** moonshotai 最新的仓库还是 Kimi-K3（最后修改 09-02），官方承诺的期限是 11-04 之前。HF 搜 "K3.1" 只能搜到上期那个冒名仓库。
- **趋势榜第 15 的 burner22/numbat 声称是泄露的 Anthropic 检查点，已判定为假**：社区审计显示权重是生成出来的，不是训练结果。已列入冒名/虚假区，不放链接。
- **榜单基本没动**：LMArena 三榜都没刷新；AA 首页默认图与 10-30 完全一致；AA 图像两榜只有 ±1 名的漂移。

---

## 一、重点

### 1. microsoft/Mage-VL-Cowork：4B 的"能点也能写代码"电脑操作代理（本窗新发 · 开源）

微软 Mage 团队在本窗放出一个 4B 的电脑操作代理。它把截图点击（computer_use）和终端/代码执行（bash）放进同一个视觉语言策略里，不需要外部编排器。卡片和项目页给出的成绩是 OSWorld-Verified 66.0%（50 步预算），作者称这是 4B 档的最好成绩。这件事值得关注的点是：端侧小模型做复杂电脑操作已经接近可用（与第一、三部分的 arXiv 2610.40747 是同一项，正文合并为一条）；训练配方（五阶段课程 + 在线 RL）和任务合成引擎 Mage-CUA-Forge 都写进了技术报告，可以复现。适合做桌面自动化/RPA、端侧代理、CUA 训练数据合成的团队。

```
已核
id: microsoft/Mage-VL-Cowork
createdAt: 2026-10-30 20:13 SGT (12:13 UTC)
lastModified: 2026-10-30 20:14 SGT (12:14 UTC)，权重随首批提交上传
likes/downloads: 143 / 1,152    Trending #40（新进）
license: apache-2.0（卡片徽章同为 Apache 2.0）    pipeline: image-text-to-text
权重: 2 个 safetensors，HF 统计约 4.74B 参数
开放度: 开源（OSI 许可）
官方性: 作者为 microsoft 官方 org；项目页 microsoft.github.io/Mage/cowork 反链到该 HF 仓库
基座: 中间版 microsoft/Mage-VL 4B 检查点
```

待核（卡片/项目页自报）：OSWorld-Verified 66.0%；在线 RL 比 Hybrid SFT 高 +10.16pp，同时模型调用减少 13.0%、输出 token 减少 25.4%；Mage-CUA-Forge 在 6,915 个技能上合成 293,806 个任务，单任务成本降 82.6%；训练用 32×B200，加 1,120 个 CPU 沙箱槽。

链接：[HF](https://huggingface.co/microsoft/Mage-VL-Cowork) · [项目页](https://microsoft.github.io/Mage/cowork/) · [arXiv 2610.40747](https://arxiv.org/abs/2610.40747) · [技术报告 PDF](https://github.com/microsoft/Mage/blob/main/assets/mage_vl_cowork_tech_report.pdf)

### 2. sensenova/SenseNova-Loop-9B-Preview：把同一段层"跑两遍"的 9B 多模态模型（本窗官宣 · 开源）

商汤放出一个 9B 的循环（looped）解码器多模态模型。32 个不同的层中，有一段连续 24 层共享权重、执行两次，所以一次前向共执行 56 层；同时用双流 mHC 管理两条残差流。卡片写明训练序列最长 262,144 token，定位长上下文和 agent 工作流。值得关注的原因是：这是少见的"不加参数、只加深度"的开放实验，对推理成本和能力的取舍有参考价值。适合做架构研究、长文档和 agent 场景的小模型使用者。需要注意时间线：仓库建于窗前，权重在窗口开始前约 12 小时上传，但官方 News 写的发布日期是 10-30，并且窗内有大量文档提交，所以算作本窗官宣。

```
已核
id: sensenova/SenseNova-Loop-9B-Preview
createdAt: 2026-10-28 23:34 SGT (15:34 UTC)
权重上传: 2026-10-29 21:46 SGT (13:46 UTC)，窗前约 12h
lastModified: 2026-11-02 23:43 SGT (15:43 UTC)，共 39 次提交，窗内以文档为主
likes/downloads: 186 / 1,536    Trending #26（新进）
license: apache-2.0    pipeline: image-text-to-text
权重: 9 个 safetensors，HF 统计约 9.66B 参数
开放度: 开源
官方性: sensenova 官方 org；GitHub OpenSenseNova/SenseNova-Loop 的 README 反链 HF 仓库，News 标注 "[2026.10.30] We release"
```

待核：混合注意力（卡片写 3 线性 + 1 全注意力的模式）和 MTP 的细节；技术报告尚未发布（卡片写 TBD）；vLLM/SGLang 支持依赖尚未合并的 PR（卡片列出 vllm#64832 和 sglang#47281）。

链接：[HF](https://huggingface.co/sensenova/SenseNova-Loop-9B-Preview) · [GitHub](https://github.com/OpenSenseNova/SenseNova-Loop)

### 3. nvidia/DeepSeek-V4.1-Flash-1017-NVFP4：上期榜首开放模型的官方 4 位部署版（本窗新发 · 开放权重/MIT）

NVIDIA 给 AA 开放权重榜第一的 DeepSeek V4.1 Flash 1017 做了 NVFP4 量化：路由专家从 MXFP4 转成 NVFP4（W4A4），Engram 查表从 FP8 转成 MXFP4。卡片自测六项基准与源检查点基本持平。它的意义在于降低这款模型在 Blackwell（GB300）上的部署门槛。代价是需要带 vLLM PR #61530 的定制构建，SGLang 没有验证过。适合已在 Blackwell 集群上部署 DSV4.1 的推理团队。

```
已核
id: nvidia/DeepSeek-V4.1-Flash-1017-NVFP4
createdAt: 2026-10-31 01:37 SGT (10-30 17:37 UTC)
权重上传: 2026-10-31 02:09 SGT (10-30 18:09 UTC)    lastModified: 2026-10-31 02:24 SGT (18:24 UTC)
likes/downloads: 137 / 1,839    Trending #41（新进）
license: mit（继承基座）    pipeline: image-text-to-text
权重: 48 个 safetensors，HF 统计约 665B（含量化 scale）
开放度: 开放权重（MIT，OSI 许可；作为衍生量化版本列出）
官方性: nvidia 官方 org，卡片 base_model 指向 deepseek-ai/DeepSeek-V4.1-Flash-1017
```

待核（卡片 vLLM 自测，单位 %，源 MXFP4 → NVFP4）：GPQA Diamond 92.77 → 92.93；AA-LCR 80.41 → 80.19；SciCode 57.58 → 57.32；IFBench 76.33 → 76.47；MMMU-Pro 78.38 → 78.73；Terminal-Bench 2.1 81.81 → 81.11。卡片还写明：552B 主干，prefill 激活 8B、decode 激活 16B，另有 196B Engram；在 4×GB300 上运行；Engram 转换是有损的。

链接：[HF](https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4) · [基座](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) · [vLLM PR #61530](https://github.com/vllm-project/vllm/pull/61530)

### 4. speridlabs/idol：单张图出 3D 高斯点云，本窗热度从 #192 冲到 #6（窗前发布 · 本窗起量 · 开源）

Speridlabs 的 Idol 输入一张图（照片、渲染图或生成图），输出可以旋转查看的 3D Gaussian splat，包括原图看不到的侧面。它支持多档细节，从 32,768 到 1,048,576 个高斯。权重和卡片都在窗口开始前完成，但前两期没有覆盖；本窗 likes 从 33 涨到 419，Trending 从 #192 升到 #6，Comfy-Org 也做了官方节点版。值得关注的原因是：开源单图转 3D 的门槛又降了一档（官方页称 0.66B 参数、显存不到 8GB）。适合 3D 资产、电商、游戏原型和 ComfyUI 工作流的用户。

```
已核
id: speridlabs/idol
createdAt: 2026-10-28 23:55 SGT (15:55 UTC)
权重上传: 2026-10-29 00:04 SGT (10-28 16:04 UTC)    lastModified: 2026-10-30 02:17 SGT (10-29 18:17 UTC)，均在窗前
likes/downloads: 419 / 7,787（上期 likes 33）    Trending #6（上期 #192）
license: apache-2.0    pipeline: image-to-3d    权重: 4 个
开放度: 开源
官方性: 官方研究页 speridlabs.com/research/idol 反链该 HF 仓库
衍生: Comfy-Org/Idol（apache-2.0，createdAt 2026-11-02 03:33 SGT / 11-01 19:33 UTC，44 / 399）
```

待核：卡片称显存 7.2GB、生成时间不到 2 秒；官方页称 0.66B 参数、显存不到 8GB。两处说法不完全一样，以实测为准。

链接：[HF](https://huggingface.co/speridlabs/idol) · [官方研究页](https://speridlabs.com/research/idol) · [Comfy-Org/Idol](https://huggingface.co/Comfy-Org/Idol)

### 5. 跟进：Mistral Large 4 补上技术报告；Nanbeige4.3-33B 首次进入 AA 测评（本窗更新）

**Mistral Large 4**（上期重点）在本窗往 HF 仓库加了一份技术报告 PDF。报告关键自述如下（待核）：
- 规模为 52B 激活 / 1T 总参数的多模态 MoE。
- 开发中把 KV 压到极限后，发现 agent 任务吃亏，于是做了"模型手术"：先改回全注意力，再改成 DeepSeek Sparse Attention。
- FrontierCode 2.0 19.7%，Terminal-Bench 4.0 41%，AA Cyber Index 50.9%。
- 校准过的 NVFP4 检查点 606GB，可以部署在 4×GB300 上。
- 支持 high/medium/low 三档推理强度。

热度上，likes 从 1,222 涨到 1,500，下载从 278 涨到 5,500，Trending 从 #14 升到 #4。许可证是 Mistral Ecosystem Open-Weight License（改版 MIT，做 MaaS 需要另签商业许可），属于**开放权重，不是 OSI 开源**。

**Nanbeige4.3-33B**（10-27 期覆盖）：
- AA 更新流 11-02 新增测评，模型页写 "scores 20 on the Artificial Analysis Intelligence Index"（解析值 20.4，同类中位数 13）。这个分数在开放权重第一梯队（30 分左右）之下。
- 官方在 10-31 补了 FP8/INT8/INT4 三个量化版，但量都很小。
- 主仓库热度：likes 1,007，下载 16,976；Trending 从 #2 降到 #14。

```
已核
mistralai/Mistral-Large-4-1T-A52B
  技术报告提交: #12 2026-11-02 23:50 SGT (15:50 UTC)；#14 "Update technical report" 2026-11-03 02:30 SGT (11-02 18:30 UTC)
  license: other（Mistral Ecosystem Open-Weight License）    权重: 54 个    1,500 / 5,500    Trending #4
Nanbeige/Nanbeige4.3-33B-FP8   createdAt 2026-10-31 08:45 SGT (00:45 UTC)，lastModified 17:27 SGT (09:27 UTC)，apache-2.0，9 个权重，4 / 116
Nanbeige/Nanbeige4.3-33B-INT8  lastModified 2026-10-31 17:25 SGT (09:25 UTC)，4 / 64
Nanbeige/Nanbeige4.3-33B-INT4  lastModified 2026-10-31 17:41 SGT (09:41 UTC)，5 / 127
AA: Nanbeige4.3-33B Intelligence Index 20（解析值 20.4），isOpenWeights true，AA 记录发布日 2026-10-25
```

链接：[Mistral 技术报告 PDF](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B/blob/main/assets/technical_report.pdf) · [Mistral HF](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B) · [AA Nanbeige4.3-33B 模型页](https://artificialanalysis.ai/models/nanbeige4-3-33b) · [Nanbeige4.3-33B-FP8](https://huggingface.co/Nanbeige/Nanbeige4.3-33B-FP8)

---

## 二、旁线

- **Kimi K3.1 Pro：仍未开放。** Moonshot 官方博客写 "Full model weights will be released by Nov 4, 2026"（官方自述）。截至 11-03 09:19 SGT，moonshotai org 最新仓库仍是 [moonshotai/Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3)（最后修改 2026-09-02 10:22 SGT）。AA 的 K3.1 Pro 页面仍标注 "model weights are not publicly available"（isOpenWeights false，指数 46）。下期必须第一时间复查。[Moonshot 博客](https://www.kimi.ai/blog/kimi-k3-1-pro)
- **HuggingFaceBio/FineDNA**（数据集，本窗新发）：apache-2.0，基因组/DNA 训练数据，含真核各类群与 mRNA/剪接等 mid-training 配置，标签含 midtraining/sft/rl。createdAt 2026-10-30 19:42 SGT（11:42 UTC），40 / 4,441，数据集 Trending #12。[HF](https://huggingface.co/datasets/HuggingFaceBio/FineDNA)
- **google/gemma-4-12B-it 修复分词器**（本窗更新，维护类）：提交 #55 "Remediate 210 glitch tokens in tokenizer.json"，时间 2026-10-30 23:47 SGT（15:47 UTC），同日 gemma-4-12B 也有更新。下载量很大（1,718,827），用自带 tokenizer 的部署建议同步。[HF](https://huggingface.co/google/gemma-4-12B-it)
- **inclusionAI ZwZ2 官方 GGUF**（本窗新发，量化）：[27B](https://huggingface.co/inclusionAI/ZwZ2-27B-GGUF)、[9B](https://huggingface.co/inclusionAI/ZwZ2-9B-GGUF)、[4B](https://huggingface.co/inclusionAI/ZwZ2-4B-GGUF)，创建于 2026-10-30 17:45–18:28 SGT。likes 都只有 1–2，下载约 1k 级。
- **lodestones/chroma-h3**（本窗新发，社区微调）：基于 MiniMax-H3 的图像微调，许可证 minimax-h3-community-license（开放权重/自定义许可），createdAt 2026-10-31 09:41 SGT（01:41 UTC），40 / 52。[HF](https://huggingface.co/lodestones/chroma-h3)
- **ostris/primal_vae**（本窗新发）：apache-2.0 的 VAE，createdAt 2026-10-31 04:40 SGT（10-30 20:40 UTC），43 / 814。卡片信息少，待核用途。[HF](https://huggingface.co/ostris/primal_vae)
- **Edge0/Audio8-TTS-Realistic-Air**（热度新进，权重在窗前）：0.6B TTS，卡片称支持 23 种语言，apache-2.0，246 / 7,259，Trending #16。权重约在 10-27（窗前），窗内只改了 README。[HF](https://huggingface.co/Edge0/Audio8-TTS-Realistic-Air)
- **xiaomi-research/Xiaomi-OCR-0**（热度新进，非新发）：0.87B OCR，apache-2.0，245 / 18,472，Trending #30。权重是 09-30 的，窗内只换了 logo。[HF](https://huggingface.co/xiaomi-research/Xiaomi-OCR-0)
- **ccore/Qwen3.5-4B-3D-Coder**（热度延续）：Trending 从 #16 升到 #8，563 / 63,499。配套数据集 [ccore/ThreeJS-3D-Scenes](https://huggingface.co/datasets/ccore/ThreeJS-3D-Scenes) 在数据集榜 #10。属于社区微调。[HF](https://huggingface.co/ccore/Qwen3.5-4B-3D-Coder)
- **数据集榜其他新面孔**（多为老数据集回流）：[open-index/hacker-news](https://huggingface.co/datasets/open-index/hacker-news) #7、[lerobot/FineART](https://huggingface.co/datasets/lerobot/FineART) #22、[nvidia/Open-SWE-Traces](https://huggingface.co/datasets/nvidia/Open-SWE-Traces) #35、[codepawl/simready-glb](https://huggingface.co/datasets/codepawl/simready-glb) #8。榜首仍是 [nvidia/simready-assets](https://huggingface.co/datasets/nvidia/simready-assets)（1,270 / 1,213,121）。

---

## 三、榜单对比（对比 10-30 快照）

| 榜单 | 本期状态 | 变化 |
|---|---|---|
| LMArena 文本 | Oct 27 · 9,003,272 票 · 419 个模型 | **未刷新**。Gemini 4 Carbon 仍是 #1（1528±9，预备）；Mistral Large 4 #113（1432±6，12,066 票，标注 Proprietary）。Kimi K3.1 Pro、Ling 3.1、LFM3、MiniMax-M3.1-Flash、Nanbeige 都不在榜 |
| LMArena 视觉 | Oct 19 · 1,493,948 票 · 167 个模型 | **未刷新**。#1 Claude Fable 5 (High) 1309±7；Mistral Large 4 #52（1252±19，1,008 票） |
| LMArena 文生图 | Oct 26 · 6,872,557 票 · 82 个模型 | **未刷新**。#1 GPT-Image-2.5 Sunburst 1427±5（预备）。FLUX 3 / FLUX 3 Klein、Fibo 2.0、MAI-Image-2.7 都不在榜 |
| AA Intelligence Index v5 首页默认图 | 28 条 | **与 10-30 完全一致**。Gemini 4 Carbon 59.4 居首，Kimi K3.1 Pro 46.0。开放权重排序：DSV4.1 Flash 1017 32.5、GLM-5.3 31.7、MiMo-V2.6-Pro 29.9、Ling 3.1 Flash 29.5、MiniMax-M3.1-Flash 28.9、Step 5 Preview 28.5、Mistral Large 4 26.0 |
| AA 更新流（窗内新测评） | — | 10-30：DeepSeek V4.1 Flash 1017 (Non-reasoning)；11-01：Gemini 4 Carbon (Medium)、DSV4.1 Flash 1017 (High)；11-02：Gemini 4 Carbon (Low)、**Nanbeige4.3-33B（20）**。10-28 之后没有新文章 |
| AA 文生图 | 106 个模型 | 无新条目，只有 ±1 名漂移：FLUX 3 Klein #21→#22（1043）、Qwen-Image-2.1 #22→#21（1043）、Fibo 2.0 #23（1039）、FLUX 3 Image #13（1117）；Grok Imagine 2.0 与 MAI-Image-2.6 互换 #5/#6 |
| AA 图像编辑 | 77 个模型 | 无新条目。MAI-Image-2.7-Preview 仍为 #2，分数 1193→1195（4,914 个样本）；Krea 3 Ultra #5→#4；FLUX 3 Image #15（1122）、Fibo 2.0 #23（1088）、FLUX 3 Klein #27（1072） |

关注清单结论：Gemini 4 Carbon 的分数和名次不变，只是新增了 Low/Medium 档测评；Kimi K3.1 Pro 在 AA 仍按非开放权重计；Mistral Large 4 名次不变；Ling 3.1 Flash、LFM3、MiniMax-M3.1-Flash 都没有进入新的榜单；MAI-Image-2.7-Preview 编辑榜分数 +2；FLUX 3 Klein 和 Fibo 2.0 只有 ±1 名的漂移。

来源：[LMArena 文本](https://lmarena.ai/leaderboard/text) · [LMArena 视觉](https://lmarena.ai/leaderboard/vision) · [LMArena 文生图](https://lmarena.ai/leaderboard/text-to-image) · [AA 模型榜](https://artificialanalysis.ai/models) · [AA 文生图](https://artificialanalysis.ai/text-to-image/leaderboard) · [AA 图像编辑](https://artificialanalysis.ai/text-to-image/leaderboard/editing)

---

## 四、热度延续（只记变化，不展开）

| id | 当前 Trending（上期） | likes / downloads | 备注 |
|---|---|---|---|
| [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) | #1（#4） | 1,052 / 42,384 | 窗内只有 MLX 批量转换等维护 |
| [deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) | #2（#1） | 4,704 / 177,009 | 官方仓库无更新；新增 NVIDIA NVFP4 版，见重点 3 |
| [nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) | #3（#8） | 684 / 32,439 | — |
| [baidu/Unlimited-OCR-2](https://huggingface.co/baidu/Unlimited-OCR-2) | #5（#10） | 562 / 147,588 | — |
| [Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) | #7 | 10,365 / 2,467,613 | 老模型 |
| [Pika-Labs/Pika-H3-Flex](https://huggingface.co/Pika-Labs/Pika-H3-Flex) | #9（#70） | 361 / 491 | 上期旁线 |
| [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | #10 | 19,013 / 7,915,637 | Qwen 窗内无新仓库 |
| [black-forest-labs/flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy) | #12 | 2,356 / 1,003,813 | gated:auto；11-02 有维护提交 |
| [Nanbeige/Nanbeige4.3-33B](https://huggingface.co/Nanbeige/Nanbeige4.3-33B) | #14（#2） | 1,007 / 16,976 | 见重点 5 |
| [RecursiveSI/flint](https://huggingface.co/RecursiveSI/flint) | #21（#3） | 1,311 / 29,574 | 降温 |
| [MiniMaxAI/MiniMax-M3.1-Flash](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash) | #51（#6） | 541 / 23,530 | 10-30 加了 Terminal-Bench 结果（只改 README） |
| [openbmb/MiniCPM-OCR-1.0](https://huggingface.co/openbmb/MiniCPM-OCR-1.0) | #54（#20） | 402 / 4,191 | 只改 README |
| [inclusionAI/Ling-3.1-flash-1019](https://huggingface.co/inclusionAI/Ling-3.1-flash-1019) | #59（#74） | 94 / 1,851 | 11-02 只改 README |
| [CohereLabs/10-2026-qwen-investigation-traces](https://huggingface.co/datasets/CohereLabs/10-2026-qwen-investigation-traces) | 数据集 #4 | 104 / 6,227 | 10-27 期事件，无新进展 |

窗内没有新仓库的机构：openai、meta-llama、Qwen、deepseek-ai、moonshotai、zai-org 等。

---

## 五、降权 / 冒名 / 虚假声明

**冒名 / 虚假（单独列出，不进正文结论）**
- burner22/numbat（不放链接）：Trending #15，296 / 7,108，无许可证，createdAt 2026-10-23 09:37 SGT，772 个分片，HF 统计约 6.85T 参数。README 声称是约 14T 的 Anthropic "Mythos-class" 预训练中途检查点泄露。账号 2026-10-16 才注册，只有这一个模型，不隶属任何机构。社区独立审计显示，抽查的 norm 和 conv 张量都能由张量名逐位复现，权重是生成出来的，不是训练结果。**已判定为假，不要下载。**
  - 另有一个同名衍生 GGUF 空仓库（0 个文件），不放链接。
- 上期已标冒名的 K3.1 仓库：本期仍是 HF 上唯一「K3.1」命中，只有 README，没有权重，**不是 Moonshot 官方**，不放链接。
- Kimi-K3 个人转存：窗内新建 7 个，0 likes，是官方 K3 的镜像，**不是 K3.1**，不放链接。

**降权**
- [FusionCow/Sulphur-3](https://huggingface.co/FusionCow/Sulphur-3)：Trending #18，255 / 195，gated manual，无许可证，README 拿不到，来历不明。
- [deep-principle/Hydrogen-1.0](https://huggingface.co/deep-principle/Hydrogen-1.0)：gated auto，MIT，约 753B，downloads 0，卡片拿不到。gated:auto 不等于没发布，但目前没有可核验的信息。
- 去审查/改装类：OBLITERATUS、AtomicChat、huihui、orcarouter、dealignai 等的 abliterated/Uncensored 变体；DavidAU Heretic 系列；以及 akhaliq LoRA、nota-ai 剪枝版 Mistral、ISTA-DASLab Coder GGUF（dl 0）。
- 只做维护的官方提交：LiquidAI MLX 批量转换（11-03）、openbmb MiniCPM-OCR/V-4.7 README、reflection Beam 评测结果、Cloudflare clef 评测、BFL klein（11-03 07:49 SGT，gated auto）、nvidia Cosmos3/Dory 配置、tencent Youtu-Parsing-Omni logo、ibm granite-speech tokenizer、CohereLabs tiny-aya。

---

## 六、更正 / 待核 / 缺口

- **更正**：上期没有收录 speridlabs/idol（当时 Trending #192，33 likes）。本期补进重点，并注明权重在窗前。
- **待核**：
  - Mage-VL-Cowork 的 OSWorld 等成绩是自报，arXiv 页面只从项目页取到编号，没有逐页读。
  - SenseNova-Loop 的技术报告尚未发布。
  - DSV4.1-NVFP4 的基准是 NVIDIA 自测。
  - Mistral Large 4 技术报告只读了摘要和引言部分。
  - Idol 的显存/参数口径卡片与官方页不一致。
  - Nanbeige 的 AA 测评日期：更新流写 2 Nov，页面另一处片段显示 1 Nov。
- **缺口**：
  - LMArena 文本榜全表与 10-30 快照抽样逐行比对一致（头部日期、票数、模型数相同），快照沿用 10-30 表并加注；视觉榜和文生图榜本期逐行重存。
  - AA 首页只列 60 个模型，Nanbeige 的分数取自单独的模型页。
  - Sulphur-3 和 Hydrogen-1.0 是 gated 仓库，README 和提交记录都拿不到。
- **下期必查**：moonshotai 在 11-04 前后是否发布 Kimi K3.1 Pro 权重（要核对作者是 moonshotai、siblings 里有权重、license 与卡片一致）；LMArena 是否刷新；SenseNova-Loop 的技术报告。
