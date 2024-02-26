from django.conf import settings
from django.db import models


class Client(models.Model):
    fio = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(max_length=150, verbose_name='почта')
    comment = models.TextField(verbose_name='комментарий')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             null=True, blank=True)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Newsletter(models.Model):
    objects = models.Manager

    PERIODICITY_CHOISES = [
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
    periodicity = models.CharField(max_length=50, choices=PERIODICITY_CHOISES,
                                   verbose_name='периодичность рассылки')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,
                              verbose_name='статус рассылки')

    # client = models.ManyToManyField(Client)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True,
                               blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             null=True, blank=True)

    def __str__(self):
        return f'{self.time} - {self.status}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Massage(models.Model):
    objects = models.Manager

    title = models.CharField(max_length=40, verbose_name='тема письма')
    content = models.TextField(verbose_name='содержание')

    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE,
                                   null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Logs(models.Model):

    ATTEMPT_CHOICES = [
        ('Успешна', 'Successful'),
        ('Не успешна', 'Not successful'),
    ]

    data_of_attempt = models.DateTimeField(verbose_name='дата последней '
                                                        'попытки')
    status_attempt = models.CharField(max_length=50, choices=ATTEMPT_CHOICES,
                                      verbose_name='статус попытки')
    mail_server_response = models.TextField(verbose_name='ответ почтового '
                                                         'сервера')
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE,
                                   null=True, blank=True,
                                   verbose_name='ответ почтового сервера')

    def __str__(self):
        return self.status_attempt

    class Meta:
        verbose_name = 'логи'
        verbose_name_plural = 'логи'
