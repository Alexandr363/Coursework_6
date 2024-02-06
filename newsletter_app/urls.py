from django.urls import path

from newsletter_app.apps import NewsletterAppConfig
from newsletter_app.views import ClientListView, ClientCreateView, \
    ClientUpdateView, IndexTemplateView, ClientDetailView, ClientDeleteView, \
    NewsletterCreateView, NewsletterListView, NewsletterDetailView, \
    NewsletterUpdateView, NewsletterDeleteView, MassageCreateView, \
    MassageListView, MassageDetailView, MassageUpdateView, MassageDeleteView, \
    LogsCreateView, LogsListView, LogsDetailView, LogsUpdateView, LogsDeleteView

app_name = NewsletterAppConfig.name

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),

    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('detail_client/<int:pk>/', ClientDetailView.as_view(), name='detail_client'),
    path('update_client/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),

    path('client_list/', ClientListView.as_view(), name='client_list'),


    path('create_newsletter/', NewsletterCreateView.as_view(), name='create_newsletter'),
    path('detail_newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='detail_newsletter'),
    path('update_newsletter/<int:pk>/', NewsletterUpdateView.as_view(), name='update_newsletter'),
    path('delete_newsletter/<int:pk>/', NewsletterDeleteView.as_view(), name='delete_newsletter'),

    path('newsletter_list/', NewsletterListView.as_view(), name='newsletter_list'),


    path('create_massage/', MassageCreateView.as_view(), name='create_massage'),
    path('detail_massage/<int:pk>/', MassageDetailView.as_view(), name='detail_massage'),
    path('update_massage/<int:pk>/', MassageUpdateView.as_view(), name='update_massage'),
    path('delete_massage/<int:pk>/', MassageDeleteView.as_view(), name='delete_massage'),

    path('massage_list/', MassageListView.as_view(), name='massage_list'),


    path('create_logs/', LogsCreateView.as_view(), name='create_logs'),
    path('detail_logs/<int:pk>/', LogsDetailView.as_view(), name='detail_logs'),
    path('update_logs/<int:pk>/', LogsUpdateView.as_view(), name='update_logs'),
    path('delete_logs/<int:pk>/', LogsDeleteView.as_view(), name='delete_logs'),

    path('logs_list/', LogsListView.as_view(), name='logs_list'),

]
