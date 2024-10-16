from django import forms
from .models import Curriculum

class UpdateFormCurriculum(forms.ModelForm):
    class Meta:
        model = Curriculum
        exclude = ('user',)