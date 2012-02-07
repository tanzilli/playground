import _mysql

db=_mysql.connect(host="10.55.98.234",db="physical",user="physical",passwd="mypassword")

db.query("""	CREATE TABLE IF NOT EXISTS events (
	id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	timestamp TIMESTAMP NOT NULL,
	description VARCHAR(250) NOT NULL);""")

for i in range(10):
	db.query("INSERT INTO events (description) VALUES ('This is the record # %d')" % i)

print "Terminated"
