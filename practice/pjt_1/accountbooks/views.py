from django.shortcuts import render, redirect
from .models import Accountbook
from django.db.models import Sum

# Create your views here.
def init(request):
    return redirect('accountbooks:index')


def index(request):
    accountbooks = Accountbook.objects.all()
    sum_amount = Accountbook.objects.aggregate(Sum('amount'))
    print(sum_amount)
    
    context = {
        'accountbooks': accountbooks,
        'sum_amount' : sum_amount['amount__sum'],
    }

    return render(request, 'accountbooks/index.html', context)


def detail(request, account_book_pk):
    accountbook = Accountbook.objects.get(pk=account_book_pk)
    context = {
        'accountbook':accountbook,
    }

    return render(request, 'accountbooks/detail.html', context)


def new(request):
    return render(request, 'accountbooks/new.html')


def create(request):
    note = request.POST.get('note')
    description = request.POST.get('description')
    print(request.POST.get('category'))
    category = request.POST.get('category')
    amount = request.POST.get('amount')
    date = request.POST.get('date')

    accountbook = Accountbook(note=note, description=description, category=category, amount=amount, date=date)
    accountbook.save()
    return redirect('accountbooks:index')


def edit(request, account_book_pk):
    accountbook = Accountbook.objects.get(pk=account_book_pk)
    context = {
        'accountbook': accountbook
    }
    return render(request, 'accountbooks/edit.html', context)


def update(request, account_book_pk):
    accountbook = Accountbook.objects.get(pk=account_book_pk)
    accountbook.note = request.POST.get('note')
    accountbook.description = request.POST.get('description')
    accountbook.category = request.POST.get('category')
    accountbook.amount = request.POST.get('amount')
    accountbook.date = request.POST.get('date')

    accountbook.save()
    return redirect('accountbooks:detail', account_book_pk)


def delete(request, account_book_pk):
    accountbook = Accountbook.objects.get(pk=account_book_pk)
    accountbook.delete()
    return redirect('accountbooks:index')

def copy(request, account_book_pk):
    accountbook = Accountbook.objects.get(pk=account_book_pk)
    note = accountbook.note
    description = accountbook.description
    category = accountbook.category
    amount = accountbook.amount
    date = accountbook.date

    accountbook_new = Accountbook(note=note, description=description, category=category, amount=amount, date=date)
    accountbook_new.save()

    return redirect('accountbooks:index')




    

    