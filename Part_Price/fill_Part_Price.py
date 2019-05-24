import pyodbc


#server = '127.0.0.1'
server = '192.168.1.21'
database = 'Castit'
username = 'prog_jdbc'
password = 'Pr0gIt!'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

castit_cursor = cnxn.cursor()
cnxn.cursor()

parts_from_as400 = castit_cursor.execute("select customerno, part_number from part_number_by_customer_name").fetchall()

#parts_from_pp = castit_cursor.execute("select part_number from part_price").fetchall()

as400_but_not_Castit = castit_cursor.execute("select part_number, customerno from Part_Number_by_Customer_Name where part_number not in (select part_number from part_price)").fetchall()

'''
count = 0

for row in as400_but_not_Castit:
   print(row)
   count = count + 1

print("There are ", count, " parts in the as400.")
count = 0

for row in as400_but_not_Castit:
        count = count + 1

print("There are ", count, " parts in the as400 but not in the parts_price on Castit.")
'''

for row in as400_but_not_Castit:
   castit_cursor.execute("insert into part_price(part_number, owned_by, enduse_code) values(?, ?, ?)", row[0].rstrip(), row[1].rstrip(), '1234')
   #print(row[0].rstrip(), row[1].rstrip(), '1234')
cnxn.commit()
