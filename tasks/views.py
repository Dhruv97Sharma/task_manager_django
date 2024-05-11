from django.shortcuts import render
from .models import Task
# Create your views here.

def index(request):
    tasks = Task.objects.all().order_by('-id')
    done_tasks_cnt = Task.objects.filter(status='done').count()
    todo_tasks_cnt = Task.objects.filter(status='todo').count()
    return render(request, 'index.html', {'tasks': tasks, 'done_tasks_cnt': done_tasks_cnt, 'todo_tasks_cnt': tasks.count()})

# Creating a new Task
def create_task(request):
    name = request.POST.get('name')
    task = Task.objects.create(name=name)
    task.save()
    tasks = Task.objects.all().order_by('-id')
    todo_tasks_cnt = Task.objects.filter(status='todo').count()
    done_tasks_cnt = Task.objects.filter(status='done').count()
    return render(request, 'task-list.html', {'tasks': tasks, 'done_tasks_cnt': done_tasks_cnt, 'todo_tasks_cnt': todo_tasks_cnt})

# Toggling task as todo or done
def mark_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.status = 'done' if task.status == 'todo' else 'todo'
    task.save()
    tasks = Task.objects.all().order_by('-id')
    todo_tasks_cnt = Task.objects.filter(status='todo').count()
    done_tasks_cnt = Task.objects.filter(status='done').count()
    return render(request, 'task-list.html', {'tasks': tasks, 'done_tasks_cnt': done_tasks_cnt, 'todo_tasks_cnt': todo_tasks_cnt})

# Deleting a Task
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    tasks = Task.objects.all().order_by('-id')
    todo_tasks_cnt = Task.objects.filter(status='todo').count()
    done_tasks_cnt = Task.objects.filter(status='done').count()
    return render(request, 'task-list.html', {'tasks': tasks, 'done_tasks_cnt': done_tasks_cnt, 'todo_tasks_cnt': todo_tasks_cnt})

# Clearing all completed tasks
def clear_completed_tasks(request):
    tasks = Task.objects.filter(status='done')
    for task in tasks:
        task.delete()
    tasks = Task.objects.all().order_by('-id')
    todo_tasks_cnt = Task.objects.filter(status='todo').count()
    done_tasks_cnt = Task.objects.filter(status='done').count()
    return render(request, 'task-list.html', {'tasks': tasks, 'done_tasks_cnt': done_tasks_cnt, 'todo_tasks_cnt': todo_tasks_cnt})