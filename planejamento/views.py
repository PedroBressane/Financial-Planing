from django.shortcuts import render
from perfil.models import Categoria
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.views.decorators.csrf import csrf_exempt
import json


def definir_planejamento(request):
    categorias = Categoria.objects.all()
    return render(request, 'definir_planejamento.html', {'categorias': categorias})

@csrf_exempt
def update_valor_categoria(request, id):
    novo_valor = json.load(request)['novo_valor']
    categoria = Categoria.objects.get(id=id)
    categoria.valor_planejamento = novo_valor
    categoria.save()
    messages.add_message(request,constants.SUCCESS, 'Categoria atualizada com sucesso')
    return JsonResponse({'status': 'Sucesso'})


def ver_planejamento(request):
    #realizar barra com total de gasto
    categorias = Categoria.objects.all()
    return render(request, 'ver_planejamento.html', {'categorias': categorias})
