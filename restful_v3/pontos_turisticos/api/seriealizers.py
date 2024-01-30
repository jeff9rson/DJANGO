from rest_framework import seriealizers
from pontos_turisticos.models import PontoTuristico

class PontoTuristicoSerializer(seriealizers.ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = '__all__'