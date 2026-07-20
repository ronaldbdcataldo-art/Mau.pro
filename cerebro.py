import asyncio

class CerebroMau:
    def __init__(self, visualizador, narrador):
        self.visualizador = visualizador
        self.narrador = narrador
        self.modo = "REPOSO"

    async def cambiar_modo(self, nuevo_modo):
        print(f"[CEREBRO] Cambiando a modo {nuevo_modo}")
        self.modo = nuevo_modo
        await self.visualizador.mostrar_estado(nuevo_modo)

    async def contar_cuento(self, texto):
        print("[CEREBRO] Mau está contando un cuento...")
        if self.narrador:
            await self.narrador.narrar(texto)

    async def gimnasia(self, instruccion):
        print(f"[CEREBRO] Mau escucha: {instruccion}")
        await asyncio.sleep(2)  # tiempo para que los niños actúen
        await self.visualizador.ejecutar_movimiento(instruccion)

    async def enseñar_vocales(self):
        vocales = ["A", "E", "I", "O", "U"]
        for v in vocales:
            await self.visualizador.mostrar_vocal(v)
            await asyncio.sleep(1)

    async def procesar(self, instruccion):
        if "música" in instruccion.lower():
            await self.cambiar_modo("MUSICA")
        elif "cuento" in instruccion.lower():
            await self.contar_cuento("Había una vez un pez dorado que flotaba en el lago...")
        elif "gimnasia" in instruccion.lower():
            await self.gimnasia("Giren a la derecha")
        elif "vocales" in instruccion.lower():
            await self.enseñar_vocales()
        else:
            print("[CEREBRO] Instrucción no reconocida:", instruccion)
