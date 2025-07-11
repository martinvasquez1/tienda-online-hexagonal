class ClienteError(Exception):
    """Excepción base para errores de cliente."""

    pass


class ClienteNoEncontrado(ClienteError):
    """Excepción para cliente no encontrado."""

    pass


class NombreRequerido(ClienteError):
    """Excepción para nombre requerido."""

    pass
