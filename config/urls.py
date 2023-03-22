"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import ArticoloSitemap, CategoriaSitemap, FontiSitemap
from .sitemap import StaticMap
from django.conf.urls import handler404


sitemaps = {
    'staticMap': StaticMap,
    'articoloMap': ArticoloSitemap,
    'categoriaMap': CategoriaSitemap,
    'fontiMap': FontiSitemap,
}

urlpatterns = [
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('informativa-privacy/', views.privacyPage, name='privacyPage'),
    path('legal-sharing/', views.legalSharing, name='legalSharing'),
    path('partnership-estia-legalars/', views.estiaPartner, name='estiaPartner'),
    path('chi-siamo/', views.chiSiamo, name="chiSiamo"),
    path('diritto-civile/', views.dirittoCivile, name="diritto-civile"),
    path('diritto-penale/', views.dirittoPenale, name="diritto-penale"),
    path('diritto-amministrativo', views.dirittoAmm,
         name="diritto-amministrativo"),
    path('diritto-del-lavoro/', views.dirittoLavoro, name="diritto-lavoro"),
    path('investimenti-e-truffe-online',
         views.truffeOnline, name="truffe-online"),
    path('separazioni-e-divorzi/', views.divorzi, name="separazioni-divorzi"),
    path('esdebitazione/', views.esdebitazione, name="esdebitazione"),
    path('reati-ambientali/', views.reatiAmbientali, name="reati-ambientali"),
    path('mandato-di-arresto-europeo/', views.mandatoUe, name="mandato-europeo"),
    path('real-estate/', views.realEstate, name="real-estate"),
    path('diffamazione-a-mezzo-stampa/',
         views.diffamazione, name="diffamazione"),
    path('colpa-medica/', views.colpaMedica, name="colpa-medica"),
    path('tutela-nei-rapporti-bancari/',
         views.rapportiBancari, name="rapporti-bancari"),
    path('tutela-dellimmagine-sul-web/',
         views.tutelaImmagine, name="tutela-immagine"),
    path('diritto-di-impresa/', views.dirittoImpresa, name="diritto-impresa"),
    path('permesso-di-soggiorno/', views.permessoSoggiorno,
         name="permesso-soggiorno"),
    path('crisi-di-impresa-e-risanamento-aziendale/',
         views.impresaRisanamento, name="impresa-risanamento"),
    path('tutela-avverso-atti-esattoriali/',
         views.attiEsattoriali, name="atti-esattoriali"),
    path('contatti/', views.contatti, name="contatti"),
    #     path('registrazione/', views.register, name="registrazione"),
    path('accesso/', views.login, name="accesso"),
    path('registrazione/', views.signup, name="registrazione"),
    path('logout/', views.logout_view, name='logout'),
    path('blog/', include('blog.urls')),
    path('area-personale/', include('userArea.urls')),
    path('password_reset/', views.password_reset.as_view(), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', views.CustomPasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('ricerca/', views.ricerca, name="ricerca"),
    path('homepage-new/press-area/',
         views.redirectPressArea),
    path('partnership-tra-estia-e-legal-ars/', views.redirectEstia),
    path('<slug:slug>/', views.redirect_blog_article),
    path('homepage-new/fonti-normative/', views.redirectFonti),
    path('homepage-new/fonti-normative/<slug:slug>/', views.redirectFontiDetails),
    path('homepage-new/chi-siamo/', views.redirectChiSiamo),
    path('homepage-new/diritto-civile-3/', views.redirectCivile),
    path('homepage-new/diritto-penale-3/', views.redirectPenale),
    path('homepage-new/diritto-amministrativo-3/', views.redirectAmministrativo),
    path('homepage-new/diritto-del-lavoro/', views.redirectLavoro),
    path('homepage-new/investimenti-e-truffe-online/', views.redirectInvestimenti),
    path('homepage-new/separazioni-e-divorzi/', views.redirectDivorzi),
    path('homepage-new/esdebitazione-2/', views.redirectEsdebitazione),
    path('homepage-new/reati-ambientali-2/', views.redirectAmbiente),
    path('homepage-new/mandato-di-arresto-europeo/', views.redirectMandato),
    path('homepage-new/real-estate/', views.redirectEstate),
    path('homepage-new/diffamazione-a-mezzo-di-stampa/',
         views.redirectDiffamazione),
    path('homepage-new/colpa-medica-2/',
         views.redirectMedica),
    path('homepage-new/tutela-nei-rapporti-bancari/',
         views.redirectBanca),
    path('homepage-new/tutela-dellimmagine-sul-web/',
         views.redirectImmagine),
    path('homepage-new/diritto-di-impresa-3/',
         views.redirectImpresa),
    path('homepage-new/permesso-di-soggiorno/',
         views.redirectSoggiorno),
    path('homepage-new/crisi-di-impresa-e-risanamento-aziendale/',
         views.redirectRisanamento),
    path('homepage-new/tutela-avverso-atti-esattoriali/',
         views.redirectEsattoriali),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.error_404
