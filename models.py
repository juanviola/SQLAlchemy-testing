import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.dialects import mysql
import datetime

Base = declarative_base()

# class Person(Base):
class Vendor(Base):
    __tablename__ = 'Vendors'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    ilo_user = Column(String(250), nullable=False)
    ilo_pass = Column(String(250), nullable=False)

class Machine(Base):
    __tablename__ = 'Machines'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    status = Column(mysql.ENUM('NEW','OS'))
    mac1 = Column(String(255))
    mac2 = Column(String(255))
    ilo_ip = Column(String(255))
    ip = Column(String(255))
    createdAt = Column(mysql.DATETIME, default=datetime.datetime.now)
    updatedAt = Column(mysql.DATETIME, default=datetime.datetime.now)
    ScopeId = Column(Integer)
    VendorId = Column(Integer)

class Demo(Base):
    __tablename__ = 'Demos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('mysql+mysqldb://root:okok123@127.0.0.1:3306/test')


# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
