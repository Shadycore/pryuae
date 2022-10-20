from abc import abstractmethod
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
from mnt.models import Cultivo, Insumo
from mnt.forms import CultivoForm, InsumoForm

## Cultivo ------------------------------------------------------------
class CultivoView(LoginRequiredMixin, generic.ListView):
    model = Cultivo
    template_name="mnt/cultivo_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class CultivoNew(LoginRequiredMixin, generic.CreateView):
    model = Cultivo
    template_name = "mnt/cultivo_form.html"
    context_object_name =  "obj"
    form_class = CultivoForm 
    success_url = reverse_lazy("mnt:cultivo_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)

class CultivoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Cultivo
    template_name = "mnt/cultivo_form.html"
    context_object_name =  "obj"
    form_class = CultivoForm 
    success_url = reverse_lazy("mnt:cultivo_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)

## Insumo  ------------------------------------------------------------
class InsumoView(LoginRequiredMixin, generic.ListView):
    model = Insumo
    template_name="mnt/insumo_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class InsumoNew(LoginRequiredMixin, generic.CreateView):
    model = Insumo
    template_name = "mnt/insumo_form.html"
    context_object_name =  "obj"
    form_class = InsumoForm 
    success_url = reverse_lazy("mnt:insumo_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)

class InsumoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Insumo
    template_name = "mnt/insumo_form.html"
    context_object_name =  "obj"
    form_class = InsumoForm 
    success_url = reverse_lazy("mnt:insumo_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)