from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recetas/', views.lista_recetas, name='lista_recetas'),
    path('recetas/<int:receta_id>/', views.detalle_receta, name='detalle_receta'),    
    
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('mis-recetas/', views.mis_recetas, name='mis_recetas'),       
    path('crear-receta/', views.crear_receta, name='crear_receta'),
]