from django.urls import path, include
from rpts.views import iProveedoresView, iClientesView, iComprasView 
urlpatterns = [
    #Reportes
    path('Informe/proveedores', iProveedoresView.as_view(template_name='rpts/iProveedores.html'), name='iproveedores'),
    path('Informe/clientes', iClientesView.as_view(template_name='rpts/iClientes.html'), name='iclientes'),
   path('Informe/compras', iComprasView.as_view(template_name='rpts/iCompras.html'), name='icompras'),
]
