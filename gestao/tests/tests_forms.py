from django.test import TestCase
from gestao.forms import DespesaForm
from ..models import Despesa, Avista, Aprazo, Mensal, Pessoa, Metodos, Grupo

class DespesaFormTestCase(TestCase):

    def setUp(self):
        self.grupo = Grupo.objects.create(nome='Casa')
        self.metodos = Metodos.objects.create(nome='Cartão')
        self.pessoa = Pessoa.objects.create(nome='Rafael')

    def test_formulario_despesa(self):
        form = DespesaForm(data={
            'nome': 'água',
            'valor': 15,
            'metodo_pagamento': 'AV',
            'grupo_despesa':self.grupo,
            'metodos_despesa':self.metodos,
            'pessoa_despesa':self.pessoa
        })
        self.assertTrue(form.is_valid())
