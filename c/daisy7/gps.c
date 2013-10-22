/*! \file gps.c
 
Copyright (c) 2005, David M Howard (daveh at dmh2000.com)
All rights reserved.

This product is licensed for use and distribution under the BSD Open Source License.
see the file COPYING for more details.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, 
OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT 
OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE 
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, 
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. 

*/

        

#include"gps.h"

static char nmeaStringBuffer[NMEA_STRING_LENGTH];
char GPS_logBuffer[500];		/*!< buffer di caratteri usato per stampare su console i messaggi  */


static char* pvect;
static nmeap_context_t nmea;	   	/*!< parser context */
static nmeap_gga_t     gga;		/*!< this is where the data from GGA messages will show up */
static nmeap_rmc_t     rmc;		/*!< this is where the data from RMC messages will show up */
static int             user_data; 	/*!< user can pass in anything. typically it will be a pointer to some user data */
static char nmeaBuffer[NMEA_BUFFER_LENGTH + 1];	/*!< buffer per contenere lo streming NMEA dal GPS */
int    wrongSentencesCounter = 0;


NavInputs_t read_nav_data()
{
return gpsData;
}


//-----------------------------------------------------------------
/*! \brief This routine will read the char buffer pointed by (static)pvect pointer verifying the end of the string ('\0') 

 \param  char*		: the pointer to the character of the buffer to be read
 \return 0=the value contained in ch is a valid character value, -1= end of the buffer string	

\note -.

*/
int readchar(char *ch) 
{
    if (*pvect == '\0') {
        return -1;
    }
    else {
        *ch = *pvect++;
    }
    return 0;
}


//-----------------------------------------------------------------
/*! \brief This routine will print the GGA loaded fields 

 \param  nmeap_gga_t *gga	: the pointer to the loaded NMEA_GGA structure
 \return none.

\note -.
*/

 void print_gga(nmeap_gga_t *gga)
{
    #if (GPS_DEBUG)	
    sprintf(GPS_logBuffer, "found GPGGA message %.6f %.6f %.0f %lu %d %d %f %f\n",
            gga->latitude  ,
            gga->longitude, 
            gga->altitude , 
            gga->time     , 
            gga->satellites,
            gga->quality   ,
            gga->hdop      ,
            gga->geoid     
            );
   
    #endif
}	

/** called when a gpgga message is received and parsed */
//-----------------------------------------------------------------
/*! \brief This routine will call the print_gga() routine 

 \param  nmeap_context_t *context	: the pointer to the context structure
 \param  void *data			: the pointer to the data
 \param  void *user_data		: the pointer to the user data structure (if there is one)
 \return none.

\note -.
*/
 void gpgga_callout(nmeap_context_t *context,void *data,void *user_data)
{
    nmeap_gga_t *gga = (nmeap_gga_t *)data;
    
    //printf("-------------callout\n");
    print_gga(gga);
}

//-----------------------------------------------------------------
/*! \brief This routine will print the RMC loaded fields 

 \param  nmeap_rmc_t *rmc	: the pointer to the loaded NMEA_RMC structure
 \return none.

\note -.
*/
 void print_rmc(nmeap_rmc_t *rmc)
{
     #if (GPS_DEBUG)
    sprintf(GPS_logBuffer, "found GPRMC string %lu %c %.6f %.6f %f %f %lu %f\n",
            rmc->time,
            rmc->warn,
            rmc->latitude,
            rmc->longitude,
            rmc->speed,
            rmc->course,
            rmc->date,
            rmc->magvar
            );
    ConsoleLog (GPS, GPS_logBuffer, INFO);
    #endif
}

/** called when a gprmc message is received and parsed */
//-----------------------------------------------------------------
/*! \brief This routine will call the print_rmc() routine 

 \param  nmeap_context_t *context	: the pointer to the context structure
 \param  void *data			: the pointer to the data
 \param  void *user_data		: the pointer to the user data structure (if there is one)
 \return none.

\note -.
*/
 void gprmc_callout(nmeap_context_t *context,void *data,void *user_data)
{
    nmeap_rmc_t *rmc = (nmeap_rmc_t *)data;
    
    //printf("-------------callout\n");
    print_rmc(rmc);
}

//-----------------------------------------------------------------
/*! \brief This routine will get the GPS data from the GGA/RMC NMEA Strings 

 \param  char *nmeaString	: the pointer to the NMEA string buffer
 \return 0=OK, -1=string with problems.

\note -.
*/

int parseNMEAString(char *nmeaString)
{
    int 	status;
    int 	result = GPS_NO_ERRORS;
    char        ch;
    unsigned int 	done = FALSEG;
           
    pvect = nmeaString;
    
	/* ---------------------------------------*/
	/*STEP 2 : initialize the nmea context    */                                                
	/* ---------------------------------------*/
    //printf("initialize the nmea context\n");
    status = nmeap_init(&nmea,(void *)&user_data);
    if (status != 0) {
        printf("nmeap_init %d\n",status);
        goto parseNMEAString_EXIT;
    }
    
	/* ---------------------------------------*/
	/*STEP 3 : add standard GPGGA parser      */                                                
	/* -------------------------------------- */
    //printf("add standard GPGGA parser\n");
    status = nmeap_addParser(&nmea,"GPGGA",nmeap_gpgga,gpgga_callout,&gga);
    if (status != 0) {
        printf("nmeap_add %d\n",status);
        goto parseNMEAString_EXIT;
    }

	/* ---------------------------------------*/
	/*STEP 4 : add standard GPRMC parser      */                                                
	/* -------------------------------------- */
    //printf("add standard GPRMC parser\n");	
    status = nmeap_addParser(&nmea,"GPRMC",nmeap_gprmc,gprmc_callout,&rmc);
    if (status != 0) {
        printf("nmeap_add %d\n",status);
        goto parseNMEAString_EXIT;
    }
    
	/* ---------------------------------------*/
	/*STEP 5 : process input until done       */                                                
	/* -------------------------------------- */
    //printf("process input string until done       \n");		
    for(;;) 
    {
	/* ---------------------------------------*/
	/*STEP 6 : get a byte at a time           */                                                
	/* -------------------------------------- */
	//printf(" get a byte at a time. ");	
        result = readchar((char*)&ch);
        if (result < 0) {
        	goto parseNMEAString_EXIT;
           	break;
        }
        //printf ("Il carattere letto e':  ----->  %c\n", ch);
        
	/* --------------------------------------- */
	/*STEP 7 : pass it to the parser           */
	/* status indicates whether a complete msg */
	/* arrived for this byte                   */
	/* NOTE : in addition to the return status */
	/* the message callout will be fired when  */
	/* a complete message is processed         */
	/* --------------------------------------- */

        status = nmeap_parse(&nmea,ch);
        
	/* ---------------------------------------*/
	/*STEP 8 : process the return code        */                                                
	/* -------------------------------------- */

        switch(status) {
        case NMEAP_GPGGA:
	    /* GOT A GPGGA MESSAGE */
            //printf("-------------switch\n");
            //print_gga(&gga);
            //printf("-------------\n");
            
            gpsData.lat = gga.latitude;
            gpsData.lon = gga.longitude; 
            gpsData.heigth = gga.altitude;
            gpsData.gpsFixQuality = gga.quality;
            done = TRUEG;
            break;
        case NMEAP_GPRMC:
	    /* GOT A GPRMC MESSAGE */
            //printf("-------------switch\n");
            //print_rmc(&rmc);
            //printf("-------------\n");
            
            gpsData.lat = rmc.latitude;
            gpsData.lon = rmc.longitude; 
            gpsData.heigth = 0.0; 
            //gpsData.speed	= rmc.speed * 0.51F;  // Speed over the ground in [knots] converted in [m/s]
            gpsData.speed	= rmc.speed;  // Speed over the ground in [knots]
            if (rmc.warn == 'A')				// Status A=active or V=Void.
            {
           	 gpsData.gpsFixQuality = 1;
            }
            else
            {
            	 gpsData.gpsFixQuality = 0;
            }
            done = TRUEG;
            break;
        case WRONG_CHEKCSUM:
            printf("NMEA sentence with Wrong CheckSum!\n");
            done = TRUEG;
            break;
            
        default:
            //printf("*");
            break;
        }
        
        if (done == TRUEG) {
        	if (status == WRONG_CHEKCSUM)	
        		result = GPS_WRONG_CHECKSUM;
        	else
        		result = GPS_NO_ERRORS;
        	break;  
        }      
    }// for(;;)
    
    return result;
    
    parseNMEAString_EXIT:    
    return GPS_PARSER_ERROR;
}



void clearNMEABuffer()
{
	int i = 0;
	for (i=0;i<NMEA_BUFFER_LENGTH;i++)
	{ 
		nmeaBuffer[i] = '\0';
	}
}


void clearNMEAStringBuffer()
{
	int i = 0;
	for (i=0;i<NMEA_STRING_LENGTH;i++)
	{ 
		nmeaStringBuffer[i] = '\0';
	}	
}

//-----------------------------------------------------------------
/*! \brief This routine will get the GPS user position and it manages the GPS NMEA streaming 

 \param  [GLOBAL] fd	: GPS COM port handle
 \param  [GLOBAL] gpsData	: GPS structure with lat, lon, heigth, ...
 \return :
	GPS_UNABLE_TO_READ_SERIAL
	GPS_UNABLE_TO_GET_POSITION
	GPS_WAITING_FOR_LOCK
	GPS_NO_ERRORS
\note - .

*/

int getUserPosition(int fd)
{
	clearNMEABuffer();
	clearNMEAStringBuffer();
			
	
	int result = 0;					
	nmeaBuffer[NMEA_BUFFER_LENGTH] = '\0';		/*!< termino la stringa con il carattere fine stringa 0x00.


	/* leggo dallo streaming seriale della porta COM2 */
	#if (GPS_DEBUG)
	printf("Reading GPS Serial port.....");
	#endif
	
	result = read(fd, nmeaBuffer, NMEA_BUFFER_LENGTH);
					
	if (result <= 0) {
		printf("Unable to read NMEA streaming from GPS serial.");
		return GPS_UNABLE_TO_READ_SERIAL;
	}	
	tcflush(fd, TCIFLUSH);
	tcflow(fd, TCION); 
	
	result = searchCompleteNMEAString(&nmeaBuffer[0]);		
	if (result == GPS_NO_ERRORS)
	{		
		#if (GPS_DEBUG)
		printf("Found a valid NMEA string....");
		#endif
		
		result = parseNMEAString(nmeaStringBuffer);
					
		#if (BLIND_TEST)
		result = GPS_NO_ERRORS;	
		gpsData.gpsFixQuality = 1;
		#endif			
		
		if (result != GPS_NO_ERRORS)	{
			wrongSentencesCounter++;
		}
		else	{
			wrongSentencesCounter = 0;
			if (gpsData.gpsFixQuality == 0)	{
				#if (GPS_DEBUG)
				printf("Waiting for GPS Service/Satellite lock.....");	
				#endif
				result = GPS_WAITING_FOR_LOCK;
			}
		}	
	}
	else	{
		printf( "NMEA searching string failed!\n");	
		wrongSentencesCounter++;
	}
	
	if (wrongSentencesCounter >= MAX_NMEA_GPSWRONG_SENTENCES)
	{
		printf( "Error during NMEA parsing or CheckSum Error.\n");	
		result = GPS_UNABLE_TO_GET_POSITION;
	}
	tcflow(fd, TCIOFF);
	
	return result;	
}



int searchCompleteNMEAString (char* nmeaBuffer)
{

	int i = 0;
	int kk = 0;
	char *p1;		// puntatore per scorrere tutto l' nmeaBuffer
	char *p2;		// puntatore per scorrere l' nmeaBuffer dopo il carattere $ e recuperare il tipo di stringa NMEA (5 caratteri) e salvarla nella stringa char NMEA_TYPE[]
	char NMEA_TYPE[6] = ""; // contiene il tipo di stringa NMEA (p.e. GPGGA, GPRMC, ....)
	p1 = nmeaBuffer;
	
	int NMEAStartFound = 0;
	int NMEACheckSumFound = 0;
	int checkSumDigits = 0;
	
	for (i=0;i<NMEA_BUFFER_LENGTH;i++)
	{
		//printf("%c\n", *p1);
		switch(*p1) 
		{
    		case '$':
    		
			NMEA_TYPE[0] = 0;
    			NMEA_TYPE[1] = 0;
    			NMEA_TYPE[2] = 0;    			
    			NMEA_TYPE[3] = 0;    			
    			NMEA_TYPE[4] = 0;  
    			NMEA_TYPE[5] = 0;  
    			// imposto il puntatore p2 per scorrere il buffer senza perdere la posizione attuale.
    			p2=p1;	// p2 ora punta al carattere "$"
    			// carico il tipo di stringa NMEA dopo il carattere "$"
    			p2++;
    			NMEA_TYPE[0] = *p2;
    			p2++;
    			NMEA_TYPE[1] = *p2;
    			p2++;
    			NMEA_TYPE[2] = *p2;    			
    			p2++;
    			NMEA_TYPE[3] = *p2;    			
    			p2++;
    			NMEA_TYPE[4] = *p2;  
    			
    			#if (GPS_DEBUG)
    			sprintf (NMEA_TYPE, "%s%c", NMEA_TYPE, '\0');    			
    			printf ("NMEA_TYPE IS : --> %s\n", NMEA_TYPE);
    			#endif
    			if ( ( strcmp(NMEA_TYPE, "GPGGA") == 0) || (strcmp(NMEA_TYPE, "GPRMC") == 0) )
    			//if (strcmp(NMEA_TYPE, "GPRMC") == 0)
    			{  			    			
    				NMEAStartFound = 1;
    			}
    			break;
    		
    		case '*':
    			if(NMEAStartFound)
    			{
    				NMEACheckSumFound = 1;
    			}
    			break;
    		}
		
		if(NMEAStartFound)
		{
			nmeaStringBuffer[kk] = *p1;
			//printf ("%c", nmeaStringBuffer[kk]);
			kk++;			
		}			
	  
	  if(NMEACheckSumFound)
		{
			checkSumDigits++;
		}	
		
		if (checkSumDigits == 3)
		{
			// Completo la stringa con i caratteri speciali
			sprintf (nmeaStringBuffer, "%s%c%c%c", nmeaStringBuffer, '\r','\n','\0');
			return 0;
		}
		p1++;
	}
	return -1;
}

	//printf ("lat:%3.2f lon:%3.2f alt:%1.0f speed:%2.2f \n", gpsData.lat, gpsData.lon, gpsData.heigth, gpsData.speed);

int open_gps(char serial_port[20], long int badu){
//serial port opening
	int fd;
	struct termios oldtio, newtio;
	if(serial_port!=NULL)
		{fd=open(serial_port, O_RDWR | O_NOCTTY | O_NONBLOCK);}
	else{fd=open(NODEMDEVICE_STD_GPS, O_RDWR | O_NOCTTY | O_NONBLOCK );}
  	printf ("FD opened\n");
  	if (fd<0) {
	   printf("Errore\n");
	   perror (serial_port);
	   exit(-1);
  	}
  	tcgetattr(fd,&oldtio);
  	bzero(&newtio,sizeof(newtio));
	if(badu==115200){newtio.c_cflag=(BAUDRATEGPS115200 | CS8 | CLOCAL | CREAD);}
	if(badu==38400){newtio.c_cflag=(BAUDRATEGPS38400 | CS8 | CLOCAL | CREAD);}
	if(badu==19200){newtio.c_cflag=(BAUDRATEGPS19200 | CS8 | CLOCAL | CREAD);}
	if(badu==9600){newtio.c_cflag=(BAUDRATEGPS9600 | CS8 | CLOCAL | CREAD);}
	if(badu==4800){newtio.c_cflag=(BAUDRATEGPS4800 | CS8 | CLOCAL | CREAD);}
	if((badu!=4800)&&(badu!=9600)&&(badu!=19200)&&(badu!=38400)&&(badu!=115200))
		{
		perror("worning error on badurate serial device set slowat 4800");
		newtio.c_cflag=(BAUDRATEGPS9600 | CS8 | CLOCAL | CREAD);
		}

	//newtio.c_cflag=(BAUDRATEGPS | CS8 | CLOCAL | CREAD);//only 9600 badu
  	newtio.c_iflag= IGNPAR; //| ICRNL;
  	newtio.c_oflag=0;
  	newtio.c_lflag=ICANON;
  
  	tcflush(fd,TCIFLUSH);
  	tcsetattr(fd,TCSANOW,&newtio);

	return fd;
	//end setting serial port
}

int close_gps(int fd)
{
	return close(fd);
}
