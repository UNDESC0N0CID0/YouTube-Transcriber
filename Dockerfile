# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copiar los archivos de requerimientos e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el script de la aplicación
COPY youtube_downloader.py .

# Copiar el script de inicialización de Whisper
COPY dependency/__init__.py /usr/local/lib/python3.9/site-packages/whisper/

# Crear un directorio para los videos descargados
RUN mkdir /app/downloads

# Ejecutar el script
CMD ["python", "youtube_downloader.py"]
