from .models import BlogPost
from django import forms
from tinymce.widgets import TinyMCE

# Create the form class.
class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField()
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 40, 'rows': 20}))

    class Meta:
        model = BlogPost
        fields = [
            'title',
            'cover_image',
            'content',
            'category',
            'tag', 
            ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError('Ohhh at least 3 characters! ')
        return title
