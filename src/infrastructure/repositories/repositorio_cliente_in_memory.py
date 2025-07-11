from typing import List, Optional

from src.domain.repositories.repositorio_cliente import RepositorioCliente
from src.domain.entities.Cliente import Cliente, TipoCliente


class RepositorioClienteInMemory(RepositorioCliente):
    _instance = None

    def __init__(self):
        self.clientes = []
        self.siguiente_id = 1

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(RepositorioClienteInMemory, cls).__new__(cls)
        return cls._instance

    def agregar(
        self, nombre: str, email: str, direccion: str, tipo: TipoCliente
    ) -> Cliente:
        nuevo_cliente = Cliente(self.siguiente_id, nombre, email, direccion, tipo)
        self.clientes.append(nuevo_cliente)
        self.siguiente_id += 1

        return nuevo_cliente

    def obtener_clientes(self) -> List[Cliente]:
        return self.clientes

    def obtener(self, id_cliente) -> Optional[Cliente]:
        cliente = next(
            (cliente for cliente in self.clientes if cliente.id == id_cliente), None
        )
        return cliente

    def actualizar(
        self,
        id: int,
        nombre: Optional[str],
        email: Optional[str],
        direccion: Optional[str],
        tipo: Optional[TipoCliente],
    ) -> Optional[Cliente]:
        cliente = self.obtener(id)

        if cliente is None:
            return cliente

        if nombre is not None:
            cliente.nombre = nombre
        if email is not None:
            cliente.email = email
        if direccion is not None:
            cliente.direccion = direccion
        if tipo is not None:
            cliente.tipo = tipo

        return cliente

    def eliminar(self, id_cliente) -> None:
        cliente = self.obtener(id_cliente)

        if not cliente:
            return None

        self.productos = [c for c in self.productos if c.id != id_cliente]
        return cliente
