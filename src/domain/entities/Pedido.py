from typing import List
from uuid import uuid4
from enum import Enum
from datetime import datetime, timedelta

from src.domain.entities.Cliente import Cliente, TipoCliente
from src.domain.entities.MetodoDePago import MetodoDePago
from src.domain.entities.Producto import Producto
from src.domain.service.estrategias_descuento import EstrategiaDescuento
from src.domain.service.factory_descuento import FactoryDescuento
from src.domain.value_objects.producto_pedido import ProductoPedido


class EstadoPedido(Enum):
    PENDIENTE = "pendiente"
    PAGADO = "pagado"
    EN_PREPARACION = "en_preparación"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"


class TipoPedido(Enum):
    ESTANDAR = "estandar"
    EXPRESS = "express"
    PROGRAMADO = "programado"
    INTERNACIONAL = "internacional"


class Pedido:
    def __init__(self, id, cliente_id: str, tipo: TipoPedido):
        self.id = id
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.estado = EstadoPedido.PENDIENTE
        self.items: List[ProductoPedido] = []
        self.fecha = datetime.now()
        self.fecha_entrega = None

        self.precio_estandar = self._obtener_precio_estandar()
        self.cargo_adicional = self._obtener_cargo_adicional()
        self.impuestos_aduaneros = self._obtener_impuesto_aduaneros()

    def _obtener_precio_estandar(self) -> float:
        return 100.0

    def _obtener_cargo_adicional(self) -> float:
        cargos = {
            TipoPedido.ESTANDAR: 0.0,
            TipoPedido.EXPRESS: 20.0,
            TipoPedido.PROGRAMADO: 0.0,
            TipoPedido.INTERNACIONAL: 0.0,
        }
        return cargos.get(self.tipo, 0.0)

    def _obtener_impuesto_aduaneros(self) -> float:
        if self.tipo == TipoPedido.INTERNACIONAL:
            return 100.0
        return 0.0

    def _precio_productos(self):
        return sum(item.subtotal() for item in self.items)

    def _obtener_estrategia_descuento(
        self, tipo_cliente: TipoCliente
    ) -> EstrategiaDescuento:
        return FactoryDescuento.crear_estrategia(tipo_cliente)

    def calcular_descuento(self, cliente: Cliente) -> tuple[float, float]:
        subtotal = self._precio_productos()
        estrategia = self._obtener_estrategia_descuento(cliente.tipo)

        monto_descuento = estrategia.calcular_descuento(subtotal)
        porcentaje_descuento = estrategia.get_porcentaje_descuento()

        return monto_descuento, porcentaje_descuento

    def tiene_envio_gratis(self, cliente: Cliente) -> bool:
        estrategia = self._obtener_estrategia_descuento(cliente.tipo)
        return estrategia.tiene_envio_gratis()

    def agregar_producto(self, producto: Producto, cantidad: int):
        if producto.stock < cantidad:
            raise ValueError(
                f"Stock insuficiente para {producto.nombre}. "
                f"Disponible: {producto.stock}. Pedido: {cantidad}."
            )

        item_existente = self.buscar_item_por_producto_id(producto.id)
        if item_existente:
            cantidad_nueva = item_existente.cantidad_solicitada + cantidad
            if producto.stock < cantidad_nueva:
                raise ValueError(
                    f"Stock insuficiente para {producto.nombre}. "
                    f"Disponible: {producto.stock}. Pedido: {cantidad}."
                )
            item_existente.cantidad_solicitada = cantidad_nueva
        else:
            item_nuevo = ProductoPedido(
                producto=producto,
                cantidad_solicitada=cantidad,
                precio_unitario=producto.precio,
            )
            self.items.append(item_nuevo)

    def buscar_item_por_producto_id(self, id_producto: int):
        for item in self.items:
            if item.producto.id == id_producto:
                return item
        return None

    def remover_producto(self, producto_id: str) -> None:
        self.items = [item for item in self.items if item.producto.id != producto_id]

    def calcular_precio(self) -> float:
        subtotal = self._precio_productos()
        return (
            self.precio_estandar
            + self.cargo_adicional
            + self.impuestos_aduaneros
            + subtotal
        )

    def calcular_fecha_entrega(self) -> datetime:
        dias_entrega = {
            TipoPedido.ESTANDAR: 5,
            TipoPedido.EXPRESS: 1,
            TipoPedido.PROGRAMADO: 7,
            TipoPedido.INTERNACIONAL: 15,
        }
        dias = dias_entrega.get(self.tipo, 5)
        return self.fecha + timedelta(days=dias)

    def transformar_diccionario(self) -> dict:
        """Transforma pedido a diccionario usando items correctamente"""
        return {
            "id": str(self.id),
            "cliente_id": self.cliente_id,
            "tipo": self.tipo.value,
            "estado": self.estado.value,
            "items": [item.to_dict() for item in self.items],
            "resumen": {
                "subtotal": self._precio_productos(),
                "precio_estandar": self.precio_estandar,
                "cargo_adicional": self.cargo_adicional,
                "impuestos_aduaneros": self.impuestos_aduaneros,
                "total": self.calcular_precio(),
                "total_items": len(self.items),
                "total_productos": sum(item.cantidad_solicitada for item in self.items),
            },
            "fecha": self.fecha.isoformat(),
            "fecha_entrega": self.fecha_entrega.isoformat(),
        }

    def generar_factura(self, cliente: Cliente, metodo_de_pago: MetodoDePago) -> str:
        id_acortado = str(self.id)[:8]

        lineas_items = []
        for item in self.items:
            lineas_items.append(
                f"- {item.producto.nombre} x{item.cantidad_solicitada}: ${item.subtotal():.2f}"
            )
        items_texto = "\n".join(lineas_items)

        subtotal = self._precio_productos()
        descuento_monto, descuento_porcentaje = self.calcular_descuento(cliente)
        subtotal_con_descuento = subtotal - descuento_monto

        costo_envio = self.cargo_adicional
        if self.tiene_envio_gratis(cliente):
            costo_envio = 0.0
            nota_envio = " (Gratis)"
        else:
            nota_envio = ""

        total_final = (
            subtotal_con_descuento
            + self.precio_estandar
            + costo_envio
            + self.impuestos_aduaneros
        )

        factura = f"""
        # Factura #{id_acortado}

        **Cliente:** {cliente.nombre} ({cliente.email})
        **Tipo de cliente:** {cliente.tipo.value.upper()}
        **Método de pago:** {metodo_de_pago.nombre}
        **Fecha:** {self.fecha.strftime("%Y-%m-%d %H:%M")}
        **Tipo de pedido:** {self.tipo.value.upper()}

        ## Items:
        {items_texto}

        ## Resumen:
        - Subtotal productos: ${subtotal:.2f}
        - Descuento ({int(descuento_porcentaje)}%): -${descuento_monto:.2f}
        - Subtotal con descuento: ${subtotal_con_descuento:.2f}
        - Precio estándar: ${self.precio_estandar:.2f}
        - Costo de envío: ${costo_envio:.2f}{nota_envio}
        - Impuestos aduaneros: ${self.impuestos_aduaneros:.2f}
        - **TOTAL: ${total_final:.2f}**

        **Estado:** {self.estado.value}
        **Entrega estimada:** {self.fecha_entrega.strftime("%Y-%m-%d") if self.fecha_entrega else "Por calcular"}

        ---
        *Gracias por su compra*
                """

        return factura

    def validar_stock_completo(self) -> bool:
        return all(item.tiene_stock_suficiente() for item in self.items)
