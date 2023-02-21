## The following features of Django are used in this project
- Abstract Model
- Model Forms
- Static Files, Media Files
- Templates and Templates Language
- Views & Urls
- Admin Panel
- Add class to form field Django ModelForm
- Django Cripspy Forms
- TinyMCE with Forms
- enctype='multipart/form-data'
- Form Validators(forms def cleaned_data)
- Creating out own form validators with function
- Tagify
- Django Extensions Plugin
- shell_plus
- Many to Many structure
- Easy Thumbnail
- truncatewords_html

### Python Shell
```
from django.contrib.auth.models import User

User.objects.get_or_create(username="django@django.com")

obj, created = User.objects.get_or_create(username="django@django.com")
tag1,created=Tag.objects.get_or_create(title='django')
post=BlogPost.objects.first()
post.tag.add(tag1)

Tag.objects.all().delete()
```

