from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.repositories.repositorio_producto import RepositorioProducto
from src.domain.entities.Producto import Producto


class RepositorioProductoInMemory(RepositorioProducto):
    def agregar(self, producto: Producto) -> None:
        return "Este método agregará un nuevo producto al repositorio."

    def obtener(self, id_producto) -> Optional[Producto]:
        return "Este método obtendrá un producto por su ID."

    def listar(self) -> List[Producto]:
        return "Este método listará todos los productos en el repositorio."

    def actualizar(self, producto: Producto) -> None:
        return "Este método actualizará la información de un producto existente."

    def eliminar(self, id_producto) -> None:
        return "Este método eliminará un producto del repositorio por su ID."
