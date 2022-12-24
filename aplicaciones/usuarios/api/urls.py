from django.urls import path
from aplicaciones.usuarios.api.api import crear_usuario_api_view

urlpatterns = [

    #Normal

    #Apis
    path('crear_usuario_api/',crear_usuario_api_view,name='crear_usuario_api'),
    #path('obtener_comprobantes_api_view/',obtener_comprobantes_api_view,name='obtener_comprobanteApi'),
    
]