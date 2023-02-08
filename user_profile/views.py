from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def login_view(request):
    context=dict()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username, password)
        if user is not None:
        # A backend authenticated the credentials
        #Login oldugunu kullaniciya belli edelim
            login(request, user)
            return redirect('home_view')
        else:
            print('Return invalid login error message')
    return render(request, 'user_profile/login.html', context)
