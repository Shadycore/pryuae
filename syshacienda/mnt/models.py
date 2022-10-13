
from django.db import models
from baseapp.models import BaseFields
from baseapp.models import ContactFields
from baseapp.models import PersonFields


## tablas codigos principales ******************************************** ##
# - Cultivo - #
class Cultivo(BaseFields):
    idCultivo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    lote = models.CharField(max_length=50)
    fechaInicio = models.DateField(blank=True, null=True)
    fechaFin = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre = self.nombre.capitalize()
        self.lote = self.lote
        self.fechaInicio = self.fechaInicio
        self.fechaFin = self.fechaFin
        super(Cultivo,self).save()

    class Meta:
        verbose_name_plural = "Cultivos"
        db_table = 'cultivo'

# - Insumo - #
class Insumo(BaseFields):
    idInsumo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    uso = models.CharField(max_length=50)
    precio = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.nombre

    def save (self):
        pass

    class Meta:
        verbose_name_plural = "Insumos"
        db_table = 'insumo'

# - Hacienda - #
class Hacienda(BaseFields, PersonFields, ContactFields ):
    idhacienda = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nombre

    def save (self):
        pass

    class Meta:
        verbose_name_plural = "Haciendas"
        db_table = 'hacienda'

## tablas entes ******************************************** ##
# - Empleado - #
class Empleado(BaseFields, PersonFields, ContactFields):
    idEmpleado = models.AutoField(primary_key=True)
    fchNacimiento = models.DateField()

    def __str__(self):
        return self.nombres

    def save (self):
        pass
       
    class Meta:
        verbose_name_plural = "Empleados"
        db_table = 'empleado'
# - Proveedor - #
class Proveedor(BaseFields, PersonFields, ContactFields):
    idProveedor = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

    def save (self):
        pass
       
    class Meta:
        verbose_name_plural = "Proveedores"
        db_table = 'proveedor'

# - Cliente - #
class Cliente(PersonFields, ContactFields, BaseFields):
    idCliente = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.nombres

    def save (self):
        pass
    class Meta:
        verbose_name_plural = "Clientes"
        db_table = 'cliente'


## tablas codigos relacionados ******************************************** ##
# - Actividad - #
class Actividad(BaseFields):
    idActividad = models.AutoField(primary_key=True)
    idCultivo = models.IntegerField()
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        return self.nombre

    def save (self):
        pass

    class Meta:
        verbose_name_plural = "Actividades"
        db_table = 'actividad'

# - Asignacion - #
class Asignacion(BaseFields):
    idAsignacion = models.AutoField(primary_key=True)
    idActividad = models.IntegerField()
    idEmpleado = models.IntegerField()
    idCultivo = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        return self.nombre

    def save (self):
        pass
    class Meta:
        verbose_name_plural = "Asignaciones"
        db_table = 'asignacion'

# - AsignacionMaterial - #
class AsignacionMaterial(BaseFields):
    idMaterial = models.AutoField(primary_key=True)
    idInsumo = models.IntegerField()
    idCultivo = models.IntegerField()
    encargado = models.CharField(max_length=50)
    fecha = models.DateField()
    
    def __str__(self):
        return self.fecha

    def save (self):
        pass
    class Meta:
        verbose_name_plural = "AsignacionMateriales"
        db_table = 'asignacion_material'

# - Cosecha - #
class Cosecha(BaseFields):
    idCosecha = models.AutoField(primary_key=True)
    idHacienda = models.IntegerField()
    idCultivo = models.IntegerField()
    fecha = models.DateField()
    cantidad = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.fecha

    def save (self):
        pass
    class Meta:
        verbose_name_plural = "Cosechas"
        db_table = 'cosecha'

# - Registro Empleado - #
class RegistroEmpleado(BaseFields):
    idRegistro = models.AutoField(primary_key=True)
    idHacienda = models.IntegerField()
    idEmpleado = models.IntegerField()
    contrato = models.CharField(max_length=100)
    cargo = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.cargo

    def save (self):
        pass

    class Meta:
        verbose_name_plural = "RegistroEmpleados"
        db_table = 'registro_empleado'

# - DescripcionLote - #
class DescripcionLote(BaseFields):
    idDescripcionLote = models.AutoField(primary_key=True)
    idCultivo = models.IntegerField()
    area = models.FloatField(blank=True, null=True)
    idProduccion = models.IntegerField()
    etapa = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.etapa

    def save (self):
        pass

    class Meta:
        verbose_name_plural = "DescripcionLotes"
        db_table = 'descripcion_lote'

# - Produccion - #
class Produccion(BaseFields):
    idProduccion = models.AutoField(primary_key=True)
    idCultivo = models.IntegerField()
    idInsumo = models.IntegerField()
    fecha = models.DateField()
    cantidadCosecha = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.fecha

    def save (self):
        pass

    class Meta:
        verbose_name_plural = "Producciones"
        db_table = 'produccion'

# - RegistroInsumo - #
class RegistroInusmo(BaseFields):
    idRegistroInsumo = models.AutoField(primary_key=True)
    idInsumo = models.IntegerField()
    idCultivo = models.IntegerField()
    fechaCompra = models.DateField()
    precio = models.TextField() 
    fechaIngreso = models.DateField()
    fechaExpira = models.DateField()
    requerimiento = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.fechaingreso

    def save (self):
        pass
       
    class Meta:
        verbose_name_plural = "RegistroInsumos"
        db_table = 'registro_inusmo'

## Venta ******************************************** ##
# - Venta - #
class Venta(BaseFields):
    idVenta = models.AutoField(primary_key=True)
    idCultivo = models.IntegerField()
    idProduccion = models.IntegerField()
    cantidad = models.FloatField()
    precio = models.TextField()  
    fecha = models.DateField()

    def __str__(self):
        return self.cantidad

    def save (self):
        pass
       
  
    class Meta:
        verbose_name_plural = "Ventas"
        db_table = 'venta'

# - DetalleVenta - #
class DetalleVenta(BaseFields):
    idDetalleVenta = models.AutoField(primary_key=True)
    idVenta = models.IntegerField()
    idCliente = models.IntegerField()
    fechaVenta = models.DateField(blank=True, null=True)
    cantidadVenta = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.cantidadVenta

    def save (self):
        pass 

    class Meta:
        verbose_name_plural = "DetalleVentas"
        db_table = 'detalle_venta'

