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
    nome = models.CharField(max_length=100)
    valor = models.FloatField()
    data = models.DateField()
    parcela = models.FloatField()
    grupo_despesa = models.ForeignKey('Grupo', on_delete=models.CASCADE)
    metodos_despesa = models.ForeignKey('Metodos', on_delete=models.CASCADE)
    pessoa_despesa = models.ForeignKey('Pessoa', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
