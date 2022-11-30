from django.urls import path
from .views import ListaPacienteView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView

urlpatterns = [
     path('', ListaPacienteView.as_view(), name='paciente.index'),
     path('novo/', PacienteCreateView.as_view(), name='paciente.novo'),
     path('editar/<int:pk>', PacienteUpdateView.as_view(), name='paciente.editar'),
     path('remover/<int:pk>', PacienteDeleteView.as_view(), name='paciente.remover')
]