from django.db import models

from django.db import models
from jovens.models import Jovem
from reunioes.models import Reuniao

class Presenca(models.Model):
    jovem = models.ForeignKey(Jovem, on_delete=models.CASCADE)
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE)
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.jovem} - {self.reuniao}"
from django.db import models
from jovens.models import Jovem
from reunioes.models import Reuniao

class Presenca(models.Model):
    jovem = models.ForeignKey(Jovem, on_delete=models.CASCADE)
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE)
    presente = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.jovem} - {self.reuniao}'
from django.db import models
from jovens.models import Jovem