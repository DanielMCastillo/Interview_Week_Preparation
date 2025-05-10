#API Palindromo
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Texto(BaseModel):
    contenido:str

@app.post("/es-palindromo/")
def es_palindromo(data:Texto):
    limpio = ''.join(c for c in data.contenido if c.isalnum()).lower()
    return {"resultado": limpio == limpio[::-1]}

