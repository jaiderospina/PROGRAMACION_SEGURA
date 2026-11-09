import re, sys, pathlib

PATRONES = {
    "correo": r"[\w.+-]+@[\w-]+\.[\w.-]+",
    "ip": r"\b\d{1,3}(?:\.\d{1,3}){3}\b",
    "url": r"https?://[^\s\"')]+",
    "credencial": r"(?i)(password|passwd|clave|secret|token|api[_-]?key)\s*[:=]\s*['\"][^'\"]+['\"]",
    "cadena_larga": r"\b[A-Za-z0-9+/_-]{32,}\b",
}

def revisar(carpeta, nombres_propios):
    patrones = dict(PATRONES)
    for n in nombres_propios:
        patrones["nombre:" + n] = r"(?i)\b" + re.escape(n) + r"\b"
    total = 0
    for ruta in pathlib.Path(carpeta).rglob("*"):
        if ruta.is_file() and ruta.suffix in {".py", ".js", ".java", ".cs", ".php", ".sql", ".md", ".txt", ".json", ".yml", ".yaml", ".env", ".ini", ".cfg"}:
            for i, linea in enumerate(ruta.read_text(errors="ignore").splitlines(), 1):
                for tipo, pat in patrones.items():
                    if re.search(pat, linea):
                        total += 1
                        print(f"{ruta}:{i}: [{tipo}] {linea.strip()[:80]}")
    print(f"\nHallazgos: {total}")

if __name__ == "__main__":
    revisar(sys.argv[1], sys.argv[2:])
