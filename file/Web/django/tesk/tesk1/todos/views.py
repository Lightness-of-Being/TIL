from django.shortcuts import render
from .models import Todo
# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }
    return render(request, 'todos/index.html', context)

def new(request):
    return render(request, 'todos/new.html')

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    content = {
        'todo' : todo
    }
    return render(request, 'todos/detail.html', content)

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    completed = request.GET.get('completed')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')
    

    todo = Todo(title=title, content=content, priority=priority, deadline=deadline, completed=True if completed == 'on' else False)
    
    todo.save()
    
    return render(request, 'todos/create.html')