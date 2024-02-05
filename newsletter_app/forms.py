from django import forms
from newsletter_app.models import Client, Newsletter, Massage, Logs


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'


class MassageForm(forms.ModelForm):

    class Meta:
        model = Massage
        fields = '__all__'


class LogsForm(forms.ModelForm):

    class Meta:
        model = Logs
        fields = '__all__'


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
