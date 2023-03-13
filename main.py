import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("MySQL Database Connection Successful")
    except Error as err:
        print(f"Error {err}")
    return connection
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: {err}")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query sucessful")
    except Error as err:
        print(f"Error: {err}")
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: {err}")

#Queries
create_database_query = "create database EXOTIC_DEALERSHIP"

#create coupe table
create_coupe_table = """  
create table COUPE_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL);"""

#create suv table
create_suv_table = """
create table SUV_MODELS(
vin_number VARCHAR(12) PRIMARY KEY,
make VARCHAR(50) NOT NULL,
model VARCHAR(50) NOT NULL,
mileage integer NOT NULL,
price integer NOT NULL);
"""

#populate coupe table

#populate coupe table
coupe_vehicles = """ 
insert into COUPE_MODELS values
('123abc321','Ashton Martin', 'Vanquish', 2000, 115000),
('asd748541', 'Audi', 'RS 7', 1200, 12500) """

#populate suv table
suv_table = """
insert into SUV_models values
('123abc324','Jeep', 'Trackhawk',700, 111555)
('asd748441', 'Lamborghini', 'URUS', 1200, 135000) """

#read values from coupe table
display_coupe_models_table = """
SELECT * FROM COUPE_MODELS;
"""

#read values from suv table
display_suv_models_table = """
SELECT * FROM SUV_MODELS;
"""


update_firstSUV_mileage = """
update suv_models
SET mileage = 5000
where vin_number = '123abc321'
"""

update_firstCoupe_mileage = """
update suv_models
SET mileage = 5000
where vin_number = '123abc321'
"""


#delete value from table

remove_firstCoupe_vehicle = """
DELETE FROm COUPE_MODELS
WHERE vin_number = '123abc321';"""


#calling statement
connection = create_server_connection("localhost", "root", "student","exotic_dealership")
#call work horse function to run query
execute_query(connection,remove_firstCoupe_vehicle )

#call work horse function to run query
execute_query(connection, update_firstCoupe_mileage)

#call read query function to fetch information from MySQL
results = read_query(connection, display_coupe_models_table)
#iterate through the table to display all information
for result in results:
    print(result)
