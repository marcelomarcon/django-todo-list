from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h3>Hello Word</h3>')


def todo_list(request):
    return render(request, 'todo/index.html')