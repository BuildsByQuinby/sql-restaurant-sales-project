# Restaurant Sales SQL Project

## Overview
This project simulates restaurant order data for a pizza restaurant and uses SQL to analyze sales, customer behavior, and ordering patterns. The dataset was generated using Python Faker, and the restaurant was inspired by my wife’s and my favorite pizza spot, Miguel’s Pizza.

![ERD Diagram](Miguels_Pizza.png)

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
├── schema.sql
├── analysis_queries.sql
├── customers.csv
├── address.csv
├── items.csv
├── orders.csv
├── generate_item.py
├── generate_restaurant_data.py
└── images/
    ├── erd.png
    ├── menu.png
    └── logo.png
```
## Files
Briefly explain what each file does.
