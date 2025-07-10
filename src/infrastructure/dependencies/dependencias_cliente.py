from src.application.servicio_cliente_port import ServicioClientePort
from src.infrastructure.repositories.repositorio_cliente_in_memory import (
    RepositorioClienteInMemory,
)

# Este archivo sera para configuración de depencencias.
# Para producción, una organización puede usar una BD real,
# mietras que para pruebas una en memoria.

repo = RepositorioClienteInMemory()


def obtener_servicio_cliente() -> ServicioClientePort:
    return ServicioClientePort(repo)
