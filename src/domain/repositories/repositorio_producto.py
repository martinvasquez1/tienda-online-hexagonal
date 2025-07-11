from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.Producto import Producto


class RepositorioProducto(ABC):
    @abstractmethod
    def crear_producto(self, nombre: str, precio: float) -> None:
        """Agrega un nuevo producto al repositorio."""
        pass

    @abstractmethod
    def obtener_productos(self) -> List[Producto]:
        """Lista todos los productos en el repositorio."""
        pass

    @abstractmethod
    def obtener_producto(self, id_producto) -> Optional[Producto]:
        """Obtiene un producto por su ID."""
        pass

    @abstractmethod
    def actualizar_producto(
        self, id: int, nombre: Optional[str], precio: Optional[float]
    ) -> Optional[Producto]:
        """Actualiza la información de un producto existente."""
        pass

    @abstractmethod
    def eliminar_producto(self, id_producto) -> Optional[Producto]:
        """Elimina un producto del repositorio por su ID."""
        pass
