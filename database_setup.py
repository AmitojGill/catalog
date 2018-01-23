import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base as Base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

class Categories(Base):
	__tablename__='categories'
	id = Column(Integer, primary_key = True)
	name = Column(String(80),nullable = False)

class Items(Base):


engine = create_engine('sqlite///catalog.db')

Base.metadata.create_all(engine)