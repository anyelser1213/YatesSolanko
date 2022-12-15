from django.shortcuts import render, redirect
from aplicaciones.usuarios.models import Usuarios


#Clases para las plantillas
from django.views.generic import View,TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView

# Create your views here.




class registrar(TemplateView):

    template_name = "usuarios/registrarUsuario.html"

    def dispatch(self, request, *args, **kwargs):

        print("Estas autenticado GENIAL")
        #print("Permisos: ",list(Permission.objects.all()))
        print("usuario: ",request.user)



        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."

        
        
        return context



"""
class ProductosCrear(CreateView):

    model = Usuarios  
    form_class = ProductoForm
    template_name = "productos/productos-crear.html"
    success_url = reverse_lazy('productos:ProductoListar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."
        context['titulo'] = "Crear Productos"
        context['usuario'] = self.request.user
        return context

    def post(self,request,*args,**kwargs):
        
        print("entrando en post")

        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()#Guardamos el objeto
            return HttpResponseRedirect(self.success_url)

        #En caso de que no se cree el self.object se coloca en None
        self.object = None
        print(form.errors)

        #Aqui llamamos a todas las variables establecidas en get_context
        context = self.get_context_data(**kwargs)
        context['form'] = form

        #Asi es otra forma de enviar el contexto
        return render(request,self.template_name,context)
        
        #Asi es una forma de enviar
        #return render(request,self.template_name,{"form":form})

"""
