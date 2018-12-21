from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

rest = session.query(Restaurant).all()
items = session.query(MenuItem).filter_by(rest_name='#Urban Burger')
for i in rest:
    print(i.name)
    print(" ")
for a in items:
    print(items.name)
    print("")
