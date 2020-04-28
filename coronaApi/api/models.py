from django.db import models
from .predictor import predict_covid

# Create your models here.

class paciente(models.Model):
    cpf = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length = 200)
    sexo = models.CharField(max_length=10)
    idade = models.IntegerField()
    doenca = models.BooleanField()
    nome_doenca = models.CharField(max_length = 1000, null= True)
    observacao = models.CharField(max_length = 1000, null= True)
    radiografia = models.TextField()
    
    def __str__(self):
        return str(self.nome)

class exame(models.Model):
    id_exame = models.AutoField(primary_key=True)
    Paciente = models.ForeignKey(paciente, on_delete=models.CASCADE, editable=False)
    h1n1 = models.FloatField(editable=False, null=True)
    gripe_comum = models.FloatField(editable=False, null=True)
    covid = models.FloatField(editable=False, null=True)
    radiografia = models.TextField(editable=False)
    data = models.DateTimeField(editable=False)

    def __str__(self):
        return self.Paciente.nome