from django import forms
from hello.models import LogMessage


# Defines Django form that contains a field from data model LogMessage
class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required