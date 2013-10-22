/*
 * File: iduec.h
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
#ifndef  _IDUEC_H_
#define _IDUEC_H_

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

#include <termios.h> 
#include "/usr/include/linux/i2c-dev.h"


int openi2c(void);
int closei2c(int fd);
void setdevicei2c(int fd, char address);
void writebytei2c(int fd,char reg, char data);
char readbytei2c(int fd, char reg);


#endif
