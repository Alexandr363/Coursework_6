from django.urls import reverse_lazy
from django.views.generic import (CreateView, UpdateView, ListView,
                                  TemplateView, DetailView, DeleteView)

from newsletter_app.forms import ClientForm, NewsletterForm, MassageForm, \
    LogsForm
from newsletter_app.models import Client, Newsletter, Massage, Logs


class IndexTemplateView(TemplateView):
    template_name = 'newsletter_app/index.html'


"""__________Client Views_____________"""


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('newsletter:client_list')


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('newsletter:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('newsletter:client_list')


class ClientListView(ListView):
    model = Client


"""__________Newsletter Views_____________"""


class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:newsletter_list')


class NewsletterDetailView(DetailView):
    model = Newsletter


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:newsletter_list')


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('newsletter:newsletter_list')


class NewsletterListView(ListView):
    model = Newsletter


"""__________Massage Views_____________"""


class MassageCreateView(CreateView):
    model = Massage
    form_class = MassageForm
    success_url = reverse_lazy('newsletter:massage_list')


class MassageDetailView(DetailView):
    model = Massage


class MassageUpdateView(UpdateView):
    model = Massage
    form_class = MassageForm
    success_url = reverse_lazy('newsletter:massage_list')


class MassageDeleteView(DeleteView):
    model = Massage
    success_url = reverse_lazy('newsletter:massage_list')


class MassageListView(ListView):
    model = Massage


"""__________Logs Views_____________"""


class LogsCreateView(CreateView):
    model = Logs
    form_class = LogsForm
    success_url = reverse_lazy('newsletter:logs_list')


class LogsDetailView(DetailView):
    model = Logs


class LogsUpdateView(UpdateView):
    model = Logs
    form_class = LogsForm
    success_url = reverse_lazy('newsletter:logs_list')


class LogsDeleteView(DeleteView):
    model = Logs
    success_url = reverse_lazy('newsletter:logs_list')


class LogsListView(ListView):
    model = Logs
