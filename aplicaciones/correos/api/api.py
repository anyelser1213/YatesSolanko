import json

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from aplicaciones.usuarios.models import Usuarios
#from aplicaciones.usuarios.api.serializers import EmailSerializer


#PARA EL ENVIO DE CORREOS
from django.core.mail import send_mail
from django.conf import settings

#Para obtener numeros aleatorios
import random

@api_view(['GET','POST'])
def recibir_codigo_email_api_view(request):


    if request.method == 'GET':
        jugadas = Usuarios.objects.all()
        jugadas_serializer = Usuarios(jugadas,many=True)
        return Response(jugadas_serializer.data)
    

    elif request.method == 'POST':

        print("datos",request.data, "Usuario: ",request.user,request.user.id)
        
        correo = str(request.data.get('correo'))

        

        codigo_random = random.randint(100000, 999999)

        print("El codigo generado es: ",codigo_random)
        Titulo = 'Codigo de registro'
        Mensaje_a_enviar = 'Ingrese este codigo en el registro para validar su email '+str(codigo_random)

        #Para pruebas
        #email_from = 'anyelserperez@gmail.com'
        #recipient_list = [settings.EMAIL_HOST_USER,"anyelserperez@gmail.com"]

        #Para envios reales   
        email_from = settings.EMAIL_HOST_USER
        #lista_de_correos_a_enviar = ['anyelserperez@gmail.com',correo]
        lista_de_correos_a_enviar = [correo,]


        


        send_mail( Titulo, Mensaje_a_enviar, email_from, lista_de_correos_a_enviar )
        
        print("email: ",correo)
        
        
        #jugada_serializer = JugadaSerializer(data = request.data) #De json a objeto otra ves y guardamos
        
        #Datos que enviaremos
        datos = {"codigo":codigo_random}

        #print("El tipo de dato es: ",type(datos))

        return JsonResponse(datos,safe = False)



"""

@api_view(['GET','POST'])
def obtener_comprobantes_api_view(request):


    if request.method == 'GET':
        jugadas = Jugadas_Numeros.objects.all()
        jugadas_serializer = Jugadas_Numeros(jugadas,many=True)
        return Response(jugadas_serializer.data)
    

    elif request.method == 'POST':

        #Donde guardaremos los datos
        data={}

        print("datos",request.data, "Usuario: ",request.user.username,"Es superUser: ",request.user.is_superuser)
        id_tipo = str(request.data.get('tipos'))

        if request.user.is_superuser:

            Elementos = Jugadas_Numeros.objects.filter(id_jugada__id_tipo_jugada__nombre=str(id_tipo)).order_by('-status').values("id","id_jugada__digitos","id_telefono__numero_telefono","id_comprobante__numero_comprobante","status")
            #Elementos = Jugadas_Numeros.objects.filter(id_jugada__id_tipo_jugada__nombre=str(id_tipo)).values("status")
            
            #print(id_tipo)
            #print("")
            #print(Elementos.count())
            #print(Elementos)

            aux = 0
            for elem in Elementos:
                print("\n")
                #print(elem["id_jugada__digitos"])
                data[aux] = ({'id':elem['id'],'digitos':elem['id_jugada__digitos'],'telefono':elem['id_telefono__numero_telefono'],'comprobante':elem['id_comprobante__numero_comprobante'],'status':elem['status']})
                #data.update(str(elem):"")
                #data.update({str(aux):"Ultima Jugada guardada, "})
                aux+=1

        #En caso de que es un usuario normal
        else:

            Elementos = Jugadas_Numeros.objects.filter(id_jugada__id_tipo_jugada__nombre=str(id_tipo),id_usuario=request.user.id).order_by('-status').values("id","id_jugada__digitos","id_telefono__numero_telefono","id_comprobante__numero_comprobante","status")
            #print(id_tipo)
            #print("")
            #print(Elementos.count())
            print(Elementos)

            aux = 0
            for elem in Elementos:
                print("\n")
                #print(elem)
                data[aux] = ({'id':elem['id'],'digitos':elem['id_jugada__digitos'],'telefono':elem['id_telefono__numero_telefono'],'comprobante':elem['id_comprobante__numero_comprobante'],'status':elem['status']})
                aux+=1

        #id_comprobante = str(request.data.get('id_comprobante'))
        #comprobante = str(request.data.get('comprobante'))


        print(data)
        #Datos que enviaremos
        #datos = {"Mensaje":"Exitoso"}

        #Elemento = Jugadas_Numeros.objects.get(id=id_comprobante)
        #Elemento.status="Pagado"
        #Elemento.save()
        
        #print("Elemento Jugada: ",Elemento)
        #print("id_comprobante: ",id_comprobante)
        #print("Comprobante: ",comprobante)
        
        
        #comprobantes_serializer = Jugada_NumerosSerializer(data = request.data) #De json a objeto otra ves y guardamos
        

        #print("El tipo de dato es: ",type(datos))

        return JsonResponse(data,safe = False)
        
        

"""