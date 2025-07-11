from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from src.domain.entities.Pedido import Pedido


class ServicioPedidoPort(ABC):
    @abstractmethod
    def crear_pedido(self, cliente_id: str) -> Optional[Pedido]:
        """Registra un nuevo pedido y devuelve el objeto Pedido creado."""
        pass

    @abstractmethod
    def obtener_pedidos(self, cliente_id: str) -> List[Pedido]:
        """Devuelve una lista de todos los pedidos registrados."""
        pass

    @abstractmethod
    def obtener_pedido(self, cliente_id: str, pedido_id: str) -> Optional[Pedido]:
        """Busca un pedido por su ID y devuelve el objeto Pedido si se encuentra."""
        pass

    @abstractmethod
    def actualizar_pedido(self, id: str) -> Optional[Pedido]:
        """Actualiza un pedido por su ID y devuelve el objeto Pedido si se encuentra."""
        pass

    @abstractmethod
    def eliminar_pedido(self, id: str) -> bool:
        """Elimina un pedido por su ID y devuelve True si se eliminó con éxito."""
        pass
