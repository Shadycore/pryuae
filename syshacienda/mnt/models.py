
from io import open_code
from unicodedata import name
from django.db import models
from baseapp.models import BaseFields
from baseapp.models import ContactFields
from baseapp.models import PersonFields


## tablas codigos principales ******************************************** ##
# - Cultivo - #
class Cultivo(BaseFields):
    #idCultivo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    lote = models.CharField(max_length=50)
    fechaInicio = models.DateField(blank=True, null=True)
    fechaFin = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{}:{}'.format(self.nombre, self.lote)

    def save(self):
        self.nombre = self.nombre.capitalize()
        self.lote = self.lote
        self.fechaInicio = self.fechaInicio
        self.fechaFin = self.fechaFin
        self.estado = self.estado
        super(Cultivo,self).save()

    class Meta:
        verbose_name_plural = "Cultivos"
        db_table = 'cultivo'

# - Insumo - #
class Insumo(BaseFields):
    #idInsumo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    uso = models.CharField(max_length=50)
    precio = models.FloatField(blank=True, null=True) 

    def __str__(self):
        return '{}:{}'.format(self.nombre, self.tipo)

    def save(self):
        self.nombre = self.nombre.capitalize()
        self.tipo = self.tipo
        self.uso = self.uso
        self.precio = self.precio
        self.estado = self.estado
        super(Insumo,self).save()

    class Meta:
        verbose_name_plural = "Insumos"
        db_table = 'insumo'

# - Hacienda - #
class Hacienda(BaseFields, PersonFields, ContactFields ):
    #idhacienda = models.AutoField(primary_key=True)

    def __str__(self):
         return '{}:{}'.format(self.identificacion, self.nombre)

    def save (self):
        self.nombre = self.nombre.capitalize()
        self.apellido = self.apellido.capitalize()
        self.telefono = self.telefono
        self.celular = self.celular
        self.email = self.email
        self.direccion = self.direccion
        self.ciudad = self.ciudad
        self.identificacion = self.identificacion
        self.estado = self.estado
        super(Hacienda,self).save()

    class Meta:
        verbose_name_plural = "Haciendas"
        db_table = 'hacienda'

## tablas entes ******************************************** ##
# - Empleado - #
class Empleado(BaseFields, PersonFields, ContactFields):
    #idEmpleado = models.AutoField(primary_key=True)
    fchNacimiento = models.DateField()

    def __str__(self):
        return "{} : {} {}".format(self.identificacion, self.nombre, self.apellido)

    def save (self):
        self.nombre = self.nombre.capitalize()
        self.apellido = self.apellido.capitalize()
        self.telefono = self.telefono
        self.celular = self.celular
        self.email = self.email
        self.direccion = self.direccion
        self.ciudad = self.ciudad
        self.fchNacimiento = self.fchNacimiento
        self.identificacion = self.identificacion
        self.estado = self.estado
        super(Empleado,self).save()
       
    class Meta:
        verbose_name_plural = "Empleados"
        db_table = 'empleado'
        


# - Proveedor - #
class Proveedor(BaseFields, PersonFields, ContactFields):
    #idProveedor = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "{} : {} ".format(self.identificacion ,self.nombre)

    def save (self):
        self.nombre = self.nombre.capitalize()
        self.apellido = self.apellido.capitalize()
        self.telefono = self.telefono
        self.celular = self.celular
        self.email = self.email
        self.direccion = self.direccion
        self.ciudad = self.ciudad
        self.descripcion = self.descripcion
        self.identificacion = self.identificacion
        self.estado = self.estado
        super(Proveedor,self).save()
    
    class Meta:
        verbose_name_plural = "Proveedores"
        db_table = 'proveedor'

# - Cliente - #
class Cliente(PersonFields, ContactFields, BaseFields):
    #idCliente = models.AutoField(primary_key=True)
    
    def __str__(self):
        return "{} : {} {} ".format(self.identificacion ,self.nombre, self.apellido)

    def save (self):
        self.nombre = self.nombre.capitalize()
        self.apellido = self.apellido.capitalize()
        self.telefono = self.telefono
        self.celular = self.celular
        self.email = self.email
        self.direccion = self.direccion
        self.ciudad = self.ciudad
        self.identificacion = self.identificacion
        #self.estado = self.estado
        super(Cliente,self).save()

    class Meta:
        verbose_name_plural = "Clientes"
        db_table = 'cliente'


## tablas codigos relacionados ******************************************** ##
# - Actividad - #
class Actividad(BaseFields):
    #idActividad = models.AutoField(primary_key=True)
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, null=True )
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        return'{}:{} {}'.format(self.id,self.cultivo.nombre, self.nombre)

    def save (self):
        self.nombre = self.nombre.capitalize()
        self.fecha = self.fecha
        self.estado = self.nombre
        super(Actividad,self).save()
    
    class Meta:
        verbose_name_plural = "Actividades"
        db_table = 'actividad'
        unique_together=('cultivo', 'nombre', 'fecha')

# - Asignacion - #
class Asignacion(BaseFields):
    #idAsignacion = models.AutoField(primary_key=True)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True)
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, null=True)
    descripcion = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        return "{}: {}".format(self.id, self.descripcion)

    def save (self):
        self.descripcion = self.descripcion.capitalize()
        self.fecha = self.fecha
        self.estado = self.estado
        super(Asignacion,self).save()

    class Meta:
        verbose_name_plural = "Asignaciones"
        db_table = 'asignacion'
        unique_together=('actividad', 'empleado', 'cultivo','descripcion')

# - AsignacionMaterial - #
class AsignacionMaterial(BaseFields):
    #idMaterial = models.AutoField(primary_key=True)
    insumo =  models.ForeignKey(Insumo, on_delete=models.CASCADE, null=True)
    cultivo =  models.ForeignKey(Cultivo, on_delete=models.CASCADE, null=True)
    encargado = models.CharField(max_length=50)
    fecha = models.DateField()
    
    def __str__(self):
        return "{}: {} {} {}".format(self.id, self.encargado, self.cultivo, self.insumo)

    def save (self):
        self.encargado = self.encargado.capitalize()
        self.fecha = self.fecha
        self.estado = self.estado
        super(AsignacionMaterial,self).save()

    class Meta:
        verbose_name_plural = "AsignacionMateriales"
        db_table = 'asignacion_material'
        unique_together=('insumo', 'cultivo', 'encargado')

# - Cosecha - #
class Cosecha(BaseFields):
    #idCosecha = models.AutoField(primary_key=True)
    hacienda =  models.ForeignKey(Hacienda, on_delete=models.CASCADE, null=True)
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, null=True)
    fecha = models.DateField()
    cantidad = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "{}: {} {}".format(self.id, self.hacienda, self.cultivo)

    def save (self):
        self.fecha = self.fecha
        self.cantidad = self.cantidad
        self.estado = self.estado
        super(Cosecha,self).save()

    class Meta:
        verbose_name_plural = "Cosechas"
        db_table = 'cosecha'
        unique_together=('hacienda', 'cultivo', 'fecha')

# - Registro Empleado - #
class RegistroEmpleado(BaseFields):
    #idRegistro = models.AutoField(primary_key=True)
    hacienda = models.ForeignKey(Hacienda, on_delete=models.CASCADE, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True)
    contrato = models.CharField(max_length=100)
    cargo = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return "{}: {} {} {}".format(self.id, self.hacienda, self.empleado, self.cargo)

    def save (self):
        self.contrato = self.contrato
        self.cargo = self.cargo
        self.estado = self.estado
        super(RegistroEmpleado,self).save()


    class Meta:
        verbose_name_plural = "RegistroEmpleados"
        db_table = 'registro_empleado'
        unique_together=('hacienda', 'empleado', 'cargo')

# - Produccion - #
class Produccion(BaseFields):
    #idProduccion = models.AutoField(primary_key=True)
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, null=True)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, null=True)
    fecha = models.DateField()
    cantidadCosecha = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{}: {} {} {}".format(self.id, self.cultivo, self.insumo, self.fecha)

    def save (self):
        self.fecha = self.fecha
        self.cantidadCosecha = self.cantidadCosecha
        self.estado = self.estado
        super(Produccion,self).save()

    class Meta:
        verbose_name_plural = "Producciones"
        db_table = 'produccion'
        unique_together=('cultivo', 'insumo', 'fecha', 'cantidadCosecha')

# - DescripcionLote - #
class DescripcionLote(BaseFields):
    #idDescripcionLote = models.AutoField(primary_key=True)
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, null=True)
    area = models.FloatField(blank=True, null=True)
    produccion = models.ForeignKey(Produccion, on_delete=models.CASCADE, null=True)
    etapa = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "{}: {} {} {}".format(self.id, self.cultivo, self.produccion, self.etapa)

    def save (self):
        self.area = self.area
        self.etapa = self.etapa
        self.estado = self.estado
        super(DescripcionLote,self).save()

    class Meta:
        verbose_name_plural = "DescripcionLotes"
        db_table = 'descripcion_lote'



# - RegistroInsumo - #
class RegistroInsumo(BaseFields):
    #idRegistroInsumo = models.AutoField(primary_key=True)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, null=True)
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, null=True)
    fechaCompra = models.DateField()
    precio = models.FloatField() 
    fechaIngreso = models.DateField()
    fechaExpira = models.DateField()
    requerimiento = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "{}: {} {} {}".format(self.id, self.insumo, self.cultivo, self.requerimiento)

    def save (self):
        self.insumo = self.insumo
        self.cultivo = self.cultivo
        self.fechaCompra = self.fechaCompra
        self.precio = self.precio
        self.fechaIngreso = self.fechaIngreso
        self.fechaExpira = self.fechaExpira
        self.requerimiento = self.requerimiento
        self.estado = self.estado
        super(RegistroInsumo,self).save()
       
    class Meta:
        verbose_name_plural = "RegistroInsumos"
        db_table = 'registro_insumo'

## Venta ******************************************** ##
# - Venta - #
class Venta(BaseFields):
    #idVenta = models.AutoField(primary_key=True)
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, null=True)
    Produccion = models.ForeignKey(Produccion, on_delete=models.CASCADE, null=True)
    cantidad = models.FloatField()
    precio = models.FloatField()  
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
    #idDetalleVenta = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    fechaVenta = models.DateField(blank=True, null=True)
    cantidadVenta = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.cantidadVenta

    def save (self):
        pass 

    class Meta:
        verbose_name_plural = "DetalleVentas"
        db_table = 'detalle_venta'
