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
- Axios Usage

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

Random Post Adding To Db via shell_plus
titles = [
    'Django Form Usage',
    'Django Model Form',
    'Django MVT',
    'Django URL Namespace',
    'Django Template Language',
    'Django Usage',
    'IPython',
    'Crispy Forms',
    'Easy Thumbnail Usage',
    'Django Extensions Usage',
]
item=BlogPost.objects.first()

for title in titles:
    item.pk=None
    item.title=title
    item.slug=slugify(title)
    item.view_count=randrange(10,100)
    item.save()

# Top Post Check
posts=BlogPost.objects.filter(is_active=True)
top_posts=BlogPost.objects.order_by('-view_count')[:6]
top_posts.count()

p=BlogPost.objects.first()
p.is_active=not p.is_active

user=User.objects.first()
user.userpostfav_set.all()
ids=user.userpostfav_set.filter(is_deleted=False).values_list('post_id',flat=True).order_by('-updated_at')
posts=BlogPost.objects.filter(id__in=ids)
```

