from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render

#Para enviar mensajes a correos
from django.core.mail import EmailMessage
from django.template.loader import render_to_string



#Decoradores
from django.views.decorators.csrf import csrf_protect

#Traducciones
from django.utils.translation import gettext as _



#Clases para las plantillas
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView

    



class Index(TemplateView):

    template_name = "principal/index.html"

    def dispatch(self, request, *args, **kwargs):

        """
        if request.user.is_anonymous:
            print("No estas autenticado, eres un usuario anonimo")
            return redirect("login:login")

        else:

            print("Estas autenticado GENIAL",request.user)
            print("usuario: ",request.user)
            print("usuario permisos: ",request.user.get_all_permissions())
            print(request.user.has_perm('src.ver_zulia'))
        
            
            #Aqui verificamos si el usuario esta activo para que ingrese
            
            if request.user.activo:   
                print("Usuario activo y validado")
            else:
                print("El usuario no esta activo")
                messages.add_message(request, messages.INFO, "Usuario Inactivo")
                return redirect("src:logout")
        """

            #return redirect("src:index")
            #print("Usuario ",request.user)

            #Esto es algo que podria funcionar en algun momento
            #grupo="prueba"
            #print('Proyecto %s' % (grupo))

            

            
            #empresa_creada = Empresa.objects.filter(creado_por_id=request.user.id)


        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."



#Para pruebas
@csrf_protect
def home(request):
     # Si estamos identificados devolvemos la portada
    
    contexto = {"Traduccion":_("Welcome to my site.")} 
    print(_("Welcome to my site."))
    return render(request, "principal/index.html", contexto)


@csrf_protect
def about(request):
     # Si estamos identificados devolvemos la portada
    
    contexto = {"Traduccion":_("Welcome to my site.")} 
    print(_("Welcome to my site."))
    return render(request, "principal/about.html", contexto)
