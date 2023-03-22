from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHome, name='blog-home'),
    path('articoli-giuridici/', views.blogNews, name='blog-news'),
    path('articoli-giuridici/<slug:slug>/',
         views.blog_news_details, name='blog_news_details'),
    path('categoria/<slug:slug>/', views.blog_category_details,
         name='blog_category_details'),
    path('fonti-normative/', views.blogFonti, name='blog-fonti'),
    path('fonti-normative/<slug:slug>/',
         views.blogFonti_details, name='blog_fonti_details'),
    path('articles/<int:article_id>/save/',
         views.save_article, name='save_article'),
    path('articles/<int:article_id>/remove/',
         views.remove_article, name='remove_article'),
    path('vantaggi/', views.blogVantaggi, name='blog-vantaggi'),
]
