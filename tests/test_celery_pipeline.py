import os
import subprocess

import tasks


def test_async_generate_video_pipeline(monkeypatch):
    tasks.celery_app.conf.task_always_eager = True
    monkeypatch.setattr(tasks, "log_emission", lambda *a, **k: None)

    def fake_run(cmd, check, capture_output, text, env, timeout):
        out = None
        if "--output" in cmd:
            idx = cmd.index("--output")
            out = cmd[idx + 1]
        if out:
            os.makedirs(os.path.dirname(out), exist_ok=True)
            with open(out, "wb") as f:
                f.write(b"dummy")
        return subprocess.CompletedProcess(cmd, 0, stdout="ok", stderr="")

    monkeypatch.setattr(subprocess, "run", fake_run)

    eager_result = tasks.async_generate_video.apply(args=("texto de prueba", "celery-pipeline-test", {}))
    result = getattr(eager_result, "result", None)
    assert isinstance(result, dict)
    assert result.get("status") == "completed"
    assert os.path.exists("assets/output/celery-pipeline-test.mp4")
