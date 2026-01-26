# text to speech with gtts(Proceses and save it )
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text,output_filepath):
    language = "en"

    audio_obj = gTTS(
        text=input_text,
        lang = language,
        slow = False
    )
    audio_obj.save(output_filepath)
    

text = """
Hello! I am your Medical AI Assistant.
I can help you with basic medical questions.
"""
text_to_speech_with_gtts_old(input_text=text, output_filepath="gtts_testing_normal_3.mp3")
print("File Saved on Explorer. complate!")


# with autoplay
# Text → MP3 → WAV → Play

import subprocess
from pydub import AudioSegment
import os

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"

    mp3_file = output_filepath
    wav_file = output_filepath.replace(".mp3", ".wav")

    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(mp3_file)

    # Convert MP3 to WAV
    AudioSegment.from_mp3(mp3_file).export(wav_file, format="wav")

    # Play WAV (Windows)
    subprocess.run([
        "powershell",
        "-c",
        f'(New-Object Media.SoundPlayer "{wav_file}").PlaySync();'
    ])

    os.remove(wav_file) # wav_file automaticalyy remove the it 
    

input_text = """
Hello! I am your Medical AI Assistant.
I can help you with basic medical questions.
"""
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay_3.mp3")
# print("You Autoplay Complate!")
