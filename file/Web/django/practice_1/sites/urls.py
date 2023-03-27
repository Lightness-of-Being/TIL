from django.urls import path, include
from .views import throw, catch, number, number_print


app_name = 'sites'


urlpatterns = [
    path('throw/', throw, name='throw'),
    path('catch/', catch, name='catch'),
    path('number-print/<int:num>/', number, name='number'),
    path('number-print/', number_print, name='print'),

]

