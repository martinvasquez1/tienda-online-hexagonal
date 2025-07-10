from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.Producto import Producto


class ServicioProductoPort(ABC):
    @abstractmethod
    def registrar_producto(self, precio: float) -> Optional[Producto]:
        """Registra un nuevo producto y devuelve el objeto Producto creado."""
        pass

    @abstractmethod
    def listar_todos_los_productos(self) -> List[Producto]:
        """Devuelve una lista de todos los productos registrados."""
        pass

    @abstractmethod
    def buscar_producto_por_id(self, id: int) -> Optional[Producto]:
        """Busca un producto por su ID y devuelve el objeto Producto si se encuentra."""
        pass

    @abstractmethod
    def eliminar_producto(self, id: int) -> bool:
        """Elimina un producto por su ID y devuelve True si se eliminó con éxito."""
        pass
