import asyncio
import pygame
import math

class VisualizadorMau:
    def __init__(self, mau):
        self.mau = mau
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Mau.pro")
        self.font = pygame.font.SysFont("Arial", 72)
        self.clock = pygame.time.Clock()

    async def mostrar_estado(self, estado):
        print(f"[VISUALIZADOR] Mau está en modo {estado}")
        self.screen.fill((200, 255, 200))
        texto = self.font.render(estado, True, (0, 0, 0))
        self.screen.blit(texto, (300, 250))
        pygame.display.flip()
        await asyncio.sleep(1)

    async def ejecutar_movimiento(self, instruccion):
        print(f"[VISUALIZADOR] Mau ejecuta movimiento: {instruccion}")
        if "derecha" in instruccion.lower():
            await self.gesto_grande()
        else:
            await asyncio.sleep(1)

    async def mostrar_vocal(self, vocal):
        print(f"[VISUALIZADOR] Mostrando vocal: {vocal}")
        self.screen.fill((255, 255, 255))
        texto = self.font.render(vocal, True, (0, 128, 0))
        self.screen.blit(texto, (350, 250))
        pygame.display.flip()
        await asyncio.sleep(1)

    async def animar_flotacion(self):
        for i in range(40):
            y = 250 + (10 * math.sin(i/3))
            self.screen.fill((200, 255, 200))
            texto = self.font.render("Mau", True, (0, 0, 0))
            self.screen.blit(texto, (350, int(y)))
            pygame.display.flip()
            await asyncio.sleep(0.05)

    async def gesto_grande(self):
        print("[VISUALIZADOR] Mau hace gesto de GRANDE")
        self.screen.fill((255, 255, 255))
        texto = self.font.render("GRANDE", True, (0, 128, 0))
        self.screen.blit(texto, (250, 250))
        # Brazos extendidos como líneas
        pygame.draw.line(self.screen, (0, 200, 0), (320, 300), (250, 250), 8)
        pygame.draw.line(self.screen, (0, 200, 0), (480, 300), (550, 250), 8)
        pygame.display.flip()
        await asyncio.sleep(2)
