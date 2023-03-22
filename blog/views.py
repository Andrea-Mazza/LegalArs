from django.shortcuts import redirect, render, get_object_or_404
from .models import Articolo, Categoria, FontiCategoria, Fonti
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required


# Create your views here.


def blogHome(request):
    return render(request, 'blog_home.html')


def blogNews(request):
    post_list = Articolo.objects.order_by('-publish')
    paginator = Paginator(post_list, 9)
    page = request.GET.get('page')

    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)
    context = {'posts': posts}
    return render(request, 'blog_news.html', context)


def blog_news_details(request, slug):
    posts = get_object_or_404(Articolo, slug=slug)
    if request.method == 'POST':
        article_id = request.POST.get('article_id')
        if article_id:
            article = get_object_or_404(Articolo, id=article_id)
            if request.user in article.saved_by.all():
                article.saved_by.remove(request.user)
            else:
                article.saved_by.add(request.user)
    context = {'posts': posts}
    return render(request, 'blog_news_details.html', context)


def blog_category_details(request, slug):
    category = Categoria.objects.get(slug=slug)
    posts = Articolo.objects.filter(categoria=category)
    return render(request, 'blog_category_details.html', {'posts': posts, 'categoria': category})


def blogFonti(request):
    fonti = Fonti.objects.all()
    fonti_categoria = FontiCategoria.objects.all().order_by('nome')
    context = {'fonti': fonti, 'fonti_categoria': fonti_categoria}
    return render(request, 'blog_fonti.html', context)


def blogFonti_details(request, slug):
    fonte = get_object_or_404(Fonti, slug=slug)
    fonti = Fonti.objects.all()
    fonti_categoria = FontiCategoria.objects.all().order_by('nome')
    context = {'fonte': fonte, 'fonti': fonti,
               'fonti_categoria': fonti_categoria}
    return render(request, 'blog_fonti_details.html', context)


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


def blogVantaggi(request):
    return render(request, 'vantaggi.html')
