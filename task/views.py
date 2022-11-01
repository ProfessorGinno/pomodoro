from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task
#from .forms import SearchTask

class TaskList(ListView):
    model = Task

class CreateTask(CreateView):
    model = Task
    template_name = 'task/create_task.html'
    success_url = '/index'
    fields = ['name', 'description', 'advance_percentage']


class EditTask(UpdateView):
    model = Task
    template_name = 'task/edit_task.html'
    success_url = '/task'
    fields = ['name', 'description', 'creation_date', 'update_date', 'advance_percentage']

class DeleteTask(DeleteView):
    model = Task
    template_name = 'task/delete_task.html'
    success_url = '/list-task'

class UpdateTask(UpdateView):
    model = Task
    success_url = '/list-task/'
    template_name = 'task/update_task.html'
    fields = ['name', 'description', 'advance_percentage']

"""class MostrarMascota(DetailView):
    model = Mascota
    template_name = 'mascota/mostrar_mascota.html'

def una_vista(request):
    return render(request, 'home/index.html')"""