# Import for csv
import csv

# Connecting to the databse
import cx_Oracle

username = 'SYSTEM'
password = '1111'
databaseName = 'localhost/xe'
connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()

# Operating csv file
cities, startups, investmnets = {}, {}, []

with open('investments.csv', newline='') as csvfile:
    ireader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in ireader:
        cities[row[-3].strip().replace("'",'')] = [row[-4].strip().replace("'",''), row[-5].strip(), row[-6].strip()]
        startups[row[0].strip().replace("'",'')] = [row[-3].strip().replace("'",''), row[2].strip().replace("'",''), row[3].strip().replace(",",''), row[1].strip()]
        investmnets.append([row[0].strip().replace("'",''), row[-2].strip(), row[-1].strip()])

# print(cities)
# print(startups)
# print(investmnets)

# Writing to DataBase
insert = ""

for city, info in cities.items():
    insert += "INSERT INTO City(city, region, state_code, country_code)\n"
    insert += f"VALUES('{city}', '{info[0]}', '{info[1]}', '{info[2]}')\n"
    cursor.execute(insert)
    # print(insert)
    insert = ""

connection.commit()

for startup, info in startups.items():
    insert += "INSERT INTO Startup(name, city, market, total_funding, website)\n"
    insert += f"VALUES('{startup}', '{info[0]}', '{info[1]}', {int(info[2])}, '{info[3]}')\n"
    cursor.execute(insert)
    # print(insert)
    insert = ""

connection.commit()

for info in investmnets:
    insert += "INSERT INTO Investment(name, seed, venture)\n"
    insert += f"VALUES('{info[0]}', {info[1]}, {info[2]})\n"
    cursor.execute(insert)
    # print(insert)
    insert = ""

connection.commit()

connection.close()