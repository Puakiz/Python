"""Defines URL patterns for learning_logs."""
from django.urls import path, re_path

from . import views

app_name = "learning_logs"

urlpatterns = [
    # Home page
    re_path(r'^$', views.index, name='index'),

    # Show all topics.
    re_path(r'^topics/$', views.topics, name='topics'),
]
