"""
Generate synthetic menu item data for SQL restaurant project.

Creates:
- items.csv

Generates a variety of menu items across categories such as pizza, subs,
wings, sides, and drinks, with randomized sizes, SKUs, and prices.
"""

from faker import Faker
import pandas as pd
import random

fake = Faker()

categories = {
    "Pizza": ["Cheese", "Pepperoni", "Supreme", "Veggie", "BBQ Chicken"],
    "Sub": ["Italian Sub", "Turkey Sub", "Ham & Cheese", "Philly Cheesesteak"],
    "Wings": ["Buffalo Wings", "Garlic Parmesan Wings", "BBQ Wings"],
    "Side": ["Fries", "Mozzarella Sticks", "Garlic Bread", "Onion Rings"],
    "Salad": ["Garden Salad", "Greek Salad", "Caesar Salad"],
    "Pasta": ["Spaghetti", "Chicken Alfredo", "Lasagna"],
    "Dessert": ["Cheesecake", "Cannoli", "Chocolate Cake"],
    "Drink": ["Soda", "Iced Tea", "Water"]
}

sizes = ["Small", "Medium", "Large", "Regular"]

items = []
item_id = 1

for category, names in categories.items():
    for name in names:
        item = {
            "item_id": item_id,
            "sku": fake.unique.bothify(text="??##"),
            "item_name": name,
            "item_cat": category,
            "item_size": random.choice(sizes),
            "item_price": round(random.uniform(2, 20), 2)
        }
        items.append(item)
        item_id += 1

df = pd.DataFrame(items)
df.to_csv("items.csv", index=False)

print("items.csv generated successfully")
