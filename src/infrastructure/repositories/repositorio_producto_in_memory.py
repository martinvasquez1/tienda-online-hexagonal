from typing import List, Optional

from src.domain.repositories.repositorio_producto import RepositorioProducto
from src.domain.entities.Producto import Producto


class RepositorioProductoInMemory(RepositorioProducto):
    def __init__(self):
        self.productos = []
        self.siguiente_id = 1

    def crear_producto(self, nombre: str, precio: float, stock: int) -> None:
        nuevo_producto = Producto(self.siguiente_id, nombre, precio, stock)
        self.productos.append(nuevo_producto)
        self.siguiente_id += 1

        return nuevo_producto

    def obtener_productos(self) -> List[Producto]:
        return self.productos

    def obtener_producto(self, id_producto) -> Optional[Producto]:
        producto = next((p for p in self.productos if p.id == id_producto), None)
        return producto

    def actualizar_producto(
        self,
        id: int,
        nombre: Optional[str],
        precio: Optional[float],
        stock: Optional[int],
    ) -> Optional[Producto]:
        producto = next((p for p in self.productos if p.id == id), None)

        if not producto:
            return None

        if nombre is not None:
            producto.nombre = nombre
        if precio is not None:
            producto.precio = precio
        if stock is not None:
            producto.stock = stock

        return producto

    def eliminar_producto(self, id_producto) -> Optional[Producto]:
        producto = next((p for p in self.productos if p.id == id_producto), None)

        if not producto:
            return None

        self.productos = [p for p in self.productos if p.id != id_producto]
        return producto
