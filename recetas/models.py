from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    ingredientes = models.TextField(verbose_name="Ingredientes")
    instrucciones = models.TextField(verbose_name="Instrucciones")
    tiempo_preparacion = models.IntegerField(
        verbose_name="Tiempo de preparación (minutos)"
    )
    porciones = models.IntegerField(verbose_name="Porciones")
    categoria = models.CharField(
        max_length=100,
        choices=[
            ('desayuno', 'Desayuno'),
            ('almuerzo', 'Almuerzo'),
            ('cena', 'Cena'),
            ('postre', 'Postre'),
        ],
        verbose_name="Categoría"
    )
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"