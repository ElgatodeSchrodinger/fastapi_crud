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
    user_id: int
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
    user_id: int
    # user: List[UserCreate] = []


class UserBase(BaseModel):
    id: int
    email: str
    is_active: bool
    employee: List[EmployeeBase] = []
    client: List[ClientBase] = []

class UserCreate(BaseModel):
    email: str
    hashed_password: str
    is_active: bool
    employee: List[EmployeeCreate] = []
    client: List[ClientCreate] = []


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