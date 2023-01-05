from django.urls import path, include
from rpts.views import iProveedoresView, iClientesView, iComprasView 
from rpts.reportes import imprimirLista

urlpatterns = [
    #Reportes
    path('informe/proveedores', iProveedoresView.as_view(template_name='rpts/iProveedores.html'), name='iproveedores'),
    path('informe/clientes', iClientesView.as_view(template_name='rpts/iClientes.html'), name='iclientes'),
   path('informe/compras', iComprasView.as_view(template_name='rpts/iCompras.html'), name='icompras'),

    #Impresión
    path('informe/imprimir/<int:id>', imprimirLista, name="imprimelista"),
    path('informe/imprimircompra/<int:id>/<str:f1>/<str:f2>', imprimirLista, name="imprimecompra"),
]
