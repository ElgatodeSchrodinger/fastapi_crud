from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base, engine







# class Producto(Base):
#     __tablename__ = "producto"

#     id = Column(Integer, primary_key=True, index=True)
#     estado = Column(Boolean, default=True)
#     nombre = Column(String)
#     precio = Column(Float)
#     stock = Column(Integer)
#     detalleventa = relationship("DetalleVenta", back_populates="id_venta")

# class DetalleVenta(Base):
#     __tablename__ = "detalleventa"

#     id = Column(Integer, primary_key=True, index=True)
#     cantidad = Column(Integer)
#     sub_total = Column(Float)
#     id_product = Column(Integer, ForeignKey('producto.id'))
#     id_venta = Column(Integer, ForeignKey('venta.id'))


# class Venta(Base):
#     __tablename__ = "venta"

#     id = Column(Integer, primary_key=True, index=True)
#     estado = Column(Boolean, default=True)
#     fecha = Column(DateTime)
#     monto_total = Column(Float)
#     id_cliente = Column(Integer, ForeignKey('client.id'))
#     id_empleado = Column(Integer, ForeignKey('employee.id'))
#     detalleventa = relationship("DetalleVenta", back_populates="id_venta")



class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    clave = Column(String)
    estado = Column(Boolean, default=True)
    # id_client = Column(Integer, ForeignKey('client.id'))
    # id_employee = Column(Integer, ForeignKey('employee.id'))
    # employee = relationship("Employee", back_populates="user")
    # client = relationship("Client", back_populates="user")
    id_empleado = Column(Integer, ForeignKey('employee.id'), nullable=True)
    empleado = relationship("Employee", back_populates="user")
    id_cliente = Column(Integer, ForeignKey('client.id'), nullable=True)
    cliente = relationship("Client", back_populates="user")

class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String)
    apellidos = Column(String)
    dni = Column(String)
    genero = Column(String)
    celular = Column(String)
    direccion = Column(String)
    fecha_nacimiento = Column(DateTime)
    user = relationship("User", back_populates="empleado", uselist=False)
    # venta = relationship("Venta", back_populates="id_cliente")

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
    user = relationship("User", back_populates="cliente", uselist=False)
    # venta = relationship("Venta", back_populates="id_cliente")

