from .models import FeedBack
from django.forms import ModelForm, TextInput, Textarea


class FeedBackForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = ["name", "email", "message"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your comment'
            }),
        }