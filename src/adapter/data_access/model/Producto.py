from pydantic import BaseModel


class Producto(BaseModel):
    codigo: int
    nombre: str
    precio: float
