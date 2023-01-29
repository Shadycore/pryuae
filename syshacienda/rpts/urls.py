from django.urls import path, include
from rpts.views import iProveedoresView, iClientesView, \
                        iComprasView, iComprasView_, \
                        oProduccionView, oProductosMasVendidosView, \
                        oVentasPorCultivoView, oGananciasView, \
                        impComprasView, impGananciasView, impProduccionView, \
                        impProductosMasVendidosView, impVentasPorCultivoView
                        
from rpts.reportes import imprimirClientes, imprimirProveedores

urlpatterns = [
    #Reportes
    path('informe/proveedores', iProveedoresView.as_view(template_name='rpts/iProveedores.html'), name='iproveedores'),
    path('informe/clientes', iClientesView.as_view(template_name='rpts/iClientes.html'), name='iclientes'),
    path('informe/compras', iComprasView, name='icompras'),
    path('informe/produccion', oProduccionView, name='iproduccion'),
    path('informe/productosmasvendidos', oProductosMasVendidosView, name='iproductosmasvendidos'),
    path('informe/ventasporcultivo', oVentasPorCultivoView, name='iventasporcultivo'),
    path('informe/ganancias', oGananciasView, name='iganancias'),

    #Impresión
    path('informe/imprimir/clientes', imprimirClientes, name="imprimirclientes"),
    path('informe/imprimir/proveedores', imprimirProveedores, name="imprimirproveedores"),
    path('informe/imprimir/compras/<int:f1>', impComprasView , name="imprimircompras"),
    path('informe/imprimir/ganancias/<int:f1>', impGananciasView , name="imprimirganancias"),
    path('informe/imprimir/produccion/<int:f1>', impProduccionView , name="imprimirproduccion"),
    path('informe/imprimir/productos/<int:f1>', impProductosMasVendidosView , name="imprimirproductos"),
    path('informe/imprimir/ventas/<int:f1>', impVentasPorCultivoView , name="imprimirventas"),
    
]
