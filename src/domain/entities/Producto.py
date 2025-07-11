class Producto:
    def __init__(self, id, pedido_id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.pedido_id = pedido_id
