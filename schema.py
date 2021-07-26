from datetime import datetime
from pydantic import BaseModel

from typing import ForwardRef, List, Optional


from fastapi import Form

class EmployeeBase(BaseModel):
    id: int
    nombres: str
    apellidos: str
    dni: str
    genero: str
    celular: str
    email: Optional[str]
    direccion: str
    fecha_nacimiento: datetime
    id_user: int
    # user: List[UserBase] = []

class EmployeeUpdate(BaseModel):
    nombres: Optional[str]
    apellidos: Optional[str]
    dni: Optional[str]
    genero: Optional[str]
    celular: Optional[str]
    email: Optional[str]
    direccion: Optional[str]
    fecha_nacimiento: Optional[datetime]

class EmployeeCreate(BaseModel):
    nombres: str
    apellidos: str
    dni: str
    genero: str
    celular: str
    email: str
    direccion: str
    fecha_nacimiento: datetime
    # user: List[UserCreate] = []


class ClientBase(BaseModel):
    id: int
    nombres: str
    apellidos: str
    dni: str
    genero: str
    celular: str
    direccion: str
    fecha_nacimiento: datetime
    user_id: int
    # user: List[UserBase] = []


class ClientCreate(BaseModel):
    nombres: str
    apellidos: str
    dni: str
    genero: str
    celular: str
    direccion: str
    fecha_nacimiento: datetime
    # user: List[UserCreate] = []





class UserBase(BaseModel):
    id: int
    nombre: str
    estado: bool
    # id_empleado: List[EmployeeBase] = []
    # id_cliente: List[ClientBase] = []

## AUX
class UserCreate(BaseModel):
    nombre: str
    clave: str
    estado: bool
    tipo: str
    nombres: str
    apellidos: str
    dni: str
    genero: str
    celular: str
    direccion: str
    fecha_nacimiento: datetime
class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True


class Employee(EmployeeBase):
    id: int
    
    class Config:
        orm_mode = True


class Client(ClientBase):
    id: int
    
    class Config:
        orm_mode = True





## Product Scheme

class ProductBase(BaseModel):
    estado: bool
    nombre: str
    precio: float
    stock: int
    image: str
    description: str


class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    
    class Config:
        orm_mode = True


##

## Auxiliar BaseScheme

class Login(BaseModel):
    usuario: str
    clave: str

class AltUser(BaseModel):
    id_cliente: int

class AltProduct(BaseModel):
    id_producto: int

class AltDetalleVenta(BaseModel):
    cantidad: int
    sub_total: float
    id_product: int

class SaleCreate(BaseModel):
    fecha: datetime
    id_cliente: int
    id_empleado: Optional[int]
    estado: str
    monto_total: float
    detalle_venta: List[AltDetalleVenta]


class SaleBase(BaseModel):
    fecha: datetime
    id_cliente: int
    id_empleado: int
    estado: str
    monto_total: float
    detalleventa: List[AltDetalleVenta]

class Sale(SaleBase):
    id: int
    class Config:
        orm_mode = True

class SaleUpdate(BaseModel):
    estado: str
    id_empleado: Optional[int]
