# synthesize_text_action.py
import torch
from transformers import pipeline
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import base64
import io
import numpy as np
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

# from actions.synthesize_text_action import synthesize_text
import soundfile as sf
import torch
from transformers import pipeline
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from pydub import AudioSegment

# Load the text-to-speech pipeline
# Load the text-to-speech pipeline
pipe = pipeline("text-to-speech", model="suno/bark-small", device="cpu")

def synthesize_text(text):
    print("Synthesizing text...")
    print(text)
    output = pipe(text)
    audio_array = output["audio"]
    sampling_rate = output["sampling_rate"]

    # Ensure audio is 1D
    if len(audio_array.shape) > 1:
        audio_array = audio_array.squeeze()

    # Normalize audio
    audio_array = np.clip(audio_array, -1.0, 1.0)

    # Save audio to WAV in memory
    audio_buffer = io.BytesIO()
    sf.write(audio_buffer, audio_array, samplerate=sampling_rate, format="WAV")
    audio_buffer.seek(0)

    # Convert WAV to MP3
    audio_segment = AudioSegment.from_file(audio_buffer, format="wav")
    compressed_audio_buffer = io.BytesIO()
    audio_segment.export(compressed_audio_buffer, format="mp3", bitrate="64k")
    compressed_audio_buffer.seek(0)

    # Encode the MP3 as Base64
    base64_audio = base64.b64encode(compressed_audio_buffer.read()).decode("utf-8")
    return base64_audio