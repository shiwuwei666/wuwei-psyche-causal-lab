from typing import Protocol, List, Dict, Any
from ..schemas import PsycheVector


class BaseStrategyEngine(Protocol):
    def suggest(self, v: PsycheVector, persona_bucket: str) -> List[Dict[str, Any]]:
        ...