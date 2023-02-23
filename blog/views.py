from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogPostModelForm
# Create your views here.
from .models import Category, Tag, BlogPost
from django.contrib.auth.decorators import login_required
import json
from django.contrib import messages


@login_required(login_url='user:login_view')
def create_blog_post_view(request):
    form= BlogPostModelForm()
    if request.method== 'POST':
        form = BlogPostModelForm(request.POST or None, request.FILES or None)
        print(form)
        print(form.errors)
        if form.is_valid():
            f = form.save(commit=False)
            f.user= request.user
            f.save()
            tags=json.loads(form.cleaned_data.get('tag'))

            print(tags)
            for item in tags:
                tag_item, created= Tag.objects.get_or_create(title=item.get('value').lower())
                tag_item.is_active=True
                tag_item.save()
                f.tag.add(tag_item)
            messages.success(request, "Yor post saved succesfully..")
            return redirect('home_view')
        
    context = dict(
    form = form
    )   
    return render(request, 'blog/create_blog_post.html', context)  

def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = BlogPost.objects.filter(category=category)
    context=dict(
        category=category,
        posts=posts,
    )
    return render(request, 'blog/post_list.html', context)

def tag_view(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = BlogPost.objects.filter(tag=tag)
    context=dict(
        tag=tag,
        posts=tag.blogpost_set.all,
    )
    return render(request, 'blog/post_list.html', context)
