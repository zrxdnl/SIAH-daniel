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
     
class ProntuarioDeleteView(DeleteView):
     model = Prontuario
     success_url = '/prontuario/'

class ProntuarioUpdateView(UpdateView):
     model = Prontuario
     form_class = ProntuarioForm
     success_url = '/prontuario/'
