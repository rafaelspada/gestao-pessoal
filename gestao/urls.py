from tempfile import template

from django.urls import path, include
from .views import DespesaView

urlpatterns = [
    path("despesas/", DespesaView.as_view(template_name='cadastro_despesas.html'), name="cadastro"),
]
