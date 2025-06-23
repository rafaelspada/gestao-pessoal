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

    def __init__(self, *args, **kwargs):
        super(AvistaForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    data_pagamento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class AprazoForm(forms.ModelForm):
    class Meta:
        model = Aprazo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AprazoForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    data_pagamento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class MensalForm(forms.ModelForm):
    class Meta:
        model = Mensal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MensalForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False