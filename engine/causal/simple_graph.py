from typing import Dict, Any, List

from .base import BaseCausalEngine
from ..schemas import PsycheVector, CausalGraph, CausalEdge, SimulationResult


class SimpleCausalEngine(BaseCausalEngine):
    """
    简化版因果图：
    Motive -> Belief -> Affect -> Behavior -> Risk
    权重只是示意，并非真实临床参数。
    """

    def build_graph(self, v: PsycheVector) -> CausalGraph:
        nodes = ["Motive", "Belief", "Affect", "Behavior", "Risk"]
        edges: List[CausalEdge] = [
            CausalEdge("Motive", "Belief", 0.6, "动因影响信念解释"),
            CausalEdge("Belief", "Affect", 0.7, "信念调节情绪强度"),
            CausalEdge("Affect", "Behavior", 0.5, "情绪驱动行为倾向"),
            CausalEdge("Behavior", "Risk", 0.4, "行为模式影响风险"),
            CausalEdge("Belief", "Risk", 0.3, "极端信念直接抬升风险"),
        ]
        return CausalGraph(nodes=nodes, edges=edges)

    def simulate(self, v: PsycheVector, interventions: Dict[str, Any]) -> SimulationResult:
        modified = PsycheVector(
            motive=dict(v.motive),
            belief_bias=dict(v.belief_bias),
            affect=dict(v.affect),
            behavior_tendency=dict(v.behavior_tendency),
            context_tags=list(v.context_tags),
            risk_score=v.risk_score,
        )

        delta_belief = 0.0
        if "belief.perfectionism" in interventions:
            delta = interventions["belief.perfectionism"]
            modified.belief_bias["perfectionism"] = max(
                0.0, min(1.0, modified.belief_bias.get("perfectionism", 0.0) + delta)
            )
            delta_belief += delta

        modified.affect["negative"] = max(
            0.0,
            min(1.0, modified.affect.get("negative", 0.0) - 0.3 * delta_belief),
        )

        modified.risk_score = max(
            0.0,
            min(
                1.0,
                modified.affect["negative"]
                + modified.belief_bias.get("self_doubt", 0.0) * 0.5,
            ),
        )

        return SimulationResult(
            original_vector=v,
            modified_vector=modified,
            intervention=interventions,
            notes="Simple rule-based simulation, for research/demo only.",
        )