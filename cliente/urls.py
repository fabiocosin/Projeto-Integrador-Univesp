from django.urls import path
from .views import ListaClienteView, ClienteCreateView

urlpatterns = [
    path('', ListaClienteView.as_view(), name='cliente.index'),
    path('novo/', ClienteCreateView.as_view(), name='cliente.novo')
]