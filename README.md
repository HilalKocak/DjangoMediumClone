## The following features of Django are used in this project
This project is clone of https://medium.com/

This project allows different users to register, the registered user to publish blog posts. The user's blog posts have categories and tags. In this way, database relations such as onetomany and manytomany are used.

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
- Add ordering to model structure
- show blog info from db
- bootstrap jumbatron
- get_absolute_url
- django template builtins: with

### Python Shell
```
from django.contrib.auth.models import User

User.objects.get_or_create(username="django@django.com")

obj, created = User.objects.get_or_create(username="django@django.com")
tag1,created=Tag.objects.get_or_create(title='django')
post=BlogPost.objects.first()
post.tag.add(tag1)

Tag.objects.all().delete()

Tag.objects.all().update(is_active=True)

user=User.objects.first()
profile, created= Profile.objects.get_or_create(user=user)

cat=Category.objects.first()
cat.blogpost_set.all() or BlogPost.objects.filter(category=cat)

```

