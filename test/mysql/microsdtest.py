import MySQLdb
import time

db=MySQLdb.connect(host="127.0.0.1",port=3306,db="mydb",user="root",passwd="ariag25")
cur = db.cursor()

while True:
	for i in range (0,10):
		query="INSERT INTO microsdtest (field1,field2) VALUES ('Field 1 Record %d','Field 2 Record %d');" % (i,i)
		cur.execute(query)
		db.commit()

	query="DELETE FROM microsdtest LIMIT 9;"
	cur.execute(query)
	db.commit()
	
	


