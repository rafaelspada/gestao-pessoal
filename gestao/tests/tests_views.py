from django.test import TestCase
from django.urls import reverse

class DespesaViewTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('despesas'))  # self.client simula uma requisição get, busca pelo nome

    def test_acesso_view_despesa(self):
        self.assertEqual(self.response.status_code, 200)

    def teste_template_view_despesa(self):
        self.assertTemplateUsed(self.response, 'cadastro_despesas.html')
