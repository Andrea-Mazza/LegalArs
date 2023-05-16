from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('bacheca/', views.bacheca, name='bacheca'),
    path('impostazioni_account/', views.impostazioni_account,
         name='impostazioni_account'),
    path('articoli_salvati/', views.articoli_salvati, name='articoli_salvati'),
    path('servizi/', views.scopri_servizi, name='servizi'),
    path('servizi-attivati/', views.miei_servizi, name='miei_servizi'),
    path('servizi/<slug:servizio_slug>/',
         views.spiegazione_servizio, name='spiegazione_servizio'),
]
