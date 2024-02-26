from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail
from newsletter_app.models import Newsletter
from django.utils import timezone


def newsletter():
    today = timezone.now()
    start = today.replace(second=0, microsecond=0)
    end = start + timedelta(minutes=10000)

    mail = Newsletter.objects.filter(time__gte=start, time__lt=end)

    for i in mail:
        for j in i.massage_set.all():
            send_mail(
                subject=j.title,
                message=j.content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[]
            )
