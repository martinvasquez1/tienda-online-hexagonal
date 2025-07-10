from src.application.servicio_pedido_port import ServicioPedidoPort
from src.infrastructure.repositories.repositorio_pedido_in_memory import RepositorioPedidoInMemory

# Este archivo sera para configuración de depencencias.
# Para producción, una organización puede usar una BD real,
# mietras que para pruebas una en memoria.

repo = RepositorioPedidoInMemory()

def obtener_servicio_pedido() -> ServicioPedidoPort:
    return ServicioPedidoPort(repo)
~                                          