from django.urls import path
from . import views

urlpatterns = [
    path('member/home/', views.member, name='member'),
    path('leader/home/', views.leader, name='leader'),
    path('', views.home, name='home'),
    path('leader/newTask/', views.newTask, name='newTask'),
    path('leader/newSubTask/<int:pk>/', views.newSubTask, name='newSubTask'),
    path('leader/subTask/<pk>/remove/', views.subtask_remove, name='subtask_remove'),
    path('leader/task/<int:pk>/', views.task_info, name='task_info'),
    path('leader/task/edit/<int:pk>/', views.subtask_edit, name='subtask_edit'),
    
]