import mysql.connector
import random
from datetime import date, timedelta
# MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sales_db"
)

mycursor = mydb.cursor()
print("MySQL connected successfully!")

mycursor.execute("SELECT product_id, price FROM products ")
products = mycursor.fetchall()
print(products)


mycursor.execute(" SELECT customer_id FROM customers ")
customers = mycursor.fetchall()
print(customers)



orders = []
start_date = date(2025, 1, 1)
for i in range(100):
    customer_id = random.choice(customers)[0]
    product_id, unit_price = random.choice(products)

    quantity = random.randint(1, 5)
    discount = random.choice([0, 5, 10, 15, 20])
    order_status = random.choice([
        "Delivered",
        "Delivered",
        "Delivered",
        "Pending",
        "Cancelled",
        "Returned"
    ])

    order_date = start_date + timedelta(days=random.randint(0, 365))

    subtotal = float(unit_price) * quantity
    discount_amount = subtotal * discount / 100
    total_amount = subtotal - discount_amount

    orders.append((
        customer_id,
        product_id,
        quantity,
        float(unit_price),
        discount,
        round(total_amount, 2),
        order_status,
        order_date
    ))
print("Total orders generated:", len(orders))


# insert_query = """
# INSERT INTO orders
# (customer_id, product_id, quantity, unit_price, discount,
#  total_amount, order_status, order_date)
# VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
# """
# mycursor.executemany(insert_query, orders)
# mydb.commit()
# print(mycursor.rowcount, "orders inserted successfully!")

mycursor.execute("""
    SELECT order_id, order_status, total_amount, order_date
    FROM orders
""")
order_data = mycursor.fetchall()
print("Total orders found:", len(order_data))

payment_data = []
payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery"
]

for order_id, order_status, total_amount, order_date in order_data:

    if order_status == "Delivered":
        payment_status = "Paid"

    elif order_status == "Pending":
        payment_status = "Pending"

    elif order_status == "Cancelled":
        payment_status = "Failed"

    elif order_status == "Returned":
        payment_status = "Refunded"

    payment_method = random.choice(payment_methods)

    payment_data.append((
        order_id,
        payment_method,
        payment_status,
        order_date,
        float(total_amount)
    ))
print("Total payments generated:", len(payment_data))

# insert_payment_query = """
# INSERT INTO payments
# (order_id, payment_method, payment_status, payment_date, amount)
# VALUES (%s, %s, %s, %s, %s)
# """
# mycursor.executemany(insert_payment_query, payment_data)
# mydb.commit()
# print(mycursor.rowcount, "payments inserted successfully!")

mycursor.execute("SELECT COUNT(*) FROM payments")
total_payments = mycursor.fetchone()[0]
print("Total payments:", total_payments)

mycursor.execute("SELECT COUNT(*) FROM orders")
total_orders = mycursor.fetchone()[0]
print("Total orders in database:", total_orders)

# mycursor.execute("DELETE FROM orders")
# mycursor.execute("ALTER TABLE ORDERS AUTO_INCREMENT = 1")
# mydb.commit()
# print(mycursor.rowcount, "orders deleted")

mycursor.execute("SELECT * FROM orders LIMIT 10")
for row in mycursor:
    print(row)

