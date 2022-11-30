from django.urls import path
from .views import ListaFuncionarioView, FuncionarioCreateView, FuncionarioDeleteView

urlpatterns = [
     path('', ListaFuncionarioView.as_view(), name='funcionario.index'),
     path('novo/', FuncionarioCreateView.as_view(), name='funcionario.novo'),
     path('remover/<int:pk>', FuncionarioDeleteView.as_view(), name='funcionario.remover')
]

