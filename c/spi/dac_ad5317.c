#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

#define SPIDEV "/dev/spidev0.0"

void main(void) {
	int i;
	int ch;
	int f;
	unsigned int word;
	unsigned char buffer[2];

	for(;;) {
		for (i=0;i<1024;i++) {
			for (ch=0;ch<4;ch++) {
				word=(ch<<14)|(i<<2);
				buffer[0]=word>>8;
				buffer[1]=word&0x00FF;
				f = open(SPIDEV,O_WRONLY);
				write(f,buffer,2);
				close(f);
			}
		}
	}
}
