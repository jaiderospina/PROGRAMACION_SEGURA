# Laboratorio guiado (semana 2)

Solo se ejecuta en local contra este repositorio. Ver las reglas de laboratorio del README.

Con la aplicaciÃ³n en marcha (`python3 app/app.py`), en otra terminal:

1. **LÃ­nea base.** Un inicio de sesiÃ³n vÃ¡lido:

   ```bash
   curl -i -X POST -d "usuario=lector1&clave=lectura123" http://127.0.0.1:8000/login
   ```

2. **Entrada que cambia la consulta.** Se envÃ­a a `/login` un usuario con comilla simple y comentario SQL (`admin1'--`) y se compara con la lÃ­nea base.
3. **Salida sin escapar.** Se envÃ­a a `/buscar` un parÃ¡metro `q` que contenga una etiqueta HTML y se observa cÃ³mo se refleja.
4. **Ruta controlada por el usuario.** Se pide a `/reporte` un nombre de archivo que salga de la carpeta de reportes.
5. **Acceso sin autenticar.** Se consulta `/admin/usuarios` sin iniciar sesiÃ³n.

Para cada hallazgo se registra: ubicaciÃ³n (archivo y lÃ­nea), categorÃ­a OWASP Top 10, CWE, evidencia y correcciÃ³n propuesta. Las pruebas de `tests/test_seguridad.py` sirven como criterio de correcciÃ³n.
