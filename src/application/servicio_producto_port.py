from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.Producto import Producto


class ServicioProductoPort(ABC):
    @abstractmethod
    def crear_producto(
        self,
        cliente_id: int,
        pedido_id: int,
        nombre: str,
        precio: float,
        stock: int,
    ) -> Optional[Producto]:
        """Registra un nuevo producto y devuelve el objeto Producto creado."""
        pass

    @abstractmethod
    def obtener_productos(self, cliente_id, pedido_id) -> List[Producto]:
        """Devuelve una lista de todos los productos registrados."""
        pass
