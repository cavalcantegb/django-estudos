from rest_framework import serializers
from .models import *

class MaquinaSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = Maquina
        fields = ('isnMaquina', 
                  'placa_mae',
                  'placa_mae_descricao',
                  'processador',
                  'processador_descricao',
                  'placa_video',
                  'placa_video_descricao')

