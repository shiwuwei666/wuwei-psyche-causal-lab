"""
简单命令行 Demo：
python examples/scripts/demo_cli.py "最近工作压力很大，总觉得自己不够好。"
"""

import sys
from engine.runtime.engine_core import EngineCore
from engine.causal.simple_causal_engine import SimpleCausalEngine


def main():
    if len(sys.argv) < 2:
        print("用法: python demo_cli.py \"你的句子...\"")
        sys.exit(1)

    text = sys.argv[1]
    engine = EngineCore.default()
    result = engine.run_full_pipeline(text)
    v = result["psyche_vector"]

    print("=== PsycheVector ===")
    print("Motive:", v.motive)
    print("Belief Bias:", v.belief_bias)
    print("Affect:", v.affect)
    print("Behavior:", v.behavior_tendency)
    print("Risk Score:", v.risk_score)

    causal_engine = SimpleCausalEngine(v)
    cf = causal_engine.simulate_counterfactual("self_doubt", -0.2)
    print("\n=== Counterfactual Demo ===")
    print(cf)


if __name__ == "__main__":
    main()