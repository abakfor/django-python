from django.shortcuts import render, redirect
from django.views.generic import TemplateView

def index(request):
    return redirect('index')
class IndexView(TemplateView):
    template_name = 'index.html'
