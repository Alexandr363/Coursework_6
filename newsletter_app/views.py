from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, UpdateView, ListView,
                                  TemplateView, DetailView, DeleteView)

from newsletter_app.forms import ClientForm, NewsletterForm, MassageForm, \
    LogsForm
from newsletter_app.models import Client, Newsletter, Massage, Logs


class IndexTemplateView(TemplateView):
    template_name = 'newsletter_app/index.html'


"""__________Client Views_____________"""


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('newsletter:client_list')


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientUpdateView(LoginRequiredMixin,UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('newsletter:client_list')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('newsletter:client_list')


class ClientListView(ListView):
    model = Client


"""__________Newsletter Views_____________"""


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:newsletter_list')


class NewsletterDetailView(LoginRequiredMixin, DetailView):
    model = Newsletter


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:newsletter_list')


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy('newsletter:newsletter_list')


class NewsletterListView(ListView):
    model = Newsletter


"""__________Massage Views_____________"""


class MassageCreateView(LoginRequiredMixin, CreateView):
    model = Massage
    form_class = MassageForm
    success_url = reverse_lazy('newsletter:massage_list')


class MassageDetailView(LoginRequiredMixin, DetailView):
    model = Massage


class MassageUpdateView(LoginRequiredMixin, UpdateView):
    model = Massage
    form_class = MassageForm
    success_url = reverse_lazy('newsletter:massage_list')


class MassageDeleteView(LoginRequiredMixin, DeleteView):
    model = Massage
    success_url = reverse_lazy('newsletter:massage_list')


class MassageListView(ListView):
    model = Massage


"""__________Logs Views_____________"""


class LogsCreateView(LoginRequiredMixin, CreateView):
    model = Logs
    form_class = LogsForm
    success_url = reverse_lazy('newsletter:logs_list')


class LogsDetailView(LoginRequiredMixin, DetailView):
    model = Logs


class LogsUpdateView(LoginRequiredMixin, UpdateView):
    model = Logs
    form_class = LogsForm
    success_url = reverse_lazy('newsletter:logs_list')


class LogsDeleteView(LoginRequiredMixin, DeleteView):
    model = Logs
    success_url = reverse_lazy('newsletter:logs_list')


class LogsListView(ListView):
    model = Logs
