from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Paciente
from fichamedica.models import Fichamedica
from prontuario.models import Prontuario
from .forms import PacienteForm
class ListaPacienteView(ListView):
     model = Paciente
     queryset = Paciente.objects.all().order_by('nome_paciente')
     
     def fichaPaciente(self, valor):
          queryset = Fichamedica.filter(Numero_CPF__numero_do_documento_paciente__icontains=valor)
          return queryset

     def get_queryset(self):
          queryset = super().get_queryset()
          filtro = self.request.GET.get('nome') or None
          filtro2 = self.request.GET.get('link') or None
          filtro3 = self.request.GET.get('link2') or None

          if filtro3:
               queryset = Prontuario.objects.filter(Numero_CPF__numero_do_documento_paciente__icontains=filtro3)

          if filtro2:
               queryset = Fichamedica.objects.filter(Numero_CPF__numero_do_documento_paciente__icontains=filtro2)
         
          if filtro:
               if filtro.isdigit():
                    queryset = queryset.filter(numero_do_documento_paciente__icontains=filtro)
               else:
                    queryset = queryset.filter(nome_paciente__contains=filtro)
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