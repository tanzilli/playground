/*
 * File: iduec.c
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
 * C/C++ source on      	        : 29 02 2011
 *
 * 
 * 
 * 
 * 
 */
#include "iduec.h"



int openi2c(void)
  {
	int fd;
	char filename[20];
	sprintf(filename, "/dev/i2c-0");
	fd = open(filename, O_RDWR);
	if (fd < 0) {
		printf("Error on open i2c \n");
		exit(1);
	}
 
return fd;	
  }

int closei2c(int fd)
  {
	return close(fd);
  }

void setdevicei2c(int fd, char address)
  {
	if (ioctl(fd, I2C_SLAVE, address) < 0)
	{
		printf("Error i2c on slave address\n");
		//exit(1);
	}
  }

void writebytei2c(int fd,char reg, char data)
 {
	char buf[2];
	buf[0] = reg;
	buf[1] = data;
	if ((write(fd,buf,2))!=2) 
	{
		printf("Error i2c send the read command\n");
		//exit(1);
	}
 

}

char readbytei2c(int fd, char reg)
  {
	char buf[1];
	buf[0] = reg;
	if ((write(fd,buf,1))!=1) {
		printf("Error i2c on select the High Byte\n");
		//exit(1);
	}
 
	if ((read(fd,buf,1))!=1) {
		printf("Error i2c on read the  High Byte\n");
		//exit(1);
	}
	return buf[0];
  }



