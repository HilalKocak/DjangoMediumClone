from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from slugify import slugify
# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, f"{request.user.username} Daha once login olmussun")
        return redirect('home_view')
    context=dict()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if len(username) < 4 or len(password) < 4:
             messages.add_message(request, messages.WARNING, '4 karakterden büyük olmali')
             return redirect('user_profile:login_view')

        user = authenticate(request, username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
            messages.add_message(request, messages.SUCCESS, 'Login oldun')
            login(request, user)
            return redirect('home_view')
        else:
            print('Return invalid login error message')
    return render(request, 'user_profile/login.html', context)

def logout_view(request):
    messages.info(request, f"{request.user.username} Oturumun kapatildi")
    logout(request)
    return redirect('home_view')


def register_view(request):
    context = dict()
    if request.method == 'POST':
        post_info = request.POST
        email = post_info.get('email')
        email_confirm = post_info.get('email_confirm')
        first_name = post_info.get('first_name')
        last_name = post_info.get('last_name')
        password = post_info.get('password')
        password_confirm = post_info.get('password_confirm')
        instagram = post_info.get('instagram')
        print('*'*30)
        print(email, email_confirm, first_name, last_name, password, password_confirm, instagram,)
        
        if len(first_name)<3 or len(last_name)<3 or len(password)<3 or len(email)<3:
            messages.warning(request, "Bilgiler en az üç karakterden oluşmalı")
            return redirect('user_profile:register_view')
        
        if email != email_confirm:
            messages.warning(request, "Emailler eslesmiyor")
            return redirect('user_profile:register_view')
            
        if password != password_confirm:
            messages.warning(request, "Sifreler eslesmiyor")
            return redirect('user_profile:register_view')
        
        user, created = User.objects.get_or_create(username=email)
        print("This is user : ",user) # sadece mail adresini adık user ile
        print("created: ", created)
        # Eger Kullanici Created Degilse Kullanici Daha Once Sisteme Kayitlidir..
        if not created:
            user_login = authenticate(request, username=email, password=password)
            if user is not None:
                messages.success(request, "Daha Once Kayit Olmussunuz.. Ana Sayfaya Yonlendirildiniz..")
                # Kullanici Login oldu ;)
                login(request, user_login)
                return redirect('home_view')
            messages.warning(request, f'{email} adresi sistemde kayitli ama Login olamadiniz.. Login Sayfasina Yonlendiriliyorsunuz')
            return redirect('user_profile:login_view')
        
        user.email=email
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)

        profile, profile_created = Profile.objects.get_or_create(user=user)
        profile.instagram = instagram
        profile.slug = slugify(f"{first_name}-{last_name}")
        user.save()
        profile.save()

        messages.success(request, f"{user.first_name} Sisteme kaydedildiniz..")
        user_login = authenticate(request, username=email, password=password)
        login(request, user_login)
        return redirect('home_view')

    return render(request, 'user_profile/register.html', context)

