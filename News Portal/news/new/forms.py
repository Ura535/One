from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'Category_post',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title is not None and len(title) < 10:
            raise ValidationError({
                "title": "Couldn't be less then 10 symbols."
            })
        return cleaned_data

