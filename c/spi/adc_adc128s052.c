#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

void main(void) {
	int f;
	unsigned char ch;
	unsigned char buffer[2];
	unsigned int value;

	for (;;) { 
		for(ch=0;ch<8;ch++) {
			f = open("/dev/spidev0.0",O_RDWR);
			buffer[0]=ch<<3;
			buffer[1]=0;
			write(f,buffer,2);
			read(f,buffer,2);
			value=buffer[0]<<8|buffer[1];
			close(f);
			printf("[%d]=%05d ",ch,value);
		}
		printf("\n");
	}	
}
