from cProfile import label
from dataclasses import fields
from datetime import date
from socket import fromshare
from tkinter import Widget
from django import forms
from django.forms import DateInput
from mnt.models import *
from vent.models import *


class VentaForm(forms.ModelForm):
    cultivo = forms.ModelChoiceField(
        queryset=Cultivo.objects.filter(estado=True)
        .order_by('nombre')
    )
    produccion = forms.ModelChoiceField(
        queryset=Produccion.objects.filter(estado=True)
        .order_by('cultivo')
    )

    class Meta:

        model = Venta
        fields = ['cantidad',
                    'precio',
                    'fecha',
                    'estado']
        labels = {'cantidad':'Ingres cantidad',
                'precio': 'Precio',
                'fecha': 'Fecha',
                'estado': 'Estado'}

        Widget = {'cantidad': forms.FloatField,
                'precio': forms.FloatField,
                'fecha': forms.DateInput,
                'estado': forms.CheckboxInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

        self.fields['cultivo'].empty_label =  "Seleccione el cultivo"
        self.fields['produccion'].empty_label =  "Seleccione la producción"


class DetalleVentaForm:
    venta = forms.ModelChoiceField(
        queryset=Cultivo.objects.filter(estado=True)
        .order_by('id')
    )
    cliente = forms.ModelChoiceField(
        queryset=Produccion.objects.filter(estado=True)
        .order_by('nombre')
    )

    class Meta:
        model = DetalleVenta
        fields = ['cantidadVenta',
                    'fechaVenta',
                    'estado']
        labels = {'cantidadVenta':'Cantidad Venta',
                'fechaVenta': 'Fecha de Venta',
                'estado': 'Estado'}

        Widget = {'cantidad': forms.FloatField,
                'precio': forms.FloatField,
                'fecha': forms.DateInput,
                'estado': forms.CheckboxInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

        self.fields['venta'].empty_label =  "Seleccione la venta"
        self.fields['cliente'].empty_label =  "Seleccione el cliente"

