from . import models
from django.forms import ModelForm

class BibliotecaForm(ModelForm):
    class Meta:
        model = models.Libro
        fields = ['titulo', 'año_publicacion', 'descripcion', 'autor', 'categorias']
