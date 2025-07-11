from abc import ABC, abstractmethod


class EstrategiaDescuento(ABC):
    @abstractmethod
    def calcular_descuento(self, subtotal: float) -> float:
        """Retorna el monto del descuento"""
        pass

    @abstractmethod
    def tiene_envio_gratis(self) -> bool:
        """Retorna si el tipo de cliente tiene envío gratis"""
        pass

    @abstractmethod
    def get_porcentaje_descuento(self) -> float:
        """Retorna el porcentaje para mostrar al usuario"""
        pass


class DescuentoClienteNuevo(EstrategiaDescuento):
    def calcular_descuento(self, subtotal: float) -> float:
        return subtotal * 0.05

    def tiene_envio_gratis(self) -> bool:
        return False

    def get_porcentaje_descuento(self) -> float:
        return 5.0


class DescuentoClienteFrecuente(EstrategiaDescuento):
    def calcular_descuento(self, subtotal: float) -> float:
        return subtotal * 0.10

    def tiene_envio_gratis(self) -> bool:
        return False

    def get_porcentaje_descuento(self) -> float:
        return 10.0


class DescuentoClienteVIP(EstrategiaDescuento):
    def calcular_descuento(self, subtotal: float) -> float:
        return subtotal * 0.15

    def tiene_envio_gratis(self) -> bool:
        return True

    def get_porcentaje_descuento(self) -> float:
        return 15.0
