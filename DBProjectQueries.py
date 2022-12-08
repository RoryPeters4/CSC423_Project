import sqlite3
import pandas as pd

#This function takes a database connection and a query as paramaters and returns a pandas dataframe.
#Used for SELECT commands since other commands don't have output.
def SelectQuery(DB, query):
    cursor = DB.cursor()
    cursor.execute(query)
    column_names = [row[0] for row in cursor.description]
    table_data = cursor.fetchall()
    df = pd.DataFrame(table_data, columns=column_names) 
    return df

#This function takes a database connection and a query as paramaters and returns nothing.
#Used for any  query that manipulates the data (Doesn't return any data)
def ManipulationQuery(DB, query):
    cursor = DB.cursor()
    cursor.execute(query)
    table_data = cursor.fetchall()
    df = pd.DataFrame(table_data)

#Creates a connection with the PawsomePetsDatabase
db_connect = sqlite3.connect('PawsomePetsDatebase.db')

# Query to display the StaffNo and S_Name of all Clinic Managers, as well as the ClinicNo and C_Name of the clinic they manage
query = """
    SELECT s.StaffNo, s.S_Name, c.ClinicNo, c.C_Name
    FROM StaffMember s, Clinic c
    WHERE s.S_Position = 'Clinic Manager' AND s.ClinicNo = c.ClinicNo
    """
print(SelectQuery(db_connect, query), '\n')

# Query to display each Owner's OwnerNo & O_Name and all of their pets information
query = """
    SELECT o.OwnerNo, o.O_Name, p.*
    FROM Owner o, Pet p
    WHERE o.OwnerNo = p.OwnerNo
    """
print(SelectQuery(db_connect, query), '\n')

# Query to display the Examination details and pet information of PetNo = 1
query = """
    SELECT e.*, p.*
    FROM Examination e, Pet p
    WHERE e.PetNo = 1 AND e.PetNo = p.PetNo
    """
print(SelectQuery(db_connect, query), '\n')

#Query that lists all staff members with a salary over 50,000
query = """
    SELECT * FROM StaffMember WHERE salary > 50000
"""
print(SelectQuery(db_connect, query), '\n')

# Query that updates the ClinicNo of the StaffMember with StaffNo 2
query = """
    UPDATE StaffMember
    SET ClinicNo = 1
    WHERE StaffNo = 1
"""
ManipulationQuery(db_connect, query), '\n'

# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()
