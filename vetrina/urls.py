from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'vetrina'

urlpatterns = [
    path('', views.home, name='home'),
    path('legal-sharing/', views.legal_sharing, name='legal_sharing'),
    path('estia/', views.estia, name='estia'),
    path('chi-siamo/', views.chi_siamo, name='chi_siamo'),
    path('aree-di-attività/diritto-civile/',
         views.diritto_civile, name='diritto_civile'),
    path('aree-di-attività/diritto-penale/',
         views.diritto_penale, name='diritto_penale'),
    path('aree-di-attività/diritto-amministrativo/',
         views.diritto_amministrativo, name='diritto_amministrativo'),
    path('aree-di-attività/diritto-del-lavoro/',
         views.diritto_lavoro, name='diritto_lavoro'),
    path('servizi/investimenti-e-truffe-online/',
         views.investimenti_truffe, name='investimenti_truffe'),
    path('servizi/separazioni-e-divorzi/',
         views.separazioni_divorzi, name='separazioni_divorzi'),
    path('servizi/esdebitazione/', views.esdebitazione, name='esdebitazione'),
    path('servizi/reati-ambientali/',
         views.reati_ambientali, name='reati_ambientali'),
    path('servizi/mandato-di-arresto-europeo/',
         views.mandato_eu, name='mandato_eu'),
    path('servizi/real-estate/', views.real_estate, name='real_estate'),
    path('servizi/diffamazione-a-mezzo-di-stampa/',
         views.diffamazione_stampa, name='diffamazione_stampa'),
    path('servizi/colpa-medica/', views.colpa_medica, name='colpa_medica'),
    path('servizi/tutela-nei-rapporti-bancari/',
         views.rapporti_bancari, name='rapporti_bancari'),
    path('servizi/tutela-dell-immagine-sul-web/',
         views.tutela_immagine, name='tutela_immagine'),
    path('servizi/diritto-di-impresa/',
         views.diritto_impresa, name='diritto_impresa'),
    path('servizi/permesso-di-soggiorno/',
         views.permesso_soggiorno, name='permesso_soggiorno'),
    path('servizi/crisi-di-impresa-e-risanamento-aziendale/',
         views.impresa_risanamento, name='impresa_risanamento'),
    path('servizi/tutela-avverso-atti-esattoriali/',
         views.atti_esattoriali, name='atti_esattoriali'),
    path('contatti/', views.contattaci, name='contatti'),
    path('privacy/', views.privacy, name='privacy'),
    path('ricerca/', views.ricerca, name='ricerca'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
