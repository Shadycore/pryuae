from django.urls import path, include
from rpts.views import iProveedoresView, iClientesView, iComprasView 
from rpts.reportes import imprimirClientes, imprimirProveedores, imprimirCompras

urlpatterns = [
    #Reportes
    path('informe/proveedores', iProveedoresView.as_view(template_name='rpts/iProveedores.html'), name='iproveedores'),
    path('informe/clientes', iClientesView.as_view(template_name='rpts/iClientes.html'), name='iclientes'),
   path('informe/compras', iComprasView.as_view(template_name='rpts/iCompras.html'), name='icompras'),

    #Impresión
    path('informe/imprimir/clientes', imprimirClientes, name="imprimirclientes"),
    path('informe/imprimir/proveedores', imprimirProveedores, name="imprimirproveedores"),
    path('informe/imprimircompras/<int:id>/<str:f1>/<str:f2>', imprimirCompras, name="imprimircompras"),
]
