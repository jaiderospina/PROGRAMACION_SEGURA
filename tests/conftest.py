import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))


@pytest.fixture()
def cliente(tmp_path, monkeypatch):
    monkeypatch.setenv("BIBLIOTECA_DB", str(tmp_path / "prueba.db"))
    import db
    db.inicializar()
    import app as modulo
    modulo.app.config["TESTING"] = True
    return modulo.app.test_client()
