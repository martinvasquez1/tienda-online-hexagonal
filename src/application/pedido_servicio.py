from typing import List, Optional
from uuid import UUID

from src.application.pedido_servicio_port import PedidoServiceBase
from src.domain.repositories.repositorio_pedido import RepositorioPedido
from src.domain.entities.Pedido import Pedido


class PedidoServicio(PedidoServiceBase):
    def __init__(self, repositorio_pedido: RepositorioPedido):
        self.repositorio_pedido = repositorio_pedido

    def registrar_pedido(self, productos) -> Optional[Pedido]:
        return "Este método registrará un nuevo pedido y devolverá el objeto Pedido creado."

    def listar_todos_los_pedidos(self) -> List[Pedido]:
        return "Este método devolverá una lista de todos los pedidos registrados."

    def buscar_pedido_por_id(self, id: UUID) -> Optional[Pedido]:
        return "Este método buscará un pedido por su ID y devolverá el objeto Pedido si se encuentra."

    def eliminar_pedido(self, id: UUID) -> bool:
        return "Este método eliminará un pedido por su ID y devolverá True si se eliminó con éxito."
