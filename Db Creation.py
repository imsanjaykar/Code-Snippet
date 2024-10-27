import mysql.connector
from mysql.connector import errorcode

# Database connection details
db_config = {
    'user': 'root',
    'password': 'Root1',
    'host': 'localhost',
}

# Connect to MySQL server
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

#Steps to Create a new database and to ensure that no Database should present with this name
database_name = "profile"
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
print(f"Database '{database_name}' created successfully!")

# Close the connection
cursor.close()
connection.close()