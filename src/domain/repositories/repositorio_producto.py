from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.Producto import Producto


class RepositorioProducto(ABC):
    @abstractmethod
    def crear_producto(self, pedido_id: int, nombre: str, precio: float) -> None:
        """Agrega un nuevo producto al repositorio."""
        pass

    @abstractmethod
    def obtener_productos(self, pedido_id: int) -> List[Producto]:
        """Lista todos los productos en el repositorio."""
        pass
