from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
from mnt.models import Cultivo
#from mnt.forms import CultivoForm

class CultivoView(LoginRequiredMixin, generic.ListView):
    model = Cultivo
    template_name="mnt/cultivo_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"
"""
class CultivoIns(LoginRequiredMixin, generic.CreateView):
    model = Cultivo
    template_name = "mnt/CultivoForm.html"
    context_object_name: str = "obj"
    form_class = CultivoForm 
    success_url = reverse_lazy("mnt/Cultivos")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
"""