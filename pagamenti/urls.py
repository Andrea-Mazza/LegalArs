from django.urls import path
from . import views

app_name = 'pagamenti'

urlpatterns = [
    path('checkout_session/<slug:servizio_slug>/<uuid:pratica>/', views.create_checkout_session,
         name="checkout_session"),
    path('success/<slug:servizio_slug>/<uuid:pratica>/',
         views.checkout_success, name="success"),
    path('cancel/<slug:servizio_slug>/<uuid:pratica>/',
         views.checkout_cancel, name="cancel"),
]
