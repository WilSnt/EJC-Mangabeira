from django.db import models

from django.db import models
from circulos.models import Circulo

class Jovem(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    circulo = models.ForeignKey(Circulo, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
from django.db import models
from circulos.models import Circulo

class Jovem(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=50)
    circulo = models.ForeignKey(Circulo, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
from django.db import models
from circulos.models import Circulo