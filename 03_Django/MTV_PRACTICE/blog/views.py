from django.shortcuts import render, redirect

from .models import Posting


def new(request):
    return render(request, 'blog/new.html')


def create(request):
    posting = Posting()
    posting.title = request.POST['title']
    posting.content = request.POST['content']
    posting.rank = request.POST['rank']
    posting.save()
    return redirect('blog:detail', posting.pk)


def index(request):
    postings = Posting.objects.all()
    return render(request, 'blog/index.html', {
        'postings': postings,
    })


def detail(request, pk):
    posting = Posting.objects.get(pk=pk)
    return render(request, 'blog/detail.html', {
        'posting': posting,
    })


def edit(request, pk):
    posting = Posting.objects.get(pk=pk)
    return render(request, 'blog/edit.html', {
        'posting': posting,
    })


def update(request, pk):
    posting = Posting.objects.get(pk=pk)
    posting.title = request.POST['title']
    posting.content = request.POST['content']
    posting.rank = request.POST['rank']
    posting.save()
    return redirect('blog:detail', posting.pk)


def delete(request, pk):
    if request.method == 'POST':
        posting = Posting.objects.get(pk=pk)
        posting.delete()
    return redirect('blog:index')
    