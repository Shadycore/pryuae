from django.db import models


class baseFields(models.Model):
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    fechaModificacion = models.DateTimeField(auto_now = True, verbose_name="Fecha de Actualizacion")

    class Meta:
        abstract = True

class Actividad(baseFields):
    idactividad = models.AutoField(primary_key=True)
    idcultivo = models.IntegerField()
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    estado = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre

    def save (self):
        pass

    class Meta:
        verbose_name_plural = "Actividades"
        db_table = 'actividad'


class Asignacion(baseFields):
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


class AsignacionMaterial(baseFields):
    idmaterial = models.AutoField(primary_key=True)
    idinsumo = models.IntegerField()
    idcultivo = models.IntegerField()
    encargado = models.CharField(max_length=50)
    fecha = models.DateField()
    estado = models.CharField(max_length=8)
    
    def __str__(self):
        return self.fecha

    def save (self):
        pass
    class Meta:
        verbose_name_plural = "AsignacionMateriales"
        db_table = 'asignacion_material'


class Cliente(baseFields):
    idcliente = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    cedula = models.CharField(max_length=15)
    celular = models.CharField(max_length=10, blank=True, null=True)
    correo = models.CharField(max_length=25, blank=True, null=True)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=8)
    
    def __str__(self):
        return self.nombres

    def save (self):
        pass
    class Meta:
        verbose_name_plural = "Clientes"
        db_table = 'cliente'

class Cosecha(baseFields):
    idcosecha = models.AutoField(primary_key=True)
    idhacienda = models.IntegerField()
    idcultivo = models.IntegerField()
    fecha = models.DateField()
    cantidad = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=8)

    def __str__(self):
        return self.fecha

    def save (self):
        pass
    class Meta:
        verbose_name_plural = "Cosechas"
        db_table = 'cosecha'


class Cultivo(baseFields):
    idcultivo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    lote = models.CharField(max_length=50)
    fechainicio = models.DateField()
    fechafin = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre

    def save (self):
        pass
    class Meta:
        verbose_name_plural = "Cultivos"
        db_table = 'cultivo'

class DatoEmpleado(baseFields):
    idregistro = models.AutoField(primary_key=True)
    idhacienda = models.IntegerField()
    idempleado = models.IntegerField()
    contrato = models.CharField(max_length=100)
    cargo = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=8)

    def __str__(self):
        return self.cargo

    def save (self):
        pass

    class Meta:
        verbose_name_plural = "DatosEmpleados"
        db_table = 'dato_empleado'


class DescripcionLote(baseFields):
    iddescripcion_lote = models.AutoField(primary_key=True)
    idcultivo = models.IntegerField()
    area = models.FloatField(blank=True, null=True)
    idproduccion = models.IntegerField()
    etapa = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=8)

    def __str__(self):
        return self.etapa

    def save (self):
        pass

    class Meta:
        verbose_name_plural = "DescripcionLotes"
        db_table = 'descripcion_lote'


class DetalleVenta(baseFields):
    iddetalle_venta = models.AutoField(primary_key=True)
    idventa = models.IntegerField()
    fecha_venta = models.DateField(blank=True, null=True)
    idcliente = models.IntegerField()
    cantidadventa = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=8)

    def __str__(self):
        return self.cantidadventa

    def save (self):
        pass 

    class Meta:
        verbose_name_plural = "DetalleVentas"
        db_table = 'detalle_venta'

class Empleado(baseFields):
    idempleado = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    cedula = models.CharField(max_length=15)
    celular = models.CharField(max_length=10, blank=True, null=True)
    correo = models.CharField(max_length=25, blank=True, null=True)
    fchnacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    estado = models.CharField(max_length=8)

    def __str__(self):
        return self.nombres

    def save (self):
        pass
       
    class Meta:
        verbose_name_plural = "Empleados"
        db_table = 'empleado'


class Hacienda(baseFields):
    idhacienda = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    ruc = models.CharField(max_length=15)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.CharField(max_length=20, blank=True, null=True)
    ciudad = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre

    def save (self):
        pass
       

    class Meta:
        verbose_name_plural = "Haciendas"
        db_table = 'hacienda'


class Insumo(baseFields):
    idinsumo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    uso = models.CharField(max_length=50)
    precio = models.TextField(blank=True, null=True) 
    estado = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre

    def save (self):
        pass
       

    class Meta:
        verbose_name_plural = "Insumos"
        db_table = 'insumo'


class Produccion(baseFields):
    idproduccion = models.AutoField(primary_key=True)
    idcultivo = models.IntegerField()
    idinsumo = models.IntegerField()
    fecha = models.DateField()
    cantcosecha = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=8)

    def __str__(self):
        return self.fecha

    def save (self):
        pass
       

    class Meta:
        verbose_name_plural = "Producciones"
        db_table = 'produccion'


class Proveedor(baseFields):
    idproveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ruc = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    ciudad = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre

    def save (self):
        pass
       
    class Meta:
        verbose_name_plural = "Proveedores"
        db_table = 'proveedor'


class RegistroInusmo(baseFields):
    idregistro_insumo = models.AutoField(primary_key=True)
    fechacompra = models.DateField()
    precio = models.TextField() 
    fechaingreso = models.DateField()
    fechaexpira = models.DateField()
    requerimiento = models.CharField(max_length=100, blank=True, null=True)
    idinsumo = models.IntegerField()
    idcultivo = models.IntegerField()
    estado = models.CharField(max_length=8)

    def __str__(self):
        return self.fechaingreso

    def save (self):
        pass
       

    class Meta:
        verbose_name_plural = "RegistroInsumos"
        db_table = 'registro_inusmo'


class Roles(baseFields):
    idrol = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    estado = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre

    def save (self):
        pass
       
    class Meta:
        verbose_name_plural = "Roles"
        db_table = 'roles'


class Usuario(baseFields):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    estado = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre

    def save (self):
        pass
       

    class Meta:
        verbose_name_plural = "Usuarios"
        db_table = 'usuario'


class Venta(baseFields):
    idventa = models.AutoField(primary_key=True)
    idcultivo = models.IntegerField()
    idproduccion = models.IntegerField()
    cantidad = models.FloatField()
    precio = models.TextField()  
    fecha = models.DateField()
    estado = models.CharField(max_length=8)

    def __str__(self):
        return self.cantidad

    def save (self):
        pass
       
  
    class Meta:
        verbose_name_plural = "Ventas"
        db_table = 'venta'
