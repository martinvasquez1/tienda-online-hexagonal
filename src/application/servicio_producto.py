from typing import List, Optional

from src.application.servicio_producto_port import ServicioProductoPort
from src.domain.repositories.repositorio_cliente import RepositorioCliente
from src.domain.repositories.repositorio_pedido import RepositorioPedido
from src.domain.repositories.repositorio_producto import RepositorioProducto
from src.domain.entities.Producto import Producto

from src.infrastructure.http_handlers.exceptions.exceptions_cliente import (
    ClienteNoEncontrado,
)
from src.infrastructure.http_handlers.exceptions.exceptions_pedido import (
    PedidoNoEncontrado,
)


class ServicioProducto(ServicioProductoPort):
    def __init__(
        self,
        repositorio_producto: RepositorioProducto,
        repositorio_cliente: RepositorioCliente,
        repositorio_pedido: RepositorioPedido,
    ):
        self.repositorio_producto = repositorio_producto
        self.repositorio_cliente = repositorio_cliente
        self.repositorio_pedido = repositorio_pedido

    def check_cliente(self, cliente_id):
        cliente = self.repositorio_cliente.obtener(cliente_id)
        if not cliente:
            raise ClienteNoEncontrado(f"Cliente con ID {cliente_id} no encontrado.")

    def check_pedido(self, pedido_id):
        pedido = self.repositorio_pedido.obtener_pedido(pedido_id)
        if not pedido:
            raise PedidoNoEncontrado(f"Pedido con ID {pedido_id} no encontrado.")

    def crear_producto(
        self, cliente_id: int, pedido_id: int, nombre: str, precio: float, stock: int
    ) -> Optional[Producto]:
        self.check_cliente(cliente_id)
        self.check_pedido(pedido_id)

        nuevo_producto = self.repositorio_producto.crear_producto(
            pedido_id, nombre, precio, stock
        )
        return nuevo_producto

    def obtener_productos(self, cliente_id, pedido_id) -> List[Producto]:
        self.check_cliente(cliente_id)
        self.check_pedido(pedido_id)

        productos = self.repositorio_producto.obtener_productos(pedido_id)
        return productos
