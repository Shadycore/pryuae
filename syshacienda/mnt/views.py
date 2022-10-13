from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

class CultivoList(LoginRequiredMixin, generic.ListView):
    pass
