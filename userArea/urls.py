from . import views
from django.urls import path, include

app_name = "userArea"
urlpatterns = [
    path('', views.user_home, name="user_home"),
    path('servizi/', views.servizi_home, name="servizi_home"),
    path('servizi/lista/', views.servizi_all, name="servizi_all"),
    path('servizi/attivi/', views.servizi_attivi, name="servizi_attivi"),
    path('servizi/attivi/<int:pk>/', views.servizio_attivo_details,
         name="servizio_attivo_details"),
    path('servizi/recupero-credito/', include('recuperoCredito.urls')),
    path('articoli-salvati/', views.post_saved, name="post_saved"),
]
