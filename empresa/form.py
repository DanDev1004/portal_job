from django import forms
from .models import Empresa

class UpdateFormEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        exclude = ('user',)