from django.urls import path
from . import views

app_name = 'recupero_credito'

urlpatterns = [
    path('pratica/<int:pratica_id>', views.pratica_details, name='pratica_details'),
    path('get-tipo-creditore/', views.get_tipo_creditore,
         name='get_tipo_creditore'),
    path('get-cr-pf-form/', views.get_cr_pf_form, name="get_cr_pf_form"),
    path('get-cr-pj-form/', views.get_cr_pj_form, name="get_cr_pj_form"),
    path('get-tipo-debitore/', views.get_tipo_debitore,
         name='get_tipo_debitore'),
    path('get-db-pf-form/', views.get_db_pf_form, name="get_db_pf_form"),
    path('get-db-pj-form/', views.get_db_pj_form, name="get_db_pj_form"),
    path('get-somma/', views.get_somma, name='get_somma'),
    path('get-firma/', views.get_firma, name='get_firma'),
    path('get-documenti/', views.get_documenti_firma, name='get_documenti'),
    path('check-fields/', views.check_fields,
         name='check-fields'),

    path('give-preventivo/', views.give_preventivo, name='give_preventivo'),

]