"""Sincronización del catálogo con un servicio externo (semana 5: cifrado en tránsito)."""
import json
import ssl
import urllib.request

CATALOGO_URL = "https://catalogo.ejemplo.test/libros.json"


def sincronizar_catalogo(url=CATALOGO_URL):
    contexto = ssl._create_unverified_context()
    with urllib.request.urlopen(url, context=contexto, timeout=10) as r:
        return json.loads(r.read().decode())
