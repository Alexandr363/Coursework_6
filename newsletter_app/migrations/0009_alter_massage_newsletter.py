# Generated by Django 5.0 on 2024-02-20 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter_app', '0008_client_user_newsletter_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='massage',
            name='newsletter',
            field=models.ManyToManyField(related_name='massages', to='newsletter_app.newsletter'),
        ),
    ]