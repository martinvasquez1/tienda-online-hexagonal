from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.Producto import Producto


class ServicioProductoPort(ABC):
    @abstractmethod
    def crear_producto(
        cliente_id: int, pedido_id: int, self, nombre: str, precio: float, stock: int
    ) -> Optional[Producto]:
        """Registra un nuevo producto y devuelve el objeto Producto creado."""
        pass

    @abstractmethod
    def obtener_productos(self) -> List[Producto]:
        """Devuelve una lista de todos los productos registrados."""
        pass

    @abstractmethod
    def obtener_producto(self, id: int) -> Optional[Producto]:
        """Busca un producto por su ID y devuelve el objeto Producto si se encuentra."""
        pass

    @abstractmethod
    def actualizar_producto(
        self,
        id: int,
        nombre: Optional[str],
        precio: Optional[float],
        stock: Optional[int],
    ) -> Optional[Producto]:
        """Actualiza un producto por su ID y devuelve el objeto Producto si existe."""
        pass

    @abstractmethod
    def eliminar_producto(self, id: int) -> Optional[Producto]:
        """Elimina un producto por su ID y devuelve el producto si se eliminó con éxito."""
        pass
