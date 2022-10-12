from django.urls import path, include
from baseapp.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
