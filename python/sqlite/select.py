#!/usr/bin/python
import time
from pysqlite2 import dbapi2 as sqlite
 
# Insert a new record for this sample on the SQLite database
 
connection = sqlite.connect('/root/mydb.sqlite')
cursor = connection.cursor()
cursor.execute('SELECT * FROM tbl1')
connection.commit()
 

