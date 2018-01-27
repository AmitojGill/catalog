import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Categories(Base):
	__tablename__='categories'
	id = Column(Integer, primary_key = True)
	name = Column(String(80),nullable = False)

class Items(Base):
	__tablename__='items'
	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	description = Column(String(250))
	img = Column(String(250))
	buy=Column(String(250))
	category_id = Column(Integer, ForeignKey('categories.id'))
	category = relationship(Categories)


engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)