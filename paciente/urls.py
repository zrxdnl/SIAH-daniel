from django.urls import path
from .views import ListaPacienteView

urlpatterns = [
     path('', ListaPacienteView.as_view(), name='paciente.index')
]