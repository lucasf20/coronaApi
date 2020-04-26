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
        pac.h1n1 = predict_covid(pac.radiografia)[0]
        pac.gripe_comum = predict_covid(pac.radiografia)[1]
        pac.covid = predict_covid(pac.radiografia)[2]
        pac.save()
        return redirect("/pacientes/"+pk+"/")
        

# Create your views here.
