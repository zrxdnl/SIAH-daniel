from django.urls import path
from .views import ListaFichamedicaView, FichamedicaCreateView, FichamedicaDeleteView

urlpatterns = [
     path('', ListaFichamedicaView.as_view(), name='fichamedica.index'),
     path('novo/', FichamedicaCreateView.as_view(), name='fichamedica.novo'),
     path('remover/<int:pk>', FichamedicaDeleteView.as_view(), name='fichamedica.remover')
]