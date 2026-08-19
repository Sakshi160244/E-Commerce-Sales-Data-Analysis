import mysql.connector


def create_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sales_db"
    )

    print("Database connected successfully!")

    return mydb