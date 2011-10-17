#include "sensirion.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


static int verbose = 0;
static const char * version_str = "1.02 20090128";

void usage(void)
{
    fprintf(stderr, "Usage: "
            "sht_test [-h] [-r] [-v] [-V]\n"
            "  where:\n"
            "    -h       print usage message\n"
            "    -r       send reset to SHT before fetching info\n"
            "    -v       increase verbosity (more written to log)\n"
            "    -V       print version string then exit\n\n"
            "Test Sensirion SHT-71, CLK=(I)OG%d DATA=IOG%d\n", CLOCK_BIT,
            DATA_BIT);
}


#if 0
	// Output loop example

	gpioexport(85);
	gpiosetdir(85,GPIO_OUT);
	for (;;) {
		gpiosetbits(85);
		gpioclearbits(85);
	}
#endif

#if 0
	// Line input example

	gpioexport(84);
	for (;;) {
		printf("%d\n",gpiogetbits(84));
	}
#endif


// ----------
// main code
// ----------

int main(int argc, char ** argv) 
{
	int opt, soh, sot;
	int do_reset = 0;
	float rel_humidity, temperature_c;

	gpioexport(DATA_BIT);
	gpioexport(CLOCK_BIT);
	gpiosetdir(CLOCK_BIT,GPIO_OUT);
	gpiosetdir(DATA_BIT,GPIO_IN);

	while ((opt = getopt(argc, argv, "hrvV")) != -1) {
		switch (opt) {
		case 'h':
		    usage();
		    exit(EXIT_SUCCESS);
		case 'r':
		    ++do_reset;
		    break;
		case 'v':
		    ++verbose;
		    break;
		case 'V':
		    printf("%s\n", version_str);
		    exit(EXIT_SUCCESS);
		default: /* '?' */
		    usage();
		    exit(EXIT_FAILURE);
		}
	}

	if (optind < argc) {
		if (optind < argc) {
			for (;optind < argc;++optind)
				fprintf(stderr, "Unexpected extra argument: %s\n",argv[optind]);
			usage();
			exit(EXIT_FAILURE);
		}
	}

	if (verbose)
		fprintf(stderr, "%s: Clock line ID=%d, Data line ID=%d\n",__FILE__ ,CLOCK_BIT, DATA_BIT);

	if (do_reset > 0) SendReset();

	// assume 12 bit (rather than 8 bit) accuracy
	soh = ReadHumidity();
	sot = ReadTemperature();
	if (verbose) fprintf(stderr, "soh=%d [0x%x]  sot=%d [0x%x]\n", soh, soh,  sot, sot);

#if 1
	// new formula from SHT7x version 4.1 datasheet
	rel_humidity = -2.0468 + (0.0367 * soh) + (-1.5955E-6 * soh * soh);
#else
	// older formula
	rel_humidity = -4 + (0.0405 * soh) + -2.8E-6;
#endif

	if (rel_humidity > 99.9)
		rel_humidity = 100.0;
	else if (rel_humidity < 0.1)
		rel_humidity = 0.0;

	temperature_c = -39.66 + (0.01 * sot);
	printf ("Rel. Humidity: %.2f %%\n", rel_humidity);
	printf ("Temperature  : %.2f C\n", temperature_c);
	return 0;
}


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

int gpiosetdir(int gpioid,int mode) 
{
	FILE *filestream;
	char filename[50];

	sprintf(filename,"/sys/class/gpio/gpio%d/direction",gpioid);
	if ((filestream=fopen(filename,"w"))==NULL) {
		printf("Error on direction setup\n");
		return -1;
	}	
	if (mode==GPIO_IN) {
		fprintf(filestream,"in");
	} else {
		fprintf(filestream,"out");
	}
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

void SendStart(void)
{
	// Invia la sequenza di inizializzazione sul bus I2C
	DATA_LINE_OUT;

	CLOCK_LINE_HIGH;
	usleep(1000);
	DATA_LINE_IN;
	DATA_LINE_LOW;
	CLOCK_LINE_LOW;
	CLOCK_LINE_HIGH;
	usleep(1000);
	DATA_LINE_HIGH;
	CLOCK_LINE_LOW;
	DATA_LINE_IN;
}

void SendReset(void)
{
	// Resetta il Sensore
	int i;

	for (i=0; i<12; i++) {
		CLOCK_LINE_HIGH;
		usleep(1000);
		CLOCK_LINE_LOW;
	}
}

static int SendByte(unsigned char byte)
{
	// Invia un byte al sensore
	unsigned char tempbyte;
	int i;

	DATA_LINE_OUT;
	tempbyte=byte;

	for (i=0x80; i>0; i/=2)	{
		if (tempbyte & i) DATA_LINE_HIGH;
		else DATA_LINE_LOW;

		CLOCK_LINE_HIGH;
		usleep(1000);
		CLOCK_LINE_LOW;
	}

	DATA_LINE_IN;
	CLOCK_LINE_HIGH;
	CLOCK_LINE_LOW;
	return 1;
}

static unsigned char ReadByte(int withack)
{
  // Legge un byte dal sensore e invia un ack
  // withack
  //   1 = ACK inviato
  //   0 = ACK non inviato

  unsigned char tempbyte;
  int i;

  tempbyte=0;
  DATA_LINE_IN;

  for (i=0x80;i>0;i/=2)
    {
      CLOCK_LINE_HIGH;
      if (DATA_LINE_READ) tempbyte |=i;
      CLOCK_LINE_LOW;
    }

  if (withack)
    {
      // ACK del byte
      DATA_LINE_OUT;
      DATA_LINE_LOW;
      CLOCK_LINE_HIGH;
      CLOCK_LINE_LOW;
      DATA_LINE_IN;
    } else
    {
      // Senza ACK
      DATA_LINE_OUT;
      DATA_LINE_HIGH;
      CLOCK_LINE_HIGH;
      CLOCK_LINE_LOW;
      DATA_LINE_IN;
    }
  
  return tempbyte;
}

static int ReadTemperature(void)
{
	// Legge la temperatura

	unsigned char Lsb,Msb,Chk;

	SendStart();
	if (!SendByte(CMD_READ_TEMP)) return 0;
	while (DATA_LINE_READ);
	Msb=ReadByte(1);
	Lsb=ReadByte(1);
	Chk=ReadByte(0);


	return((Msb<<8)+Lsb);
}

static int ReadHumidity(void)
{
	unsigned char Lsb,Msb,Chk;

	SendStart();
	if (!SendByte(CMD_READ_HUM)) return 0;
	while (DATA_LINE_READ);
	Msb=ReadByte(1);
	Lsb=ReadByte(1);
	Chk=ReadByte(0);

	return((Msb<<8)+Lsb);
}
  


