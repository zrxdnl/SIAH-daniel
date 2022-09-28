from django.urls import path 
from .views import ListaUnidadeView, UnidadeCreateview
urlpatterns = [
     path('', ListaUnidadeView.as_view(), name='unidade.index'),
     path('novo/', UnidadeCreateview.as_view(), name='unidade.novo')
]