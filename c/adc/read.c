// Read the voltage values from the 
// built-in ADC
// http://www.acmesystems.it/?id=foxg20_adc

#include "stdio.h"
#include "stdlib.h"
#include "fcntl.h"
#include "unistd.h"
#include "sys/types.h"
#include "sys/stat.h"
#include "sys/ioctl.h"
#include "math.h"

#define ADC_SYSFS "/sys/bus/platform/devices/at91_adc/chan"
#define VREF 3.24
#define V_PER_POINT VREF/2**10

int ADC_Read(int channel){
	int fd,rtc;
	char filename[41];
	char buffer[5];

	sprintf(filename,"%s%d",ADC_SYSFS,channel);

	if ((fd=open(filename,O_RDONLY))<0) return -1;

	read(fd,buffer,5);
	rtc = atoi(buffer);
	close(fd);

	return rtc;
}


void main(void) {
	int channel;

	while(1) {
		for (channel=0;channel<4;channel++) {
			printf("Channel %d = %.2f\n",channel,(float)ADC_Read(channel)*VREF/pow(2,10));
		}
		printf("-------\n");
		sleep(1);
	} 

}
