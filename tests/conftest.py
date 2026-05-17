import sqlite3
import pytest
from types import SimpleNamespace

import server
import tasks


@pytest.fixture(autouse=True)
def in_memory_db_and_celery(monkeypatch):
    # Shared in-memory DB helpers
    conn = sqlite3.connect(":memory:", check_same_thread=False)

    def _init_db_shared():
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS emissions
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT, output_path TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        c.execute('''CREATE TABLE IF NOT EXISTS settings
                     (key TEXT PRIMARY KEY, value TEXT)''')
        conn.commit()

    def _set_setting_shared(key, value):
        c = conn.cursor()
        c.execute("REPLACE INTO settings (key, value) VALUES (?, ?)", (key, value))
        conn.commit()

    def _get_setting_shared(key):
        c = conn.cursor()
        c.execute("SELECT value FROM settings WHERE key = ?", (key,))
        row = c.fetchone()
        return row[0] if row else None

    def _log_emission_shared(text, output_path):
        c = conn.cursor()
        c.execute("INSERT INTO emissions (text, output_path) VALUES (?, ?)", (text, output_path))
        conn.commit()

    monkeypatch.setattr(server, "init_db", _init_db_shared)
    monkeypatch.setattr(server, "set_setting", _set_setting_shared)
    monkeypatch.setattr(server, "get_setting", _get_setting_shared)
    monkeypatch.setattr(server, "log_emission", _log_emission_shared)

    # Disable cryptography Fernet in tests
    monkeypatch.setattr(server, "FERNET", None)

    # Make Celery tasks run eagerly
    try:
        tasks.celery_app.conf.task_always_eager = True
    except Exception:
        pass

    # Patch apply_async to avoid external workers
    def _fake_apply_async(*args, **kwargs):
        return SimpleNamespace(id="test-job")

    monkeypatch.setattr(tasks.async_generate_video, "apply_async", _fake_apply_async)

    yield


@pytest.fixture
def client():
    server.app.config["TESTING"] = True
    with server.app.test_client() as c:
        yield c
