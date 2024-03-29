# Generated by Django 5.0 on 2024-02-02 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter_app', '0005_massage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_of_attempt', models.DateTimeField(verbose_name='дата последней попытки')),
                ('status_attempt', models.CharField(choices=[('Успешна', 'Successful'), ('Не успешна', 'Not successful')], max_length=50, verbose_name='статус попытки')),
                ('mail_server_response', models.TextField(verbose_name='ответ почтового сервера')),
                ('newsletter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='newsletter_app.newsletter', verbose_name='ответ почтового сервера')),
            ],
        ),
    ]
