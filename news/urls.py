from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.home, name='home'),
    path('articoli/', views.articoli_home, name='articoli_home'),
    path('vantaggi/', views.vantaggi, name='vantaggi'),
    path('<slug:categoria_slug>/<slug:post_slug>/',
         views.articolo_details, name='articolo_details'),
    path('<slug:categoria_slug>/', views.categoria_details,
         name='categoria_details'),
    path('articles/<int:article_id>/save/',
         views.save_article, name='save_article'),
    path('articles/<int:article_id>/remove/',
         views.remove_article, name='remove_article'),
]
