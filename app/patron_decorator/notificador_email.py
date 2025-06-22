from patron_decorator.notificador_interface import Notificador 

#2 - Componente concreto: ConcreteComponent
class NotificadorEmail(Notificador):  # Concrete Component
    def __init__(self, destinatarios):
        self.destinatarios = destinatarios

    def send(self, mensaje: str) -> None:
        for email in self.destinatarios:
            print(f"Email enviado a {email}: {mensaje}")
