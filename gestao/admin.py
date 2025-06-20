from django.contrib import admin
from .models import Pessoa, Metodos, Grupo, Despesa, Avista, Aprazo, Mensal

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
    list_display = '__all__'

admin.site.register(Avista)
class AvistaAdmin(admin.ModelAdmin):
    list_display = '__all__'

admin.site.register(Aprazo)
class AprazoAdmin(admin.ModelAdmin):
    list_display = '__all__'

admin.site.register(Mensal)
class MensalAdmin(admin.ModelAdmin):
    list_display = '__all__'