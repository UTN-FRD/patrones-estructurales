from escuela.estudiante import Estudiante
from escuela.profesor import Profesor
from escuela.curso import Curso

# Para trabajar con la escuela debo crear todos los objetos y relacionarlos.
# Toda la lógica está en el cliente...
# Ver la implementación de Facade en main_facade.py

curso = Curso("Diseño de Sistemas")

profesor1 = Profesor("Juan Manuel", 123, curso)
profesor2 = Profesor("María Laura", 321, curso)

estudiante1 = Estudiante("Vanesa", 2020)
estudiante2 = Estudiante("Miguel", 2021)

curso.inscribir_estudiante(estudiante1)
curso.inscribir_estudiante( Estudiante("Juana", 2020) )

curso.mostrar_estudiantes()
