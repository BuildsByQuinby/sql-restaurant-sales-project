# Restaurant Sales SQL Project

## Overview
This project simulates transactional data for a pizza restaurant and uses SQL to analyze sales performance, customer behavior, and ordering patterns. The dataset was generated using Python (Faker) to mimic realistic restaurant operations, including customers, orders, and delivery activity over time. The project is inspired by Miguel’s Pizza, a real restaurant that my spouse and I love, which served as the conceptual foundation for the business scenario. While the structure and idea are grounded in that experience, the menu items and underlying data are synthetically generated and do not directly reflect the actual restaurant. This project demonstrates relational database design across multiple tables (orders, customers, address, item), data generation using Python, and SQL-based analysis of revenue, product performance, and customer trends, with the goal of showcasing practical SQL skills in a realistic business context.

![Miguels_Pizza](images/Miguels_Pizza.png)

## Dataset
The database contains four tables:
- orders
- customers
- address
- item

## Tools Used
- MySQL Workbench
- dbdiagram.io
- Python
- CSV files

## Schema

![ERD Diagram](images/ERD_dbdiagram.png)

## Business Questions
- What are the best-selling items?
- Which items generate the most revenue?
- What are the busiest ordering times?
- Which customers spend the most?
- How many orders are delivery vs pickup?

## Key Insights

## Structure
```
sql-restaurant-sales-project/
│
├── README.md
├── analysis_queries.sql
└── data/
    ├── customers.csv
    ├── address.csv
    ├── items.csv
    ├── orders.csv
    ├── generate_item.py
    └── generate_data.py
└── images/
    ├── Miguels_Pizza.png
    └── ERD_dbdiagram.png
```
## Data Generation

The dataset was generated using Python and the Faker library to simulate realistic restaurant activity. The data includes randomized customer information, delivery addresses, menu items, and weighted order behavior to better reflect real-world patterns.

The script used to generate the data can be found in:
`data/generate_data.py`
`data/generate_items.py`

It creates:
- customers.csv
- address.csv
- orders.csv
- items.csv

## Files
