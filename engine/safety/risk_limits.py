from dataclasses import dataclass


@dataclass
class RiskConfig:
    max_strategy_risk: float = 0.4
    max_cf_risk: float = 0.6


DEFAULT_RISK_CONFIG = RiskConfig()