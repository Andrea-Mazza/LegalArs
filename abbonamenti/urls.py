from django.urls import path
from . import views

app_name = 'abbonamenti'

urlpatterns = [
    path('success/', views.checkout_success, name="success"),
    path('cancel/', views.checkout_cancel, name="cancel"),
    path('customer-portal-session/', views.customer_portal_session,
         name='customer_portal_session'),

    path('checkout/<slug:servizio_slug>/',
         views.create_checkout_session, name='create_checkout_session'),
]
