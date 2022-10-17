from cProfile import label
from dataclasses import fields
from socket import fromshare
from tkinter import Widget
from django import froms
from .models import Cultivo


class CultivoForm(Forms.Models):
    class Meta:
        model = Cultivo
        fields = ['nombre','lote','fechaInicio','fechaFin']
        labels = ['nombre':'Nombre del Cultivo',
                'lote': 'Lote',
                'fechaInicio': 'Fecha de inicio',
                'fechaFin' : 'Fecha Finalización']
        Widget = ('descripcion': Forms.TextInput)