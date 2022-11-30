from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Funcionario
from .forms import FuncionarioForm

class ListaFuncionarioView(ListView):
     model = Funcionario 
     queryset = Funcionario.objects.all().order_by('Nome_Funcionario')
     def get_queryset(self):
          queryset = super().get_queryset()

          filtro = self.request.GET.get('nome') or None
          if filtro:
               queryset= queryset.filter(nome_Funcionario__contains=filtro)
               
          return queryset

class FuncionarioCreateView(CreateView):
     model = Funcionario
     form_class = FuncionarioForm
     success_url = '/funcionario/'
