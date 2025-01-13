# Convertir entrevistas de audio a texto con Python [Open Source]

<!-- ABOUT THE PROJECT -->
## Acerca del proyecto

Este proyecto aborda la problemática de convertir entrevistas de audio a texto, utilizando modelos de inteligencia
artificial open source o código abierto. La idea es que puedas convertir tus entrevistas de audio a texto de manera sencilla y rápida.

## Tutorial
* Vídeo tutorial de Youtube <a href="https://youtu.be/7utWPIAaw-M">https://youtu.be/7utWPIAaw-M</a>
 
<!-- GETTING STARTED -->
## Tecnologías

* Python

### Prerequisitos

Debe tener instalado Python en su computadora. Puede descargarlo desde el siguiente enlace: <a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a>

* Clonar el repositorio
  ```sh
  git clone https://github.com/backtesty/Speech2Text.git
  ```

* Crear el entorno virtual
  ```sh
  python -m venv env
  ```
* Activar entorno virtual (windows):
  ```sh
  env\Scripts\activate
  ```
* Instalar las dependencias del proyecto:
  ```sh
  pip install -r requirements.txt
  ```
* Migrar la base de datos:
  ```sh
  python manage.py main.py
  ```
## Acceso a los modelos de inteligencia artificial

### Modelo de Diarización de Audio
* pyannote/speaker-diarization-3.1: <a href="https://github.com/pyannote/pyannote-audio?tab=readme-ov-file">https://github.com/pyannote/pyannote-audio?tab=readme-ov-file</a>

### Whisper para la transcripción de audio
* Whisper: <a href="https://github.com/openai/whisper">https://github.com/openai/whisper</a>

### Hugging Face Open Source Model
* Hugging Face: <a href="https://huggingface.co/pyannote/speaker-diarization-3.1">https://huggingface.co/pyannote/speaker-diarization-3.1</a>

## Finalmente

Agradezco tu visita, no olvides seguirme y tu respectivo me gusta si te sirvió el vídeo, más información en mi canal de <a href="https://www.youtube.com/channel/UCxGqlLmQXjFjkrnSRLa7B7g">YouTube</a>.
