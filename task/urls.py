from msilib.schema import ListView
from django.urls import path, include
from .views import CreateTask, TaskList, DeleteTask, UpdateTask

urlpatterns = [
    path('list-task/', TaskList.as_view(), name='list_task'),
    path('create-task/', CreateTask.as_view(), name='create_task'),
    path('delete-task/<int:pk>/', DeleteTask.as_view(), name='delete_task'),
    path('update-task/<int:pk>/', UpdateTask.as_view(), name='update_task'),
]
