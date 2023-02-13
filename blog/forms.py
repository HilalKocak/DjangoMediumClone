from django.forms import ModelForm
from .models import Post

# Create the form class.
class PostModelForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'cover_image',
            'content',
            'category',
            'tag', 
            ]

