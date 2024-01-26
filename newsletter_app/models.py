from django.db import models


class Client(models.Model):
    fio = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(max_length=150, verbose_name='почта')
    comment = models.TextField(verbose_name='комментарий')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Newsletter(models.Model):

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

    time = models.DateTimeField(auto_now=True, verbose_name='время рассылки')
    periodicity = models.CharField(max_length=50, choices=PERIODICITY_CHOISES,
                                   verbose_name='периодичность рассылки')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,
                              verbose_name='статус рассылки')

    def __str__(self):
        return f'{self.time} - {self.status}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
