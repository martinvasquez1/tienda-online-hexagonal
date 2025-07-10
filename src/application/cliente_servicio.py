from typing import List, Optional

from src.application.cliente_servicio_port import ClienteServiceBase
from src.domain.entities.Cliente import Cliente, TipoCliente
from src.domain.repositories.repositorio_cliente import RepositorioCliente


class ClienteServicio(ClienteServiceBase):
    def __init__(self, repositorio_cliente: RepositorioCliente):
        self.repositorio_cliente = repositorio_cliente

    def registrar_cliente(
        self, nombre: str, email: str, direccion: str, tipo: TipoCliente
    ) -> Optional[Cliente]:
        return "Este método registrará un nuevo cliente y devolverá el objeto Cliente creado."

    def listar_todos_los_clientes(self) -> List[Cliente]:
        return "Este método devolverá una lista de todos los clientes registrados."

    def buscar_cliente_por_id(self, id) -> Optional[Cliente]:
        return "Este método buscará un cliente por su ID y devolverá el objeto Cliente si se encuentra."

    def eliminar_cliente(self, id) -> bool:
        return "Este método eliminará un cliente por su ID y devolverá True si se eliminó con éxito."
