from src.application.servicio_producto import ServicioProducto
from src.infrastructure.repositories.repositorio_producto_in_memory import (
    RepositorioProductoInMemory,
)

# Este archivo sera para configuración de depencencias.
# Para producción, una organización puede usar una BD real,
# mietras que para pruebas una en memoria.

repo = RepositorioProductoInMemory()


def obtener_servicio_prodcuto() -> ServicioProducto:
    return ServicioProducto(repo)
