from fastapi import FastAPI
from pydantic import BaseModel
from classifier_service import clasificar_mensaje
app = FastAPI(title="Clasificador Automatizado de Mensajes - Pallo Christopher - Decimo Semestre")

class MensajeEntrada(BaseModel):
    texto: str

@app.get("/")
async def root():
    return {"message": "Clasificador de Mensajes con IA (Gemini)"}

@app.post("/clasificar")
def clasificar(mensaje: MensajeEntrada):
    categoria = clasificar_mensaje(mensaje.texto)
    return {
        "mensaje": mensaje.texto,
        "clasificacion": categoria
    }
