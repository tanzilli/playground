#!/usr/bin/python
#http://www.acmesystems.it/sqlite

import time
from pysqlite2 import dbapi2 as sqlite
 
connection = sqlite.connect('/root/mydb.sqlite')
cursor = connection.cursor()
cursor.execute('SELECT * FROM tbl1')

for row in cursor:
	print row

connection.commit()
connection.close()
 

