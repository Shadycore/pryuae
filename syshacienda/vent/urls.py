from django.urls import path, include
from vent.views import VentaView, Ventas, ProduccionView 
from vent.reportes import imprimir_venta_list, imprimir_venta_recibo
urlpatterns = [
    #Ventas
    path('Ventas/', VentaView.as_view(template_name='vent/venta_list.html'), name='venta_list'),
    path('Venta/new', Ventas, name='venta_new'),
    path('Venta/edit/<int:pk>', Ventas, name='venta_edit'),
    path('Venta/busca_produccion',ProduccionView.as_view(), name="busca_produccion"),
    path('Venta/imprimir/<int:pk>',imprimir_venta_recibo, name="venta_imprimir"),
    path('Venta/imprimir-todas/<str:f1>/<str:f2>',imprimir_venta_list, name="venta_imprimir_all"),

]
