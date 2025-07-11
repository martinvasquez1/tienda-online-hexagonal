from typing import List, Optional

from src.application.servicio_cliente_port import ServicioClientePort
from src.domain.entities.Cliente import Cliente, TipoCliente
from src.domain.repositories.repositorio_cliente import RepositorioCliente


class ServicioCliente(ServicioClientePort):
    def __init__(self, repositorio_cliente: RepositorioCliente):
        self.repositorio_cliente = repositorio_cliente

    def registrar_cliente(
        self, nombre: str, email: str, direccion: str, tipo: TipoCliente
    ) -> Optional[Cliente]:
        nuevo_cliente = self.repositorio_cliente.agregar
        return nuevo_cliente

    def obtener_clientes(self) -> List[Cliente]:
        clientes = self.repositorio_cliente.obtener_clientes()
        return clientes

    def obtener(self, id) -> Optional[Cliente]:
        cliente = self.repositorio_cliente.obtener(id)
        return cliente

    def actualizar(
        self,
        id: int,
        nombre: Optional[str],
        email: Optional[str],
        direccion: Optional[str],
        tipo: Optional[TipoCliente],
    ) -> Optional[Cliente]:
        cliente = self.repositorio_cliente.actualizar(
            id, nombre, email, direccion, tipo
        )
        return cliente

    def eliminar_cliente(self, id) -> bool:
        fueEliminado = self.repositorio_cliente.eliminar(id)
        return fueEliminado
