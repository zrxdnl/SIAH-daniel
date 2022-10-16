from django.urls import path
from .views import ListaSetorView, SetorCreateView, SetorDeleteView, SetorUpdateView

urlpatterns = [
    path('', ListaSetorView.as_view(), name='setor.index'),
    path('novo/', SetorCreateView.as_view(), name='setor.novo'),
    path('editar/<int:pk>', SetorUpdateView.as_view(), name='setor.editar'),
    path('remover/<int:pk>', SetorDeleteView.as_view(), name='setor.remover'),
]
