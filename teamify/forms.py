from django import forms

from .models import Task,subTask

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('task_name', 'task_description','task_assign_to')

class subTaskForm(forms.ModelForm):

    class Meta:
        model = subTask
        fields = ('subtask_name', 'subtask_description','subtask_assign_to')