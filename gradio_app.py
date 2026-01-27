# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

import os
import base64
import gradio as gr
from io import BytesIO
from dotenv import load_dotenv
from gtts import gTTS
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not found")

client = Groq(api_key=GROQ_API_KEY)

LLM_MODEL = "meta-llama/llama-4-maverick-17b-128e-instruct"
STT_MODEL = "whisper-large-v3"

system_prompt = """
You have to act as a professional doctor.
Analyze the medical image carefully.
Give simple, clear advice.
Do not use markdown.
Respond like a real doctor.
Keep it short.
"""

def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def analyze_image_with_query(query, encoded_image):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": query},
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}"
                    }
                }
            ]
        }
    ]

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=messages
    )
    return response.choices[0].message.content

def transcribe_with_groq(audio_filepath):
    with open(audio_filepath, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            file=audio_file,
            model=STT_MODEL,
            language="en"
        )
    return transcript.text


def text_to_speech_with_gtts(input_text, output_filepath="final.mp3"):
    tts = gTTS(text=input_text, lang="en")
    tts.save(output_filepath)
    return output_filepath

def process_inputs(audio_filepath, image_filepath):

    # Speech → Text
    patient_text = transcribe_with_groq(audio_filepath)

    # Image + Query → Doctor Brain
    if image_filepath:
        encoded_image = encode_image(image_filepath)
        doctor_response = analyze_image_with_query(
            query=patient_text,
            encoded_image=encoded_image
        )
    else:
        doctor_response = "No image provided for medical analysis."

    # Doctor Voice
    doctor_audio = text_to_speech_with_gtts(doctor_response)

    return patient_text, doctor_response, doctor_audio

iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="Patient Voice"),
        gr.Image(type="filepath", label="Medical Image")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(label="Doctor Voice")
    ],
    title="🩺 AI Doctor with Vision and Voice"
)

iface.launch(debug=True)