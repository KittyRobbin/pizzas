from random import choice as rc
from app import app
# from faker import Faker
from models import db, Restaurant, Pizza, RestaurantPizza

# fake = Faker()
with app.app_context():
# This will delete any existing rows
# so you can run the seed file multiple times without having duplicate entries in your database
    print("Deleting data...")
    db.drop_all()
    db.create_all()

    print("Creating restaurants...")
    shack = Restaurant(name="Karen's Pizza Shack", address='address1')
    bistro = Restaurant(name="Sanjay's Pizza", address='address2')
    palace = Restaurant(name="Kiki's Pizza", address='address3')
    aubergene = Restaurant(name="Mary's Pizza", address='address4')
    pizzahut = Restaurant(name="Joe's Pizza", address='address5')
    restaurants = [shack, bistro, palace, aubergene, pizzahut]

    print("Creating pizzas...")
    cheese = Pizza(name="cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pepperoni = Pizza(name="pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    california = Pizza(name="california", ingredients="Dough, Sauce, Ricotta, Red peppers, Mustard")
    french = Pizza(name="french", ingredients="Dough, Onions, Cheese")
    pineapple = Pizza(name="pineapple", ingredients="Dough, Pineapples, Cheese")
    pizzas = [cheese, pepperoni, california, french, pineapple]

    print("Creating RestaurantPizza...")
    pr1 = RestaurantPizza(restaurant_id=1, pizza_id=1, price=12)
    pr2 = RestaurantPizza(restaurant_id=5, pizza_id=5, price=1)
    pr3 = RestaurantPizza(restaurant_id=3, pizza_id=2, price=13)
    pr4 = RestaurantPizza(restaurant_id=4, pizza_id=3, price=20)
    pr5 = RestaurantPizza(restaurant_id=2, pizza_id=4, price=28)
    restaurantPizzas = [pr1, pr2, pr3, pr4, pr5]
    db.session.add_all(restaurants)
    db.session.add_all(pizzas)
    db.session.add_all(restaurantPizzas)
    db.session.commit()

    print("Seeding done!")