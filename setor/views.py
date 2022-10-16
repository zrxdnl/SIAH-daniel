from urllib import request
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Setor
from .forms import SetorForm
class ListaSetorView(ListView):
     model = Setor
     queryset = Setor.objects.all().order_by('nome_setor')
     def get_queryset(self):
          queryset = super().get_queryset()

          filtro = self.request.GET.get('nome') or None
          if filtro:
               if filtro.isnumeric():
                    queryset= queryset.filter(codigo_setor__contains=filtro)
               else:
                    queryset= queryset.filter(nome_setor__contains=filtro)                  
          return queryset

class SetorCreateView(CreateView):
     model = Setor
     form_class = SetorForm
     success_url = '/setor/'

class SetorDeleteView(DeleteView):
     model = Setor
     success_url = '/setor/'

class SetorUpdateView(UpdateView):
     model = Setor
     form_class = SetorForm
     success_url = '/setor/'
