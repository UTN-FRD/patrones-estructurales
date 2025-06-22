from abc import ABC, abstractmethod

# 2- La Interfaz ClientInterface describe un protocolo que otras clases deben seguir para poder colaborar con el código cliente.
class ClientInterface(ABC):
    @abstractmethod
    def obtener_datos(self) -> dict:
        pass
