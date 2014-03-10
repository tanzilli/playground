#include <stdio.h>
#include <fcntl.h>
#include <linux/i2c-dev.h>
#include <errno.h>

#define I2C_ADDR 0x27 // PCF8574T
//#define I2C_ADDR 0x3F	// PCF8574AT

int expsend(int fd,unsigned char value) {
	unsigned char buffer[2];
	
	buffer[0]=value;		
	if (write(fd,buffer,1)!=1) {
		printf("Error writing file: %s\n", strerror(errno));
		return -1;
	}
	return 0;
}

int main (void) {
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

	for (;;) {
		expsend(fd,0x10); //Backlight OFF
		usleep(1000000);
		expsend(fd,0); //Backlight ON
		usleep(1000000);
	}

	return 0;
}

