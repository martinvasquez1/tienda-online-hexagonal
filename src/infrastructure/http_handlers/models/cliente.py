from typing import Optional
from pydantic import BaseModel

from src.domain.entities.Cliente import TipoCliente


class CrearCliente(BaseModel):
    nombre: str
    email: str
    direccion: str
    tipo: TipoCliente = TipoCliente.NUEVO


class ActualizarCliente(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    direccion: Optional[str] = None
    tipo: Optional[TipoCliente] = None
