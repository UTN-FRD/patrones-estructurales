from escuela_adapter.persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, legajo, curso):
        super().__init__(nombre)
        self.legajo = legajo
        self.curso = curso

    def __str__(self):
        return f"{super().__str__()} ({self.legajo}) - {self.curso}"

    