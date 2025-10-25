import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import django
from todos.tasks import send_test_email_task
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")
django.setup()

# Trigger the task
result = send_test_email_task.delay()

print("Task sent to Celery, check worker log!")
print("Task ID:", result.id)
