#include "mysql/mysql.h"
#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"    
#include "fcntl.h"  

int main(int argc, char **argv)
{
	MYSQL *conn;
	MYSQL_RES *result;
	MYSQL_ROW row;
	int num_fields;
	int i;

	if ((conn = mysql_init(NULL))==NULL) {
		fprintf(stderr, "Failed on mysql_init()\n");
		exit(1);
	}

	if (mysql_real_connect(conn, "127.0.0.1", "root", "ariag25", "mydb", 3306, NULL, 0)==NULL) {
		fprintf(stderr, "Failed to connect to database: Error: %s\n", mysql_error(conn));
		exit(1);
	}

	if (mysql_query(conn, "SELECT * FROM addressbook")!=0) {
		fprintf(stderr, "Failed on SQL Query: %s\n", mysql_error(conn));
		exit(1);
	}

	result = mysql_store_result(conn);

	num_fields = mysql_num_fields(result);

	while ((row = mysql_fetch_row(result))) {
		for(i = 0; i < num_fields; i++) {
			printf("%s ", row[i] ? row[i] : "NULL");
		}
		printf("\n");
	}
	mysql_free_result(result);
	mysql_close(conn);
	exit(0);
}
