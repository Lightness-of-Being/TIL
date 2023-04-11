from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def init(requst):
    return redirect('todos:index')

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }
    return render(request, 'todos/index.html', context)

def new(request):
    return render(request, 'todos/new.html')

def create(request):
    pk = request.POST.get('pk')
    title = request.POST.get('title')
    content = request.POST.get('content')
    completed = request.POST.get('completed')
    priority = request.POST.get('priority')
    created_at = request.POST.get('created_at')
    updated_at = request.POST.get('updated_at')
    deadline = request.POST.get('deadline')

    todos = Todo(pk=pk, title=title, content=content, priority=priority, created_at=created_at, updated_at=updated_at, deadline=deadline)
    
    todos.save()
    return redirect('todos:index')

def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    return render(request, 'todos/detail.html')
