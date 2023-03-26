from . import views
from django.urls import path, include
from recuperoCredito.views import CreateCheckoutSessionView, SuccessView, CancelView
from config.writing_script.procura_speciale import write_procura_speciale

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
    path('create-checkout-session/<int:pk>/',
         CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('success/', SuccessView, name="success"),
    path('cancel/', CancelView.as_view(), name="cancel"),
    path('procura-special/<int:pk>/',
         write_procura_speciale, name="procura-script"),
]
