from django.shortcuts import render
from django.views.generic import ListView
from .models import Paciente

class ListaPacienteView(ListView):
     model = Paciente
     queryset = Paciente.objects.all().order_by('nome_paciente')
     

