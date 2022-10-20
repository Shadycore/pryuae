from django.urls import path, include
from mnt.views import CultivoView, CultivoNew, CultivoEdit
from mnt.views import InsumoView ,InsumoNew, InsumoEdit

urlpatterns = [
    #Cultivos
    path('Cultivos/', CultivoView.as_view(template_name='mnt/cultivo_list.html'), name='cultivo_list'),
    path('Cultivo/new', CultivoNew.as_view(template_name='mnt/cultivo_form.html'), name='cultivo_new'),
    path('Cultivo/edit/<int:pk>', CultivoEdit.as_view(template_name='mnt/cultivo_form.html'), name='cultivo_edit'),
    #Insumos
    path('Insumos/', InsumoView.as_view(template_name='mnt/insumo_list.html'), name='insumo_list'),
    path('Insumo/new', InsumoNew.as_view(template_name='mnt/insumo_form.html'), name='insumo_new'),
    path('Insumo/edit/<int:pk>', InsumoEdit.as_view(template_name='mnt/insumo_form.html'), name='insumo_edit'),

]
