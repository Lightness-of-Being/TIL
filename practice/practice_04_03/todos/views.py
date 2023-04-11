from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
# Create your views here.
def init(request):
    return redirect('todos:index')

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos,
    }
    return render(request, 'todos/index.html', context)

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo' : todo,
    }

    return render(request, 'todos/detail.html', context)

def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos:index')


def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm()
    context = {
        'form' : form
    }
    return render(request, 'todos/create.html', context)



