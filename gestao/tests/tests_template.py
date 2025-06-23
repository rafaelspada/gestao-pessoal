from django.test import TestCase
from django.urls import reverse

from gestao.forms import DespesaForm
from ..models import Despesa, Avista, Aprazo, Mensal, Pessoa, Metodos, Grupo

class test_template_despesa_post(TestCase):

    def setUp(self):
        data = dict(nome='luz')
        self.resp = self.client.post(reverse('despesas'), data=data)

    def test_name_template_despesa(self):
        self.assertContains(self.resp, '<input type="text" name="nome"')
        self.assertContains(self.resp, '<input type="number" name="valor"')
        #self.assertContains(self.resp, '<input type="date" name="data_pagamento"')


'''    def test_post(self):
       
       self.assertEqual(200, self.resp.status_code)
       
       
       self.assertContains(self.resp, 'value="luz"')'''