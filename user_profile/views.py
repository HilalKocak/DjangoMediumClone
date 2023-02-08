from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_view(request):
    # Login olan kullanici direk ana sayfaya yonlendirilsin
    if request.user.is_authenticated:
        messages.info(request, f"{request.user.username} Daha once login olmussun")
        return redirect('home_view')
    context=dict()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        #Bu kullanici bilgileri dogru girmis mi
        if user is not None:
        # A backend authenticated the credentials
        #Login oldugunu kullaniciya belli edelim
            messages.add_message(request, messages.SUCCESS, 'Login oldun')
            login(request, user)
            return redirect('home_view')
        else:
            print('Return invalid login error message')
    return render(request, 'user_profile/login.html', context)

def logout_view(request):
    messages.info(request, f"{request.user.username} Oturumun kapatıldı")
    logout(request)
    return redirect('home_view')