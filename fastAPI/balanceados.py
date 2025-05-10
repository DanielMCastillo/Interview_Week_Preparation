from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Expresion(BaseModel):
    cadena: str

@app.post("/balanceado/")
def parentesis_balanceados(exp: Expresion):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}
    for c in exp.cadena:
        if c in "([{":
            pila.append(c)
        elif c in ")]}":
            if not pila or pila[-1] != pares[c]:
                return {"balanceado": False}
            pila.pop()
    return {"balanceado": len(pila) == 0}
