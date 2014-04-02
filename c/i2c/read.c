#include <stdio.h>
#include <fcntl.h>
#include <linux/i2c-dev.h>
#include <errno.h>

#define I2C_ADDR 0x20
 
int main (void) {
	char buffer[1];
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

	buffer[0]=0xFF;
	write(fd, buffer, 1);
	
	read(fd, buffer, 1);
	printf("0x%02X\n", buffer[0]);
	return 0;
}
