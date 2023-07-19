from django.shortcuts import render
from .models import Articulo
from django.views.generic import ListView, DetailView

# Create your views here.

class PostListView(ListView):
    model = Articulo
    template_name = 'articulos/articulos.html'
    context_object_name = 'articulos'

class PostDetailView(DetailView):
    model = Articulo
    template_name = 'articulos/articulo_ind.html'
    context_object_name = 'articulos'
    pk_url_kwarg = 'id'
    queryset = Articulo.objects.all()