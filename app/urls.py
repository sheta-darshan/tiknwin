from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from .views import index, register

app_name = 'app'

urlpatterns = [
    path("", index, name="index"),
    path("register",register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="app/login.html")),
    path('logout/', auth_views.LoginView.as_view(template_name="app/logout.html") , name='logout'),
    path("change-password/", auth_views.PasswordChangeView.as_view(template_name="change-password.html")),
]