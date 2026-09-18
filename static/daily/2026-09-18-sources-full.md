# 2026-09-18 三日刊全量原始素材

这是本窗三日刊的**全量原始素材归档**，用来留档与回溯线索；**不是**站点上那篇深读正文。

- **信息窗口**：≈2026-09-15 → 2026-09-18（Asia/Singapore）
- **信息来源**
  - 官博 / arXiv 与学术
  - GitHub 发布与热仓
  - Hugging Face / 模型卡
  - X（Following / 公开 AI 讨论）

## 本期配图

![三日刊信息图](https://luoli523.github.io/guige-ai-site/img/daily/2026-09-18-infographic.png)

---

## 研 / 官博与学术

【三日刊素材 · 2026-09-18】窗口 ≈2026-09-15→18。只交素材。

### OpenAI

#### Introducing Astra for Law（Sep 17）
**人话一句** 把 GPT‑6 Astra 配成律所/法律科技可用的法律工作台：研究、工作流、合规控制 + 接法律工具。
**为何重要** Astra 垂直落地；API 侧 Harvey、Legora 等可接。
**数字/要点（官方自报·待核）** 26 个新生态插件（含 Relativity、Clio）；强调端到端法律工作流与“legal-grade”控制。
**深读** 法律 AI / 垂直 agent → **选读**。
**证据** FACT [Astra for Law](https://openai.com/index/astra-for-law)

#### Our framework for reporting model misalignment（Sep 16）
**人话一句** OpenAI 公布系统性披露模型错位/异常行为的框架，并附过去六个月 **6** 份报告，不再等凑齐再发。
**为何重要** 行业透明度信号；对齐研究/政策可读。
**深读** 对齐/安全 → **选读**。
**证据** FACT [Model misalignment reporting framework](https://openai.com/index/model-misalignment-reporting-framework)

（同窗还有广告、银发用户、商业价值度量、Cooley IPO 等客户/倡导文，信号弱，不抬。）

### Anthropic

#### Measurements for understanding the pace of AI development inside frontier labs（Sep 17）
**人话一句** Anthropic 提议并自报三组「实验室内部节奏」指标：AI 做了多少 AI R&D、agent 被怎么盯着、算力怎么分。
**为何重要** 少见的一线实验室过程透明度；服务「是否该放缓」公共讨论。
**数字（官方自报·待核，截至约 2026-08）** Claude「主导(AL4)」约占 AI R&D **26%**；≥「协作(AL3)」**>90%**；尚无 AL5 全自主子集。监测：相关 agent 行动 **100%** 经在线监控。算力快照（7/13–7/20）：AI R&D 中安全约 **6%**，AI 驱动的 AI R&D 中安全约 **12%**（保守口径）。计划嵌入多组织第三方评估员。
**深读** 政策/对齐 → **必读/选读**。
**证据** FACT [Measuring pace of AI development](https://www.anthropic.com/institute/measuring-pace-of-ai-development)

### Google DeepMind

#### Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking（Sep 15）
**人话一句** 新一代实时语音对话模型：Live 偏自然流畅，Live Extended Thinking 边说边深思/做复杂任务。
**为何重要** 语音 agent 产品线升级；API / Workspace / Gemini app 可用。
**数字（官方自报·待核）** Extended Thinking：Artificial Analysis Speech-to-Speech Quality Index **#1（82.6）**；τ-Voice **68.6%**；τ-Voice-banking **35.1%**。Live：Speech Agent Arena 偏好第二；近实时视觉；**97** 语种中途切换；后台工具调用不打断对话；音频 SynthID 水印。
**深读** 语音/多模态产品 → **选读**。
**证据** FACT [Gemini 3.8 Live](https://deepmind.google/blog/introducing-gemini-3-8-live-and-3-8-live-extended-thinking/)
（blog.google 另有科学应用/多语言等软文，不抬。）

### Meta AI / Microsoft Research
本窗 **无够格新官博**。

### arXiv（RSS 最新可见批为 **Thu 17 Sep**；周末空窗）

#### NeMo Data Designer — NVIDIA（[arXiv:2609.17699](https://arxiv.org/abs/2609.17699)）
**人话一句** 开源多模态合成数据框架：声明式列配置 + 预览迭代，服务 Nemotron 与企业场景。
**为何重要** 大厂数据基建开源。
**深读** 数据/训练 → **选读**。代码：NVIDIA-NeMo/DataDesigner。

#### Do Frontier Models Seek Safety Evidence Before Acting? — [arXiv:2609.17865](https://arxiv.org/abs/2609.17865)
**人话一句** 测前沿模型在行动前会不会主动去拿安全证据（SAFE 基准）；非大厂一作。
**为何重要** 对齐评测新角度。
**深读** 安全 → 选读摘要即可。

#### ERPBench — [arXiv:2609.17885](https://arxiv.org/abs/2609.17885)
**人话一句** 企业 ERP 上的 computer-use agent 评测（状态落地、改持久业务记录）。
**为何重要** 企业 CUA 评测缺口。
**深读** Agent 评测 → 选读。

**组装提示**：主线可走「透明度双发（OpenAI 错位披露 + Anthropic 内部节奏指标）+ Gemini 3.8 Live 产品 + Astra for Law 垂直」。

---

【三日刊 · arXiv 补丁】升级选题（9/15–17 批；9/18 批尚未出）。严格大厂一作仍稀；NVIDIA NeMo 维持，并换入更高信号热题：

1) **Trusting Trust Revisited** [arXiv:2609.17817](https://arxiv.org/abs/2609.17817) — UW/Georgetown
人话：给会自我改写的 coding agent 投毒「自测基准」，可让它在干净任务上写出漏洞，且常扛过后续干净进化。
为何重要：RSI×供应链攻击面；基准投毒=控制面。
数字：论文自报 PoC（含关 HTTPS 校验等）·待核。
深读：安全/agent → **选读**。

2) **RSIAgent** [arXiv:2609.15364](https://arxiv.org/abs/2609.15364) — Aether/UCSD/UIC
人话：免训多智能体 RSI（课程+actor+verifier）靠环境记忆提升 OSWorld/ALE。
为何重要：显式 RSI；强宣称相对闭源前沿 ·**高度待核**。
深读：RSI → 选读，数字勿当事实。

3) **SWE-bench 收敛审计** [arXiv:2609.17394](https://arxiv.org/abs/2609.17394) — Imperial 等
人话：榜上前列已统计不可分；scaffold 差异远大于相邻名次。
为何重要：采购/对比别再迷信 Verified 小数点。
深读：评测 → **选读**。

4) **Coalitional alignment** [arXiv:2609.15803](https://arxiv.org/abs/2609.15803) — Collina/Goel/Roth/Sengupta
人话：把审批权交给一群可能不对齐的审查 agent，何时仍「够安全」。
为何重要：人盯不过来时的 AI 盯 AI 理论。
深读：对齐理论 → 选读。

5) **MODA** [arXiv:2609.14896](https://arxiv.org/abs/2609.14896) — UW/Stanford（含 Yejin Choi、Natasha Jaques）
人话：用 mode-conditioned RL 同时拉高质量与多样性，抗对齐 mode collapse。
为何重要：产品侧同质化痛点。
数字：论文自报多样性大涨 ·待核。

**维持** NVIDIA NeMo Data Designer [arXiv:2609.17699](https://arxiv.org/abs/2609.17699)。
可降级：SAFE / ERPBench。官博包不变。

---

【三日刊 · 官博微补】漏网 1 条 + Astra for Law 数字补强：

**Anthropic · Life Sciences Verification Program（Sep 17）**
人话：给通过核验的生命科学机构放开 Mythos/Opus/Sonnet 的生物类限制（相对公开版 Fable），分 Standard / High-risk（半年一审）；网络等非生物防护仍开。
为何重要：双用途生物政策落地——不是一刀切，而是门禁放行。
数字：早期已接入「数十」家；High-risk 每 6 个月续期（官方自报）。
证据 FACT [Life Sciences Verification Program](https://www.anthropic.com/news/life-sciences-verification-program)
深读：政策/生物安全 → **选读**。

**Astra for Law 数字补强（官方自报·待核）**
法律检索索引 >2.3 亿 URL；覆盖 >99.9% 已公布美国先例判例；整体正确性 54.0% vs 仅联网 Astra 38.7%（约 +40% 相对）；案例题多找 24% 参考案例、相关段落最高 +54%。

其余 OpenAI 广告/银发/ROI 文、Google Keyword 科学/语言包仍不抬。Meta/MSR 仍 ZERO。

---

## GitHub

【三日刊采集完成 · GitHub 2026-09-18】已双投递（用户聊天 + 本条）。
快照：2026-09-18T01:23:42Z / 09:23 SGT｜窗口：≈09-15→09-18

### 重要发布
1. openai/codex rust-v0.155.0 — /voice + MCP Touch ID + daemon 恢复 — ⭐124929 — FACT [GitHub Release](https://github.com/openai/codex/releases/tag/rust-v0.155.0)
2. openai-python v3.15.0 — agent session/WS/prewarming — ⭐31638 — FACT [GitHub Release](https://github.com/openai/openai-python/releases/tag/v3.15.0)
3. huggingface_hub v1.32.0 — Shared blob store 跨仓去重 — ⭐3908 — FACT [GitHub Release](https://github.com/huggingface/huggingface_hub/releases/tag/v1.32.0)
4. Qwen Code v0.24.0（+Desktop）— Breaking + hooks/daemon — ⭐27932 — FACT [GitHub Release](https://github.com/QwenLM/qwen-code/releases/tag/v0.24.0)
5. anthropic-sdk-python v1.6.0 — Managed Agents auto permissions + compaction — ⭐3905 — FACT [GitHub Release](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v1.6.0)

### 热仓
6. Trending Skills 集群 — security-audit-skill / agent-skills / claude-code / ECC — FACT [GitHub Trending](https://github.com/trending?since=daily)
7. deepseek-harness dsh-v0.1.6-alpha.2 — 插件管理/审阅卡 — ⭐227977 — FACT [GitHub Release](https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.1.6-alpha.2)

### 关键 org
8. anthropics/uplifting-biomolecular-modeling — 生物分子优化 kit 新仓 — ⭐48 — FACT [GitHub Repo](https://github.com/anthropics/uplifting-biomolecular-modeling)

头条候选：Codex 0.155 → openai-python 3.15 → HF Hub blob → 生物分子 kit → Trending Skills。完整人话理解层已发用户侧。

---

## 模型 / Hugging Face

【HF/模型素材包 · 三日刊 2026-09-18】
窗口：≈2026-09-15 09:00 SGT → 2026-09-18 09:21
来源：HF Trending + `/api/models|datasets`；不编造 benchmark。已双投递用户。宁缺毋滥。

### 1. Edge0/Edge0-35B-A3B-preview（窗口更新 · 三日最强信号）
- **人话**：端侧/边缘向 35B-A3B MoE 预览（约 3B 激活），Apache-2.0；标签含 mlx / prerouter / ssd-offload。
- **为何重要**：09-17 再更新，Trending #1；likes≈3307 / downloads≈37k（较 9/15 刊明显爬升）。
- **对谁有用 / 建议**：端侧 MoE、本地大模型部署 → **值得读卡**；仍是 preview，生产前核稳定性与基座授权（待核）。
- **证据**：FACT｜[HF · Edge0](https://huggingface.co/Edge0/Edge0-35B-A3B-preview)

### 2. m-a-p/YuE2-3B（窗口更新 · 音乐）
- **人话**：MAP 文生音乐 / 符号规划模型（text-to-audio），非聊天；许可 CC-BY-NC-4.0。
- **为何重要**：09-16 更新并维持高 Trending（likes≈721 / dl≈11.6k）。
- **对谁有用 / 建议**：音乐 AIGC → **扫卡**；商用先核 NC 许可。
- **证据**：FACT｜[HF · YuE2-3B](https://huggingface.co/m-a-p/YuE2-3B)

### 3. nvidia 量化部署线（窗口内多卡）
- **人话**：NVIDIA 把热门开源卡压成 NVFP4，方便自家栈省显存跑。
- **为何重要**：窗口内可见 `Qwen3.8-27B-NVFP4`（likes≈105 / dl≈83k，09-17 更新）与新建 `DeepSeek-V4.1-Flash-NVFP4`（09-16 创建，热度仍低）。
- **对谁有用 / 建议**：NVIDIA 部署/推理优化 → **Qwen NVFP4 可跟**；DeepSeek 量化卡尚早，扫一眼即可。
- **证据**：FACT｜[HF · Qwen3.8-27B-NVFP4](https://huggingface.co/nvidia/Qwen3.8-27B-NVFP4) ｜[HF · DeepSeek-V4.1-Flash-NVFP4](https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-NVFP4)

### 4. nex-agi/Nex-N2.5-Pro（窗口更新）
- **人话**：Nex 开源 MoE（标签 qwen3_5_moe），Apache-2.0。
- **为何重要**：09-17 更新（likes≈660 / dl≈31k），三日仍有维护信号。
- **对谁有用 / 建议**：猎新开源基座 → **扫一眼**；评测深度待核。
- **证据**：FACT｜[HF · Nex-N2.5-Pro](https://huggingface.co/nex-agi/Nex-N2.5-Pro)

### 背景热度（不占头条）
- **deepseek-ai/DeepSeek-V4.1-Flash**：仍居 Trending 前列（likes≈3005 / dl≈391k），**本窗无新 mod** → 延续故事，勿写成新发。[HF · DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- **openbmb/MiniCPM5-2B**：端侧热度延续（likes≈1537 / dl≈330k），本窗无新 mod。
- **tencent EVIE-8B/4.5B**：09-17 有更新的视觉文档检索；热度中低。WeVisDoc 新建但 downloads≈0 → 暂缓头条。
- **ibm-granite/granite-speech-5.0-470m-turboctc**：窗口有改的小体积 ASR（dl≈37k）→ 语音垂直可扫。
- **降权**：Uncensored/魔改 GGUF、downloads=0 的社区卡。

### 大厂空白
Qwen / DeepSeek / Google / Meta / Mistral / MiniMax / Z.ai 本三日几乎无新基座；官方动作偏 **NVIDIA 量化包装、腾讯文档检索小更新**。

### 归并建议
三日主信号：**Edge0 端侧 MoE 继续爆发、YuE2 音乐更新、NVIDIA NVFP4 部署线**。其余次要或跳过。

（只交素材，不成稿。可归并主线。）

---

## X 动态

【三日刊·X素材 · 2026-09-18 | 双投递】窗≈09-15→18。用户侧已交同包。够格摘要：

1. Astra for Law [X post](https://x.com/OpenAI/status/2100679992720142459) 官方自报 · Today's News
2. Anthropic R&D pace 指标 [X post](https://x.com/AnthropicAI/status/2100684274114699295) · [Measuring pace of AI development](https://www.anthropic.com/institute/measuring-pace-of-ai-development) 官方自报
3. Claude Projects 并行线程 [X post](https://x.com/claudeai/status/2100632677904744716) 官方自报 · Today's News
4. 生物分子开源模推理加速 [X post](https://x.com/AnthropicAI/status/2100701581109072332) 官方自报
5. AlphaGenome Atlas [X post](https://x.com/GoogleDeepMind/status/2100586770572177551) 官方自报
6. Google Home MCP [X post](https://x.com/TechCrunch/status/2100269763549176222) · TechCrunch / Google Home devices 待核/FACT
7. WhatsApp Business MCP [X post](https://x.com/TechCrunch/status/2099955188467405227) 待核
8. Unity Codex 插件 [X post](https://x.com/OpenAIDevs/status/2100742955191484909) 官方自报

网页：Gemini 3.8 Live · OpenAI misalignment framework · SF Koa · Muse Mac · 三家安全谈
主轴：垂直Agent / MCP物理化 / 研发自测与错位披露。无新frontier基座。只交素材。
