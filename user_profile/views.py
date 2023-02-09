from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
        print(request.POST)
    
    return render(request, 'user_profile/register.html', context)

