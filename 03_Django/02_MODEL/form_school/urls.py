from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    # /school/create/
    path('create/', views.create, name='create'),
    # /school/
    path('', views.index, name='index'),  # ul > li > a > 이름
    # /school/1/
    path('<int:student_pk>/', views.detail, name='detail'),  # 모든 정보 잘 표시
    # /school/1/update/
    path('<int:student_pk>/update/', views.update, name='update'),
    # /school/1/delete/
    path('<int:student_pk>/delete/', views.delete, name='delete'),

]
