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

     def get_queryset(self):
               queryset = super().get_queryset()

               filtro = self.request.GET.get('nome') or None
               filtro2 = self.request.GET.get('marca') or None 
               filtro3 = self.request.GET.get('link') or None
               if filtro:
                    if filtro2 == 'CF':
                         queryset = queryset.filter(Numero_Ficha__icontains=filtro)
                    else:
                         queryset = queryset.filter(Numero_CPF__numero_do_documento_paciente__icontains=filtro)
               return queryset

class FichamedicaDeleteView(DeleteView):
     model = Fichamedica
     success_url = '/fichamedica/'

class FichamedicaUpdateView(UpdateView):
     model = Fichamedica
     form_class = FichamedicaForm
     success_url = '/fichamedica/'