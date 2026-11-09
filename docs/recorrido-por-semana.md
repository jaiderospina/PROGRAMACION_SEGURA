# Recorrido del caso por semana

Organización final de la asignatura. Las actividades calificadas pesan 30 %, 35 % y 35 %.

| Semana | Tema | Trabajo sobre este repositorio | Actividad evaluativa |
| --- | --- | --- | --- |
| 1 | Ingeniería del software seguro y modelado de amenazas | Leer `app/` completo; elaborar la matriz de requisitos y un modelo de amenazas básico; ejecutar `scripts/revisar_anonimizacion.py` sobre el propio caso | Firma del protocolo (requisito, sin calificación) |
| 2 | Taxonomía de vulnerabilidades | Reproducir los ataques del laboratorio (`docs/laboratorio-guiado.md`) y clasificar cada hallazgo con OWASP y CWE | Foro de crítica metodológica 2 (formativa) |
| 3 | Codificación segura y diseño defensivo | Corregir con consultas parametrizadas, escape de salida, validación de rutas y control de acceso; revisar dependencias | Entrega 1 (30 %) |
| 4 | Fundamentos de criptografía | Identificar qué datos del caso requieren qué mecanismo | Cuestionario formativo |
| 5 | Criptografía aplicada | Almacenar contraseñas con salado y función lenta; validar certificados en `catalogo.py`; generar tokens con CSPRNG; cifrar el campo `documento` | Entrega 2 (35 %) |
| 6 | Verificación y pruebas de seguridad | Ejecutar `pytest -m seguridad`, bandit y pip-audit; configurar el pipeline | Entrega 3 (35 %) |
| 7 | Marco normativo, ética y comunicación | Documentar decisiones técnicas; laboratorio de SAST y SCA | Laboratorio formativo |

El criterio de avance es objetivo: cada prueba de `tests/test_seguridad.py` que pasa a verde corresponde a una corrección lograda.
