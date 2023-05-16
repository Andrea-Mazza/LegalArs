from django.shortcuts import get_object_or_404, render, redirect
from .models import Articolo, Categoria
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'news/home.html')


def articoli_home(request):
    post_list = Articolo.objects.order_by('-data_pubblicazione')
    paginator = Paginator(post_list, 9)
    page = request.GET.get('page')

    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)
    context = {'posts': posts}
    return render(request, 'news/articoli_home.html', context)


def articolo_details(request, categoria_slug, post_slug):
    category = Categoria.objects.get(slug=categoria_slug)
    post = Articolo.objects.get(slug=post_slug, categoria=category)
    context = {'post': post}
    return render(request, 'news/post_details.html', context)


def categoria_details(request, categoria_slug):
    category = Categoria.objects.get(slug=categoria_slug)
    post_list = Articolo.objects.filter(
        categoria=category).order_by('-data_pubblicazione')
    paginator = Paginator(post_list, 9)
    page = request.GET.get('page')

    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)
    context = {'posts': posts, 'categoria': category}
    return render(request, 'news/categoria_details.html', context)


@login_required
def save_article(request, article_id):
    article = get_object_or_404(Articolo, id=article_id)
    article.saved_by.add(request.user)
    article = get_object_or_404(Articolo, id=article_id)
    next_url = request.GET.get('next', '')
    return redirect(next_url)


@login_required
def remove_article(request, article_id):
    article = get_object_or_404(Articolo, id=article_id)
    article.saved_by.remove(request.user)
    article = get_object_or_404(Articolo, id=article_id)
    next_url = request.POST.get('next', '/')
    return redirect(next_url)


def vantaggi(request):
    return render(request, 'news/vantaggi.html')
