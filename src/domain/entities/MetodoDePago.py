class MetodoDePago:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def to_dict(self) -> dict:
        return {"nombre": self.nombre}
