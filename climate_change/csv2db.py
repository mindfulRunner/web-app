# https://www.geeksforgeeks.org/how-to-import-a-csv-file-into-a-sqlite-database-table-using-python/

import csv
import sqlite3
import re

connection = sqlite3.connect('ghg_forum.db')

cursor = connection.cursor()

csv_columns = 'ObjectId,Country,ISO2,ISO3,Indicator,Unit,Source,CTS_Code,CTS_Name,CTS_Full_Descriptor,Industry,Gas_Type,Seasonal_Adjustment,Scale,F2010Q1,F2010Q2,F2010Q3,F2010Q4,F2011Q1,F2011Q2,F2011Q3,F2011Q4,F2012Q1,F2012Q2,F2012Q3,F2012Q4,F2013Q1,F2013Q2,F2013Q3,F2013Q4,F2014Q1,F2014Q2,F2014Q3,F2014Q4,F2015Q1,F2015Q2,F2015Q3,F2015Q4,F2016Q1,F2016Q2,F2016Q3,F2016Q4,F2017Q1,F2017Q2,F2017Q3,F2017Q4,F2018Q1,F2018Q2,F2018Q3,F2018Q4,F2019Q1,F2019Q2,F2019Q3,F2019Q4,F2020Q1,F2020Q2,F2020Q3,F2020Q4,F2021Q1,F2021Q2,F2021Q3,F2021Q4,F2022Q1,F2022Q2,F2022Q3,F2022Q4,F2023Q1,F2023Q2'
# print(csv_columns)

splitted_csv_columns = csv_columns.split(',')
# print(splitted_csv_columns)

csv_column_data_types = ''
for i in range(len(splitted_csv_columns)):
    csv_column = splitted_csv_columns[i]
    csv_column_data_type = ''
    if csv_column == 'ObjectId':
        csv_column_data_type = csv_column + ' INTEGER'
    elif re.match(r"F20\d\dQ\d", csv_column): # https://docs.python.org/3/library/re.html#re.match
        csv_column_data_type = csv_column + ' REAL'
    else:
        csv_column_data_type = csv_column + ' TEXT'
    csv_column_data_type = csv_column_data_type + ' NOT NULL'
    csv_column_data_types += csv_column_data_type
    if i < len(splitted_csv_columns) - 1:
        csv_column_data_types += ',\n'

# print(csv_column_data_types)

# create_table = '''
# CREATE TABLE ghg(
# ObjectId,
# Country TEXT NOT NULL,
# ISO2 TEXT NOT NULL,
# ISO3 TEXT NOT NULL,
# Indicator TEXT NOT NULL,
# Unit TEXT NOT NULL,
# Source TEXT NOT NULL,
# CTS_Code TEXT NOT NULL,
# CTS_Name TEXT NOT NULL,
# CTS_Full_Descriptor TEXT NOT NULL,
# Industry TEXT NOT NULL,
# Gas_Type TEXT NOT NULL,
# Seasonal_Adjustment TEXT NOT NULL,
# Scale TEXT NOT NULL,
# F2010Q1 REAL NOT NULL,
# F2010Q2 REAL NOT NULL,
# F2010Q3 REAL NOT NULL,
# F2010Q4 REAL NOT NULL,
# F2011Q1 REAL NOT NULL,
# F2011Q2 REAL NOT NULL,
# F2011Q3 REAL NOT NULL,
# F2011Q4 REAL NOT NULL,
# F2012Q1 REAL NOT NULL,
# F2012Q2 REAL NOT NULL,
# F2012Q3 REAL NOT NULL,
# F2012Q4 REAL NOT NULL,
# F2013Q1 REAL NOT NULL,
# F2013Q2 REAL NOT NULL,
# F2013Q3 REAL NOT NULL,
# F2013Q4 REAL NOT NULL,
# F2014Q1 REAL NOT NULL,
# F2014Q2,F2014Q3,F2014Q4,F2015Q1,F2015Q2,F2015Q3,F2015Q4,F2016Q1,F2016Q2,F2016Q3,F2016Q4,F2017Q1,F2017Q2,F2017Q3,F2017Q4,F2018Q1,F2018Q2,F2018Q3,F2018Q4,F2019Q1,F2019Q2,F2019Q3,F2019Q4,F2020Q1,F2020Q2,F2020Q3,F2020Q4,F2021Q1,F2021Q2,F2021Q3,F2021Q4,F2022Q1,F2022Q2,F2022Q3,F2022Q4,F2023Q1,F2023Q2
# );

# '''

create_table = 'CREATE TABLE ghg(\n' + csv_column_data_types + ');'

print(create_table)

cursor.execute(create_table)

file = open('db/Quarterly_Greenhouse_Gas_(GHG)_Air_Emissions_Accounts.csv')

contents = csv.reader(file)

question_marks = ['?'] * len(splitted_csv_columns)
questions = ','.join(question_marks)
# print(questions)

insert_records = 'INSERT INTO ghg(' + csv_columns + ') VALUES (' +  questions + ')'

cursor.executemany(insert_records, contents)

select_records = 'SELECT * FROM ghg'

rows = cursor.execute(select_records).fetchall()

# for row in rows:
#     print(row)

connection.commit()
connection.close()
