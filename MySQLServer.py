import mysql.connector

from mysql.connector import Error

def myConnection():
 
    try:
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Joe@1114_alx"
        )
        print("Connection successful!")
        return conn
    except mysql.connector.Error as e:
        
        print(f"Database connection error: {e}")
        return None


def create_database():
    try:
        
        connn = myConnection()
        if connn is None:
            print("Could not connect to database")
            return 
        cursor =connn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        connn.commit()
        connn.close()
        print("Database 'alx_book_store' created successfully!")
        
    except mysql.connector.Error as e:
        print(f"Error creating database:{e}")
		 
create_database()