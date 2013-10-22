/*
 * File: daisysette.c
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

#include "daisysette.h"
//GYRO itg3200
//#define ITG3200_ADDR 		0x68  alternative address
#define ITG3200_ADDR 		0x69
#define ITG3200_POWERM_W 	0x3E
#define ITG3200_POWERM_NORMAL   0x00
#define ITG3200_SAMPLE_DIVREG_W 0x15
#define ITG3200_SAMPLE_DIV_50 	0x13	//50HZ
#define ITG3200_SAMPLE_DIV_100 	0x09	//100HZ
#define ITG3200_SAMPLE_DIV_400 	0x01	//500HZ
#define ITG3200_SAMPLE_DIV_1000 0x00    //1000HZ DEF

#define ITG3200_TEMP_H 		0x1B
#define ITG3200_TEMP_L  	0x1C
#define ITG3200_GYROX_H  	0x1D
#define ITG3200_GYROX_L  	0x1E
#define ITG3200_GYROY_H  	0x1F
#define ITG3200_GYROY_L  	0x20
#define ITG3200_GYROZ_H  	0x21
#define ITG3200_GYROZ_L  	0x22
#define ITG3200_DLPF_W 		0x16  //set filter
#define ITG3200_DLPF_5HZ	0x1E  //5hz cut filter

#define ITG3200_SENSIVITY 	15.0  //lsb/deg/sec

//LIS331DLH
#define LIS331DLH_ADDR 	0x18 	       //alternative address
//#define LIS331DLH_ADDR 		0x19
#define LIS331DLH_REG1 		0x20
//set data acq vel
#define LIS331DLH_REG1_50	0x27 //50hz
#define LIS331DLH_REG1_100	0x2F //100hz
#define LIS331DLH_REG1_1000	0x3F //1000hz
#define LIS331DLH_REG1_400	0x37 //400hz
#define LIS331DLH_REG1_DEF	0x2F //100hz
#define LIS331DLH_ACCX_H  	0x29
#define LIS331DLH_ACCX_L  	0x28
#define LIS331DLH_ACCY_H  	0x2B
#define LIS331DLH_ACCY_L  	0x2A
#define LIS331DLH_ACCZ_H  	0x2D
#define LIS331DLH_ACCZ_L  	0x2C

#define LIS331DLH_SENSIVITY 	1733.0 	//mg 1000count g

//Magnetometro HMC883L
#define HMC5883L_ADDR 		0x1E
#define HMC5883L_REGA		0x00
#define HMC5883L_REGB		0x01
#define HMC5883L_REG_MODE	0x02
#define HMC5883L_MAGX_H		0x03
#define HMC5883L_MAGX_L		0x04
#define HMC5883L_MAGZ_H		0x05
#define HMC5883L_MAGZ_L		0x06
#define HMC5883L_MAGY_H		0x07
#define HMC5883L_MAGY_L		0x08
//settaggi
#define HMC5883L_REGA_CONF 			0x78  //data output continuos 75hz media 8 valori
#define HMC5883L_REGB_CONF_1_3GA 		0x20  //data output 1.3Ga
#define HMC5883L_REGB_CONF_1_9GA 		0x40  //data output 1.9Ga
#define HMC5883L_REGB_CONF_2_5GA 		0x60  //data output 2.5Ga

#define HMC5883L_REG_MODE_CONF 			0x00  //data output continuos measurement mode

//sensibilità
#define sensivity_LSB_Gauss_1_3		1090
#define sensivity_LSB_Gauss_1_9		820
#define sensivity_LSB_Gauss_2_5 	660


//giroscopio l3g4200d
#define L3G4200D_ADDRESS	  0X68
//#define L3G4200D_ADDRESS	  0X69
#define L3G4200D_WHO_AM_I	  0X0F
#define L3G4200D_CTRL_REG1	  0x20
#define L3G4200D_CTRL_REG2	  0x21	
#define L3G4200D_CTRL_REG3	  0x22	
#define L3G4200D_CTRL_REG4	  0x23
#define L3G4200D_CTRL_REG5	  0x24	
#define L3G4200D_REFERENCE	  0x25

#define L3G4200D_OUT_TMP	  0x26
#define L3G4200D_GYROX_L	  0x28	
#define L3G4200D_GYROX_H	  0x29	
#define L3G4200D_GYROY_L	  0x2A	
#define L3G4200D_GYROY_H	  0x2B	
#define L3G4200D_GYROZ_L	  0x2C	
#define L3G4200D_GYROZ_H	  0x2D	
//settaggi
#define L3G4200D_CTRL_REG1_400HZ_25LPF 		0X9F
#define L3G4200D_CTRL_REG1_400HZ_50LPF 		0XAF
#define L3G4200D_CTRL_REG1_200HZ_25LPF 		0X5F
#define L3G4200D_CTRL_REG1_200HZ_50LPF 		0X6F

#define L3G4200D_CTRL_REG2_NO_HI_PASS 		0X20

#define L3G4200D_CTRL_REG3_NO_INTERRUPT		0X00

#define L3G4200D_CTRL_REG4_250DPS		0X00
#define L3G4200D_CTRL_REG4_500DPS		0X10
#define L3G4200D_CTRL_REG4_2000DPS		0X20		

#define L3G4200D_CTRL_REG5_ENABLE_LPF2		0X02
#define L3G4200D_CTRL_REG5_DISABLE_LPF2		0X00
/*
//mdps
#define SENSIVITY_L3G4200D_250DPS		8.75F //mdps/digit
#define SENSIVITY_L3G4200D_500DPS		17.5F //mdps/digit
#define SENSIVITY_L3G4200D_2000DPS		70.0F //mdps/digit	
*/


//dps
#define SENSIVITY_L3G4200D_250DPS		0.00875F //mdps/digit
#define SENSIVITY_L3G4200D_500DPS		0.0175F //mdps/digit
#define SENSIVITY_L3G4200D_2000DPS		0.0700F //mdps/digit	

#define TMEDEL 100

#define sensivity_tmp 280 

//BMP085
#define BMP085_ADDRESS 0x77  // I2C address of BMP085

//pressure sensor global variable
const unsigned char OSS = 0;  // Oversampling Setting
static int ac1;
static int ac2; 
static int ac3; 
static unsigned int ac4;
static unsigned int ac5;
static unsigned int ac6;
static int b1; 
static int b2;
static int mb;
static int mc;
static int md;
static long b5; 
static int temp_u;
static unsigned long press_u;


int sensivity1g_acc_cal=17000; //1000 =1g for calibration

int calibration_sample =50;
static int debug_mode_d7=0;


void set_d7_debug_mode(int mode)
 {
	debug_mode_d7=mode;
 }

void set_d7_initialize(int fd)
  {
	unsigned char buf;
	int temp;
	//set gyro
	#if(ITG3200==1)
		setdevicei2c(fd, ITG3200_ADDR);
		writebytei2c(fd,ITG3200_POWERM_W,ITG3200_POWERM_NORMAL);
		writebytei2c(fd,ITG3200_SAMPLE_DIVREG_W,ITG3200_SAMPLE_DIV_400);
		writebytei2c(fd,ITG3200_DLPF_W ,ITG3200_DLPF_5HZ);
	#endif
	#if(L3G4200D==1)
		setdevicei2c(fd, L3G4200D_ADDRESS);
		#if(L3G4200D_LPF_HZ==1)
			writebytei2c(fd,L3G4200D_CTRL_REG1,L3G4200D_CTRL_REG1_400HZ_50LPF);
		#endif
		#if(L3G4200D_LPF_HZ==2)
			writebytei2c(fd,L3G4200D_CTRL_REG1,L3G4200D_CTRL_REG1_400HZ_25LPF);
		#endif
		#if(L3G4200D_LPF_HZ==3)
			writebytei2c(fd,L3G4200D_CTRL_REG1,L3G4200D_CTRL_REG1_200HZ_50LPF);
		#endif
		#if(L3G4200D_LPF_HZ==4)
			writebytei2c(fd,L3G4200D_CTRL_REG1,L3G4200D_CTRL_REG1_200HZ_25LPF);
		#endif
		writebytei2c(fd,L3G4200D_CTRL_REG2,L3G4200D_CTRL_REG2_NO_HI_PASS);
		writebytei2c(fd,L3G4200D_CTRL_REG3,L3G4200D_CTRL_REG3_NO_INTERRUPT);
		#if(L3G4200D_DPS==1)
			writebytei2c(fd,L3G4200D_CTRL_REG4,L3G4200D_CTRL_REG4_250DPS);
		#endif
		#if(L3G4200D_DPS==2)
			writebytei2c(fd,L3G4200D_CTRL_REG4,L3G4200D_CTRL_REG4_500DPS);
		#endif
		#if(L3G4200D_DPS==3)
			writebytei2c(fd,L3G4200D_CTRL_REG4,L3G4200D_CTRL_REG4_2000DPS);
		#endif
		#if(L3G4200D_LPF2==1)
			writebytei2c(fd,L3G4200D_CTRL_REG5,L3G4200D_CTRL_REG5_ENABLE_LPF2);
		#endif
		#if(L3G4200D_LPF2==0)
			writebytei2c(fd,L3G4200D_CTRL_REG5,L3G4200D_CTRL_REG5_DISABLE_LPF2);
		#endif
	#endif
	//setto accelerometro
	#if(LIS331DLH==1)
		setdevicei2c(fd, LIS331DLH_ADDR );
		writebytei2c(fd,LIS331DLH_REG1,LIS331DLH_REG1_400);
	#endif
	//setto magnetometro
	#if(HMC5883L==1)
		setdevicei2c(fd, HMC5883L_ADDR );
		writebytei2c(fd,HMC5883L_REGA,HMC5883L_REGA_CONF);
		#if(GAIN_MAG==1)
		writebytei2c(fd,HMC5883L_REGB,HMC5883L_REGB_CONF_1_3GA);
		#endif
		#if(GAIN_MAG==2)
		writebytei2c(fd,HMC5883L_REGB,HMC5883L_REGB_CONF_1_9GA);
		#endif
		#if(GAIN_MAG==3)
		writebytei2c(fd,HMC5883L_REGB,HMC5883L_REGB_CONF_2_5GA);
		#endif
		writebytei2c(fd,HMC5883L_REG_MODE,HMC5883L_REG_MODE_CONF);
	#endif
	#if(BMP085==1)
	setdevicei2c(fd, BMP085_ADDRESS);
	buf=readbytei2c(fd, 0xAA);
	ac1 = buf<<8;
	buf=readbytei2c(fd, 0xAB);
	ac1 |= buf;
	if(ac1>32768)
		{ac1=ac1-65535;}
	buf=readbytei2c(fd, 0xAC);
	ac2 = buf<<8;
	buf=readbytei2c(fd, 0xAD);
	ac2 |= buf;
	if(ac2>32768)
		{ac2=ac2-65535;}
	buf=readbytei2c(fd, 0xAE);
	ac3 = buf<<8;
	buf=readbytei2c(fd, 0xAF);
	ac3 |= buf;
	if(ac3>32768)
		{ac3=ac3-65535;}
	buf=readbytei2c(fd, 0xB0);
	ac4 = buf<<8;
	buf=readbytei2c(fd, 0xB1);
	ac4 |= buf;
	buf=readbytei2c(fd, 0xB2);
	ac5 = buf<<8;
	buf=readbytei2c(fd, 0xB3);
	ac5 |= buf;
	buf=readbytei2c(fd, 0xB4);
	ac6 = buf<<8;
	buf=readbytei2c(fd, 0xB5);
	ac6 |= buf;
	buf=readbytei2c(fd, 0xB6);
	b1 = buf<<8;
	buf=readbytei2c(fd, 0xB7);
	b1 |= buf;
	if(b1>32768)
		{b1=b1-65535;}
	buf=readbytei2c(fd, 0xB8);
	b2 = buf<<8;
	buf=readbytei2c(fd, 0xB9);
	b2 |= buf;
	if(b2>32768)
		{b2=b2-65535;}
	buf=readbytei2c(fd, 0xBA);
	mb = buf<<8;
	buf=readbytei2c(fd, 0xBB);
	mb |= buf;
	if(mb>32767)
		{mb=mb-65535;}
	buf=readbytei2c(fd, 0xBC);
	mc = buf<<8;
	buf=readbytei2c(fd, 0xBD);
	mc |= buf;
	if(mc>32768)
		{mc=mc-65535;}
	buf=readbytei2c(fd, 0xBE);
	md = buf<<8;
	buf=readbytei2c(fd, 0xBF);
	md |= buf;
	if(md>32768)
		{md=md-65535;}
	printf("ac1 %d ac2 %d , ac3 %d , ac4 %d , ac5 %d ,ac6 %d ,b1 %d , b2 %d , mb %d ,mc %d , md %d , b5 %d",ac1,ac2,ac3,ac4,ac5,ac6,b1,b2,mb,mc,md,b5);

	#endif
 }

int read_l3g4200d(int fd, int *gyro)
 {
	unsigned char buf;
	int temp,X,Y,Z;

	setdevicei2c(fd, L3G4200D_ADDRESS);
	
	//temp = buf<<8;
	//buf=readbytei2c(fd, L3G4200D_OUT_TMP);
	//temp |= buf;
	temp=0;
	buf=readbytei2c(fd, L3G4200D_GYROX_H);
	X = buf<<8;
	buf=readbytei2c(fd, L3G4200D_GYROX_L);
	X |= buf;
	if(X>32768)
		{X=X-65535;}
	buf=readbytei2c(fd, L3G4200D_GYROY_H);
	Y = buf<<8;
	buf=readbytei2c(fd, L3G4200D_GYROY_L);
	Y |= buf;
	if(Y>32768)
		{Y=Y-65535;}

	buf=readbytei2c(fd, L3G4200D_GYROZ_H);
	Z = buf<<8;
	buf=readbytei2c(fd, L3G4200D_GYROZ_L);
	Z |= buf;
	if(Z>32768)
		{Z=Z-65535;}
	if(debug_mode_d7==1){
	printf("debug gyro acquisite x: %d  , y: %d  , z: %d \n", X,Y,Z);
	}
	gyro[0]=temp/sensivity_tmp;
	gyro[1]=X;
	gyro[2]=Y;
	gyro[3]=Z;
	return 1;
 }
int read_itg3200(int fd, int *gyro)
 {
	unsigned char buf;
	int temp,X,Y,Z;
	setdevicei2c(fd, ITG3200_ADDR);

	//buf=readbytei2c(fd, ITG3200_TEMP_H);
	//temp = buf<<8;
	//buf=readbytei2c(fd, ITG3200_TEMP_L);
	//temp |= buf;
	temp=0;
	buf=readbytei2c(fd, ITG3200_GYROX_H);
	X = buf<<8;
	buf=readbytei2c(fd, ITG3200_GYROX_L);
	X |= buf;
	if(X>32768)
		{X=X-65535;}
	buf=readbytei2c(fd, ITG3200_GYROY_H);
	Y = buf<<8;
	buf=readbytei2c(fd, ITG3200_GYROY_L);
	Y |= buf;
	if(Y>32768)
		{Y=Y-65535;}

	buf=readbytei2c(fd, ITG3200_GYROZ_H);
	Z = buf<<8;
	buf=readbytei2c(fd, ITG3200_GYROZ_L);
	Z |= buf;
	if(Z>32768)
		{Z=Z-65535;}
	if(debug_mode_d7==1){
	printf("debug gyro acquisite x: %d  , y: %d  , z: %d \n", X,Y,Z);
	}
	gyro[0]=temp/sensivity_tmp;
	gyro[1]=X;
	gyro[2]=Y;
	gyro[3]=Z;
	return 1;
 }


int read_lis331dlh(int fd,int *accell)
 {
	setdevicei2c(fd, LIS331DLH_ADDR );
	//writebytei2c(fd,LIS331DLH_REG1,LIS331DLH_REG1_50);
	char buf=0x00;
	int Xacc=0,Yacc=0,Zacc=0;

	buf=readbytei2c(fd, LIS331DLH_ACCX_H);
	Xacc = buf<<8;
	buf=readbytei2c(fd, LIS331DLH_ACCX_L);
	Xacc |= buf;
	if(Xacc>32768)
		{Xacc=Xacc-65535;}
	buf=readbytei2c(fd, LIS331DLH_ACCY_H);
	Yacc = buf<<8;
	buf=readbytei2c(fd, LIS331DLH_ACCY_L);
	Yacc |= buf;
	if(Yacc>32768)
		{Yacc=Yacc-65535;}
	buf=readbytei2c(fd, LIS331DLH_ACCZ_H );
	Zacc = buf<<8;
	buf=readbytei2c(fd, LIS331DLH_ACCZ_L );
	Zacc |= buf;
	if(Zacc>32768)
		{Zacc=Zacc-65535;}
	if(debug_mode_d7==1){
	printf("debug accelerazioni acquisite x: %d  , y: %d  , z: %d \n", Xacc,Yacc,Zacc);
	}
	accell[0]=Xacc;
	accell[1]=Yacc;
	accell[2]=Zacc;
	return 1;

}


int read_hmc883l(int fd,int *mag)
 {
	setdevicei2c(fd, HMC5883L_ADDR  );

	char buf=0x00;
	int Xmag=0,Ymag=0,Zmag=0;

	buf=readbytei2c(fd, HMC5883L_MAGX_H);
	Xmag = buf<<8;
	buf=readbytei2c(fd, HMC5883L_MAGX_L);
	Xmag |= buf;
	if(Xmag>32768)
		{Xmag=Xmag-65535;}
	buf=readbytei2c(fd, HMC5883L_MAGY_H);
	Ymag = buf<<8;
	buf=readbytei2c(fd, HMC5883L_MAGY_L);
	Ymag |= buf;
	if(Ymag>32768)
		{Ymag=Ymag-65535;}
	buf=readbytei2c(fd, HMC5883L_MAGZ_H );
	Zmag = buf<<8;
	buf=readbytei2c(fd, HMC5883L_MAGZ_L );
	Zmag |= buf;
	if(Zmag>32768)
		{Zmag=Zmag-65535;}
	if(debug_mode_d7==1){
	printf("debug magnetometri acquisiti x: %d  , y: %d  , z: %d \n", Xmag,Ymag,Zmag);
	}
	mag[0]=Xmag;
	mag[1]=Ymag;
	mag[2]=Zmag;
	return 1;

 }

datasensincomp myupdatesensor(int fd){
	datasensincomp temps;
	//accell_float accell_hrs;
	int gyro[4],gyro1[4],gyro2[4];
	float gyrof[4],gyro1f[4],gyro2f[4];
	//float x,y,z, normgravity;
	int accell[3],accell1[3],accell2[3];
	float accellf[3],accell1f[3],accell2f[3];
	int mag[3],mag1[3];
	float magf[3],mag1f[3];
	//read magneto
	usleep(TMEDEL);
	#if(HMC5883L==1)
		//1
		read_hmc883l(fd,mag);
		magf[0]=(float)(mag[0]);
		magf[1]=(float)(mag[1]);
		magf[2]=(float)(mag[2]);
		#if(GAIN_MAG==1)
			magf[0]=magf[0]/sensivity_LSB_Gauss_1_3;
			magf[1]=magf[1]/sensivity_LSB_Gauss_1_3;
			magf[2]=-magf[2]/sensivity_LSB_Gauss_1_3;
		#endif
		#if(GAIN_MAG==2)
			magf[0]=magf[0]/sensivity_LSB_Gauss_1_9;
			magf[1]=magf[1]/sensivity_LSB_Gauss_1_9;
			magf[2]=-magf[2]/sensivity_LSB_Gauss_1_9;
		#endif
		#if(GAIN_MAG==3)
			magf[0]=magf[0]/sensivity_LSB_Gauss_2_5;
			magf[1]=magf[1]/sensivity_LSB_Gauss_2_5;
			magf[2]=-magf[2]/sensivity_LSB_Gauss_2_5;
		#endif
	#endif

	usleep(TMEDEL);
	/******1*****/
	#if(ITG3200==1)
		read_itg3200(fd , gyro);
		gyrof[1]=(float)(gyro[1]);
		gyrof[2]=(float)(gyro[2]);
		gyrof[3]=(float)(gyro[3]);
		gyrof[1]=-gyrof[2]/ITG3200_SENSIVITY;
		gyrof[2]=-gyrof[1]/ITG3200_SENSIVITY;
		gyrof[3]=-gyrof[3]/ITG3200_SENSIVITY;

	#endif

	#if(L3G4200D==1)
		read_l3g4200d(fd , gyro);
		gyrof[1]=(float)(gyro[1]);
		gyrof[2]=(float)(gyro[2]);
		gyrof[3]=(float)(gyro[3]);
		#if(L3G4200D_DPS==1)
			gyrof[1]=gyrof[1]*SENSIVITY_L3G4200D_250DPS;
			gyrof[2]=gyrof[2]*SENSIVITY_L3G4200D_250DPS;
			gyrof[3]=gyrof[3]*SENSIVITY_L3G4200D_250DPS;
		#endif
		#if(L3G4200D_DPS==2)
			gyrof[1]=gyrof[1]*SENSIVITY_L3G4200D_500DPS;
			gyrof[2]=gyrof[2]*SENSIVITY_L3G4200D_500DPS;
			gyrof[3]=gyrof[3]*SENSIVITY_L3G4200D_500DPS;
		#endif
		#if(L3G4200D_DPS==3)
			gyrof[1]=gyrof[1]*SENSIVITY_L3G4200D_2000DPS;
			gyrof[2]=gyrof[2]*SENSIVITY_L3G4200D_2000DPS;
			gyrof[3]=gyrof[3]*SENSIVITY_L3G4200D_2000DPS;
		#endif
	#endif
	usleep(TMEDEL);
	#if(LIS331DLH==1)
		read_lis331dlh(fd ,accell);
		accellf[0]=(float)(accell[0]);
		accellf[1]=(float)(accell[1]);
		accellf[2]=(float)(accell[2]);
		accellf[0]=accellf[0]/(LIS331DLH_SENSIVITY );
		accellf[1]=accellf[1]/(LIS331DLH_SENSIVITY );
		accellf[2]=accellf[2]/(LIS331DLH_SENSIVITY );
	#endif

	usleep(TMEDEL);
	/******2*****/
	#if(ITG3200==1)
		read_itg3200(fd , gyro1);
		gyro1f[1]=(float)(gyro1[1]);
		gyro1f[2]=(float)(gyro1[2]);
		gyro1f[3]=(float)(gyro1[3]);
		gyro1f[1]=-gyro1f[2]/ITG3200_SENSIVITY;
		gyro1f[2]=-gyro1f[1]/ITG3200_SENSIVITY;
		gyro1f[3]=-gyro1f[3]/ITG3200_SENSIVITY;

	#endif
	#if(L3G4200D==1)
		read_l3g4200d(fd , gyro1);
		gyro1f[1]=(float)(gyro1[1]);
		gyro1f[2]=(float)(gyro1[2]);
		gyro1f[3]=(float)(gyro1[3]);
		#if(L3G4200D_DPS==1)
			gyro1f[1]=gyro1f[1]*SENSIVITY_L3G4200D_250DPS;
			gyro1f[2]=gyro1f[2]*SENSIVITY_L3G4200D_250DPS;
			gyro1f[3]=gyro1f[3]*SENSIVITY_L3G4200D_250DPS;
		#endif
		#if(L3G4200D_DPS==2)
			gyro1f[1]=gyro1f[1]*SENSIVITY_L3G4200D_500DPS;
			gyro1f[2]=gyro1f[2]*SENSIVITY_L3G4200D_500DPS;
			gyro1f[3]=gyro1f[3]*SENSIVITY_L3G4200D_500DPS;
		#endif
		#if(L3G4200D_DPS==3)
			gyro1f[1]=gyro1f[1]*SENSIVITY_L3G4200D_2000DPS;
			gyro1f[2]=gyro1f[2]*SENSIVITY_L3G4200D_2000DPS;
			gyro1f[3]=gyro1f[3]*SENSIVITY_L3G4200D_2000DPS;
		#endif
	#endif
	usleep(TMEDEL);
	#if(LIS331DLH==1)
		read_lis331dlh(fd ,accell1);
		accell1f[0]=(float)(accell1[0]);
		accell1f[1]=(float)(accell1[1]);
		accell1f[2]=(float)(accell1[2]);
		accell1f[0]=accell1f[0]/(LIS331DLH_SENSIVITY );
		accell1f[1]=accell1f[1]/(LIS331DLH_SENSIVITY );
		accell1f[2]=accell1f[2]/(LIS331DLH_SENSIVITY );
	#endif

	usleep(TMEDEL);
	/******3*****/
	#if(ITG3200==1)
		read_itg3200(fd , gyro2);
		gyro2f[1]=(float)(gyro2[1]);
		gyro2f[2]=(float)(gyro2[2]);
		gyro2f[3]=(float)(gyro2[3]);
		gyro2f[1]=-gyro2f[2]/ITG3200_SENSIVITY;
		gyro2f[2]=-gyro2f[1]/ITG3200_SENSIVITY;
		gyro2f[3]=-gyro2f[3]/ITG3200_SENSIVITY;
	#endif
	#if(L3G4200D==1)
		read_l3g4200d(fd , gyro2);
		gyro2f[1]=(float)(gyro2[1]);
		gyro2f[2]=(float)(gyro2[2]);
		gyro2f[3]=(float)(gyro2[3]);
		#if(L3G4200D_DPS==1)
			gyro2f[1]=gyro2f[1]*SENSIVITY_L3G4200D_250DPS;
			gyro2f[2]=gyro2f[2]*SENSIVITY_L3G4200D_250DPS;
			gyro2f[3]=gyro2f[3]*SENSIVITY_L3G4200D_250DPS;
		#endif
		#if(L3G4200D_DPS==2)
			gyro2f[1]=gyro2f[1]*SENSIVITY_L3G4200D_500DPS;
			gyro2f[2]=gyro2f[2]*SENSIVITY_L3G4200D_500DPS;
			gyro2f[3]=gyro2f[3]*SENSIVITY_L3G4200D_500DPS;
		#endif
		#if(L3G4200D_DPS==3)
			gyro2f[1]=gyro2f[1]*SENSIVITY_L3G4200D_2000DPS;
			gyro2f[2]=gyro2f[2]*SENSIVITY_L3G4200D_2000DPS;
			gyro2f[3]=gyro2f[3]*SENSIVITY_L3G4200D_2000DPS;
		#endif

	#endif
	usleep(TMEDEL);
	#if(LIS331DLH==1)
		read_lis331dlh(fd ,accell2);
		accell2f[0]=(float)(accell2[0]);
		accell2f[1]=(float)(accell2[1]);
		accell2f[2]=(float)(accell2[2]);
		accell2f[0]=accell2f[0]/(LIS331DLH_SENSIVITY );
		accell2f[1]=accell2f[1]/(LIS331DLH_SENSIVITY );
		accell2f[2]=accell2f[2]/(LIS331DLH_SENSIVITY );
	#endif
	usleep(TMEDEL);
	
	//read magneto
	#if(HMC5883L==1)
		//2
		read_hmc883l(fd,mag1);

		mag1f[0]=(float)(mag1[0]);
		mag1f[1]=(float)(mag1[1]);
		mag1f[2]=(float)(mag1[2]);

		#if(GAIN_MAG==1)
			mag1f[0]=mag1f[0]/sensivity_LSB_Gauss_1_3;
			mag1f[1]=mag1f[1]/sensivity_LSB_Gauss_1_3;
			mag1f[2]=-mag1f[2]/sensivity_LSB_Gauss_1_3;
		#endif
		#if(GAIN_MAG==2)
			mag1f[0]=mag1f[0]/sensivity_LSB_Gauss_1_9;
			mag1f[1]=mag1f[1]/sensivity_LSB_Gauss_1_9;
			mag1f[2]=-mag1f[2]/sensivity_LSB_Gauss_1_9;
		#endif
		#if(GAIN_MAG==3)
			mag1f[0]=mag1f[0]/sensivity_LSB_Gauss_2_5;
			mag1f[1]=mag1f[1]/sensivity_LSB_Gauss_2_5;
			mag1f[2]=-mag1f[2]/sensivity_LSB_Gauss_2_5;
		#endif


		temps.mag_X[0]=magf[0];
		temps.mag_Y[0]=magf[1];
		temps.mag_Z[0]=magf[2];
		//interpolate
		temps.mag_X[1]=(magf[0]+mag1f[0])/2;
		temps.mag_Y[1]=(magf[1]+mag1f[1])/2;
		temps.mag_Z[1]=(magf[2]+mag1f[2])/2;

		temps.mag_X[2]=mag1f[0];
		temps.mag_Y[2]=mag1f[1];
		temps.mag_Z[2]=mag1f[2];

	#else
		temps.mag_X=0;
		temps.mag_Y=0;
		temps.mag_Z=0;
	#endif

	#if((ITG3200==1)||(L3G4200D==1))
		temps.gyro_X[0]=gyrof[1];
		temps.gyro_X[1]=gyro1f[1];
		temps.gyro_X[2]=gyro2f[1];

		temps.gyro_Y[0]=gyrof[2];
		temps.gyro_Y[1]=gyro1f[2];
		temps.gyro_Y[2]=gyro2f[2];

		temps.gyro_Z[0]=gyrof[3];
		temps.gyro_Z[1]=gyro1f[3];
		temps.gyro_Z[2]=gyro2f[3];
	
	#else
		temps.gyro_X=0;
		temps.gyro_Y=0;
		temps.gyro_Z=0;
	#endif
	
	#if(LIS331DLH==1)
		temps.acc_X[0]=accellf[0];
		temps.acc_X[1]=accell1f[0];
		temps.acc_X[2]=accell2f[0];

		temps.acc_Y[0]=accellf[1];
		temps.acc_Y[1]=accell1f[1];
		temps.acc_Y[2]=accell2f[1];

		temps.acc_Z[0]=accellf[2];
		temps.acc_Z[1]=accell1f[2];
		temps.acc_Z[2]=accell2f[2];

	#else
		temps.acc_X=0;
		temps.acc_Y=0;
		temps.acc_Z=0;
	#endif

//	if(debug_mode_d7==1){
//	printf("debug bias subctract and scaled gyrox %f gyroy%f gyroz %f accx %f accy %f accz %f magx %f magy %f magz %f \n"
//			,temps.gyro_X,temps.gyro_Y,temps.gyro_Z,temps.acc_X,temps.acc_Y,temps.acc_Z,temps.mag_X,temps.mag_Y,temps.mag_Z);
//	}

	return temps;
}

float * self_calibrate_gyro_d7(int fd)
 {
	 int gyro[4];
	 long int gyrosum[4];
	 gyrosum[1]=0;
	 gyrosum[2]=0;
	 gyrosum[3]=0;
	 float gyrof[4];
	 int i;
	 int div=1;
	 bias_dsette ret;
	 for(i=1;i<=calibration_sample;i++)
	 {
		 memset(&gyro,0,sizeof(gyro));
			#if(ITG3200==1)
				read_itg3200(fd , gyro);
			#endif
			#if(L3G4200D==1)
				read_l3g4200d(fd , gyro);
			#endif
		gyrosum[1]=gyrosum[1]+gyro[1];
		gyrosum[2]=gyrosum[2]+gyro[2];
		gyrosum[3]=gyrosum[3]+gyro[3];
		div=i;
	 }
	 gyrof[1]=((float)gyrosum[1])/div;
	 gyrof[2]=((float)gyrosum[2])/div;
	 gyrof[3]=((float)gyrosum[3])/div;
	 printf("debug bias calibration gyrox %f gyroy%f gyroz %f \n",gyrof[1],gyrof[2],gyrof[3]);
 	return gyrof;
}


float* self_collect_accel_sample(int fd)
 {
	 int accell[3];
	 float accellsum[3];
	 float accell2f[3];
	 accellsum[1]=0;
	 accellsum[2]=0;
	 accellsum[0]=0;
	 int i;
	 int div=1;
	 for(i=1;i<=calibration_sample;i++)
	{
		memset(&accell,0,sizeof(accell));
		#if(LIS331DLH==1)
			read_lis331dlh(fd ,accell);
		#endif
		accell2f[0]=(float)(accell[0]);
		accell2f[1]=(float)(accell[1]);
		accell2f[2]=(float)(accell[2]);
		accell2f[0]=accell2f[0]/(LIS331DLH_SENSIVITY );
		accell2f[1]=accell2f[1]/(LIS331DLH_SENSIVITY );
		accell2f[2]=accell2f[2]/(LIS331DLH_SENSIVITY );
		accellsum[0]=accellsum[0]+accell2f[0];
		accellsum[2]=accellsum[2]+accell2f[2];
		accellsum[1]=accellsum[1]+accell2f[1];
	    	div=i;
	}

	 accell2f[0]=accellsum[0]/div;
	 accell2f[1]=accellsum[1]/div;
	 accell2f[2]=accellsum[2]/div;

	 printf("debug collected acceleration data accx %f accy %f accz %f \n",accell2f[0],accell2f[1],accell2f[2] );
	 return accell2f;
}


float* self_collect_mag_sample(int fd)
 {
	 int mag[3];
	 float magsum[3];
	 float magf[3];
	 magsum[1]=0;
	 magsum[2]=0;
	 magsum[0]=0;
	 int i;
	 int div=1;
	 for(i=1;i<=calibration_sample;i++)
	{
		memset(&mag,0,sizeof(mag));
		#if(HMC5883L==1)
			read_hmc883l(fd,mag);
			magf[0]=(float)(mag[0]);
			magf[1]=(float)(mag[1]);
			magf[2]=(float)(mag[2]);
			#if(GAIN_MAG==1)
				magf[0]=magf[0]/sensivity_LSB_Gauss_1_3;
				magf[1]=magf[1]/sensivity_LSB_Gauss_1_3;
				magf[2]=-magf[2]/sensivity_LSB_Gauss_1_3;
			#endif
			#if(GAIN_MAG==2)
				magf[0]=magf[0]/sensivity_LSB_Gauss_1_9;
				magf[1]=magf[1]/sensivity_LSB_Gauss_1_9;
				magf[2]=-magf[2]/sensivity_LSB_Gauss_1_9;
			#endif
			#if(GAIN_MAG==3)
				magf[0]=magf[0]/sensivity_LSB_Gauss_2_5;
				magf[1]=magf[1]/sensivity_LSB_Gauss_2_5;
				magf[2]=-magf[2]/sensivity_LSB_Gauss_2_5;
			#endif
		#endif

		magsum[0]=magsum[0]+magf[0];
		magsum[2]=magsum[2]+magf[2];
		magsum[1]=magsum[1]+magf[1];
	    	div=i;
	}

	 magf[0]=magsum[0]/div;
	 magf[1]=magsum[1]/div;
	 magf[2]=magsum[2]/div;

	 printf("debug collected mgnetic data magx %f magy %f magz %f \n",magf[0],magf[1],magf[2] );
	 return magf;
}

int readtemp(int fd)
{
	unsigned char buf;
	int temp=0;
	#if(ITG3200==1)
	setdevicei2c(fd, ITG3200_ADDR);
	buf=readbytei2c(fd, ITG3200_TEMP_H);
	temp = buf<<8;
	buf=readbytei2c(fd, ITG3200_TEMP_L);
	temp |= buf;
	#endif
	#if(L3G4200D==1)
	setdevicei2c(fd, L3G4200D_ADDRESS);
	buf=readbytei2c(fd, L3G4200D_OUT_TMP);
	temp = buf<<8;
	#endif
return temp/sensivity_tmp;
}


float readaltitude_press(int fd ,int azione)
{
	short temperature;
	long x1, x2, x3, b3, b6, p;
	unsigned long b4, b7;
	long x1p, x2p;
	float pressione;
	unsigned char buf;
	if(azione==0)
	{
		//printf("azione 0 \n");
		setdevicei2c(fd, BMP085_ADDRESS);
		//richiedo aggiornamento temperature
		writebytei2c(fd,0xF4,0x2E);
		return -10000;
	}
	//leggo temperatura
	if(azione==1)
	{

		setdevicei2c(fd, BMP085_ADDRESS);
		buf=readbytei2c(fd, 0xF6);
		temp_u = buf<<8;
		buf=readbytei2c(fd, 0xF7);
		temp_u |= buf;
		//printf("azione 1 leggo temp  %d \n",temp_u );
		return -10000;
	}

	//richiedo aggiornamento pressione
	if(azione==2)
	{
		//printf("azione 2 \n");
		setdevicei2c(fd, BMP085_ADDRESS);
		writebytei2c(fd,0xF4,0x34 + (OSS<<6));
		return -10000;
	}
	if(azione==3)
	{

		//printf("ac1 %d ac2 %d , ac3 %d , ac4 %d , ac5 %d ,ac6 %d ,b1 %d , b2 %d , mb %d ,mc %d , md %d , b5 %d",ac1,ac2,ac3,ac4,ac5,ac6,b1,b2,mb,mc,md,b5);
		setdevicei2c(fd, BMP085_ADDRESS);
		buf=readbytei2c(fd, 0xF6);
		press_u = buf<<16;
		buf=readbytei2c(fd, 0xF7);
		press_u|= buf<<8;
		buf=readbytei2c(fd, 0xF8);
		press_u |= buf;
		press_u = press_u >> (8-OSS);
		//printf("azione 3 leggo press  %ld \n",press_u );
		x1p = (((long)temp_u - (long)ac6)*(long)ac5) >> 15;
		x2p = ((long)mc << 11)/(x1p + md);
		b5 = x1p + x2p;
		temperature= ((b5 + 8)>>4);
		//printf("1 temperature %d \n",temperature);

		b6 = b5 - 4000;
		// Calculate B3
		x1 = (b2 * (b6 * b6)>>12)>>11;
		x2 = (ac2 * b6)>>11;
		x3 = x1 + x2;
		b3 = (((((long)ac1)*4 + x3)<<OSS) + 2)>>2;
		// Calculate B4
		x1 = (ac3 * b6)>>13;
		x2 = (b1 * ((b6 * b6)>>12))>>16;
		x3 = ((x1 + x2) + 2)>>2;
		b4 = (ac4 * (unsigned long)(x3 + 32768))>>15;

		b7 = ((unsigned long)(press_u - b3) * (50000>>OSS));
		if (b7 < 0x80000000)
		p = (b7<<1)/b4;
		else
		p = (b7/b4)<<1;
		x1 = (p>>8) * (p>>8);
		x1 = (x1 * 3038)>>16;
		x2 = (-7357 * p)>>16;
		//printf("1\n");
		p += (x1 + x2 + 3791)>>4;
		pressione =((float)p)/100;
		//printf("1 %f  altitudine%f\n",pressione, (float)(44330*(1-pow((pressione/1013.25),(1/5.255)))));
		return (float)(44330*(1-pow((pressione/1013.25),(1/5.255))));
	}

}
