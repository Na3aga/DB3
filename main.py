
import cx_Oracle

username = 'SYSTEM'
password = '1111'
databaseName = 'localhost/xe'

connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()

query = """
SELECT *
    FROM
    (SELECT
         strtp_city_ivst.COUNTRY_CODE,
         COUNT(strtp_city_ivst.INVSTID) AS "Number of investments"
    FROM strtp_city_ivst
    GROUP BY
        strtp_city_ivst.COUNTRY_CODE
    ORDER BY
        "Number of investments" DESC
        )
WHERE ROWNUM <= 12
"""

cursor.execute(query)
print('Запит 1')
print('|country code         |number of investments')
print('-'*35)

row = cursor.fetchone()
while row:

    print(f"|{row[0]}|{row[1]}")
    row = cursor.fetchone()

print()



"""----------------------------------------------------------------------
Запит 2 - вивести топ штатів та їх загальне ФІНАНСУВАННЯ компаній, а також фінансування компаній іншиї країн (однією групою)"""

query = '''
SELECT
    strtp_city_ivst.STATE_CODE, SUM(strtp_city_ivst.TOTAL_FUNDING)  AS "total funding"
FROM strtp_city_ivst
GROUP BY
    strtp_city_ivst.STATE_CODE
ORDER BY
    "total funding" DESC
'''

cursor.execute(query)
print('Запит 2')
print('|state code  |total funding')
print('-'*25)

row = cursor.fetchone()
while row:

    print(f"|{row[0]}|{row[1]}")
    row = cursor.fetchone()

print()

"""------------------------------------------------------------------------
Запит 3 - вивести динаміку переглядів виступів на ted.com по роках (за всі роки)."""

query = '''
SELECT
    strtp_city_ivst.SEED, ROUND(AVG(strtp_city_ivst.VENTURE)) AS VENTURE
FROM
    strtp_city_ivst
GROUP BY
    strtp_city_ivst.SEED
ORDER BY
    strtp_city_ivst.SEED'''

cursor.execute(query)
print('Запит 3')
print('|seed  |venture')
print('-'*20)

row = cursor.fetchone()
while row:

    print(f"|{row[0]}|{row[1]}")
    row = cursor.fetchone()
    
print()

connection.close()