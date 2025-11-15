from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Any, Dict

from ..deps import get_engine
from engine.runtime.engine_core import EngineCore
from engine.causal.simple_causal_engine import SimpleCausalEngine

router = APIRouter(tags=["causal"])


class CausalSimRequest(BaseModel):
    text: str
    belief: str = "self_doubt"
    delta: float = -0.2
    meta: Dict[str, Any] | None = None


@router.post("/causal/simulate")
def simulate_counterfactual(req: CausalSimRequest, engine: EngineCore = Depends(get_engine)):
    """
    Simplified counterfactual demo endpoint.

    - 使用 SimpleTextVectorizer 先生成 PsycheVector
    - 然后用 SimpleCausalEngine 做一个线性反事实演示
    - 仅用于教学/研究 demo，不代表完整因果引擎
    """
    v = engine.vectorizer.encode(req.text, context=req.meta or {})
    causal_engine = SimpleCausalEngine(v)
    sim_result = causal_engine.simulate_counterfactual(req.belief, req.delta)

    return {
        "psyche_vector": v.__dict__,
        "counterfactual": sim_result,
    }