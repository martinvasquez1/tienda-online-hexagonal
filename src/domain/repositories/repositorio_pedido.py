from ..entities import Pedido


class RepositorioPedido(ABC):
    @abstractmethod
    def agregar(self, pedido: Pedido) -> None:
        """Agrega un nuevo pedido al repositorio."""
        pass

    @abstractmethod
    def obtener(self, id_pedido) -> Optional[Pedido]:
        """Obtiene un pedido por su ID."""
        pass

    @abstractmethod
    def listar(self) -> List[Pedido]:
        """Lista todos los pedidos en el repositorio."""
        pass

    @abstractmethod
    def actualizar(self, pedido: Pedido) -> None:
        """Actualiza la información de un pedido existente."""
        pass

    @abstractmethod
    def eliminar(self, id_pedido) -> None:
        """Elimina un pedido del repositorio por su ID."""
        pass
