#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

int gpioexport(int gpioid) 
{
	FILE *filestream;

	if ((filestream=fopen("/sys/class/gpio/export","w"))==NULL) {
		printf("Error on export GPIO\n");
		return -1;
	}	
	fprintf(filestream,"%d",gpioid);
	fclose(filestream);
	return 0;
}

int gpiosetdir(int gpioid,char *mode) 
{
	FILE *filestream;
	char filename[50];

	sprintf(filename,"/sys/class/gpio/gpio%d/direction",gpioid);
	if ((filestream=fopen(filename,"w"))==NULL) {
		printf("Error on direction setup\n");
		return -1;
	}	
	fprintf(filestream,mode);
	fclose(filestream);
	return 0;
}

int gpiogetbits(int gpioid) 
{
	FILE *filestream;
	char filename[50];
	char retchar;

	sprintf(filename,"/sys/class/gpio/gpio%d/value",gpioid);
	if ((filestream=fopen(filename,"r"))==NULL) {
		printf("Error on gpiogetbits %d\n",gpioid);
		return -1;
	}	
	retchar=fgetc(filestream);
	fclose(filestream);
	if (retchar=='0') return 0;
	else return 1;
}

int gpiosetbits(int gpioid) 
{
	FILE *filestream;
	char filename[50];

	sprintf(filename,"/sys/class/gpio/gpio%d/value",gpioid);
	if ((filestream=fopen(filename,"w"))==NULL) {
		printf("Error on setbits %d\n",gpioid);
		return -1;
	}	
	fprintf(filestream,"1");
	fclose(filestream);
	return 0;
}

int gpioclearbits(int gpioid) 
{
	FILE *filestream;
	char filename[50];

	sprintf(filename,"/sys/class/gpio/gpio%d/value",gpioid);
	if ((filestream=fopen(filename,"w"))==NULL) {
		printf("Error on clearbits %d\n",gpioid);
		return -1;
	}	
	fprintf(filestream,"0");
	fclose(filestream);
	return 0;
}

int main(void) 
{
	int led = 82;
	
	gpioexport(led);
	gpiosetdir(led,"out");
	for (;;) {
		gpiosetbits(led);
		sleep(1);
		gpioclearbits(led);
		sleep(1);
	}
}

