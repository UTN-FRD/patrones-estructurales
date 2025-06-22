from patron_decorator.decorator_notificador import DecoradorNotificador

#4 - Decoradores concretos: Concrete Decorators
class NotificadorSMS(DecoradorNotificador):  # ConcreteDecorator1
    def send(self, mensaje: str) -> None:
        super().send(mensaje)  # super: ejecuta el wrappee
        print(f"SMS enviado: {mensaje}")  # extra()
