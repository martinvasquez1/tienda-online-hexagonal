from src.application.servicio_pedido import ServicioPedido
from src.infrastructure.repositories.repositorio_pedido_in_memory import (
    RepositorioPedidoInMemory,
)
from src.infrastructure.repositories.repositorio_cliente_in_memory import (
    RepositorioClienteInMemory,
)
from src.infrastructure.repositories.repositorio_producto_in_memory import (
    RepositorioProductoInMemory,
)

# Este archivo sera para configuración de depencencias.
# Para producción, una organización puede usar una BD real,
# mietras que para pruebas una en memoria.

repo_pedido = RepositorioPedidoInMemory()
repo_clientes = RepositorioClienteInMemory()
repo_productos = RepositorioProductoInMemory()


def obtener_servicio_pedido() -> ServicioPedido:
    return ServicioPedido(repo_pedido, repo_clientes, repo_productos)
