import time
import sqlite3
 
connection = sqlite3.connect('mydb.sqlite')
cursor = connection.cursor()
cursor.execute('SELECT * FROM tbl1')

for row in cursor:
	print row

connection.commit()
connection.close()
