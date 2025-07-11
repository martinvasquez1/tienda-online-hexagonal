from src.domain.entities.Cliente import TipoCliente
from src.domain.service.estrategias_descuento import (
    DescuentoClienteFrecuente,
    DescuentoClienteNuevo,
    DescuentoClienteVIP,
    EstrategiaDescuento,
)


class FactoryDescuento:
    _estrategias = {
        TipoCliente.NUEVO: DescuentoClienteNuevo,
        TipoCliente.FRECUENTE: DescuentoClienteFrecuente,
        TipoCliente.VIP: DescuentoClienteVIP,
    }

    @classmethod
    def crear_estrategia(cls, tipo_cliente: TipoCliente) -> EstrategiaDescuento:
        estrategia_class = cls._estrategias.get(tipo_cliente)
        if not estrategia_class:
            raise ValueError(f"Tipo de cliente no soportado: {tipo_cliente}")
        return estrategia_class()

    @classmethod
    def registrar_estrategia(cls, tipo_cliente: TipoCliente, estrategia_class):
        cls._estrategias[tipo_cliente] = estrategia_class
