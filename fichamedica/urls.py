from django.urls import path
from .views import ListaFichamedicaView, FichamedicaCreateView

urlpatterns = [
     path('', ListaFichamedicaView.as_view(), name='fichamedica.index'),
     path('novo/', FichamedicaCreateView.as_view(), name='fichamedica.novo'),
]