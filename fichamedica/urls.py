from django.urls import path
from .views import ListaFichamedicaView, FichamedicaCreateView, FichamedicaDeleteView, FichamedicaUpdateView

urlpatterns = [
     path('', ListaFichamedicaView.as_view(), name='fichamedica.index'),
     path('novo/', FichamedicaCreateView.as_view(), name='fichamedica.novo'),
     path('editar/<int:pk>', FichamedicaUpdateView.as_view(), name='fichamedica.editar'),
     path('remover/<int:pk>', FichamedicaDeleteView.as_view(), name='fichamedica.remover')
]