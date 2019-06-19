from django.shortcuts import render,redirect,get_object_or_404
from django.urls import path
from . import views
from .models import Task,subTask
from .forms import TaskForm,subTaskForm
from django.utils import timezone
# Create your views here.
def member(request):
    tasks = Task.objects.order_by('created_date')
    subTasks = subTask.objects.order_by('subtask_created_date')

    return render(request, 'views/member/member_home.html', {'tasks': tasks,'subTasks': subTasks})

def leader(request):
    tasks = Task.objects.order_by('created_date').filter(task_creator=request.user.id)
    subTasks = subTask.objects.order_by('subtask_created_date')
    return render(request, 'views/leader/leader_home.html', {'tasks': tasks,'subTasks': subTasks})

def home(request):
    return render(request, 'views/main/home.html', {})

def newTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_creator = request.user
            task.published_date = timezone.now()
            task.save()
            return render(request, 'views/leader/leader_home.html', {})
    else:
        form = TaskForm()
        return render(request, 'views/leader/add_task.html', {'form': form})

def newSubTask(request, pk):
    if request.method == "POST":
        form = subTaskForm(request.POST)
        if form.is_valid():
            tasks = get_object_or_404(Task, task_id=pk)
            subTask = form.save(commit=False)
            subTask.subtask_creator = tasks
            subTask.save()
            url = '/leader/task/'+ str(pk)
            return redirect(url)
    else:
        form = subTaskForm()
        return render(request, 'views/leader/add_subTask.html', {'form': form})

def task_info(request, pk):
    tasks = get_object_or_404(Task, pk=pk)
    subTasks = subTask.objects.order_by('subtask_created_date').filter(subtask_creator=tasks.pk)
    return render(request, 'views/leader/task_detail.html', {'tasks': tasks,'subTasks': subTasks})