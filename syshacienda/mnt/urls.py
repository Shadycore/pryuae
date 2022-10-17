from django.urls import path, include
from mnt.views import CultivoList

urlpatterns = [
    path('Cultivos/', CultivoList.as_view(), name='CultivosList'),
]
