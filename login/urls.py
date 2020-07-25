from django.urls import path, include
from . import views
from .views import SignInView
from .views import SignUpView

urlpatterns = [
    path('', views.index),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
