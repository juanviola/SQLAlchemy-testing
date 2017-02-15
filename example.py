#!/usr/bin/python

from sqlalchemy import *
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

db = create_engine('mysql+mysqldb://root:okok123@127.0.0.1:3306/racktables_dev')

db.echo = True
metadata = MetaData(db)

objects = Table('Object', metadata, autoload=True)

def run(stmt):
    rs = stmt.execute()
    for row in rs:
        print row

# Most WHERE clauses can be constructed via normal comparisons
s = objects.select(objects.c.name.like("%DC4%"))

run(s)
