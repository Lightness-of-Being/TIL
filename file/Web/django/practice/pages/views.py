from django.shortcuts import render

# Create your views here.

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    return render(request, 'pages/catch.html')