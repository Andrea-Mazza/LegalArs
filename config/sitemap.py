from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticMap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'home',
            'privacyPage',
            'legalSharing',
            'estiaPartner',
            'chiSiamo',
            'diritto-civile',
            'diritto-penale',
            'diritto-amministrativo',
            'diritto-lavoro',
            'truffe-online',
            'separazioni-divorzi',
            'esdebitazione',
            'reati-ambientali',
            'mandato-europeo',
            'real-estate',
            'diffamazione',
            'colpa-medica',
            'rapporti-bancari',
            'tutela-immagine',
            'diritto-impresa',
            'permesso-soggiorno',
            'impresa-risanamento',
            'atti-esattoriali',
            'contatti',
            'ricerca',
        ]

    def location(self, item):
        return reverse(item)
