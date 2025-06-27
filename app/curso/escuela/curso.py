
class Curso():
    def __init__(self, materia):
        self.materia = materia
        self.estudiantes = []

    def __str__(self):
        return f"{self.materia} - {len(self.estudiantes)}"

    def inscribir_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        print("**"+self.materia+"**")
        for estudiante in self.estudiantes:
            print(estudiante)
