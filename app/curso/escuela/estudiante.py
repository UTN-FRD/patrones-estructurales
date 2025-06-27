from escuela.persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, anio_ingreso):
        super().__init__(nombre)
        self.anio_ingreso = anio_ingreso
        
    def __str__(self):
        return f"{super().__str__()} - Ingreso: {self.anio_ingreso}"