# AI Doctor with Vision and Voice

A voice and image based AI doctor app built with Python and Gradio.
You speak your symptoms, upload a medical image, and the AI responds 
like a real doctor — both in text and voice.

This is not for real medical use. I built it to learn how to combine 
STT, LLM vision, and TTS together in one pipeline.

## What it does

You open the app, speak into your mic, upload an image (like a skin photo 
or report), and the bot analyzes both. It then gives a short, clear 
response like a doctor would — and also speaks it out loud.

## How it works
```
You speak into the mic
↓
Audio is transcribed using Whisper (Groq STT)
↓
Your text + uploaded medical image is sent to Llama 4 Maverick
↓
AI responds like a doctor (no markdown, short and clear)
↓
Response is converted to speech using gTTS
↓
You see the text + hear the doctor voice
```

## Project Structure

```
AI_VOICE_BOT/
│
├── src/
│   └── gradio_app.py        - main voice bot app with gradio UI
│
├── learning/
│   ├── image_query_1.py     - practice: sending image to llama model
│   ├── speech_to_text_2.py  - practice: recording mic audio and STT
│   └── text_to_speech_3.py  - practice: converting text to speech
│
├── assets/                  - sample images and audio files
├── .env                     - api keys (not pushed to github)
├── .gitignore
├── practice.ipynb           - rough notebook for experimenting
├── requirements.txt
└── README.MD
```

## Models Used

- LLM + Vision  : meta-llama/llama-4-maverick-17b-128e-instruct  (via Groq)
- STT           : whisper-large-v3  (via Groq)
- TTS           : gTTS (Google Text to Speech)

## Setup

Requirements:
- Python 3.13+
- Groq API key

Steps:

```bash
git clone https://github.com/RahulNinawe05/AI_Voice_bot
cd AI_Voice_Bot

python -m venv .venv
.venv\Scripts\activate        # windows

pip install -r requirements.txt
```
## API Key Setup

Create a .env file in the root folder:
```
GROQ_API_KEY: # Get free key from: https://console.groq.com/keys
```