from django.shortcuts import render,redirect
from rest_framework import viewsets
from rest_framework.response import Response
from .models import paciente, exame
from rest_framework.decorators import action
from .serializers import PacienteSerializer, ExameSerializer
from .predictor import predict_covid
from django.utils.timezone import localtime

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = paciente.objects.all()
    serializer_class = PacienteSerializer
        
class ExameViewSet(viewsets.ModelViewSet):
    queryset = exame.objects.all()
    serializer_class = ExameSerializer

    def create(self, request, *args, **kwargs):
        exa = exame()
        pac = paciente.objects.get(cpf = request.data['cpf'])
        exa.Paciente = pac
        exa.radiografia = request.data['radiografia']
        pred = predict_covid(request.data['radiografia'])
        exa.h1n1 = pred[0]
        exa.gripe_comum = pred[1]
        exa.covid = pred[2]
        exa.data = localtime()
        exa.save()
        return redirect("/exames/"+str(exa.id_exame))

# Create your views here.
