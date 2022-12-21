from django.urls import path, include
from vent.views import VentaView, VentaNew, VentaEdit, DetalleVentaEdit, DetalleVentaNew, DetalleVentaView, Ventas 

urlpatterns = [
    #Ventas
    path('Ventas/', VentaView.as_view(template_name='vent/venta_list.html'), name='venta_list'),
    #path('Venta/new', VentaNew.as_view(template_name='vent/venta_form.html'), name='venta_new'),
    path('Venta/new', Ventas, name='venta_new'),
    #path('Venta/edit/<int:pk>', VentaEdit.as_view(template_name='vent/venta_form.html'), name='venta_edit'),
    #mantenimientos
    path('mnt/', include(('mnt.urls','mnt'), namespace="mnt")),
]
