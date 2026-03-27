-- =====================================
-- KPI QUERIES
-- =====================================

-- 1. Total Revenue
SELECT SUM(o.quantity * i.item_price) AS total_revenue
FROM orders o
JOIN item i ON o.item_id = i.item_id;

-- 2. Average Order Value
SELECT AVG(order_total) AS avg_order_value
FROM (
    SELECT 
        order_id,
        SUM(o.quantity * i.item_price) AS order_total
    FROM orders o
    JOIN item i ON o.item_id = i.item_id
    GROUP BY order_id
) t;


-- =====================================
-- PRODUCT PERFORMANCE
-- =====================================

-- Top 10 items by revenue
SELECT 
    i.item_name, 
    SUM(o.quantity * i.item_price) AS revenue
FROM orders o
JOIN item i ON o.item_id = i.item_id
GROUP BY i.item_name
ORDER BY revenue DESC
LIMIT 10;


-- =====================================
-- CUSTOMER ANALYSIS
-- =====================================

-- Top customers by spend
SELECT 
    c.cust_id, 
    c.cust_firstname, 
    c.cust_lastname,
    SUM(o.quantity * i.item_price) AS total_spent
FROM orders o
JOIN customers c ON o.cust_id = c.cust_id
JOIN item i ON o.item_id = i.item_id
GROUP BY c.cust_id, c.cust_firstname, c.cust_lastname
ORDER BY total_spent DESC
LIMIT 10;


-- =====================================
-- OPERATIONAL METRICS
-- =====================================

-- Orders by hour
SELECT 
    HOUR(created_at) AS order_hour, 
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_hour
ORDER BY order_hour;


-- =====================================
-- GEOGRAPHIC ANALYSIS
-- =====================================

-- Revenue by zipcode
SELECT 
    a.delivery_zipcode,
    SUM(o.quantity * i.item_price) AS revenue
FROM orders o
JOIN address a ON o.add_id = a.add_id
JOIN item i ON o.item_id = i.item_id
GROUP BY a.delivery_zipcode
ORDER BY revenue DESC;