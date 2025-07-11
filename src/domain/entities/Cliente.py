from uuid import uuid4
from enum import Enum


class TipoCliente(Enum):
    NUEVO = "nuevo"
    FRECUENTE = "frecuente"
    VIP = "vip"


class Cliente:
    def __init__(
        self, id: int, nombre: str, email: str, direccion: str, tipo: TipoCliente
    ):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.tipo = tipo
