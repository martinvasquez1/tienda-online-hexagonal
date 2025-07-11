from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.repositories.repositorio_cliente import RepositorioCliente
from src.domain.entities.Cliente import Cliente, TipoCliente


class RepositorioClienteInMemory(RepositorioCliente):
    def __init__(self):
        self.clientes = []
        self.siguiente_id = 1

    def agregar(self, cliente: Cliente) -> None:
        nuevo_cliente = Cliente()
        self.clientes.append(nuevo_cliente)
        self.siguiente_id += 1

        return nuevo_cliente

    def obtener_clientes(self) -> List[Cliente]:
        return self.clientes

    def obtener(self, id_cliente) -> Optional[Cliente]:
        cliente = next((c for c in self.clientes if c.id == id_cliente), None)
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
        return "Este método eliminará un cliente del repositorio por su ID."
