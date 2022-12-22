from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name ="correos"

urlpatterns = [
        
    #path('correoPrueba', views.registrar.as_view() ,name="correoPrueba"),



    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)