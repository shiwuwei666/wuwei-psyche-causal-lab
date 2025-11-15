from typing import Optional, Dict, List
import re

from .base import BaseVectorizer
from ..schemas import PsycheVector


class SimpleTextVectorizer(BaseVectorizer):
    """
    非常简化的示例向量器：
    - 通过关键词 + 规则拼一个大致可用的 PsycheVector
    - 仅用于 demo 和研究，不用于临床/严肃诊断
    """

    MOTIVE_KEYWORDS = {
        "安全": "safety",
        "压力": "safety",
        "被淘汰": "safety",
        "认可": "recognition",
        "肯定": "recognition",
        "价值": "value",
        "有用": "value",
        "归属": "belonging",
        "孤独": "belonging",
        "好奇": "curiosity",
        "想试试": "curiosity",
    }

    NEGATIVE_AFFECT = ["焦虑", "紧张", "害怕", "担心", "难受"]
    POSITIVE_AFFECT = ["开心", "放松", "踏实", "安心"]

    def encode(self, text: str, context: Optional[Dict] = None) -> PsycheVector:
        text = text or ""
        motive_scores: Dict[str, float] = {
            "safety": 0.0,
            "belonging": 0.0,
            "value": 0.0,
            "recognition": 0.0,
            "curiosity": 0.0,
        }

        for zh, key in self.MOTIVE_KEYWORDS.items():
            if zh in text:
                motive_scores[key] += 0.2

        affect_scores: Dict[str, float] = {
            "negative": 0.0,
            "positive": 0.0,
        }
        for kw in self.NEGATIVE_AFFECT:
            if kw in text:
                affect_scores["negative"] += 0.2
        for kw in self.POSITIVE_AFFECT:
            if kw in text:
                affect_scores["positive"] += 0.2

        belief_bias: Dict[str, float] = {
            "perfectionism": 0.0,
            "self_doubt": 0.0,
        }
        if re.search(r"不够好|不行|不如别人", text):
            belief_bias["self_doubt"] = 0.7
        if "必须" in text or "一定要" in text:
            belief_bias["perfectionism"] = 0.5

        behavior_tendency: Dict[str, float] = {
            "avoidance": 0.0,
            "overwork": 0.0,
        }
        if "加班" in text or "拼命" in text:
            behavior_tendency["overwork"] = 0.6
        if "想躲开" in text or "逃避" in text:
            behavior_tendency["avoidance"] = 0.6

        context_tags: List[str] = []
        if "工作" in text or "公司" in text:
            context_tags.append("work")
        if "家人" in text or "父母" in text:
            context_tags.append("family")

        risk_score = min(
            1.0,
            affect_scores["negative"]
            + belief_bias["self_doubt"] * 0.5
            + behavior_tendency["avoidance"] * 0.3,
        )

        return PsycheVector(
            motive=motive_scores,
            belief_bias=belief_bias,
            affect=affect_scores,
            behavior_tendency=behavior_tendency,
            context_tags=context_tags,
            risk_score=risk_score,
        )