import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")
django.setup()

from todos.models import Task


Task.objects.create(title="Buy groceries")
Task.objects.create(title="Go to Gym", completed=True)

incomplete_tasks = Task.objects.filter(completed=False)
for task in incomplete_tasks:
    task.completed = True
    task.save()
    print(f"Task '{task.title}' marked as completed")

Task.objects.filter(title__icontains="Gym").update(title="Gym Workout")
print("Updated Gym related tasks")
