# Cartilla semana 1 — Caso de software propio y protocolo de anonimización

| Campo | Detalle |
| --- | --- |
| Asignatura | Fundamentos de programación segura y criptografía básica |
| Fecha | 8 de noviembre de 2026 |
| Versión | 1.0 |
| Unidad y semana | Unidad 1, semana 1: Ingeniería del software seguro y modelado de amenazas |
| Tipo de recurso | Cartilla (material de autoría propia): guía del caso y formato del protocolo de anonimización |
| Resultado de aprendizaje | RAE 2. Analizar código fuente identificando vulnerabilidades de las taxonomías reconocidas (OWASP Top 10, CWE) y proponiendo correcciones conforme a prácticas de codificación segura. |

## Introducción

En esta asignatura, el análisis de vulnerabilidades, su corrección y la implementación de controles criptográficos se realizan sobre un mismo software de autoría propia, denominado «el caso». Trabajar sobre un único código permite que cada semana se apoye en la anterior: lo que se clasifica en la semana 2 se corrige en la semana 3, se protege con criptografía en la semana 5 y se verifica en la semana 6.

Un software propio también implica riesgos. Puede contener información reservada de una organización, datos personales o credenciales. Por esta razón, antes de compartirlo con el curso se anonimiza y se firma un protocolo de confidencialidad e integridad académica. Los requisitos legales y regulatorios forman parte de lo que se documenta en cualquier proyecto de software (Fishpool, 2020), y el marco normativo colombiano se estudia en la semana 7.

Esta cartilla orienta cinco decisiones: cómo se elige el caso, cómo se usa a lo largo de la asignatura, qué reglas rigen las prácticas de laboratorio, cómo se anonimiza y cuál es el texto del protocolo que se firma.

## Desarrollo

### El caso y su recorrido por la asignatura

El caso es un programa de autoría propia que acompaña todo el curso. La tabla resume qué se hace con él cada semana y qué producto se genera, según la organización final de la asignatura.

| Semana | Uso del caso | Actividad evaluativa |
| --- | --- | --- |
| 1 | Selección, anonimización y firma del protocolo | Firma del protocolo (requisito, sin calificación) |
| 2 | Clasificación de hallazgos con OWASP y CWE | Foro de crítica metodológica 2 (formativa) |
| 3 | Análisis de vulnerabilidades y correcciones | Entrega 1 (30 %) |
| 4 | Identificación de los datos del caso que requieren protección | Cuestionario formativo (sin calificación) |
| 5 | Implementación de controles criptográficos | Entrega 2 (35 %) |
| 6 | Integración de controles en el ciclo de vida: pipeline, pruebas y documentación | Entrega 3 (35 %) |
| 7 | Incorporación de SAST y SCA al pipeline del caso | Laboratorio formativo (sin calificación) |

### Criterios para elegir el caso

El caso se elige con estos criterios, que se pueden ajustar con autorización del docente:

- Es de autoría propia o se cuenta con autorización escrita para usarlo en el curso.
- Es lo bastante pequeño para leerse completo en pocas horas, por ejemplo entre 200 y 1000 líneas.
- Recibe entradas externas (formularios, archivos, consultas), porque allí se concentran las vulnerabilidades que se analizan en las semanas 2 y 3.
- Preferiblemente está escrito en Python o SQL, como los laboratorios de la asignatura.
- Puede despojarse de información reservada sin dejar de funcionar.

Una aplicación vulnerable tiene consecuencias para la protección de datos, como las que prevé el Reglamento General de Protección de Datos de la Unión Europea (GDPR) (Fishpool, 2020). Por esta razón, la elección del caso se registra en la siguiente ficha, que se conserva durante toda la asignatura.

| Elemento de la ficha | Qué se registra |
| --- | --- |
| Nombre en clave del caso | Un nombre que no revele la organización ni el proyecto |
| Lenguaje y tamaño | Lenguaje principal y número aproximado de líneas |
| Entradas externas | Formularios, archivos, parámetros, consultas a bases de datos o API |
| Datos que maneja | Tipos de datos (por ejemplo, contraseñas, datos de contacto), siempre sintéticos |
| Dependencias | Bibliotecas y versiones que usa |
| Autorización | Autoría propia o autorización escrita de quien la otorga |

### Reglas éticas de laboratorio

Desde la semana 2 se reproducen ataques controlados, como la inyección SQL del laboratorio. Antes de hacerlo se fijan cuatro reglas, que forman parte del protocolo:

1. Solo se ataca el caso anonimizado o el entorno que provea el docente.
2. No se prueban ataques contra sistemas de terceros ni de la propia organización sin autorización escrita que fije alcance y fechas.
3. Si se encuentra una vulnerabilidad en software ajeno, no se explota más de lo necesario para confirmarla y se reporta a su responsable (divulgación responsable).
4. Se registra qué se probó, cuándo y dónde.

El marco penal colombiano, incluida la Ley 1273 de 2009, se estudia en la semana 7. Mientras tanto, las cuatro reglas anteriores son el criterio de actuación. La tabla aplica las reglas a tres situaciones.

| Situación | Decisión | Regla aplicada |
| --- | --- | --- |
| Se prueba una inyección SQL en el laboratorio de la asignatura | Permitido | Regla 1: es el entorno que provee el docente |
| Se prueba la misma inyección contra el sitio web de la propia empresa para ver si es vulnerable | No permitido sin autorización escrita | Regla 2: falta autorización con alcance y fechas |
| Se encuentra una falla en la aplicación de un proveedor durante su uso normal | Se confirma lo mínimo necesario y se reporta al proveedor | Regla 3: divulgación responsable |

### Anonimización del caso

Anonimizar es retirar del código todo lo que permita identificar a una persona, una organización o un sistema real, sin alterar el comportamiento del programa. La lista de verificación se completa sobre la copia que se entrega, nunca sobre el original.

- [ ] Retirar nombres de personas, empresas, instituciones y proyectos de comentarios, variables, rutas y textos.
- [ ] Cambiar dominios, URL internas, direcciones IP y nombres de servidores por valores de ejemplo.
- [ ] Eliminar credenciales, llaves, tokens y cadenas de conexión. Las credenciales incrustadas en el código se cuentan entre los problemas que conviene detectar pronto (Fishpool, 2020).
- [ ] Sustituir los datos reales por datos sintéticos.
- [ ] Entregar una copia sin historial de control de versiones, porque el historial conserva lo que se borró.
- [ ] Ejecutar el script de revisión (`scripts/revisar_anonimizacion.py`) y corregir hasta obtener cero hallazgos.
- [ ] Comprobar que el programa sigue funcionando con sus pruebas, que en un ciclo seguro se ejecutan con cada cambio (Fishpool, 2020).

El script busca correos, direcciones IP, URL, credenciales, cadenas largas que parecen llaves y los nombres propios que se le indiquen. Se ejecuta así:

```bash
python3 scripts/revisar_anonimizacion.py carpeta_del_caso NombreEmpresa Apellido
```

El script no interpreta el contexto: puede dejar pasar un dato disfrazado o marcar texto inofensivo. La revisión final es responsabilidad de quien entrega el caso.

### Formato del protocolo de confidencialidad e integridad académica

El siguiente texto es la base del protocolo. Si la Universidad cuenta con un texto institucional, este se reemplaza en los puntos que se contradigan. Al firmar, se declara que:

1. El software presentado es de autoría propia o se cuenta con autorización escrita para usarlo en este curso.
2. El software fue anonimizado con la lista de verificación de esta cartilla y no contiene información reservada, datos personales reales ni credenciales vigentes.
3. No se divulgará fuera del curso el código ni los hallazgos de otras personas del grupo.
4. Si se encuentra una vulnerabilidad en el caso de otra persona, se comunicará solo a esa persona y al docente.
5. Se declarará dónde y para qué se usaron herramientas de inteligencia artificial en el desarrollo del caso y de los entregables.
6. No se alterarán evidencias (salidas, capturas, registros) ni se presentará trabajo ajeno como propio. Las prácticas de ataque se limitarán al caso anonimizado o al entorno que provea el docente, según las reglas de laboratorio de esta cartilla.
7. Se acepta que un incumplimiento se trate según el reglamento académico de la Universidad [citar el artículo vigente].

Sobre la cláusula 5: el código generado con inteligencia artificial puede estar sujeto a las mismas leyes de propiedad intelectual que el escrito por una persona, y su titularidad debe determinarse (Omoyeni, 2023). Declarar su uso protege la integridad académica de quien entrega.

| Nombre completo | Documento | Programa | Fecha | Firma |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Conclusión

El caso conecta las siete semanas de la asignatura: se elige con criterios verificables, se anonimiza con una lista de control y un script, y se trabaja bajo cuatro reglas de laboratorio y un protocolo firmado. Sin ese protocolo, el caso no se comparte con el curso. Los productos de las demás actividades de la semana (matriz de requisitos, mapa del ciclo de vida de desarrollo seguro y tabla de hallazgos del laboratorio) se conservan, porque son la base del análisis de código de las semanas 2 y 3.

## Referencias

Fishpool, B. (2020). *Software development in practice*. BCS, The Chartered Institute for IT.

Omoyeni, T. (2023). *Generative AI tools for developers: A practical guide*. SitePoint.
