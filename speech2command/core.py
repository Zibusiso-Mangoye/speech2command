import os

from gtts import gTTS
import speech_recognition as sr
from playsound import playsound


class S2CClient:
    def __init__(self) -> None:
        self.recogniser = sr.Recognizer()
        playsound("speech2command\data\starting_sound.mp3")
    
    def get_audio(self) -> bytes:
        with sr.Microphone() as source:
            s2c_welcome_message = "Hello sir, waiting for command"
            self.play_sound(s2c_welcome_message)
            audio = self.recogniser.listen(source)
        return audio

    def audio_to_text(self, audio):
        text = ""
        try:
            text = self.recogniser.recognize_google(audio)
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError:
            print("could not request results from API")
        return text

    def play_sound(self, text):
        try:
            tts = gTTS(text, slow=False)
            tempfile = "./temp.mp3"
            tts.save(tempfile)
            playsound(tempfile)
            os.remove(tempfile)
        except AssertionError:
            print("could not play sound")
            
    def execute(self, command) -> None:

        if 'read' in command:
            print("Reading...")
            
        return