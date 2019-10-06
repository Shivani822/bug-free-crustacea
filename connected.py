import mysql.connector
import datetime
from PIL import Image

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="owner"

)

#print(mydb)

mycursor = mydb.cursor()
'''
mycursor.execute("CREATE DATABASE owner")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

mycursor.execute("CREATE TABLE vehicle_info(nameplate VARCHAR(10), address VARCHAR(255))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

sql="INSERT INTO ovehicle(nameplate,address) VALUES (%s,%s )"
s=("MP09UP19500","Navlakha Indore")
mycursor.execute(sql, s)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM ovehicle")
result=mycursor.fetchall()
for x in result:
  print(x)

mycursor.execute("SHOW COLUMNS FROM vehicle_info")
re=mycursor.fetchall()
for x in re:
  print(x)

x = datetime.datetime.now()
print(x)
'''