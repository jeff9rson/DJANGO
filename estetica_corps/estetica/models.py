from django.db import models

class Estetica(models.Model):
    cabelos = models.CharField(max_length=50,blank=False)
    unhas = models.CharField(max_length=60)
    limpeza_de_pele = models.CharField(max_length=50)

def __str__(self):
    return self.nome
