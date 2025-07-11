from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.repositories.repositorio_pedido import RepositorioPedido
from src.domain.entities.Pedido import Pedido, PedidoEstandar
from src.infrastructure.repositories.decorators import singleton


@singleton
class RepositorioPedidoInMemory(RepositorioPedido):
    def __init__(self):
        self.pedidos = []
        self.siguiente_id = 1

    def crear_pedido(self) -> Optional[Pedido]:
        # TODO: Dependiendo del tipo de usuario instanciar una clase distinta.
        # De momento se retornara un usuario estandar.
        nuevo_pedido = PedidoEstandar(self.siguiente_id)
        return nuevo_pedido

    def obtener_pedidos(self) -> List[Pedido]:
        return "Este método listará todos los pedidos en el repositorio."

    def obtener_pedido(self, id_pedido) -> Optional[Pedido]:
        return "Este método obtendrá un pedido por su ID."

    def actualizar_pedido(self, pedido: Pedido) -> None:
        return "Este método actualizará la información de un pedido existente."

    def eliminar_pedido(self, id_pedido) -> None:
        return "Este método eliminará un pedido del repositorio por su ID."
