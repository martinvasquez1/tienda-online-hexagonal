from pydantic import BaseModel
from typing import Any


class CrearProducto(BaseModel):
    nombre: str
    precio: float


class ActualizarProducto(BaseModel):
    id: int
    nombre: str
    precio: float
