import time
import sqlite3
 
connection = sqlite3.connect('events.sqlite')
cursor = connection.cursor()
cursor.execute("SELECT strftime('%d/%m/%Y %H:%M:%S',timestamp),description FROM events;")

for row in cursor:
	print "  Timestamp:",row[0]
	print "Description:",row[1]
	print " "	

connection.commit()
connection.close()
