#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Vendor, Base, Machine

engine = create_engine('mysql+mysqldb://root:okok123@127.0.0.1:3306/test')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Insert a Person in the person table
# new_person = Person(name='new person')
# session.add(new_person)
# session.commit()

new_machine = Machine(name='My Super')
session.add(new_machine)
session.commit()

# # Insert an Address in the address table
# new_address = Address(post_code='00000', person=new_person)
# session.add(new_address)
# session.commit()
