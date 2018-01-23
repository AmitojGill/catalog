import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base as Base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine



engine = create_engine('sqlite///catalog.db')