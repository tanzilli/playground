#include <stdio.h>
#include <fcntl.h>
#include <linux/i2c-dev.h>
#include <errno.h>


#define I2C_ADDR 0x20
 
int main (void) {
	char value;
	int fd;

	fd = open("/dev/i2c-0", O_RDWR);

	if (fd < 0) {
		printf("Error opening file: %s\n", strerror(errno));
		return 1;
	}

	if (ioctl(fd, I2C_SLAVE, I2C_ADDR) < 0) {
		printf("ioctl error: %s\n", strerror(errno));
		return 1;
	}

	for (value=0; value<=255; value++) {
		if (write(fd, &value, 1) != 1) {
			printf("Error writing file: %s\n", strerror(errno));
		}
		usleep(100000);
	}
	return 0;
}

