from django.db import models

class Circulo(models.Model):
    nome = models.CharField(max_length=20)
    cor = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    