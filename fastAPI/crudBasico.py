from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float

productos: List[Producto] = []

@app.post("/productos/")
def agregar_producto(p: Producto):
    productos.append(p)
    return {"mensaje": "Producto agregado"}

@app.get("/productos/")
def listar_productos():
    return productos

@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    for p in productos:
        if p.id == id:
            productos.remove(p)
            return {"mensaje": "Producto eliminado"}
    raise HTTPException(status_code=404, detail="Producto no encontrado")
