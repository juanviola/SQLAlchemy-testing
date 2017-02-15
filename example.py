#!/usr/bin/python

from sqlalchemy import *
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

db = create_engine('mysql+mysqldb://root:okok123@127.0.0.1:3306/racktables_dev')

db.echo = True
metadata = MetaData(db)

class Object(Base):
    __tablename__ = 'Object'

    id              = Column(Integer, primary_key=True)
    name            = Column(String(255))
    label           = Column(String(255))
    objtype_id      = Column(Integer)
    asset_no        = Column(String(64))
    has_problems    = Column(Enum('yes','no'))
    comment         = Column(Text)

    children        = relationship("AttributeValue")

class AttributeValue(Base):
    __tablename__ = 'AttributeValue'

    object_id       = Column(Integer, primary_key=True)
    object_tid      = Column(Integer)
    attr_id         = Column(Integer)
    string_value    = Column(Text)
    uint_value      = Column(Integer)
    float_value     = Column(Float)

    # children        = relationship("AttributeValue")


# objects = Table('Object', metadata, autoload=True)

def run(stmt):
    rs = stmt.execute()
    for row in rs:
        print row

# Most WHERE clauses can be constructed via normal comparisons
#s = objects.select(objects.c.name.like("%DC4%"))

s = Object.query.join(Object.name, aliased=True)\
                    .filter_by(objtype_id=4)

run(s)
