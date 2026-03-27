"""
Generate synthetic restaurant data for SQL analysis project.

Creates:
- customers.csv
- address.csv
- orders.csv

Uses Faker to simulate realistic customer and order behavior.
"""

from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()
random.seed(42)

NUM_CUSTOMERS = 300
NUM_ORDERS = 5000

# Item IDs already in your MySQL item table
ITEM_IDS = list(range(1, 29))

# -----------------------------
# Customers
# -----------------------------
customers = []
for cust_id in range(1, NUM_CUSTOMERS + 1):
    customers.append({
        "cust_id": cust_id,
        "cust_firstname": fake.first_name(),
        "cust_lastname": fake.last_name()
    })

customers_df = pd.DataFrame(customers)

# -----------------------------
# Addresses
# One address per customer
# -----------------------------
addresses = []
zipcodes = ["43201", "43205", "43206", "43207", "43215", "43224", "43229", "43230", "43004", "43068"]

for add_id in range(1, NUM_CUSTOMERS + 1):
    addresses.append({
        "add_id": add_id,
        "delivery_address1": fake.street_address(),
        "delivery_address2": fake.secondary_address() if random.random() < 0.15 else "",
        "delivery_city": "Columbus",
        "delivery_zipcode": random.choice(zipcodes)
    })

addresses_df = pd.DataFrame(addresses)

# -----------------------------
# Weighted order times
# -----------------------------
def weighted_order_datetime():
    start_date = datetime.now() - timedelta(days=180)
    day_offset = random.randint(0, 179)
    dt = start_date + timedelta(days=day_offset)

    weekday = dt.weekday()  # 0=Mon, 6=Sun

    if weekday in [4, 5]:  # Fri/Sat
        hour = random.choices(
            [11, 12, 13, 17, 18, 19, 20, 21],
            weights=[8, 14, 10, 10, 16, 16, 10, 6],
            k=1
        )[0]
    else:
        hour = random.choices(
            [11, 12, 13, 17, 18, 19, 20],
            weights=[7, 12, 8, 9, 14, 13, 7],
            k=1
        )[0]

    minute = random.randint(0, 59)
    second = random.randint(0, 59)

    return dt.replace(hour=hour, minute=minute, second=second, microsecond=0)

# -----------------------------
# Weighted item popularity
# Higher IDs are still possible, just less common
# -----------------------------
item_weights = {
    1: 18, 2: 20, 3: 14, 4: 10, 5: 10,
    6: 9, 7: 8, 8: 7, 9: 9,
    10: 8, 11: 7, 12: 6,
    13: 7, 14: 6, 15: 5, 16: 4,
    17: 6, 18: 5, 19: 5,
    20: 6, 21: 5, 22: 4,
    23: 3, 24: 3, 25: 3,
    26: 7, 27: 6, 28: 5
}

item_population = list(item_weights.keys())
item_weight_values = list(item_weights.values())

# -----------------------------
# Orders
# -----------------------------
orders = []
for row_id in range(1, NUM_ORDERS + 1):
    cust_id = random.randint(1, NUM_CUSTOMERS)
    add_id = cust_id
    delivery = random.choice([0, 1])

    orders.append({
        "row_id": row_id,
        "order_id": f"O{100000 + row_id}",
        "created_at": weighted_order_datetime().strftime("%Y-%m-%d %H:%M:%S"),
        "item_id": random.choices(item_population, weights=item_weight_values, k=1)[0],
        "quantity": random.choices([1, 2, 3, 4], weights=[55, 28, 12, 5], k=1)[0],
        "cust_id": cust_id,
        "delivery": delivery,
        "add_id": add_id
    })

orders_df = pd.DataFrame(orders)

# -----------------------------
# Save files
# -----------------------------
customers_df.to_csv("customers.csv", index=False)
addresses_df.to_csv("address.csv", index=False)
orders_df.to_csv("orders.csv", index=False)

print("Generated customers.csv, address.csv, and orders.csv")