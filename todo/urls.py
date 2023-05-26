from django.urls import path

# Views locais
from todo.views import index, todo_list


urlpatterns = [
    path('hello/', index),
    path('list/', todo_list),
]