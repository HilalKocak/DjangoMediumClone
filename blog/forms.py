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
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class':'form-control'})
