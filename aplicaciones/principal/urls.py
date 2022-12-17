from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns #Pendiente con esto

from . import views

app_name ="principal"

urlpatterns = [
    #path('', views.Index.as_view(), name='index'),
    
    path('', views.Index.as_view() ,name="index"),
    path('about', views.about ,name="about"),




    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)