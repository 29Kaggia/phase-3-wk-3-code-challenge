# seeds.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

engine = create_engine('sqlite:///restaurant_reviews.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create sample instances
restaurant1 = Restaurant(name='Restaurant 1', price=2)
restaurant2 = Restaurant(name='Restaurant 2', price=3)
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')
review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=5, restaurant=restaurant2, customer=customer2)

# Add instances to the session
session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])

# Commit the changes to the database
session.commit()
