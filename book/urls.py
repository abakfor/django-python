from django.urls import path, include
from . import views
from .views import IndexView


urlpatterns = [
    path('', views.index, name=''),
    path('index/', IndexView.as_view(), name='index')
]
