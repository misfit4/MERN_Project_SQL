Exotic Dealership MySQL:

The purpose of this application is to create a database to hold information about the vehicles in stock.
Python will be used to create the database table and all infformation inside pertaining to CRUD
operations.

- Installation of extensions:
    -mysql
    -mysql-connector
    -mysql-connector-python
    - pandas - pandas is a software library written for the Python
    programming language
    for data manipulation and analysis. In particular, it offers
    data structures and operations for
    manipulating numerical tables and time series.


1.)Establish communication from PyCharm to mySQL

*insert screenshot of connection

2.) 

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

2.) Establish communication from main.py to mySQL:

*insert screenshot of successful connection.

3.)cCreate database from main.py

*insert screenshot of successful creation of database.

4.) Create coupe table for DB:
*insert screenshot of creation of table.

5.) Create SUV table for DB:
*insert screenshot of creation of table.

6.) Populate coupe table:
*insert screenshot of table being populated 

7.) Populate SUV table:
*insert screenshot of table being populated 

8.) create function to read data from tables
*insert screenshot of values from table being displayed in PyCharm

9.) display updated information in PyChar