from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  
from django.contrib.auth.decorators import login_required  
from .models import Receta
from .forms import RecetaForm 

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

def registro(request):
    """Vista para registrar nuevos usuarios"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'recetas/registro.html', {'form': form})

def login_view(request):
    """Vista para iniciar sesión"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'recetas/login.html', {'form': form})

def logout_view(request):
    """Vista para cerrar sesión"""
    logout(request)
    return redirect('home')

@login_required
def mis_recetas(request):
    """Vista para ver las recetas del usuario actual"""
    recetas = Receta.objects.filter(autor=request.user).order_by('-fecha_creacion')
    return render(request, 'recetas/mis_recetas.html', {'recetas': recetas})

@login_required
def crear_receta(request):
    """Vista para crear nuevas recetas"""
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.autor = request.user
            receta.save()
            return redirect('mis_recetas')
    else:
        form = RecetaForm()
    
    return render(request, 'recetas/crear_receta.html', {'form': form})