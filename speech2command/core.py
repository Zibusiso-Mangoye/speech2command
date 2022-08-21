import speech_recognition as sr
import gtts
from playsound import playsound
import os
from datetime import datetime
from notion import NotionClient

r = sr.Recognizer()

token = "YOUR NOTION TOKEN HERE"
database_id = "YOUR NOTION DATABASE_ID HERE"

client = NotionClient(token, database_id)

ACTIVATION_COMMAND = "hey sam"
class S2CClient:
    
    def get_audio(self):
        with sr.Microphone() as source:
            print("Say something")
            audio = r.listen(source)
        return audio

    def audio_to_text(self, audio):
        text = ""
        try:
            text = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError:
            print("could not request results from API")
        return text

    def play_sound(self, text):
        try:
            tts = gtts.gTTS(text)
            tempfile = "./temp.mp3"
            tts.save(tempfile)
            playsound(tempfile)
            os.remove(tempfile)
        except AssertionError:
            print("could not play sound")