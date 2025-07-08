from uuid import uuid4
from enum import Enum


class TipoCliente(Enum):
    NUEVO = "nuevo"
    FRECUENTE = "frecuente"
    VIP = "vip"


class Cliente:
    def __init__(self, nombre: str, email: str, direccion: str, tipo: TipoCliente):
        self.id = uuid4()
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.tipo = tipo
