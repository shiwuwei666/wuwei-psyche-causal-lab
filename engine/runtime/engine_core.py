from dataclasses import dataclass
from typing import Dict, Any

from ..schemas import PsycheVector
from ..vectorizer.simple_text_vectorizer import SimpleTextVectorizer
from ..causal.simple_causal_engine import SimpleCausalEngine
from ..persona.simple_buckets import SimplePersonaBuckets
from ..strategy.low_risk_rules import LowRiskStrategyEngine
from ..safety.policies import apply_safety_policy


@dataclass
class EngineCore:
    vectorizer: Any
    causal_engine: Any
    persona_model: Any
    strategy_engine: Any

    @classmethod
    def default(cls) -> "EngineCore":
        return cls(
            vectorizer=SimpleTextVectorizer(),
            causal_engine=SimpleCausalEngine(),
            persona_model=SimplePersonaBuckets(),
            strategy_engine=LowRiskStrategyEngine(),
        )

    def run_full_pipeline(self, text: str, meta: Dict[str, Any] | None = None) -> Dict[str, Any]:
        v: PsycheVector = self.vectorizer.encode(text, context=meta)
        graph = self.causal_engine.build_graph(v)
        bucket = self.persona_model.assign_bucket(v)
        raw_suggestions = self.strategy_engine.suggest(v, bucket)
        safety_result = apply_safety_policy(text, v, raw_suggestions)

        return {
            "psyche_vector": v,
            "causal_graph": graph,
            "persona_bucket": bucket,
            "safety": safety_result,
        }