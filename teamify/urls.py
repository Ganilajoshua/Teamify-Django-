from django.urls import path
from . import views

urlpatterns = [
    path('member/home/', views.member, name='member'),
    path('leader/home/', views.leader, name='leader'),
    path('', views.home, name='home'),
    path('leader/newTask/', views.newTask, name='newTask'),
    path('leader/newSubTask/<int:pk>/', views.newSubTask, name='newSubTask'),
    path('leader/task/<int:pk>/', views.task_info, name='task_info'),
]