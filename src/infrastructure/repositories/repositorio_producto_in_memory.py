from typing import List, Optional

from src.domain.repositories.repositorio_producto import RepositorioProducto
from src.domain.entities.Producto import Producto


class RepositorioProductoInMemory(RepositorioProducto):
    _instance = None

    def __init__(self):
        self.productos = []
        self.siguiente_id = 1

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(RepositorioProductoInMemory, cls).__new__(cls)
        return cls._instance

    def crear_producto(
        self, pedido_id: int, nombre: str, precio: float, stock: int
    ) -> None:
        nuevo_producto = Producto(self.siguiente_id, pedido_id, nombre, precio, stock)
        self.productos.append(nuevo_producto)
        self.siguiente_id += 1

        return nuevo_producto

    def obtener_productos(self, pedido_id: int) -> List[Producto]:
        return [p for p in self.productos if p.pedido_id == pedido_id]
