from datetime import datetime
from pydantic import BaseModel

from typing import ForwardRef, List, Optional


class EmployeeBase(BaseModel):
    id: int
    name: str
    lastname: str
    dni: str
    gender: str
    phone: str
    address: str
    birthday: datetime
    user_id: int
    # user: List[UserBase] = []

class EmployeeCreate(BaseModel):
    name: str
    lastname: str
    dni: str
    gender: str
    phone: str
    address: str
    birthday: datetime
    # user: List[UserCreate] = []


class ClientBase(BaseModel):
    id: int
    name: str
    lastname: str
    dni: str
    gender: str
    phone: str
    address: str
    birthday: datetime
    user_id: int
    # user: List[UserBase] = []


class ClientCreate(BaseModel):
    name: str
    lastname: str
    dni: str
    gender: str
    phone: str
    address: str
    birthday: datetime
    # user: List[UserCreate] = []


class UserBase(BaseModel):
    id: int
    nombre: str
    estado: bool
    id_empleado: List[EmployeeBase] = []
    id_cliente: List[ClientBase] = []

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




## Auxiliar BaseScheme

class Login(BaseModel):
    usuario: str
    clave: str
