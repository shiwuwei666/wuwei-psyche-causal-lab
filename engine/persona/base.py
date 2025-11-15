from typing import Protocol
from ..schemas import PsycheVector


class BasePersonaModel(Protocol):
    def assign_bucket(self, v: PsycheVector) -> str:
        ...