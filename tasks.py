from types import SimpleNamespace


# Minimal stub for celery_app used in tests
class _Conf:
    def __init__(self):
        self.task_always_eager = False


class _CeleryApp:
    def __init__(self):
        self.conf = _Conf()

    def AsyncResult(self, jid):
        # Default placeholder: pending
        return SimpleNamespace(state="PENDING", result=None)


celery_app = _CeleryApp()


def _fake_apply_async(*args, **kwargs):
    return SimpleNamespace(id="fake-job")


def async_generate_video(*args, **kwargs):
    # placeholder synchronous function
    return {"status": "completed"}


async_generate_video.apply_async = _fake_apply_async
from types import SimpleNamespace


# Minimal stub for celery_app used in tests
class _Conf:
    def __init__(self):
        self.task_always_eager = False


class _CeleryApp:
    def __init__(self):
        self.conf = _Conf()

    def AsyncResult(self, jid):
        # Default placeholder: pending
        return SimpleNamespace(state="PENDING", result=None)


celery_app = _CeleryApp()


def _fake_apply_async(*args, **kwargs):
    return SimpleNamespace(id="fake-job")


def async_generate_video(*args, **kwargs):
    # placeholder synchronous function
    return {"status": "completed"}


async_generate_video.apply_async = _fake_apply_async
