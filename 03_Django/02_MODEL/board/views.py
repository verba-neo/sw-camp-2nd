from django.shortcuts import render, redirect

from .models import Article


# 게시글 작성용 HTML 제공
def new(request):    
    return render(request, 'board/new.html')


# 게시글 DB에 저장 => redirect
def create(request):
    article = Article()
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    return redirect('board:detail', article.pk)


# 전체 게시글 조회
def index(request):
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        'articles': articles,
    })


# 단일 게시글 조회
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'board/detail.html', {
        'article': article,
    })


# 게시글 수정용 HTML
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'board/edit.html', {
        'article': article,
    })


# 게시글 수정 저장 => redirect
def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    return redirect('board:detail', article.pk)


# 단일 게시글 삭제
def delete(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('board:index')


