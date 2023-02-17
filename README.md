## The following features of Django are used in this project
- Abstract Model
- Model Forms
- Static Files, Media Files
- Templates and Templates Language
- Views & Urls
- Admin Panel

### Python Shell
from django.contrib.auth.models import User
User.objects.get_or_create(username="django@django.com")

obj, created = User.objects.get_or_create(username="django@django.com")

