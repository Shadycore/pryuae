from django.urls import path, include
from rpts.views import iProveedoresView, iClientesView, \
                        iComprasView, iComprasView_, \
                        oProduccionView, oProductosMasVendidosView
from rpts.reportes import imprimirClientes, imprimirProveedores, imprimirCompras

urlpatterns = [
    #Reportes
    path('informe/proveedores', iProveedoresView.as_view(template_name='rpts/iProveedores.html'), name='iproveedores'),
    path('informe/clientes', iClientesView.as_view(template_name='rpts/iClientes.html'), name='iclientes'),
    #path('informe/compras', iComprasView_.as_view(template_name='rpts/icompras.html'), name='icompras'),
    path('informe/compras', iComprasView, name='icompras'),
    path('informe/produccion', oProduccionView, name='iproduccion'),
    path('informe/productosmasvendidos', oProductosMasVendidosView, name='iproductosmasvendidos'),
     path('informe/ventasporcultivo', oProductosMasVendidosView, name='iventasporcultivo'),
    #path('informe/compras/<int:f1>', iComprasView, name='icomprasf1'),

    #Impresión
    path('informe/imprimir/clientes', imprimirClientes, name="imprimirclientes"),
    path('informe/imprimir/proveedores', imprimirProveedores, name="imprimirproveedores"),
    path('informe/imprimir/compras/<int:f1>', iComprasView, name="imprimircompras"),
]
