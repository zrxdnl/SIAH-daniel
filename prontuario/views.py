from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .models import Prontuario
from .forms import ProntuarioForm
# Create your views here.
class ProntuarioCreateView(CreateView):
     model = Prontuario
     form_class = ProntuarioForm
     success_url = '/prontuario/' 

class ListaProntuarioView(ListView):
     model = Prontuario
     queryset = Prontuario.objects.all().order_by('Numero_Prontuario')
     def get_queryset(self):
               queryset = super().get_queryset()

               filtro = self.request.GET.get('nome') or None
               filtro2 = self.request.GET.get('marca') or None
               if filtro:
                    if filtro2 == 'CP':
                         queryset = queryset.filter(Numero_Prontuario__icontains=filtro)
                    elif filtro2 == 'NS':
                         queryset = queryset.filter(Codigo_Setor__codigo_setor__icontains=filtro)
                    else:
                         queryset = queryset.filter(Numero_SUS__cartao_sus_paciente__icontains=filtro)
               return queryset
     
class ProntuarioDeleteView(DeleteView):
     model = Prontuario
     success_url = '/prontuario/'

class ProntuarioUpdateView(UpdateView):
     model = Prontuario
     form_class = ProntuarioForm
     success_url = '/prontuario/'
