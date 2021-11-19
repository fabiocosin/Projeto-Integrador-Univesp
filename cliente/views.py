from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import cliente
from .forms import ClienteForm

class ListaClienteView(ListView):
    model = cliente
    QuerySet = cliente.objects.all().order_by('nome_completo')

class ClienteCreateView(CreateView):
    model = cliente
    form_class = ClienteForm
    success_url = '/clientes/'