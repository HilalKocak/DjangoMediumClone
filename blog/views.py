from django.shortcuts import render
from .forms import BlogPostModelForm
# Create your views here.
from .models import Category, Tag, BlogPost
from django.contrib.auth.decorators import login_required

@login_required(login_url='user:login_view')
def create_blog_post_view(request):
    form= BlogPostModelForm()
    context = dict(
        form = form
    )
    if request.method== 'POST':
        form = BlogPostModelForm(request.POST or None, request.FILES or None)
        print(form)
        print(form.errors)
        if form.is_valid():
            f = form.save(commit=False)
            f.user= request.user
            f.save()
            print(form.cleaned_data)
            
    return render(request, 'blog/create_blog_post.html', context)  