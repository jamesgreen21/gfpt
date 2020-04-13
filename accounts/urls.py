from django.urls import path
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views


app_name = 'accounts'
urlpatterns = [
    path('register/', accounts_views.register, name='register'),
    path('profile/', accounts_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', accounts_views.user_logout, name='logout'),
]
