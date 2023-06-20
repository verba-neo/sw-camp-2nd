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
]
