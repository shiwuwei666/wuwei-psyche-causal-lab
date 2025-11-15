from functools import lru_cache
from engine.runtime.engine_core import EngineCore


@lru_cache()
def get_engine() -> EngineCore:
    return EngineCore.default()