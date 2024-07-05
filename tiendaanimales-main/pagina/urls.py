from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='index'), 
    path ('Accesorios', views.Accesorios, name='Accesorios'),  
    path ('Comidas', views.Comidas, name='Comidas'),
    path ('Juguetes', views.Juguetes, name='Juguetes'),
    path ('Snacks', views.Snacks, name='Snacks'),
    path ('Registro/', views.Registro, name='Registro'),    
]
