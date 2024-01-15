from django.db import models

class Cliente(models.Model):
    nome = models.CharField('nome', max_length=30)
    sobrenome = models.CharField('sobrenome', max_length=30)