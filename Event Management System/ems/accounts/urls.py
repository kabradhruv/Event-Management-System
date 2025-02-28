from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# app_name='accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
]
