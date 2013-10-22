import time
import sqlite3
 
connection = sqlite3.connect('events.sqlite')
cursor = connection.cursor()
cursor.execute('SELECT * FROM events;')

for row in cursor:
	print row

connection.commit()
connection.close()
