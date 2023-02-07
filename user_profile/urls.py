from django.urls import path
from user_profile.views import login_view


app_name='user_profile'
urlpatterns = [
    path("login/", login_view,name= 'login_view'),
]
