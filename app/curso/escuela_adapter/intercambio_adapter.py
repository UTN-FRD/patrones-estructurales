from escuela_adapter.estudiante import Estudiante

# este es el adaptador del Intercambio
# Como implementa la interfaz de estudiante se puede tratar como Estudiante
class IntercambioAdapter(Estudiante):
    def __init__(self, intercambio, anio_ingreso):
        self.intercambio = intercambio # aqui tengo la instancia adaptada
        self.anio_ingreso = anio_ingreso

    def obtener_nombre(self):
        return self.intercambio.nombre

    def obtener_anio_ingreso(self):
        return self.anio_ingreso

    def __str__(self):
        return f"{self.obtener_nombre()} (Intercambio, Ingreso: {self.anio_ingreso})"