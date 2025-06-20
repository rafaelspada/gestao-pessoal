from django import forms
from .models import Despesa, Avista, Aprazo, Mensal


class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = '__all__'

class AvistaForm(forms.ModelForm):
    class Meta:
        model = Avista
        fields = '__all__'

class AprazoForm(forms.ModelForm):
    class Meta:
        model = Aprazo
        fields = '__all__'

class MensalForm(forms.ModelForm):
    class Meta:
        model = Mensal
        fields = '__all__'