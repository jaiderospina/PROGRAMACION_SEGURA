# Guía de la semana 1

Oct 31, 2026 · @Jaider Ospina Navas

Material de estudio autónomo de 9 horas para la Semana 1, con citas de página de la carpeta BIBLIOGRAFIA\_ROSARIO y de la documentación en línea de OWASP.

## Ficha de la semana y supuestos

Esta semana te lleva de ver la seguridad como un conjunto de controles de gestión a escribirla como requisitos de software que se pueden verificar en el código. Trabajas unas 9 horas (punto medio del rango de 8 a 10) y cierras con un requisito sin calificación: firmar el protocolo de anonimización y confidencialidad.

|  Elemento | Detalle |
| --- | --- |
| Semana | 1. La programación segura como problema de ingeniería |
| RAE asociado | RAE 2. Analizar código fuente identificando vulnerabilidades de las taxonomías reconocidas (OWASP Top 10, CWE) y proponiendo correcciones conforme a prácticas de codificación segura |
| Dedicación | 9 horas de trabajo autónomo (ver la ruta de trabajo) |
| Evaluación | Firma del protocolo de anonimización y confidencialidad (requisito, sin calificación) |
| Fuentes permitidas | Libros de la carpeta BIBLIOGRAFIA\_ROSARIO y documentación en línea de OWASP, nada más |

## Ruta de trabajo (9 horas)

Sigue los bloques en orden: cada uno deja un producto que usas en el siguiente. Si te sobra tiempo, amplía el laboratorio (bloque 6), que es el que más transfiere a las semanas siguientes.

| Bloque | Tiempo | Qué haces | Producto | Fuente principal |
| --- | --- | --- | --- | --- |
| 1. Orientación | 0 h 30 min | Lees la ficha, los objetivos y el protocolo de la semana | Lista de dudas | Esta guía |
| 2. Tema 1, presentación narrada | 1 h 30 min | Ves/lees la presentación y las lecturas de apoyo | Notas en tus palabras | Fishpool pp. 165–166, 318–319, 340; Sistemas seguros p. 27 y p. 58; OWASP A06:2025 |
| 3. Tema 1, ejercicio | 1 h 30 min | Conviertes cuatro riesgos en requisitos de software verificables | Matriz riesgo → control → requisito → prueba | Fishpool p. 165–166; OWASP Threat Modeling Cheat Sheet |
| 4. Tema 2, lectura | 1 h 30 min | Estudias el Secure SDLC, los principios de diseño y ASVS | Resumen de una página | Fishpool pp. 75–78, 343–345; OWASP Secure Product Design, ASVS, SAMM |
| 5. Tema 2, ejercicio | 1 h | Ubicas actividades de seguridad en cada fase de tu propio ciclo | Mapa de Secure SDLC de tu caso | OWASP SAMM, Proactive Controls 2024 |
| 6. Laboratorio | 1 h 30 min | Lees código vulnerable, lo clasificas con Top 10 y CWE y lo corriges | Tabla de hallazgos y código corregido | Fishpool pp. 224–225, 341–343; OWASP Top 10:2025 |
| 7. Tema 3, cartilla | 1 h | Lees la cartilla, eliges tu caso y lo anonimizas | Caso anonimizado | Cartilla (texto base en esta guía) |
| 8. Cierre | 0 h 30 min | Firmas el protocolo y haces la autoevaluación | Protocolo firmado | Esta guía |

Total: 9 horas. El nuevo módulo de marco ético y legal (sección 1.8, 30 minutos) sale de los bloques 4 y 5, con 15 minutos de cada uno.

## Objetivos de aprendizaje

Al terminar la semana puedes:

1. Explicar por qué la seguridad de una aplicación se decide desde los requisitos y el diseño, y no solo al escribir código.
2. Convertir un riesgo y su control en un requisito de software que se pueda probar.
3. Ubicar una actividad de seguridad en cada fase del ciclo de vida de desarrollo (Secure SDLC).
4. Reconocer cuándo un fragmento de código viola un principio de diseño seguro de OWASP.
5. Clasificar una vulnerabilidad en OWASP Top 10:2025 y en CWE, y proponer una corrección verificable (primer paso del RAE 2).
6. Preparar un caso de software propio con el protocolo de anonimización y confidencialidad, y aplicar las reglas éticas y legales mínimas antes de practicar ataques de laboratorio.

## Tema 1. De la gestión del riesgo al código: de los controles a los requisitos de software

Un control de seguridad solo protege al software cuando se escribe como un requisito que alguien puede probar. Este tema te da la cadena riesgo → control → requisito → prueba y te hace practicarla.

### 1.1 Por qué es un problema de ingeniería

- **El código es un punto de entrada.** Fishpool explica que las aplicaciones son «soft targets» porque pueden estar mal programadas o usar componentes comprometidos, y que el atacante las usa como entrada para escalar privilegios en la infraestructura (Fishpool, 2020, p. 318).
- **Una brecha suele nacer en la programación.** El libro llama AppSec a la seguridad de aplicaciones y dice que su debilidad es una de las causas raíz de las brechas de datos. Sus metas son identificar amenazas, proteger datos críticos, corregir vulnerabilidades existentes y evitar nuevos exploits (Fishpool, 2020, p. 340).
- **Un buen algoritmo mal programado deja de ser seguro.** La seguridad de un algoritmo criptográfico depende de cómo esté programado; un error de programación o de configuración hace que la seguridad real sea menor que la teórica. Para nombrar esos errores de forma única existen listas como CVE, mantenida por MITRE (González Manzano y De Fuentes, 2014, p. 58 del PDF; impresa 53).
- **El diseño no se arregla con buen código.** OWASP lo resume en A06:2025 Insecure Design: un diseño inseguro no se corrige con una implementación perfecta (OWASP, 2025a, A06).

### 1.2 Qué es un requisito de seguridad

Fishpool pide documentar el propósito del proyecto con, entre otros, requisitos legales y regulatorios, administración (por ejemplo, acceso de usuarios) y auditoría (Fishpool, 2020, p. 165). También dice que todo proyecto tiene requisitos no funcionales y la lista empieza por la seguridad, seguida de integridad de datos, interoperabilidad, escalabilidad, rendimiento y fiabilidad (pp. 165–166). Su ventaja: conocerlos desde el inicio permite medir después si el proyecto los cumplió (p. 166).

Para que un requisito sirva a quien programa y a quien prueba, escríbelo en cuatro pasos:

| Paso | Pregunta | Ejemplo (portal de facturas) |
| --- | --- | --- |
| Riesgo | ¿Qué puede salir mal y cuánto importa? | Un cliente lee las facturas de otro |
| Control | ¿Qué decide la organización para reducirlo? | Cada cliente consulta solo sus propias facturas |
| Requisito | ¿Qué debe hacer el software, en una frase comprobable? | «El sistema entrega una factura solo si el cliente de la sesión autenticada es el titular de esa factura» |
| Prueba | ¿Cómo demuestro que se cumple? | Caso de abuso: el cliente A pide la factura del cliente B y el sistema la niega |

La columna de ejemplo es de elaboración propia; el escenario viene del libro, como ves a continuación.

### 1.3 Ejemplo trabajado con el libro

González Manzano y De Fuentes (2014, p. 27 del PDF; impresa 22) plantean a quien gestiona un portal de luz y gas definir los servicios de seguridad de tres funciones. Su solución: integridad, confidencialidad y autenticación (del cliente y del servidor) en las tres; no repudio en emisión para las facturas; y no repudio en recepción más sellado de tiempo para el buzón de reclamaciones. Para el sellado el libro advierte que hace falta una fuente de tiempo fiable y cita como ejemplo el Real Instituto y Observatorio de la Armada.

El paso que falta es convertir esos servicios en requisitos:

| Función | Servicios (según el libro) | Requisito de software (elaboración propia) |
| --- | --- | --- |
| Zona personal del cliente | Integridad, confidencialidad, autenticación de cliente y servidor | La sesión solo se crea tras validar las credenciales y viajan por un canal en el que el cliente puede verificar la identidad del servidor |
| Consulta de facturas | Los anteriores + no repudio en emisión | Cada factura mostrada incluye una evidencia verificable de que la emitió el proveedor |
| Buzón de reclamaciones | Los anteriores + no repudio en recepción + sellado de tiempo | Cada reclamación recibida genera un acuse con fecha y hora tomadas de una fuente de tiempo fiable |

### 1.4 El modelado de amenazas como puente

El Threat Modeling Cheat Sheet de OWASP propone seis pasos: preparación (activos, agentes de amenaza, superficie de ataque, probabilidad, impacto, controles, más objetivos de negocio y requisitos de seguridad y cumplimiento); identificar el diseño de la aplicación; descomponer y modelar el sistema con diagramas de flujo de datos y límites de confianza; identificar agentes de amenaza; construir una matriz de trazabilidad que evalúe impacto y probabilidad (menciona DREAD y PASTA); y definir contramedidas con un dueño del riesgo y una estrategia de tratamiento: reducir, transferir, evitar o aceptar (OWASP, s. f.-a).

A06:2025 recomienda aplicar el modelado de amenazas a autenticación, control de acceso, lógica de negocio y flujos clave, y escribir pruebas tanto para casos de uso como de mal uso (OWASP, 2025a, A06). En el modelo de madurez OWASP SAMM v2, la función Diseño agrupa tres prácticas que son justo las de este tema: Threat Assessment, Security Requirements y Secure Architecture (OWASP, s. f.-b).

### 1.5 Cuánto rigor: depende del riesgo

Fishpool distingue sistemas de bajo riesgo, como un control de inventario, de otros donde un error causa daño grave, como el control de trenes o vehículos autónomos. Para los segundos recomienda una metodología muy documentada, con análisis y diseño hechos y riesgos mitigados antes de programar (Fishpool, 2020, p. 104).

### 1.6 Guion de la presentación narrada (material de autoría propia, unos 8 minutos)

| Diapositiva | Mensaje | Idea para narrar (30 a 90 s) | Fuente |
| --- | --- | --- | --- |
| 1 | El código es una puerta de entrada | Las aplicaciones son blancos fáciles cuando están mal programadas o usan componentes comprometidos; desde ahí el atacante escala | Fishpool p. 318 |
| 2 | Diseño inseguro no es lo mismo que un error de código | Un diseño inseguro no se arregla con una implementación perfecta; por eso la seguridad empieza antes de programar | OWASP A06:2025 |
| 3 | Riesgo, control, requisito, prueba | Presenta la tabla de cuatro pasos y por qué la prueba es la que hace verificable el requisito | Fishpool pp. 165–166 |
| 4 | Ejemplo: portal de luz y gas | Muestra los servicios de seguridad por función y cómo se vuelven requisitos | Sistemas seguros p. 27 |
| 5 | Modelar amenazas en seis pasos | Cuéntales el recorrido de la hoja de trucos de OWASP, sin entrar en herramientas | OWASP Threat Modeling Cheat Sheet |
| 6 | Qué haces esta semana | Anuncia el ejercicio de la matriz y el laboratorio con código | Esta guía |

### 1.7 Ejercicio (1 h 30 min): tu matriz de requisitos

Completa una tabla de cuatro columnas (riesgo, control, requisito, prueba) para estos cuatro riesgos. Usa el formato de la sección 1.2.

1. Un usuario accede a datos que pertenecen a otro usuario.
2. Alguien altera datos mientras viajan entre cliente y servidor.
3. La aplicación usa una librería con una vulnerabilidad conocida. Apoyo: Fishpool explica que herramientas de despliegue automático como Jenkins tienen complementos de verificación de dependencias (p. 343) y Sinha enseña a revisar paquetes de Python con *pip-audit* (pp. 566–567).
4. Hay credenciales incrustadas en el código. Apoyo: Fishpool las cita entre los problemas que se detectan antes al mover la seguridad «hacia la izquierda» del proceso (p. 319).

Antes de entregar, revisa cada requisito con esta lista:

- [ ] Dice quién o qué actúa y bajo qué condición.
- [ ] Se puede responder «si» o «no» tras una prueba concreta.
- [ ] No impone una tecnología cuando basta con el comportamiento.
- [ ] La prueba incluye al menos un caso de abuso, no solo el caso normal.

### 1.8 Reglas éticas de laboratorio antes de practicar (30 min)

Desde la semana 2 vas a reproducir ataques como la inyección SQL del laboratorio. Antes de hacerlo fija las reglas. Fishpool incluye los requisitos legales y regulatorios entre lo que debe documentarse en todo proyecto (2020, p. 165) y recuerda que una aplicación vulnerable tiene consecuencias para la protección de datos (p. 318).

**Reglas del laboratorio** (criterio de esta guía, que forma parte del protocolo de la sección 3.3):

1. Solo atacas tu caso anonimizado o el entorno que provea el docente.
2. No pruebas ataques contra sistemas de terceros ni de tu organización sin autorización escrita que fije alcance y fechas.
3. Si encuentras una vulnerabilidad en software ajeno, no la explotas más de lo necesario para confirmarla y la reportas a su responsable (divulgación responsable).
4. Registras qué probaste, cuándo y dónde.

**Lectura breve:** ninguna esta semana. El marco normativo colombiano, incluida la Ley 1273 de 2009, se estudia en la semana 7; aquí solo se aplican las reglas de arriba.

**Mini-ejercicio:** clasifica cada caso como permitido o no permitido y justifica con las reglas de arriba.

- [ ] Pruebas una inyección SQL en el laboratorio de esta guía.
- [ ] Pruebas la misma inyección contra el sitio web de tu empresa «para ver si es vulnerable».
- [ ] Encuentras una falla en una aplicación de un proveedor mientras la usas normalmente.

## Tema 2. Ciclo de vida de desarrollo seguro (Secure SDLC) y principios de diseño seguro OWASP

Un Secure SDLC es el ciclo de vida de siempre con una actividad de seguridad en cada fase, hecha lo antes posible. Este tema te da el mapa de actividades, los principios de diseño y las taxonomías con las que vas a nombrar vulnerabilidades.

### 2.1 El ciclo de vida y mover la seguridad «hacia la izquierda»

- **Punto de partida.** Fishpool advierte que no hay un marco que sirva para todo y propone el SDLC como base razonable (2020, p. 75). Sus fases son: brief, viabilidad, análisis, planificación, diseño, desarrollo, pruebas y despliegue (pp. 75–78); después viene el mantenimiento (p. 81).
- **El enfoque tradicional falla.** Si la seguridad se deja al final de la línea de producción, los defectos ya están «horneados» en el código y cuestan más de aislar y corregir (pp. 343–344).
- **Shift left.** Desde fines de 2016 se habla de mover la seguridad al inicio del proceso. Así las vulnerabilidades se encuentran antes y se resuelven más rápido, a menudo con menos personas, y el autor contrasta pérdidas de millones por una brecha evitable con unos cientos de libras en una prueba temprana (pp. 344–345).
- **DevSecOps.** Como los modelos tradicionales de seguridad no encajan bien con DevOps, nace la idea de «security as code»: la seguridad está presente en toda la tubería y no se reduce a una prueba de penetración previa al lanzamiento (pp. 318–319).
- **Pruebas en la tubería.** Todo cambio debe pasar pruebas unitarias, de integración, de regresión y de usuario antes de desplegarse; el libro avisa de que automatizarlas exige experiencia (p. 345).
- **Revisión entre pares.** La programación en pareja y la revisión formal de código mantienen la retroalimentación lo más cerca posible del momento en que se escribe el código (pp. 196–197).

### 2.2 Mapa de actividades de seguridad por fase

Las fases son las de Fishpool; la asignación de actividades es una síntesis de esta guía a partir de las fuentes de la columna final.

| Fase | Actividad de seguridad | Evidencia que deja | Fuentes |
| --- | --- | --- | --- |
| Análisis | Requisitos de seguridad y cumplimiento; identificar datos sensibles | Lista de requisitos verificables | Fishpool pp. 165–166; SAMM «Security Requirements»; Proactive Controls C4 «Address Security from the Start» |
| Diseño | Modelado de amenazas; aplicar principios de diseño seguro | Diagrama con límites de confianza y matriz de amenazas | Cheat Sheets de OWASP; A06:2025 |
| Desarrollo | Validar entradas, consultas parametrizadas, controlar dependencias | Código que pasa revisión y análisis de dependencias | Fishpool pp. 225, 342–343; Sinha pp. 566–567; C3 y C6 de Proactive Controls |
| Pruebas | Pruebas de abuso, revisión entre pares, escaneo automatizado | Casos de prueba y reporte de hallazgos | Fishpool pp. 197, 345; Omoyeni pp. 42, 44 |
| Despliegue | Configuración segura por defecto; revisar la cadena de suministro | Lista de verificación de despliegue | C5 «Secure By Default Configurations»; Top 10 A02 y A03 |
| Operación y mantenimiento | Registro y alertas; actualizar paquetes | Bitácora y plan de parches | C9 de Proactive Controls; Top 10 A09; Sinha p. 566 |

Sobre el escaneo con IA: Omoyeni muestra herramientas que revisan código en busca de vulnerabilidades como las del Top 10 de OWASP y sugieren correcciones (2023, p. 42), pero advierte que el código generado puede introducir vulnerabilidades y plantear problemas de propiedad intelectual (p. 44). Trata sus resultados como una pista, no como una conclusión.

### 2.3 Principios de diseño seguro

La hoja de trucos *Secure Product Design* de OWASP presenta cuatro principios (OWASP, s. f.-c). La columna «Cómo se ve en el código» es de elaboración propia.

| Principio | Qué dice OWASP | Cómo se ve en el código | Apoyo en los libros |
| --- | --- | --- | --- |
| Mínimo privilegio y separación de funciones | Dar a usuarios y sistemas solo el acceso necesario y repartir tareas para que nadie controle todo un proceso | La cuenta de la aplicación en la base de datos solo puede hacer las operaciones que la aplicación necesita | Principles of Programming p. 69 (impresa 52): cada cuenta recibe el mínimo de derechos; así un atacante con las credenciales de una recepcionista no puede, por ejemplo, cambiar su propio salario. Fishpool p. 342: limitar permisos en operaciones sensibles de la base de datos |
| Defensa en profundidad | Capas de control, de modo que si una falla otras siguen protegiendo el activo | Validar la entrada, parametrizar la consulta y restringir la cuenta, las tres a la vez | Fishpool p. 342 enumera varias técnicas combinables contra inyección |
| Confianza cero | Tratar usuarios, dispositivos y redes como no confiables hasta verificarlos, también dentro de la red de la organización | El servicio interno también autentica y autoriza cada petición | Sin apoyo directo en los libros de la carpeta. Como contraejemplo, Sistemas seguros p. 189 advierte que guardar en caché la información de autenticación del usuario pone en riesgo la seguridad |
| Seguridad en abierto | Quien programa, sobre todo en código abierto, entiende las implicaciones de seguridad de su código y trabaja con especialistas | Revisión por pares y análisis de dependencias antes de integrar | Fishpool pp. 196–197 y 343 |

La Guía del Desarrollador de OWASP añade que un diseño seguro establece valores por defecto seguros, reduce la superficie de ataque y falla de forma bien definida y predecible (OWASP, s. f.-d).

### 2.4 ASVS y su capítulo de arquitectura

El Application Security Verification Standard (ASVS) de OWASP es una lista de requisitos de seguridad verificables. Sirve para que tu requisito de la sección 1.7 use un vocabulario reconocido y para que otra persona pueda comprobarlo.

- **ASVS 4.0, capítulo V1 (el que cita la organización de la asignatura).** Su objetivo es que la seguridad se considere en todas las fases del desarrollo, que se conozcan los roles funcionales y de seguridad de cada componente y que se entienda que probar la aplicación aislada no basta, porque los clientes dependen de servicios remotos (OWASP, 2017, revisión archivada del wiki). En la revisión archivada del wiki aparecen requisitos como identificar todos los componentes y confirmar que son necesarios, aplicar controles de seguridad en los servicios remotos y no solo en el cliente, identificar datos sensibles, producir un modelo de amenazas, centralizar los controles, considerar la seguridad en todo el SDLC, mantener componentes sin vulnerabilidades conocidas y tener una política explícita de gestión de claves (OWASP, 2017).
- **ASVS 5.0.0 (mayo de 2025), la versión vigente.** Reorganizó el estándar: su capítulo 1 ahora es «Encoding and Sanitization» (OWASP, 2025b), y los temas de arquitectura pasaron al capítulo V15 «Secure Coding and Architecture», según el listado de 17 capítulos de la ficha de arc42 (s. f.), una página de terceros que debes contrastar con el estándar oficial.

Qué hacer con esto: en la semana cita el V1 de ASVS 4.0 como pide la tabla del curso y, para trabajo nuevo, busca el requisito equivalente en ASVS 5.0.0. No pude verificar en línea la correspondencia exacta entre ambas versiones ni los números de requisito de 4.0.3; la numeración de arriba corresponde a la revisión archivada y debes confirmarla en el PDF oficial antes de publicar.

### 2.5 OWASP Top 10:2025 y CWE: las taxonomías del RAE 2

El Top 10:2025 tiene diez categorías (OWASP, 2025a). La columna final es un criterio de esta guía sobre dónde se previene mejor cada una.

| Id | Categoría | Fase donde más se previene |
| --- | --- | --- |
| A01 | Broken Access Control | Análisis y diseño |
| A02 | Security Misconfiguration | Despliegue |
| A03 | Software Supply Chain Failures | Desarrollo y despliegue |
| A04 | Cryptographic Failures | Diseño |
| A05 | Injection | Desarrollo |
| A06 | Insecure Design | Análisis y diseño |
| A07 | Authentication Failures | Diseño y desarrollo |
| A08 | Software or Data Integrity Failures | Despliegue |
| A09 | Security Logging and Alerting Failures | Operación |
| A10 | Mishandling of Exceptional Conditions | Desarrollo |

Tres ideas para usar las taxonomías:

- **CWE clasifica el tipo de debilidad.** Cada página del Top 10 lista los CWE que agrupa; A06 reúne 39 y destaca CWE-256 (almacenamiento sin protección de credenciales), CWE-269 (gestión indebida de privilegios), CWE-434 (carga de archivos peligrosos), CWE-501 (violación de límite de confianza) y CWE-522 (credenciales insuficientemente protegidas) (OWASP, 2025a, A06). CVE, en cambio, identifica un fallo concreto y ya descubierto (González Manzano y De Fuentes, 2014, p. 58).
- **Las listas cambian.** Fishpool, escrito con el Top 10 de 2017, dice que la inyección SQL seguía siendo la vulnerabilidad número uno (2020, p. 225). En 2025 la inyección es A05 y el control de acceso, A01. Por eso se cita siempre la edición.
- **Los controles proactivos son el reverso del Top 10.** Los Top 10 Proactive Controls 2024 son: C1 Implement Access Control, C2 Use Cryptography to Protect Data, C3 Validate all Input & Handle Exceptions, C4 Address Security from the Start, C5 Secure By Default Configurations, C6 Keep your Components Secure, C7 Secure Digital Identities, C8 Leverage Browser Security Features, C9 Implement Security Logging and Monitoring y C10 Stop Server Side Request Forgery (OWASP, 2024).

### 2.6 Ejercicio (1 h): el mapa de Secure SDLC de tu caso

Copia la tabla de la sección 2.2 y ajústala al software propio que usarás como caso (Tema 3). Para cada fase escribe:

1. La actividad de seguridad que hoy haces, si existe, o «ninguna».
2. Una actividad que añadirías, con el control de Proactive Controls o la categoría del Top 10 que la justifica.
3. La evidencia que dejaría esa actividad.

Al final, marca la fase donde hoy hay más huecos y explica en dos frases por qué mover allí una actividad ahorraría trabajo (apoya el argumento en Fishpool, 2020, pp. 344–345).

## Laboratorio guiado: leer código vulnerable, clasi&#32;&#32;

## ficarlo y corregirlo (1 h 30 min)

Este laboratorio es tu primer ejercicio del RAE 2. Usa Python 3 y SQLite, sin instalar nada. Guárdalo como `lab.py` y ejecútalo. Yo lo probé y las salidas de abajo son las reales.

```python
import os, sqlite3

BASE = os.path.abspath("reportes")
os.makedirs(BASE, exist_ok=True)
open(os.path.join(BASE, "enero.txt"), "w").write("reporte publico")
open("secreto.txt", "w").write("dato reservado")

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE usuarios (nombre TEXT, clave TEXT, rol TEXT)")
db.executemany("INSERT INTO usuarios VALUES (?,?,?)",
               [("ana", "x1", "admin"), ("luis", "x2", "lector")])

# --- VULNERABLE ---
def login_vulnerable(nombre, clave):
    sql = f"SELECT rol FROM usuarios WHERE nombre = '{nombre}' AND clave = '{clave}'"
    return db.execute(sql).fetchall()

def abrir_vulnerable(nombre_archivo):
    return open(os.path.join(BASE, nombre_archivo)).read()

# --- CORREGIDO ---
def login_seguro(nombre, clave):
    return db.execute("SELECT rol FROM usuarios WHERE nombre = ? AND clave = ?",
                      (nombre, clave)).fetchall()

PERMITIDOS = {"enero.txt"}
def abrir_seguro(nombre_archivo):
    if nombre_archivo not in PERMITIDOS:
        raise PermissionError("archivo no permitido")
    return open(os.path.join(BASE, nombre_archivo)).read()

print("1 vulnerable, entrada normal :", login_vulnerable("luis", "x2"))
print("2 vulnerable, entrada maligna:", login_vulnerable("ana", "' OR '1'='1"))
print("3 seguro, entrada maligna    :", login_seguro("ana", "' OR '1'='1"))
print("4 vulnerable, traversal      :", abrir_vulnerable("../secreto.txt"))
try:
    abrir_seguro("../secreto.txt")
except PermissionError as e:
    print("5 seguro, traversal          : PermissionError ->", e)
print("6 seguro, entrada legitima   :", abrir_seguro("enero.txt"))
```

Salida esperada:

```text
1 vulnerable, entrada normal : [('lector',)]
2 vulnerable, entrada maligna: [('admin',), ('lector',)]
3 seguro, entrada maligna    : []
4 vulnerable, traversal      : dato reservado
5 seguro, traversal          : PermissionError -> archivo no permitido
6 seguro, entrada legitima   : reporte publico
```

### Qué observar

1. **Inyección SQL (línea 2).** La entrada `' OR '1'='1` hace verdadera la condición y la consulta devuelve a todos los usuarios. Fishpool describe este ataque como la modificación de sentencias SQL existentes por entradas sin sanear (2020, p. 225). Su mitigación más común es la consulta parametrizada, que «ata» los valores a una sentencia ya preparada, de modo que un valor malicioso no se ejecuta como código (p. 342). La versión segura (línea 3) usa justo el marcador `?` que el libro muestra en su ejemplo con SQLite (p. 225).
2. **Recorrido de rutas (línea 4).** Con `../secreto.txt` el programa sale del directorio permitido. Fishpool lo describe como modificar la ruta de un archivo para «escapar» de un directorio permitido y propone una regla simple: nunca dejar que el usuario especifique el nombre de un archivo, sino ofrecerle una lista de opciones (p. 343). La función segura aplica esa regla con una lista de nombres permitidos.
3. **Defensa en profundidad.** La corrección es una sola capa. Fishpool añade limitar los permisos de la cuenta que accede a operaciones sensibles de la base de datos (p. 342); eso es mínimo privilegio (sección 2.3).

### Tabla de hallazgos que debes entregar a ti mismo

Llena una fila por cada vulnerabilidad. Las dos primeras ya están resueltas como ejemplo.

| Hallazgo | Función | Categoría Top 10:2025 | CWE | Corrección | Evidencia |
| --- | --- | --- | --- | --- | --- |
| Concatenación de entrada en SQL | `login_vulnerable` | A05 Injection | CWE-89 | Consulta parametrizada | Salida 3: lista vacía |
| Ruta controlada por el usuario | `abrir_vulnerable` | A01 Broken Access Control | CWE-22 | Lista de nombres permitidos | Salida 5: PermissionError |
| (tu hallazgo 3) |  |  |  |  |  |

Para el tercer hallazgo, añade a `lab.py` una contraseña escrita dentro del código, corrígela leyendo el valor desde una variable de entorno y clasifícala. Pista: Fishpool cita las credenciales incrustadas entre los problemas que conviene detectar pronto (2020, p. 319), y A06 destaca CWE-256 y CWE-522 (OWASP, 2025a, A06).

La clasificación de la segunda fila (A01) y los números CWE-89 y CWE-22 son de esta guía; Fishpool cubre la inyección SQL y la ruta de archivos, pero no los numera. Confirma ambos en la página de cada categoría del Top 10:2025 y en el catálogo CWE antes de enseñarlos.

## Tema 3. Caso de software propio y protocolo de anonimización, confidencialidad e integridad académica

Todo el curso trabaja sobre un software que tú escribiste. Para protegerte a ti y a tu organización, lo anonimizas antes de compartirlo y firmas un protocolo. Lo que sigue es el texto base de la cartilla (material de autoría propia); si la Universidad tiene un texto oficial, reemplaza las partes que se contradigan.

### 3.1 Cómo elegir tu caso

Elige un programa que cumpla estos criterios (son criterios de esta guía, ajustables):

- Es de tu autoría o tienes autorización escrita para usarlo en el curso.
- Es lo bastante pequeño para leerlo completo en unas horas, por ejemplo entre 200 y 1000 líneas.
- Recibe entradas externas (formularios, archivos, consultas), que es donde suelen estar las vulnerabilidades.
- Preferiblemente está en Python o SQL, como los laboratorios.
- Puedes quitarle la información reservada sin que deje de funcionar.

Esto importa porque los requisitos legales y regulatorios forman parte del propósito de un proyecto (Fishpool, 2020, p. 165) y porque una aplicación vulnerable tiene consecuencias para la protección de datos, como el GDPR que menciona el libro (p. 318).

### 3.2 Protocolo de anonimización: lista de verificación

- [ ] Retira nombres de personas, empresas, instituciones y proyectos de comentarios, variables, rutas y textos.
- [ ] Cambia dominios, URL internas, direcciones IP y nombres de servidores por valores de ejemplo.
- [ ] Elimina credenciales, llaves, tokens y cadenas de conexión. Fishpool cita las credenciales incrustadas entre los problemas que conviene detectar pronto (2020, p. 319).
- [ ] Sustituye datos reales por datos sintéticos.
- [ ] Entrega una copia sin historial de control de versiones, porque el historial conserva lo que borraste.
- [ ] Ejecuta el script de revisión de abajo y corrige hasta llegar a cero hallazgos.
- [ ] Comprueba que el programa sigue funcionando con tus pruebas, que en un ciclo seguro se ejecutan con cada cambio (Fishpool, 2020, p. 345).

Script de apoyo (`revisar_anonimizacion.py`; lo probé con un caso de ejemplo y detectó nombre, IP, credencial, URL y correo). Se ejecuta así: `python3 revisar_anonimizacion.py carpeta_del_caso NombreEmpresa Apellido`.

```python
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
```

El script no entiende el contexto: puede dejar pasar un dato disfrazado o marcar texto inocente. La revisión final es tuya.

### 3.3 Texto base del protocolo de confidencialidad e integridad académica

Al firmar declaras que:

1. El software presentado es de mi autoría o tengo autorización escrita para usarlo en este curso.
2. Lo anonimicé con la lista de la sección 3.2 y no contiene información reservada, datos personales reales ni credenciales vigentes.
3. No divulgaré fuera del curso el código ni los hallazgos de otras personas del grupo.
4. Si encuentro una vulnerabilidad en el caso de otra persona, la comunico solo a esa persona y al docente.
5. Declaro dónde y para qué usé herramientas de inteligencia artificial. El código generado con IA puede estar sujeto a las mismas leyes de propiedad intelectual que el escrito por una persona, y hay que determinar su titularidad (Omoyeni, 2023, p. 44).
6. No alteraré evidencias (salidas, capturas, registros) ni presentaré trabajo ajeno como propio. Solo practicaré ataques sobre mi caso anonimizado o el entorno que provea el docente, según la sección 1.8.
7. Acepto que un incumplimiento se trata según el reglamento académico de la Universidad \[citar artículo vigente\].

| Nombre completo | Documento | Programa | Fecha | Firma |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Actividad evaluativa y autoevaluación

### Actividad evaluativa: firma del protocolo (requisito, sin calificación)

Esta semana no hay nota. El requisito es firmar el protocolo de anonimización y confidencialidad; sin él no compartes tu caso con el curso.

1. Completa la lista de verificación de la sección 3.2 sobre tu caso.
2. Ejecuta el script de revisión hasta obtener cero hallazgos.
3. Lee completo el texto de la sección 3.3.
4. Firma y fecha el protocolo.
5. Súbelo por el canal que indique el aula virtual, junto con tu caso anonimizado.

Los productos de las otras actividades (matriz de requisitos, mapa de Secure SDLC y tabla de hallazgos del laboratorio) no se entregan esta semana. Guárdalos: son la base del análisis de código del RAE 2.

### Autoevaluación (30 min)

Responde sin mirar la guía y luego compara.

| Pregunta | Respuesta esperada | Dónde repasar |
| --- | --- | --- |
| 1. ¿Por qué un diseño inseguro no se arregla con código perfecto? | Porque el control faltó o fue ineficaz desde el diseño; implementarlo bien no lo crea | OWASP A06:2025; sección 1.1 |
| 2. Escribe la cadena para convertir un riesgo en algo probable. | Riesgo → control → requisito → prueba | Sección 1.2 |
| 3. ¿Qué gana una organización al mover la seguridad «hacia la izquierda»? | Encuentra y corrige las vulnerabilidades antes, con menos personas y menor costo | Fishpool pp. 344–345 |
| 4. ¿Cuál es la mitigación más común de la inyección SQL y por qué funciona? | Consulta parametrizada: los valores atados no se ejecutan como código | Fishpool pp. 225, 342; laboratorio |
| 5. ¿En qué se diferencian CVE y CWE? | CVE identifica un fallo concreto ya descubierto; CWE clasifica el tipo de debilidad | González Manzano y De Fuentes p. 58; OWASP A06 |
| 6. Nombra los cuatro principios de diseño seguro de la hoja de OWASP. | Mínimo privilegio y separación de funciones, defensa en profundidad, confianza cero y seguridad en abierto | Sección 2.3 |
| 7. ¿Qué cambió en el capítulo 1 de ASVS al pasar de 4.0 a 5.0? | Pasó de arquitectura y modelado de amenazas a «Encoding and Sanitization»; la arquitectura se ubica ahora en V15 (por confirmar) | Sección 2.4 |

## Referencias

### Libros de la carpeta BIBLIOGRAFIA\_ROSARIO

Las páginas citadas son las del visor PDF. En González Manzano y De Fuentes la página impresa es la del PDF menos 5; en Franceschetti, la del PDF menos 17.

- Fishpool, B. (2020). *Software development in practice*. BCS, The Chartered Institute for IT. (Archivo: Software\_Development\_in\_Practice\_-\_Bernie\_Fishpool.pdf)
- González Manzano, L., y De Fuentes García-Romero de Tejada, J. M. (2014). *Sistemas seguros de acceso y transmisión de datos (MF0489\_3)*. IC Editorial.
- Franceschetti, D. R. (Ed.). (2018). *Principles of programming & coding*. Salem Press.
- Omoyeni, T. (2023). *Generative AI tools for developers: A practical guide*. SitePoint.
- Sinha, J. (2025). *Kickstart Python programming fundamentals*. Orange Education.

### Documentación en línea de OWASP (consultada el 31 de octubre de 2026)

- OWASP. (2025a). *OWASP Top 10:2025*. [owasp.org/Top10/2025](https://owasp.org/Top10/2025/); categoría A06: [Insecure Design](https://top10.owasp.org/2025/A06_2025-Insecure_Design/)
- OWASP. (2025b). *Application Security Verification Standard (ASVS) 5.0.0*. [github.com/owasp/asvs](https://github.com/owasp/asvs)
- OWASP. (2024). *OWASP Top 10 Proactive Controls 2024*. [top10proactive.owasp.org](https://top10proactive.owasp.org/the-top-10/)
- OWASP. (2017). *ASVS V1 Architecture* \[revisión archivada del wiki\]. [wiki.owasp.org](https://wiki.owasp.org/index.php?diff=next&oldid=235588&title=ASVS_V1_Architecture)
- OWASP. (s. f.-a). *Threat Modeling Cheat Sheet* \[revisión del wiki\]. [wiki.owasp.org](https://wiki.owasp.org/index.php?diff=next&oldid=246981&title=Threat_Modeling_Cheat_Sheet)
- OWASP. (s. f.-b). *OWASP SAMM v2: el modelo*. [owaspsamm.org/model](https://owaspsamm.org/model/)
- OWASP. (s. f.-c). *Secure Product Design Cheat Sheet*. [cheatsheetseries.owasp.org](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Product_Design_Cheat_Sheet.html)
- OWASP. (s. f.-d). *OWASP Developer Guide: Design*. [devguide.owasp.org](https://devguide.owasp.org/en/04-design/)
