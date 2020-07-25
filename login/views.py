from django.shortcuts import render, redirect
from django.views.generic import TemplateView


def index(request):
    return redirect('signin')
class SignInView(TemplateView):
    template_name = 'authentication-signin2.html'
class SignUpView(TemplateView):
    template_name = 'authentication-signup2.html'
