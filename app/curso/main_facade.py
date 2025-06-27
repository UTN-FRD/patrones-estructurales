from escuela_facade import EscuelaFacade

# Con Facade centralizo todo en un solo objeto. 
# De esta manera la lógica queda encapsulada

escuela_facade = EscuelaFacade()
escuela_facade.mostrar_todos_estudiantes()
escuela_facade.mostrar_estudiantes(0)
