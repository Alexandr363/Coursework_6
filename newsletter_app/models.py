from django.conf import settings
from django.db import models


class Client(models.Model):
    fio = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(max_length=150, verbose_name='почта')
    comment = models.TextField(verbose_name='комментарий')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Massage(models.Model):
    objects = models.Manager

    title = models.CharField(max_length=40, verbose_name='тема письма')
    content = models.TextField(verbose_name='содержание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Newsletter(models.Model):
    objects = models.Manager

    PERIODICITY_CHOICES = [
        ('Раз в день', 'Daily'),
        ('Раз в неделю', 'Weekly'),
        ('Раз в меcяц', 'Monthly'),
    ]

    STATUS_CHOICES = [
        ('Завершена', 'Completed'),
        ('Создана', 'Created'),
        ('Запущена', 'Started'),
    ]

    time = models.DateTimeField(verbose_name='время рассылки')
    periodicity = models.CharField(
        max_length=50,
        choices=PERIODICITY_CHOICES,
        verbose_name='периодичность рассылки',
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        verbose_name='статус рассылки',
    )

    clients = models.ManyToManyField(Client)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    massage = models.ForeignKey(
        Massage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.time} - {self.status}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Logs(models.Model):
    objects = models.Manager

    ATTEMPT_CHOICES = [
        ('Успешна', 'Successful'),
        ('Не успешна', 'Not successful'),
    ]

    data_of_attempt = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата последней попытки',
    )
    status_attempt = models.CharField(
        max_length=50,
        choices=ATTEMPT_CHOICES,
        verbose_name='статус попытки',
    )
    mail_server_response = models.TextField(
        verbose_name='ответ почтового сервера',
        blank=True,
    )
    newsletter = models.ForeignKey(
        Newsletter,
        on_delete=models.CASCADE,
        verbose_name='рассылка',
    )

    def __str__(self):
        return self.status_attempt

    class Meta:
        verbose_name = 'логи'
        verbose_name_plural = 'логи'

    @classmethod
    def log_success(cls, newsletter: Newsletter):
        cls.objects.create(newsletter=newsletter, status_attempt='Успешна')

    @classmethod
    def log_error(cls, newsletter: Newsletter, error_msg: str):
        cls.objects.create(
            newsletter=newsletter,
            status_attempt='Не успешна',
            mail_server_response=error_msg
        )
