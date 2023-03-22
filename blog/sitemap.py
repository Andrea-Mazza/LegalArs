from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Articolo, Categoria, Fonti


class ArticoloSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return Articolo.objects.all()

    def location(self, obj):
        return reverse('blog_news_details', args=[obj.slug])


class CategoriaSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return Categoria.objects.all()

    def location(self, obj):
        return reverse('blog_category_details', args=[obj.slug])


class FontiSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return Fonti.objects.all()

    def location(self, obj):
        return reverse('blog_category_details', args=[obj.slug])
