from django.urls import path, include
from mnt.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
