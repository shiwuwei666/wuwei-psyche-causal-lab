"""
官方 Demo 场景脚本

用法：
    python examples/scripts/demo_scenarios.py
"""

from engine.runtime.engine_core import EngineCore
from engine.causal.simple_causal_engine import SimpleCausalEngine


SCENARIOS = [
    {
        "id": "S1",
        "title": "工作压力 × 自我怀疑",
        "text": "最近工作压力特别大，总觉得自己不够好，担心哪天就被淘汰了。加班到很晚也睡不好，一想到明天开会就心慌。",
    },
    {
        "id": "S2",
        "title": "亲密关系不安",
        "text": "最近总觉得对象会离开我，他没回消息我就一直刷手机，会脑补各种最坏的情况，控制不住想发很多消息去确认。",
    },
    {
        "id": "S3",
        "title": "轻度抑郁样无力感",
        "text": "最近什么都提不起兴趣，做什么都觉得没意义。明明也没有特别大的事，但就是觉得每天像机械一样活着，心里挺空的。",
    },
    {
        "id": "S4",
        "title": "好奇探索型（低风险）",
        "text": "最近对心理学和人工智能特别好奇，感觉像打开了一个新的世界，很想系统地学一学，看看能不能用在自己的人生和工作上。",
    },
]


def run_scenario(engine: EngineCore, scenario: dict):
    print("=" * 80)
    print(f"[{scenario['id']}] {scenario['title']}")
    print("- 输入文本:")
    print("  ", scenario["text"])
    print("-" * 80)

    result = engine.run_full_pipeline(scenario["text"])
    v = result["psyche_vector"]
    persona = result.get("persona_bucket")
    safety = result.get("safety", {})

    print("PsycheVector 摘要:")
    print("  Motive:", getattr(v, "motive", None))
    print("  Belief Bias:", getattr(v, "belief_bias", None))
    print("  Affect:", getattr(v, "affect", None))
    print("  Behavior:", getattr(v, "behavior_tendency", None))
    print("  Risk Score:", getattr(v, "risk_score", None))
    print("  Persona Bucket:", persona)
    print("  Safety Mode:", safety.get("mode"))

    causal_engine = SimpleCausalEngine(v)
    cf = causal_engine.simulate_counterfactual("self_doubt", -0.2)

    print("\n简化反事实 Demo: belief='self_doubt', delta=-0.2")
    print("  Affect Change:", cf["effect"]["affect_change"])
    print("  Risk Change:", cf["effect"]["risk_change"])
    print("  Note:", cf["note"])
    print()


def main():
    engine = EngineCore.default()
    for s in SCENARIOS:
        run_scenario(engine, s)


if __name__ == "__main__":
    main()