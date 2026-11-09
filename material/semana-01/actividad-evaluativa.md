# Actividad evaluativa semana 1 — Firma del protocolo de anonimización y confidencialidad

| Campo | Detalle |
| --- | --- |
| Código de la asignatura | Por asignar |
| Fecha | 8 de noviembre de 2026 |
| Versión | 1.0 |
| Tipo de actividad | Tarea (requisito, sin calificación) |
| Nombre de la actividad | Anonimización del caso y firma del protocolo de confidencialidad e integridad académica (individual) |
| Semana | Semana 1, unidad 1 |
| Intentos | Los necesarios hasta cumplir el requisito |
| Tiempo de dedicación del estudiante | 2 horas |
| Instrucciones para el desarrollo y montaje | Montar en plataforma una actividad tipo tarea. Configuración: tipo de entrega individual; archivos admitidos: un ZIP con el caso anonimizado y un PDF con el protocolo firmado; calificación: sin nota, con retroalimentación del docente; finalización: requisito que se marca como cumplido cuando el docente verifica los criterios de la tabla final. |

## Anonimización del caso y firma del protocolo de confidencialidad e integridad académica

### Objetivo de la actividad

Anonimizar un software de autoría propia aplicando una lista de verificación y un script de revisión, y formalizar el compromiso de confidencialidad e integridad académica mediante la firma del protocolo, para contar con un caso seguro de compartir sobre el cual se analizarán vulnerabilidades y se propondrán correcciones en las semanas siguientes.

### Contexto

Todo el curso trabaja sobre un mismo software de autoría propia, denominado «el caso». Un código real puede contener nombres, direcciones, datos personales o credenciales que no deben salir de la organización de origen. Por ello, el caso se anonimiza antes de compartirse y se firma un protocolo que fija las reglas de confidencialidad, uso de herramientas de inteligencia artificial y prácticas de laboratorio. Esta actividad no se califica, pero es requisito: sin el protocolo firmado y el caso anonimizado no se comparte el caso con el curso.

### Instrucciones

Para desarrollar esta actividad, se recomienda seguir los siguientes pasos:

1. Leer completa la cartilla de la semana 1, en especial las secciones sobre criterios para elegir el caso, reglas éticas de laboratorio, anonimización y formato del protocolo.
2. Elegir el caso con los criterios de la cartilla y diligenciar la ficha del caso.
3. Redactar una justificación de entre 100 y 150 palabras que explique por qué el caso cumple los criterios de elección y qué entradas externas procesa.
4. Trabajar sobre una copia del software y completar la lista de verificación de anonimización de la cartilla.
5. Ejecutar el script de revisión (`scripts/revisar_anonimizacion.py`), indicando como nombres propios los de la persona autora, la organización y el proyecto. Corregir y repetir la ejecución hasta obtener la línea «Hallazgos: 0», y guardar la salida final en un archivo de texto.
6. Revisar manualmente el caso, porque el script no interpreta el contexto y puede dejar pasar datos disfrazados.
7. Comprobar que el programa sigue funcionando con sus pruebas después de anonimizarlo.
8. Leer completo el texto del protocolo, completar la tabla con nombre, documento, programa y fecha, y firmarlo.
9. Subir los archivos en el plazo establecido en el aula virtual.
10. Revisar la tabla de criterios antes de la entrega, para asegurar que el trabajo cumple con cada uno.

**Productos que se entregan**

| Producto | Formato | Contenido |
| --- | --- | --- |
| Caso anonimizado | ZIP | Código anonimizado, sin historial de control de versiones |
| Ficha y justificación del caso | PDF | Ficha de la cartilla completa y justificación de 100 a 150 palabras |
| Informe del script | TXT | Salida final de la revisión, con «Hallazgos: 0» |
| Protocolo firmado | PDF | Texto del protocolo con la tabla de identificación y la firma |

Los productos de las demás actividades de la semana (matriz de requisitos, mapa del ciclo de vida de desarrollo seguro y tabla de hallazgos del laboratorio) no se entregan en esta actividad. Se conservan porque son la base del análisis de código de las semanas 2 y 3.

### Criterios de verificación

La actividad no se califica, por lo que no se aplica una rúbrica de cuatro niveles. El docente verifica cinco criterios con dos resultados posibles: cumple o aún no cumple. El requisito se marca como completado cuando los cinco criterios cumplen.

| Criterio | Cumple | Aún no cumple |
| --- | --- | --- |
| 1. Selección del caso y ficha | El caso cumple los cinco criterios de elección de la cartilla (autoría o autorización escrita, entre 200 y 1000 líneas aproximadamente, al menos una entrada externa, lenguaje preferido, funcionamiento sin información reservada) y la ficha tiene sus seis elementos diligenciados. | El caso incumple al menos un criterio de elección o la ficha tiene al menos un elemento sin diligenciar. |
| 2. Anonimización verificada | Las siete verificaciones de la lista están completadas; el informe del script termina en «Hallazgos: 0»; el ZIP no contiene historial de control de versiones; la revisión manual del docente no encuentra nombres, direcciones IP, credenciales ni datos personales reales. | Falta al menos una de las siete verificaciones, el informe registra uno o más hallazgos, el ZIP incluye historial de control de versiones o el docente identifica al menos un dato reservado. |
| 3. Protocolo firmado | El PDF contiene las siete cláusulas, la tabla con nombre, documento, programa y fecha completos, y la firma. Si el caso no es de autoría propia, se adjunta la autorización escrita. | Falta alguna cláusula, algún campo de la tabla o la firma, o el caso no es de autoría propia y no se adjunta autorización. |
| 4. Redacción y presentación | Los archivos se entregan en los formatos indicados (ZIP, PDF y TXT) y la justificación tiene entre 100 y 150 palabras, con ortografía y puntuación que no alteran el sentido. | Falta un archivo, se entrega en un formato distinto o la justificación queda fuera del rango de palabras o contiene errores que alteran el sentido. |
| 5. Argumentación propia | La justificación explica por qué el caso cumple los criterios de elección, nombra al menos dos entradas externas del programa y anticipa al menos un riesgo de seguridad que se analizará en las semanas 2 y 3. | La justificación no explica el cumplimiento de los criterios, nombra menos de dos entradas externas o no anticipa ningún riesgo. |

### Cierre

Si uno o más criterios aparecen como «Aún no cumple», el docente devuelve la tarea con retroalimentación sobre cada uno y se habilita un nuevo intento dentro del plazo del aula. Esta actividad constituye una oportunidad para preparar el caso con el que se desarrollarán las actividades calificadas de la asignatura, a partir de la semana 3.
