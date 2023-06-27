# board/urls.py
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # /board/create/
    path('create/', views.create_feed, name='create_feed'),
    # /board/
    path('', views.feed_index, name='feed_index'),
    # /board/1/
    path('<int:feed_pk>/', views.feed_detail, name='feed_detail'),
    # /board/1/update/
    path('<int:feed_pk>/update/', views.update_feed, name='update_feed'),
    # /board/1/delete/
    path('<int:feed_pk>/delete/', views.delete_feed, name='delete_feed'),

    # /board/1/reactions/create/
    path('<int:feed_pk>/reactions/create', views.create_reaction, name='create_reaction'),
    # /board/1/reactions/1/delete/
    path('<int:feed_pk>/reactions/<int:reaction_pk>/delete/', views.delete_reaction, name='delete_reaction'),

    # /board/1/like/
    path('<int:feed_pk>/like/', views.like_feed, name='like_feed'),
]
