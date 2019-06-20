from django.shortcuts import render,redirect,get_object_or_404
from django.urls import path
from . import views
from .models import Task,subTask
from .forms import TaskForm,subTaskForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
# Create your views here.
@login_required(login_url='/login/')
def member(request):
    tasks = Task.objects.order_by('created_date')
    subTasks = subTask.objects.order_by('subtask_created_date')

    return render(request, 'views/member/member_home.html', {'tasks': tasks,'subTasks': subTasks})
@login_required(login_url='/login/')
def leader(request):
    tasks = Task.objects.order_by('created_date').filter(task_creator=request.user.id)
    subTasks = subTask.objects.order_by('subtask_created_date')
    return render(request, 'views/leader/leader_home.html', {'tasks': tasks,'subTasks': subTasks})

def home(request):
    return render(request, 'views/main/home.html', {})

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
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
        members = User.objects.all()
        print(members)
        return render(request, 'views/leader/add_subTask.html', {'form': form,'members': members})

@login_required(login_url='/login/')
def task_info(request, pk):
    tasks = get_object_or_404(Task, pk=pk)
    subTasks = subTask.objects.order_by('subtask_created_date').filter(subtask_creator=tasks.pk)
    return render(request, 'views/leader/task_detail.html', {'tasks': tasks,'subTasks': subTasks})

@login_required(login_url='/login/')
def subtask_edit(request, pk):
    task = get_object_or_404(subTask, pk=pk)
    if request.method == "POST":
        form = subTaskForm(request.POST,instance=task)
        if form.is_valid():
            task = form.save(commit=False)
        #     subTask.subtask_creator = request.user
            task.save()
            return redirect('/leader/home')
    else:
        form = subTaskForm(instance=task)
    return render(request, 'views/leader/edit_subtask.html', {'form': form})

@login_required(login_url='/login/')
def subtask_remove(request, pk):
    subtask = get_object_or_404(subTask, pk=pk)
    subtask.delete()
    return redirect('/leader/home/')
        
