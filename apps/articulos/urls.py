from django.urls import path
from .views import PostListView, PostDetailView


urlpatterns = [
    path('articulos/', PostListView.as_view(), name='articulos'),
    path('articulos/<int:id>/', PostDetailView.as_view(), name='articulo_ind'),
]