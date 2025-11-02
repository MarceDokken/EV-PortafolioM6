from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recetas/', views.lista_recetas, name='lista_recetas'),
    path('recetas/<int:receta_id>/', views.detalle_receta, name='detalle_receta'),
]