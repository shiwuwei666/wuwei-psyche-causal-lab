from fastapi.testclient import TestClient
from apps.api.main import app


client = TestClient(app)


def test_causal_simulate_endpoint():
    resp = client.post(
        "/v1/causal/simulate",
        json={"text": "最近工作压力很大，总觉得自己不够好。"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "psyche_vector" in data
    assert "counterfactual" in data
    assert "effect" in data["counterfactual"]