from django.urls import path, include
from bi.views import analiticaView

urlpatterns = [
    path('analitica', analiticaView, name="analiticaView"),
]
