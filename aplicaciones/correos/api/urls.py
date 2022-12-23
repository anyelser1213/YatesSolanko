from django.urls import path
from aplicaciones.usuarios.api.api import enviar_codigo_email_api_view

urlpatterns = [

    #Normal

    #Apis
    path('enviar_codigo_email/',enviar_codigo_email_api_view,name='enviar_codigo_email'),
    
    
    #path('obtener_comprobantes_api_view/',obtener_comprobantes_api_view,name='obtener_comprobanteApi'),
    
    #path('consultarjugada/',consultarJugada_api_view,name='consultar_jugada'),
    #path('jugada/',JugadaApiView.as_view(),name='jugadaApi')
]