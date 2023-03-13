Install Extensions:


Configuration:
    - Installation of extensions:
    -mysql
    -mysql-connector
    -mysql-connector-python
    - pandas - pandas is a software library written for the Python
    programming language
    for data manipulation and analysis. In particular, it offers
    data structures and operations for
    manipulating numerical tables and time series.


file>settings>name of project > project interpreter, search each extension then
install


Establish communication to mySQL


1.) content for main.py.
-establish connection from code window to mySQL
content for main.py:

import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password
        )
        print("MySQL Database Connection Successful")
    except Error as err:
        print(f"Error {err}")
    return connection


#calling statement
connection = create_server_connection("localhost", "root", "student")

2.)Creation of database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: {err}")
#call create_database function to create DB in mySQL
create_database(connection, create_database_query)
#Queries
create_database_query = "create database EXOTIC_DEALERSHIP"
#calling statement
connection = create_server_connection("localhost", "root", "student")
#call create_database function to create DB in mySQL
create_database(connection, create_database_query)