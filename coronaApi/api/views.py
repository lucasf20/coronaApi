from django.shortcuts import render,redirect
from rest_framework import viewsets
from rest_framework.response import Response
from .models import paciente
from rest_framework.decorators import action
from .serializers import PacienteSerializer
from .predictor import predict_covid

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = paciente.objects.all()
    serializer_class = PacienteSerializer

    @action(detail=True, methods=['get'])
    def calculate(self,request,pk):
        pac = paciente.objects.get(cpf = pk)
        pred = predict_covid(pac.radiografia)
        pac.h1n1 = pred[0]
        pac.gripe_comum = pred[1]
        pac.covid = pred[2]
        pac.save()
        return redirect("/pacientes/"+pk+"/")
        

# Create your views here.
