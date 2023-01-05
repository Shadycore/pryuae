from django.db import models

#Para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum


from django.db import models
from vent.models import Venta, DetalleVenta
from mnt.models import Cliente, Cultivo, Produccion, Empleado, Asignacion, Proveedor
# Create your models here.


