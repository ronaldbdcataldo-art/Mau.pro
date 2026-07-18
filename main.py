import flecha as pie
from centro.llm_manager import GerenteDeLLM
from centro.administrador_de_voz import AdministradorDeVoz

# --- CONFIGURACIÓN Y CONSTANTES ---
# Centralizamos aquí los valores para no tener que buscar dentro del código después
COLOR_PRINCIPAL = "naranja"
TAMANO_ICONO = 150
TAMANO_TEXTO = 30

async def principal(página: pie.Page):
    # Configuración de la página
    página.título = 'Proyecto Mau'
    página.alineación_vertical = pie.Alineación_del_eje_principal.CENTRO
    página.alineación_horizontal = pie.Alineación_de_ejes_cruzados.CENTRO
    página.modo_tema = pie.Modo_de_tema.LUZ

    # Renderizado de la interfaz
    página.agregar(
        pie.Icono("rostro", tamaño=TAMANO_ICONO, color=COLOR_PRINCIPAL),
        pie.Texto('¡Hola! Soy Mau, tu amigo.', tamaño=TAMANO_TEXTO, peso=pie.Peso_de_fuente.BOLD)
    )

    # Inicialización de servicios
    # Al estar aquí, la UI carga primero y luego se preparan los servicios
    llm = GerenteDeLLM()
    voz = AdministradorDeVoz()
    
    imprimir('Sistema Mau: Interfaz y servicios listos.')

# Punto de entrada
pie.aplicación(objetivo=principal)
