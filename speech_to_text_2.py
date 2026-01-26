# Ye code microphone se audio record karta hai, usko MP3 file me save karta hai.

# ffmpeg - image,video,etc Professing
# portaudio - record the audio
#Step1: Setup Audio recorder (ffmpeg & portaudio)

import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=20, phrase_time_limit=10):
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            logging.info("Start speaking now...")
            audio_data = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit
            )

            logging.info("Recording complete.")

            wav_data = audio_data.get_wav_data()
            audio = AudioSegment.from_wav(BytesIO(wav_data))
            audio.export(file_path, format="mp3", bitrate="128k")

            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"Error: {e}")

audio_filepath="audio_voice_2.mp3"
record_audio(file_path=audio_filepath)


#Step2: Setup Speech to text-STT-model for transcription
import os
from groq import Groq

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise Exception("GROQ_API_KEY is missing. Set it using setx or set command.")

client = Groq(api_key=os.getenv(GROQ_API_KEY))
speech_to_text_model = "whisper-large-v3"

audio_file = open(audio_filepath,'rb')
transcription = client.audio.transcriptions.create(
    model=speech_to_text_model,
    file=audio_file,
    language='en'
)

print(transcription.text)