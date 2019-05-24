import pyodbc
import csv

#server = '127.0.0.1'
server = '192.168.1.21'
database = 'Castit'
username = 'prog_jdbc'
password = 'Pr0gIt!'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

castit_cursor = cnxn.cursor()

file = open('Part_Price_by_Customer_Name.csv', 'r')
next(file, None)
reader = csv.reader(file)


for row in reader:
    #print( row[2].rstrip(), row[0].rstrip())
    castit_cursor.execute("insert into part_price(part_number, owned_by) values(?, ?)", row[2].rstrip(), row[0].rstrip())


this = castit_cursor.execute("select part_number, part_name, owned_by from part_price")

for thi in this:
    print(thi[0], thi[1], thi[2])

cnxn.commit()
file.close()
cnxn.close()
