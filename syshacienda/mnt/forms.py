from cProfile import label
from dataclasses import fields
from socket import fromshare
from tkinter import Widget
from django import forms
from django.forms import DateInput
from .models import Cultivo


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
                'estado': forms.CheckboxInput} 

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
