from django.shortcuts import render, redirect

#PARA EL ENVIO DE CORREOS
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def enviar_email(request):
    subject = 'Gracias por registrarte en este sitio'
    message = 'Este es el primer mensaje de prueba '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['anyelserperez@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('principal:index')