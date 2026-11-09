"""Acceso a datos del caso. Todos los datos son sintéticos."""
import hashlib
import os
import sqlite3

BASE = os.path.dirname(os.path.abspath(__file__))
DB_POR_DEFECTO = os.path.join(BASE, "biblioteca.db")


def ruta_db():
    return os.environ.get("BIBLIOTECA_DB", DB_POR_DEFECTO)


def conectar():
    return sqlite3.connect(ruta_db())


def inicializar():
    """Crea la base de datos con datos sintéticos si no existe."""
    if os.path.exists(ruta_db()):
        return
    con = conectar()
    con.executescript(
        """
        CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY, usuario TEXT, clave TEXT, rol TEXT, documento TEXT
        );
        CREATE TABLE libros (
            id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, anio INTEGER
        );
        """
    )
    usuarios = [
        ("lector1", "lectura123", "lector", "1000000001"),
        ("lector2", "lectura456", "lector", "1000000002"),
        ("admin1", "admin123", "admin", "1000000003"),
    ]
    for u, c, r, d in usuarios:
        con.execute(
            "INSERT INTO usuarios (usuario, clave, rol, documento) VALUES (?, ?, ?, ?)",
            (u, hashlib.md5(c.encode()).hexdigest(), r, d),
        )
    libros = [
        ("Software development in practice", "Autor Ejemplo A", 2020),
        ("Fundamentos de redes", "Autora Ejemplo B", 2018),
        ("Criptografía para curiosos", "Autor Ejemplo C", 2021),
        ("Python desde cero", "Autora Ejemplo D", 2022),
    ]
    con.executemany("INSERT INTO libros (titulo, autor, anio) VALUES (?, ?, ?)", libros)
    con.commit()
    con.close()
