from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup.py import Base, Categories, Items

engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


catagories = ["Kitchen & Dining","Bed & Bath", "Appliances", "Garden & Outdoor", "Fine Art", "Pet Supplies"]

for i in catgories:
	category = Categories(name=i)
	session.add(i)
	session.commit()



