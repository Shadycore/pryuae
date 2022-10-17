from django.urls import path, include
from mnt.views import CultivoList

urlpatterns = [
    path('', CultivoList.as_view(), name='Cultivos'),
]
