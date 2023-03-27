from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def throw(request):
    return render(request, 'sites/throw.html')


def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message
    }
    return render(request, 'sites/catch.html', context)
    

def number(request, num):
    number = request.GET.get('number')
    context = {
        'number': number,
        'num' : num,
    }
    print(num,number)
    return render(request, 'sites/number.html', context)


def number_print(request):
    return render(request, 'sites/number_print.html')
