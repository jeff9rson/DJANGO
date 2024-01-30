from django.db import models
class Reunioes(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=150)
    local = models.CharField(max_length=60)
    nome_do_participante = models.TextField(max_length=50)
    dia_e_horario = models.DateTimeField(max_length=50)

    def __str__(self):
        return self.titulo