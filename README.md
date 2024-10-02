# YouTube Video Transcriber

Este proyecto es una aplicación de línea de comandos (CLI) que permite descargar videos de YouTube y transcribir su contenido de audio utilizando el modelo Whisper. La transcripción se guarda en un archivo de texto para su posterior uso. Además, el proyecto cuenta con soporte para Docker, facilitando su despliegue y ejecución.

## Características

- Descarga videos de YouTube en el mejor formato de audio disponible.
- Transcribe el audio utilizando el modelo Whisper.
- Guarda la transcripción en un archivo de texto.
- Contenedores Docker para facilitar la configuración y ejecución del proyecto.

## Requisitos

- Docker y Docker Compose
- Python 3.8 o superior (si se ejecuta sin Docker)
- Paquetes Python: `whisper`, `pytube`, `tqdm`, `yt_dlp`

## Configuración

1. Construye el contenedor Docker:
   ```bash
   docker-compose build
   ```

## Uso

### Ejecución con Docker

1. Ejecuta la aplicación utilizando Docker Compose:
   ```bash
   docker-compose run youtube_transcriber <URL_DEL_VIDEO_YOUTUBE>
   ```

   Reemplaza `<URL_DEL_VIDEO_YOUTUBE>` con la URL del video que deseas transcribir.

### Ejecución sin Docker

1. Instala las dependencias de Python:
   ```bash
   pip install -r requirements.txt
   ```

2. Ejecuta la aplicación de línea de comandos:
   ```bash
   python youtube_downloader.py <URL_DEL_VIDEO_YOUTUBE>
   ```

## Estructura del proyecto

- `youtube_downloader.py`: Archivo principal de la aplicación que maneja la descarga y transcripción de videos de YouTube.
- `Dockerfile`: Configuración para construir la imagen Docker.
- `docker-compose.yml`: Configuración de Docker Compose para la ejecución del contenedor.
- `downloads/`: Carpeta donde se guardan los archivos descargados.
- `transcriptions/`: Carpeta donde se guardan las transcripciones.

## Personalización

- Puedes cambiar el modelo de Whisper usando la opción `--model` en la línea de comandos:
  ```bash
  python youtube_downloader.py <URL_DEL_VIDEO_YOUTUBE> --model base
  ```
  Los modelos disponibles son `tiny`, `base`, `small`, `medium`, `large`, `turbo`.

|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~10x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~7x       |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~4x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |
| turbo  |   809 M    |        N/A         |      `turbo`       |     ~6 GB     |      ~8x       |

## Créditos

Este proyecto utiliza las bibliotecas:

- [whisper](https://github.com/openai/whisper) para la transcripción de audio.
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) para la descarga de videos de YouTube.
