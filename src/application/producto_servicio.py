from typing import List, Optional

from src.domain.entities.producto import Producto
from src.application.producto_servicio_port import ProductoServiceBase
from src.domain.repositories.repositorio_producto import RepositorioProducto


class ProductoServicio(ProductoServiceBase):
    def __init__(self, repositorio_producto: RepositorioProducto):
        self.repositorio_producto = repositorio_producto

    def registrar_producto(self, precio: float) -> Optional[Producto]:
        return "Este método registrará un nuevo producto y devolverá el objeto Producto creado."

    def listar_todos_los_productos(self) -> List[Producto]:
        return "Este método devolverá una lista de todos los productos registrados."

    def buscar_producto_por_id(self, id: int) -> Optional[Producto]:
        return "Este método buscará un producto por su ID y devolverá el objeto Producto si se encuentra."

    def eliminar_producto(self, id: int) -> bool:
        return "Este método eliminará un producto por su ID y devolverá True si se eliminó con éxito."
