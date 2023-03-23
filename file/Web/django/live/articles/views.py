from django.shortcuts import render

# Create your views here.
# 필수로 request 라고 인자를 쓴다
def index(request):
    context = {
        'name' : 'aefs'
    }
    return render(request, 'index.html', context)
def dinner(request):
    foods = ['볶음밥', '보쌈', '서브웨이', '햄버거',]
    context = {
        'foods' : foods,
    }
    return render(request, 'dinner.html', context)
def search(request):
    return render(request, 'search.html')
def throw(request):
    return render(request, 'throw.html')
def catch(request):
    data = request.GET.get('message')
    context = {
        'data': data,
    }
    return render(request, 'catch.html', context)
