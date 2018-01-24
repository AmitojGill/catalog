from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, Items

engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


categories = ["Kitchen & Dining","Bed & Bath", "Appliances", 
				"Garden & Outdoor", "Fine Art", "Pet Supplies"]

#Delete any previus data
delete_all = session.query(Categories).all()

for i in delete_all:
	session.delete(i)
	session.commit()

delete_items = session.query(Items).all()

for i in delete_items:
	session.delete(i)
	session.commit()

for i in categories:
	category = Categories(name=i)
	session.add(category)
	session.commit()
	print "%s added to the categories table" % i

cat = session.query(Categories).all()

for i in cat:
	print i.name

data = {"category":"Kitchen & Dining", "name":"Cookware", "description":"Gotham Steel 10-Piece Nonstick Frying Pan and Cookware Set - Graphite"}

new_data = Items(name = data["name"], description = data["description"], category_id=data['category'])
session.add(new_data)
session.commit()
