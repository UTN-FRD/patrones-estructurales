from patron_composite.item_pedido_interface import ItemPedido

# 2 - Objeto hoja: Leaf
class Producto(ItemPedido):  # Leaf
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_precio(self) -> float:
        print(f"Producto: {self.nombre} - ${self.precio}")
        return self.precio