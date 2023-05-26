from django.shortcuts import render, HttpResponse

from todo.models import Todo

# Create your views here.

def index(request):
    return HttpResponse('<h3>Hello Word</h3>')


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def add_task(request):
    ...