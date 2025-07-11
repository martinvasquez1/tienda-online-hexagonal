from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.Cliente import Cliente, TipoCliente


class ServicioClientePort(ABC):
    @abstractmethod
    def registrar_cliente(
        self, nombre: str, email: str, direccion: str, tipo: TipoCliente
    ) -> Optional[Cliente]:
        """Registra un nuevo cliente y devuelve el objeto Cliente creado."""
        pass

    @abstractmethod
    def obtener_clientes(self) -> List[Cliente]:
        """Devuelve una lista de todos los clientes registrados."""
        pass

    @abstractmethod
    def obtener(self, id) -> Optional[Cliente]:
        """Busca un cliente por su ID y devuelve el objeto Cliente si se encuentra."""
        pass

    @abstractmethod
    def actualizar(
        self,
        id: int,
        nombre: Optional[str],
        email: Optional[str],
        direccion: Optional[str],
        tipo: Optional[TipoCliente],
    ) -> Optional[Cliente]:
        """Actualiza los datos de un cliente"""
        pass

    @abstractmethod
    def eliminar_cliente(self, id) -> bool:
        """Elimina un cliente por su ID y devuelve True si se eliminó con éxito."""
        pass
