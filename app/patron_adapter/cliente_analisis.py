from patron_adapter.client_interface import ClientInterface

# 1- La clase Cliente contiene la lógica de negocio existente del programa.
class ClienteDeAnalisis:
    def __init__(self, fuente_datos: ClientInterface):
        self.fuente = fuente_datos

    # 5- El código cliente no se acopla a la clase adaptadora concreta siempre y 
    # cuando funcione con la clase adaptadora a través de la interfaz con el cliente. 
    def procesar(self):
        datos = self.fuente.obtener_datos()
        for accion in datos["mercado"]:
            print(f"Procesando acción {accion['nombre']} a ${accion['precio']}")
