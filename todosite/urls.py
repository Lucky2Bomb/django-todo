from django.http import HttpResponse
from django.urls import path

from .views import *
urlpatterns = [
    path('', TodosView.as_view(), name='index'),
    # path('todo/<int:pk>', TodoDetailView.as_view(), name='index_details'),
    path('todo/<int:todo_id>', TasksView.as_view(), name='index_details'),
    path('todo/<int:todo_id>/add-task', add_task, name='add_task'),
    # path('todo/')
]