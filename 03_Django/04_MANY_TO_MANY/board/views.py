from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

from .models import Feed, Reaction
from .forms import FeedForm, ReactionForm


@login_required
@require_http_methods(['GET', 'POST'])
def create_feed(request):
    if request.method == 'GET':
        form = FeedForm()
    
    else:
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.author = request.user
            feed.save()
            return redirect('board:feed_detail', feed.pk)

    return render(request, 'board/form.html', {
        'form': form,
    })


@require_safe
def feed_index(request):
    feeds = Feed.objects.all()
    return render(request, 'board/index.html', {
        'feeds': feeds,
    })


@require_safe
def feed_detail(request, feed_pk):
    feed = get_object_or_404(Feed, pk=feed_pk)
    reactions = feed.reactions.all()
    form = ReactionForm()

    return render(request, 'board/detail.html', {
        'feed': feed,
        'reactions': reactions,
        'form': form,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def update_feed(request, feed_pk):
    feed = get_object_or_404(Feed, pk=feed_pk)

    if request.user != feed.author:    
        return redirect('board:feed_detail', feed.pk)

    if request.method == 'GET':
        form = FeedForm(instance=feed)
    else:
        form = FeedForm(request.POST, instance=feed)
        if form.is_valid():
            feed = form.save()
            return redirect('board:feed_detail', feed.pk)

    return render(request, 'board/form.html', {
        'form': form,
    })


@login_required
@require_POST
def delete_feed(request, feed_pk):
    feed = get_object_or_404(Feed, pk=feed_pk)

    if request.user != feed.author:    
        return redirect('board:feed_detail', feed.pk)

    feed.delete()
    return redirect('board:feed_index')


@login_required
@require_POST
def create_reaction(request, feed_pk):
    feed = get_object_or_404(Feed, pk=feed_pk)
    form = ReactionForm(request.POST)
    if form.is_valid():
        reaction = form.save(commit=False)
        reaction.feed = feed
        reaction.author = request.user
        reaction.save()
        return redirect('board:feed_detail', feed.pk)


@login_required
@require_POST
def delete_reaction(request, feed_pk, reaction_pk):
    feed = get_object_or_404(Feed, pk=feed_pk)
    reaction = get_object_or_404(Reaction, pk=reaction_pk)

    if request.user != reaction.author:    
        return redirect('board:feed_detail', feed.pk)

    reaction.delete()
    return redirect('board:feed_detail', feed.pk)
