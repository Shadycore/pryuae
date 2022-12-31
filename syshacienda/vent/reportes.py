from django.shortcuts import render
from django.utils.dateparse import parse_date
from datetime import timedelta

from vent.models import Venta, DetalleVenta

def imprimir_venta_recibo(request,id):
    template_name="vent/venta_imprimir.html"

    vent = Venta.objects.get(id=id)
    det = DetalleVenta.objects.filter(venta=id)

    context={
        'request':request,
        'venta':vent,
        'detalle':det
    }

    return render(request,template_name,context)

def imprimir_venta_list(request,f1,f2):
    template_name="vent/venta_imprimir_all.html"

    f1=parse_date(f1)
    f2=parse_date(f2)
    f2=f2 + timedelta(days=1)

    enc = Venta.objects.filter(fecha__gte=f1,fecha__lt=f2)
    f2=f2 - timedelta(days=1)
    
    context = {
        'request':request,
        'f1':f1,
        'f2':f2,
        'enc':enc
    }

    return render(request,template_name,context)
