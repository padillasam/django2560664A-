from django.urls import path
from . import views

urlpatterns = [    
    path('lista',views.listaaprendices,name='lista_aprendices')    
]