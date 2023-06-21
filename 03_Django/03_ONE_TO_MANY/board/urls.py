from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # /board/create/
    path('create/', views.create_article, name='create_article'),
    # /board/
    path('', views.article_index, name='article_index'),
    # /board/1/
    path('<int:article_pk>/', views.article_detail, name='article_detail'),
    # /board/1/update/
    path('<int:article_pk>/update/', views.update_article, name='update_article'),
    # /board/1/delete/
    path('<int:article_pk>/delete/', views.delete_article, name='delete_article'),

    # /board/1/comments/create/
    path('<int:article_pk>/comments/create/', views.create_comment, name='create_comment'),
    # /board/1/comments/1/delete/
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
]
