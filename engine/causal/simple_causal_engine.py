from typing import Dict, Any

from .base import BaseCausalEngine
from ..schemas import PsycheVector, SimulationResult, CausalGraph, CausalEdge


class SimpleCausalEngine(BaseCausalEngine):
    """
    Simplified (non-patented) counterfactual engine.
    Used ONLY for research, demo and educational purposes.
    """

    def __init__(self, psyche_vector: PsycheVector | None = None):
        self.vector = psyche_vector

    def build_graph(self, v: PsycheVector | None = None) -> CausalGraph:
        nodes = ["Motive", "Belief", "Affect", "Behavior", "Risk"]
        edges = [
            CausalEdge("Motive", "Belief", 0.6, "动因影响信念解释"),
            CausalEdge("Belief", "Affect", 0.7, "信念调节情绪强度"),
            CausalEdge("Affect", "Behavior", 0.5, "情绪驱动行为倾向"),
            CausalEdge("Behavior", "Risk", 0.4, "行为模式影响风险"),
        ]
        return CausalGraph(nodes=nodes, edges=edges)

    def simulate_counterfactual(self, belief: str, delta: float) -> Dict[str, Any]:
        affect_change = delta * 0.7
        risk_change = affect_change * 0.4
        return {
            "input": {"belief": belief, "delta": delta},
            "graph": {
                "nodes": [n for n in self.build_graph().nodes],
                "edges": [e.__dict__ for e in self.build_graph().edges],
            },
            "effect": {
                "affect_change": affect_change,
                "risk_change": risk_change,
            },
            "note": "This is a simplified educational demo, NOT the full causal reasoning system.",
        }

    def simulate(self, v: PsycheVector, interventions: Dict[str, Any]) -> SimulationResult:
        belief = interventions.get("belief", "")
        delta = float(interventions.get("delta", 0.0))
        effect = self.simulate_counterfactual(belief, delta)

        modified = PsycheVector(
            motive=dict(v.motive),
            belief_bias=dict(v.belief_bias),
            affect=dict(v.affect),
            behavior_tendency=dict(v.behavior_tendency),
            context_tags=list(v.context_tags),
            risk_score=max(0.0, min(1.0, v.risk_score + effect["effect"]["risk_change"])),
        )

        modified.affect["negative"] = max(
            0.0, min(1.0, modified.affect.get("negative", 0.0) - effect["effect"]["affect_change"])
        )

        return SimulationResult(
            original_vector=v,
            modified_vector=modified,
            intervention={"belief": belief, "delta": delta},
            notes="Simplified linear counterfactual placeholder.",
        )