from django.shortcuts import render
import random

# Create your views here.
def today_dinner(request):
    foods = ['김치찌개', '삼계탕', '떡볶이', '돈까스', '국밥', '초밥', '우동', '라면']
    food = random.choice(foods)
    context = {
        'food':food,
    }
    return render(request, 'today_dinner.html', context)
def throw(request):
    return render(request, 'throw.html')
def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'catch.html', context)