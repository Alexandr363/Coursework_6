from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail
from newsletter_app.models import Newsletter
from django.utils import timezone


def newsletter():
    today = timezone.now()
    start = today.replace(second=0, microsecond=0)
    end = start + timedelta(minutes=100000)

    mails = Newsletter.objects.filter(time__gte=start, time__lt=end)

    for mail in mails:

        mail.status = 'Запущена'
        mail.save()

        for massage in mail.massage_set.all():
            send_mail(
                subject=massage.title,
                message=massage.content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[mail.client.email]
            )

        mail.status = 'Завершена'
        mail.save()

        if mail.periodicity == 'Раз в день':
            mail.time = today + timedelta(days=1)
            mail.save()
        elif mail.periodicity == 'Раз в неделю':
            mail.time = today + timedelta(days=7)
            mail.save()
        else:
            mail.time = today + timedelta(days=30)
            mail.save()
