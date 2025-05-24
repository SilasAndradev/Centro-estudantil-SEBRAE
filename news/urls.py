from django.urls import path

from news.views import (
    NoticiaPublicar, 
    NoticiaEditar, 
    NoticiaExcluir, 
    NoticiaPage, 
    Procurar,
    RedirectToHome,
    HomePage
    )

urlpatterns = [
    path('publicar/', NoticiaPublicar, name='publicar'),
    path('editar/<str:pk>/', NoticiaEditar, name='editar'),
    path('excluir/<str:pk>/', NoticiaExcluir, name='excluir'),
    path('noticia/<str:pk>/', NoticiaPage, name='noticia'),
    path('noticia/feed/', NoticiaPage, name='feed'),
    path('noticia/', RedirectToHome),
    path('', HomePage),
    path('procurar/', Procurar, name='procurar'),

]