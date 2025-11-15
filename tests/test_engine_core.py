from engine.runtime.engine_core import EngineCore


def test_engine_core_pipeline_basic():
    engine = EngineCore.default()
    result = engine.run_full_pipeline("最近工作压力很大，总觉得自己不够好。")
    v = result["psyche_vector"]
    assert 0.0 <= v.risk_score <= 1.0
    assert isinstance(result["persona_bucket"], str)
    assert "safety" in v.motive


def test_engine_core_safety_layer():
    engine = EngineCore.default()
    text = "我最近经常想自杀，不想活了。"
    result = engine.run_full_pipeline(text)
    safety = result["safety"]
    assert safety["mode"] == "safe_message_only"
    assert safety["suggestions"] == []