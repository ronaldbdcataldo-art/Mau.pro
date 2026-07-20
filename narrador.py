import pyttsx3
import asyncio

class NarradorMau:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # velocidad
        self.engine.setProperty('voice', 'spanish')  # voz en español

    async def narrar(self, texto):
        print('[NARRADOR] Mau está narrando...')
        self.engine.say(texto)
        self.engine.runAndWait()
        await asyncio.sleep(1)
