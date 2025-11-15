from .base import BasePersonaModel
from ..schemas import PsycheVector


class SimplePersonaBuckets(BasePersonaModel):
    """
    根据动因分布粗略分桶，仅用于群体画像/报表，不用于标签化个体。
    """

    def assign_bucket(self, v: PsycheVector) -> str:
        motive = v.motive or {}
        if not motive:
            return "unknown"

        key = max(motive, key=motive.get)
        mapping = {
            "safety": "safety_dominant",
            "belonging": "belonging_dominant",
            "value": "value_dominant",
            "recognition": "recognition_dominant",
            "curiosity": "curiosity_dominant",
        }
        return mapping.get(key, "mixed")