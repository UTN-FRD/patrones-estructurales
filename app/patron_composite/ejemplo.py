from patron_composite.caja_composite import Caja
from patron_composite.producto_leaf import Producto

# 4 - Cliente
# Productos simples
libro = Producto("Libro", 100)
celular = Producto("Celular", 300)

# Caja pequeña con un producto
caja_pequena = Caja("Caja chica", costo_empaque=5)
caja_pequena.add(libro)

# Caja mediana con otro producto y la caja pequeña
caja_mediana = Caja("Caja mediana", costo_empaque=10)
caja_mediana.add(celular)
caja_mediana.add(caja_pequena)

# Caja grande que contiene varias cajas y productos
caja_grande = Caja("Caja grande", costo_empaque=15)
caja_grande.add(caja_mediana)
caja_grande.add(Producto("Auriculares", 150))

# Cliente calcula precio total de la caja grande
print("\n🧾 Precio total del pedido:")
precio_total = caja_grande.calcular_precio()
print(f"\n💰 Precio total final: ${precio_total}")
