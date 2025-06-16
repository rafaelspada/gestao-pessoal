from django import forms
from .models import Despesa

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['nome', 'valor', 'data_pagamento', 'data_compra', 'parcela', 'grupo_despesa', 'metodos_despesa', 'pessoa_despesa']
