from patron_decorator.notificador_email import NotificadorEmail
from patron_decorator.notificador_sms import NotificadorSMS
from patron_decorator.notificador_slack import NotificadorSlack

#5 - Cliente
# a = new ConcComponent()
notificador = NotificadorEmail(["user1@mail.com", "user2@mail.com"])

# b = new ConcDecorator1(a)
#sms = NotificadorSMS(notificador)

# c = new ConcDecorator2(b)
full_notificador = NotificadorSlack(notificador)

# c.execute()
full_notificador.send("¡Nuevo evento en el sistema!")