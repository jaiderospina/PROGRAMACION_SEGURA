# Caso del curso: Biblioteca de la Facultad

Repositorio del curso virtual **Fundamentos de programaciÃ³n segura y criptografÃ­a bÃ¡sica** (Universidad del Rosario). Contiene el software que se analiza, se corrige y se protege durante las siete semanas, junto con el material de cada semana.

> **Advertencia.** El programa es **vulnerable a propÃ³sito**. Solo se ejecuta en el equipo local (`127.0.0.1`). No se publica en internet ni se reutiliza su cÃ³digo en sistemas reales. Todos los datos son sintÃ©ticos.

## QuÃ© contiene

| Carpeta o archivo | Contenido |
| --- | --- |
| `app/` | AplicaciÃ³n web mÃ­nima en Flask y SQLite (login, bÃºsqueda, reportes, administraciÃ³n, restablecimiento de clave, sincronizaciÃ³n del catÃ¡logo) |
| `tests/` | Pruebas funcionales (deben pasar siempre) y pruebas de seguridad (fallan en la versiÃ³n original) |
| `scripts/revisar_anonimizacion.py` | Script de revisiÃ³n de anonimizaciÃ³n de la semana 1 |
| `material/` | Cartilla, actividad evaluativa y guÃ­a de cada semana |
| `docs/` | Recorrido del caso por semana y laboratorio guiado |
| `.github/workflows/ci.yml` | Pipeline de ejemplo para las semanas 6 y 7 (pruebas, SAST y SCA) |
| `requirements-legacy.txt` | Versiones antiguas para el ejercicio de anÃ¡lisis de dependencias (SCA) |

## CÃ³mo ejecutarlo

```bash
python3 -m venv .venv
source .venv/bin/activate          # En Windows: .venv\Scripts\activate
pip install -r requirements.txt -r requirements-dev.txt
python3 app/app.py                 # Escucha en http://127.0.0.1:8000
```

Pruebas:

```bash
pytest -m "not seguridad"   # Funcionales: deben pasar antes y despuÃ©s de corregir
pytest -m seguridad         # Seguridad: 11 fallan en la versiÃ³n original
```

La base de datos `app/biblioteca.db` se crea sola al iniciar, con tres usuarios y cuatro libros sintÃ©ticos. Para reiniciarla se borra el archivo.

## Recorrido por la asignatura

| Semana | QuÃ© se hace con el caso |
| --- | --- |
| 1 | Elegir el caso propio, anonimizarlo y firmar el protocolo (este repositorio es el caso de ejemplo y el entorno que provee el docente) |
| 2 | Clasificar los hallazgos con OWASP Top 10 y CWE |
| 3 | Corregir las vulnerabilidades. Entrega 1 |
| 4 | Identificar quÃ© datos requieren protecciÃ³n criptogrÃ¡fica |
| 5 | ContraseÃ±as, cifrado en trÃ¡nsito y en reposo, claves. Entrega 2 |
| 6 | Pruebas, pipeline y documentaciÃ³n tÃ©cnica. Entrega 3 |
| 7 | SAST y SCA en el pipeline (laboratorio formativo) |

Detalle en [`docs/recorrido-por-semana.md`](docs/recorrido-por-semana.md).

## Reglas de laboratorio

1. Solo se ataca este caso en local o el entorno que provea el docente.
2. No se prueban ataques contra sistemas de terceros ni de la propia organizaciÃ³n sin autorizaciÃ³n escrita.
3. Si se encuentra una vulnerabilidad en software ajeno, se confirma lo mÃ­nimo y se reporta al responsable.
4. Se registra quÃ© se probÃ³, cuÃ¡ndo y dÃ³nde.

El texto completo del protocolo estÃ¡ en `material/semana-01/cartilla.md`.

## Ramas

- `main`: versiÃ³n original, con las vulnerabilidades.
- `solucion-docente`: versiÃ³n corregida de referencia (16 pruebas en verde) y clave de hallazgos en `docs/hallazgos-conocidos-docente.md`. **No se comparte con el estudiantado.**
