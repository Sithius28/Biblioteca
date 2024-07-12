from django.urls import path, include
from . import views

app_name = 'biblioteca_app'


urlpatterns = [
	path('index', views.index, name="index"),
    path('formulario', views.formulario, name='formulario'),
	]