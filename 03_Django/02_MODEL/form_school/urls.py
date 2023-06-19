from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # path('edit/', views.edit, name='edit'),
    # path('update/', views.update, name='update'),
]
