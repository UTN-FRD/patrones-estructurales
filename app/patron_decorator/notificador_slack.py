from patron_decorator.decorator_notificador import DecoradorNotificador

#4 - Decoradores concretos: Concrete Decorators
class NotificadorSlack(DecoradorNotificador):  # ConcreteDecorator2
    def send(self, mensaje: str) -> None:
        super().send(mensaje)
        print(f"Slack notificado: {mensaje}")