/*
 * File: main.c
 * Autor: Federico LOlli
 *  *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * @author Federico Lolli <federicololli@hotmail.com>
 * @version 0.1
 * @date 21/01/2011
 *
 * Model version                        : 0.1
 * C/C++ source on      	        : 06 01 2011
 *
 * 
 * 
 * 
 * 
 */


#include<math.h>
#include <time.h>
#include <errno.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include <signal.h>
#include <stdio.h> 
#include <termios.h> 
#include <sys/ioctl.h>
#include <stdlib.h>
#include "iduec.h"
#include "daisysette.h"
#include "global_sensor.h"
#include "gps.h"

void sighandlersigterm(int sig);
   int fd_iduec=0,fd_gps=0;
    
int main(int argc, char *argv[])
{ 

  NavInputs_t gpsData1;
  int cnt_gps=0;
  int cnt_baro=0;
  int statusbaro=0; 
  int update_tmp_cnt=0;
  float tmp_altitude=0,altitude=0;

  //structure data
  datasensincomp datasensor;
  /*opendevice esterni*/
  /*apertura i2c*/
  fd_iduec=openi2c();
  fd_gps= open_gps("/dev/ttyS2",115200);
   set_d7_initialize(fd_iduec);

  /*collego il segnale di terminazione*/
  signal(SIGTERM,sighandlersigterm);

 /*main loop*/
 while (1) 
  {
	/*****************************GPS enable*********************************/

	if(getUserPosition(fd_gps)<0)//salva i dati in varibile globale gpsData
	{printf("parser nemea string problem");}
	gpsData1=read_nav_data();
	if(gpsData1.lat==0||gpsData1.lon==0)
	{
		gpsData1.lat=0 ;
		gpsData1.lon=0;
		gpsData1.heigth=0;
		gpsData1.speed=0.0;
		gpsData1.gpsFixQuality=0;
	}
	printf("lat %f lon %f vel %f  altitude %f \n",gpsData1.lat,gpsData1.lon,gpsData1.speed,gpsData1.heigth);

	//update altitude
	tmp_altitude=readaltitude_press(fd_iduec ,statusbaro);
	statusbaro ++;
	if(statusbaro>3)
	{
		statusbaro=0;
	}
	//update altitude if data is true
	if(tmp_altitude>-500)
	{
		altitude=tmp_altitude;
	}	
	printf("altitudine %f \n",altitude);
	/******************IMU D7*************************/

	//acquiring inertial data from i2c
	datasensor = myupdatesensor(fd_iduec);

	printf("acc0: %f %f %f mag0: %f %f %f gyro0: %f %f %f \n",
		datasensor.acc_X[0],datasensor.acc_Y[0],datasensor.acc_Z[0],
		 datasensor.mag_X[0],datasensor.mag_Y[0],datasensor.mag_Z[0],
		datasensor.gyro_X[0],datasensor.gyro_Y[0],datasensor.gyro_Z[0]);
  	printf("acc1: %f %f %f mag1: %f %f %f gyro1: %f %f %f \n",
		datasensor.acc_X[1],datasensor.acc_Y[1],datasensor.acc_Z[1],
		 datasensor.mag_X[1],datasensor.mag_Y[1],datasensor.mag_Z[1],
		datasensor.gyro_X[1],datasensor.gyro_Y[1],datasensor.gyro_Z[1]);
  	printf("acc2: %f %f %f mag2: %f %f %f gyro2: %f %f %f \n",
		datasensor.acc_X[2],datasensor.acc_Y[2],datasensor.acc_Z[2],
		 datasensor.mag_X[2],datasensor.mag_Y[2],datasensor.mag_Z[2],
		datasensor.gyro_X[2],datasensor.gyro_Y[2],datasensor.gyro_Z[2]);
	set_d7_debug_mode(1);
	sleep(2);


  }//end main loop


  closei2c(fd_iduec);
  close_gps(fd_gps);
 


  return 0;
}

/*signal*/
void sighandlersigterm(int sig)
{

  closei2c(fd_iduec);
  close_gps(fd_gps);
  exit(1);
}






