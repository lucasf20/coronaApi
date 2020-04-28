from rest_framework import routers, serializers, viewsets
from .models import *

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = paciente
        fields = '__all__'

class ExameSerializer(serializers.ModelSerializer):
    class Meta:
        model = exame
        fields = '__all__'