<p align="center">
  <img src="assets/hero_banner.png" width="100%" />
</p>

<p align="center">
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-AGPL--3.0-blue.svg" />
  </a>
  <a href="https://pypi.org/project/wuwei-psyche">
    <img src="https://img.shields.io/badge/python-3.10%2B-green.svg" />
  </a>
  <img src="https://img.shields.io/badge/status-lab%20edition-lightgrey.svg" />
</p>

# Wuwei Psyche Causal Lab

> A causal psychological modeling toolkit for motives–beliefs–affect–behavior, with audit trails and safe-by-default interventions.

「**施无畏心理因果实验室**」是一套用于研究和实验  
**“动因 – 信念 – 情绪 – 行为”** 链条的轻量级工具包。

它可以帮你把一段文本转成结构化的**心理向量**、构建简化版**心理因果图**、做**反事实模拟**和**人格分桶画像**，用于：

- 心理与行为研究
- 产品/对话体验设计
- 可解释 AI 心理建模实验

> ⚠️ 本项目不是医疗诊断工具，不提供治疗或处方。  
> ⚠️ 本项目默认只提供低风险、自助型建议，并内置安全护栏。  
> 详情见：[DISCLAIMER](./DISCLAIMER.md)、[ETHICS](./ETHICS.md)、[SECURITY](./SECURITY.md)。

---

## ✨ Features / 功能一览

- 🧩 **文本 → 心理向量（PsycheVector）**
  - 动因分布（motive）
  - 信念偏差（belief_bias）
  - 情绪因子（affect）
  - 行为倾向（behavior_tendency）
  - 情境标签（context_tags）
  - 风险评分（risk_score，0–1）

- 🔗 **简化心理因果图（CausalGraph）**
  - 采用示意 DAG：Motive → Belief → Affect → Behavior → Risk
  - 每条边有方向与权重说明

- 🔁 反事实模拟：见下文“简化反事实示例”
  - 用于“如果这个信念柔和一点，会发生什么？”

- 🧱 **人格分桶（Persona Buckets）——研究/报表用**
  - 根据动因分布粗略分桶（安全感主导 / 归属主导 / 价值主导等）
  - 用于群体画像与策略效果分析

- 💡 **低风险策略建议（Low-Risk Strategies）**
  - 呼吸/放松练习
  - 情绪/念头记录
  - 联系现实中的支持系统
  - 均通过安全过滤，不含医疗/药物/强干预建议

- 🛡️ **安全护栏（Safety Layer）**
  - 高危关键词检测（自伤/他伤/医疗相关）
  - 风险阈值控制（risk ceiling）
  - 高危场景自动降级为“仅提示安全信息”

- 🌐 **FastAPI + Demo 页面**
  - `POST /v1/analyze`：一键跑完整 pipeline
  - `GET /demo`：浏览器小页面，快速体验

---

## 🏗 架构概览

```text
Text
  ↓ (SimpleTextVectorizer)
PsycheVector (motive/belief/affect/behavior/context/risk)
  ↓ (SimpleCausalEngine)
CausalGraph
  ↓ (SimplePersonaBuckets)
Persona Bucket
  ↓ (LowRiskStrategyEngine)
Raw Suggestions
  ↓ (Safety Policies)
Safe Suggestions / Safe Message Only


模块对应目录：

engine/vectorizer — 文本 → PsycheVector

engine/causal — 因果图 & 反事实模拟

engine/persona — 人格分桶

engine/strategy — 策略生成（低风险）

engine/safety — 高危检测 & 风险阈值 & 降级策略

engine/runtime — EngineCore：串接所有模块

apps/api — FastAPI 接口与演示页面

🚀 快速开始
1. 安装依赖
# 建议使用虚拟环境/uv/poetry，以下以 pip 为例
pip install -e .

2. 启动 API 服务
uvicorn apps.api.main:app --reload


打开浏览器访问：

Demo 页面：http://127.0.0.1:8000/demo

OpenAPI 文档（如果 FastAPI 默认开启）：http://127.0.0.1:8000/docs

3. 调用示例
cURL
curl -X POST http://127.0.0.1:8000/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "text": "最近工作压力很大，总觉得自己不够好，担心被淘汰。"
  }'


返回示例（简化）：

{
  "psyche_vector": {
    "motive": {"safety": 0.4, "belonging": 0.0, "value": 0.0, "recognition": 0.0, "curiosity": 0.0},
    "belief_bias": {"perfectionism": 0.5, "self_doubt": 0.7},
    "affect": {"negative": 0.4, "positive": 0.0},
    "behavior_tendency": {"avoidance": 0.0, "overwork": 0.6},
    "context_tags": ["work"],
    "risk_score": 0.68
  },
  "causal_graph": {
    "nodes": ["Motive", "Belief", "Affect", "Behavior", "Risk"],
    "edges": [
      {"source":"Motive","target":"Belief","weight":0.6,"description":"动因影响信念解释"},
      ...
    ]
  },
  "persona_bucket": "safety_dominant",
  "safety": {
    "mode": "normal",
    "message": "",
    "suggestions": [
      {"id": "breathing_1", "title": "做一个 3 分钟的呼吸练习", ...},
      ...
    ]
  }
}

📚 examples & notebooks

examples/notebooks/01_quickstart.ipynb
快速体验：文本 → 向量 → 因果图 → 建议

examples/notebooks/02_causal_graph_demo.ipynb
展示如何构建因果图和进行简单反事实模拟

examples/notebooks/03_persona_buckets.ipynb
用合成数据做“人格桶 × 策略效果”分析

（notebook 目前为占位，欢迎补充 PR）

⚖️ 使用边界 & 伦理

请在使用前务必阅读：

DISCLAIMER

ETHICS

SECURITY

简要说明：

本项目仅用于研究、教学和产品设计实验；

不应用于医疗诊断、治疗决策或紧急情况；

不应用于针对未成年人或高危人群的情感操控；

发现滥用风险，欢迎通过 Issue 或邮件反馈。

🧑‍💻 贡献指南（Contributing）

欢迎：

新的 vectorizer 实现（不同语言、不同模型）

更丰富的 demo 场景与 notebook

更严谨的安全/伦理规则讨论

测试用例与 CI 改进

请遵守：

CODE_OF_CONDUCT

🧾 Usage & Commercial Use

- 学术研究 / 教学实验：欢迎直接使用，引用本项目即可；
- 产品原型 / 内部 PoC：欢迎在团队内部试用；
- 医疗诊断 / 治疗决策：不适用（详见 DISCLAIMER）；
- 未成年人情感陪伴 / 成瘾性设计：明确不建议使用本项目。

如需在闭源商业产品中使用本项目的部分组件（例如作为心理因果引擎的一部分），可通过仓库 Issues 或邮箱与作者洽谈单独商业授权或定制合作。

📜 License

本项目代码以 AGPL-3.0-or-later 许可证发布。  
这意味着：

- 你可以自由地查看、学习和修改代码；
- 你可以基于本项目开展研究和非商业实验；
- 如果你将本项目作为在线服务的一部分向他人提供，一般情况下需要开源你的相关修改。

如需将本项目用于闭源商业产品或特殊场景，请联系我们洽谈单独授权。详情见 `LICENSE`。

---

开源发布长文 / 技术说明

一、为什么要做这样一套东西？

现在的很多 AI，都擅长一件事：预测下一个词。
但当我们问一个更人类的问题：

“TA 为什么会这么想、这么做？如果某个信念变了，会不会轻松一点？”

大多数系统就开始模糊、敷衍，甚至“编”。

我一直在做的一件事情，是把人类心理结构抽成一个可计算的模型：
从 动因（M）– 信念（B）– 情绪（A）– 行为（C） 的链条出发，让机器能够以一种可审计、可反事实推理的方式来理解“人是怎么运转的”。

这次开源的 Wuwei Psyche Causal Lab，就是这条路线中的一个“实验室版本”实现：

它不是一个“情感陪伴机器人”；

它也不是一个“临床级诊断工具”；

它是一台面向研究者、工程师和产品设计者的心理因果引擎。

你可以把它当作：

“一个能把心里话拆成结构化向量，再画成因果图，还能做一点‘如果信念柔和一点，会怎样？’的小实验机器。”

二、它到底能做什么？（开源版能力）

开源版做了几件刚刚好的事情：

文本 → 心理向量（PsycheVector）

一段中文文本，比如：

“最近工作压力很大，总觉得自己不够好，担心被淘汰。”

会被转成一个结构化向量，粗略刻画：

哪些动因在被拉扯（安全感？认同感？价值感？）

信念偏差是否偏向“完美主义 / 自我怀疑”

情绪因子大致在什么区间（负向/正向）

行为倾向像是“过度用力”还是“回避拖延”

当前情境标签（工作？家庭？自我内耗？）

一个 0–1 的风险评分（只是粗略参考）

简化心理因果图

它会构建一个小小的因果图：

Motive → Belief → Affect → Behavior → Risk


每条边有方向、有权重、有文字说明：
“动因影响信念解释”“信念调节情绪强度”“情绪驱动行为倾向”等等。

这不是为了“精准预测”，而是为了让你有一张可讨论的心理结构示意图。

反事实模拟（What if...?）

你可以对某个节点做一个小小的“如果”：

如果完美主义的强度降低一点；

如果自我怀疑稍微松动一点；

系统会用一套简单的规则，推演下游的情绪和风险评分可能会怎么变化。

它没有任何临床承诺，但非常适合做：

心理教育和认知重构的教学演示；

产品设计时，对“话术风格”的敏感性实验；

AI 人格系统中的“内部心智可视化”。

人格分桶 & 低风险建议

在合成数据或匿名数据场景下，你可以：

按“动因主导结构”给样本分桶（安全感型、价值感型等）；

看不同桶对不同策略的平均响应（比如简单的呼吸练习 / 记录练习）。

开源版里面的建议刻意做得很“温和”：

呼吸练习、写下念头、联系现实中的支持系统；

不提供任何医疗或强干预建议；

有安全模块会判断风险，一旦命中高危语境，就直接降级为“只给安全提示”。

三、它刻意“少做了什么”？（安全与边界）

因为这是一个跟“心理”和“风险”相关的系统，我在开源设计时刻意做了几件“少做”的事：

不开源临床级 / 高阶干预模块

真正更复杂的那一层：

多模态信号（生理数据、环境传感）；

高维人格/动因网络；

强干预策略和在线学习机制；

统统不会出现在这个开源仓库里。
开源版只保留了结构清晰、风险相对可控的那一圈。

默认只做“低风险、自助型”建议

不会告诉任何人“你得了什么病”；

不会给药物或治疗决策建议；

检测到自伤、他伤、医疗相关高危表达时，会直接拒绝干预，只输出安全提示，提醒去找现实中的专业机构。

不做未成年人情感操控产品

在伦理说明里，我明确写了禁止用途：

未成年人强依赖型情感陪伴；

成瘾性产品的心理剥削优化；

洗脑训练营、极端组织动员等场景。

这些是我不愿意看到这套结构被使用的地方。



—— Wuwei
Wuwei Psyche Causal Lab · 施无畏心理因果实验室
邮箱：shiwuwei666@163.com

---
🔁 Simplified Counterfactual Demo（简化反事实示例）

本仓库中包含一个简化（非专利级）反事实模拟模块：

- 仅基于固定结构的示意性因果图：`Motive → Belief → Affect → Behavior → Risk`
- 使用简单的权重与线性规则推演变化趋势
- 设计目的是教学、研究、体验心理结构的可视化
- 不包含任何商业版/专利版的高级反事实建模算法

> 声明：
> 本模块仅为“教学级占位实现（placeholder）”，并非本项目正在开发中的完整反事实机制。
> 完整版本包含更复杂的因果路径推理、信念核替换机制、路径干预模拟器、反事实评估器等内容，目前处于内部实验与专利规划阶段，因此不在开源仓库中公开。

示例：

```python
result = engine.simulate_counterfactual(
    belief="self_doubt",
    delta=-0.2,
)
```

返回的结果仅用于展示如何在心理因果图上进行反事实推演实验，不用于临床、商业决策或高风险情境。
