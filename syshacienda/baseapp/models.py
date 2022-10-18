from django.db import models
from django.contrib.auth.models import User

class BaseFields(models.Model):
    estado = models.BooleanField(default=True, verbose_name="Estado del registro")
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    fechaModificacion = models.DateTimeField(auto_now = True, verbose_name="Fecha de actualizacion", blank=True, null=True)
    usuarioCreacion = models.ForeignKey(User, on_delete = models.DO_NOTHING, verbose_name="Usuario registra")
    usuarioModificacion = models.IntegerField(blank=True, null=True, verbose_name = "Usuario modifica")

    class Meta:
        abstract = True

class ContactFields(models.Model):
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name = "Telefono de contacto")
    celular = models.CharField(max_length=10, blank=True, null=True, verbose_name = "Número celular")
    correo = models.CharField(max_length=50, blank=True, null=True, verbose_name = "Correo electrónico")
    direccion = models.CharField(max_length=100, verbose_name="Direccion")
    ciudad = models.CharField(max_length=20, blank=True, null=True, verbose_name= "Ciudad")

    class Meta:
        abstract = True

class PersonFields(models.Model):
    nombres = models.CharField(max_length=25, verbose_name="Nombre")
    apellidos = models.CharField(max_length=25, verbose_name="Apellido")
    identificacion = models.CharField(max_length=15, unique=True, verbose_name = "Número de identificación")
    
    class Meta:
        abstract = True
