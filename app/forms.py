from django import forms

from app.models import Paper


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Paper
        exclude = ["author"]   
