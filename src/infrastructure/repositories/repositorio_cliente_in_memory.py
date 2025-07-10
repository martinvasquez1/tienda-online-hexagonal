from src.domain.repositories.repositorio_cliente import RepositorioCliente
from src.domain.entities.Cliente import Cliente


class RepositorioClienteInMemory(RepositorioCliente):
    def agregar(self, cliente: Cliente) -> None:
        return "Este método agregará un nuevo cliente al repositorio."

    def obtener(self, id_cliente) -> Optional[Cliente]:
        return "Este método obtendrá un cliente por su ID."

    def listar(self) -> List[Cliente]:
        return "Este método listará todos los clientes en el repositorio."

    def actualizar(self, cliente: Cliente) -> None:
        return "Este método actualizará la información de un cliente existente."

    def eliminar(self, id_cliente) -> None:
        return "Este método eliminará un cliente del repositorio por su ID."
