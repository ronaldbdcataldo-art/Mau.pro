class CerebroMau:
    def __init__(self, visualizador, llm):
        self.visual = visualizador
        self.llm = llm
        self.modo = "TUTOR" 

    async def procesar(self, entrada):
        if self.modo == "MUSICA":
            await self.visual.bailar()
            return "¡Estoy bailando!"
        
        elif self.modo == "OBSERVADOR":
            accion = await self.llm.generar_respuesta("OBSERVADOR", entrada)
            self.visual.ejecutar_accion(accion)
            return None
        
        else: # TUTOR
            return await self.llm.generar_respuesta("TUTOR", entrada)