import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    database="sales_db",
    password="",
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE sales_db")
mycursor.execute("SHOW DATABASES ")
for x in mycursor:
  print(x)


