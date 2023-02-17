from .models import Post
from django import forms

# Create the form class.
class PostModelForm(forms.ModelForm):
    tag = forms.CharField()
    class Meta:
        model = Post
        fields = [
            'title',
            'cover_image',
            'content',
            'category',
            'tag', 
            ]

