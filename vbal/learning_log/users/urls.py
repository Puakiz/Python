"""Defines URL patterns for users"""

from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views

app_name = "users"

urlpatterns = [
    # Login page
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='users/login.html'),
            name='login'),

    # Logout page
    re_path(r'^logout/$', views.logout_view, name='logout'),

    # Regsitration page
    re_path(r'^register/$', views.register, name='register'),

]
