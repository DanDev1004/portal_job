from django import forms
from .models import Alerta

class AddFormAlerta(forms.ModelForm):
    class Meta:
        model = Alerta
        exclude = ('user','empresa')


class UpdateFormAlerta(forms.ModelForm):
    class Meta:
        model = Alerta
        exclude = ('user','empresa')