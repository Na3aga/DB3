import cx_Oracle
import chart_studio
chart_studio.tools.set_credentials_file(username = 'na3aga', api_key = 'LWQffbuUY6FDiEZKPn3N')

import plotly.graph_objects as go
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dashboard
import re

def fileId_from_url(url):
	raw_fileID = re.findall("~[A-z.]+/[0-9]+", url)[0][1:]
	return raw_fileID.replace('/', ':')

username = 'SYSTEM'
password = '1111'
databaseName = 'localhost/xe'

connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()
#---------------------------------------------------
query = """
SELECT *
    FROM
    (SELECT
         CITY.COUNTRY_CODE, COUNT(INVESTMENT.INVSTID) AS "Number of investments"
    FROM INVESTMENT
        JOIN STARTUP ON INVESTMENT.NAME = STARTUP.NAME
        JOIN CITY ON STARTUP.CITY = CITY.CITY
    GROUP BY
        CITY.COUNTRY_CODE
    ORDER BY
        "Number of investments" DESC
        )
WHERE ROWNUM <= 12
"""
cursor.execute(query)

countries = []
numbers = []

for record in cursor.fetchall():
	countries.append(record[0])
	numbers.append(record[1])

bar = go.Bar(x = countries, y = numbers)
bar_scheme = py.plot([bar], filename = 'country_numbers')

#----------------------------------------------------

query = '''
SELECT
    CITY.STATE_CODE, SUM(STARTUP.TOTAL_FUNDING)  AS "total funding"
FROM CITY
    JOIN STARTUP ON CITY.CITY = STARTUP.CITY
GROUP BY
    CITY.STATE_CODE
ORDER BY
    "total funding" DESC
'''
cursor.execute(query)
states = []
fundings = []

for record in cursor.fetchall():
	states.append(record[0])
	fundings.append(record[1])

pie = go.Pie(labels = states, values = fundings)
pie_scheme = py.plot([pie], filename = 'state_funding')


#---------------------------------------------------------------
query = '''
SELECT
    INVESTMENT.SEED, ROUND(AVG(INVESTMENT.VENTURE)) AS VENTURE
FROM
    INVESTMENT
GROUP BY
    INVESTMENT.SEED
ORDER BY
    INVESTMENT.SEED'''
cursor.execute(query)

seeds = []
ventures = []

for record in cursor.fetchall():
	seeds.append(record[0])
	ventures.append(record[1])

scatter = go.Scatter(
	x= seeds,
	y = ventures
)

data = [scatter]
plot_scheme = py.plot(data, filename = 'seed_ventures')


####

my_board = dashboard.Dashboard()
bar_scheme_id = fileId_from_url(bar_scheme)
pie_scheme_id = fileId_from_url(pie_scheme)
plot_scheme_id = fileId_from_url(plot_scheme)

box_1 = {
	'type' : 'box',
	'boxType' : 'plot',
	'fileId' : bar_scheme_id,
	'title' : 'Запит 1 country_numbers'
}

box_2 = {
	'type' : 'box',
	'boxType' : 'plot',
	'fileId' : pie_scheme_id,
	'title' : 'Запит 2 state_funding'
}

box_3 = {
	'type' : 'box',
	'boxType' : 'plot',
	'fileId' : plot_scheme_id,
	'title' : 'Запит 3 seed_ventures'
}

my_board.insert(box_3)
my_board.insert(box_1, 'right', 1)
my_board.insert(box_2, 'above', 2)

py.dashboard_ops.upload(my_board, 'DB Lab 2 Havryliuk KM-82')