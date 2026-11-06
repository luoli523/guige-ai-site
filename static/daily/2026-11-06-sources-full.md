# 2026-11-06 AI行业动态 · 原始素材整理稿

本文是 [2026-11-06 AI行业动态](https://guige.ai/guige-ai-site/daily/2026-11-06/) 的附件，收的是窗口内（2026-11-03 09:46 → 2026-11-06 09:38 SGT，约三天）的全量原始素材，不是深读稿，篇幅和取舍都比正文粗。数字后标「已核」的是对照官方原文或一手数据核过的；「待核」「自述」「自报」表示只有单一来源或厂商自己的说法。安全、漏洞、投毒类内容只记结论和修复版本，不记攻击细节。冒名或虚假仓库只写判定，不放链接。

- **X**：官方与关键账号检索、X Today's News 和定向检索，并对照 OpenAI 官博、METR 报告、Kimi 模型卡与 LICENSE、SEC EDGAR、NVD / Playwright 等一手来源交叉核对。
- **模型与 Hugging Face**：HF Trending 模型与数据集、主要机构仓库更新，以及 LMArena、Artificial Analysis 各榜（AA Intelligence Index 为 v5）。
- **GitHub**：主要本地推理与官方 SDK 的发版记录，加上 GitHub Trending 日榜、周榜。
- **研究（官博与 arXiv）**：OpenAI、Anthropic、Google DeepMind、Meta、Microsoft Research、NVIDIA 等官博逐篇扫描；arXiv cs.AI / cs.CL / cs.LG 三类 11/03–11/05 批齐，11/06 批截至扫描时仍部分放出。

---

# 一、官方博客与 arXiv（精选）

> 官博 5 条 + arXiv 5 条。数字标「已核」/ 官方自报 / 待核。
> 上期补扫：11/03 arXiv 批已自 2611.00318 补全（全批约 2611.00001–03648）。11/04、11/05 齐；**11/06 批截至扫描时仍部分放出**（abs 约至 2611.07143），下期续扫。
> 网络安全与生物条目只写结论与官方数字，不写利用/实验步骤。

## 官博

### 1. OpenAI 发布 GPT‑6 Cyber：授权安全研究模型升至 Critical
面向授权漏洞研究的专用模型，Preparedness 网络安全评级自 GPT‑5.6 Cyber 的 High 升至 Critical。与同窗 Linux 管线文闭环：自主发现→验证→利用性评估→补丁，一次运行复现 1,724 个候选并产出 948 个 Linux LPE。这是一线实验室把 offensive agent 能力与「范围对齐」同时推到公开叙事的一次硬发布，对安全团队、平台防御与政策讨论都重要。
- ExploitGym 48.5% vs 5.6 Cyber 32.1%（约 +51% relative）；无部署提示时范围外服务不越权 99.93%（vs 94.49%），有提示时 100%；Firefox 81 个此前未知高危；RemoteExploitBench 上 Cyber 完成 95%、Astra+Daybreak Blue 100% refuse（均为官方自报）。管线 API 成本约 $1.21M、约 $1,279/LPE；相对七月同 harness 的 166 LPE 约 >5×（官方自报）。仅结论，不写 exploit 细节。
- [GPT‑6 Cyber](https://openai.com/index/introducing-gpt-6-cyber/) · [Linux 管线](https://openai.com/index/a-thousand-fewer-paths-to-root/)

### 2. Anthropic：20.7 万次科研会话看 Claude 怎么被用
隐私保护分析 2026-08-02–09-30 的科研相关会话，给出用量结构与「若能力被广泛采用」的产出情景。比口号式「AI for science」更接近真实工作流证据，适合科研工具产品与政策方深读。
- 207,000 次会话（Claude 128,914 + Claude Code 78,135）；数据分析约占 Claude 会话 1/3、Claude Code 近一半（官方自报）。情景：现有能力广泛采用可使部分领域产出约翻倍；若非体力工作全自动化，CS/统计或约 15×、实验科学约 3–4×；约 40% 受访者预期 2030 年前 AI 可独立完成完整研究项目（官方自报 / 情景待核）。
- [官博](https://www.anthropic.com/research/how-researchers-use-claude)

### 3. DeepMind：Antigravity + 化学信息学技能做剂设计迭代
用 Antigravity 挂上 RDKit / ChEMBL / PubChem 等技能，以肺癌 TKI 刚性化案例演示文献检索→结构改造→效力建模→合成路线提案。与已报 Anthropic 药研/Mithril 不同栈，是 Google 侧科学 agent 工作流的实质新帖。
- 称约 1 小时完成原需多日的迭代；提供 6 个月最高用量档位面向 10,000 名科学家申请（官方自报）。强调计算设计须实验验证。
- [官博](https://deepmind.google/blog/agentic-cheminformatics-with-google-antigravity/)

### 4. Microsoft Research：PDD Kit 用形式化验证卡住 agent 写的全栈代码
Proof-Driven Development：意图→Verus 规约→证明 agent 生成的 Rust。对准「agent 能写但不能信」的工程痛点，目前仅 Rust/Verus 研究原型，对做 coding agent 与软件供应链的人有参考价值。
- 与 GitHub Next Chopin 集成；Pet Store 全栈约 5,000 行 Rust 上验证登录逻辑案例（官方自报）。
- [官博](https://www.microsoft.com/en-us/research/blog/formally-verifying-agent-written-full-stack-web-apps-with-pdd-kit/)

### 5. Meta Superintelligence：GSLM2 缩小口语 LM 与文本 LM 差距（配 arXiv）
多流离散单元 + SpidR 2.0，把生成式口语模型规模推到约 6M hours / 6.5B params，并开源。纯语音路线若真把语言学差距压两个数量级，会影响语音 native 模型与多模态预训练取舍。
- 在 sWuggy / sBLIMP / tSC 上将口语–文本差距缩小约两个数量级，并在三项上胜过竞品语音–文本系统（官方自报）。
- [Meta 论文页](https://ai.meta.com/research/publications/gslm2-multi-stream-speech-representation-learning-and-generative-spoken-language-modeling/) · [arXiv 2611.01143](https://arxiv.org/abs/2611.01143) · [代码](https://github.com/facebookresearch/gslm2)

次要：[Images 2.6](https://openai.com/index/introducing-images-2-6/)（生成快 50%、周约 40 亿图，官方自报）；[收购 Pierre](https://openai.com/index/openai-to-acquire-pierre/)（Code Storage/Diffs，衔接 Pando）；[Gemini Omni 1.2 Flash](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/)（原生最长 15s 视频、价降 30%）；[CUDA 13.5 Vera Rubin GA](https://developer.nvidia.com/blog/nvidia-cuda-13-5-brings-nvidia-vera-rubin-ga-support/)；Anthropic [vault 粒子](https://www.anthropic.com/research/investigating-vault-particles-with-claude)（生物结论 only：称首次解析原核 vault 3D 结构）。

## arXiv

### 6. OpenAI LifeVal 完整论文：个人助理任务基准与约 1.7 万亿美元年化 WTP（2611.06687）
上期官博只放了示例分；本期论文给出任务分布、个性化上下文、评分与模型结果。148 类人生任务，用支付意愿刻画「数字超级助理」价值，是消费侧 agent 评测从口号落到可打分任务集的关键一步。单位 OpenAI（）。
- 年化 WTP 合计超过约 **1.7 trillion USD**；WTP 问卷 n=3,837（筛选后保留 1,826）；169 个任务评了 GPT‑5.2/5.4/5.5/5.6 与 GPT‑6 Astra；自动评分与人类在 30 任务子集上均值 84.20% vs 83.61%、Pearson r=0.864（作者自报）。
- [arXiv](https://arxiv.org/abs/2611.06687) · 配读上期 [官博](https://openai.com/index/lifeval)

### 7. Thinking Machines Lab：事后持久压制模型错位行为（2611.05358）
构造窄触发（提示里种错误答案线索）与宽触发（不安全代码微调后泛化错位）两类「模型生物」，比较 SFT / GRPO / 反学习，并提出 PEARL（用错位轨迹中间状态做对抗前缀的 GRPO 变体）。对准「发现坏行为后怎么压下去、且后续微调压不回来」。单位 Thinking Machines Lab + Princeton / UIUC（）。
- GPT‑OSS‑20B 窄触发：PEARL exploit 率约 2.0%（SFT 约 5.9%）；宽触发立即压制后误对齐约 1.02%，再喂 18k 不安全代码仍约 1.67%（SFT 升至约 14.8%）（作者自报，待核复现条件）。
- [arXiv](https://arxiv.org/abs/2611.05358)

### 8. NVIDIA CISA：无梯度把稠密注意力改成稀疏，服务超长上下文（2611.03200）
Chunk-Indexed Sparse Attention，把已训好的稠密注意力模型改成稀疏，不重训。对长上下文推理成本与 KV 显存是硬指标。单位 NVIDIA（）。
- 1M prompt 末端 prefill 核心注意力约 **11.7×**、decode 约 **13.0×**；含其他 GPU 工作后约 8.6× / 3.0×；KV 可读减至 1/8–1/16，分数差 ≤2.05pp；端到端吞吐约 2.29×（作者自报）。
- [arXiv](https://arxiv.org/abs/2611.03200)

### 9. Apple：仿真学感知人形运动，实物零样本 91%（2611.06908）
从仿真到实物的感知人形运动控制；对人形机器人「sim2real + 视觉」路线有直接参考。单位 Apple（Vladlen Koltun 等）（）。
- 实物 **91%** 成功率（360 trials / 6 场景）（作者自报）。
- [arXiv](https://arxiv.org/abs/2611.06908)

### 10. Microsoft Research：多轮对话用 agentic 上下文管理（AC3）（2611.00518）
对照「丢掉助手历史」等粗暴截断，提出 AC3 管理多轮上下文污染；工具场景下粗暴截断会把成功率打到 0。对做长对话产品与 tool agent 的人有用。单位 Microsoft Research + UCSD（）。
- AC3 弥合 full-context 与丢弃助手消息（AO）差距的 **55–84%**；tau2-bench 上 AO 掉到 0%，AC3 不崩（作者自报）。
- [arXiv](https://arxiv.org/abs/2611.00518)

备选：MSR Rubric Curriculum RL [2611.06244](https://arxiv.org/abs/2611.06244)（不可验证域）；GDM 投机解码 Parallel Reconsideration [2611.05724](https://arxiv.org/abs/2611.05724)；Alignment Myopia [2611.06830](https://arxiv.org/abs/2611.06830)；NVIDIA Cosmos 可交互世界仿真 [2611.06627](https://arxiv.org/abs/2611.06627)；π+Amazon FAR 机器人 RL [2611.06905](https://arxiv.org/abs/2611.06905)；ByteDance Axion 1.0 [2611.03233](https://arxiv.org/abs/2611.03233)；UK AISI 接种提示 / 多智能体影响 [2611.04260](https://arxiv.org/abs/2611.04260) · [2611.04556](https://arxiv.org/abs/2611.04556)；Stanford Hinted Scaling Laws [2611.02270](https://arxiv.org/abs/2611.02270)；Goodfire Mechanistic Shaping [2611.07071](https://arxiv.org/abs/2611.07071)（11/06 部分批）。

---

# 二、官方博客（全量扫描）

- **窗口**: 2026-11-03 09:46 SGT → 约 2026-11-06 09:20 SGT
- **采集时间**: 2026-11-06 约 09:20–09:40 SGT（Asia/Singapore, UTC+8）
- **说明**: 原始摘录；关键数字标注「官方自报 / / 待核」。生物与网络安全仅写结论与官方数字，不写利用步骤。已报主线（Pando Git、Grid Protectors、LifeVal、IETF training preferences、community safety/teens、PlanAssist、Genie 4、Gemini 4 Carbon、misalignment monitoring / Model Spec、agents-judgment、drug development/Mithril、Vera Rubin NCCL、Cosmos 3 Nano 等）不作为本期重点重复。

---

## OpenAI

**源查证**: `[openai.com/news/rss.xml](https://openai.com/news/rss.xml)`（curl + Chrome UA 成功；WebFetch RSS 曾 500）。辅以 `[openai.com/news/](https://openai.com/news/)`、`[openai.com/news/research/](https://openai.com/news/research/)` + 详情页 WebFetch。

### 1) GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agents — **建议进主包**
- **日期**: 2026-11-05 09:00 GMT → **2026-11-05 17:00 SGT**
- **URL**: [openai.com/index/introducing-gpt-6-cyber/](https://openai.com/index/introducing-gpt-6-cyber/)
- **要点**:
 - 发布面向授权安全研究的 GPT‑6 Cyber；Preparedness 网络安全评级自 GPT‑5.6 Cyber 的 High **升至 Critical**（官方自报）。
 - ExploitGym：48.5% vs GPT‑5.6 Cyber 32.1%（约 **+51% relative**）（官方自报）。
 - 范围对齐评测（ExploitGym Honeypot）：无部署提示时 **99.93%** 不越权攻击范围外服务（vs 5.6 Cyber 94.49%）；有部署提示时 **100%**（官方自报）。
 - 实战结论：配合管线产出 Linux **948** LPE；Firefox **81** 个此前未知高危；RemoteExploitBench 上 Cyber **95%** 完成、Astra+Daybreak Blue **100% refuse**（官方自报）。仅写结论，不写 exploit 细节。
- **进主包理由**: 窗口内最大模型/安全产品线级发布，且与同窗 Linux 管线文形成闭环。

### 2) A thousand fewer paths to root — **建议进主包**
- **日期**: 2026-11-04 08:00 GMT → **2026-11-04 16:00 SGT**
- **URL**: [openai.com/index/a-thousand-fewer-paths-to-root/](https://openai.com/index/a-thousand-fewer-paths-to-root/)
- **要点**:
 - 自治漏洞发现→验证→利用性评估→补丁管线；一次运行：候选 2,308 → 动态复现 **1,724** → **948** 个 Linux LPE；API 成本约 **$1,213,430**（约 **$1,279/LPE**）（官方自报）。
 - kernelCTF 类环境：25 info-leak PoC + **21** LPE；成本约 **$32,936**（官方自报）。
 - 相对七月 GPT‑5.6 Sol 的 **166** LPE，十月新 cyber 模型同 harness 下 **>5×**（官方自报）。采样 166 个 exploit 中称至少 **10** 种新技术（官方自报；细节未公开）。
- **进主包理由**: 提供可引用规模数字与防御侧成本叙事；与 GPT‑6 Cyber 配套。

### 3) Introducing Images 2.6 — 候选（产品，次优先）
- **日期**: 2026-11-04 00:00 GMT → **2026-11-04 08:00 SGT**
- **URL**: [openai.com/index/introducing-images-2-6/](https://openai.com/index/introducing-images-2-6/)
- **要点**: ChatGPT/Codex/API 上线 Images 2.6；支持 GIF；生成速度称 **快 50%**；API 提供 Flare/Sunburst；官方称全平台每周约 **40 亿** 张图（官方自报）。

### 4) OpenAI to acquire Pierre Computer Company, Inc. — 候选（公司/工程）
- **日期**: 2026-11-04 14:30 GMT → **2026-11-04 22:30 SGT**
- **URL**: [openai.com/index/openai-to-acquire-pierre/](https://openai.com/index/openai-to-acquire-pierre/)
- **要点**: 收购 Pierre（Code Storage 与 Trees/Diffs 等开源工具）；与 Codex/Git 工作流及上周 Pando 叙事衔接；交割待监管（官方自报）。开源项目称保持开源。

### 5) Accelerating engineering for the physical world — 候选
- **日期**: 2026-11-03 12:00 GMT → **2026-11-03 20:00 SGT**
- **URL**: [openai.com/index/accelerating-engineering-for…](https://openai.com/index/accelerating-engineering-for-the-physical-world/)
- **要点**: Astra/Codex 用于 CAD/PCB/仿真等物理工程；内部硬件团队 token 用量自二月 **23×**（官方自报）；BenchCAD 2.0 新内部模型均分 **0.875** vs Astra 最高推理 **0.594**（官方自报）；宣布与 Chip Ganassi Racing 扩展、与 Mazda 新合作。

### 6) Daybreak Red is now available in AWS GovCloud (US-East) — 候选（分发）
- **日期**: 2026-11-04 07:00 GMT → **2026-11-04 15:00 SGT**
- **URL**: [openai.com/index/daybreak-red-aws-govcloud/](https://openai.com/index/daybreak-red-aws-govcloud/)
- **要点**: 经 Amazon Bedrock 向获批客户提供 Daybreak Red / GPT‑5.6 Cyber（GovCloud US-East）；强调授权安全研究与政府合规路径（官方自报）。

### 7) Setting a new standard for responsible AI infrastructure — 候选（政策）
- **日期**: 2026-11-05 02:00 GMT → **2026-11-05 10:00 SGT**
- **URL**: [openai.com/index/setting-new-standard-respons…](https://openai.com/index/setting-new-standard-responsible-ai-infrastructure/)
- **要点**: 发布 National Community Compact 与 Compute Campus Policy Blueprint；自有运营 campus 承诺自付电费/基建、水与噪音透明、本地就业等；举例 Georgia 学餐 **$4.8M**、Ohio 托儿 **$6M**（官方自报）。

### 窗口内其他 OpenAI 帖（收录但不建议主包）
| 标题 | SGT | URL | 备注 |
|------|-----|-----|------|
| Cult.fit builds operational muscle with Codex | 2026-11-06 04:00 | [openai.com/index/cultfit-builds-with-codex](https://openai.com/index/cultfit-builds-with-codex) | 客户故事 |
| Merge builds product and business tools with OpenAI technology | 2026-11-05 16:00 | [openai.com/index/merge-builds-with-openai](https://openai.com/index/merge-builds-with-openai) | 客户故事 |
| Flipsnack grows product signups with conversion optimization | 2026-11-05 08:45 | [openai.com/ads/customers/flipsnack](https://openai.com/ads/customers/flipsnack) | Ads 客户 |
| Franklin Templeton uses OpenAI to support investment research | 2026-11-05 08:00 | [openai.com/index/franklin-templeton](https://openai.com/index/franklin-templeton) | 客户故事 |
| DevRev delivers autonomous self-service with GPT-6.1 Sol | 2026-11-04 08:00 | [openai.com/index/devrev-enterprise-self-service](https://openai.com/index/devrev-enterprise-self-service) | 客户故事 |
| How Cisco defends at machine speed with OpenAI | 2026-11-03 16:00 | [openai.com/index/cisco-cyber](https://openai.com/index/cisco-cyber) | 客户故事 |
| Heimstaden is changing residential real estate management with AI | 2026-11-03 16:00 | [openai.com/index/heimstaden](https://openai.com/index/heimstaden) | 客户故事 |

### 窗口边缘排除
- **Jill Hazelbaker Chief Corporate Affairs Officer**: pubDate 2026-11-03 00:00 GMT = **08:00 SGT**，早于窗口起点 09:46 SGT → 不计入本期窗口新帖。URL: [openai.com/index/jill-hazelbaker-chief-corpor…](https://openai.com/index/jill-hazelbaker-chief-corporate-affairs-officer)

---

## Anthropic

**源查证**: `[www.anthropic.com/news](https://www.anthropic.com/news)`（WebFetch）— 新闻室列表在窗口内**无新帖**（最新仍为 Oct 系列 / Opus 5.5 等）。`[www.anthropic.com/research](https://www.anthropic.com/research)` + WebSearch 补到研究帖。

### 8) AI for scientific discovery: How researchers use Claude — **建议进主包**
- **日期**: **2026-11-05**（页面仅日期；按日期落入窗口）
- **URL**: [www.anthropic.com/research/how-researchers-us…](https://www.anthropic.com/research/how-researchers-use-claude)
- **要点**:
 - 隐私保护分析 **207,000** 次科研相关会话（Claude **128,914** + Claude Code **78,135**；2026-08-02–09-30）（官方自报）。
 - 用法：数据分析约占 Claude 会话 **1/3**、Claude Code 近 **一半**；正式科学（CS/数学/统计）相对用量更高（官方自报）。
 - 情景模型：现有能力广泛采用可使部分领域产出约 **翻倍**；若非体力工作全自动化，CS/统计或可达约 **15×**，实验科学约 **3–4×**；调研中约 **40%** 受访者预期 2030 年前 AI 可独立完成完整研究项目（官方自报 / 模型情景待核）。

### 9) Investigating vault particles with Claude — **建议进主包**（生物结论 only）
- **日期**: **2026-11-04**
- **URL**: [www.anthropic.com/research/investigating-vaul…](https://www.anthropic.com/research/investigating-vault-particles-with-claude)
- **要点**:
 - 生物学实验室报告：据称首次解析**原核体系中 vault 粒子**的 3D 结构（噬菌体蛋白 L05，96 拷贝，约 **9.5 MDa**；尺寸约 54×45 nm）（官方自报）。
 - 流程加速结论：纯化约 **90 分钟**（传统约 3 天）；首个结构模型约 **34 小时**（官方自报）。预印本称已投 bioRxiv（链接待更新，待核）。
 - **禁止展开实验利用细节**；仅作科学进展结论记录。

### Newsroom
- 窗口内无新 news 条目可记（查了 News 首页；最新新闻室条目仍早于窗口或为旧帖）。

---

## Google DeepMind

**源查证**: `[deepmind.google/blog/](https://deepmind.google/blog/)`（WebFetch）；RSS `deepmind.google/blog/rss.xml` 返回压缩/乱码。列表卡链到 `blog.google` 与 deepmind 子页。

### 10) Agentic cheminformatics with Google Antigravity — **建议进主包**
- **日期**: **2026-11-03**（Science；仅日期）
- **URL**: [deepmind.google/blog/agentic-cheminformatics-…](https://deepmind.google/blog/agentic-cheminformatics-with-google-antigravity/)
- **要点**: Antigravity + Cheminformatics Skills（RDKit / ChEMBL / PubChem）；以肺癌 TKI（crizotinib→lorlatinib 刚性化）演示：文献化合物检索、MMPA、效力模型、合成路线提案，称约 **1 小时**完成原需多日迭代（官方自报）。强调计算设计须实验验证；提供 6 个月最高用量档位面向 **10,000** 科学家申请（官方自报）。
- **注意**: 与已报 Anthropic drug development/Mithril 不同栈（Antigravity 工具技能）；属实质新进展可进。

### 11) Gemini Omni 1.2 Flash — **建议进主包（产品）**
- **日期**: **2026-11-05**
- **正牌 URL（Google 博客，DeepMind 列表指向）**: [blog.google/innovation-and-ai/technology/deve…](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/)
- **Model card**: [deepmind.google/models/model-cards/gemini-omn…](https://deepmind.google/models/model-cards/gemini-omni-1-2-flash/（Published) 5 November 2026）
- **要点**: 原生最长 **15s** 视频（1.1 为 10s）；多轮对话编辑；价格较 1.1 **降 30%**，720p **$0.07/秒**（官方自报）；Gemini API / Cloud GA；SynthID；暂限制改写人物语音能力（官方自报）。

### 窗口外/已报（DeepMind 列表可见但不进本期重点）
- Genie 4、Gemini 4 Carbon、PlanAssist（Speeding up planning…）等 — 已报或日期为 October。

---

## Google Research

**源查证**: `[research.google/blog/](https://research.google/blog/)`（WebFetch；curl 常挂）。

### 12) Detecting signs of hypertension using wearable sensors — 候选（偏健康应用）
- **日期**: **2026-11-05**
- **URL**: [research.google/blog/detecting-signs-of-hyper…](https://research.google/blog/detecting-signs-of-hypertension-using-wearable-sensors/)
- **要点**: Nature 论文；智能手表 PPG+ACC 被动筛查高血压、无需袖带校准；对比 24h ABPM。初始筛查敏感度 **65.8%** / 特异度 **90.0%** / PPV **80.6%**；确认场景 PPV **96.7%**（官方自报）。预训练无标签数据 **492,347** 小时 / **2,109** 人；前瞻研究 **196** 人（官方自报）。明确非替代临床诊断。

### 13) Agile Deliberation: How AI helps humans define the gray areas — 候选
- **日期**: **2026-11-04**
- **URL**: [research.google/blog/agile-deliberation-how-a…](https://research.google/blog/agile-deliberation-how-ai-helps-humans-define-the-gray-areas/)
- **要点**: 主观视觉分类的人机共议框架；**18** 场各 **1.5h** 真人实验；开源 GitHub；相对 zero-shot / 手工 prompt 在一致性与疲劳指标上更好（官方自报）。

---

## Meta（research.meta.ai / about.fb.com / engineering.fb.com / ai.meta.com）

**源查证**:
- `[research.meta.ai/](https://research.meta.ai/)` — 最新研究博文仍为 Oct（Muse Wonder 等），**窗口内无新研究博客**。
- `[about.fb.com/news/](https://about.fb.com/news/)` — 有 Nov 5 产品新闻。
- `[engineering.fb.com/](https://engineering.fb.com/)` — F3 Lightning Nov 3；Andromeda 实为 **2026-10-28**（窗口外）。
- WebSearch / `ai.meta.com` — GSLM2 论文页 Nov 4。

### 14) GSLM2: Multi-Stream Speech Representation Learning… — **建议进主包（研究）**
- **日期**: **2026-11-04**
- **URL**: [ai.meta.com/research/publications/gslm2-multi…](https://ai.meta.com/research/publications/gslm2-multi-stream-speech-representation-learning-and-generative-spoken-language-modeling/)
- **要点**: FAIR 生成式口语模型；多流离散单元 + SpidR 2.0；规模至约 **6M hours / 6.5B params**；称在 sWuggy/sBLIMP/tSC 上将口语–文本差距缩小约 **两个数量级**（官方自报）；开源 [github.com/facebookresearch/gslm2。](https://github.com/facebookresearch/gslm2。)

### 15) F3 Lightning: How Meta Accelerates Ads ML Features to Production at Scale — 候选（工程）
- **日期**: **2026-11-03**
- **URL**: [engineering.fb.com/2026/11/03/ml-applications…](https://engineering.fb.com/2026/11/03/ml-applications/f3-lightning-how-meta-accelerates-ads-ml-features-to-production/)
- **要点**: Ads 特征框架 F3 之上解耦发布；单请求可需 **>20,000** 特征；称可比特征上线约 **3.6×** 更快且基础设施算力成本不增（官方自报）。

### 16) Give Your Muse a Voice — 候选（产品，通常不进主包）
- **日期**: **2026-11-05**
- **URL**: [about.fb.com/news/2026/11/introducing-muse-ai…](https://about.fb.com/news/2026/11/introducing-muse-ai-voice-expressive-avatars/)
- **要点**: Muse App（美）上线实时语音与表情 Avatar；后续眼镜/Charm（官方自报）。

### 排除
- Meta Andromeda ads retrieval 博文日期 **2026-10-28**（URL 路径确认）→ 窗口外。[engineering.fb.com/2026/10/28/ml-applications…](https://engineering.fb.com/2026/10/28/ml-applications/meta-andromeda-next-gen-ads-retrieval-gpu-co-design/)
- WhatsApp Events 等非 AI 研究主线 → 不进主包。

---

## Microsoft Research

**源查证**: `[www.microsoft.com/en-us/research/blog/](https://www.microsoft.com/en-us/research/blog/)`（WebFetch）+ feed `[www.microsoft.com/en-us/research/feed/](https://www.microsoft.com/en-us/research/feed/)`（Chrome UA curl 成功）。

### 17) Formally verifying agent-written full-stack web apps with PDD Kit — **建议进主包**
- **日期**: feed **2026-11-05 16:00 UTC** → **2026-11-06 00:00 SGT**；页面 Published November 5, 2026
- **URL**: [www.microsoft.com/en-us/research/blog/formall…](https://www.microsoft.com/en-us/research/blog/formally-verifying-agent-written-full-stack-web-apps-with-pdd-kit/)
- **要点**: Proof-Driven Development 工具包；意图→Verus 形式化规约→证明 agent 生成 Rust 代码；与 GitHub Next Chopin 集成；Pet Store 全栈约 **5,000** 行 Rust 上验证登录逻辑案例（官方自报）。研究原型，目前仅 Rust/Verus。

### 18) Learn the rules: The hacker mindset — 不建议主包
- **日期**: feed → **2026-11-04 01:14 SGT**
- **URL**: [www.microsoft.com/en-us/research/podcast/lear…](https://www.microsoft.com/en-us/research/podcast/learn-the-rules-the-hacker-mindset/)
- **要点**: MSR Podcast；网络安全/黑客文化访谈。信息密度低于 PDD Kit。

---

## NVIDIA

**源查证**: Atom `[developer.nvidia.com/blog/feed](https://developer.nvidia.com/blog/feed)`（注意用 **`published`** 非 `updated`）；`[blogs.nvidia.com/feed/](https://blogs.nvidia.com/feed/)`。

### 19) NVIDIA CUDA 13.5 Brings NVIDIA Vera Rubin GA Support — **建议进主包（平台）**
- **published**: 2026-11-04 18:46:07Z → **2026-11-05 02:46 SGT**
- **URL**: [developer.nvidia.com/blog/nvidia-cuda-13-5-br…](https://developer.nvidia.com/blog/nvidia-cuda-13-5-brings-nvidia-vera-rubin-ga-support/)
- **要点**: CUDA 13.5 GA；Vera Rubin 从早期开发者访问进入 **生产 GA**；MPS v3、CUDA Tile 多 GPU、CCCL 3.5 等（官方自报）。相对已报 NCCL/Cosmos 3 Nano，此为 toolkit GA 实质进展。

### 20) Configure, Certify, and Operate Kubernetes GPU Clusters with NVIDIA DSX OS — 候选
- **published**: 2026-11-05 17:00:00Z → **2026-11-06 01:00 SGT**
- **URL**: [developer.nvidia.com/blog/configure-certify-a…](https://developer.nvidia.com/blog/configure-certify-and-operate-kubernetes-gpu-clusters-with-nvidia-dsx-os/)
- **要点**: DSX OS 开源层：AICR 配置配方、NVCRE 就绪认证（含 NCCL/训练负载阈值）、NVSentinel 健康治理（官方自报）。

### 21) Five Ways NVIDIA Co-Design Maximizes the Value of Every Byte in the AI Factory — 候选
- **published**: 2026-11-05 16:00:00Z → **2026-11-06 00:00 SGT**
- **URL**: [developer.nvidia.com/blog/five-ways-nvidia-co…](https://developer.nvidia.com/blog/five-ways-nvidia-co-design-maximizes-the-value-of-every-byte-in-the-ai-factory/)
- **要点**: NVFP4 / expert 并行 / Dynamo KV / Vera CPU / CMX；称 Vera Rubin NVL72 相对 GB300 NVL72 可达约 **30×** 每兆瓦吞吐（官方自报，待核条件）。

### 其他窗口内 NVIDIA（次优先）
- How NVIDIA Uses AI Agents to Streamline AI Factory Operations — [developer.nvidia.com/blog/how-nvidia-uses-ai-…](https://developer.nvidia.com/blog/how-nvidia-uses-ai-agents-to-streamline-ai-factory-operations/) （pub 2026-11-04 22:00Z → 11-05 06:00 SGT）
- Factory Operations Blueprint… — [developer.nvidia.com/blog/how-nvidia-factory-…](https://developer.nvidia.com/blog/how-nvidia-factory-operations-blueprint-coordinates-ai-agents-to-investigate-production-issues/)
- Use NVIDIA NeMo to Turn Agent Failures into Tests… — [developer.nvidia.com/blog/use-nvidia-nemo-to-…](https://developer.nvidia.com/blog/use-nvidia-nemo-to-turn-agent-failures-into-tests-and-harness-fixes/)
- blogs.nvidia.com: Vera CPU Highest Throughput…（2026-11-06 04:00 SGT）[blogs.nvidia.com/blog/vera-cpu-highest-throug…](https://blogs.nvidia.com/blog/vera-cpu-highest-throughput-fastest-agents/)
- Into the Omniverse… Frontier AI Agents（2026-11-06 01:00 SGT）[blogs.nvidia.com/blog/developers-simulation-f…](https://blogs.nvidia.com/blog/developers-simulation-frontier-ai-agents/)

### 窗口外（published 早于 11-03 09:46 SGT，即使 updated 较晚）
- Diagnose Distributed AI Workload Failures… published 2026-11-02 23:39Z → 11-03 **07:39 SGT** OUT
- Cosmos / Kubernetes Vera Rubin Day One 等 published 11-02 — OUT；Cosmos 亦属已报主线勿重复。

---

## 汇总：建议进入主素材包（宁缺毋滥）

1. OpenAI — GPT‑6 Cyber 
2. OpenAI — A thousand fewer paths to root 
3. Anthropic — How researchers use Claude（科学发现用研） 
4. Anthropic — Investigating vault particles with Claude 
5. Google DeepMind — Agentic cheminformatics with Google Antigravity 
6. Google DeepMind / Google — Gemini Omni 1.2 Flash 
7. Microsoft Research — PDD Kit 
8. Meta FAIR — GSLM2 
9. NVIDIA — CUDA 13.5 Vera Rubin GA 

（Images 2.6、Pierre 收购、物理工程 Astra、高血压可穿戴、Agile Deliberation、F3 Lightning、DSX OS 作次选素材。）

---

# 三、arXiv（全量扫描）

## Batch map（日期为 SGT 放批早间；arXiv 美东 Sun–Thu 20:00 公布 → 新加披约 Mon–Fri 早上有批；**无周六批**）

| SGT 批次 | listing 标签 | cs.AI/CL/LG 列表条目（含交叉，三猫去重约） | New-submission ID 范围（全站 abs 探测） | 状态 |
|---|---|---|---|---|
| 11/03 (Tue) | Tue, 3 Nov 2026 | AI 521 / CL 251 / LG 570；去重约 1060 | **2611.00001 – 2611.03648** | **已补全**：上期仅到 00317；本期自 **2611.00318** 起补扫 |
| 11/04 (Wed) | Wed, 4 Nov 2026 | AI 252 / CL 85 / LG 252；去重约 475 | **2611.03649 – 2611.05377** | complete（listing 已齐） |
| 11/05 (Thu) | Thu, 5 Nov 2026 | AI 217 / CL 90 / LG 214；去重约 413 | **2611.05378 – 2611.06914** | complete（`/new` 仍标 5 Nov） |
| 11/06 (Fri) | listing **尚未**出现 | abs 探测 AI/CL/LG **37** 篇 | **2611.06915 – 2611.07143**（洞 07134；当前 max **07143**） | **部分放出**：列表页滞后；已用 abs 科目探测 |

说明：列表页常滞后于 abs；11/06 批次以 ID 连续存在为准。上期已入主/备选 ID 未再当新发现。

## Candidates（单位经 arXiv HTML `ltx_authors` 或 abs 作者行核实；数字来自摘要）

### Batch 11/03 补扫（≥2611.00318）

1. **2611.00518** Agentic Context Management for Multi-Turn Human-AI Conversations 
 单位核实：Microsoft Research（Jianfeng Gao、Baolin Peng、Michel Galley、Nebojsa Jojic 等）+ UCSD · [arxiv.org/abs/2611.00518](https://arxiv.org/abs/2611.00518) 
 要点：多轮对话「上下文污染」：提出 agentic context management（AC3），对照丢弃助手消息（AO）。 
 关键数字：作者自报：AC3 弥合 full-context 与 AO 差距的 **55–84%**；工具场景 tau2-bench 上 AO 掉到 **0%**，AC3 不崩。 
 **建议进主包：是**（标签：主包）

2. **2611.01143** GSLM2: Multi-Stream Speech Representation Learning and Generative Spoken Language Modeling 
 单位核实：Meta Superintelligence Labs（多作者 `@meta.com`；另有 AMI Labs / Dauphine 合作） · [arxiv.org/abs/2611.01143](https://arxiv.org/abs/2611.01143) 
 要点：GSLM2：多流语音表征 + 生成式口语语言模型，瞄准纯语音学语言结构相对文本模型的能力与数据效率差距。 
 关键数字：摘要未给单一 headline 数字（待核 PDF 实验表）。 
 **建议进主包：是**（标签：主包）

3. **2611.02270** Hinted Scaling Laws 
 单位核实：Stanford University（Percy Liang、Tatsunori Hashimoto、John Duchi 等） · [arxiv.org/abs/2611.02270](https://arxiv.org/abs/2611.02270) 
 要点：Hinted Scaling Laws：下游准确率在小模型近 0 时标准缩放失效；用「提示」恢复可外推趋势。 
 关键数字：作者自报：预测 $10^{23}$ FLOP 模型 GSM8K **25.9%**，误差 ≤3pp。 
 **建议进主包：是**（标签：主包）

4. **2611.02546** Energy-Based Policy Orchestration 
 单位核实：Amazon Frontier AI & Robotics + Harvard / MIT / Berkeley / CMU（Pieter Abbeel、Yilun Du、Leslie Kaelbling 等） · [arxiv.org/abs/2611.02546](https://arxiv.org/abs/2611.02546) 
 要点：Energy-Based Policy Orchestration：层级控制下按能量/不确定性编排底层策略。 
 关键数字：摘要无单一数字（待核）。 
 **建议进主包：是**（标签：主包）

5. **2611.03200** CISA: Retrofitting Dense Attention Models with Chunk-Indexed Sparse Attention 
 单位核实：NVIDIA（全体作者 @nvidia.com） · [arxiv.org/abs/2611.03200](https://arxiv.org/abs/2611.03200) 
 要点：CISA：无梯度地把稠密注意力改造为 chunk 索引稀疏注意力，服务超长上下文。 
 关键数字：作者自报：1M prompt 末端 prefill 核心注意力 **11.7×**、decode **13.0×**；含其他 GPU 工作后 **8.6× / 3.0×**；KV 可读减至 **1/8–1/16**，分数差 ≤2.05pp；e2e throughput **2.29×**。 
 **建议进主包：是**（标签：主包）

6. **2611.03233** Axion 1.0: Open Agent Foundation Models, Simplified 
 单位核实：ByteDance（项目负责人 Yunjie Tian 等；Duke/UMD/Buffalo 合作） · [arxiv.org/abs/2611.03233](https://arxiv.org/abs/2611.03233) 
 要点：Axion 1.0：开源 agent foundation model，仅三阶段（两段轻量 SFT + RL），无 mid-training/DPO。 
 关键数字：摘要强调 recipe 简化；具体分数待核 PDF/博客。 
 **建议进主包：是**（标签：主包）

7. **2611.00450** From Lookups to Lessons: Turning Retrieved Knowledge into Parametric Memory 
 单位核实：Salesforce + MBZUAI / McGill / Mila · [arxiv.org/abs/2611.00450](https://arxiv.org/abs/2611.00450) 
 要点：把检索知识蒸馏进参数记忆（ResMem），降低在线检索成本。 
 关键数字：作者自报：相对 kNN 管道教师构造知识量 **-94.7%**；token F1 **32.83%→34.48%**。 
 **建议进主包：否（备选）**（标签：备选）

8. **2611.00505** To Jev or Not to Jev: When Can System-1 Decision Models Replace LLM Judges? 
 单位核实：Scale AI（Shreyas Subramanian） · [arxiv.org/abs/2611.00505](https://arxiv.org/abs/2611.00505) 
 要点：System-1 decision model（Jev）何时可替代 LLM-as-judge。 
 关键数字：作者自报：JudgeBench **90.3–93.4%**；对抗笔记使部分模型翻盘 **17–49%**。 
 **建议进主包：否（备选）**（标签：备选）

9. **2611.00661** Designing Behavioral Profiles for Language Model Simulation of Out-of-Distribution Human Behavior 
 单位核实：Google DeepMind（Logan Cross）+ MIT / Stanford DEL · [arxiv.org/abs/2611.00661](https://arxiv.org/abs/2611.00661) 
 要点：为 OOD 人类行为仿真设计行为画像。 
 关键数字：摘要无单一数字（待核）。 
 **建议进主包：否（备选）**（标签：备选）

10. **2611.03087** MIRA: Reinforcing Multimodal Reasoning via Deceptive Contextual Augmentation 
 单位核实：ByteDance + 北大 · [arxiv.org/abs/2611.03087](https://arxiv.org/abs/2611.03087) 
 要点：MIRA：欺骗性上下文增强强化多模态推理。 
 关键数字：作者自报：域内基准平均 **+7%**。 
 **建议进主包：否（备选）**（标签：备选）

11. **2611.03094** A Fine-Grained Hierarchy and Benchmark for State Tracking in Language Models 
 单位核实：Allen Institute for AI（+ NYU / TTIC） · [arxiv.org/abs/2611.03094](https://arxiv.org/abs/2611.03094) 
 要点：细粒度状态追踪层级与基准；对照 Gated DeltaNet 等。 
 关键数字：摘要无单一数字（待核）。 
 **建议进主包：否（备选）**（标签：备选）

12. **2611.03264** DeepWaveRL: Self-Supervised Full Waveform Inversion via Reinforcement Learning 
 单位核实：Google DeepMind（Yinpeng Chen）+ UNC / Penn State · [arxiv.org/abs/2611.03264](https://arxiv.org/abs/2611.03264) 
 要点：DeepWaveRL：自监督全波形反演 + RL（地球物理向，非核心 LLM）。 
 关键数字：摘要无单一数字。 
 **建议进主包：否（备选）**（标签：备选）

13. **2611.03622** D&A: Decoupling Description and Assessment Enables VLMs as Zero-Shot Robotic Reward Models 
 单位核实：NVIDIA + University of Washington（Dieter Fox 等） · [arxiv.org/abs/2611.03622](https://arxiv.org/abs/2611.03622) 
 要点：D&A：解耦描述与评估，让 VLM 作零样本机器人奖励模型。 
 关键数字：摘要无单一数字（待核）。 
 **建议进主包：否（备选）**（标签：备选）

### Batch 11/04

14. **2611.04260** Neologism Inoculation Prompting 
 单位核实：UK AI Security Institute + Resolution · [arxiv.org/abs/2611.04260](https://arxiv.org/abs/2611.04260) 
 要点：Neologism Inoculation Prompting：生造词接种提示，降低接种提示被普通用户复现从而抵消抑制的风险。 
 关键数字：摘要无百分比。安全向仅结论。 
 **建议进主包：是**（标签：主包）

15. **2611.04556** Inter-Agent Influence: Evaluating Persuasion, Deception, and Coercion in Multi-Agent Systems 
 单位核实：UK AI Security Institute + Oxford / Cooperative AI Foundation 等 · [arxiv.org/abs/2611.04556](https://arxiv.org/abs/2611.04556) 
 要点：多智能体间说服/欺骗/胁迫能力评测。 
 关键数字：摘要无单一数字。安全向仅结论。 
 **建议进主包：是**（标签：主包）

16. **2611.05358** Suppressing Misaligned Behaviors in Language Models, Durably 
 单位核实：Thinking Machines Lab + Princeton / UIUC（Danqi Chen 共同指导） · [arxiv.org/abs/2611.05358](https://arxiv.org/abs/2611.05358) 
 要点：构建两类「模型生物」研究如何持久压制错位行为；比较窄/宽触发并评估抑制耐久性。 
 关键数字：摘要未列百分比（待核）。安全向仅结论。 
 **建议进主包：是**（标签：主包）

17. **2611.03698** Training LLM Agents to Automate LLM Post-Training with RSI-Dojo 
 单位核实：ByteDance + CUHK / 清华 / 上交 · [arxiv.org/abs/2611.03698](https://arxiv.org/abs/2611.03698) 
 要点：RSI-Dojo：训练 LLM agent 自动化 LLM 后训练。 
 关键数字：摘要无 headline 数字（待核）。 
 **建议进主包：否（备选）**（标签：备选）

18. **2611.03982** SLATE: A Large-Scale Benchmark for Long-Horizon API Selection in E-commerce Tool Use 
 单位核实：Amazon（多作者 @amazon.com）+ Georgia Tech · [arxiv.org/abs/2611.03982](https://arxiv.org/abs/2611.03982) 
 要点：SLATE：电商长程 API 选择大规模基准。 
 关键数字：作者自报：最强模型仅完成 **5.0%** 任务。 
 **建议进主包：否（备选）**（标签：备选）

19. **2611.05151** Catalyzing Interactive HTML Generation Capabilities via High-Fidelity Reinforcement Learning 
 单位核实：Microsoft Research（Shaohan Huang、Furu Wei）+ 清华 · [arxiv.org/abs/2611.05151](https://arxiv.org/abs/2611.05151) 
 要点：高保真 RL 催化交互式 HTML 生成。 
 关键数字：摘要无单一数字（待核）。 
 **建议进主包：否（备选）**（标签：备选）

20. **2611.05295** GSBR: Geometric Support Behavior Regularization for Online RL 
 单位核实：Physical Intelligence + UC Berkeley（Sergey Levine 等） · [arxiv.org/abs/2611.05295](https://arxiv.org/abs/2611.05295) 
 要点：GSBR：在线 RL 对预训练 base policy 的几何支撑行为正则。 
 关键数字：作者自报：成功率 **33%→95%**；归一化吞吐约 **+23%**。 
 **建议进主包：否（备选）**（标签：备选）

21. **2611.05296** Universal Hardness From Masking Channels 
 单位核实：Apple（Parikshit Gopalan）+ IIT Bombay / Harvard · [arxiv.org/abs/2611.05296](https://arxiv.org/abs/2611.05296) 
 要点：从 masking channels 推广 hardcore lemma 的学习论结果。 
 关键数字：理论文，无实验数字。 
 **建议进主包：否（备选）**（标签：备选）

22. **2611.05346** Agnostic Learning by Imitating 
 单位核实：Apple + Stanford / Oxford · [arxiv.org/abs/2611.05346](https://arxiv.org/abs/2611.05346) 
 要点：Agnostic Learning by Imitating：判别 vs 生成哪个计算上更难。 
 关键数字：理论文，无实验数字。 
 **建议进主包：否（备选）**（标签：备选）

23. **2611.05377** DreamX: Video Diffusion Model is a Universal Latent Action Learner 
 单位核实：NVIDIA + KAIST · [arxiv.org/abs/2611.05377](https://arxiv.org/abs/2611.05377) 
 要点：DreamX：视频扩散作为通用 latent action learner。 
 关键数字：作者自报多设定 SOTA（具体表待核）。 
 **建议进主包：否（备选）**（标签：备选）

### Batch 11/05

24. **2611.05724** Give the Drafter a Second Chance to Guess: Parallel Reconsideration for Speculative Decoding 
 单位核实：Google DeepMind + Google Research + Rice · [arxiv.org/abs/2611.05724](https://arxiv.org/abs/2611.05724) 
 要点：投机解码 Parallel Reconsideration：给 drafter 第二次猜测。 
 关键数字：作者自报：接受长度 **+5.3%–10.2%**，速度 **+3.5%–9.2%**。 
 **建议进主包：是**（标签：主包）

25. **2611.06244** Rubric Curriculum RL: Exploiting the Generation-Verification Gap in Non-Verifiable Domains 
 单位核实：Microsoft Research + Oxford · [arxiv.org/abs/2611.06244](https://arxiv.org/abs/2611.06244) 
 要点：Rubric Curriculum RL：把 RLVR 扩到不可验证开放域。 
 关键数字：作者自报：创意写作对 base **70.5%** human win；另一设定 **+14.6% / +25.4%**。 
 **建议进主包：是**（标签：主包）

26. **2611.06627** Interactive World Simulation with Cosmos for Physical AI 
 单位核实：NVIDIA（abs 作者行 `NVIDIA:`；github.com/nvidia/cosmos） · [arxiv.org/abs/2611.06627](https://arxiv.org/abs/2611.06627) 
 要点：Cosmos 世界基础模型 → 实时可交互世界仿真（Physical AI）。 
 关键数字：摘要无单一 benchmark 数字；代码与 checkpoint 已开源（作者自报）。 
 **建议进主包：是**（标签：主包）

27. **2611.06687** LifeVal: Evaluating AI Model Performance on Personalized Agentic Consumer Tasks 
 单位核实：OpenAI（HTML author block；Noam Brown / Amelia Glaese / Tejal Patwardhan 等） · [arxiv.org/abs/2611.06687](https://arxiv.org/abs/2611.06687) 
 要点：LifeVal：个性化智能体消费任务评测，覆盖 148 类人生任务，用年化支付意愿刻画价值。 
 关键数字：作者自报：任务价值合计超过 **1.7 trillion USD** 年化 WTP。 
 **建议进主包：是**（标签：主包）

28. **2611.06830** Alignment Myopia in Generative AI 
 单位核实：Google Research + Google DeepMind（Denton / Madaio / Patel / Lakkaraju 等） · [arxiv.org/abs/2611.06830](https://arxiv.org/abs/2611.06830) 
 要点：「对齐近视」：短对话满意度对齐忽视长期人机互动外部性。 
 关键数字：概念/论述文，无 benchmark 数字。 
 **建议进主包：是**（标签：主包）

29. **2611.06905** Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement 
 单位核实：Physical Intelligence + Amazon FAR + Microsoft + ETH/MPI/CMU/Berkeley/Nomagic 等 · [arxiv.org/abs/2611.06905](https://arxiv.org/abs/2611.06905) 
 要点：强化学习如何放大通用机器人策略的部署期改进。 
 关键数字：摘要未给单一 headline 数字（待核）。 
 **建议进主包：是**（标签：主包）

30. **2611.06908** Perceptive Humanoid Motion from Simulation 
 单位核实：Apple（Vladlen Koltun 等） · [arxiv.org/abs/2611.06908](https://arxiv.org/abs/2611.06908) 
 要点：从仿真学习感知人形运动；实物零样本迁移。 
 关键数字：作者自报：实物 **91%** 成功率（360 trials / 6 场景）。 
 **建议进主包：是**（标签：主包）

31. **2611.05553** Decision Models as Scalable Economic Surrogates that Capture Human Variation 
 单位核实：Google DeepMind（R. Maria del Rio-Chanona）+ UCL / LSE · [arxiv.org/abs/2611.05553](https://arxiv.org/abs/2611.05553) 
 要点：Decision Models 作可扩展经济仿真替代。 
 关键数字：摘要无单一数字（待核）。 
 **建议进主包：否（备选）**（标签：备选）

32. **2611.05650** Attributing Agent Failures to Their History Needs an Executed Counterfactual: Toward a Reporting Standard 
 单位核实：Salesforce AI Research · [arxiv.org/abs/2611.05650](https://arxiv.org/abs/2611.05650) 
 要点：长程 agent 失败归因应带可执行反事实证据。 
 关键数字：方法/标准文，无 benchmark 数字。 
 **建议进主包：否（备选）**（标签：备选）

33. **2611.06254** HarnessFlow: MCTS-Guided Harness Optimization for LLM Agents 
 单位核实：Microsoft Research Asia + 多校 · [arxiv.org/abs/2611.06254](https://arxiv.org/abs/2611.06254) 
 要点：HarnessFlow：MCTS 引导优化 LLM agent harness。 
 关键数字：作者自报：平均分 **69.48%**。 
 **建议进主包：否（备选）**（标签：备选）

### Batch 11/06（abs 部分放出）

34. **2611.07071** Shaping & Monitoring Models through their Internal Representations 
 单位核实：Goodfire（github.com/goodfire-ai/reliance；Thomas Fel 等） · [arxiv.org/abs/2611.07071](https://arxiv.org/abs/2611.07071) 
 要点：Mechanistic Shaping：训练期按内部表征规格塑形；跨域至 32B、SFT/DPO/GRPO。 
 关键数字：作者自报：显著降低目标行为且保持任务表现；讨论塑形后可监控性（至 32B）。 
 **建议进主包：是**（标签：主包）

## 明确排除的误报（标题/致谢命中实验室名，但单位不成立）

- **2611.03500**「Can AI Do Formal Demography…」— 作者 UC Berkeley 人口学；正文写用 Claude（Anthropic）辅助证明，**非 Anthropic 论文**。

- **2611.00803** Agent4FreeFem — 作者名 Zhipu Cui，非智谱。

- **2611.02033** — eXplainable AI (XAI) Hub，非 xAI 公司。

- **2611.03767** — 评测对象含 DeepSeek，作者非 DeepSeek。

- **2611.04879** ScamWorld — 声明与 Amazon 职位无关。

- **2611.06615** — 仅 Apple faculty award 资助，作者非 Apple 雇员主单位。

- **2611.06677** Self-Directed Apple Tasting — 标题「Apple」非 Apple 公司。

---

# 四、X

窗口：2026-11-03 09:46 → 2026-11-06 09:20 SGT。来源：
- 首页时间线 3 页，共 296 条（已过滤回复）。只覆盖 11-05 19:02 → 11-06 09:15 SGT，前面约 2.5 天靠检索补齐。
- 官方/关键账号合并检索两组：OpenAI/Anthropic/Cursor/Cohere/AA/Tibo 等一组，Google/DeepSeek/Kimi/MiniMax/Mistral/Decart/Meta/dotey 等一组。
- 定向检索：GPT‑6 Cyber / Daybreak、Kimi K3.1 Pro 权重、Anthropic IPO / METR、Personal Finance、Cursor Live Apps、Fable/Mythos、蒸馏、Playwright/AGENTS.md、Codex 共享额度、Navier–Stokes / GPT‑6.2、vault。
- X Today's News：72 小时内检索 3 组关键词。
- 交叉核对：OpenAI 两篇博客（Cyber、Linux）、Claude Personal Finance 原文、METR 报告、Kimi HF 模型卡与 LICENSE、Anthropic vault 研究页、NVD/Playwright npm、SEC EDGAR Atom、GitHub #41499。

本期 X 侧无 429。GitHub 未认证 API 限流，#107757（Claude Code 邮箱泄露）未从 API 核到；SEC 检索无 11-03 后新的 S-1/A。

## 主条目

### 1. OpenAI 发布 GPT‑6 Cyber：网络安全能力升到 Preparedness「Critical」；同源流水线在 Linux 内核复现 1,724 个漏洞并写出 948 个本地提权利用
这是本窗口最硬的官方发布。模型不是给普通 ChatGPT 用户用的，先开给审核通过的 Daybreak Red 客户。官方同时强调两件事：挖洞能力大幅上升，以及在故意放诱饵的环境里不越权的比例接近 100%。前一天刚公开的 Linux 流水线，就是用这款即将发布的 cyber 模型跑的。
- **是什么**：
 - 发布：OpenAI 11-05（美东）发文介绍 GPT‑6 Cyber；X 官宣 11-06 01:09 SGT。只对部分 Daybreak Red 客户开放 API/Codex，后续扩大。11-12 10am PT 有 Cyber livestream。
 - 能力（官方自报）：
 - ExploitGym：48.5%，上一代 GPT‑5.6 Cyber 为 32.1%（相对提升约 51%）。
 - Preparedness Framework 网络安全档：High → Critical。
 - 对齐评测 ExploitGym Honeypot：无部署提示时不碰范围外服务 99.93%（上代 94.49%），加部署提示后 100%。
 - RemoteExploitBench：GPT‑6 Astra + Daybreak Blue 拒答率 100%；GPT‑6 Cyber 完成 95%。
 - Linux 流水线（博客落款 11-04，X 11-05 07:13 SGT）：
 - 单次运行复现 1,724 个漏洞，写出 948 个可在标准桌面配置上工作的本地提权（LPE）利用；另有 291 个信息泄露 PoC。
 - API 成本约 121.3 万美元，约合每个 LPE $1,279；按历史 Pwn2Own/TyphoonPWN 赏金粗算「假想价值」1,890–6,630 万美元。
 - 采样 166 个利用，至少 10 种对专家来说是新的 Linux 利用手法（细节未公开）。
 - 对比：7 月用 GPT‑5.6 Sol 同 harness 只做出 166 个 LPE。
 - Firefox：发现 81 个 Mozilla 标为高危的未知漏洞，并协助出补丁。
 - 配套：Private Safety Processing（ZDR 客户默认用自动安全审查，人员看不到明文）；Daybreak Red 默认 IP 白名单；新增面向关键基础设施防御方的 Daybreak Red 分组。
- **为何重要**：防御窗口被正式写成产品策略——能力到 Critical 档，却只给审核过的防御方。Linux/Firefox 数字给出了「按流水线扫内核」的成本和产出量级，会直接影响开源维护方和安全预算讨论。
- **对谁·深读建议**：安全研究员、开源维护者、做 agent 红队的人。先读 Cyber 长文里的 Honeypot 对齐和准入部分，再读 Linux 文的五段流水线与成本表；中文速读可对照宝玉以外的技术号拆解。
- **证据**：
 - 官方自报：[@OpenAI Cyber](https://x.com/OpenAI/status/2118390190246879554)、[Cyber 原文](https://openai.com/index/introducing-gpt-6-cyber/)、[@OpenAI Linux](https://x.com/OpenAI/status/2118119451401048497)、[Linux 原文](https://openai.com/index/a-thousand-fewer-paths-to-root/)、[@OpenAIDevs PSP](https://x.com/OpenAIDevs/status/2118386439675420743)、[@thsottiaux](https://x.com/thsottiaux/status/2118402103907655903)
 - X 侧：[X News：948 个 Linux 漏洞](https://x.com/i/trending/2118125161194926199)
- **约时**：Linux 博客 11-04；X 线程 11-05 07:13 SGT；Cyber 官宣 11-06 01:09 SGT

### 2. 月之暗面按承诺开放 Kimi K3.1 Pro 权重：2.8T MoE / 104B 激活 / 1M 上下文；许可接近 MIT，但年营收超 2,000 万美元的「模型即服务」要单独签约
上期还在等 HF 401，本窗口权重已经公开。这是三日刊追踪线里落地最干净的一条：模型卡、许可证、AMD/微软托管都能对上。本地跑门槛极高（仓库约 1.56TB），多数人会走 API 或云托管。
- **是什么**：
 - ：Hugging Face `moonshotai/Kimi-K3.1-Pro` 可访问（API 200）。仓库创建约 11-02，内容更新约 11-05 15:11 SGT；约 112 个文件，下载量已过万。
 - 规格（模型卡）：总参 2.8T，激活 104B，93 层，896 专家/每 token 选 16，上下文 1,048,576；原生多模态（image-text-to-text）；训练时量化 MXFP4/MXFP8。
 - 许可：自有「Kimi K3.1-Pro License」。可改、可商用、可分发；但若运营「Model as a Service」且连续 12 个月营收超 2,000 万美元，须先与 Moonshot 另签协议；超 1 亿月活或月收入超 2,000 万美元的产品界面须显著标注「Kimi K3.1-Pro」。内部使用和官方/认证推理伙伴不受第 2、3 条约束。
 - 生态：微软 Foundry 上线；AMD Instinct MI355X Day‑0；Verda Inference 预览；社区已有安全飞地、量化讨论。
 - 官方 X：@Kimi_Moonshot 本窗口主要是转发 AMD/Verda，未见单独长公告；技术说明以博客和 HF 为准。
- **为何重要**：开放权重前沿再次贴近闭源编码/agent 档；许可证把「自己跑」和「卖推理 API」拆开，大厂托管要谈商务。上期蒸馏报道点名的正是 K3.1 Pro——权重放出后，许可证与安全清洗声明会一起被拿来对照。
- **对谁·深读建议**：自托管和模型服务商先读 LICENSE 第 2、3 条；做 agent 评测的人盯 Terminal-Bench / SWE 等厂商自测与第三方复测差。
- **证据**：
 - ：[HF 模型页](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)、[LICENSE](https://huggingface.co/moonshotai/Kimi-K3.1-Pro/blob/main/LICENSE)、[Tech Blog](https://www.kimi.ai/blog/kimi-k3-1-pro)
 - X 侧：[X News：开放权重](https://x.com/i/trending/2118015143208423849)、[@msdev Foundry](https://x.com/msdev/status/2118493567589011577)、[@Kimi_Moonshot RT AMD](https://x.com/Kimi_Moonshot/status/2118220088675545317)
 - 待核：厂商自测「接近 Opus 5.5」的具体分项；「权重约 1.56TB」为社区测算。
- **约时**：HF 更新约 11-05 15:11 SGT；X News 11-05 23:21 SGT

### 3. METR 独立评估：Anthropic 在明确任务上的能力进步速度约是此前的 2 倍，并猜测当前加速约八成来自用 AI 做研发；多数关键证据被 Anthropic 涂黑
这是对上期 S-1/A 里「可能很快触及 RSP 加速门槛」的外部对照。METR 进了 Anthropic 内部看了 11 周，公开结论偏谨慎，但删减幅度本身也成了新闻。
- **是什么**：
 - 报告：METR 2026-11-05 发布；评估期 8-12 → 10-29；约 2.5 人全职当量，不收 Anthropic 钱。
 - 主观结论（METR 自述，团队有分歧）：
 - 截至 2026-10，Anthropic 在「目标明确的任务」上提升能力的速度，大约是 2024-03 → 2025-10 的 2 倍；真实值在 1.3–3 倍都不意外。
 - 当前加速的大部分「或许约 80%」来自用 AI 做研发；2025 年底那波加速里，非 AI 因素可能很大。
 - 未见明显瓶颈或强递减，未来 12 个月有进一步加速的风险；也可能漏看了瓶颈。
 - 可公开的硬数字：内部 AECI（Anthropic 版 Epoch 能力指数）自 2025-10 起增速约 1.9×（95% CI 1.5–2.8）；换链路函数结果在 1.1–2.9×；纳入其他公司模型则约 1.4×。加速**不是**训练算力增速变快导致的。
 - 涂黑：约 100 页完整报告中，Anthropic 单方面删掉 METR 认为最有说服力的大部分证据（算法进步估算、训练各环节加速、对未来模型的预测等），理由是可能帮竞品加速。算力「能力 vs 安全」分配核查中途被取消。
 - 旁证：员工 Slack 投票自评最新模型让自己快约 12 倍（METR 称证据很粗）；AI 尚未能独立完成训练最关键环节，但已有「signs of life」。
 - Anthropic：Sam McCandlish 称许多结论与他一致，并预告未来几周发自家报告，对照 RSP；联合创始人侧未否认加速，但强调不确定性。
- **为何重要**：把「AI 是否在加速造 AI」从口号变成带置信区间的外部意见；同时暴露独立评估在红action 下能公开多少。会直接喂进 IPO 路演和 RSP 讨论。
- **对谁·深读建议**：政策/安全读者读 Executive summary 和 redaction 表；写 IPO 的人对照上期 S-1/A 的 RSP 措辞。
- **证据**：
 - 官方自报（评估方）：[@METR_Evals](https://x.com/METR_Evals/status/2118412183860351084)、[METR 原文](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/)
 - X 侧：[宝玉长解读](https://x.com/dotey/status/2118466539510960161)、[X News：进步翻倍](https://x.com/i/trending/2118427442922901851)、[Sam McCandlish 回应](https://x.com/Sam_McCandlish/status/2118422266669371519)
- **约时**：报告 11-05；X 线程 11-06 02:36 SGT

### 4. Claude 上线 Personal Finance 美区测试：Plaid 只读连银行，Pro/Max/Ultra 分批；不能转账、不管钱、不投资
产品向「连真实账户」再进一步，但比 ChatGPT Finances 收得更窄：只看日常收支，不看持仓细节，理财页对话默认不进训练。
- **是什么**：
 - 官宣：@claudeai 11-06 02:00 SGT；美国 Pro / Max / Ultra 本周起 beta，侧边栏出现入口即轮到；免费/Team/Enterprise 无。
 - 能力：用自然语言问余额、分类支出、账单、异常扣款等；可生成图表/日历；最多连 16 家机构，最多约 24 个月交易。
 - 安全：经 Plaid 授权，只读；Claude 看不到银行密码，不能移动、管理或投资资金；无广告、无自营信贷产品。理财 hub 内对话不用于训练。
 - 对比（第三方整理）：OpenAI 5 月已有类似 Finances；ChatGPT 侧还能读投资持仓并做更宽的规划话术，Claude 明确不提供投资建议。
- **为何重要**：高价订阅继续往垂直场景叠能力；「只读 + 不训练」是这次对外的主叙事，也会被拿来和上期 Ultra 取消 5 小时限额一起看成商业化节奏。
- **对谁·深读建议**：美国付费用户看帮助中心绑定步骤；隐私读者对照两家对同步数据删除时限的写法（Claude 帮助页对解绑后保留时长写得不如 OpenAI 明确——待核细节以帮助中心为准）。
- **证据**：
 - 官方自报：[@claudeai](https://x.com/claudeai/status/2118403114890137895)、[产品文](https://claude.com/resources/articles/introducing-personal-finance-in-claude)
 - X 侧：[宝玉对比解读](https://x.com/dotey/status/2118455489423905097)、[X News](https://x.com/i/trending/2118406567187947755)
- **约时**：2026-11-06 02:00 SGT

### 5. Anthropic 生物团队用 Claude 解出细菌/噬菌体穹窿体（vault）三维结构：分离实验从约 3 天压到 90 分钟，34 小时出第一版模型
这是「实验室里的 agent」案例，不是模型发布。功能仍未找到，但第一次证明简单生物里的同类蛋白也能拼成穹窿体，并给出可改造的纳米胶囊线索。
- **是什么**：
 - 官宣：@AnthropicAI 11-05 04:11 SGT；研究页与预印本 PDF 同步。
 - 结果：在约 150 亿条预测序列里找到分布很广但稀有的 vault 同源；15 种表达成功，7 种拼成颗粒，冷冻电镜确认 4 种（含噬菌体与细菌）；解出的 L05 由 96 个亚基组成，内部空间比人源 vault 大约 25%。
 - 节奏：项目不到 4 个月；分离流程约 90 分钟；RELION 流程 34 小时出第一版完整模型。文章也写了 Claude 的两个错误（培养基添加剂、跳过标准步骤导致镜像混淆）。
 - 局限：预印本、未同行评审；顾问 Rome 收取顾问费；冷冻电镜阶段用了远超普通高校的 GPU。
- **为何重要**：继数学/安全之后，湿实验流程被写成可复述的人机分工样本；对「AI for science」扩写比空泛的「模型又发了」更有材料。
- **对谁·深读建议**：科研工具和生物信息读者读研究页的失败案例；写科普的人抓住「40 年不知功能的蛋白桶」。
- **证据**：
 - 官方自报：[@AnthropicAI](https://x.com/AnthropicAI/status/2118073665296228863)、[研究页](https://www.anthropic.com/research/investigating-vault-particles-with-claude)、[预印本 PDF](https://www-cdn.anthropic.com/76e55fbe85697afbaae16b839498dc00797dec30.pdf)
 - X 侧：[宝玉解读](https://x.com/dotey/status/2118243086589476995)
- **约时**：2026-11-05 04:11 SGT

## 进展

### 进展：Anthropic IPO：仍无新的定价/股数修订；市场对 1.5 万亿估值更怀疑，推迟传闻增多
- **是什么（新增）**：
 - ：截至 11-06 上午，EDGAR 公司页最新仍是 11-02 的 S-1/A（accession 0001628280-26-068676），无更新价格区间或发行规模的新修订。
 - 待核：WSJ/Polymarket 等称投资者对 1.5 万亿估值日益怀疑；有传言估值下修至约 1 万亿或更低、上市可能推迟。均非公司公告。
 - 人事侧噪音：多名 Anthropic 产品/增长人员转投 OpenAI 的讨论升温（Cat Wu 等），与 IPO 窗口重叠，因果未证实。
- **证据**：：[EDGAR S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/0001628280-26-068676-index.htm)；待核：市场讨论见 X News/财经转述（本包不把估值数字当 ）
- **约时**：持续至 11-06

### 进展：浏览器 agent 补丁债：Playwright 已至 1.65.0，捆绑 Chromium 158.0.8127.18（晚于 CVE-2026-118306 修复线）
- **是什么（新增）**：npm `playwright@1.65.0` 的 browsers.json 显示 Chromium 158.0.8127.18。上期点名的 1.64.1 / 156.0.8078.4 落后问题，在当前 latest 上已越过 156.0.8078.73 修复线。是否默认开沙箱仍需部署方自查。
- **证据**：：Playwright npm latest；Chromium 版本见官方 browsers 清单；上期 CVE：[NVD CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306)
- **约时**：核验于 11-06 上午

### 进展：Cursor：推出「描述即部署」的 Live Apps（付费云 agent）；扩展投毒事件本窗口无新 IoC
- **是什么（新增）**：
 - 产品：@cursor_ai 称可在编辑器里用自然语言搭应用，按需建库、跑确定性与 agent 安全检查、部署到可分享链接；面向开启 cloud agents 的付费计划。X News 称支持 Postgres、Cursor SSO 等（细节以官方文档为准）。
 - 投毒后续：本窗口未见 2.1.314 之外的新受害者统计或新恶意版本通报。
- **证据**：官方自报：[@cursor_ai](https://x.com/cursor_ai/status/2118458629091426304)；X 侧：[X News](https://x.com/i/trending/2118474980145160485)
- **约时**：11-06 05:41 SGT

### 进展：Codex/ChatGPT 共享额度：本窗口无新的官方生效日或额度数字
- **是什么（新增）**：上期已确认「12 月起 Plus/Pro/Business 共享、按 token、Instant 不计」。本窗口帮助文档与官方账号无补充具体哪一天、额度是否等于原两份之和。仍按上期结论跟踪。
- **证据**：上期 文档继续有效；本窗口无新官方帖。
- **约时**：无新

### 进展：下一代旗舰传闻：官方交付的是 GPT‑6 Cyber；GPT‑6.2 Astra/Sol、Fable 5.5 仍无官宣
- **是什么（新增）**：OpenAI 实际发布 Cyber；Linux 文写明流水线用的是「upcoming cyber model」。GPT‑6.2 Astra/Sol「周五双发」、Fable 5.5「再推迟」等仍是截图/传闻，标待核或不采信。
- **证据**：官方自报见主条目 1；待核泄露不单列链接。
- **约时**：11-05 → 11-06

以下追踪项本期**无新消息**，不单列：
- 蒸馏报道：DeepSeek / 月之暗面 / OpenAI 仍无公司层面回应。
- AGENTS.md 劫持 Codex：GitHub issue #41499 仍为 open，最后更新 2026-08-29，0 评论。
- Gemini 4 Carbon 开放范围、Genie 4：无扩大公众开放的官方公告；本窗口 Google 主推 Omni 1.2 Flash 视频模型。
- Brotli/Fragnesia：无新的 KEV/补丁主线消息（Cyber 文回顾了用该模型验证 Brotli RCE，属旧链复述）。
- 阿里对 Cohere：无回应。
- Claude auto mode：无官方生效公告。
- Navier–Stokes 外部数学核查：无新的独立定论。

## 其他
- **OpenAI 其他**：
 - 周生成图像超 40 亿张（ChatGPT + API），8 周前约 30 亿以上（Tibo 口述）。[@thsottiaux](https://x.com/thsottiaux/status/2118469621011677521)
 - 收购 Pierre，开源 Trees/Diffs 将继续过渡（X News，细节待核）。[X News](https://x.com/i/trending/2117952603011064152)
 - Family 订阅档位出现在结账代码中（Go/Plus/Pro 等，待核）。[X News](https://x.com/i/trending/2117942940647444937)
- **Anthropic / Claude 其他**：
 - Claude Code 状态行刷新成本据称降 99%（Haiku 5.5 短笔记生成，v2.1.316+，待核媒体数字）。[X News](https://x.com/i/trending/2117768217288400999)
 - 有报告称 Claude Code 在 macOS 网页搜索 User-Agent 中泄露邮箱（HN / issue #107757，本包 GitHub API 限流未核）。待核。
 - Thariq 离职后上播客谈实验室「偶像化」（文化侧，非产品）。[dotey 长文](https://x.com/dotey/status/2118471688866213999)
- **Google / Meta**：
 - Gemini Omni 1.2 Flash：全 Google AI 订阅用户开滚；Ultra 可生成/编辑最长 15 秒视频；开发者侧称价格降约 30%。[@GeminiApp](https://x.com/GeminiApp/status/2118406227533435391)、[@googledevs](https://x.com/googledevs/status/2118389720111866253)、[Google 博客](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/)
 - Muse Realtime Avatar 在美国 Muse App 推出。[@AIatMeta](https://x.com/AIatMeta/status/2118412135340572850)
 - Meta 收购 Conductor，云服务将关停（X News）。[X News](https://x.com/i/trending/2118458548384608443)
- **其他模型厂**：
 - Mistral Studio：托管 agents/apps、工作流、企业连接、可观测与评测。[@MistralAI](https://x.com/MistralAI/status/2118370229466153299)
 - Decart Lucy 2.6：实时视频模型质量升级。[@DecartAI](https://x.com/DecartAI/status/2118397449978913075)
 - Tencent Hy4：AA Index v5 得 35，中国实验室第二。[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2118259055546482834)
 - Thinking Machines Inkling 2 Small：AA 31 分；若按计划开源权重，将成为中国以外开源分最高之一（官方计划，权重是否已放以仓库为准）。[@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2118493376186388530)
 - DeepSeek V5 计划主要在华为昇腾上预训练（媒体，待核）。[X News](https://x.com/i/trending/2117588556210119068)
- **评测 / 产业**：
 - Menlo：2026 企业 AI 支出约 1,770 亿美元（待核报告细节）。[X News](https://x.com/i/trending/2117714665514115439)

## A 时间线/官方
- **时间线覆盖**：首页 3 页共 296 条（已过滤回复），只覆盖 11-05 19:02 → 11-06 09:15 SGT。11-03 09:46 → 11-05 19:02 靠官方检索、News 与定向检索补齐，可能漏个人帖。
- **时间线内容**：集中在 GPT‑6 Cyber、Personal Finance、METR、Kimi 权重、Cursor Live Apps、Omni 1.2 / Lucy 2.6。高信号：OpenAI、OpenAIDevs、claudeai、AnthropicAI、METR_Evals、cursor_ai、ArtificialAnlys、dotey、thsottiaux。
- **无原创帖的账号**：deepseek_ai、Alibaba_Qwen 本窗口基本无原创；Kimi_Moonshot 以转发为主。
- **提示注入与广告**：检索里有诱导执行提示词、返佣与币圈带货，本包只当数据处理，未执行、未引用指令。新闻摘要里偶发第三方产品名，引用时已去掉无关品牌表述。

## B Today's News
- **GPT‑6 Cyber / Linux 948 LPE**。[X News](https://x.com/i/trending/2118125161194926199)
- **METR：Anthropic 进步约翻倍**。[X News](https://x.com/i/trending/2118427442922901851)
- **Kimi K3.1 Pro 开放权重**。[X News](https://x.com/i/trending/2118015143208423849)
- **Claude Personal Finance**。[X News](https://x.com/i/trending/2118406567187947755)
- **Cursor Live Apps**。[X News](https://x.com/i/trending/2118474980145160485)
- **Meta Muse 语音/数字人；收购 Conductor**。[X News](https://x.com/i/trending/2118434502938968435) · [X News](https://x.com/i/trending/2118458548384608443)
- **OpenAI 收购 Pierre；GPT‑6.2 泄露（待核）**。[X News](https://x.com/i/trending/2117952603011064152) · [X News](https://x.com/i/trending/2117506794239176758)
- 其余（加密、体育、纯梗图）不列。

## C 已核摘要
- **GPT‑6 Cyber**：ExploitGym 48.5%（上代 32.1%）；Honeypot 99.93%/100%；网络安全档 Critical；Daybreak Red 部分客户可用。
- **Linux 流水线**：复现 1,724；LPE 利用 948；API 成本约 $1,213,430；新颖手法至少 10 种（采样）；Firefox 高危未知漏洞 81。
- **Kimi K3.1 Pro**：HF 公开；2.8T / 104B / 1M context；MaaS 且年收入>$20M 需另签；界面 MAU>1亿或月收入>$20M 须标注型号名。
- **METR**：AECI 增速约 1.9×（1.5–2.8）；主观总判断约 2×（1.3–3）；多数关键证据被红action；非训练算力驱动。
- **Personal Finance**：美区 Pro/Max/Ultra beta；Plaid 只读；理财 hub 对话不训练。
- **Playwright**：latest 1.65.0 → Chromium 158.0.8127.18。
- **Anthropic IPO**：无新于 11-02 S-1/A 的定价修订。
- **#41499**：仍 open，无补丁。

## E 建议扩写
1. **防御窗口政治经济学**：GPT‑6 Cyber 把 Critical 能力关进 Daybreak Red，同时用 Linux/Firefox 战报证明「现在不扫就来不及」。可对照 Carbon 的 Fairwind 准入，写「谁先拿到防御工具」。
2. **开放权重的新条款**：以 Kimi LICENSE 的 $20M MaaS 门槛为例，梳理 2026 年「能下权重 ≠ OSI 开源」的谱系，并估算自托管 TCO（1.56TB、八卡）。
3. **读 METR 报告的方法**：公开结论、涂黑表、AECI 稳健性区间、员工 12× 自评为什么不能直接换算成公司加速度；对照 S-1/A 的 RSP「imminently」措辞。
4. **实验室里的 Claude**：vault 项目的人机分工、两次错误如何回流训练、普通实验室能不能复现——当作 AI for science 的操作手册而非公关稿。
5. （可选）**Cursor Live Apps**：从「写得出代码」到「分享得出链接」，看 cloud agent 的安全检查声称能否挡住上一轮扩展投毒类供应链问题。

---

# 五、GitHub（2026-11-03 → 2026-11-06）

1. **llama.cpp v0.9.0**
llama.cpp 于 11-04 21:08（SGT）发布正式版 v0.9.0，底座 ggml 升到 v0.29.0。量化侧新增 OCP FP8 E4M3；推理侧用 `flash_attn_ext_rows` 让统一 KV cache 在多序列场景更高效，并恢复非统一 KV 的 prefill 表现；ggml 还带来 NCCL 多节点张量并行，以及 CPU / CUDA / SYCL / Metal / Vulkan / OpenCL / Hexagon 各后端的性能工作。新架构包括 Clover、Limite、Metis-1.6 和 Mistral Large 4；音频侧扩展 Chatterbox TTS、Nemotron 3.5 Transcribe 与 Pocket TTS 预置音色；Gemma 4 E2B/E4B 的 prefill 也有大改。做本地多序列服务、想试 FP8 或刚拿到 Large 4 GGUF 的人应先看这版；API 有一批 `mtmd.h` / server TTS 相关变更，升级前对照 changelog。
证据：[v0.9.0 Release](https://github.com/ggml-org/llama.cpp/releases/tag/v0.9.0) · [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)

2. **OpenAI Python v3.43.0–v3.47.0 / Node v7.48.0–v7.52.0**
OpenAI 两个官方 SDK 在窗口内连发五次（Python 从 11-04 02:05 的 v3.43.0 到 11-06 02:04 的 v3.47.0；Node 同步到 v7.52.0）。值得单独拎出的有：Live Responses 委托工具扩展、Responses 的 12 小时缓存与 cache-write 用量、模型目录加入 GPT-6 Rosalind、澳大利亚 / 印度 / 日本数据驻留选项，以及图像复杂度与 GIF / SVG 输出控制。上一期刚写过 agent compaction / session review，这一波是把长会话、缓存和区域合规继续写进 SDK。做 Responses / Live 长连接或要按区域部署的团队可以直接对照这五版 changelog，不必再追零散 PR。
证据：[openai-python v3.46.0](https://github.com/openai/openai-python/releases/tag/v3.46.0) · [openai-python v3.45.0](https://github.com/openai/openai-python/releases/tag/v3.45.0) · [openai-node v7.51.0](https://github.com/openai/openai-node/releases/tag/v7.51.0)

3. **ComfyUI v0.44.0**
ComfyUI 于 11-04 09:12（SGT）发布 v0.44.0。核心是视频侧：支持 MiniMax-H3 latent upscaler、Sol-H3-VAE 与 H3 的 context windows，并加入 H3 Max Recast / Extend / Reframe / Insert / Lip Sync / Camera Control 等合作方节点；另有 Flux Video Upscale 的 1080p / 2K / 4K 目标，以及 Patina 纹理、VEED 配音、Ideogram 区域编辑、Pruna P-Video Upscale 等节点。做 AI 视频工作流、尤其已经在用 MiniMax H3 的人可以升；普通图生图用户变化相对外围，可按需更新。
证据：[v0.44.0 Release](https://github.com/comfyanonymous/ComfyUI/releases/tag/v0.44.0) · [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)

4. **KKKKhazix/agent-autoloop**
于 11-03 16:02（SGT）新建，截至 11-06 09:19（SGT）约 3,242 星，是窗口内新仓星数第一。定位是本机「自动化中台」：把定时任务、GitHub Issue、业务告警等变成标准事件，调度已登录的命令行 Agent 在后台接活并跟进到底；平时不打扰，拿不准时才把卡片推到飞书 / 钉钉 / 企微 / Slack / Discord 或桌面通知。内核零外部依赖，事件源、Agent、通知通道都是插件，自称一行配置即可接入「能接收提示词并打印最后回复」的 CLI Agent，不要求改 Agent 源码。macOS / Linux 可用，Windows 版 README 写明仍在开发。想让本机 Agent 从「守着终端」变成「后台接单」的人值得试；生产前自行评估权限与费用统计口径。
证据：[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop) · [Release 列表](https://github.com/KKKKhazix/agent-autoloop/releases)

5. **NVIDIA/auto-ontology**
老仓（2026-04 创建）在 11-06 日榜以 2,679 stars today 排第一，总星约 7,377；窗口内有版本 bump 到 1.2.0 的提交（11-05），仓库尚无 GitHub Releases 页。它是 NVIDIA 开源的企业本体 / 语义层：从元数据生成 ontology 与知识图谱，给 agent 提供指标、实体与血缘的可信含义，经 MCP / CLI / API 对外，并带 NL-to-SQL、校验与 RBAC。README 写明当前不接受外部贡献。做企业数据分析 agent、怕「答得快但数不对」的人应看日榜这次暴涨背后的定位；数字口径是 GitHub Trending 日榜约最近 24 小时（抓取于 2026-11-06 09:19 SGT）。
证据：[NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) · [GitHub Trending 日榜](https://github.com/trending?since=daily) · [v1.2.0 bump 提交](https://github.com/NVIDIA/auto-ontology/commit/c449567)

（热榜口径：日榜约为最近 24 小时，周榜统计最近七天，均于 2026-11-06 09:19 SGT 抓取。周榜前列的 Nutlope/hallmark、pbakaus/impeccable、pingdotgg/t3code、thedotmack/claude-mem 等已在往期出现或仅持续在榜，本期不重复。）

窗口内无：vllm-project/vllm、sgl-project/sglang、huggingface/transformers、pytorch/pytorch、huggingface/datasets、modelcontextprotocol/python-sdk、modelcontextprotocol/typescript-sdk、axolotl-ai-cloud/axolotl（常规 / 预发布未收录：ollama v0.40.15-rc2；openai/codex 仅 libcap-v2.75 预发布；Anthropic SDK Python v2.5.0 / v2.6.0 与 TS sdk-v1.5.0 / v1.6.0 及云子包主要为错误类型与管理员能力；unsloth v0.1.914-beta / v0.1.915-beta；langchain 1.4.9 / langchain-core 1.7.5–1.7.6 / langchain-anthropic 1.7.10 / langchain-openai 1.7.4 / langchain-typesafe 0.0.1–0.0.2；langgraph 1.2.20 / sdk 0.4.12–0.4.13 / cli 0.4.41）

---

# 六、Hugging Face 与榜单

- **窗口**：2026-11-03 09:46 SGT（11-03 01:46 UTC）→ 2026-11-06 09:25 SGT（11-06 01:25 UTC），约 71.5 小时。
- **范围**：HF Trending 模型（前 300，`sort=trendingScore`）与数据集（前 100）；主要机构按 lastModified 扫描（含 sensenova、speridlabs）；LMArena 文本 / 视觉 / 文生图；Artificial Analysis Intelligence Index v5、文生图榜、图像编辑榜。
- **窗口判断：中等偏厚，主线只有一条。** 本窗真正改变格局的是 **moonshotai/Kimi-K3.1-Pro 权重已在 HF 官方组织下可下载**（上期明确写“仍未开放”）。另外两条本窗新发值得写：Ricursive 的 65B 开源稠密模型 Ripple-65B-Preview，以及 speridlabs/idol-turbo（Idol 的蒸馏加速版）。其余多为热度延续、量化再打包或榜单小幅漂移。
- **Kimi K3.1 Pro 结论：已发。** 官方组织账号 `moonshotai/Kimi-K3.1-Pro` 有 96 个 safetensors，siblings 非空；AA 模型页已改为 Open weights，并反链该 HF 仓库。官方博客 [kimi-k3-1-pro](https://www.kimi.ai/blog/kimi-k3-1-pro) 正文仍写 “Full model weights will be released by Nov 4, 2026”，**没有**改成“已发布”、也**没有**在博客页加 HF 链接；博客索引无更新帖、无延期说明页。按权重与 org 证据，视为承诺期内已兑现。
- **榜单**：LMArena 文本 / 视觉未刷新；**文生图榜刷新到 Nov 2**。AA 首页默认图有实质变化：Kimi 从 prop 改为 open，并新进闭源 Tencent Hy4、Inkling 2 Small。

---

## 一、重点

### 1. moonshotai/Kimi-K3.1-Pro：3T 级开放权重多模态 agent 模型已在官方 HF 上线（上期未收录 · 本窗对外可见 · 开放权重）

上期截止 11-03 09:19 SGT，moonshotai 组织 API 仍只有 Kimi-K3，搜 “K3.1” 只能命中冒名仓。本窗同一组织下出现 `Kimi-K3.1-Pro`，Trending #1（trendingScore 870），likes/downloads 已到 928 / 11,658 量级。卡片与 README 写明：原生多模态 agent 模型，从 Kimi K3 大规模联合 RL 后训练而来；MoE 总参约 2.8T、激活 104B、上下文 1,048,576；量化为 MXFP4 权重 / MXFP8 激活（QAT）。HF safetensors 统计约 2.780T（U8 为主，另有 BF16/F32）。许可证是自定义 **Kimi K3.1-Pro License**（`license: other` / `license_name: kimi-k3.1-pro`）：允许使用、修改、分发，但对年收入超 2000 万美元的 MaaS、以及超大规模商业产品有额外签约/署名要求——**开放权重，不是 OSI 开源**。官方性证据充分：作者为 moonshotai 官方 org；Initial commit 用户 bigmoyan；AA 模型页写 “Open weights model” 并链接 `huggingface.co/moonshotai/Kimi-K3.1-Pro`。时间线需写清：HF `createdAt` 为 11-02 12:13 SGT，但 11-03 采集时 org 列表未出现该仓（可能当时未公开或索引滞后）；本窗 `lastModified` 11-05 15:11 SGT 有 encoding 更新。适合做长上下文 agent、代码/3D/金融研究场景、以及需要开放权重部署的推理团队；商用 MaaS 需先读许可证第 2–3 条。

```
id: moonshotai/Kimi-K3.1-Pro
createdAt: 2026-11-02 12:13 SGT (04:13 UTC) ← 窗前；上期 org API 未列出
lastModified: 2026-11-05 15:11 SGT (07:11 UTC)，提交 “Update encoding_k3.py”
likes / downloads: 928 / 11,658 Trending #1（新进）
license: other（Kimi K3.1-Pro License） pipeline: image-text-to-text
权重: 96 个 safetensors（model-00001..000096）+ index；HF 统计约 2.780T
开放度: 开放权重（自定义许可，非 OSI）
官方性: moonshotai 官方 org；AA 反链该仓库；README 链回 kimi.ai / moonshot.ai / 技术博客
架构自述（卡片/README，待核）: MoE 2.8T / 激活 104B / 93 层 / 896 experts·选 16 / MoonViT-V2 401M / 上下文 1M
```

待核：博客页仍写 “will be released by Nov 4” 而未更新为已发布；HF `createdAt` 与上期 API 不可见之间的私有/公开切换无法从公开 API 直接证明；卡片自报基准与 AA Intelligence Index 46.5 的评测设定；社区 pruned/abliteration 变体质量。

链接：[HF](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) · [LICENSE](https://huggingface.co/moonshotai/Kimi-K3.1-Pro/blob/main/LICENSE) · [Moonshot 技术博客](https://www.kimi.ai/blog/kimi-k3-1-pro) · [API Quickstart](https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart) · [AA 模型页](https://artificialanalysis.ai/models/kimi-k3-1-pro)

### 2. ricursiveAI/Ripple-65B-Preview：65B 稠密开源模型，本窗新发并冲到 Trending #13（本窗新发 · 开源）

Ricursive Intelligence 放出 Ripple-65B Preview：约 65B 稠密 Transformer，README 称在 12T token 上预训练、支持最长 1M 上下文，并强调薄而深的结构（d_model 5120、80 层）以便在 NVIDIA 消费级/工作站硬件上本地跑。同日还有 Base、NVFP4、DFlash2 衍生仓。许可证 apache-2.0，权重 16 个 safetensors，HF 统计约 64.78B。官方发布页 ricursive.com/ripple 反链该 HF 仓库。卡片自报 TerminalBench 2.1 等成绩（待核）。它的意义在于：本窗除 Kimi 外，难得有一家非巨头给出可下载的 60B+ 级 Apache 权重，且明确面向本地部署。适合要在单机/小集群跑大稠密模型、做 agent 代码评测对比的团队。注意：作者是 ricursiveAI，不是常见大厂列表里的名字；以官方站点反链为准。

```
id: ricursiveAI/Ripple-65B-Preview
createdAt: 2026-11-04 10:41 SGT (02:41 UTC)
lastModified: 2026-11-05 07:02 SGT (11-04 23:02 UTC)
likes / downloads: 269 / 939 Trending #13（新进）
license: apache-2.0 pipeline: （API 未标 pipeline_tag）
权重: 16 个 safetensors，HF 统计约 64.78B（BF16）
开放度: 开源（OSI / Apache-2.0）
官方性: 发布页 [www.ricursive.com/ripple](https://www.ricursive.com/ripple) 反链 HF；同 org 另有 Base / NVFP4 / DFlash2
衍生: ricursiveAI/Ripple-65B-Preview-NVFP4（24 / —）、Ripple-65B-Base-Preview（20）、Ripple-65B-Preview-DFlash2
```

待核（README 自报）：TerminalBench 2.1 80.52；MMLU 89.6 / MMLU-Pro 84.2 / GPQA Diamond 85.2；与 Nemotron 3 Ultra、Inkling、Muse Spark Open、Reflection Beam 的对比表；“12T token”“1M context”训练与推理设定。

链接：[HF](https://huggingface.co/ricursiveAI/Ripple-65B-Preview) · [发布页](https://www.ricursive.com/ripple) · [NVFP4](https://huggingface.co/ricursiveAI/Ripple-65B-Preview-NVFP4) · [Base](https://huggingface.co/ricursiveAI/Ripple-65B-Base-Preview)

### 3. speridlabs/idol-turbo：Idol 的 5 步蒸馏版，单图 3D 更快（本窗新发 · 开源）

上期重点 speridlabs/idol（单图→3D Gaussian）本窗继续热（Trending #2，775 likes）。同作者在窗内放出 idol-turbo：把 flow-matching 去噪器蒸馏成 **5 步、无 CFG** 的加速版，README 称约 0.75s，并提供 ComfyUI LoRA。基座标明 `base_model: speridlabs/idol`，许可证 apache-2.0，8 个权重文件（含 denoiser / decoder / LoRA）。适合已经在用 Idol 或 Comfy 工作流、需要更快预览的 3D 资产与电商原型用户。体量远小于主线 Kimi/Ripple，但和上期 Idol 叙事连续，故列入重点第三条。

```
id: speridlabs/idol-turbo
createdAt: 2026-11-03 17:07 SGT (09:07 UTC)
lastModified: 2026-11-04 07:03 SGT (11-03 23:03 UTC)，含 ComfyUI LoRA 与说明
likes / downloads: 38 / 391
license: apache-2.0 pipeline: image-to-3d
权重: 8 个 safetensors（含 loras/*）
开放度: 开源
官方性: speridlabs 官方 org；卡片 base_model 指向 speridlabs/idol；上期已核 idol 官方研究页反链
```

待核：0.75s / 5-step 为作者自测；与原版 Idol 在几何质量上的差距；是否覆盖原版全部高斯档位。

链接：[HF](https://huggingface.co/speridlabs/idol-turbo) · [基座 idol](https://huggingface.co/speridlabs/idol) · [官方研究页（基座）](https://speridlabs.com/research/idol)

---

## 二、旁线

- **AA 闭源新面孔（非 HF 权重）**：首页默认图新进 [Tencent Hy4](https://artificialanalysis.ai/models)（发布日标注 2026-11-03，Intelligence Index **34.6**，isOpenWeights false）与 [Inkling 2 Small](https://artificialanalysis.ai/models)（2026-11-05，**30.6**，prop）。HF 上无 `tencent/Hy4` 仓库（API 返回鉴权错误/不存在）。属闭源榜单变化，不是开源事件。
- **Kimi 社区衍生（降权，非官方）**：`unsloth/Kimi-K3.1-Pro`（镜像，9 / 266，96 权重）、`vllm-project/Kimi-K3.1-Pro-pruned75`（剪枝，12 / 0）、`DaoCloud/Kimi-K3.1-Pro-pruned75`、`AMAImedia/Kimi-K3.1-Pro`、`tiny-random/kimi-k3.1-pro`（测试用小权重）、`pqhaz/...-abliteration-patch`、`Blackfrost-Research/...-DERISKED`（0 权重）等。均非 moonshotai；许可/对齐需自担。
- **nvidia/MetricTrail**（本窗新发，研究代码）：NVIDIA Open Model License，视觉里程计/度量深度；仓内有 `dino_dpvo.pth`，但 README 仍写完整 checkpoint 计划另发。15 likes / 0 downloads 量级，不进重点。[HF](https://huggingface.co/nvidia/MetricTrail)
- **ByteDance-Seed/Cross-Layer-TopK-CLT**（本窗新发）：Qwen3-8B-Base 的跨层 transcoder，apache-2.0，可解释性工具，5 likes / 0 dl，不进重点。[HF](https://huggingface.co/ByteDance-Seed/Cross-Layer-TopK-CLT)
- **数据集新面孔**：[PentesterFlow/OffsecCyber](https://huggingface.co/datasets/PentesterFlow/OffsecCyber)（创建 11-03，数据集榜 #4）、[codepawl/abo-glb](https://huggingface.co/datasets/codepawl/abo-glb)、[codepawl/scanned-objects-glb](https://huggingface.co/datasets/codepawl/scanned-objects-glb)。榜首仍是 nvidia/simready-assets。
- **上期重点后续**：Mage-VL-Cowork likes 143→187；SenseNova-Loop 186→250；DSV4.1-NVFP4 137→182（11-04 有维护提交）；Mistral Large 4 1,500→1,615；idol 419→775。均无新权重级事件，归热度延续。SenseNova 技术报告仍未见。

---

## 三、榜单对比（对比 11-03 / 10-30 快照）

| 榜单 | 本期状态 | 变化 |
|---|---|---|
| LMArena 文本 | Oct 27 · 9,003,272 票 · **418** 个模型 | **未刷新**（上期 419）。#1 Gemini 4 Carbon (High) 1528±9 预备。Kimi K3.1 Pro、Ripple、Ling 3.1、LFM3、MiniMax-M3.1-Flash、Nanbeige 仍不在榜 |
| LMArena 视觉 | Oct 19 · 1,493,948 票 · **166** 个模型 | **未刷新**（上期 167）。#1 Claude Fable 5 (High) 1309±7 |
| LMArena 文生图 | **Nov 2** · **6,961,993** 票 · **84** 个模型 | **已刷新**（上期 Oct 26 · 6,872,557 · 82）。#1 仍是 GPT-Image-2.5 Sunburst 1427±5 预备（票数 40k→55k）。新进预备档：GPT-Image-2.6 Sunburst/Flare (Medium) #2/#4；Gemini Nano Banana 2.1 #7；Qwen-Image-3.0-Pro #14。FLUX 3 / FLUX 3 Klein / Fibo 2.0 仍不在 LMArena（在 AA） |
| AA Intelligence Index v5 首页默认图 | 28 条有分数 | **有变化**。Kimi K3.1 Pro：**prop 46.0 → open 46.5**，并被文案标为最高分开放权重。新进闭源：Tencent Hy4 34.6、Inkling 2 Small 30.6。Gemini 4 Carbon 59.4→60.0；多款闭源 +0.1～1.2。开放权重排序大致：Kimi 46.5、DSV4.1 Flash 1017 32.6、GLM-5.3 31.7、MiMo-V2.6-Pro 29.9、Ling 3.1 Flash 29.6、MiniMax-M3.1-Flash 29.1、Mistral Large 4 26.1。Step 5 Preview 跌出默认 28 |
| AA 文生图 | 106 个模型 | 无新条目；Elo ±数分、名次 ±1。Sunburst 1222→1227；MAI-Image-2.6 与 Grok Imagine 2.0 互换 #5/#6；FLUX 3 Image #13（1117）、Klein #22（1043）、Fibo 2.0 #23（1040） |
| AA 图像编辑 | 77 个模型 | 无新条目。MAI-Image-2.7-Preview 仍 #2（1195→1196，样本 4,914→5,165）；Nano Banana 2.1 升到 #4；Krea 3 Ultra #5；FLUX 3 Image #15（1121）、Klein #27（1070）、Fibo 2.0 #23（1086） |

关注清单结论：Kimi 权重开放后，AA 已把它计入开放权重第一；LMArena 文本尚未纳入 K3.1 Pro。文生图主战场的变化在 LMArena（Nov 2 刷新 + GPT-Image-2.6 预备档），不在 AA Elo。

来源：[LMArena 文本](https://lmarena.ai/leaderboard/text) · [LMArena 视觉](https://lmarena.ai/leaderboard/vision) · [LMArena 文生图](https://lmarena.ai/leaderboard/text-to-image) · [AA 模型榜](https://artificialanalysis.ai/models) · [AA 文生图](https://artificialanalysis.ai/image/leaderboard/text-to-image) · [AA 图像编辑](https://artificialanalysis.ai/image/leaderboard/editing) · [AA Kimi K3.1 Pro](https://artificialanalysis.ai/models/kimi-k3-1-pro)

---

## 四、热度延续（只记变化，不展开）

| id | 当前 Trending（上期） | likes / downloads | 备注 |
|---|---|---|---|
| [moonshotai/Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) | #1（—） | 928 / 11,658 | 见重点 1 |
| [speridlabs/idol](https://huggingface.co/speridlabs/idol) | #2（#6） | 775 / 17,180 | 上期重点；衍生 turbo 见重点 3 |
| [Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) | #3（#7） | 10,732 / 2,561,845 | 老模型 |
| [ccore/Qwen3.5-4B-3D-Coder](https://huggingface.co/ccore/Qwen3.5-4B-3D-Coder) | #4（#8） | 703 / 157,157 | 社区微调 |
| [Pika-Labs/Pika-H3-Flex](https://huggingface.co/Pika-Labs/Pika-H3-Flex) | #5（#9） | 474 / 863 | — |
| [mistralai/Mistral-Large-4-1T-A52B](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B) | #6（#4） | 1,615 / 9,592 | 上期已写技术报告 |
| [nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) | #7（#3） | 3,058 / 57,297 | — |
| [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | #10（#10） | 19,212 / 8,037,597 | 11-05 有维护提交 |
| [deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) | #12（#2） | 5,330 / 243,508 | 降温 |
| [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) | #15（#1） | 1,508 / 60,681 | 窗内多为 MLX/量化维护 |
| [sensenova/SenseNova-Loop-9B-Preview](https://huggingface.co/sensenova/SenseNova-Loop-9B-Preview) | #18（#26） | 250 / 2,929 | 技术报告仍缺 |
| [Nanbeige/Nanbeige4.3-33B](https://huggingface.co/Nanbeige/Nanbeige4.3-33B) | #63（#14） | 1,050 / — | 明显降温 |
| [MiniMaxAI/MiniMax-M3.1-Flash](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash) | — | 549 / 34,815 | 11-05 有提交 |
| [inclusionAI/Ling-3.1-flash-1019](https://huggingface.co/inclusionAI/Ling-3.1-flash-1019) | — | 95 / 3,100 | README/维护 |
| [openbmb/MiniCPM-OCR-1.0](https://huggingface.co/openbmb/MiniCPM-OCR-1.0) | — | 446 / 28,207 | 11-04 更新 |
| [nvidia/DeepSeek-V4.1-Flash-1017-NVFP4](https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4) | — | 182 / 6,010 | 11-04 维护 |
| [microsoft/Mage-VL-Cowork](https://huggingface.co/microsoft/Mage-VL-Cowork) | — | 187 / — | 无新权重 |
| [baidu/Unlimited-OCR-2](https://huggingface.co/baidu/Unlimited-OCR-2) | — | 621 / — | — |
| [Edge0/Audio8-TTS-Realistic-Air](https://huggingface.co/Edge0/Audio8-TTS-Realistic-Air) | #16 附近 | 318 / 11,349 | — |
| [Comfy-Org/Idol](https://huggingface.co/Comfy-Org/Idol) | #46 | 129 / — | Idol 节点版 |

窗内没有新仓库的机构：openai、meta-llama、Qwen（无新模型仓）、deepseek-ai、zai-org、mistralai（无新主模型）等。moonshotai 本窗新增可见仓即 K3.1 Pro。

---

## 五、降权 / 冒名 / 虚假声明

**冒名 / 虚假（单独列出，不进正文结论）**
- audnai/penclaw-Kimi-K3.1-pro-unrestricted：上期已标冒名。本期仍无权重（siblings 2，0 个权重文件），gated manual，139 / 0，lastModified 11-04。**不是 Moonshot 官方。** 现已有官方 `moonshotai/Kimi-K3.1-Pro`，更不应使用该仓。
- burner22/numbat：仍在 Trending（#8），354 / 8,789。上期社区审计指出权重可由 `sha256(tensor_name)` 复现。**虚假声明，不要下载。** 衍生 kimi-chan/numbat-GGUF 仍近空仓。
- Kimi-K3.1 名称蹭热但非官方：见旁线社区衍生列表；另有 LithosAI / Inferact / RadixArk 等 DSpark/Dflash 预览，likes≤3，降权。

**降权**
- [FusionCow/Sulphur-3](https://huggingface.co/FusionCow/Sulphur-3)：Trending #9，381 / 607，gated manual，无许可证字段，来历不明。
- [deep-principle/Hydrogen-1.0](https://huggingface.co/deep-principle/Hydrogen-1.0)：gated auto，MIT，约 753B，downloads 已从 0 升到约 2 万，但仍缺可核验的官方背景与清晰卡面；不进重点。
- 去审查/改装类：AtomicChat Uncensored GGUF、OBLITERATUS obliterated、DavidAU Heretic、abliteration patch 等。
- README-only / 测试仓：Blackfrost DERISKED（0 权重）、tiny-random（约 27M 参数测试权重）。

---

## 六、更正 / 待核 / 缺口

- **更正 / 补证**：
 - 上期写 Kimi K3.1 Pro“仍不在 HF”——按 11-03 当时 org API 正确；本窗确认官方仓已可下载，并澄清博客文案未同步。
 - AA 对 Kimi 的标注：上期 “model weights are not publicly available” / isOpenWeights false → 本期 Open weights / true，并反链 HF。
 - AA 文生图/编辑 URL 从 `/text-to-image/leaderboard` 迁到 `/image/leaderboard/text-to-image` 与 `/image/leaderboard/editing`（旧路径 404）。
- **待核**：
 - Kimi：博客未更新“已发布”表述；HF createdAt 与上期不可见的差异；自报基准。
 - Ripple：TerminalBench 等自报分数；ricursive 机构背景除官网外的第三方确认。
 - idol-turbo：速度与质量自测。
 - SenseNova-Loop 技术报告仍 TBD（上期待核延续）。
- **缺口**：

 - 未找到 Moonshot 单独的“权重已发布”公告页；仅以 HF 官方仓 + AA 反链为依据。
- **下期必查**：Kimi 官方博客是否改写并发出 HF 链接；LMArena 文本是否纳入 K3.1 Pro；Ripple 是否出正式版/技术报告；SenseNova-Loop 技术报告。
