import MySQLdb

db=MySQLdb.connect(host="127.0.0.1",port=3306,db="mydb",user="root",passwd="ariag25")

cur = db.cursor()
cur.execute("SELECT * FROM addressbook;")

rows = cur.fetchall()

for row in rows:
	print row
