from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

myFirstRestaurant = Restaurant(name="Pizza Palace")

cheesepizza = MenuItem(name="Cheese Pizza", description="Made with all natural ingredients and fresh mozzarella",
                       course="Entree", price="$8.99", restaurant=myFirstRestaurant)

# session.add(myFirstRestaurant)
# session.add(cheesepizza)
# session.commit()

# show2 = session.query(MenuItem).all()
# show = session.query(Restaurant).first()

# print(show.name)

# items = session.query(MenuItem).all()
# for item in items:
#     print(item.name)

# places = session.query(Restaurant).all()
# veggieBurgers = session.query(MenuItem).filter_by(name='Veggie Burger')
# UrbanVeggieBurger = session.query(MenuItem).filter_by(id=7).one()
#print(UrbanVeggieBurger.price)
# for veggieBurger in veggieBurgers:
#     print(veggieBurger.id)
#     print(veggieBurger.price)
#     print(veggieBurger.restaurant.name)
#     print("\n")

# UrbanVeggieBurger.price = "$5.99"
# session.add(UrbanVeggieBurger)
# session.commit()

# print(UrbanVeggieBurger.price)

# for veggieBurger in veggieBurgers:
#     veggieBurger.price = "$2.99"
#     session.add(veggieBurger)
#     session.commit()

# for veggieBurger in veggieBurgers:
#     print(veggieBurger.id)
#     print(veggieBurger.price)
#     print(veggieBurger.restaurant.name)
#     print("\n")

for place in places:
    print(place.name)
    print("\n")
