from datetime import timedelta
from smtplib import SMTPException
from dateutil.relativedelta import relativedelta

from django.conf import settings
from django.core.mail import send_mail
from newsletter_app.models import Newsletter, Logs
from django.utils import timezone


def newsletter():
    today = timezone.now()
    start = today.replace(second=0, microsecond=0)
    end = start + timedelta(minutes=100_000)

    mails = Newsletter.objects.select_related('massage').filter(
        time__gte=start, time__lt=end
    ).exclude(status='Запущена')

    for mail in mails:

        mail.status = 'Запущена'
        mail.save(update_fields=['status'])

        try:
            send_mail(
                subject=mail.massage.title,
                message=mail.massage.content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=list(mail.clients.values_list(
                    'email',
                    flat=True)),
            )
        except SMTPException as e:
            Logs.log_error(mail, error_msg=str(e))
        else:
            Logs.log_success(mail)
        finally:
            mail.status = 'Завершена'

        if mail.periodicity == 'Раз в день':
            mail.time = today + relativedelta(days=1)
            mail.save()
        elif mail.periodicity == 'Раз в неделю':
            mail.time = today + relativedelta(weeks=1)
            mail.save()
        else:
            mail.time = today + relativedelta(months=1)

        mail.save()
