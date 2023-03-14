from django import forms
from .models import Notes
from django.core.exceptions import ValidationError


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Title',
            'text': 'Write your notes here',
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3 or len(title) > 100:
            raise ValidationError("Title must be between 3 and 100 characters")
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 3:
            raise ValidationError("Text must be at least 3 characters")
        return text
