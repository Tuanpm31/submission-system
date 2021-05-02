from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register", register, name="register"),
    path("login", LoginView.as_view(extra_context={'title': 'Login'}), name="login"),
    path("logout", LogoutView.as_view(extra_context={'title': 'Logout'}), name="logout"),
]
