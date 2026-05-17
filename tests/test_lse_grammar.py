import pytest
from types import SimpleNamespace

import spoken_to_signed.text_to_gloss.llm as llm


@pytest.mark.parametrize("text", [
    "El tren va a salir pronto de la vía uno",
    "Mañana no habrá trenes a las ocho",
    "El próximo tren con destino Atocha entrará por la vía dos",
])
def test_translation(monkeypatch, text):
    monkeypatch.setattr(llm, "text_to_gloss", lambda t, lang: [[SimpleNamespace(gloss="TEST")]])
    results = llm.text_to_gloss(text, "es")
    assert isinstance(results, list)
    assert hasattr(results[0][0], "gloss")
import pytest
from types import SimpleNamespace

import spoken_to_signed.text_to_gloss.llm as llm


@pytest.mark.parametrize("text", [
    "El tren va a salir pronto de la vía uno",
    "Mañana no habrá trenes a las ocho",
    "El próximo tren con destino Atocha entrará por la vía dos",
])
def test_translation(monkeypatch, text):
    # Mock the LLM call to avoid external requests and make the test deterministic
    monkeypatch.setattr(llm, "text_to_gloss", lambda t, lang: [[SimpleNamespace(gloss="TEST")]])
    results = llm.text_to_gloss(text, "es")
    assert isinstance(results, list)
    assert hasattr(results[0][0], "gloss")
