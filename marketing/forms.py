from django import forms
from .models import Subscribtions


class EmailSubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribtions
        fields = ('email', )
