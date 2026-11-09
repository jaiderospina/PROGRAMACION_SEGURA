# Laboratorio guiado (semana 2)

Solo se ejecuta en local contra este repositorio. Ver las reglas de laboratorio del README.

Con la aplicación en marcha (`python app/app.py`), en otra terminal. En Windows PowerShell se usa `curl.exe` (en macOS y Linux, `curl`); el detalle de cada comando está en la [guía del estudiante](guia-del-estudiante.md):

1. **Línea base.** Un inicio de sesión válido:

   ```powershell
   curl.exe -i -X POST -d "usuario=lector1&clave=lectura123" http://127.0.0.1:8000/login
   ```

2. **Entrada que cambia la consulta.** Se envía a `/login` un usuario con comilla simple y comentario SQL (`admin1'--`) y se compara con la línea base.
3. **Salida sin escapar.** Se envía a `/buscar` un parámetro `q` que contenga una etiqueta HTML y se observa cómo se refleja.
4. **Ruta controlada por el usuario.** Se pide a `/reporte` un nombre de archivo que salga de la carpeta de reportes.
5. **Acceso sin autenticar.** Se consulta `/admin/usuarios` sin iniciar sesión.

Para cada hallazgo se registra: ubicación (archivo y línea), categoría OWASP Top 10, CWE, evidencia y corrección propuesta. Las pruebas de `tests/test_seguridad.py` sirven como criterio de corrección.
