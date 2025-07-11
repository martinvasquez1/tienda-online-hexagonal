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

    def buscar_producto_por_id(self, id: int) -> Optional[Producto]:
        return "Este método buscará un producto por su ID y devolverá el objeto Producto si se encuentra."

    def eliminar_producto(self, id: int) -> bool:
        return "Este método eliminará un producto por su ID y devolverá True si se eliminó con éxito."
