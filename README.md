# Caso del curso: Biblioteca de la Facultad

Repositorio del curso virtual **Fundamentos de programación segura y criptografía básica** (Universidad del Rosario). Contiene el software que se analiza, se corrige y se protege durante las siete semanas, junto con el material de cada semana.

> **Acceso.** Repositorio privado: se accede por invitación del docente, con permisos de solo lectura para el estudiantado.

> **Advertencia.** El programa es **vulnerable a propósito**. Solo se ejecuta en el equipo local (`127.0.0.1`). No se publica en internet ni se reutiliza su código en sistemas reales. Todos los datos son sintéticos.

## Qué contiene

| Carpeta o archivo | Contenido |
| --- | --- |
| `app/` | Aplicación web mínima en Flask y SQLite (login, búsqueda, reportes, administración, restablecimiento de clave, sincronización del catálogo) |
| `tests/` | Pruebas funcionales (deben pasar siempre) y pruebas de seguridad (fallan en la versión original) |
| `scripts/revisar_anonimizacion.py` | Script de revisión de anonimización de la semana 1 |
| `material/` | Cartilla, actividad evaluativa y guía de cada semana |
| `docs/` | Guía del estudiante, recorrido del caso por semana y laboratorio guiado |
| `.github/workflows/ci.yml` | Pipeline de ejemplo para las semanas 6 y 7 (pruebas, SAST y SCA) |
| `requirements-legacy.txt` | Versiones antiguas para el ejercicio de análisis de dependencias (SCA) |

## Cómo ejecutarlo

La explicación detallada, comando por comando, está en la [guía del estudiante](docs/guia-del-estudiante.md). Resumen:

```bash
python3 -m venv .venv
source .venv/bin/activate          # En Windows: .venv\Scripts\activate
pip install -r requirements.txt -r requirements-dev.txt
python app/app.py                  # Escucha en http://127.0.0.1:8000
```

Pruebas:

```bash
pytest -m "not seguridad"   # Funcionales: deben pasar antes y después de corregir
pytest -m seguridad         # Seguridad: 11 fallan en la versión original
```

La base de datos `app/biblioteca.db` se crea sola al iniciar, con tres usuarios y cuatro libros sintéticos. Para reiniciarla se borra el archivo.

## Recorrido por la asignatura

| Semana | Qué se hace con el caso |
| --- | --- |
| 1 | Elegir el caso propio, anonimizarlo y firmar el protocolo (este repositorio es el caso de ejemplo y el entorno que provee el docente) |
| 2 | Clasificar los hallazgos con OWASP Top 10 y CWE |
| 3 | Corregir las vulnerabilidades. Entrega 1 |
| 4 | Identificar qué datos requieren protección criptográfica |
| 5 | Contraseñas, cifrado en tránsito y en reposo, claves. Entrega 2 |
| 6 | Pruebas, pipeline y documentación técnica. Entrega 3 |
| 7 | SAST y SCA en el pipeline (laboratorio formativo) |

Detalle en [`docs/recorrido-por-semana.md`](docs/recorrido-por-semana.md).

## Reglas de laboratorio

1. Solo se ataca este caso en local o el entorno que provea el docente.
2. No se prueban ataques contra sistemas de terceros ni de la propia organización sin autorización escrita.
3. Si se encuentra una vulnerabilidad en software ajeno, se confirma lo mínimo y se reporta al responsable.
4. Se registra qué se probó, cuándo y dónde.

El texto completo del protocolo está en `material/semana-01/cartilla.md`.

## Ramas

- `main`: versión original, con las vulnerabilidades.
- `solucion-docente`: versión corregida de referencia (16 pruebas en verde) y clave de hallazgos en `docs/hallazgos-conocidos-docente.md`. **No se comparte con el estudiantado.**
