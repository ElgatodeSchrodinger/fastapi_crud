from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base, engine
# from sqlalchemy_utils import URLType


class Producto(Base):
    __tablename__ = "producto"

    id = Column(Integer, primary_key=True, index=True)
    estado = Column(Boolean, default=True)
    nombre = Column(String)
    precio = Column(Float)
    stock = Column(Integer)
    image = Column(String, nullable=True)
    # detalleventa = relationship("DetalleVenta", back_populates="product")

class DetalleVenta(Base):
    __tablename__ = "detalleventa"

    id = Column(Integer, primary_key=True, index=True)
    cantidad = Column(Integer)
    sub_total = Column(Float)
    id_product = Column(Integer, ForeignKey('producto.id'))
    product = relationship("Producto") #, back_populates="detalleventa")
    id_venta = Column(Integer, ForeignKey('venta.id'))
    venta = relationship("Venta", back_populates="detalleventa")


class Venta(Base):
    __tablename__ = "venta"

    id = Column(Integer, primary_key=True, index=True)
    estado = Column(String, default=True)
    fecha = Column(DateTime)
    monto_total = Column(Float)
    id_cliente = Column(Integer, ForeignKey('client.id'))
    cliente = relationship("Client")
    id_empleado = Column(Integer, ForeignKey('employee.id'))
    empleado = relationship("Employee")

    detalleventa = relationship("DetalleVenta", back_populates="venta")



class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    clave = Column(String)
    estado = Column(Boolean, default=True)
    empleado = relationship("Employee", back_populates="user", uselist=False)
    cliente = relationship("Client", back_populates="user", uselist=False)

class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String)
    apellidos = Column(String)
    dni = Column(String)
    genero = Column(String)
    celular = Column(String)
    email = Column(String)
    direccion = Column(String)
    fecha_nacimiento = Column(DateTime)
    user = relationship("User", back_populates="empleado")
    id_user = Column(Integer, ForeignKey('user.id'))
    # venta = relationship("Venta", back_populates="empleado")

class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String)
    apellidos = Column(String)
    dni = Column(String)
    genero = Column(String)
    celular = Column(String)
    direccion = Column(String)
    fecha_nacimiento = Column(DateTime)
    user = relationship("User", back_populates="cliente")
    id_user = Column(Integer, ForeignKey('user.id'))
    # venta = relationship("Venta", back_populates="cliente")

