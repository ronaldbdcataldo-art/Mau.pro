from gtts import gTTS
import os

class VoiceManager:
    def __init__(self):
        pass

    def speak(self, text: str):
        tts = gTTS(text=text, lang='es')
        tts.save('audio_mau.mp3')
        print('Mau está hablando...')
