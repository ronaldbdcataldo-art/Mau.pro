import os
from dotenv import load_dotenv
import google.generativeai as genai

# Cargar variables de entorno
load_dotenv()

# Configuración
MODELO_POR_DEFECTO = 'gemini-1.5-flash'

class GerenteDeLLM:
    def __init__(self):
        # Lee la clave desde el .env
        self.clave_api = os.getenv('GEMINI_API_KEY')
        
        if not self.clave_api:
            raise ValueError("¡Error! No encontré la GEMINI_API_KEY en el archivo .env")

        genai.configure(api_key=self.clave_api)
        self.modelo = genai.GenerativeModel(MODELO_POR_DEFECTO)

    async def generar_respuesta(self, modo: str, tema: str) -> str:
        prompt = f"Eres Mau, un personaje tierno. Modo: {modo}. Tema: {tema}."
        
        try:
            respuesta = await self.modelo.generate_content_async(prompt)
            return respuesta.text
        except Exception as e:
            return f"Mau tuvo un error: {e}"
