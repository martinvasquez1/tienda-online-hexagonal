from dataclasses import dataclass
from ..entities.Producto import Producto


@dataclass
class ProductoPedido:
    producto: Producto
    cantidad_solicitada: int
    precio_unitario: float

    def subtotal(self) -> float:
        return self.cantidad_solicitada * self.precio_unitario

    def to_dict(self) -> dict:
        return {
            "id": self.producto.codigo,
            "nombre": self.producto.nombre,
            "cantidad": self.cantidad_solicitada,
            "precio_unitario": self.precio_unitario,
            "subtotal": self.subtotal(),
            "stock_disponible": self.producto.stock,
        }
