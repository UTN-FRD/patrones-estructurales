# Si entra un nuevo tipo de estudiante que no podemos modificar
# Por ejemplo un estudiante de intercambio (adapter/intercambio.py)
#
# Aqui necesitamos hacer 2 cosas
# - Crear un adaptador para el estudiante de intercambio
# - Crear una interfaz para Estudiantes

from escuela_adapter.intercambio import Intercambio
from escuela_adapter.intercambio_adapter import IntercambioAdapter
from escuela_adapter.escuela_facade import EscuelaFacade

# este es el estudiante de intercambio que llega nuevo
intercambio = Intercambio()
intercambio.set_nombre("Peter")
intercambio.set_origen("EEUU")

# para manejarlo en el sistema lo meto en el adaptador
intercambio_adapter = IntercambioAdapter(intercambio, 2025)

escuela_facade = EscuelaFacade()
print("Mostrando todos los estudiantes")
escuela_facade.mostrar_todos_estudiantes()
print("Mostrando los estudiantes del curso 0")
escuela_facade.mostrar_estudiantes(0)

escuela_facade.inscribir_estudiante_en_curso(0, intercambio_adapter)

print("Mostrando todos los estudiantes")
escuela_facade.mostrar_todos_estudiantes()
print("Mostrando los estudiantes del curso 0")
escuela_facade.mostrar_estudiantes(0)

