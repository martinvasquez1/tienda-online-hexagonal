from typing import List, Optional
from uuid import UUID

from src.application.servicio_pedido_port import ServicioPedidoPort
from src.domain.repositories.repositorio_pedido import RepositorioPedido
from src.domain.entities.Pedido import Pedido


class ServicioPedido(ServicioPedidoPort):
    def __init__(self, repositorio_pedido: RepositorioPedido):
        self.repositorio_pedido = repositorio_pedido

    def crear_pedido(self, usuario_id) -> Optional[Pedido]:
        nuevo_pedido = self.repositorio_pedido.crear_pedido()
        # TOOD: Hacer que el usuario tengo un pedido. Actualmente la clase Cliente
        # no esta completada

        return nuevo_pedido

    def obtener_pedidos(self) -> List[Pedido]:
        return "Este método devolverá una lista de todos los pedidos registrados."

    def obtener_pedido(self, id: str) -> Optional[Pedido]:
        return "Este método buscará un pedido por su ID y devolverá el objeto Pedido si se encuentra."

    def actualizar_pedido(self, id: str) -> Optional[Pedido]:
        return "Este método actualizara un pedido por su ID y devolverá el objeto Pedido si se encuentra."

    def eliminar_pedido(self, id: str) -> bool:
        return "Este método eliminará un pedido por su ID y devolverá True si se eliminó con éxito."
