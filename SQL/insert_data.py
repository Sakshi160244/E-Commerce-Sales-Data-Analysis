import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    database="sales_db",
    password="",
)

mycursor = mydb.cursor()
# i ="""INSERT INTO customers
# (customer_name, gender, email, age, city, state, registration_date)
# VALUES
# ('Aarav Sharma', 'Male', 'aarav.sharma@gmail.com', 24, 'Delhi', 'Delhi', '2025-01-15'),
# ('Priya Verma', 'Female', 'priya.verma@gmail.com', 28, 'Mumbai', 'Maharashtra', '2025-02-10'),
# ('Rohan Gupta', 'Male', 'rohan.gupta@gmail.com', 31, 'Gurugram', 'Haryana', '2025-02-18'),
# ('Ananya Singh', 'Female', 'ananya.singh@gmail.com', 22, 'Noida', 'Uttar Pradesh', '2025-03-05'),
# ('Karan Mehta', 'Male', 'karan.mehta@gmail.com', 35, 'Jaipur', 'Rajasthan', '2025-03-12'),
# ('Neha Kapoor', 'Female', 'neha.kapoor@gmail.com', 27, 'Chandigarh', 'Chandigarh', '2025-03-20'),
# ('Aditya Jain', 'Male', 'aditya.jain@gmail.com', 29, 'Bengaluru', 'Karnataka', '2025-04-02'),
# ('Sneha Patel', 'Female', 'sneha.patel@gmail.com', 26, 'Ahmedabad', 'Gujarat', '2025-04-15'),
# ('Vivek Malhotra', 'Male', 'vivek.malhotra@gmail.com', 33, 'Pune', 'Maharashtra', '2025-04-25'),
# ('Isha Agarwal', 'Female', 'isha.agarwal@gmail.com', 23, 'Kolkata', 'West Bengal', '2025-05-08'),
# ('Rahul Saini', 'Male', 'rahul.saini@gmail.com', 30, 'Sonipat', 'Haryana', '2025-05-16'),
# ('Meera Joshi', 'Female', 'meera.joshi@gmail.com', 32, 'Indore', 'Madhya Pradesh', '2025-05-28'),
# ('Arjun Bhatia', 'Male', 'arjun.bhatia@gmail.com', 25, 'Chennai', 'Tamil Nadu', '2025-06-06'),
# ('Pooja Nair', 'Female', 'pooja.nair@gmail.com', 29, 'Kochi', 'Kerala', '2025-06-18'),
# ('Manish Yadav', 'Male', 'manish.yadav@gmail.com', 36, 'Lucknow', 'Uttar Pradesh', '2025-07-01'),
# ('Simran Kaur', 'Female', 'simran.kaur@gmail.com', 24, 'Amritsar', 'Punjab', '2025-07-14'),
# ('Nikhil Roy', 'Male', 'nikhil.roy@gmail.com', 27, 'Kolkata', 'West Bengal', '2025-07-22'),
# ('Riya Khanna', 'Female', 'riya.khanna@gmail.com', 21, 'Faridabad', 'Haryana', '2025-08-05'),
# ('Sahil Arora', 'Male', 'sahil.arora@gmail.com', 34, 'Hyderabad', 'Telangana', '2025-08-18'),
# ('Tanya Das', 'Female', 'tanya.das@gmail.com', 26, 'Bhubaneswar', 'Odisha', '2025-08-30')"""


# i = """INSERT INTO products
# (product_name, category, price, stock_quantity)
# VALUES
# ('Wireless Mouse', 'Electronics', 899.00, 50),
# ('Bluetooth Headphones', 'Electronics', 1999.00, 35),
# ('Laptop', 'Electronics', 55000.00, 15),
# ('Smartphone', 'Electronics', 28000.00, 25),
# ('USB-C Cable', 'Electronics', 499.00, 100),

# ('Running Shoes', 'Footwear', 2999.00, 30),
# ('Casual Sneakers', 'Footwear', 2499.00, 40),
# ('Formal Shoes', 'Footwear', 3499.00, 20),

# ('Cotton T-Shirt', 'Clothing', 599.00, 80),
# ('Denim Jeans', 'Clothing', 1499.00, 45),
# ('Hoodie', 'Clothing', 1299.00, 35),
# ('Formal Shirt', 'Clothing', 999.00, 50),

# ('Coffee Maker', 'Home & Kitchen', 3499.00, 18),
# ('Electric Kettle', 'Home & Kitchen', 1799.00, 25),
# ('Non-Stick Cookware Set', 'Home & Kitchen', 2999.00, 12),

# ('Face Wash', 'Beauty', 399.00, 60),
# ('Sunscreen', 'Beauty', 699.00, 55),
# ('Perfume', 'Beauty', 1599.00, 30),

# ('Smart Watch', 'Accessories', 3999.00, 22),
# ('Backpack', 'Accessories', 1299.00, 40)"""


# mycursor.execute(i)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")


# mycursor.execute("SELECT MIN(customer_id), MAX(customer_id), COUNT(*) FROM customers")
# print(mycursor.fetchone())
# mycursor.execute("SELECT MIN(product_id), MAX(product_id), COUNT(*) FROM products")
# print(mycursor.fetchone())

# mycursor.execute("""
# SELECT product_id, product_name, price
# FROM products
# ORDER BY product_id
# """)
# for row in mycursor:
#     print(row)



