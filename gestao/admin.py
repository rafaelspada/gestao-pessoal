from django.contrib import admin
from .models import Pessoa, Metodos, Grupo, Despesa

# Register your models here.

admin.site.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

admin.site.register(Metodos)
class MetodosAdmin(admin.ModelAdmin):
    list_display = ('nome',)

admin.site.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

admin.site.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'parcela', 'grupo_despesa', 'metodos_despesa', 'pessoa_despesa', 'data_compra', 'data_pagamento')