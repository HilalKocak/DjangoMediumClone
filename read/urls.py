from django.urls import path
from user_profile.views import login_view, logout_view, register_view
from .views import all_posts_view

app_name='read'
urlpatterns = [
    path('<slug:user_slug>/', all_posts_view, name='all_posts_view'),

]
