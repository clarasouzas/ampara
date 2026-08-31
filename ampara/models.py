from django.db import models

class Impacto(models.Model):
    mulheres_conectadas = models.IntegerField()
    publicacoes_compartilhadas = models.IntegerField()
    conteudos_informativos = models.IntegerField()

class Depoimento(models.Model):
    nome = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    descricao = models.CharField(max_length=10000)
    anonimo = models.BooleanField(default=True) 


