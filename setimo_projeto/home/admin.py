from django.contrib import admin
from .models import Produto

class Listproduto(admin.ModelAdmin):
    list_display = ('nome_produto','descricao','categoria','preco')

admin.site.register(Produto, Listproduto)
