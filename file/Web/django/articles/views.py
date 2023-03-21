from django.shortcuts import render

# Create your views here.
# 필수로 request 라고 인자를 쓴다
def index(request):
    return render(request, 'index.html')
