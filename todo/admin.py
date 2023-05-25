from django.contrib import admin

from todo.models import Todo


@admin.register(Todo)
class AdminTodo(admin.ModelAdmin):
    pass