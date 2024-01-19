from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from .views import index, register, profile, match, matches, predictions, view_sports, view_matches, view_match,view_logout, confirmation_page
from django.conf.urls.static import static
from django.conf import settings

app_name = 'app'

urlpatterns = [
    path("", index, name="index"),
    path("register",register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="app/login.html")),
    path('logout/', view_logout , name='logout'),
    path("change-password/", auth_views.PasswordChangeView.as_view(template_name="change-password.html")),
    path('profile/', profile , name='profile'),
    path('match/<int:match_id>/', view_match , name='view_match'),
    path('confirmation/<int:match_id>/', confirmation_page, name='confirmation_page'),
    path('matches/', matches , name='matches'),
    path('matches/<int:sport_id>/', view_matches , name='view_matches'),
    path('predictions/', predictions , name='predictions'),
    path('sports/', view_sports , name='sports'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)