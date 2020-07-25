from django.urls import path, include
from . import views
from .views import IndexView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index),
    path('index/', IndexView.as_view(), name='index')
]
