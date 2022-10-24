from django.urls import path, include
from mnt.views import *

urlpatterns = [
    #Cultivos
    path('Cultivos/', CultivoView.as_view(template_name='mnt/cultivo_list.html'), name='cultivo_list'),
    path('Cultivo/new', CultivoNew.as_view(template_name='mnt/cultivo_form.html'), name='cultivo_new'),
    path('Cultivo/edit/<int:pk>', CultivoEdit.as_view(template_name='mnt/cultivo_form.html'), name='cultivo_edit'),
    #Insumos
    path('Insumos/', InsumoView.as_view(template_name='mnt/insumo_list.html'), name='insumo_list'),
    path('Insumo/new', InsumoNew.as_view(template_name='mnt/insumo_form.html'), name='insumo_new'),
    path('Insumo/edit/<int:pk>', InsumoEdit.as_view(template_name='mnt/insumo_form.html'), name='insumo_edit'),

    #Hacienda
    path('Haciendas/', HaciendaView.as_view(template_name='mnt/hacienda_list.html'), name='hacienda_list'),
    path('Hacienda/new', HaciendaNew.as_view(template_name='mnt/hacienda_form.html'), name='hacienda_new'),
    path('Hacienda/edit/<int:pk>', HaciendaEdit.as_view(template_name='mnt/hacienda_form.html'), name='hacienda_edit'),

    #Empleado
    path('Empleados/', EmpleadoView.as_view(template_name='mnt/empleado_list.html'), name='empleado_list'),
    path('Empleado/new', EmpleadoNew.as_view(template_name='mnt/empleado_form.html'), name='empleado_new'),
    path('Empleado/edit/<int:pk>', EmpleadoEdit.as_view(template_name='mnt/empleado_form.html'), name='empleado_edit'),

    #Proveedor
    path('Proveedores/', ProveedorView.as_view(template_name='mnt/proveedor_list.html'), name='proveedor_list'),
    path('Proveedor/new', ProveedorNew.as_view(template_name='mnt/proveedor_form.html'), name='proveedor_new'),
    path('Proveedor/edit/<int:pk>', ProveedorEdit.as_view(template_name='mnt/proveedor_form.html'), name='proveedor_edit'),

    #Cliente
    path('Clientes/', ClienteView.as_view(template_name='mnt/cliente_list.html'), name='cliente_list'),
    path('Cliente/new', ClienteNew.as_view(template_name='mnt/cliente_form.html'), name='cliente_new'),
    path('Cliente/edit/<int:pk>', ClienteEdit.as_view(template_name='mnt/cliente_form.html'), name='cliente_edit'),

    #Actividad
    path('Actividades/', ActividadView.as_view(template_name='mnt/actividad_list.html'), name='actividad_list'),
    path('Actividad/new', ActividadNew.as_view(template_name='mnt/actividad_form.html'), name='actividad_new'),
    path('Actividad/edit/<int:pk>', ActividadEdit.as_view(template_name='mnt/actividad_form.html'), name='actividad_edit'),
	path('Actividad/del/<int:pk>', ActividadDel.as_view(template_name='mnt/actividad_form.html'), name='actividad_del'),

    #Asignacion
    path('Asignaciones/', AsignacionView.as_view(template_name='mnt/asignacion_list.html'), name='asignacion_list'),
    path('Asignacion/new', AsignacionNew.as_view(template_name='mnt/asignacion_form.html'), name='asignacion_new'),
    path('Asignacion/edit/<int:pk>', AsignacionEdit.as_view(template_name='mnt/asignacion_form.html'), name='asignacion_edit'),

    #AsignacionMaterial
    path('AsignacionMateriales/', AsignacionMaterialView.as_view(template_name='mnt/asignacionmaterial_list.html'), name='asignacionmaterial_list'),
    path('AsignacionMaterial/new', AsignacionMaterialNew.as_view(template_name='mnt/asignacionmaterial_form.html'), name='asignacionmaterial_new'),
    path('AsignacionMaterial/edit/<int:pk>', AsignacionMaterialEdit.as_view(template_name='mnt/asignacionmaterial_form.html'), name='asignacionmaterial_edit'),

    #Cosecha
    path('Cosechas/', CosechaView.as_view(template_name='mnt/cosecha_list.html'), name='cosecha_list'),
    path('Cosecha/new', CosechaNew.as_view(template_name='mnt/cosecha_form.html'), name='cosecha_new'),
    path('Cosecha/edit/<int:pk>', CosechaEdit.as_view(template_name='mnt/cosecha_form.html'), name='cosecha_edit'),

    #RegistroEmpleado
    path('RegistroEmpleados/', RegistroEmpleadoView.as_view(template_name='mnt/registroempleado_list.html'), name='registroempleado_list'),
    path('RegistroEmpleado/new', RegistroEmpleadoNew.as_view(template_name='mnt/registroempleado_form.html'), name='registroempleado_new'),
    path('RegistroEmpleado/edit/<int:pk>', RegistroEmpleadoEdit.as_view(template_name='mnt/registroempleado_form.html'), name='registroempleado_edit'),

    #Produccion
    path('Produccion/', ProduccionView.as_view(template_name='mnt/produccion_list.html'), name='produccion_list'),
    path('Produccion/new', ProduccionNew.as_view(template_name='mnt/produccion_form.html'), name='produccion_new'),
    path('Produccion/edit/<int:pk>', ProduccionEdit.as_view(template_name='mnt/produccion_form.html'), name='produccion_edit'),

    #DescripcionLote
    path('DescripcionLotes/', DescripcionLoteView.as_view(template_name='mnt/descripcionlote_list.html'), name='descripcionlote_list'),
    path('DescripcionLote/new', DescripcionLoteNew.as_view(template_name='mnt/descripcionlote_form.html'), name='descripcionlote_new'),
    path('DescripcionLote/edit/<int:pk>', DescripcionLoteEdit.as_view(template_name='mnt/descripcionlote_form.html'), name='descripcionlote_edit'),

    #RegistroInsumo
    path('RegistroInsumos/', RegistroInsumoView.as_view(template_name='mnt/registroinsumo_list.html'), name='registroinsumo_list'),
    path('RegistroInsumo/new', RegistroInsumoNew.as_view(template_name='mnt/registroinsumo_form.html'), name='registroinsumo_new'),
    path('RegistroInsumo/edit/<int:pk>', RegistroInsumoEdit.as_view(template_name='mnt/registroinsumo_form.html'), name='registroinsumo_edit'),

]
