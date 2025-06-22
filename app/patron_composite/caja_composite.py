from patron_composite.item_pedido_interface import ItemPedido

# 3 - Objeto compuesto: Composite
class Caja(ItemPedido):  # Composite
    def __init__(self, nombre, costo_empaque=0):
        self.nombre = nombre
        self.costo_empaque = costo_empaque
        self._items = []  # children: List[ItemPedido]

    def add(self, item: ItemPedido):
        self._items.append(item)

    def remove(self, item: ItemPedido):
        self._items.remove(item)

    def getChildren(self):
        return self._items

    def calcular_precio(self) -> float:
        print(f"Calculando precio de la caja: {self.nombre}")
        total = self.costo_empaque
        for item in self._items:
            total += item.calcular_precio()
        print(f"Total caja '{self.nombre}' (incluye empaque ${self.costo_empaque}): ${total}")
        return total
    