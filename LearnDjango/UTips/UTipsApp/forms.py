from django import forms
from .models import Subjects, Info


class AddSubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ["name", "professor", "image"]
        label = {"subject": "", "professor": "", "image":""}


class AddTopicsForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ["subject", "topic", "text", "date_shared"]
        label = {
            "subject": "",
            "topic": "",
            "text": "",
            "date_shared": "",
        }