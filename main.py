import asyncio
from cerebro import CerebroMau
from visualizador import VisualizadorMau
from narrador import NarradorMau

class Mau:
    def __init__(self):
        self.rotate = 0

async def main():
    mau = Mau()
    visual = VisualizadorMau(mau)
    narrador = NarradorMau()
    cerebro = CerebroMau(visual, narrador)

    print("--- Iniciando Mau ---")

    await cerebro.procesar("pon música")
    await cerebro.procesar("cuento")
    await cerebro.procesar("gimnasia")
    await cerebro.procesar("vocales")
    await visual.animar_flotacion()

if __name__ == "__main__":
    asyncio.run(main())
