# Generated by Django 5.0 on 2024-02-01 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter_app', '0004_newsletter_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='тема письма')),
                ('content', models.TextField(verbose_name='содержание')),
                ('newsletter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='newsletter_app.newsletter', verbose_name='адресат рассылки')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
            },
        ),
    ]
