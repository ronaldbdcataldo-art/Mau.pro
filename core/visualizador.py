import asyncio

class VisualizadorMau:
    def __init__(self, contenedor):
        self.mau = contenedor

    async def bailar(self):
        # Efecto de baile: rotación rítmica
        for _ in range(10):
            self.mau.rotate = 0.2
            self.mau.update()
            await asyncio.sleep(0.3)
            self.mau.rotate = -0.2
            self.mau.update()
            await asyncio.sleep(0.3)
        self.mau.rotate = 0
        self.mau.update()

    def ejecutar_accion(self, accion):
        if "gesto_feliz" in accion:
            self.mau.content.color = "naranja"
        elif "gesto_triste" in accion:
            self.mau.content.color = "azul"
        self.mau.update()