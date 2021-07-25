from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base, engine



class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    # id_client = Column(Integer, ForeignKey('client.id'))
    # id_employee = Column(Integer, ForeignKey('employee.id'))
    # employee = relationship("Employee", back_populates="user")
    # client = relationship("Client", back_populates="user")
    employee = relationship("Employee", backref="user", lazy="joined")
    client = relationship("Client", backref="user", lazy="joined")

class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    lastname = Column(String)
    dni = Column(String)
    gender = Column(String)
    phone = Column(String)
    address = Column(String)
    birthday = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    # user = relationship("User", back_populates="employee", lazy="joined")


class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    lastname = Column(String)
    dni = Column(String)
    gender = Column(String)
    phone = Column(String)
    address = Column(String)
    birthday = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    # user = relationship("User", back_populates="client", lazy="joined")


Base.metadata.create_all(bind=engine)