from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    r1 = Restaurant(name="Karen's Pizza Shack", address="address1")
    r2 = Restaurant(name="Sanjay's Pizza", address="address2")
    r3 = Restaurant(name="Kiki's Pizza", address="address3")

    p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Geri", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    p3 = Pizza(name="Melanie", ingredients="Dough, Sauce, Ricotta, Red peppers, Mustard")

    db.session.add_all([r1, r2, r3, p1, p2, p3])
    db.session.commit()

    rp1 = RestaurantPizza(price=1, restaurant_id=1, pizza_id=1)

    db.session.add(rp1)
    db.session.commit()

    print("Database seeded!")