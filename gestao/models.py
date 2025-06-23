from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Metodos(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Grupo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Despesa(models.Model):
    CHOICE_METODOS = [('AV','À Vista'),
                      ('AP','À Prazo'),
                      ('MS','Mensal')]

    nome = models.CharField(max_length=100)
    valor = models.FloatField()
    metodo_pagamento = models.CharField(choices=CHOICE_METODOS, max_length=2, default='AV')
    grupo_despesa = models.ForeignKey('Grupo', on_delete=models.CASCADE)
    metodos_despesa = models.ForeignKey('Metodos', on_delete=models.CASCADE)
    pessoa_despesa = models.ForeignKey('Pessoa', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Avista(models.Model):
    avista_despesa = models.ForeignKey('Despesa', on_delete=models.CASCADE)
    data_pagamento = models.DateField()

class Aprazo(models.Model):
    aprazo_despesa = models.ForeignKey('Despesa', on_delete=models.CASCADE)
    data_pagamento = models.DateField()
    parcelas = models.IntegerField()

class Mensal(models.Model):
    mensal_despesa = models.ForeignKey('Despesa', on_delete=models.CASCADE)
    dia_pagamento = models.IntegerField()
    ativo = models.BooleanField(default=True)
