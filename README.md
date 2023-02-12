### Python Shell
from django.contrib.auth.models import User
User.objects.get_or_create(username="django@django.com")

obj, created = User.objects.get_or_create(username="django@django.com")