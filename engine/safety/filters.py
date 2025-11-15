from typing import List


HIGH_RISK_KEYWORDS_SELF_HARM = ["自杀", "不想活了", "活不下去"]
HIGH_RISK_KEYWORDS_HARM_OTHERS = ["杀了他", "报复他", "报复他们"]
HIGH_RISK_KEYWORDS_MEDICAL = ["诊断", "抑郁症", "精神病", "吃什么药"]


def detect_high_risk(text: str) -> List[str]:
    text = text or ""
    hits: List[str] = []
    for kw in HIGH_RISK_KEYWORDS_SELF_HARM:
        if kw in text:
            hits.append("self_harm")
            break
    for kw in HIGH_RISK_KEYWORDS_HARM_OTHERS:
        if kw in text:
            hits.append("harm_others")
            break
    for kw in HIGH_RISK_KEYWORDS_MEDICAL:
        if kw in text:
            hits.append("medical")
            break
    return hits