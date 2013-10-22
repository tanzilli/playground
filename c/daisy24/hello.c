#include <stdio.h>
#include <fcntl.h>
#include <linux/i2c-dev.h>
#include <errno.h>
#include <string.h>


#define I2C_ADDR 0x3E

// mode
// 0 = command
// 1 = data

int lcdsend(int fd,int mode,unsigned char value) {
	unsigned char buffer[2];

	if (mode==0) {	
		buffer[0]=0x00;		
	} else {
		buffer[0]=0x40;		
	}
	buffer[1]=value;		
	if (write(fd,buffer,2)!=2) {
		printf("Error writing file: %s\n", strerror(errno));
		return -1;
	}
	usleep(1000);
	return 0;
}

int lcdclear(int fd) {
	lcdsend(fd,0,0x01);
	return 0;
}

int lcdsetcurpos(int fd, int x, int y) {
	if (y<0 || y>1) return -1;
	if (x<0 || x>15) return -1;

	if (y==0) lcdsend(fd,0,0x80+0x00+x);
	else lcdsend(fd,0,0x80+0x40+x);
	return 0;
}

int lcdputchar(int fd, char value) {
	lcdsend(fd,1,value);
	return 0;
}

int lcdputstring(int fd,char *string) {
	int i;
	
	if (strlen(string)==0) return -1;
	if (strlen(string)>16) {
		sprintf(string,"%16s",string);
	}

	for (i=0;i<strlen(string);i++) {
		lcdputchar(fd,string[i]);
	}
	return 0;
}

 
int main (void) {
	int value;
	int fd;
	int i;	
	char stringa[32+1];	

	fd = open("/dev/i2c-0", O_RDWR);

	if (fd < 0) {
		printf("Error opening file: %s\n", strerror(errno));
		return 1;
	}

	if (ioctl(fd, I2C_SLAVE, I2C_ADDR) < 0) {
		printf("ioctl error: %s\n", strerror(errno));
		return 1;
	}

	lcdsend(fd,0,0x38);
	lcdsend(fd,0,0x39);
	lcdsend(fd,0,0x14); //Internal OSC freq
	lcdsend(fd,0,0x72); //Set contrast 
	lcdsend(fd,0,0x54); //Power/ICON control/Contrast set
	lcdsend(fd,0,0x6F); //Follower control
	lcdsend(fd,0,0x0C); //Display ON
	lcdclear(fd);	

	lcdputstring(fd,"Hello World !");

	for (i=0;;i++) {
		lcdsetcurpos(fd,0,1);
		sprintf(stringa,"%08d",i);
		lcdputstring(fd,stringa);
	}

	return 0;
}

