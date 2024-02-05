from django.contrib import admin

from newsletter_app.models import Client, Newsletter, Massage


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'id', 'email', 'fio', 'comment')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('time', 'periodicity', 'status')


@admin.register(Massage)
class MassageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
