from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.repositories.repositorio_pedido import RepositorioPedido
from src.domain.entities.Pedido import Pedido, PedidoEstandar


class RepositorioPedidoInMemory(RepositorioPedido):
    def __init__(self):
        self.pedidos = []
        self.siguiente_id = 1

    def crear_pedido(self, cliente_id: str) -> Optional[Pedido]:
        nuevo_pedido = PedidoEstandar(self.siguiente_id, cliente_id)
        return nuevo_pedido

    def obtener_pedidos(self) -> List[Pedido]:
        return "Este método listará todos los pedidos en el repositorio."

    def obtener_pedido(self, id_pedido) -> Optional[Pedido]:
        return "Este método obtendrá un pedido por su ID."

    def actualizar_pedido(self, pedido: Pedido) -> None:
        return "Este método actualizará la información de un pedido existente."

    def eliminar_pedido(self, id_pedido) -> None:
        return "Este método eliminará un pedido del repositorio por su ID."
