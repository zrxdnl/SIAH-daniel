from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import Unidade
from .forms import UnidadeForm

class ListaUnidadeView(ListView):
     model = Unidade
     queryset = Unidade.objects.all().order_by('nome_unidade')

class UnidadeCreateview(CreateView):
     model = Unidade 
     form_class = UnidadeForm
     success_url = '/unidade/'

class UnidadeDeleteView(DeleteView):
     model = Unidade
     success_url = '/unidade/'