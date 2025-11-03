from django.shortcuts import render
from .models import Receta

def lista_recetas(request):
    """Vista para listar todas las recetas"""
    recetas = Receta.objects.all().order_by('-fecha_creacion')
    return render(request, 'recetas/lista_recetas.html', {'recetas': recetas})

def detalle_receta(request, receta_id):
    """Vista para ver el detalle de una receta"""
    receta = Receta.objects.get(id=receta_id)
    return render(request, 'recetas/detalle_receta.html', {'receta': receta})

def home(request):
    """Página de inicio"""
    return render(request, 'recetas/home.html')