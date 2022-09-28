from django.urls import path
from .views import ListaSetorView, SetorCreateView, SetorDeleteView

urlpatterns = [
    path('', ListaSetorView.as_view(), name='setor.index'),
    path('novo/', SetorCreateView.as_view(), name='setor.novo'),
    path('remover/<int:pk>', SetorDeleteView.as_view(), name='setor.remover'),
]
