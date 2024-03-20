#!/usr/bin/env python3

# Script goes here!

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

if 'session' not in locals():
    session = DBSession()

# creating an instance of freebie
freebie1 = Freebie(item_name="keyboard", value=10)
freebie2 = Freebie(item_name="mouse", value=20)

company = session.query(Company).filter_by(id=1).first()
dev = session.query(Dev).filter_by(id=1).first()

# associating company and dev
freebie1.company = company
freebie2.dev = dev

session.add(freebie1)
session.add(freebie2)

session.commit()
session.close()
