#trying to automate some voice transcription

import openai_secret_manager
import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Use openai_secret_manager to get the credentials for the Google Speech-to-Text API
secrets = openai_secret_manager.get_secrets("google")

# Set the environment variable for GOOGLE_APPLICATION_CREDENTIALS
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = secrets["api_key"]

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = "audio.wav"

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)

# The transcription
transcription = ""
for result in response.results:
    transcription += result.alternatives[0].transcript

# Saving the transcription to a text file
with open("transcription.txt", "w") as f:
    f.write(transcription)

print(f"Transcription saved to transcription.txt")

#This script uses the google-cloud-speech library to interact with the Google Speech-to-Text API and the openai_secret_manager library to securely retrieve the API credentials.

#You will need to provide the path to the audio file you want to transcribe in the file_name variable. The script will transcribe the audio file and save the transcription to a text file named transcription.txt.

#