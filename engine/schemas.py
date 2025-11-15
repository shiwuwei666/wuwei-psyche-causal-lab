from dataclasses import dataclass, field
from typing import Dict, List, Any


@dataclass
class PsycheVector:
    """
    简化版心理向量：
    - motive: 动因分布
    - belief_bias: 信念偏差/信念核相关因子
    - affect: 情绪因子
    - behavior_tendency: 行为倾向
    - context_tags: 情境标签
    - risk_score: 风险评分（0~1）
    """
    motive: Dict[str, float]
    belief_bias: Dict[str, float]
    affect: Dict[str, float]
    behavior_tendency: Dict[str, float]
    context_tags: List[str] = field(default_factory=list)
    risk_score: float = 0.0


@dataclass
class CausalEdge:
    source: str
    target: str
    weight: float
    description: str = ""


@dataclass
class CausalGraph:
    nodes: List[str]
    edges: List[CausalEdge]


@dataclass
class SimulationResult:
    original_vector: PsycheVector
    modified_vector: PsycheVector
    intervention: Dict[str, Any]
    notes: str = ""