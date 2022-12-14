
from django.db import models


class Actividad(models.Model):
    idactividad = models.AutoField(primary_key=True)
    idcultivo = models.IntegerField()
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'actividad'


class Asignacion(models.Model):
    idempleado = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    cedula = models.CharField(max_length=15)
    celular = models.CharField(max_length=10, blank=True, null=True)
    correo = models.CharField(max_length=25, blank=True, null=True)
    fchnacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'asignacion'


class AsignacionMaterial(models.Model):
    idmaterial = models.AutoField(primary_key=True)
    idinsumo = models.IntegerField()
    idcultivo = models.IntegerField()
    encargado = models.CharField(max_length=50)
    fecha = models.DateField()
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'asignacion_material'


class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    cedula = models.CharField(max_length=15)
    celular = models.CharField(max_length=10, blank=True, null=True)
    correo = models.CharField(max_length=25, blank=True, null=True)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'cliente'

class Cosecha(models.Model):
    idcosecha = models.AutoField(primary_key=True)
    idhacienda = models.IntegerField()
    idcultivo = models.IntegerField()
    fecha = models.DateField()
    cantidad = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'cosecha'


class Cultivo(models.Model):
    idcultivo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    lote = models.CharField(max_length=50)
    fechainicio = models.DateField()
    fechafin = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'cultivo'


class DatoEmpleado(models.Model):
    idregistro = models.AutoField(primary_key=True)
    idhacienda = models.IntegerField()
    idempleado = models.IntegerField()
    contrato = models.CharField(max_length=100)
    cargo = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'dato_empleado'


class DescripcionLote(models.Model):
    iddescripcion_lote = models.AutoField(primary_key=True)
    idcultivo = models.IntegerField()
    area = models.FloatField(blank=True, null=True)
    idproduccion = models.IntegerField()
    etapa = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'descripcion_lote'


class DetalleVenta(models.Model):
    iddetalle_venta = models.AutoField(primary_key=True)
    idventa = models.IntegerField()
    fecha_venta = models.DateField(blank=True, null=True)
    idcliente = models.IntegerField()
    cantidadventa = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'detalle_venta'

class Empleado(models.Model):
    idempleado = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    cedula = models.CharField(max_length=15)
    celular = models.CharField(max_length=10, blank=True, null=True)
    correo = models.CharField(max_length=25, blank=True, null=True)
    fchnacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'empleado'


class Hacienda(models.Model):
    idhacienda = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    ruc = models.CharField(max_length=15)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.CharField(max_length=20, blank=True, null=True)
    ciudad = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'hacienda'


class Insumo(models.Model):
    idinsumo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    uso = models.CharField(max_length=50)
    precio = models.TextField(blank=True, null=True) 
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'insumo'


class Produccion(models.Model):
    idproduccion = models.AutoField(primary_key=True)
    idcultivo = models.IntegerField()
    idinsumo = models.IntegerField()
    fecha = models.DateField()
    cantcosecha = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'produccion'


class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ruc = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    ciudad = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'proveedor'


class RegistroInsumo(models.Model):
    idregistro_insumo = models.AutoField(primary_key=True)
    fechacompra = models.DateField()
    precio = models.TextField() 
    fechaingreso = models.DateField()
    fechaexpira = models.DateField()
    requerimiento = models.CharField(max_length=100, blank=True, null=True)
    idinsumo = models.IntegerField()
    idcultivo = models.IntegerField()
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'registro_inusmo'


class Roles(models.Model):
    idrol = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'roles'


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'usuario'


class Venta(models.Model):
    idventa = models.AutoField(primary_key=True)
    idcultivo = models.IntegerField()
    idproduccion = models.IntegerField()
    cantidad = models.FloatField()
    precio = models.TextField()  
    fecha = models.DateField()
    estado = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'venta'
