from django.urls import path
from aplicaciones.correos.api.api import recibir_codigo_email_api_view

urlpatterns = [

    #Normal

    #Apis
    path('recibir_codigo_email_api_view/',recibir_codigo_email_api_view,name='recibir_codigo_email_api_view'),
    
    
    #path('obtener_comprobantes_api_view/',obtener_comprobantes_api_view,name='obtener_comprobanteApi'),
    
    #path('consultarjugada/',consultarJugada_api_view,name='consultar_jugada'),
    #path('jugada/',JugadaApiView.as_view(),name='jugadaApi')
]