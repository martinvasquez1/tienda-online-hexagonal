from .entity import Cliente


class IRepositorioCliente(ABC):
    @abstractmethod
    def agregar(self, cliente: Cliente) -> None:
        """Agrega un nuevo cliente al repositorio."""
        pass

    @abstractmethod
    def obtener(self, id_cliente) -> Optional[Cliente]:
        """Obtiene un cliente por su ID."""
        pass

    @abstractmethod
    def listar(self) -> List[Cliente]:
        """Lista todos los clientes en el repositorio."""
        pass

    @abstractmethod
    def actualizar(self, cliente: Cliente) -> None:
        """Actualiza la información de un cliente existente."""
        pass

    @abstractmethod
    def eliminar(self, id_cliente) -> None:
        """Elimina un cliente del repositorio por su ID."""
        pass
