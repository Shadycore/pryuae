from abc import abstractmethod
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
from mnt.models import Cultivo, \
                    Insumo, \
                    Hacienda, \
                    Empleado, \
                    Proveedor, \
                    Cliente, \
                    Actividad, \
                    Asignacion, \
                    AsignacionMaterial, \
                    Cosecha, \
                    RegistroEmpleado, \
                    Produccion, \
                    DescripcionLote, \
                    RegistroInsumo, \
                    Parametro

from mnt.forms import CultivoForm, \
                    InsumoForm, \
                    HaciendaForm, \
                    EmpleadoForm, \
                    ProveedorForm, \
                    ClienteForm, \
                    ActividadForm, \
                    AsignacionForm, \
                    AsignacionMaterialForm, \
                    CosechaForm, \
                    RegistroEmpleadoForm, \
                    ProduccionForm, \
                    DescripcionLoteForm, \
                    RegistroInsumoForm, \
                    ParametroForm

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

## Hacienda  ------------------------------------------------------------
class HaciendaView(LoginRequiredMixin, generic.ListView):
    model = Hacienda
    template_name="mnt/hacienda_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class HaciendaNew(LoginRequiredMixin, generic.CreateView):
    model = Hacienda
    template_name = "mnt/hacienda_form.html"
    context_object_name =  "obj"
    form_class = HaciendaForm 
    success_url = reverse_lazy("mnt:hacienda_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)

class HaciendaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Hacienda
    template_name = "mnt/hacienda_form.html"
    context_object_name =  "obj"
    form_class = HaciendaForm 
    success_url = reverse_lazy("mnt:hacienda_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)

## Empleado  ------------------------------------------------------------
class EmpleadoView(LoginRequiredMixin, generic.ListView):
    model = Empleado
    template_name="mnt/empleado_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class EmpleadoNew(LoginRequiredMixin, generic.CreateView):
    model = Empleado
    template_name = "mnt/empleado_form.html"
    context_object_name =  "obj"
    form_class = EmpleadoForm 
    success_url = reverse_lazy("mnt:empleado_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)

class EmpleadoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Empleado
    template_name = "mnt/empleado_form.html"
    context_object_name =  "obj"
    form_class = EmpleadoForm 
    success_url = reverse_lazy("mnt:empleado_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)

## Proveedor  ------------------------------------------------------------
class ProveedorView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name="mnt/proveedor_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class ProveedorNew(LoginRequiredMixin, generic.CreateView):
    model = Proveedor
    template_name = "mnt/proveedor_form.html"
    context_object_name =  "obj"
    form_class = ProveedorForm 
    success_url = reverse_lazy("mnt:proveedor_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)

class ProveedorEdit(LoginRequiredMixin, generic.UpdateView):
    model = Proveedor
    template_name = "mnt/proveedor_form.html"
    context_object_name =  "obj"
    form_class = ProveedorForm 
    success_url = reverse_lazy("mnt:proveedor_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)

## Cliente  ------------------------------------------------------------
class ClienteView(LoginRequiredMixin, generic.ListView):
    model = Cliente
    template_name="mnt/cliente_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class ClienteNew(LoginRequiredMixin, generic.CreateView):
    model = Cliente
    template_name = "mnt/cliente_form.html"
    context_object_name =  "obj"
    form_class = ClienteForm 
    success_url = reverse_lazy("mnt:cliente_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)

class ClienteEdit(LoginRequiredMixin, generic.UpdateView):
    model = Cliente
    template_name = "mnt/cliente_form.html"
    context_object_name =  "obj"
    form_class = ClienteForm 
    success_url = reverse_lazy("mnt:cliente_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)

## Actividad  ------------------------------------------------------------
class ActividadView(LoginRequiredMixin, generic.ListView):
    model = Actividad
    template_name="mnt/actividad_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class ActividadNew(LoginRequiredMixin, generic.CreateView):
    model = Actividad
    template_name = "mnt/actividad_form.html"
    context_object_name =  "obj"
    form_class = ActividadForm 
    success_url = reverse_lazy("mnt:actividad_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)

class ActividadEdit(LoginRequiredMixin, generic.UpdateView):
    model = Actividad
    template_name = "mnt/actividad_form.html"
    context_object_name =  "obj"
    form_class = ActividadForm 
    success_url = reverse_lazy("mnt:actividad_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)
"""
class ActividadDel(LoginRequiredMixin, generic.UpdateView):
    model = Actividad
    template_name = "mnt/actividad_del.html"
    context_object_name =  "obj"
    form_class = ActividadForm 
    success_url = reverse_lazy("mnt:actividad_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)
"""
## Asignacion  ------------------------------------------------------------
class AsignacionView(LoginRequiredMixin, generic.ListView):
    model = Asignacion
    template_name="mnt/asignacion_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class AsignacionNew(LoginRequiredMixin, generic.CreateView):
    model = Asignacion
    template_name = "mnt/asignacion_form.html"
    context_object_name =  "obj"
    form_class = AsignacionForm 
    success_url = reverse_lazy("mnt:asignacion_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)

class AsignacionEdit(LoginRequiredMixin, generic.UpdateView):
    model = Asignacion
    template_name = "mnt/asignacion_form.html"
    context_object_name =  "obj"
    form_class = AsignacionForm 
    success_url = reverse_lazy("mnt:asignacion_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)

## AsignacionMaterial  ------------------------------------------------------------
class AsignacionMaterialView(LoginRequiredMixin, generic.ListView):
    model = AsignacionMaterial
    template_name="mnt/asignacionmaterial_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class AsignacionMaterialNew(LoginRequiredMixin, generic.CreateView):
    model = AsignacionMaterial
    template_name = "mnt/asignacionmaterial_form.html"
    context_object_name =  "obj"
    form_class = AsignacionMaterialForm 
    success_url = reverse_lazy("mnt:asignacionmaterial_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)

class AsignacionMaterialEdit(LoginRequiredMixin, generic.UpdateView):
    model = AsignacionMaterial
    template_name = "mnt/asignacionmaterial_form.html"
    context_object_name =  "obj"
    form_class = AsignacionMaterialForm 
    success_url = reverse_lazy("mnt:asignacionmaterial_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)

## Cosecha  ------------------------------------------------------------
class CosechaView(LoginRequiredMixin, generic.ListView):
    model = Cosecha
    template_name="mnt/cosecha_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class CosechaNew(LoginRequiredMixin, generic.CreateView):
    model = Cosecha
    template_name = "mnt/cosecha_form.html"
    context_object_name =  "obj"
    form_class = CosechaForm 
    success_url = reverse_lazy("mnt:cosecha_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)

class CosechaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Cosecha
    template_name = "mnt/cosecha_form.html"
    context_object_name =  "obj"
    form_class = CosechaForm 
    success_url = reverse_lazy("mnt:cosecha_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)

## RegistroEmpleado  ------------------------------------------------------------
class RegistroEmpleadoView(LoginRequiredMixin, generic.ListView):
    model = RegistroEmpleado
    template_name="mnt/registroempleado_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class RegistroEmpleadoNew(LoginRequiredMixin, generic.CreateView):
    model = RegistroEmpleado
    template_name = "mnt/registroempleado_form.html"
    context_object_name =  "obj"
    form_class = RegistroEmpleadoForm 
    success_url = reverse_lazy("mnt:registroempleado_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)

class RegistroEmpleadoEdit(LoginRequiredMixin, generic.UpdateView):
    model = RegistroEmpleado
    template_name = "mnt/registroempleado_form.html"
    context_object_name =  "obj"
    form_class = RegistroEmpleadoForm 
    success_url = reverse_lazy("mnt:registroempleado_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)

## Produccion  ------------------------------------------------------------
class ProduccionView(LoginRequiredMixin, generic.ListView):
    model = Produccion
    template_name="mnt/produccion_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class ProduccionNew(LoginRequiredMixin, generic.CreateView):
    model = Produccion
    template_name = "mnt/produccion_form.html"
    context_object_name =  "obj"
    form_class = ProduccionForm 
    success_url = reverse_lazy("mnt:produccion_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)

class ProduccionEdit(LoginRequiredMixin, generic.UpdateView):
    model = Produccion
    template_name = "mnt/produccion_form.html"
    context_object_name =  "obj"
    form_class = ProduccionForm 
    success_url = reverse_lazy("mnt:produccion_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)

## DescripcionLote  ------------------------------------------------------------
class DescripcionLoteView(LoginRequiredMixin, generic.ListView):
    model = DescripcionLote
    template_name="mnt/descripcionlote_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class DescripcionLoteNew(LoginRequiredMixin, generic.CreateView):
    model = DescripcionLote
    template_name = "mnt/descripcionlote_form.html"
    context_object_name =  "obj"
    form_class = DescripcionLoteForm 
    success_url = reverse_lazy("mnt:descripcionlote_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)

class DescripcionLoteEdit(LoginRequiredMixin, generic.UpdateView):
    model = DescripcionLote
    template_name = "mnt/descripcionlote_form.html"
    context_object_name =  "obj"
    form_class = DescripcionLoteForm 
    success_url = reverse_lazy("mnt:descripcionlote_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)

## RegistroInsumo  ------------------------------------------------------------
class RegistroInsumoView(LoginRequiredMixin, generic.ListView):
    model = RegistroInsumo
    template_name="mnt/registroinsumo_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class RegistroInsumoNew(LoginRequiredMixin, generic.CreateView):
    model = RegistroInsumo
    template_name = "mnt/registroinsumo_form.html"
    context_object_name =  "obj"
    form_class = RegistroInsumoForm 
    success_url = reverse_lazy("mnt:registroinsumo_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)

class RegistroInsumoEdit(LoginRequiredMixin, generic.UpdateView):
    model = RegistroInsumo
    template_name = "mnt/registroinsumo_form.html"
    context_object_name =  "obj"
    form_class = RegistroInsumoForm 
    success_url = reverse_lazy("mnt:registroinsumo_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)


## Parametro  ------------------------------------------------------------
class ParametroView(LoginRequiredMixin, generic.ListView):
    model = Parametro
    template_name="mnt/parametro_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class ParametroNew(LoginRequiredMixin, generic.CreateView):
    model = Parametro
    template_name = "mnt/parametro_form.html"
    context_object_name =  "obj"
    form_class = ParametroForm 
    success_url = reverse_lazy("mnt:parametro_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)

class ParametroEdit(LoginRequiredMixin, generic.UpdateView):
    model = Parametro
    template_name = "mnt/parametro_form.html"
    context_object_name =  "obj"
    form_class = ParametroForm 
    success_url = reverse_lazy("mnt:parametro_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)
