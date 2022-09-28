from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import Setor
from .forms import SetorForm

class ListaSetorView(ListView):
     model = Setor
     queryset = Setor.objects.all().order_by('nome_setor')

class SetorCreateView(CreateView):
     model = Setor
     form_class = SetorForm
     success_url = '/setor/'

class SetorDeleteView(DeleteView):
     model = Setor
     success_url = '/setor/'
