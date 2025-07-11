from dataclasses import dataclass


@dataclass
class DescuentoInfo:
    tipo_cliente: str
    porcentaje: float
    monto_descuento: float
    envio_gratis: bool
    descripcion: str

    def __post_init__(self):
        if self.envio_gratis:
            self.descripcion = f"{self.porcentaje}% de descuento + envío gratis"
        else:
            self.descripcion = f"{self.porcentaje}% de descuento"
