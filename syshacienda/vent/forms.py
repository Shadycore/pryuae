from cProfile import label
from dataclasses import fields
from datetime import date
#from socket import fromshare
from tkinter import Widget
from django import forms
from django.forms import DateInput
from mnt import models
from mnt.models import Cliente, Cultivo, Produccion
from vent.models import Venta, DetalleVenta


class VentaForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.filter(estado=True)
        .order_by('nombre')
    )

    class Meta:
        model = Venta
        fields = ['totalVenta',
                    'fechaVenta',
                    'estado']
        labels = {'cantidadVenta':'Cantidad Venta',
                'fechaVenta': 'Fecha de Venta',
                'estado': 'Estado'}

        Widget = {'cantidadVenta': forms.FloatField,
                'fechaVenta': forms.DateInput,
                'estado': forms.CheckboxInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['cliente'].empty_label =  "Seleccione el cliente"


class DetalleVentaForm:
    cultivo = forms.ModelChoiceField(
                queryset=Cultivo.objects.filter(estado=True)
                    .order_by('nombre'))
    produccion = forms.ModelChoiceField(
                queryset=Produccion.objects.filter(estado=True)
                    .order_by('cultivo_id'))
    class Meta:
        model = DetalleVenta
        fields = ['cantidad',
                    'precio',
                    'estado']
        labels = {'cantidad':'Ingres cantidad',
                'precio': 'Precio venta',
                'estado': 'Estado'}

        Widget = {'cantidad': forms.FloatField,
                'precio': forms.FloatField,
                'estado': forms.CheckboxInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['cultivo'].empty_label =  "Seleccione el cultivo"
        self.fields['produccion'].empty_label =  "Seleccione la producción"
