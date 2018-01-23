import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base as Base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

class Categories(Base):

class Items(Base):

engine = create_engine('sqlite///catalog.db')

Base.metadata.create_all(engine)