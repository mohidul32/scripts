from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.core.cache import cache
from django.contrib import messages
from django.db import DatabaseError

from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    # Try to get data from cache
    tasks = cache.get('tasks_list')

    if not tasks:
        print("⏳ Cache miss — fetching from DB...")
        tasks = list(Task.objects.all())
        cache.set('tasks_list', tasks, timeout=60)  # Cache for 60 seconds
    else:
        print("✅ Cache hit — fetched from Redis cache!")

    return render(request, 'todos/task_list.html', {'tasks': tasks})

def task_create(request):
    try:
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "✅ Task created successfully!")
                return redirect('task_list')
            else:
                messages.warning(request, "⚠️ Please correct the errors below.")
        else:
            form = TaskForm()
    except DatabaseError as e:
        messages.error(request, f"❌ Database error: {e}")
        form = TaskForm()
    except Exception as e:
        messages.error(request, f"⚠️ Unexpected error: {e}")
        form = TaskForm()

    return render(request, 'todos/task_form.html', {'form': form})


def task_update(request, pk):
    # TODO: check this function
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todos/task_form.html', {'form': form})

def task_delete(request, pk):
    # TODO: check this function
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todos/task_delete.html', {'task': task})
# Added by automation script


# views.py এ
def bulk_complete_tasks(request):
    Task.objects.filter(completed=True).update(completed=False)
    return redirect('task_list')
