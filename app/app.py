"""Biblioteca de la Facultad: caso del curso «Fundamentos de programación
segura y criptografía básica».

ADVERTENCIA: este programa es VULNERABLE A PROPÓSITO. Sirve para practicar el
análisis de código en un entorno local. No se debe exponer a internet ni
reutilizar su código en sistemas reales.
"""
import hashlib
import random
import sqlite3
import traceback

from flask import Flask, request, send_file, session

from db import conectar, inicializar
import os

app = Flask(__name__)
app.secret_key = "clave-de-desarrollo-123"
REPORTES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reportes")


@app.route("/")
def inicio():
    return (
        "<h1>Biblioteca de la Facultad</h1>"
        "<p>Rutas: POST /login, GET /buscar?q=, GET /reporte?nombre=, "
        "GET /admin/usuarios, GET /reset?usuario=</p>"
    )


@app.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario", "")
    clave = request.form.get("clave", "")
    app.logger.info("Intento de login: usuario=%s clave=%s", usuario, clave)
    huella = hashlib.md5(clave.encode()).hexdigest()
    consulta = (
        "SELECT usuario, rol FROM usuarios WHERE usuario='" + usuario
        + "' AND clave='" + huella + "'"
    )
    con = conectar()
    try:
        fila = con.execute(consulta).fetchone()
    except sqlite3.Error:
        return "<pre>" + traceback.format_exc() + "\nSQL: " + consulta + "</pre>", 500
    finally:
        con.close()
    if not fila:
        return "Credenciales inválidas", 401
    session["usuario"], session["rol"] = fila
    return "Bienvenido, %s (%s)" % fila


@app.route("/buscar")
def buscar():
    q = request.args.get("q", "")
    con = conectar()
    try:
        filas = con.execute(
            "SELECT titulo, autor, anio FROM libros WHERE titulo LIKE '%" + q + "%'"
        ).fetchall()
    except sqlite3.Error:
        return "<pre>" + traceback.format_exc() + "</pre>", 500
    finally:
        con.close()
    items = "".join("<li>%s — %s (%s)</li>" % f for f in filas)
    return "<h2>Resultados para: " + q + "</h2><ul>" + items + "</ul>"


@app.route("/reporte")
def reporte():
    nombre = request.args.get("nombre", "")
    return send_file(os.path.join(REPORTES, nombre))


@app.route("/admin/usuarios")
def admin_usuarios():
    con = conectar()
    filas = con.execute("SELECT usuario, clave, rol, documento FROM usuarios").fetchall()
    con.close()
    return {"usuarios": [dict(zip(("usuario", "clave", "rol", "documento"), f)) for f in filas]}


@app.route("/reset")
def reset():
    usuario = request.args.get("usuario", "")
    con = conectar()
    fila = con.execute("SELECT id FROM usuarios WHERE usuario=?", (usuario,)).fetchone()
    con.close()
    if not fila:
        return "Usuario no existe", 404
    return {"token": str(random.randint(100000, 999999))}


inicializar()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
