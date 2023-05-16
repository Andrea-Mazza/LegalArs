from django.urls import path
from . import views

app_name = 'recupero_credito'

urlpatterns = [
    path('pratica/<int:pratica_id>', views.pratica_details, name='pratica_details'),
]
