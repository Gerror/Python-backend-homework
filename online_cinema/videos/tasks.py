from django.core.mail import send_mail
from application.settings import ADMINS, EMAIL_HOST_USER
from application import celery_app


@celery_app.task()
def create_video(title):
    send_mail(
        subject='Create video',
        message=f'A new video has been created: {title}',
        from_email=EMAIL_HOST_USER,
        recipient_list=ADMINS,
        fail_silently=False,
    )