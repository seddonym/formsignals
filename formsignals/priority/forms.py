from django import forms
from .models import BlogEntryPriority


class BlogEntryPriorityForm(forms.ModelForm):
    class Meta:
        model = BlogEntryPriority
        fields = ['priority']
