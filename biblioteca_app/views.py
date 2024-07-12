from django.shortcuts import render
from .forms import BibliotecaForm
from .models import Libro, Autor, Categoria, NavItem

# Create your views here.

def index(request):
    # Obtener datos necesarios para la página de inicio
    libros_destacados = Libro.objects.all()[:3] 
    jumbotron_info = {
        'titulo': 'Bienvenido a la biblioteca local online',
        'texto': 'Aquí encontrarás una gran colección de libros para leer y disfrutar.',
    }
    nav_items = NavItem.objects.all()

    context = {
        'libros_destacados': libros_destacados,
        'jumbotron_info': jumbotron_info,
        'nav_items': nav_items,
    }
    return render(request, 'biblioteca_app/index.html', context)

def libros(request):
    libros = Libro.objects.all()

    context = {
        'libros': libros,
    }
    return render(request, 'biblioteca_app/libros.html', context)

def autores(request):
    autores = Autor.objects.all()

    context = {
        'autores': autores,
    }
    return render(request, 'biblioteca_app/autores.html', context)

def categorias(request):
    categorias = Categoria.objects.all()

    context = {
        'categorias': categorias,
    }
    return render(request, 'biblioteca_app/categorias.html', context)

def formulario(request):
    form = BibliotecaForm()

    return render(
        request,
        'biblioteca_form.html',
        {'form': form}
    )

