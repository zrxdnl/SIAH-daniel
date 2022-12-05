from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Fichamedica
from .forms import FichamedicaForm

class FichamedicaCreateView(CreateView):
     model = Fichamedica
     form_class = FichamedicaForm
     success_url = '/fichamedica/'
     
class ListaFichamedicaView(ListView):
     model = Fichamedica 
     queryset = Fichamedica.objects.all().order_by('Numero_Ficha')
