from typing import Protocol, Optional, Dict
from ..schemas import PsycheVector


class BaseVectorizer(Protocol):
    """
    文本 → PsycheVector 的抽象接口。
    高级实现（多模态/复杂模型）放在私有仓库，本项目只提供简化实现。
    """
    def encode(self, text: str, context: Optional[Dict] = None) -> PsycheVector:
        ...