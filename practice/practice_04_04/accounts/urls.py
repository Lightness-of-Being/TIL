from django.urls import path
from . import views 

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('signup/', views.signup, name='signup')
]
