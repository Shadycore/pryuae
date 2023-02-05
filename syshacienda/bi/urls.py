from django.urls import path, include
from bi.views import analiticaView, superficieView, rendimientoView, cantidadesView

urlpatterns = [
    path('analitica', analiticaView, name="analiticaView"),
    path('superficie', superficieView, name="superficieView"),
    path('rendimiento', rendimientoView, name="rendimientoView"),
    path('cantidades', cantidadesView, name="cantidadesView"),
    
]
