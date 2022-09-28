from django.urls import path 
from .views import ListaUnidadeView, UnidadeCreateview, UnidadeDeleteView
urlpatterns = [
     path('', ListaUnidadeView.as_view(), name='unidade.index'),
     path('novo/', UnidadeCreateview.as_view(), name='unidade.novo'),
     path('remover/<int:pk>', UnidadeDeleteView.as_view(), name='unidade.remover')
]