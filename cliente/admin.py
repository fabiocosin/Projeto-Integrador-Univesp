from django.contrib import admin
from .models import cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'telefone',
        'email',
        'endereco',
        'data_criacao'
    ]
    list_filter = [
        'data_criacao'
    ]
    search_fields = [
        'nome_completo'
    ]

# Register your models here.
admin.site.register(cliente, ClienteAdmin)