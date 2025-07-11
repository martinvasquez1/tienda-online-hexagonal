from typing import List, Optional

from src.application.servicio_producto_port import ServicioProductoPort
from src.domain.repositories.repositorio_producto import RepositorioProducto
from src.domain.entities.Producto import Producto


class ServicioProducto(ServicioProductoPort):
    def __init__(self, repositorio_producto: RepositorioProducto):
        self.repositorio_producto = repositorio_producto

    def crear_producto(self, nombre: str, precio: float) -> Optional[Producto]:
        nuevo_producto = self.repositorio_producto.crear_producto(nombre, precio)
        return nuevo_producto

    def obtener_productos(self) -> List[Producto]:
        productos = self.repositorio_producto.obtener_productos()
        return productos

    def obtener_producto(self, id: int) -> Optional[Producto]:
        producto = self.repositorio_producto.obtener_producto(id)
        return producto

    def actualizar_producto(
        self, id: int, nombre: Optional[str], precio: Optional[float]
    ):
        producto_actualizado = self.repositorio_producto.actualizar_producto(
            id, nombre, precio
        )
        return producto_actualizado

    def eliminar_producto(self, id: int) -> Optional[Producto]:
        producto_eliminado = self.repositorio_producto.eliminar_producto(id)
        return producto_eliminado
