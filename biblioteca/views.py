from django.shortcuts import render

def inicio(request):
    return render(
        request,
        'inicio.html',
    )

def libros(request):
    return render(
        request,
        'libros.html',
    )

def autores(request):
    return render(
        request,
        'autores.html',
    )

def categorias(request):
    return render(
        request,
        'categorias.html',
    )