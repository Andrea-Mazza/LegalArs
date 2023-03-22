from django.urls import path
from . import views

urlpatterns = [
    path('creditore/', views.start, name="recupero-credito-start"),
    path('creditore/dati/', views.dati_creditore, name='dati_creditore'),
    # path('debitore/', views.numero_debitori, name='numero_debitori'),
    path('debitore/tipo', views.tipo_debitore, name='tipo_debitore'),
    path('debitore/dati/', views.dati_debitore, name='dati_debitore'),
    path('credito/', views.credito, name="credito"),
    path('fine/', views.end, name="end"),
    # path('fattura/', views.fattura, name="fattura"),
    # path('pdf/', views.generate_pdf, name="pdf"),
]
