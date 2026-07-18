from gtts import gTTS
import os

class AdministradorDeVoz:
    def __init__(self):
        # Inicialización de la clase
        pass

    def hablar(self, texto: str):
        try:
            # Generamos el audio con gTTS
            tts = gTTS(text=texto, lang='es')
            # Guardamos el archivo
            tts.save('audio_mau.mp3')
            print('Mau está hablando...')
        except Exception as e:
            print(f"Error al generar el audio: {e}")
