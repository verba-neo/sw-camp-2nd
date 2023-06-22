from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required 

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


@login_required
@require_http_methods(['GET', 'POST'])
def create_article(request):
    if request.method == 'GET':
        form = ArticleForm()
    
    elif request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # user 정보 없음 => article 저장 불가능 => 저장 직전 STOP
            article = form.save(commit=False)
            # 이 article의 작성자 = 이 요청을 보낸 사용자
            article.user = request.user
            article.save()
            return redirect('board:article_detail', article.pk)

    return render(request, 'board/form.html', {
        'form': form,
    })


@require_safe
def article_index(request):
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        'articles': articles,
    })


@require_safe
def article_detail(request, article_pk):
    """
    try:
        article = Article.objects.get(pk=article_pk)
    except:
        # 응답. code 404
        from django.http import HttpResponseNotFound
        return HttpResponseNotFound('hihi')
        # 에러. code 404
        from django.http import Http404
        raise Http404()
    """
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    form = CommentForm()

    return render(request, 'board/detail.html', {
        'article': article,
        'comments': comments,
        'form': form,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def update_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.user != article.user:    
        return redirect('board:article_detail', article.pk)

    if request.method == 'GET':
        form = ArticleForm(instance=article)
    else:
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('board:article_detail', article.pk)

    return render(request, 'board/form.html', {
        'form': form,
    })


@login_required
@require_POST
def delete_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.user != article.user:    
        return redirect('board:article_detail', article.pk)

    article.delete()
    return redirect('board:article_index')


@login_required
@require_POST
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)  # 저장 멈춰!
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('board:article_detail', article.pk)


@login_required
@require_POST
def delete_comment(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user != comment.user:    
        return redirect('board:article_detail', article.pk)

    comment.delete()
    return redirect('board:article_detail', article.pk)
