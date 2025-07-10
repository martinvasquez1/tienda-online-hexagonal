from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.repositories.repositorio_pedido import RepositorioPedido
from src.domain.entities.Pedido import Pedido


class RepositorioPedidoInMemory(RepositorioPedido):
    def agregar(self, pedido: Pedido) -> None:
        return "Este método agregará un nuevo pedido al repositorio."

    def obtener(self, id_pedido) -> Optional[Pedido]:
        return "Este método obtendrá un pedido por su ID."

    def listar(self) -> List[Pedido]:
        return "Este método listará todos los pedidos en el repositorio."

    def actualizar(self, pedido: Pedido) -> None:
        return "Este método actualizará la información de un pedido existente."

    def eliminar(self, id_pedido) -> None:
        return "Este método eliminará un pedido del repositorio por su ID."
