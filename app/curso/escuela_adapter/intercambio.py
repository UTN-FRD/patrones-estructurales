
class Intercambio():
    def __init__(self):
        self.nombre = None
        self.pais_origen = None

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_origen(self, origen):
        self.pais_origen = origen

    def __str__(self):
        return f"{self.nombre} - Origen: {self.pais_origen}"
    