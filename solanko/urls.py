"""solanko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns #Pendiente con esto para traducciones

urlpatterns = [

    #Traducciones
    #path('i18n/', include('django.conf.urls.i18n')),

    path('admin/', admin.site.urls),

    
]


urlpatterns += i18n_patterns(

    path('', include('aplicaciones.principal.urls')),
    path('', include('aplicaciones.login.urls')),
    path('', include('aplicaciones.usuarios.urls')),
    path('', include('aplicaciones.fondo_imagenes.urls')),
    path('', include('aplicaciones.chats.urls')),
    path('', include('aplicaciones.yates.urls')),
    #path('login', include('login.urls')),


    #Para las apis
    path('api-auth/', include('rest_framework.urls')),
    #path('', include("principal.urls")),
    #path('tinymce/', include("tinymce.urls")),
    prefix_default_language=False, #Por defecto se usa el lenguaje asignado en setting
 )
