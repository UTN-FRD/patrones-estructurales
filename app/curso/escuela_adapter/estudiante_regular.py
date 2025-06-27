from escuela_adapter.persona import Persona
from escuela_adapter.estudiante import Estudiante

# Ahora la clase EstudianteRegular (ex Estudiante) hereda de Persona e implementa Estudiante
class EstudianteRegular(Persona, Estudiante):
    def __init__(self, nombre, anio_ingreso):
        super().__init__(nombre)
        self.anio_ingreso = anio_ingreso
        
    def __str__(self):
        return f"{super().__str__()} - Ingreso: {self.anio_ingreso}"