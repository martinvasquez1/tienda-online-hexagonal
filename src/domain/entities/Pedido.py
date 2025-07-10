from abc import ABC, abstractmethod
from uuid import uuid4
from enum import Enum


class EstadoPedido(Enum):
    PENDIENTE = "pendiente"
    PAGADO = "pagado"
    EN_PREPARACION = "en preparación"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"


class Pedido(ABC):
    def __init__(self, productos):
        self.id = uuid4()
        self.estado = EstadoPedido.EN_PREPARACION
        self.productos = productos
        self.precio_estandar = 10
        self.fecha = None
