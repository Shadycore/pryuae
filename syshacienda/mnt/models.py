
from django.db import models
from baseapp.models import BaseFields
from baseapp.models import ContactFields
from baseapp.models import PersonFields


class Actividad(BaseFields):
    idactividad = models.AutoField(primary_key=True)
    idcultivo = models.IntegerField()
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        return self.nombre

    def save (self):
        pass

    class Meta:
        verbose_name_plural = "Actividades"
        db_table = 'actividad'


class Asignacion(BaseFields):
    idasignacion = models.AutoField(primary_key=True)
    idactividad = models.IntegerField()
    idempleado = models.IntegerField()
    idcultivo = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        return self.nombre

    def save (self):
        pass
    class Meta:
        verbose_name_plural = "Asignaciones"
        db_table = 'asignacion'


class AsignacionMaterial(BaseFields):
    idmaterial = models.AutoField(primary_key=True)
    idinsumo = models.IntegerField()
    idcultivo = models.IntegerField()
    encargado = models.CharField(max_length=50)
    fecha = models.DateField()
    
    def __str__(self):
        return self.fecha

    def save (self):
        pass
    class Meta:
        verbose_name_plural = "AsignacionMateriales"
        db_table = 'asignacion_material'


class Cliente(PersonFields, ContactFields, BaseFields):
    idcliente = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.nombres

    def save (self):
        pass
    class Meta:
        verbose_name_plural = "Clientes"
        db_table = 'cliente'

class Cosecha(BaseFields):
    idcosecha = models.AutoField(primary_key=True)
    idhacienda = models.IntegerField()
    idcultivo = models.IntegerField()
    fecha = models.DateField()
    cantidad = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.fecha

    def save (self):
        pass
    class Meta:
        verbose_name_plural = "Cosechas"
        db_table = 'cosecha'


class Cultivo(BaseFields):
    idcultivo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    lote = models.CharField(max_length=50)
    fechainicio = models.DateField()
    fechafin = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    def save (self):
        pass
    class Meta:
        verbose_name_plural = "Cultivos"
        db_table = 'cultivo'

class RegistroEmpleado(BaseFields):
    idregistro = models.AutoField(primary_key=True)
    idhacienda = models.IntegerField()
    idempleado = models.IntegerField()
    contrato = models.CharField(max_length=100)
    cargo = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.cargo

    def save (self):
        pass

    class Meta:
        verbose_name_plural = "RegistroEmpleados"
        db_table = 'registro_empleado'


class DescripcionLote(BaseFields):
    iddescripcion_lote = models.AutoField(primary_key=True)
    idcultivo = models.IntegerField()
    area = models.FloatField(blank=True, null=True)
    idproduccion = models.IntegerField()
    etapa = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.etapa

    def save (self):
        pass

    class Meta:
        verbose_name_plural = "DescripcionLotes"
        db_table = 'descripcion_lote'


class DetalleVenta(BaseFields):
    iddetalle_venta = models.AutoField(primary_key=True)
    idventa = models.IntegerField()
    fecha_venta = models.DateField(blank=True, null=True)
    idcliente = models.IntegerField()
    cantidadventa = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.cantidadventa

    def save (self):
        pass 

    class Meta:
        verbose_name_plural = "DetalleVentas"
        db_table = 'detalle_venta'

class Empleado(BaseFields, PersonFields, ContactFields):
    idempleado = models.AutoField(primary_key=True)
    fchnacimiento = models.DateField()

    def __str__(self):
        return self.nombres

    def save (self):
        pass
       
    class Meta:
        verbose_name_plural = "Empleados"
        db_table = 'empleado'


class Hacienda(BaseFields, PersonFields, ContactFields ):
    idhacienda = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nombre

    def save (self):
        pass
       

    class Meta:
        verbose_name_plural = "Haciendas"
        db_table = 'hacienda'


class Insumo(BaseFields):
    idinsumo = models.AutoField(primary_key=True)
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


class Produccion(BaseFields):
    idproduccion = models.AutoField(primary_key=True)
    idcultivo = models.IntegerField()
    idinsumo = models.IntegerField()
    fecha = models.DateField()
    cantcosecha = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.fecha

    def save (self):
        pass
       

    class Meta:
        verbose_name_plural = "Producciones"
        db_table = 'produccion'


class Proveedor(BaseFields, PersonFields, ContactFields):
    idproveedor = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

    def save (self):
        pass
       
    class Meta:
        verbose_name_plural = "Proveedores"
        db_table = 'proveedor'


class RegistroInusmo(BaseFields):
    idregistro_insumo = models.AutoField(primary_key=True)
    fechacompra = models.DateField()
    precio = models.TextField() 
    fechaingreso = models.DateField()
    fechaexpira = models.DateField()
    requerimiento = models.CharField(max_length=100, blank=True, null=True)
    idinsumo = models.IntegerField()
    idcultivo = models.IntegerField()

    def __str__(self):
        return self.fechaingreso

    def save (self):
        pass
       
    class Meta:
        verbose_name_plural = "RegistroInsumos"
        db_table = 'registro_inusmo'

class Venta(BaseFields):
    idventa = models.AutoField(primary_key=True)
    idcultivo = models.IntegerField()
    idproduccion = models.IntegerField()
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

