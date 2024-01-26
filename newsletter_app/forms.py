from django import forms
from newsletter_app.models import Client, Newsletter


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'