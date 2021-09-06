from django.forms import ModelForm, TextInput, Textarea
from .models import *


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter title'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter description'
            })
        }
