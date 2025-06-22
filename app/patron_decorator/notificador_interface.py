from abc import ABC, abstractmethod

#1 - Interfaz común: Component
class Notificador(ABC):  # <<interface>> Component
    @abstractmethod
    def send(self, mensaje: str) -> None:
        pass
