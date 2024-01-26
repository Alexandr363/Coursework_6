from django.urls import path

from newsletter_app.apps import NewsletterAppConfig
from newsletter_app.views import ClientListView, ClientCreateView, \
    ClientUpdateView, IndexTemplateView, ClientDetailView, ClientDeleteView, \
    NewsletterCreateView, NewsletterListView, NewsletterDetailView, \
    NewsletterUpdateView, NewsletterDeleteView

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

]
