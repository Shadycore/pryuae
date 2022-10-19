from django.urls import path, include
from mnt.views import CultivoView, CultivoNew, CultivoEdit

urlpatterns = [
    path('Cultivos/', CultivoView.as_view(template_name='mnt/cultivo_list.html'), name='cultivo_list'),
    path('Cultivo/new', CultivoNew.as_view(template_name='mnt/cultivo_form.html'), name='cultivo_new'),
    path('Cultivo/edit/<int:pk>', CultivoEdit.as_view(template_name='mnt/cultivo_form.html'), name='cultivo_edit'),
]
