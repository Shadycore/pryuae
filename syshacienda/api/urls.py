from django.urls import path, include
from api.views import ProduccionList, ProduccionDetalle, ClienteList

urlpatterns = [
    path('v1/Produccion/',ProduccionList.as_view(),name='produccion_list'),
    path('v1/ProduccionDetalle/<str:codigo>',ProduccionDetalle.as_view(),name='produccion_detalle'),
    path('v1/clientes/',ClienteList.as_view(),name='cliente_list')
]