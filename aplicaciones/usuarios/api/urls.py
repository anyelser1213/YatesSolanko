from django.urls import path
from aplicaciones.usuarios.api.api import verificar_email_api_view, obtener_comprobantes_api_view

urlpatterns = [

    #Normal

    #Apis
    path('verificar_email/',verificar_email_api_view,name='verificar_email'),
    path('obtener_comprobantes_api_view/',obtener_comprobantes_api_view,name='obtener_comprobanteApi'),
    
    #path('consultarjugada/',consultarJugada_api_view,name='consultar_jugada'),
    #path('jugada/',JugadaApiView.as_view(),name='jugadaApi')
]