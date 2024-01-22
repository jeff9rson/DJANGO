from django.shortcuts import render,redirect
from .models import Food, Consumed 
def index(request):
    if request.method == 'POST':
        comida_consumida = request.POST[' comida_consumida']
        consumo = Food.objects.get(name=comida_consumida)

        user = request.user
        consumo = Consumed(user=user,comida_consumida=consumo)
        consumo.save()

        foods = Food.objects.all()
    else:
        foods = Food.objects.all()

    comida_consumida = Consumed.objects.filter(user=request.user)

    return render(request, 'nutrion/index.html', {'foods': foods, 'comida_consumida': comida_consumida})
def delete_comida(request, id):
    comida_consumida = Consumed.objects.get(id=id)
    if request.method == 'POST':
        comida_consumida.delete()
        return redirect('/')
    return render(request, 'nutrion/delete.html')