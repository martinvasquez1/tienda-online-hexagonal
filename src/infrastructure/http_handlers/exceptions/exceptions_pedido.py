class PedidoError(Exception):
    """Excepción base para errores de cliente."""

    pass


class PedidoNoEncontrado(PedidoError):
    """Excepción para cliente no encontrado."""

    pass
