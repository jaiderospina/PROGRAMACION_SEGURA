"""Pruebas de comportamiento. Deben pasar antes y después de corregir el caso."""


def test_login_valido(cliente):
    r = cliente.post("/login", data={"usuario": "lector1", "clave": "lectura123"})
    assert r.status_code == 200


def test_login_invalido(cliente):
    r = cliente.post("/login", data={"usuario": "lector1", "clave": "otra"})
    assert r.status_code == 401


def test_buscar_devuelve_libros(cliente):
    r = cliente.get("/buscar?q=Python")
    assert r.status_code == 200
    assert "Python desde cero" in r.get_data(as_text=True)


def test_reporte_publico(cliente):
    r = cliente.get("/reporte?nombre=reporte_publico.txt")
    assert r.status_code == 200
    assert "Reporte público" in r.get_data(as_text=True)


def test_reset_usuario_inexistente(cliente):
    assert cliente.get("/reset?usuario=nadie").status_code == 404
