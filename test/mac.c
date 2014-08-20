#include <stdio.h>
#include <fcntl.h>
#include <linux/i2c-dev.h>
#include <errno.h>
 
#define I2C_ADDR 0x58
 
int main (void) {
	char buffer[20];
	int fd;
	int i;

	fd = open("/dev/i2c-0", O_RDWR);

	if (fd < 0) {
		printf("Error opening file: %s\n", strerror(errno));
		return 1;
	}

	if (ioctl(fd, I2C_SLAVE, I2C_ADDR) < 0) {
		printf("ioctl error: %s\n", strerror(errno));
		return 1;
	}

	buffer[0]=0x80;
	if (write(fd, buffer, 1) != 1) {
		printf("Error writing file: %s\n", strerror(errno));
	}

	if (ioctl(fd, I2C_SLAVE, I2C_ADDR) < 0) {
		printf("ioctl error: %s\n", strerror(errno));
		return 1;
	}

	read(fd, buffer, 16);
	
	for (i=0;i<16;i++) {
		printf("%02X ",buffer[i]);
	}
	printf("\n");
	
	usleep(100000);
	close(fd);

/*
	read(fd, buffer, 6);
	printf("0x%02X\n", buffer[0]);
	*/
	return 0;
}	
