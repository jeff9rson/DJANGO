from rest_framework import viewssets
from .seriealizers import PontoTuristicoSerializer
from pontos_turisticos.models import PontoTuristico

class PontoTuristoViewSet(viewssets.modelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer