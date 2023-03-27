from django.contrib import admin
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch')
]

