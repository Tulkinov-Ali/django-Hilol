from django import forms
from .models import Foods


class ImageForm(forms.ModelForm):
    class Meta:
        model = Foods
        fields = ("name", 'category', 'price', 'type', "img")
