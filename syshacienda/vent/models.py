from django.db import models
#Para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

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
        self.total = float(float(int(self.cantidad)) * float(self.precio))
        self.proc_iva = self.proc_iva
        self.valor_iva = self.valor_iva
        self.cliente = self.cliente
        super(DetalleVenta,self).save() 
 
       
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
    total = models.FloatField(blank=True, null=True, default=0)
    def __str__(self):
        return "{} : {} {} {} ".format(self.venta_id, self.cultivo, self.cantidad, self.total)

    def save (self):
        pass

    class Meta:
        verbose_name_plural = "DetalleVentas"
        db_table = 'detalle_venta'


@receiver(post_save, sender=DetalleVenta)
def detalle_fac_guardar(sender,instance,**kwargs):
    venta_id = instance.factura.id
    produccion_id = instance.produccion.id
    
    enc = Venta.objects.get(pk=venta_id)
    if enc:
        sub_total = DetalleVenta.objects \
            .filter(factura=venta_id) \
            .aggregate(tota=Sum('total')) \
            .get('total',0.00)
        
        #descuento = DetalleVenta.objects \
        #    .filter(factura=venta_id) \
        #    .aggregate(descuento=Sum('descuento')) \
        #    .get('descuento',0.00)
        
        enc.sub_total = sub_total
        #enc.descuento = descuento
        enc.save()

    prod=Produccion.objects.filter(pk=produccion_id).first()
    if prod:
        cantidad = int(prod.existencia) - int(instance.cantidad)
        prod.existencia = cantidad
        prod.save()

