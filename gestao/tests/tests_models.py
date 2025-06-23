import datetime

from django.test import TestCase

from ..models import Despesa, Avista, Aprazo, Mensal, Pessoa, Metodos, Grupo

class Teste_despesa_Mensal(TestCase):

    #setup inicial, criação de objeto
    def setUp(self):
        grupo = Grupo.objects.create(nome='Casa')
        metodos = Metodos.objects.create(nome='Cartão')
        pessoa = Pessoa.objects.create(nome='Rafael')

        Despesa.objects.create(nome='Despesa 1',
                               valor=15,
                               metodo_pagamento='AV',
                               grupo_despesa=grupo,
                               metodos_despesa=metodos,
                               pessoa_despesa=pessoa
                              )

    def test_retorno_despesa(self):
        d1 = Despesa.objects.get(nome='Despesa 1')
        self.assertEqual(d1.metodo_pagamento, 'AV')

    def test_metodo_av(self):
        av1 = Avista.objects.create(avista_despesa=Despesa.objects.get(id=1),
                                    data_pagamento='2025-06-23')
        print(av1.data_pagamento)
        self.assertEqual(av1.data_pagamento, '2025-06-23')
