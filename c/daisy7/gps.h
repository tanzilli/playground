
#include "nmeap.h"

#include <unistd.h>
#include <stdio.h>		
#include <stdlib.h>
#include <fcntl.h>
#include <errno.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <signal.h>
#include <stdio.h> 
#include <termios.h>
#include <string.h>

#ifndef _GPS_h_
#define _GPS_h_
 

#define NMEA_STRING_LENGTH		1024
#define NMEA_BUFFER_LENGTH		1024		//!< maximum character buffer length for NMEA serial streaming
#define MAX_NMEA_GPSWRONG_SENTENCES 	50		//!< maximum sequential unlocked NMEA strings

// GPS Errors
//----------------------
#define ERROR_GPS_WRONG_CHECKSUM	100	//!< checksum NMEA errata.
#define ERROR_GPS_TIMEOUT_WAIT_GPS	101	//!< Timeout per: 	attesa segnale/servizio GPS
#define ERROR_GPS_TIMEOUT_NMEA_SYNCH	102	//!< Timeout per: 	mancato sincronismo con streaming NMEA
#define ERROR_GPS_SERIAL_PORT		104	//!< Impossibile aprire la porta seriale GPS
#define ERROR_GPS_GENERIC_ERR		105	//!< Errore generico. 
#define ERROR_GPS_IMPOSSIBLE_GET_POS	106	//!< Impossibile ottenere la posizione leggendo dalla seriale
#define ERROR_GPS_WAITING_FOR_GPS	110
#define ERROR_GPS_UNABLE_TO_READ_SERIAL	120
#define ERROR_GPS_PROBLEMS_DURING_PARSE	130

#define GPS_NO_ERRORS			0
#define	GPS_GET_POSITION_OK		GPS_NO_ERRORS			
#define GPS_UNABLE_TO_READ_SERIAL	ERROR_GPS_UNABLE_TO_READ_SERIAL
#define GPS_UNABLE_TO_GET_POSITION	ERROR_GPS_IMPOSSIBLE_GET_POS
#define GPS_PARSER_ERROR		ERROR_GPS_PROBLEMS_DURING_PARSE
#define GPS_WRONG_CHECKSUM		ERROR_GPS_WRONG_CHECKSUM
#define GPS_WAITING_FOR_LOCK		ERROR_GPS_WAITING_FOR_GPS

#define NODEMDEVICE_STD_GPS "/dev/ttyS3"
#define BAUDRATEGPS115200 B115200
#define BAUDRATEGPS38400 B38400
#define BAUDRATEGPS19200 B19200
#define BAUDRATEGPS9600 B9600
#define BAUDRATEGPS4800 B4800

#define FALSEG 0
#define TRUEG 1

#define GPS_DEBUG			0

/*! \struct NavInputs_t
This structure contains the variable that characterize the GPS info about the vessel(user) position
 */
typedef struct {
	double 	lat;		/*!< latitude in decimanl degrees [-90° .. +90°]*/
	double 	lon;		/*!< longitude  in decimal degrees [-180° .. +180°] */
	double 	heigth;		/*!< heigth of the vessel respect the sea level [mt] */
	double	speed;
	unsigned int	gpsFixQuality;	/*!< indicator of the presence of the GPS service (0=no service, >0 GPS available) */
}NavInputs_t;




static NavInputs_t 	gpsData;	/*!< dati da GPS */
NavInputs_t read_nav_data();

int readchar(char*);
 void print_gga(nmeap_gga_t*);
 void gpgga_callout(nmeap_context_t*, void*, void*);
 void print_rmc(nmeap_rmc_t*);
 void gprmc_callout(nmeap_context_t*, void*, void*);
int parseNMEAString(char*);
int searchCompleteNMEAString (char* nmeaBuffer);

int getUserPosition(int fd);  	/*!< manage GPS protocol and get GPS position */
int close_gps(int fd);
int open_gps(char serial_port[20], long int badu);
#endif

