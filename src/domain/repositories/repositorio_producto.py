from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities import Producto


class RepositorioProducto(ABC):
    @abstractmethod
    def agregar(self, producto: Producto) -> None:
        """Agrega un nuevo producto al repositorio."""
        pass

    @abstractmethod
    def obtener(self, id_producto) -> Optional[Producto]:
        """Obtiene un producto por su ID."""
        pass

    @abstractmethod
    def listar(self) -> List[Producto]:
        """Lista todos los productos en el repositorio."""
        pass

    @abstractmethod
    def actualizar(self, producto: Producto) -> None:
        """Actualiza la información de un producto existente."""
        pass

    @abstractmethod
    def eliminar(self, id_producto) -> None:
        """Elimina un producto del repositorio por su ID."""
        pass
