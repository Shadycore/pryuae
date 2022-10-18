from django.urls import path, include
from mnt.views import CultivoView

urlpatterns = [
    path('Cultivos/', CultivoView.as_view(template_name='mnt/cultivo_list.html'), name='Cultivos'),
    # path('NuevoCultivo/', CultivoIns.as_view(template_name='mnt/CultivoForm.html'), name='NuevoCultivo'),
]
