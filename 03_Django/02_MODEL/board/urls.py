from django.urls import path
from . import views

urlpatterns = [
    # Create
    # board/new/ => 게시글 생성용 HTML
    path('new/', views.new),
    # board/create/ => 게시글 저장
    path('create/', views.create),

    # Read
    # board/ => 전체 게시글 목록
    path('', views.index),
    # board/1/ => 단일 게시글 상세
    path('<int:pk>/', views.detail),

    # Update
    # board/1/edit/ => 게시글 수정용 HTML
    path('<int:pk>/edit/', views.edit),
    # board/1/update/ => 게시글 수정 후 저장
    path('<int:pk>/update/', views.update),

    # Delete
    # board/1/delete/
    path('<int:pk>/delete/', views.delete)
]
