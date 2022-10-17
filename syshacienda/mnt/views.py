from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from mnt.models import Cultivo

class CultivoList(LoginRequiredMixin, generic.ListView):
    model = Cultivo
    template_name="mnt/Cultivolist.html"
    context_object_name = "obj"
    login_url = "baseapp:login"
