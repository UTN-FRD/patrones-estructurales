from escuela.curso import Curso
from escuela.estudiante import Estudiante
from escuela.profesor import Profesor

class EscuelaFacade():
    def __init__(self):
        self.cursos = [Curso("Diseño de Sistemas"), Curso("Analisis de Sistemas")]
        self.profesores = [Profesor("Juan Manuel", 123, self.cursos[0]), Profesor("María Laura", 321, self.cursos[0])]
        self.estudiantes = [Estudiante("Vanesa", 2020), Estudiante("Miguel", 2021), Estudiante("Juana", 2020)]

        self.cursos[0].inscribir_estudiante(self.estudiantes[1])
        self.cursos[0].inscribir_estudiante(self.estudiantes[0])
        self.cursos[1].inscribir_estudiante(self.estudiantes[2])

    def mostrar_todos_estudiantes(self):
        for curso in self.cursos:
            print(curso)
            curso.mostrar_estudiantes()

    def mostrar_estudiantes(self, idx):
        print(self.cursos[idx])
        self.cursos[idx].mostrar_estudiantes()
