from django.urls import path, include
from mnt.views import *

urlpatterns = [
    #Cultivos
    path('Ventas/', CultivoView.as_view(template_name='vent/venta_list.html'), name='venta_list'),
    path('Venta/new', CultivoNew.as_view(template_name='vent/cultivo_form.html'), name='venta_new'),
    path('Venta/edit/<int:pk>', CultivoEdit.as_view(template_name='vent/venta_form.html'), name='venta_edit'),

]
