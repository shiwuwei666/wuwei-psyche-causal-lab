from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Any, Dict

from ..deps import get_engine
from engine.runtime.engine_core import EngineCore

router = APIRouter(tags=["analyze"])


class AnalyzeRequest(BaseModel):
    text: str
    locale: str | None = None
    meta: Dict[str, Any] | None = None


@router.post("/analyze")
def analyze(req: AnalyzeRequest, engine: EngineCore = Depends(get_engine)):
    result = engine.run_full_pipeline(req.text, req.meta or {})
    return {
        "psyche_vector": result["psyche_vector"].__dict__,
        "causal_graph": {
            "nodes": result["causal_graph"].nodes,
            "edges": [e.__dict__ for e in result["causal_graph"].edges],
        },
        "persona_bucket": result["persona_bucket"],
        "safety": result["safety"],
    }