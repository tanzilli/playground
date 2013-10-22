#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"    
#include "fcntl.h"     
#include "mysql/mysql.h" 

#define MYSQL_IP	"10.55.98.234"	// Remote MySQL server IP address
#define MYSQL_USER	"physical"		// MySQL user
#define MYSQL_PSW	"mypassword"	// MySQL password
#define MYSQL_DB	"physical"		// MySQL DB name

#define CREATE_TABLE "CREATE TABLE IF NOT EXISTS events ( \
	id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
	timestamp TIMESTAMP NOT NULL, \
	description VARCHAR(250) NOT NULL);"

MYSQL  *conn;
int fd;

int main (void) 
{
	int i;
	char query[200];

	conn = mysql_init(NULL);
	if (conn == NULL) {
		fprintf (stderr, "mysql_init() failed\n");
		return 1;
	}

	if (mysql_real_connect (conn,MYSQL_IP,MYSQL_USER,MYSQL_PSW,MYSQL_DB,0,NULL,0)==NULL) {
		fprintf (stderr, "mysql_real_connect() failed:\n");
		fprintf (stderr, "Error %u (%s)\n", mysql_errno (conn), mysql_error (conn));
		return 1;
	}

	if (mysql_query (conn, CREATE_TABLE) != 0) {
		printf("CREATE statement failed\n");
		return 1;
	}

	for (i=0;i<10;i++) {
		sprintf(query,"INSERT INTO events (description) VALUES ('This is the record # %d')",i);
		if (mysql_query (conn,query) != 0) {
			printf("INSERT statement failed\n");
			return 1;
		}
	}

	mysql_close(conn);
	return 0;
}

