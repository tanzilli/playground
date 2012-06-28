// The original version of this watchdog example 
// is available on the Linux Kernel Tree
// linux/Documentation/watchdog/src/watchdog-simple.c 

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main(void)
{
	int ret = 0;
	int i,fd;

	// The watchdog timer starts when /dev/watchdog is open
	printf("Enable the watchdog timer\n");
	printf("Press ctrl-C to simulate a program error\n");

	fd = open("/dev/watchdog", O_WRONLY);

	if (fd == -1) {
		perror("Watchdog disabled.");
		exit(EXIT_FAILURE);
	}

	for (i=0;i<10;i++) {
		printf("Clear the watchdog timer\n");
		ret = write(fd, "\0", 1);
		if (ret != 1) {
			ret = -1;
			break;
		}
		sleep(10);
	}
	printf("Disable the watchdog before exit\n");
	close(fd);
	return ret;
}
