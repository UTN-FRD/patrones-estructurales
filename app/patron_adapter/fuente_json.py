from patron_adapter.client_interface import ClientInterface

# Esta clase no necesita adaptador porque ya devuelve un json compatible con el cliente.
class FuenteJSON(ClientInterface):
    def obtener_datos(self):
        return {
            "mercado": [
                {"nombre": "DEF", "precio": 789},
                {"nombre": "GHI", "precio": 321}
            ]
        }
    