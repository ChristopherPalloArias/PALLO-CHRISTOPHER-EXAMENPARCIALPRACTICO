import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
genai_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def clasificar_mensaje(texto: str) -> str:
    prompt = f"""
    Necesito que clasifiques el siguiente mensaje en una de las siguientes categorias:
    - Urgente
    - Moderado
    - Normal
    Mensaje: "{texto}"
    
    Devuelve solo una palabra exacta como respuesta: Urgente, Moderado o Normal.
    """
    response = genai_client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text.strip()
