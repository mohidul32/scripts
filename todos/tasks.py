from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_test_email_task():
    send_mail(
        subject="Todo Project Test Email",
        message="Hello! This is a test email from Celery + Django.",
        from_email="from@example.com",
        recipient_list=["exit.mohidulislam@gmail.com"],
        fail_silently=False,
    )
    return "Email sent to the user"
