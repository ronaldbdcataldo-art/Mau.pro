import flet as ft
from core.llm_manager import LLMManager
from core.voice_manager import VoiceManager

async def main(page: ft.Page):
    page.title = 'Proyecto Mau'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Inicialización de servicios
    llm = LLMManager()
    voice = VoiceManager()
    
    # Ponemos el icono y el texto directamente, sin cajas intermedias
    page.add(
        ft.Icon("face", size=150, color="orange"),
        ft.Text('¡Hola! Soy Mau, tu amigo.', size=30, weight=ft.FontWeight.BOLD, color="blue")
    )
    print('Sistema Mau: Interfaz renderizada correctamente.')

ft.app(target=main)
