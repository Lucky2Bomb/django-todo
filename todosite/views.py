from django.shortcuts import render
from django.views.generic import ListView, DetailView
from todosite.models import Task, Todo
from django.http import HttpResponse

class TodosView(ListView):
    model = Todo
    template_name = 'todo/todos.html'
    # context_object_name = 'todos'

    def get_object(self):
        return Todo.objects.all()

# class Tas(DetailView):
#     model = Task
#     template_name = 'todo/todos_detail'
#     # context_object_name = 'todo_item'
    

class TasksView(ListView):
    model = Task
    template_name = 'todo/todos_detail.html'
    # context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(todo_id=self.kwargs['todo_id']).select_related('todo')

def add_task(request):
    if request.method == 'POST':
        return 'POST ADD TASK'
    elif request.method == 'DELETE' :
        return 'DELETE TASK'
    elif request.method == 'UPDATE' :
        return 'UPDATE TASK'
    else:
        return 'GET ADD TASK'