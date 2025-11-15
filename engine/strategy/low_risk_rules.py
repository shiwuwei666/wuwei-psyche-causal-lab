from typing import List, Dict, Any

from .base import BaseStrategyEngine
from ..schemas import PsycheVector


class LowRiskStrategyEngine(BaseStrategyEngine):
    """
    只提供低风险、自助型建议：
    - 呼吸/放松
    - 写下感受
    - 联系现实中的支持资源
    不提供任何医疗/药物/强干预建议。
    """

    def suggest(self, v: PsycheVector, persona_bucket: str) -> List[Dict[str, Any]]:
        suggestions: List[Dict[str, Any]] = []

        suggestions.append({
            "id": "breathing_1",
            "type": "self_regulation",
            "title": "做一个 3 分钟的呼吸练习",
            "risk_level": "low",
            "description": "找一个相对安静的地方，缓慢吸气 4 秒，停留 4 秒，再呼气 6 秒，重复几轮。",
        })

        suggestions.append({
            "id": "journaling_1",
            "type": "reflection",
            "title": "写下此刻最强烈的三个念头",
            "risk_level": "low",
            "description": "不评价、不压抑，只是写下来，看一看它们在说什么。",
        })

        suggestions.append({
            "id": "reach_out_1",
            "type": "social_support",
            "title": "考虑联系一个你信任的人聊一聊",
            "risk_level": "low",
            "description": "如果你愿意，可以选择一个让你相对放心的人，分享一点点你的感受。",
        })

        return suggestions