from django.shortcuts import render
from blog.models import BlogPost
# Create your views here.
def home_view(request):
    posts=BlogPost.objects.filter(is_active=True).order_by('-created_at')
    context=dict(
        posts=posts
    )
    return render(request, 'page/home_page.html', context)