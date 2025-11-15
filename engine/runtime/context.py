from dataclasses import dataclass
from typing import Optional, Dict, Any
from ..schemas import PsycheVector


@dataclass
class SessionContext:
    session_id: str
    last_vector: Optional[PsycheVector] = None
    meta: Dict[str, Any] = None