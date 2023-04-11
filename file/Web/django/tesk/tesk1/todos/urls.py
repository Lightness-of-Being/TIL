from django.urls import path, include
from . import views

app_name = 'todos'
urlpatterns = [
    path('new/', views.new, name='new'),
    path('detail/<int:todo_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
]
