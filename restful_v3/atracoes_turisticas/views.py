from django.shortcuts import render
from atracoes_turisticas.models import AtracaoTuristica

def index(request):
    atracoes_turisticas = AtracaoTuristica.objects.all()
    return render(request, 'atracoes_turisticas/index.html', {'atracoes_turisticas': atracoes_turisticas})