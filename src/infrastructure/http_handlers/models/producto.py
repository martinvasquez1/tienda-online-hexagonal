from pydantic import BaseModel
from typing import Any


class Producto(BaseModel):
    nombre: str
    precio: float
