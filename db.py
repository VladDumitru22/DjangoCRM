from decouple import config
from mysql.connector import Error
import mysql.connector


try:
    dataBase = mysql.connector.connect(
        host = config('DB_HOST'),
        user = config('DB_USER'),
        passwd = config('DB_PASSWORD'),
    )

    # Prepare a cursor object
    cursorObject = dataBase.cursor()

    # Create a database
    cursorObject.execute(f"CREATE DATABASE {config('DB_NAME')}")
    
except Error as e:
    if "1007" in str(e):
        print("Database already exists.")
    else:
        print(f"Error creating database: {e}")

finally:
    if 'cursorObject' in locals():
        cursorObject.close()
    if 'dataBase' in locals() and dataBase.is_connected():
        dataBase.close()
