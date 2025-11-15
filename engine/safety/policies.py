from typing import Dict, Any, List
from ..schemas import PsycheVector
from .risk_limits import RiskConfig, DEFAULT_RISK_CONFIG
from .filters import detect_high_risk


def apply_safety_policy(
    text: str,
    vector: PsycheVector,
    raw_suggestions: List[Dict[str, Any]],
    risk_cfg: RiskConfig = DEFAULT_RISK_CONFIG,
) -> Dict[str, Any]:
    """
    根据风险和高危关键词决定：
    - 返回低风险建议
    - 还是仅返回安全提示
    """
    hits = detect_high_risk(text)
    high_risk_flag = bool(hits) or vector.risk_score >= risk_cfg.max_strategy_risk

    if high_risk_flag:
        return {
            "mode": "safe_message_only",
            "reasons": hits or ["high_risk_score"],
            "message": (
                "当前内容可能涉及较高风险。本工具不提供医疗或紧急干预建议。"
                "如果你有自伤或他伤的念头，请尽快联系当地专业机构或紧急电话。"
            ),
            "suggestions": [],
        }

    safe_suggestions = [s for s in raw_suggestions if s.get("risk_level") == "low"]
    return {
        "mode": "normal",
        "reasons": [],
        "message": "",
        "suggestions": safe_suggestions,
    }