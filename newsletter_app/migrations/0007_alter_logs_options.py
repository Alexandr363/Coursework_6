# Generated by Django 5.0 on 2024-02-02 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter_app', '0006_logs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logs',
            options={'verbose_name': 'логи', 'verbose_name_plural': 'логи'},
        ),
    ]