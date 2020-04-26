from django.db import models
from .predictor import predict_covid

# Create your models here.

class paciente(models.Model):
    cpf = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length = 200)
    sexo = models.CharField(max_length=10)
    idade = models.IntegerField()
    doenca = models.BooleanField()
    nome_doenca = models.CharField(max_length = 1000)
    observacao = models.CharField(max_length = 1000)
    radiografia = models.TextField()
    h1n1 = models.IntegerField(editable=False, null=True)
    gripe_comum = models.IntegerField(editable=False, null=True)
    covid = models.IntegerField(editable=False, null=True)

    def __str__(self):
        return str(self.nome)