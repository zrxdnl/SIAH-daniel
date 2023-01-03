from django.urls import path
from .views import ListaProntuarioView, ProntuarioCreateView, ProntuarioDeleteView, ProntuarioUpdateView

urlpatterns = [
     path('', ListaProntuarioView.as_view(), name='prontuario.index'),
     path('novo/', ProntuarioCreateView.as_view(), name='prontuario.novo'),
     path('editar/<int:pk>', ProntuarioUpdateView.as_view(), name='prontuario.editar'),
     path('remover/<int:pk>', ProntuarioDeleteView.as_view(), name='prontuario.remover')
]