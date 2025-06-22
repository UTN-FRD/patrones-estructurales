from patron_decorator.notificador_interface import Notificador

#3 - Decorador base: Base Decorator
class DecoradorNotificador(Notificador):  # Base Decorator
    def __init__(self, wrappee: Notificador):  # wrappee: Component
        self._wrappee = wrappee

    def send(self, mensaje: str) -> None:
        self._wrappee.send(mensaje)  # delega a wrappee
