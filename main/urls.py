import django
from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [

    path('index',views.index,name='index'),
    path('add_tasks',views.add_tasks,name='add_tasks'),
    path("logout/", LogoutView.as_view(),name="logout"),
    path('task_list',views.task_list,name='task_list'),
    path('task',views.task,name='task'),
]
