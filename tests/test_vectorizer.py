from engine.vectorizer.simple_text_vectorizer import SimpleTextVectorizer


def test_simple_vectorizer_basic():
    v = SimpleTextVectorizer()
    vec = v.encode("最近工作压力很大，总觉得自己不够好")
    assert 0.0 <= vec.risk_score <= 1.0
    assert isinstance(vec.motive, dict)