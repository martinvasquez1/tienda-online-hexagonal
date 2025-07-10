from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.Pedido import Pedido


class PedidoServiceBase(ABC):
    @abstractmethod
    def registrar_pedido(self, productos) -> Optional[Pedido]:
        """Registra un nuevo pedido y devuelve el objeto Pedido creado."""
        pass

    @abstractmethod
    def listar_todos_los_pedidos(self) -> List[Pedido]:
        """Devuelve una lista de todos los pedidos registrados."""
        pass

    @abstractmethod
    def buscar_pedido_por_id(self, id: UUID) -> Optional[Pedido]:
        """Busca un pedido por su ID y devuelve el objeto Pedido si se encuentra."""
        pass

    @abstractmethod
    def eliminar_pedido(self, id: UUID) -> bool:
        """Elimina un pedido por su ID y devuelve True si se eliminó con éxito."""
        pass
