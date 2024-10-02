import argparse
import whisper
import os
from pytube import YouTube
from tqdm import tqdm
import yt_dlp

def progress_hook(d):
    if d['status'] == 'downloading':
        progress_bar.update(d['downloaded_bytes'] - progress_bar.n)
    elif d['status'] == 'finished':
        progress_bar.close()
        print("Descarga completada. Convirtiendo...")

def download_youtube_video(url, output_path="."):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'downloads/{output_path}/%(title)s.%(ext)s',
        'progress_hooks': [progress_hook],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        print(f"Título del video: {info['title']}")
        print(f"Duración: {info['duration']} segundos")
        print(f"Número de vistas: {info['view_count']}")
        
        global progress_bar
        progress_bar = tqdm(total=info['filesize'], unit='B', unit_scale=True, desc="Descargando", ncols=70)
        
        ydl.download([url])
        downloaded_file = ydl.prepare_filename(info)

    print(f"\nVideo descargado exitosamente en: downloads/{output_path}")
    return downloaded_file

def ensure_transcriptions_dir():
    transcriptions_dir = "transcriptions"
    if not os.path.exists(transcriptions_dir):
        os.makedirs(transcriptions_dir)
    return transcriptions_dir

def save_transcription(text, audio_filename):
    transcriptions_dir = ensure_transcriptions_dir()
    transcription_filename = os.path.join(transcriptions_dir, os.path.basename(audio_filename) + ".txt")
    with open(transcription_filename, "w") as f:
        f.write(text)

def transcribir_audio(audio_filename, model_type="turbo"):
    try:
        if not os.path.exists(audio_filename):
            raise FileNotFoundError(f"El archivo {audio_filename} no existe.")
        
        model = whisper.load_model(model_type)
        result = model.transcribe(audio_filename)
        print(f"Transcripción completada.\n")
        
        save_transcription(result["text"], audio_filename)
        
        return result["text"]
    except Exception as e:
        print(f"Error al transcribir el audio: {e}")
        return None

# Función principal que solicita la URL, descarga el audio y transcribe
def main():
    parser = argparse.ArgumentParser(description="Descargar y transcribir audio de un video de YouTube")
    parser.add_argument('url', type=str, help='URL del video de YouTube')
    parser.add_argument('--model', type=str, default='turbo', help='Tipo de modelo Whisper a usar (por defecto: turbo)')
    parser.add_argument('--summary', type=str, default='resumen corto', help='Tipo de resumen (por defecto: resumen corto)')
    args = parser.parse_args()

    video_url = args.url
    model_type = args.model
    summary_type = args.summary
    # Paso 1: Descargar el audio del video de YouTube
    audio_filename = download_youtube_video(video_url)

    if audio_filename:
        # Paso 2: Transcribir el audio (puedes cambiar a MP3 si prefieres, pero Whisper admite MP4)
        texto_transcrito = transcribir_audio(audio_filename,model_type)
        
        if texto_transcrito:
            print("\n\nTexto transcrito:\n")
            print(texto_transcrito)
        else:
            print("No se pudo transcribir el audio.")
    else:
        print("No se pudo descargar el audio del video.")

# Llamada a la función principal
if __name__ == "__main__":
    main()              