/*
pryuae: syshacienda
create database syshacienda;

use syshacienda;

drop table roles;
drop table usuario; 
drop table cultivo; 
drop table produccion; 
drop table cosecha;
drop table insumo;
drop table actividad;
drop table proveedor;
drop table hacienda;
drop table descripcion_lote;
drop table registro_inusmo;
drop table empleado;
drop table asignacion;
drop table cliente;
drop table venta;
drop table detalle_venta;
drop table asignacion_material;
drop table dato_empleado;
*/


create table roles
(idRol serial primary key,
nombre varchar(50) not null unique,
estado varchar(8) not null
);


create table usuario 
(idUsuario serial primary key,
nombre	varchar(50) not null,
apellido varchar(50) not null,
usuario varchar(50) not null,
estado varchar(8) not null
);

create table cultivo 
(idCultivo serial primary key,
nombre	varchar(50) not null,
lote varchar(50) not null,
fechaInicio date not null,
fechaFin date null,
estado varchar(8) not null
);

create table produccion 
(idProduccion serial primary key,
idCultivo int not null,
idInsumo int not null,
fecha	date not null,
CantCosecha int null,
estado varchar(8) not null
);

create table cosecha 
(idCosecha serial primary key,
idHacienda int not null,
idCultivo int not null,
fecha	date not null,
Cantidad float null,
estado varchar(8) not null
);

create table insumo
(idInsumo serial primary key,
nombre varchar(50) not null,
tipo varchar(50) not null,
uso varchar(50) not null,
Precio money null,
estado varchar(8) not null
);

create table actividad
(idActividad serial primary key,
idcultivo int not null,
nombre varchar(50) not null,
fecha date not null,
estado varchar(8) not null
);

create table proveedor
(idProveedor serial primary key,
nombre varchar(50) not null,
ruc varchar(15) not null,
direccion varchar(100) null,
descripcion varchar(100) null,
ciudad varchar(20) null,
estado varchar(8) not null
);

create table hacienda
(idHacienda serial primary key,
nombre varchar(50) not null,
direccion varchar(100) null,
ruc varchar(15) not null,
telefono varchar(20) null,
correo varchar(20) null,
ciudad varchar(20) null,
estado varchar(8) not null
);

create table descripcion_lote
(idDescripcion_lote serial primary key,
idCultivo int not null,
Area float null,
idProduccion int not null,
Etapa varchar(50) null,
estado varchar(8) not null
);

create table registro_insumo
(--id serial primary key,
fechaCompra date not null,
precio money not null,
fechaIngreso date not null,
fechaExpira date not null,
requerimiento varchar(100) null,
insumo int not null,
cultivo int not null,
estado varchar(8) not null
);

create table empleado
(idEmpleado serial primary key,
nombres varchar(25) not null,
apellidos varchar(25) not null,
cedula varchar(15) not null,
celular varchar(10) null,
correo varchar(25) null,
fchNacimiento date not null,
direccion varchar(100)  not null,
estado varchar(8) not null
);

create table asignacion
(idasignacion serial primary key,
idactividad int not null,
idempleado int not null,
idcultivo int not null,
descripcion varchar(50) null,
fecha date not null,
estado varchar(8) not null
);

create table cliente
(idCliente serial primary key,
nombres varchar(25) not null,
apellidos varchar(25) not null,
cedula varchar(15) not null,
celular varchar(10) null,
correo varchar(25) null,
direccion varchar(100)  not null,
ciudad varchar(20) null,
estado varchar(8) not null
);

create table venta
(idVenta serial primary key,
idCultivo int not null,
idProduccion int not null,
Cantidad float not null,
Precio money not null,
Fecha date not null,
estado varchar(8) not null
);

create table detalle_venta
(idDetalle_venta serial primary key,
idVenta int not null,
fecha_venta date null,
idCliente int not null,
CantidadVenta float,
estado varchar(8) not null
);

create table asignacion_material
(idMaterial serial primary key,
idInsumo int not null,
idCultivo int not null,
encargado varchar(50) not null,
Fecha date not null,
estado varchar(8) not null
);

create table dato_empleado
(idRegistro serial primary key,
idHacienda int not null,
idEmpleado int not null,
contrato varchar(100) not null,
cargo varchar(30) null,
estado varchar(8) not null
);
