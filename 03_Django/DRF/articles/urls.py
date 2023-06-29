from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # articles
    # /articles/
    path('', views.article_list_or_create),
    # /articles/1/
    path('<int:article_pk>/', views.article_detail_or_update_or_delete),
    # /articles/1/like/
    path('<int:article_pk>/like/', views.like_article),
    # comments
    # /articles/1/comments/
    path('<int:article_pk>/comments/', views.create_comment),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete)
]
