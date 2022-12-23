from django.urls import path, include
from api.views import ProduccionList, ProduccionDetalle, ClienteList

urlpatterns = [
    path('v1/ProduccionList/',ProduccionList.as_view(),name='ProduccionList'),
    path('v1/ProduccionDetalle/<str:codigo>',ProduccionDetalle.as_view(),name='ProduccionDetalle'),
    path('v1/clientes/',ClienteList.as_view(),name='ClienteList')
]