from rest_framework import routers, serializers, viewsets
from .models import *

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = paciente
        # fields = ('cpf', 'nome', 'sexo', 'idade', 'doenca', 'nome_doenca', 'observacao', 'radiografia')
        fields = '__all__'