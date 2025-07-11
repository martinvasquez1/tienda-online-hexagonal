from abc import ABC, abstractmethod
from uuid import uuid4
from enum import Enum

from src.domain.entities.Cliente import Cliente, TipoCliente
from src.domain.entities.MetodoDePago import MetodoDePago
from src.domain.entities.Producto import Producto


class EstadoPedido(Enum):
    PENDIENTE = "pendiente"
    PAGADO = "pagado"
    EN_PREPARACION = "en preparación"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"


class Pedido(ABC):
    def __init__(self, id, usuario_id):
        self.id = id
        self.estado = EstadoPedido.EN_PREPARACION
        self.productos: Producto = []
        self.precio_estandar = 10
        self.fecha = None
        self.usuario_id = usuario_id

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def _precio_productos(self):
        return sum(producto.precio for producto in self.productos)

    @abstractmethod
    def calcular_precio(self):
        pass

    def transformar_diccionario(self):
        conteo_productos = {}

        for producto in self.productos:
            codigo = str(producto.codigo)
            if codigo in conteo_productos:
                conteo_productos[codigo] += 1
            else:
                conteo_productos[codigo] = 1  #

        productos = [
            {
                "codigo": codigo,
                "cantidad": cantidad,
            }
            for codigo, cantidad in conteo_productos.items()
        ]

        return {
            "id": str(self.id),
            "estado": self.estado.name,
            "productos": productos,
            "precio_estandar": self.precio_estandar,
            "fecha": self.fecha,
        }

    def generar_factura(self, cliente: Cliente, metodo_de_pago: MetodoDePago) -> str:
        id_acortado = str(self.id)[:8]

        productos = ""
        for producto in self.productos:
            productos += f"- {producto.nombre}: ${producto.precio}\n"

        precio_total = self._precio_productos()
        precio_total_con_descuento = precio_total

        descuentos = {
            TipoCliente.NUEVO.name: 0.05,
            TipoCliente.FRECUENTE.name: 0.10,
            TipoCliente.VIP.name: 0.15,
        }

        if cliente.tipo in descuentos:
            precio_total_con_descuento *= 1 - descuentos[cliente.tipo]

        impuesto = getattr(self, "imp", None)

        factura = f"""# Factura para pedido: {id_acortado}
        Cliente: {cliente.nombre} / {cliente.email}
        Método de pago: {metodo_de_pago.nombre}

        {productos}
        Total: {precio_total}
        Descuento(%): {int(descuentos[cliente.tipo] * 100)}%
        Con descuento aplicado: {precio_total_con_descuento}

        Estado: {self.estado.name}
        Impuestos: {impuesto if impuesto else 'No hay impuestos'}
        """

        return factura


class PedidoEstandar(Pedido):
    def calcular_precio(self):
        return self.precio_estandar + self._precio_productos()


class PedidoExpres(Pedido):
    def __init__(self, productos, fecha):
        super().__init__(productos)
        self.fecha = fecha
        self.cargo_adicional = 20

    def calcular_precio(self):
        return self.precio_estandar + self.cargo_adicional + self._precio_productos()


class PedidoProgramado(Pedido):
    def __init__(self, productos, fecha):
        super().__init__(productos)
        self.fecha = fecha

    def calcular_precio(self):
        return self.precio_estandar + self._precio_productos()


class PedidoInternacional(Pedido):
    def __init__(self, productos):
        super().__init__(productos)
        self.impuestos_aduaneros = 100

    def calcular_precio(self):
        return (
            self.precio_estandar + self.impuestos_aduaneros + self._precio_productos()
        )
