from django.db import models
#Para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from baseapp.models import BaseFields
from mnt.models import Cliente, Cosecha, Produccion, Cultivo, Parametro

## Venta ******************************************** ##
# - Venta - #
class Venta(BaseFields):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    fechaVenta = models.DateTimeField(auto_now_add=True)
    subTotal = models.FloatField(blank=True, null=True, default=0)
    totalVenta = models.FloatField(blank=True, null=True, default=0)
    porcIva    = models.FloatField(blank=True, null=True)
    totalIva = models.FloatField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.id)

    def save (self):
        self.totalVenta = float(self.totalVenta)
        self.procIva = float(self.porcIva)
        self.subTotal = float(self.subtotal)
        self.totalIva = self.totalIva
        super(Venta,self).save() 
       
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
        return "{}".format(self.cultivo.nombre)

    def save (self):
        self.total = float(float(int(self.cantidad)) * float(self.precio))
        super(DetalleVenta, self).save()


    class Meta:
        verbose_name_plural = "DetalleVentas"
        db_table = 'detalle_venta'


@receiver(post_save, sender=DetalleVenta)
def detalle_fac_guardar(sender,instance,**kwargs):
    venta_id = instance.factura.id
    produccion_id = instance.produccion.id
    porciva = Parametro.objects.filter(nombreParametro='IVA')
    venta = Venta.objects.get(pk=venta_id)
    if venta:
        sub_total = DetalleVenta.objects \
            .filter(factura=venta_id) \
            .aggregate(total=Sum('total')) \
            .get('total',0.00)
        
        totaliva = sub_total * (porciva /100)
        totalventa = sub_total + totaliva
        venta.totalVenta = totalventa
        venta.subTotal  = sub_total
        venta.totalIva = totaliva
        venta.porcIva = porciva
        venta.save()

    prod=Produccion.objects.filter(pk=produccion_id).first()
    if prod:
        cantidad = int(prod.cantidadVentaCosecha) + int(instance.cantidad)
        prod.cantidadVentaCosecha = cantidad
        prod.save()

