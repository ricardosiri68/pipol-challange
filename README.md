# Pipol Hub Challange

Intrucciones para montar el proyecto con `docker`

```sh
docker build -t pipol.gpl . && docker run -p 8000:8000 pipol.glp
```

Al iniciarse el contenedor en la consola CLI se deberia ver el siguiente mensaje:

```sh
INFO:     Will watch for changes in these directories: ['/app']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [1] using WatchFiles
INFO:     Started server process [15]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Luego podemos abrir otra consola nueva y ejecutar el siguiente script bash para probar el endpoint graphql.

```sh
./test-api.sh
```

### Problemas con el script test-api.sh

Si es un problema de permisos se puede solucionar añadiendole permisos.

```sh
chmod +x test-api.sh
```