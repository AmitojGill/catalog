from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, Items

engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


categories = ["Kitchen & Dining","Bed & Bath", "Appliances", 
				"Garden & Outdoor", "Fine Art", "Pet Supplies"]

for i in categories:
	category = Categories(name=i)
	session.add(category)
	session.commit()
	print "%s added to the categories table" % i



