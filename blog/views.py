from django.shortcuts import render, redirect
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
                tag_item, created= Tag.objects.get_or_create(title=item.get('value'))
                f.tag.add(tag_item)
            messages.success(request, "Yor post saved succesfully..")
            return redirect('home_view')
        
    context = dict(
    form = form
    )   
    return render(request, 'blog/create_blog_post.html', context)  