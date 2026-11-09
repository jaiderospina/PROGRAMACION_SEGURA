# Guía del estudiante: cómo trabajar con el caso, paso a paso

Esta guía explica cómo se descarga, se instala, se ejecuta y se prueba el caso del curso, y cómo se organiza el trabajo de cada semana. Cada comando va acompañado de lo que hace. Los ejemplos están escritos para **Windows con PowerShell**; las equivalencias para macOS y Linux se indican donde difieren.

> **Advertencia.** El programa es vulnerable a propósito. Solo se ejecuta en el equipo propio (`127.0.0.1`), nunca en un servidor accesible desde internet. Las reglas de laboratorio de la cartilla de la semana 1 aplican a todo lo que se haga aquí.

## 1. Qué se necesita antes de empezar

| Requisito | Para qué sirve | Cómo se verifica |
| --- | --- | --- |
| Python 3.10 o superior | Ejecuta la aplicación y las pruebas | `python --version` |
| Git | Descarga el repositorio y registra los cambios | `git --version` |
| Un editor de código (por ejemplo, Visual Studio Code) | Lee y modifica los archivos | Se abre la carpeta del repositorio |
| Un navegador | Muestra la aplicación | Cualquiera sirve |
| Una cuenta de GitHub con acceso al repositorio | Permite clonar el repositorio privado | Se acepta la invitación del docente (sección 2) |

- `python --version` imprime la versión instalada. Si PowerShell responde que `python` no se reconoce, se prueba `py --version`; en ese caso se usa `py` en lugar de `python` en todos los comandos de esta guía.
- `git --version` hace lo mismo con Git. Si no está instalado, se descarga desde <https://git-scm.com>.

## 2. Obtener el código

**Acceso al repositorio.** El repositorio es **privado**: solo lo ven las cuentas de GitHub que el docente invita. La invitación llega al correo asociado a la cuenta de GitHub y se acepta desde el enlace del mensaje o desde <https://github.com/notifications>. Antes de clonar, se verifica que al abrir la dirección del repositorio en el navegador, con la sesión iniciada, la página carga; si aparece «404», la cuenta no tiene acceso todavía.

**Opción A (recomendada): clonar con Git.**

```powershell
git clone https://github.com/jaiderospina/PROGRAMACION_SEGURA.git
cd PROGRAMACION_SEGURA
```

- `git clone <dirección>` copia el repositorio completo, con su historial, en una carpeta nueva con el nombre del repositorio.
- La primera vez, Git abre una ventana del navegador para iniciar sesión en GitHub (lo gestiona *Git Credential Manager*, incluido con Git para Windows). Se inicia sesión con la cuenta que recibió la invitación. Si Git responde `Repository not found`, la causa casi siempre es una cuenta sin acceso o una sesión iniciada con otra cuenta.
- `cd PROGRAMACION_SEGURA` entra a esa carpeta. Todos los comandos siguientes se ejecutan **desde esta carpeta**, llamada «raíz del repositorio».

**Opción B: descargar un ZIP.** En la página del repositorio, el botón verde *Code* tiene la opción *Download ZIP*. Se descomprime y se abre una terminal dentro de la carpeta resultante. Se requiere tener la sesión iniciada con la cuenta invitada. Esta opción no incluye historial, por lo que no permite registrar cambios con Git.

Para confirmar que la terminal está en la raíz, se ejecuta:

```powershell
dir
```

`dir` lista el contenido de la carpeta. Deben aparecer `app`, `tests`, `docs`, `material`, `README.md` y `requirements.txt`.

## 3. Crear y activar el entorno virtual

Un **entorno virtual** es una carpeta con su propia copia de Python y de las bibliotecas. Evita que las dependencias del curso se mezclen con las de otros proyectos.

```powershell
python -m venv .venv
```

- `python -m venv .venv` ejecuta el módulo `venv` de Python y crea la carpeta oculta `.venv` en la raíz. Se hace una sola vez.

```powershell
.venv\Scripts\Activate.ps1
```

- Este comando **activa** el entorno en la sesión actual. Cuando funciona, el indicador de la terminal empieza con `(.venv)`.
- Si PowerShell responde que la ejecución de scripts está deshabilitada, se ejecuta una vez:

  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
  ```

  Este comando permite ejecutar scripts locales solo para el usuario actual y no cambia la configuración del equipo. Después se repite el comando de activación.

| Sistema o terminal | Comando de activación |
| --- | --- |
| Windows, PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows, Símbolo del sistema (cmd) | `.venv\Scripts\activate.bat` |
| macOS y Linux | `source .venv/bin/activate` |

El entorno se activa **en cada terminal nueva** que se abra. Para salir de él se escribe `deactivate`.

## 4. Instalar las dependencias

Con el entorno activado:

```powershell
pip install -r requirements.txt -r requirements-dev.txt
```

- `pip install` instala bibliotecas de Python.
- `-r requirements.txt` indica que la lista de bibliotecas está en ese archivo (aquí, Flask, el marco web de la aplicación).
- `-r requirements-dev.txt` agrega las bibliotecas de desarrollo (aquí, pytest, que ejecuta las pruebas).
- Al terminar aparece «Successfully installed …». Un aviso que diga que hay una versión nueva de pip no es un error y no hace falta atenderlo.

## 5. Ejecutar la aplicación

Desde la **raíz del repositorio**:

```powershell
python app/app.py
```

- `python app/app.py` ejecuta el archivo `app.py` que está dentro de la carpeta `app`. Si la terminal está dentro de `app`, el comando correcto es `python app.py`.
- La terminal queda ocupada mostrando mensajes y debe permanecer abierta mientras se use la aplicación. Debe aparecer una línea como `Running on http://127.0.0.1:8000`.
- `127.0.0.1` es la dirección del propio equipo y `8000` es el puerto. Se abre <http://127.0.0.1:8000> en el navegador y aparece la página de inicio de la «Biblioteca de la Facultad».
- Para detener la aplicación se presiona `Ctrl + C` en esa terminal.
- La primera vez, la aplicación crea el archivo `app/biblioteca.db` con tres usuarios y cuatro libros sintéticos. Para reiniciar los datos se detiene la aplicación y se borra el archivo con `Remove-Item app\biblioteca.db`; se vuelve a crear al iniciar.
- Si el puerto 8000 ya está en uso, se cambia el número en la última línea de `app/app.py` (`port=8000`) por otro libre, por ejemplo 8001.

## 6. Probar las rutas de la aplicación

| Ruta | Método | Qué hace | Ejemplo |
| --- | --- | --- | --- |
| `/` | GET | Página de inicio | Se abre en el navegador |
| `/buscar?q=texto` | GET | Busca libros por título | <http://127.0.0.1:8000/buscar?q=Python> |
| `/reporte?nombre=archivo` | GET | Descarga un reporte de la carpeta `app/reportes` | <http://127.0.0.1:8000/reporte?nombre=reporte_publico.txt> |
| `/login` | POST | Inicia sesión con usuario y clave | Se prueba con `curl.exe` (ver abajo) |
| `/admin/usuarios` | GET | Lista usuarios (ruta administrativa) | <http://127.0.0.1:8000/admin/usuarios> |
| `/reset?usuario=nombre` | GET | Genera un token de restablecimiento | <http://127.0.0.1:8000/reset?usuario=lector1> |

Las rutas `GET` se prueban escribiendo la dirección en el navegador. Para `/login`, que recibe datos por `POST`, se abre **una segunda terminal** y se ejecuta:

```powershell
curl.exe -i -X POST -d "usuario=lector1&clave=lectura123" http://127.0.0.1:8000/login
```

- `curl.exe` es la herramienta de línea de comandos que hace peticiones web. Se escribe con `.exe` porque en PowerShell `curl` es un alias de otro comando que no acepta estas opciones.
- `-i` muestra también los encabezados de la respuesta (el código de estado, por ejemplo `200 OK`).
- `-X POST` fija el método de la petición.
- `-d "usuario=...&clave=..."` envía los datos del formulario.
- Usuarios de ejemplo (sintéticos): `lector1` con clave `lectura123`, `lector2` con `lectura456` y `admin1` con `admin123`.

## 7. Ejecutar las pruebas

En una terminal con el entorno activado y ubicada en la raíz:

```powershell
python -m pytest -m "not seguridad"
```

- `python -m pytest` ejecuta pytest, que busca y corre las pruebas de la carpeta `tests`.
- `-m "not seguridad"` ejecuta solo las pruebas **funcionales**, que verifican que la aplicación hace lo que debe. Deben pasar **5 de 5**, antes y después de corregir.

```powershell
python -m pytest -m seguridad
```

- `-m seguridad` ejecuta solo las pruebas **de seguridad**, que describen el comportamiento seguro esperado. En la versión original, **11 fallan a propósito**. Cada prueba que pasa a verde indica una corrección lograda.

Opciones útiles:

| Opción | Efecto |
| --- | --- |
| `-q` | Salida resumida |
| `-x` | Se detiene en la primera prueba que falla |
| `-k nombre` | Ejecuta solo las pruebas cuyo nombre contiene `nombre` (por ejemplo, `-k login`) |
| `-v` | Muestra el nombre de cada prueba |

Cómo se lee un resultado: un punto (`.`) es una prueba que pasa y una `F` es una que falla. En la sección `FAILURES` aparecen el archivo, la línea y la comparación que no se cumplió (la línea que empieza con `E`).

## 8. Flujo de trabajo y control de versiones

Para no perder el original, cada semana se trabaja en una rama propia.

```powershell
git switch -c semana-3-correcciones
```

- `git switch -c <nombre>` crea una rama nueva y cambia a ella. Los cambios quedan aislados de `main`.

Después de modificar archivos:

```powershell
git status
git add app/app.py
git commit -m "Corrige la inyección SQL en login"
```

- `git status` muestra qué archivos cambiaron.
- `git add <archivo>` selecciona los cambios que entrarán en el registro.
- `git commit -m "<mensaje>"` guarda ese registro con un mensaje que explica qué se cambió y por qué.

El acceso del estudiantado al repositorio es de **solo lectura**: se puede clonar y consultar, pero `git push` es rechazado. Por esta razón, el trabajo de cada semana se conserva **en el equipo propio**, con las ramas y los registros anteriores como historial personal, y se entrega por el aula virtual según indique cada actividad.

Para entregar los cambios hechos sobre el código, se genera un archivo de diferencias:

```powershell
git diff main > semana-3-cambios.patch
```

- `git diff main` compara la rama actual con `main` y muestra línea por línea qué se agregó y qué se quitó.
- `> semana-3-cambios.patch` guarda esa comparación en un archivo de texto que se adjunta en el aula. También se pueden entregar directamente los archivos modificados (por ejemplo, `app/app.py`), según pida la actividad.

El material del repositorio es de uso exclusivo del curso. No se copia a repositorios propios, públicos o privados, ni se comparte con personas ajenas al grupo; esto hace parte del protocolo de confidencialidad e integridad académica firmado en la semana 1.

## 9. Qué se hace cada semana con el caso

| Semana | Trabajo | Comando principal |
| --- | --- | --- |
| 1 | Anonimizar el caso propio y firmar el protocolo | `python scripts/revisar_anonimizacion.py carpeta_del_caso NombreEmpresa Apellido` |
| 2 | Reproducir los ataques del laboratorio y clasificar cada hallazgo con OWASP y CWE | Ver `docs/laboratorio-guiado.md` |
| 3 | Corregir las vulnerabilidades (Entrega 1) | `python -m pytest -m seguridad` |
| 4 | Identificar qué datos requieren protección criptográfica | Lectura del código de `app/db.py` y `app/catalogo.py` |
| 5 | Implementar controles criptográficos (Entrega 2) | `python -m pytest -m seguridad` |
| 6 | Pruebas de seguridad y pipeline (Entrega 3) | `bandit -r app` y `pip-audit -r requirements.txt` |
| 7 | SAST y SCA en el pipeline | `.github/workflows/ci.yml` |

Sobre el comando de la semana 1: `scripts/revisar_anonimizacion.py` recorre la carpeta indicada y busca correos, direcciones IP, URL, credenciales, cadenas largas que parecen llaves y los nombres propios que se escriban a continuación. Termina con la línea `Hallazgos: N`; el objetivo es `Hallazgos: 0`.

Sobre los de la semana 6, que se instalan primero con `pip install bandit pip-audit`: `bandit -r app` hace un análisis estático (SAST) del código de la carpeta `app` de forma recursiva (`-r`) y reporta patrones inseguros; `pip-audit -r requirements.txt` compara las bibliotecas listadas con una base de vulnerabilidades conocidas (SCA). Para el ejercicio de dependencias se usa también `requirements-legacy.txt`, que fija versiones antiguas con fallas conocidas.

## 10. Problemas frecuentes

| Mensaje o síntoma | Causa | Solución |
| --- | --- | --- |
| `app\app.py : El módulo 'app' no pudo cargarse` | Se escribió la ruta como si fuera un comando, o la terminal está dentro de `app` | `python app/app.py` desde la raíz, o `python app.py` dentro de `app` |
| `ModuleNotFoundError: No module named 'flask'` | El entorno virtual no está activo | Activarlo (sección 3) e instalar (sección 4) |
| `No se puede cargar el archivo ... Activate.ps1` | PowerShell bloquea scripts | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| `python` no se reconoce | Python no está en la variable PATH | Usar `py` o reinstalar marcando *Add Python to PATH* |
| `Repository not found` al clonar | La cuenta no tiene acceso o se inició sesión con otra cuenta | Aceptar la invitación e iniciar sesión con la cuenta invitada |
| `Address already in use` o el puerto está ocupado | Otro programa usa el puerto 8000 | Cambiar el puerto en `app/app.py` (sección 5) |
| `curl` rechaza `-X` o `-d` | En PowerShell `curl` es un alias | Usar `curl.exe` |
| Las pruebas no encuentran módulos | Se ejecutó pytest fuera de la raíz | Ejecutar `python -m pytest` desde la raíz |
| Datos raros en la aplicación tras muchas pruebas | La base de datos acumuló cambios | Detener la aplicación y borrar `app\biblioteca.db` |

Para saber qué programa usa un puerto en Windows: `netstat -ano | findstr :8000` lista las conexiones de ese puerto y el número de proceso (PID) que las mantiene.
