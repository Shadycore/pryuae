from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

class Home(generic.TemplateView):
    template_name = 'baseapp/home.html'
    login_url = "baseapp/login.html"
