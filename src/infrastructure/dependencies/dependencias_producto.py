from src.application.servicio_producto import ServicioProducto
from src.infrastructure.repositories.repositorio_producto_in_memory import (
    RepositorioProductoInMemory,
)
from src.infrastructure.repositories.repositorio_cliente_in_memory import (
    RepositorioClienteInMemory,
)
from src.infrastructure.repositories.repositorio_pedido_in_memory import (
    RepositorioPedidoInMemory,
)

# Este archivo sera para configuración de depencencias.
# Para producción, una organización puede usar una BD real,
# mietras que para pruebas una en memoria.

repo_productos = RepositorioProductoInMemory()
repo_cliente = RepositorioClienteInMemory()
repo_pedido = RepositorioPedidoInMemory()


def obtener_servicio_prodcuto() -> ServicioProducto:
    return ServicioProducto(repo_productos, repo_cliente, repo_pedido)
