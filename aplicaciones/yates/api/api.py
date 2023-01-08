import json

#Para autenticar los usuarios
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from aplicaciones.usuarios.models import Usuarios
from aplicaciones.usuarios.api.serializers import UsuariosSerializer

@api_view(['GET','POST'])
def crear_usuario_api_view(request):


    if request.method == 'GET':
        usuarios = Usuarios.objects.all()
        usuarios_serializer = Usuarios(usuarios,many=True)
        return Response(usuarios_serializer.data)
    

    elif request.method == 'POST':

        print("datos",request.data, "Usuario: ",request.user.email,request.user.id)
        
        #Creamos la instancia del usuario
        miuser = Usuarios()

        #Siempre vamos a crear usuarios normales(Por ahora)
        miuser.nombre = request.data.get('nombre')
        miuser.apellido = request.data.get('apellido')
        miuser.email  = request.data.get('correo')
        miuser.activo =True
        miuser.set_password("1")
        miuser.admin =False #No puede entrar al admin
        miuser.is_superuser = False #No tiene permisos de superusuario

        miuser.set_password(request.data.get('clave'))

        #Aqui guardamos en la base de datos
        miuser.save()

        print(miuser)
        #Datos que enviaremos
        datos = {"Mensaje":"Exitoso"}


        
        
        #jugada_serializer = JugadaSerializer(data = request.data) #De json a objeto otra ves y guardamos
        

        #print("El tipo de dato es: ",type(datos))

        return JsonResponse(datos,safe = False)




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
        
        
