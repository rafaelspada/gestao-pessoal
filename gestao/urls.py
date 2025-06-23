from tempfile import template

from django.urls import path, include
from .views import DespesaView, RelatorioView

urlpatterns = [
    path("despesas/", DespesaView.as_view(template_name='cadastro_despesas.html'), name="despesas"),
    path("relatorios/", RelatorioView.as_view(template_name="relatorios_despesas.html"), name="relatorios")
]
