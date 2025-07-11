from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.Pedido import Pedido


class RepositorioPedido(ABC):
    @abstractmethod
    def crear_pedido(self, cliente_id) -> Optional[Pedido]:
        """Agrega un nuevo pedido al repositorio."""
        pass

    @abstractmethod
    def obtener_pedidos(self) -> List[Pedido]:
        """Lista todos los pedidos en el repositorio."""
        pass

    @abstractmethod
    def obtener_pedido(self, id_pedido) -> Optional[Pedido]:
        """Obtiene un pedido por su ID."""
        pass

    @abstractmethod
    def actualizar_pedido(self, pedido: Pedido) -> None:
        """Actualiza la información de un pedido existente."""
        pass

    @abstractmethod
    def eliminar_pedido(self, id_pedido) -> None:
        """Elimina un pedido del repositorio por su ID."""
        pass
