from django.urls import path, include
from bi.views import analiticaView, superficieView, rendimientoView, cantidadesView, \
                    costoproduccionView, precioventaView, lotescultivadosView, \
                    masproducidosView, valorminimoView, valormaximoView, valorpromedioView

urlpatterns = [
    path('analitica', analiticaView, name="analiticaView"),
    path('superficie', superficieView, name="superficieView"),
    path('rendimiento', rendimientoView, name="rendimientoView"),
    path('cantidades', cantidadesView, name="cantidadesView"),
    path('costoproduccion', costoproduccionView, name="costoproduccionView"),    
    path('precioventa', precioventaView, name="precioventaView"),    
    path('lotescultivados', lotescultivadosView, name="lotescultivadosView"),    
    path('masproducidos', masproducidosView, name="masproducidosView"),    
    path('valorminimo', valorminimoView, name="valorminimoView"),
    path('valormaximo', valormaximoView, name="valormaximoView"),
    path('valorpromedio', valorpromedioView, name="valorpromedioView"),
    
    
]
