# Import for csv
import csv

# Connecting to the databse
import cx_Oracle

username = 'SYSTEM'
password = '1111'
databaseName = 'localhost/xe'
connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()

# Creating csv files
query = """SELECT * FROM Startup"""
cursor.execute(query)
with open('startup_table.csv', 'w' ,newline='') as csvfile:
    writer = csv.writer(csvfile)
    for record in cursor.fetchall():
        writer.writerow(record)

query = """SELECT * FROM City"""
cursor.execute(query)
with open('city_table.csv', 'w' ,newline='') as csvfile:
    writer = csv.writer(csvfile)
    for record in cursor.fetchall():
        writer.writerow(record)

query = """SELECT * FROM Investment"""
cursor.execute(query)
with open('investment_table.csv', 'w' ,newline='') as csvfile:
    writer = csv.writer(csvfile)
    for record in cursor.fetchall():
        writer.writerow(record)


connection.close()