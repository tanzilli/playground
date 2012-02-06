#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"    
#include "fcntl.h"     
#include "mysql/mysql.h" 

#define MYSQL_IP	"10.55.98.234"  // Remote MySQL server IP address
#define MYSQL_USER	"fox"           // MySQL user
#define MYSQL_PSW	"acme"          // MySQL password
#define MYSQL_DB	"foxlogger"		// MySQL DB name


MYSQL  *conn;
int fd;

int main (void) 
{
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

	if (mysql_query (conn, "INSERT INTO events (info) VALUES ('Hello')") != 0) {
		printf("INSERT statement failed\n");
		return 1;
	} else {
		printf ("INSERT statement succeeded: %lu rows affected\n",(unsigned long) mysql_affected_rows (conn));
	}

	mysql_close(conn);
	return 0;
}

