import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    database="sales_db",
    password="",
)

mycursor = mydb.cursor()

#### Total number of customers, products, orders aur payments kitne hain?

mycursor.execute("""
SELECT
    (SELECT COUNT(*) FROM customers) AS total_customers,
    (SELECT COUNT(*) FROM products) AS total_products,
    (SELECT COUNT(*) FROM orders) AS total_orders,
    (SELECT COUNT(*) FROM payments) AS total_payments
""")
result = mycursor.fetchone()
print(result)

### Total Sales / Revenue

mycursor.execute("SELECT SUM(total_amount) AS total_sales FROM orders")
result = mycursor.fetchone()
print("Total Sales:", result[0])

### Delivered Orders se actual revenue kitni hui?

mycursor.execute("SELECT SUM(total_amount) AS delivered_revenue FROM orders WHERE order_status = 'Delivered'")
result = mycursor.fetchone()
print("Delivered Revenue:", result[0])

### Order Status-wise ### Count Kitne orders Delivered, Pending, Cancelled aur Returned hain?

mycursor.execute("SELECT order_status, COUNT(*) AS total_orders FROM orders GROUP BY order_status ORDER BY total_orders DESC")
results = mycursor.fetchall()
for row in results:
    print(row)

### Average Order Value ### Ek order par average customer kitna spend kar raha hai?

mycursor.execute("SELECT AVG(total_amount) AS average_order_value FROM orders WHERE order_status = 'Delivered' ")
result = mycursor.fetchone()
print("Average Order Value:", round(result[0], 2))

### Top 5 Best-Selling Products ### Kaunse 5 products sabse zyada quantity me sell hue?

mycursor.execute("""
SELECT 
    p.product_id,
    p.product_name,
    SUM(o.quantity) AS total_quantity_sold
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
WHERE o.order_status = 'Delivered'
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity_sold DESC
LIMIT 5
""")
results = mycursor.fetchall()
print("Top 5 Best-Selling Products:")
for row in results:
    print(row)

### Top 5 Products by Revenue

mycursor.execute("""
SELECT
    p.product_id,
    p.product_name,
    SUM(o.quantity * o.unit_price * (1 - o.discount / 100)) AS total_revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
WHERE o.order_status = 'Delivered'
GROUP BY p.product_id, p.product_name
ORDER BY total_revenue DESC
LIMIT 5
""")
results = mycursor.fetchall()
print("Top 5 Products by Revenue:")
for row in results:
    print(row)

### Category-wise Revenue ### Kaunsi product category sabse zyada revenue generate kar rahi hai?

mycursor.execute("""
SELECT
    p.category,
    SUM(o.quantity * o.unit_price * (1 - o.discount / 100)) AS total_revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
WHERE o.order_status = 'Delivered'
GROUP BY p.category
ORDER BY total_revenue DESC
""")
results = mycursor.fetchall()
print("Category-wise Revenue:")
for row in results:
    print(row)

### Top 5 Customers by Spending ## Kaunse 5 customers sabse zyada spend kar rahe hain?

mycursor.execute("""
SELECT
    c.customer_id,
    c.customer_name,
    SUM(o.total_amount) AS total_spent
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
WHERE o.order_status = 'Delivered'
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spent DESC
LIMIT 5
""")
results = mycursor.fetchall()
print("Top 5 Customers by Spending:")
for row in results:
    print(row)

### City-wise Revenue ## Kaunsi city se sabse zyada sales/revenue aa rahi hai?

mycursor.execute("""
SELECT
    c.city,
    SUM(o.total_amount) AS total_revenue
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
WHERE o.order_status = 'Delivered'
GROUP BY c.city
ORDER BY total_revenue DESC
""")

results = mycursor.fetchall()
print("City_wise Revenue:")
for row in results:
    print(row)

### State-wise Revenue Analysis. ## Kaunse states se sabse zyada revenue aa rahi hai? 

mycursor.execute("""
SELECT
    c.state,
    SUM(o.total_amount) AS total_revenue
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
WHERE o.order_status = 'Delivered'
GROUP BY c.state
ORDER BY total_revenue DESC
""")
results = mycursor.fetchall()
print("State_wise Revenue:")
for row in results:
    print(row)


### Monthly Revenue ## Kaunse months me revenue sabse zyada generate hui?

mycursor.execute("""
SELECT
    YEAR(order_date) AS order_year,
    MONTH(order_date) AS order_month,
    SUM(total_amount) AS total_revenue
FROM orders
WHERE order_status = 'Delivered'
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY order_year, order_month
""")

results = mycursor.fetchall()
print("Monthly Revenue:")
for row in results:
    print(row)

### Payment Method-wise Orders ## Customers sabse zyada kaunsa payment method use kar rahe hain?

mycursor.execute("""
SELECT
    payment_method,
    COUNT(*) AS total_payments
FROM payments
GROUP BY payment_method
ORDER BY total_payments DESC
""")

results = mycursor.fetchall()
print("Payment Method-wise Orders:")
for row in results:
    print(row)

###Payment Status-wise Count ## Kitne payments Paid, Pending, Failed aur Refunded hain?

mycursor.execute("""
SELECT
    payment_status,
    COUNT(*) AS total_payments
FROM payments
GROUP BY payment_status
ORDER BY total_payments DESC
""")
results = mycursor.fetchall()
print("Payment Status-wise Count:")
for row in results:
    print(row)

