from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'ingredientes', 'instrucciones', 'tiempo_preparacion', 'porciones', 'categoria']
        widgets = {
            'ingredientes': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Ingresa cada ingrediente en una línea...'}),
            'instrucciones': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Describe los pasos de preparación...'}),
            'titulo': forms.TextInput(attrs={'placeholder': 'Ej: Pastel de Chocolate'}),
        }
        labels = {
            'titulo': 'Título de la Receta',
            'ingredientes': 'Ingredientes',
            'instrucciones': 'Instrucciones',
            'tiempo_preparacion': 'Tiempo de Preparación (minutos)',
            'porciones': 'Porciones',
            'categoria': 'Categoría',
        }