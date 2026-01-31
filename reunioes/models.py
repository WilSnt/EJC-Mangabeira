from django.db import models

from django.db import models
from circulos.models import Circulo

class Reuniao(models.Model):
    TIPO_CHOICES = (
        ('GERAL', 'Geral'),
        ('CIRCULO', 'Círculo'),
    )

    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    data = models.DateField()
    circulo = models.ForeignKey(
        Circulo,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.tipo} - {self.data}"
from django.db import models
from circulos.models import Circulo

class Reuniao(models.Model):
    titulo = models.CharField(max_length=100)
    data = models.DateField()
    circulo = models.ForeignKey(
        Circulo,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.titulo
from django.db import models
from circulos.models import Circulo