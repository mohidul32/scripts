from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def task_list(request):
    # TODO: check this function
    tasks = Task.objects.all()
    return render(request, 'todos/task_list.html', {'tasks': tasks})

def task_create(request):
    # TODO: check this function
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
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
