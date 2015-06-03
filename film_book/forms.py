from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['movie', 'review']
        labels = {
            'movie': 'Select a Movie',
            'review': 'Write a Review on This Movie',
        }
        widgets = {
            'movie': forms.Select,
            'review': forms.Textarea,
        }
