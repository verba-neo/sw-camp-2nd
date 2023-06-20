from django.shortcuts import render, redirect

from .models import Article
from .forms import ArticleForm


def create_article(request):
    if request.method == 'GET':
        form = ArticleForm()
    
    elif request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('board:article_detail', article.pk)

    return render(request, 'board/form.html', {
        'form': form,
    })


def article_index(request):
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        'articles': articles,
    })


def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    return render(request, 'board/detail.html', {
        'article': article,
    })


def update_article(request, article_pk):
    pass


def delete_article(request, article_pk):
    pass

