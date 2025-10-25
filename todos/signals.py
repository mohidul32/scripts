# todos/signals.py
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Task

@receiver([post_save, post_delete], sender=Task)
def clear_task_cache(sender, **kwargs):
    cache.delete('tasks_list')
    print("🧹 Cache cleared after Task create/update/delete.")
