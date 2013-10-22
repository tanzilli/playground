/*
 * File: daisysette.h
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
 * C/C++ source on      	        : 06 01 2012
 *
 * 
 * 
 * 
 * 
 */


#ifndef  _DAISY7_H_
#define _DAISY7_H_

#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h> 
#include <sys/ioctl.h>
#include<math.h>
#include <time.h>
#include <errno.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include <signal.h>
#include "iduec.h"
#include <termios.h> 

#include "global_sensor.h"
#include "/usr/include/linux/i2c-dev.h"

/*
gain mag
1=1.3gauss
2=1.9gauss
3=2.5Gauss
*/
#define GAIN_MAG 	 1	
#define HMC5883L  	 1
#define BMP085 		 1

#define LIS331DLH 	 1

#define ITG3200		 0

#define L3G4200D	 1
#define L3G4200D_LPF_HZ  1  //1:400hz lpf=50hz 2:400hz lpf=25hz 2:200hz lpf=50hz 3:200hz lpf=25hz
#define L3G4200D_DPS  	 1  //1=250dps 2=500dps 3=2000dps
#define L3G4200D_LPF2    0  //secondo filtro low pass 1 attivo 0 disattivato
#define DegToRadIMU 57.2957795

struct _bias_dsette
{
	int bias_acc_x;
	int bias_acc_y;
	int bias_acc_z;
	int bias_gyro_x;
	int bias_gyro_y;
	int bias_gyro_z;
};
typedef _bias_dsette bias_dsette;


int read_itg3200(int fd, int *gyro);
int read_lis331dlh(int fd,int  *accell);
int read_hmc883l(int fd,int *mag);
int read_itg3200(int fd, int *gyro);
datasensincomp myupdatesensor(int fd);
void set_d7_debug_mode(int mode);
void set_d7_initialize(int fd);
float* self_collect_accel_sample(int fd);
float * self_calibrate_gyro_d7(int fd);
float* self_collect_mag_sample(int fd);
int readtemp(int fd);
float readaltitude_press(int fd ,int azione);


#endif
