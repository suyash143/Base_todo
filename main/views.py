from django.shortcuts import render, redirect
from .forms import TaskForm
from . import models
import datetime
from django.conf import settings
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


def index(request):
    return render(request, 'index.html')

@login_required
def add_tasks(request):
    form = TaskForm()
    users = get_user_model()

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('title')
        pk = request.POST.get('assigned')
        task, created = models.Task.objects.get_or_create(title=title, description=description,
                                                          created=datetime.datetime.now(), status='Fresh',
                                                          assigned=users.objects.get(pk=pk))

        task.save()
        print(request.POST)

    return render(request, 'add_tasks.html', {'form': form, 'users': users.objects.all()})

@login_required
def task_list(request):
    if request.method=="POST":
        id = request.POST.get('id')
        print(id)
        request.session['id'] = id
        return redirect('task')
    return render(request,'Tasks_list.html',{'tasks':models.Task.objects.filter(assigned=request.user)})

@login_required
def task(request):
    id = request.session.get('id')
    task=models.Task.objects.get(pk=id)
    if task.assigned==request.user:
        if request.method=="POST":
            print(request.POST)
            task.status=request.POST.get('status')
            if request.POST.get("is_completed")=="1":
                task.is_completed=True
            else:
                task.is_completed=False
            task.save()
            return redirect('task_list')
        return render(request, 'task.html',{'task':task})
    else:
        return render(request, 'task.html', {'h1': "Not Authorized"})


