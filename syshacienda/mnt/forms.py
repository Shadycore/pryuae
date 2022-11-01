from cProfile import label
from dataclasses import fields
from datetime import date
from socket import fromshare
from tkinter import Widget
from django import forms
from django.forms import DateInput
from mnt.models import *

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class CultivoForm(forms.ModelForm):
    class Meta:
        model = Cultivo
        fields = ['nombre',
                    'lote',
                    'fechaInicio',
                    'fechaFin',
                    'estado']
        labels = {'nombre':'Nombre del Cultivo',
                'lote': 'Lote',
                'fechaInicio': 'Fecha de inicio',
                'fechaFin' : 'Fecha Finalización',
                'estado': 'Estado'}

        Widget = {'descripcion': forms.TextInput,
                'lote': forms.TextInput,
                'fechaInicio': forms.DateInput,
                'fechaFin': forms.DateInput,
                #'estado': forms.CheckboxInput
                } 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        #self.fields['fechaFin'].widget.format = '%d/%m/%Y'
        #self.fields['estado'].widget.attrs  ="class: form-control"

    
class InsumoForm(forms.ModelForm):

    class Meta:
        model = Insumo
        fields = ['nombre',
                    'tipo',
                    'uso',
                    'precio',
                    'estado']
        labels = {'nombre':'Nombre del Cultivo',
                'tipo': 'Tipo',
                'uso': 'Uso',
                'precio' : 'Precio',
                'estado': 'Estado'}

        Widget = {'nombre': forms.TextInput,
                'tipo': forms.TextInput,
                'uso': forms.TextInput,
                'precio': forms.FloatField,
                'estado': forms.CheckboxInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class HaciendaForm(forms.ModelForm):

    class Meta:
        model = Hacienda
        fields = ['nombre',
                    'apellido',
                    'identificacion',
                    'telefono',
                    'celular',
                    'email',
                    'direccion',
                    'ciudad',
                    'estado']
        labels = {'nombre':'Nombre de la Hacienda',
                'apellido': 'Razón Social',
                'identificacion': 'Identificacion',
                'telefono': 'Teléfono',
                'celular' : 'Celular',
                'email' : 'Email',
                'direccion' : 'Direccion',
                'ciudad' : 'Ciudad',
                'estado': 'Estado'}

        Widget = {'nombre': forms.TextInput,
                'apellido': forms.TextInput,
                'identificacion': forms.TextInput,
                'telefono': forms.TextInput,
                'celular': forms.TextInput,
                'email': forms.TextInput,
                'direccion': forms.TextInput,
                'ciudad': forms.TextInput,
                'estado': forms.CheckboxInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = ['nombre',
                    'apellido',
                    'identificacion',
                    'telefono',
                    'celular',
                    'email',
                    'direccion',
                    'ciudad',
                    'fchNacimiento',
                    'estado']
        labels = {'nombre':'Nombre',
                'apellido': 'Apellido',
                'identificacion': 'Identificación',
                'telefono': 'Teléfono',
                'celular' : 'Celular',
                'email' : 'Email',
                'direccion' : 'Direccion',
                'ciudad' : 'Ciudad',
                'fchNacimiento': 'Fecha de Nacimiento',
                'estado': 'Estado'}

        Widget = {'nombre': forms.TextInput,
                'apellido': forms.TextInput,
                'identificacion': forms.TextInput,
                'telefono': forms.TextInput,
                'celular': forms.TextInput,
                'email': forms.TextInput,
                'direccion': forms.TextInput,
                'ciudad': forms.TextInput,
                'fchNacimiento': forms.DateInput,
                'estado': forms.CheckboxInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ['nombre',
                    'apellido',
                    'identificacion',
                    'telefono',
                    'celular',
                    'email',
                    'direccion',
                    'ciudad',
                    'descripcion',
                    'estado']
        labels = {'nombre':'Nombre de la Hacienda',
                'apellido': 'Razón Social',
                'identificacion': 'Identificacion',
                'telefono': 'Teléfono',
                'celular' : 'Celular',
                'email' : 'Email',
                'direccion' : 'Direccion',
                'ciudad' : 'Ciudad',
                'descripcion': 'Descripción',
                'estado': 'Estado'}

        Widget = {'nombre': forms.TextInput,
                'apellido': forms.TextInput,
                'identificacion': forms.TextInput,
                'telefono': forms.TextInput,
                'celular': forms.TextInput,
                'email': forms.TextInput,
                'direccion': forms.TextInput,
                'ciudad': forms.TextInput,
                'descripcion': forms.TextInput,
                'estado': forms.CheckboxInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nombre',
                    'apellido',
                    'identificacion',
                    'telefono',
                    'celular',
                    'email',
                    'direccion',
                    'ciudad',
                    'estado']
        labels = {'nombre':'Nombre de la Hacienda',
                'apellido': 'Razón Social',
                'identificacion': 'Identificacion',
                'telefono': 'Teléfono',
                'celular' : 'Celular',
                'email' : 'Email',
                'direccion' : 'Direccion',
                'ciudad' : 'Ciudad',
                'estado': 'Estado'}

        Widget = {'nombre': forms.TextInput,
                'apellido': forms.TextInput,
                'identificacion': forms.TextInput,
                'telefono': forms.TextInput,
                'celular': forms.TextInput,
                'email': forms.TextInput,
                'direccion': forms.TextInput,
                'ciudad': forms.TextInput,
                'estado': forms.CheckboxInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class ActividadForm(forms.ModelForm):
    cultivo = forms.ModelChoiceField(
        queryset=Cultivo.objects.filter(estado=True)
        .order_by('nombre')
    )
    class Meta:
        model = Actividad
        fields = ['cultivo',
                    'nombre',
                    'fecha',
                    'estado']
        labels = {
                'nombre': 'Nombre de actividad',
                'fecha': 'Fecha registro',
                'estado': 'Estado'
                }

        Widget = {'nombre': forms.TextInput,
                'fecha': forms.DateInput,
                'estado': forms.CheckboxInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['cultivo'].empty_label =  "Seleccione el cultivo"

class AsignacionForm(forms.ModelForm):
    cultivo = forms.ModelChoiceField(
        queryset=Cultivo.objects.filter(estado=True)
        .order_by('nombre')
    )
    actividad = forms.ModelChoiceField(
        queryset=Actividad.objects.filter(estado=True)
        .order_by('nombre')
    )
    empleado = forms.ModelChoiceField(
        queryset=Empleado.objects.filter(estado=True)
        .order_by('nombre')
    )
    class Meta:
        model = Asignacion
        fields = ['cultivo',
                    'actividad',
                    'empleado',
                    'descripcion',
                    'fecha',
                    'estado']
        labels = {
                'descripcion': 'Actividad a realizar',
                'fecha': 'Fecha',
                'estado': 'Estado'
                }

        Widget = {'descripcion': forms.TextInput,
                'fecha': forms.DateInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['actividad'].empty_label =  "Seleccione la actividad"
        self.fields['empleado'].empty_label =  "Seleccione el empleado"
        self.fields['cultivo'].empty_label =  "Seleccione el cultivo"

class AsignacionMaterialForm(forms.ModelForm):
    cultivo = forms.ModelChoiceField(
        queryset=Cultivo.objects.filter(estado=True)
        .order_by('nombre')
    )
    insumo = forms.ModelChoiceField(
        queryset=Insumo.objects.filter(estado=True)
        .order_by('nombre')
    )

    class Meta:
        model = AsignacionMaterial
        fields = ['cultivo',
                    'insumo',
                    'encargado',
                    'fecha',
                    'estado']
        labels = {
                'encargado': 'Persona encargada',
                'fecha': 'Fecha',
                'estado': 'Estado'
                }

        Widget = {'encargado': forms.TextInput,
                'fecha': forms.DateInput,
                'estado': forms.CheckboxInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['insumo'].empty_label =  "Seleccione el insumo"
        self.fields['cultivo'].empty_label =  "Seleccione el cultivo"

class CosechaForm(forms.ModelForm):
    cultivo = forms.ModelChoiceField(
        queryset=Cultivo.objects.filter(estado=True)
        .order_by('nombre')
    )
    hacienda = forms.ModelChoiceField(
        queryset=Hacienda.objects.filter(estado=True)
        .order_by('nombre')
    )

    class Meta:
        model = Cosecha
        fields = ['cultivo',
                    'hacienda',
                    'fecha',
                    'cantidad',
                    'estado']
        labels = {
                'cantidad': 'Cantidad cosecha',
                'fecha': 'Fecha',
                'estado': 'Estado'
                }

        Widget = {'cantidad': forms.IntegerField,
                'fecha': forms.DateInput,
                'estado': forms.CheckboxInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['hacienda'].empty_label =  "Seleccione la hacienda"
        self.fields['cultivo'].empty_label =  "Seleccione el cultivo"

class RegistroEmpleadoForm(forms.ModelForm):
    empleado = forms.ModelChoiceField(
        queryset=Empleado.objects.filter(estado=True)
        .order_by('nombre')
    )
    hacienda = forms.ModelChoiceField(
        queryset=Hacienda.objects.filter(estado=True)
        .order_by('nombre')
    )

    class Meta:
        model = RegistroEmpleado
        fields = ['empleado',
                    'hacienda',
                    'contrato',
                    'cargo',
                    'estado']
        labels = {
                'contrato': 'Contrato empleado',
                'cargo': 'Cargo empleado',
                'estado': 'Estado'
                }

        Widget = {'contrato': forms.TextInput,
                'cargo': forms.TextInput,
                'estado': forms.CheckboxInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['hacienda'].empty_label =  "Seleccione la hacienda"
        self.fields['empleado'].empty_label =  "Seleccione el empleado"

class ProduccionForm(forms.ModelForm):
    cultivo = forms.ModelChoiceField(
        queryset=Cultivo.objects.filter(estado=True)
        .order_by('nombre')
    )
    insumo = forms.ModelChoiceField(
        queryset=Insumo.objects.filter(estado=True)
        .order_by('nombre')
    )

    class Meta:
        model = Produccion
        fields = ['cultivo',
        'estado',
                    'insumo',
                    'fecha',
                    'cantidadCosecha'
                    ]
        labels = {
                'cantidadCosecha': 'Cantidad cosecha',
                'fecha': 'Fecha',
                'estado': 'Estado'
                }

        Widget = {'cantidadCosecha': forms.IntegerField,
                'fecha': forms.DateInput,
                'estado': forms.CheckboxInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['insumo'].empty_label =  "Seleccione el insumo"
        self.fields['cultivo'].empty_label =  "Seleccione el cultivo"

class DescripcionLoteForm(forms.ModelForm):
    cultivo = forms.ModelChoiceField(
        queryset=Cultivo.objects.filter(estado=True)
        .order_by('nombre')
    )
    produccion = forms.ModelChoiceField(
        queryset=Produccion.objects.filter(estado=True)
        .order_by('cultivo')
    )

    class Meta:
        model = DescripcionLote
        fields = ['cultivo',
                    'produccion',
                    'area',
                    'etapa',
                    'estado']
        labels = {
                'area': 'Ingrese area',
                'etapa': 'Ingrese etapa',
                'estado': 'Estado'
                }

        Widget = {'area': forms.TextInput,
                'etapa': forms.TextInput,
                'estado': forms.CheckboxInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['cultivo'].empty_label =  "Seleccione el cultivo"
        self.fields['produccion'].empty_label =  "Seleccione la producción"

class RegistroInsumoForm(forms.ModelForm):
    cultivo = forms.ModelChoiceField(
        queryset=Cultivo.objects.filter(estado=True)
        .order_by('nombre')
    )
    insumo = forms.ModelChoiceField(
        queryset=Insumo.objects.filter(estado=True)
        .order_by('nombre')
    )

    class Meta:
        model = RegistroInsumo
        fields = ['cultivo',
                    'insumo',
                    'fechaCompra',
                    'precio',
                    'fechaIngreso',
                    'fechaExpira',
                    'requerimiento',
                    'estado']
        labels = {
                'fechaCompra': 'Fecha de Compra',
                'precio':'Precio',
                'fechaIngreso':'Fecha de ingreso',
                'fechaExpira':'Fecha de expiración',
                'requerimiento': 'Ingrese el requerimiento',
                'estado': 'Estado'
                }

        Widget = {'precio': forms.IntegerField,
                'fechaCompra': forms.DateInput,
                'fechaIngreso': forms.DateInput,
                'fechaExpira': forms.DateInput,
                'requerimiento': forms.TextInput,
                'estado': forms.CheckboxInput
                } 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['insumo'].empty_label =  "Seleccione el insumo"
        self.fields['cultivo'].empty_label =  "Seleccione el cultivo"
