from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name ="chats"

urlpatterns = [
    #path('', views.Index.as_view(), name='index'),
    
    #path('index/', views.Login.as_view() ,name="login"),
    #path('logout/', views.Logout.as_view() ,name="logout"),




    
    
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)