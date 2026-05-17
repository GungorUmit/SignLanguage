from types import SimpleNamespace
import server
import tasks


def test_slugify():
    assert server._slugify("Hola Mundo") == "hola_mundo"


def test_index_route(client):
    res = client.get("/")
    assert res.status_code == 200


def test_save_and_get_api_key(client):
    key = "gsk_TEST123456"
    resp = client.post("/api/save-api-key", json={"api_key": key})
    assert resp.status_code == 200
    data = resp.get_json()
    assert data.get("success") is True

    resp2 = client.get("/api/get-api-key")
    j = resp2.get_json()
    assert "api_key_masked" in j
    assert j["api_key_masked"] is not None


def test_generate_starts_task(monkeypatch, client):
    def fake_apply_async(*args, **kwargs):
        return SimpleNamespace(id="job123")

    monkeypatch.setattr(tasks.async_generate_video, "apply_async", fake_apply_async)

    resp = client.post("/api/generate", json={"texto": "Texto de prueba"})
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "processing"
    assert "job_id" in data


def test_status_endpoint(monkeypatch, client):
    monkeypatch.setattr(tasks.celery_app, "AsyncResult", lambda jid: SimpleNamespace(state="SUCCESS", result={"status": "completed"}))
    resp = client.get("/api/status/job123")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "completed"}
