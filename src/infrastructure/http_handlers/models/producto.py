from pydantic import BaseModel
from typing import Any, Optional


class CrearProducto(BaseModel):
    nombre: str
    precio: float


class ActualizarProducto(BaseModel):
    nombre: Optional[str] = None
    precio: Optional[float] = None
