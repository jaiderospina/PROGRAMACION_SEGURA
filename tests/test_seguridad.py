"""Pruebas de seguridad del caso.

Expresan el comportamiento seguro esperado. En la versión original del caso
FALLAN a propósito: cada prueba que pasa a verde es una corrección lograda.
Se ejecutan con:  pytest -m seguridad
"""
import re

import pytest

pytestmark = pytest.mark.seguridad


def test_login_rechaza_inyeccion_sql(cliente):
    r = cliente.post("/login", data={"usuario": "admin1'--", "clave": "x"})
    assert r.status_code == 401


def test_busqueda_no_filtra_todo_el_catalogo(cliente):
    r = cliente.get("/buscar?q=zzz%' OR 1=1 --")
    cuerpo = r.get_data(as_text=True)
    assert "Python desde cero" not in cuerpo


def test_busqueda_escapa_html(cliente):
    r = cliente.get("/buscar?q=<script>alert(1)</script>")
    assert "<script>" not in r.get_data(as_text=True)


def test_reporte_bloquea_recorrido_de_rutas(cliente):
    r = cliente.get("/reporte?nombre=../db.py")
    assert r.status_code in (400, 403, 404)


def test_reporte_solo_entrega_archivos_permitidos(cliente):
    r = cliente.get("/reporte?nombre=reporte_reservado.txt")
    assert r.status_code in (400, 403, 404)


def test_admin_exige_autenticacion_y_rol(cliente):
    r = cliente.get("/admin/usuarios")
    assert r.status_code in (401, 403)


def test_admin_rechaza_rol_lector(cliente):
    cliente.post("/login", data={"usuario": "lector1", "clave": "lectura123"})
    assert cliente.get("/admin/usuarios").status_code == 403


def test_claves_no_se_guardan_con_md5(cliente):
    import db
    con = db.conectar()
    clave = con.execute("SELECT clave FROM usuarios WHERE usuario='lector1'").fetchone()[0]
    con.close()
    assert not re.fullmatch(r"[0-9a-f]{32}", clave)


def test_clave_secreta_no_esta_incrustada():
    import app as modulo
    assert modulo.app.secret_key != "clave-de-desarrollo-123"


def test_token_de_reset_no_es_predecible(cliente):
    t = {cliente.get("/reset?usuario=lector1").get_json()["token"] for _ in range(5)}
    assert all(len(x) >= 32 for x in t)


def test_catalogo_valida_certificados():
    import inspect
    import catalogo
    assert "_create_unverified_context" not in inspect.getsource(catalogo)
