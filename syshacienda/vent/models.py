from django.db import models

from baseapp.models import BaseFields
from mnt.models import Cliente, Cosecha, Produccion, Cultivo

## Venta ******************************************** ##
# - Venta - #
class Venta(BaseFields):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    fechaVenta = models.DateField(blank=True, null=True)
    totalVenta = models.FloatField(blank=True, null=True, default=0)
    porc_iva    = models.FloatField(blank=True, null=True)
    valor_iva = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "{} : {}  {}  {} ".format(self.id, self.id,self.cliente, self.totalVenta)

    def save (self):
        pass 
       
    class Meta:
        verbose_name_plural = "Ventas"
        db_table = 'venta'

# - DetalleVenta - #
class DetalleVenta(BaseFields):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, null=True)
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, null=True)
    produccion = models.ForeignKey(Produccion, on_delete=models.CASCADE, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)  
    
    def __str__(self):
        return "{} : {} {} {} ".format(self.venta_id, self.cultivo.nombre, self.cantidadVenta)

    def save (self):
        pass 

    class Meta:
        verbose_name_plural = "DetalleVentas"
        db_table = 'detalle_venta'
