from django.contrib import admin
from .models import ContraCheque

class ContraChequeAdmin(admin.ModelAdmin):
    list_display = ('nome_funcionario', 'ano', 'data_criacao', 'conta', 'agencia',)

admin.site.register(ContraCheque, ContraChequeAdmin)