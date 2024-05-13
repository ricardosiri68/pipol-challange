# Usa la imagen oficial de Python 3.11 como base
FROM python:3.10

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el contenido del directorio actual al contenedor en /app
COPY . /app

# Instala las dependencias
RUN pip install -r requirements.txt --upgrade pip

# Expone el puerto 8000 (cambia esto si tu aplicación usa otro puerto)
EXPOSE 8000

# Ejecuta tu script de Python
CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000"]