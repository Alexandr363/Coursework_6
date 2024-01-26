from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, TemplateView, \
    DetailView, DeleteView

from newsletter_app.forms import ClientForm, NewsletterForm
from newsletter_app.models import Client, Newsletter


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
