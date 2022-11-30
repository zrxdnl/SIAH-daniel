from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Paciente
from .forms import PacienteForm
class ListaPacienteView(ListView):
     model = Paciente
     queryset = Paciente.objects.all().order_by('nome_paciente')
     def get_queryset(self):
          queryset = super().get_queryset()

          filtro = self.request.GET.get('nome') or None
          if filtro:
               if filtro.isdigit():
                    queryset= queryset.filter(cartao_sus_paciente__icontains=filtro)
               else:
                    queryset= queryset.filter(nome_paciente__contains=filtro)
          return queryset

class PacienteCreateView(CreateView):
     model = Paciente
     form_class = PacienteForm
     success_url = '/paciente/'
     

class PacienteUpdateView(UpdateView):
     model = Paciente
     form_class = PacienteForm
     success_url = '/paciente/'

class PacienteDeleteView(DeleteView):
     model = Paciente
     success_url = '/paciente/'