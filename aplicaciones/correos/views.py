from django.shortcuts import render, redirect

#PARA EL ENVIO DE CORREOS
from django.core.mail import send_mail
from django.conf import settings

import random
# Create your views here.


def enviar_email(request):

    
    subject = 'Gracias por registrarte en este sitio'
    message = 'Este es el primer mensaje de prueba '

    #Para pruebas
    #email_from = 'anyelserperez@gmail.com'
    #recipient_list = [settings.EMAIL_HOST_USER,"anyelserperez@gmail.com"]

    #Para envios reales   
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['anyelserperez@gmail.com',]


    codigo_random = random.randint(100000, 900000)

    print("El codigo generado es: ",codigo_random)


    send_mail( subject, message, email_from, recipient_list )
    return redirect('principal:index')