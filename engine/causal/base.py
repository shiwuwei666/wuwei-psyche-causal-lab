from typing import Protocol, Dict, Any
from ..schemas import PsycheVector, CausalGraph, SimulationResult


class BaseCausalEngine(Protocol):
    def build_graph(self, v: PsycheVector) -> CausalGraph:
        ...

    def simulate(self, v: PsycheVector, interventions: Dict[str, Any]) -> SimulationResult:
        ...