from todosite.models import Task, Todo
from django.contrib import admin

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_finished', 'show_checked')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_editable = ('is_finished', 'show_checked')
    list_filter = ('is_finished', 'show_checked',)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'todo', 'is_checked')
    list_display_links = ('id', 'title')
    list_editable = ('is_checked',)
    ordering = ('todo', 'id')
    search_fields=('title', 'todo')

admin.site.register(Todo, TodoAdmin)
admin.site.register(Task, TaskAdmin)