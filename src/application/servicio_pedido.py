from typing import List, Optional
from uuid import UUID

from src.application.servicio_pedido_port import ServicioPedidoPort
from src.domain.repositories.repositorio_pedido import RepositorioPedido
from src.domain.repositories.repositorio_cliente import RepositorioCliente
from src.domain.repositories.repositorio_producto import RepositorioProducto

from src.domain.entities.Pedido import Pedido

from src.infrastructure.http_handlers.exceptions.exceptions_cliente import (
    ClienteNoEncontrado,
)
from src.infrastructure.http_handlers.exceptions.exceptions_pedido import (
    PedidoNoEncontrado,
)


class ServicioPedido(ServicioPedidoPort):
    def __init__(
        self,
        repositorio_pedido: RepositorioPedido,
        repositorio_cliente: RepositorioCliente,
        repositorio_producto: RepositorioProducto,
    ):
        self.repositorio_pedido = repositorio_pedido
        self.repositorio_cliente = repositorio_cliente
        self.repositorio_producto = repositorio_producto

    def check_cliente(self, cliente_id):
        cliente = self.repositorio_cliente.obtener(cliente_id)
        if not cliente:
            raise ClienteNoEncontrado(f"Cliente con ID {cliente_id} no encontrado.")

    def check_pedido(self, pedido_id):
        pedido = self.repositorio_pedido.obtener_pedido(pedido_id)
        if not pedido:
            raise PedidoNoEncontrado(f"Pedido con ID {pedido_id} no encontrado.")

    def crear_pedido(self, cliente_id) -> Optional[Pedido]:
        self.check_cliente(cliente_id)
        nuevo_pedido = self.repositorio_pedido.crear_pedido(cliente_id)
        return nuevo_pedido

    def obtener_pedidos(self, cliente_id) -> List[Pedido]:
        self.check_cliente(cliente_id)

        pedidos = self.repositorio_pedido.obtener_pedidos(cliente_id)
        for pedido in pedidos:
            productos = self.repositorio_producto.obtener_productos(pedido.id)
            pedido.productos = productos

        return pedidos

    def obtener_pedido(self, cliente_id, pedido_id: str) -> Optional[Pedido]:
        self.check_cliente(cliente_id)
        self.check_pedido(pedido_id)

        pedido = self.repositorio_pedido.obtener_pedido(pedido_id)
        productos = self.repositorio_producto.obtener_productos(pedido_id)
        pedido.productos = productos

        return pedido

    def actualizar_pedido(self, id: str) -> Optional[Pedido]:
        return "Este método actualizara un pedido por su ID y devolverá el objeto Pedido si se encuentra."

    def eliminar_pedido(self, id: str) -> bool:
        return "Este método eliminará un pedido por su ID y devolverá True si se eliminó con éxito."
