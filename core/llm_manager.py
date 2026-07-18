import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class LLMManager:
    def __init__(self):
        # Lee la clave desde el .env
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("¡Error! No encontré la GEMINI_API_KEY en el .env")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    async def generate_response(self, mode: str, topic: str) -> str:
        prompt = f"Eres Mau, un personaje tierno. Modo: {mode}. Tema: {topic}. Responde breve."
        try:
            response = await self.model.generate_content_async(prompt)
            return response.text
        except Exception as e:
            return f"Mau tuvo un error: {e}"