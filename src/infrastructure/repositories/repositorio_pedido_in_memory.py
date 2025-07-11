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

    def obtener_pedidos(self, cliente_id) -> List[Pedido]:
        pedidos_cliente = [pedido for p in self.pedidos if p.cliente_id == cliente_id]
        return pedidos_cliente

    def obtener_pedido(self, pedido_id) -> Optional[Pedido]:
        return next((p for p in self.pedidos if p.id == pedido_id), None)

    def actualizar_pedido(self, pedido: Pedido) -> None:
        return "Este método actualizará la información de un pedido existente."

    def eliminar_pedido(self, id_pedido) -> None:
        return "Este método eliminará un pedido del repositorio por su ID."
