from django.urls import path, include
from vent.views import VentaView, VentaNew, VentaEdit, DetalleVentaEdit, DetalleVentaNew, \
                        DetalleVentaView, Ventas, ProduccionView 

urlpatterns = [
    #Ventas
    path('Ventas/', VentaView.as_view(template_name='vent/venta_list.html'), name='venta_list'),
    path('Venta/new', Ventas, name='venta_new'),
    path('Venta/edit/<int:pk>', Ventas, name='venta_edit'),
    path('venta/venta_busca_produccion',ProduccionView.as_view(), name="venta_busca_produccion"),
]
